# This is a public items,everyone can hand in your edit!
OperationalSymbol = ["+", "-", "/", "*"]
def main_menu():  #主菜单功能函数
    print("----------Calculator----------")
    print("1.plus\t    [Please enter num'1']\n2.subtraction\t    [Please enter num'2']\n3.multiplication\t    [Please enter num'3']\n4.division\t    [Please enter num'4']\n")
    return eval(input("Please enter you want to Cal："))
def calculator_plus():
    global result_num
    input_objective0 = eval(input("the fir you want input："))
    input_objective1 = eval(input("the sec you want input："))
    result_num = input_objective0 + input_objective1
def calculator_subtraction():
    global result_num
    input_objective0 = eval(input("the fir you want input："))
    input_objective1 = eval(input("the sec you want input："))
    result_num = input_objective0 - input_objective1
def calculator_multiplication():
    global result_num
    input_objective0 = eval(input("the fir you want input："))
    input_objective1 = eval(input("the sec you want input："))
    result_num = input_objective0 * input_objective1
def calculator_division():
    global result_num
    input_objective0 = eval(input("the fir you want input："))
    input_objective1 = eval(input("the sec you want input："))
    result_num = input_objective0 / input_objective1
while True:
    user_choice = main_menu()
    if user_choice == 1:
        calculator_plus()
        print(f"Calculation results:{result_num}")
        input("ENTER TO BACK MAIN")
    elif user_choice == 2:
        calculator_subtraction()
        print(f"Calculation results:{result_num}")
        input("ENTER TO BACK MAIN")
    elif user_choice == 3:
        calculator_multiplication()
        print(f"Calculation results:{result_num}")
        input("ENTER TO BACK MAIN")
    elif user_choice == 4:
        calculator_division()
        print(f"Calculation results:{result_num}")
        input("ENTER TO BACK MAIN")
    elif user_choice == "":
        break


