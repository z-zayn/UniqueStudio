from myORM import *


class User(Model):
    uid = intfield("uid", primary_key=True)
    username = stringfield("username", not_null=True, unique=True)
    email = stringfield("email", unique=True)
    password = stringfield("password", not_null=True, default="12345678")
    # 指定元类之后，以上类属性将不再存在，而是在__mappings__属性指向的字典中保存有相关信息
    # 以上User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int primary key"),
    #     "name": ('username', "varchar(30)"),
    #     "email": ('email', "varchar(30)"),
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"
    # __primary_key__ = "uid"
    # __create_table__ = "......"
    # __primary_key_list_ = [......]
    # __defaults__= {..:..,......}


def main():
    User.create_table()
    u = User(uid=1, username="111", email="111@xxx.com", password="123456")
    u.create_table()
    u.insert()
    u = User(uid=2, username="222", email="222@xxx.com", password="123456")
    u.insert()
    u = User(uid=3, username="333", email="333@xxx.com", password="123456")
    u.insert()
    u = User(uid=4, username="444", email="444@xxx.com", password="123456")
    u.insert()
    u = User(uid=5, username="555", email="555@xxx.com", password="123456")
    u.insert()
    u = User(uid=6, username="666", email="666@xxx.com", password="123456")
    u.insert()
    u = User(uid=7, username="777", email="777@xxx.com", password="123456")
    u.insert()
    u = User(uid=8, email="888@xxx.com", password="123456")
    u.insert()
    u = User(uid=9, username="999", email="999@xxx.com")
    u.insert()
    u = User(uid=10, username="x", email="111@xxx.com")
    u.insert()
    u.delete(1, 2, 3)
    u.update(["username", "email", "password"], ["laowang", "laowang@xxx.com", "gebilaowang"], 6)
    u.update(["username"], ["hhh"], 11)

    u.findall([], "uid", "username", "email", 2)
    u.findall([4, 5, 6])
    u.findone(7)
    u.findone(7, "username", "uid")


if __name__ == '__main__':
    main()
