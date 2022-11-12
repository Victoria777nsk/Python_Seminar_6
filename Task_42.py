# 42. Есть список чисел. Вывести – является ли последовательность строго убывающей, или строго возрастающей, или ни то, ни другое.

def Numbers(my_list):
    counterVozr = 0
    counterUbyv = 0
    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i + 1]:
            counterVozr += 1
        elif my_list[i] > my_list[i + 1]:
            counterUbyv += 1
        else:
            print("Последовательность не является ни строго возрастающей, ни строго убывающей")
            break
    if counterUbyv == len(my_list) - 1:
        print("Последовательность является строго убывающей")
    elif counterVozr == len(my_list) - 1:
        print("Последовательность является строго возрастающей")

my_list = [1, 2, 3, 4, 5]
print(my_list)
Numbers(my_list)

my_list1 = [5, 4, 3, 2, 1]
print(my_list1)
Numbers(my_list1)

my_list2 = [1, 5, 4, 3, 2]
print(my_list2)
Numbers(my_list2)