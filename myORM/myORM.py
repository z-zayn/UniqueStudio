import pymysql
import re


def stringfield(field_name, size=100, primary_key=False, not_null=False, unique=False, default=None):
    create_sql = 'varchar(%s) ' % size
    if primary_key:
        create_sql += "primary key "
    if not_null:
        create_sql += "not null "
    if unique:
        create_sql += "unique "
    if default:
        create_sql += """default '%s' """ % default
    return field_name, create_sql


def intfield(field_name, primary_key=False, not_null=False, unique=False, default=None):
    create_sql = 'int '
    if primary_key:
        create_sql += "primary key "
    if not_null:
        create_sql += "not null "
    if unique:
        create_sql += "unique "
    if default:
        create_sql += "default %s " % default
    return field_name, create_sql


def bigintfield(field_name, primary_key=False, not_null=False, unique=False, default=None):
    create_sql = 'bigint '
    if primary_key:
        create_sql += "primary key "
    if not_null:
        create_sql += "not null"
    if unique:
        create_sql += "unique "
    if default:
        create_sql += "default %s " % default
    return field_name, create_sql


def creat_connect():
    _conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="testORM",
        charset="utf8",
    )
    _cursor = _conn.cursor()
    return _conn, _cursor


def create_tables(sql):
    _conn, _cursor = creat_connect()
    _cursor.execute(sql)
    _cursor.close()
    _conn.close()


def select(sql, size=None):
    _conn, _cursor = creat_connect()
    _cursor.execute(sql)
    if size:
        rs = _cursor.fetchmany(size)
    else:
        rs = _cursor.fetchall()
    _cursor.close()
    _conn.close()
    return rs


def execute(sql):
    _conn, _cursor = creat_connect()
    row = 0
    try:
        row = _cursor.execute(sql)
        _conn.commit()
    except Exception as result:
        print(result)

    print("%d rows affected\n" % row)
    _cursor.close()
    _conn.close()
    return row


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Model类不需要进行映射
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        defaults = dict()
        primary_key = None
        creat_table = "create table `%s`(" % name

        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的属性
            if isinstance(v, tuple):
                mappings[k] = v
                creat_table += (v[0] + ' ' + v[1] + ',')
                if "primary key" in v[1]:
                    # 找到主键
                    primary_key = v[0]  # 直接指定成主键的字段名而非属性名
                if "default" in v[1]:
                    # 记录下带有default约束的字段名和默认的值
                    default = re.findall(r".*default\s*(\S*)\s*", v[1])[0]
                    defaults[v[0]] = default

        creat_table = creat_table[:-1:]
        creat_table += ");"
        # 主键必须要有
        if not primary_key:
            raise SystemError('Primary key not found')

        # 删除已经保存好的类属性，避免之后与实例属性混淆
        for k in mappings.keys():
            attrs.pop(k)

        # 添加上新的类属性
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name   # 表名和类名一致
        attrs['__create_table__'] = creat_table     # 创建该表的sql语句
        attrs['__primary_key__'] = primary_key  # 记录主键的字段名
        attrs['__primary_key_list__'] = list()  # 记录主键
        attrs['__defaults__'] = defaults        # 记录default约束字段和默认值
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # self.name = value
            setattr(self, name, value)

    @classmethod
    def create_table(cls):
        try:
            print("SQL: %s" % cls.__create_table__)
            create_tables(cls.__create_table__)
        except Exception as result:
            print(result)
            print("")

    def insert(self):
        fields = list()
        args = list()
        for k, v in self.__mappings__.items():
            if v[0] == self.__primary_key__:
                # 如果是主键
                self.__primary_key_list__.append(getattr(self, k, None))
            if getattr(self, k, None) is None:
                if v[0] not in self.__defaults__:
                    # 表示没有设置默认值
                    continue
                # 需要用到默认值
                args.append(self.__defaults__[v[0]])
            else:
                args.append(getattr(self, k, None))
            fields.append(v[0])

        args_temp = list()
        for temp in args:
            # 判断如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s);' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print("SQL: %s" % sql)
        execute(sql)

    def delete(self, *where):
        """通过主键删除"""
        # 完成批量删除的sql语句部分
        where_sql = ''
        for single in where:
            where_sql += (str(single) + ",")
        where_sql = where_sql[:-1:]
        sql = 'delete from %s where %s in (%s);' % (self.__table__, self.__primary_key__, where_sql)
        print("SQL: %s" % sql)
        execute(sql)

    def update(self, fields, values, where):
        """通过主键更新数据"""
        # 完成多字段同时更新的sql语句部分
        set_sql = ''
        for field, value in zip(fields, values):
            if isinstance(value, str):
                value = """'%s'""" % value
            set_sql += "%s=%s," % (field, value)

        set_sql = set_sql[:-1:]

        sql = 'update %s set %s where %s=%s;' % (self.__table__, set_sql, self.__primary_key__, where)
        print("SQL: %s" % sql)
        if where not in self.__primary_key_list__:
            print("Failed to update:NO %s=%s" % (self.__primary_key__, where))
        execute(sql)

    @classmethod
    def findall(cls, where, *args):
        """通过主键查询"""
        # 记录要查询的字段名
        fields_sql = ''
        size = None
        # 完成批量查询的sql语句
        where_sql = ''
        if len(where) == 0:
            # 表示不指定查询特定的主键
            where_sql = ''
        else:
            where_sql += "where %s in (" % cls.__primary_key__
            for single in where:
                where_sql += (str(single) + ',')
            where_sql = where_sql[:-1:]
            where_sql += ')'
        if len(args) == 0:
            # 默认查询所有字段
            fields_sql = '*'
        else:
            for field in args:
                if isinstance(field, int):
                    # 如果field时int类型，就是指定查询信息条数
                    size = field
                else:
                    fields_sql += (field + ',')
            fields_sql = fields_sql[:-1:]

        sql = 'select %s from %s %s;' % (fields_sql, cls.__table__, where_sql)
        print("SQL: %s" % sql)
        rs = select(sql, size)
        if len(rs) == 0:
            return None
        else:
            for temp in rs:
                print(temp)
            print("")

    @classmethod
    def findone(cls, where=None, *args):
        """通过主键查询"""
        # 记录要查询的字段名
        fields_sql = ''
        size = 1
        if len(args) == 0:
            # 默认查询所有字段
            fields_sql = '*'
        else:
            for field in args:
                fields_sql += (field + ',')
            fields_sql = fields_sql[:-1:]

        sql = 'select %s from %s where %s=%s;' % (fields_sql, cls.__table__, cls.__primary_key__, where)
        print("SQL: %s" % sql)
        rs = select(sql, size)
        if len(rs) == 0:
            print("None")
        else:
            for temp in rs:
                print(temp)
            print("")




