# 44. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
# Приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# **Добавьте возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9.

string = '1+23*3-2*4'

def list_from_string(string:str):
    result = []
    temp = 0
    for i in range(0, len(string)):
        if not string[i].isalnum():
            result.append(string[temp:i])
            result.append(string[i])
            temp = i + 1
    result.append(string[temp:])
    print(result)
    return result

def simple_math(operation:list):
    if operation[1] == '/':
        return [str(float(operation[0]) / float(operation[2]))]
    if operation[1] == '*':
        return [str(float(operation[0]) * float(operation[2]))]
    if operation[1] == '+':
        return [str(float(operation[0]) + float(operation[2]))]
    if operation[1] == '-':
        return [str(float(operation[0]) - float(operation[2]))]

def do_math(equation:list):
    while len(equation) != 1:
        for sign in '/*+-':
            while sign in equation:
                idx = equation.index(sign)
                equation = equation[:idx - 1] + simple_math(equation[idx - 1:idx + 2]) + equation[idx + 2:]
    return equation

print(do_math(list_from_string(string)))
