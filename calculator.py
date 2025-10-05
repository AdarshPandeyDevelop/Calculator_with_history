History_File = "history.txt"


def show_history():
    file = open(History_File, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()


def clear_history():
    file = open(History_File, 'w')
    file.close()
    print('History cleared')


def save_to_history(equation, result):
    file = open(History_File, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()


def calculator(user_input):
    # parts = user_input.split()
    # if len(parts) != 3:
    #     print('Invalid input. Use format: number operator number (e.g 8 + 8)')
    #     return

    # num1 = float(parts[0])
    # op = parts[1]
    # num2 = float(parts[2])

    # Remove spaces
    user_input = user_input.replace(" ", "")

    # Find the operator
    for op in "+-*/":
        if op in user_input:
            num1, num2 = user_input.split(op)
            num1 = float(num1)
            num2 = float(num2)
            break
    else:
        print("Invalid input. Use format: number operator number (e.g 8+8 or 8 + 8)")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You cannot divide any number by Zero (0)")
            return
        result = num1 / num2
    else:
        print('Invalid operator. USE ONLY + - * /')
        return

    if int(result) == result:
        result = int(result)
    print('Result:', result)
    save_to_history(user_input, result)


def main():
    print("----SIMPLE CALCULATOR (type history, clear, exit)----")
    while True:
        user_input = input(
            "Enter calculation (+ - * /) or commmand (history, clear, exit) = ")
        if user_input == 'exit':
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculator(user_input)


main()
