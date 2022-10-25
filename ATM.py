#authon @nices
money = 5000000
input_action = 0
password_makesure = 0
detect_time = 0
print("欢迎使用鼠鼠银行ATM机")
print("----------登陆菜单----------")
print("如未创建账户请输入数字1，\n如已创建账户可输入任意数字进行账户名登陆即可登陆")
operation_input = int(input("请输入数字以进行所需的下一步操作："))# 全局变量
def account(name, password): #注册功能（密码检测）函数
    while True:
        global password_makesure, detect_time
        length = len(password)
        while length < 6:
            print("密码长度不应小于6个字符")
            password = input("请输入你的密码：")
            length = len(password)
        if length >= 6:
            password_makesure = input("请再次输入密码确定：")
            if password_makesure == password:
                print("注册成功，欢迎使用ATM")
                detect_time = 0
                break
            # else:
            #      print("与第一次输入的密码不相符！请重新输入！")
            #      detect_time = eval(input("如需重新输入账户名及密码请输入数字2\n输入："))
            #      if detect_time == 2:
            #         break
            #      else:
            #         detect_time = 1
            #         continue
def balance():  #余额功能函数
    print("----------查询余额----------")
    print(f"您的余额为{money}元")
    input("按回车以返回主菜单")
def deposit(num):  #存款功能函数
    """
    :param num:存款数额
    :return:总金额
    """
    print("----------存款功能----------")
    global money  #全局金额在函数中的变量
    money = money + num
    print(f"您的存款余额为{money}元")
    input("按回车以返回主菜单")
    return money
def withdraw(num):   #取款功能函数
    """
    :param num:取款金额
    :return: 总金额
    """
    print("----------取款功能----------")
    global money  #全局金额在函数中的变量
    global input_action  #全局操作变量
    if num > money:
        print("操作失败，余额不足！")
        input_action = int(input("输入数字1以继续取款\n或输入任意数字以返回主菜单："))
    else:
        money = money - num
        print(f"您的存款余额为{money}元")
        input("按回车以返回主菜单")
        return money
def re_withdraw(num):  #重新取款功能函数
    """
    :param num:重新输入的取款金额
    :return: 总金额
    """
    global money  #全局金额在函数中的变量
    if num > money:
        print("操作失败，余额不足！")
        input("按回车以返回主菜单!")
    else:
        money = money - num
        print(f"您的存款余额为{money}元")
        input("按回车以返回主菜单")
        return money
def transfer_money(num):  #转账功能函数
    global money
    if num > money:
        print("操作失败，余额不足！")
        input("按回车以返回主菜单!")
    else:
        bank_name = input("请输入转账目标的银行名称:")
        if bank_name != "鼠鼠银行":
            print("无法转账至该账户所在的银行")
            input("按回车以返回主菜单!")
        else:
            money = money - num
            print(f"您的存款余额为{money}元")
            input("按回车以返回主菜单")
            return money
def exchange_rateUSD(num):  #兑换美元功能函数
    """
    :param num:兑换金额
    :return: 总金额
    """
    global money
    money = money + 0.14 * num
    print(f"您的存款余额为{money}元")
    input("按回车以返回主菜单")
    return money

def exchange_rateJPY(num):  #兑换日元功能函数
    """
    :param num: 兑换金额
    :return: 总金额
    """
    global money
    money = money + 20.28 * num
    print(f"您的存款余额为{money}元")
    input("按回车以返回主菜单")
    return money
def main_menu():  #主菜单功能函数
    print("----------ATM主菜单----------")
    print("1.查询功能\t    [请输入数字1]\n2.存款功能\t    [请输入数字2]\n3.取款功能\t    [请输入数字3]\n4.转账功能\t    [请输入数字4]\n5.外币兑人民币存款  [请输入数字5]\n6.离开ATM\t    [请输入数字6]\n")
    return eval(input("请输入您所需要进行的业务："))
while True:
    if operation_input == 1:
        while True:
            if detect_time == 0:
                print("----------新建账户----------")
                name = input("请输入创建的账户名：")
                password = input("请输入你的密码：")
                account(name, password)
                break
            # elif detect_time == 2:
            #     print("----------新建账户----------")
            #     name = input("请输入创建的账户名：")
            #     password = input("请输入你的密码：")
            #     account(name, password)
            #     break
    else:
        name = input("请输入已注册的用户名进行快捷登陆：")
        break
while True:
    print(f"亲爱的{name}，您想办理什么业务？")
    action_input = main_menu()
    if action_input == 1:
        balance()
        continue
    elif action_input == 2:
        num = eval(input("请输入存款数额:"))
        deposit(num)
        continue
    elif action_input == 3:
        num = eval(input("请输入取款数额:"))
        withdraw(num)
        if input_action == 1:
            num = eval(input("请再次输入取款数额:"))
            re_withdraw(num)
        else:
            continue
    elif action_input == 4:
        num = eval(input("请输入转账数额:"))
        transfer_money(num)
        continue
    elif action_input == 5:
        print("1.美元兑人民币\n2.罕见元兑人民币")
        import time
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        str = "当前时间" + time.asctime(t)
        print(str + "\n今日美元汇率0.14\n今日罕见元汇率20.28")
        money_type = eval(input("请输入所需兑换的币种编号："))
        if money_type == 1:
            num = eval(input("请输入兑换数额:"))
            exchange_rateUSD(num)
        elif money_type == 2:
            num = eval(input("请输入兑换数额:"))
            exchange_rateJPY(num)
        continue
    else:
        print("欢迎下次使用ATM")
        input("按回车以退出ATM程序")
        break