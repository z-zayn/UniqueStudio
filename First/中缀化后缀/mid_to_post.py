def solution(mid_str):

    pri = dict()  # 定义一个字典，保存优先级
    pri["*"] = 2
    pri["/"] = 2
    pri["+"] = 1
    pri["-"] = 1
    stack = list()  # 栈是用来存运算符
    post_list = []  # 保存要输出的后缀表达式
    mid_list = list(mid_str[::])  # 把中缀表达式转换成列表

    for i in mid_list:
        if i in "0123456789":
            # 如果是数字,直接保存进后缀表达式中
            post_list.append(i)
        else:  # 如果是运算符，当栈不为空并且栈顶元素的等级比当前运算符的等级高时，栈顶元素加入到后缀列表中
            while len(stack) and pri[stack[len(stack)-1]] >= pri[i]:
                post_list.append(stack.pop())
            stack.append(i)  # 把当前运算符压入栈

    while len(stack):  # 当栈中不为空时，依次弹出栈中的元素，加到后缀列表后面
        post_list.append(stack.pop())
    return ''.join(post_list)


def main():
    print(solution("1*2+6*8"))
    print(solution("1+5+9*9*5+6/9"))


if __name__ == '__main__':
    main()
