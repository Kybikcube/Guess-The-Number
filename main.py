import random

num = random.randint(1, 100)

while True:
    num_input = int(input("Введите число от 1 до 100: "))
    if num_input == num:
        print("Вы угадали! Число было", num)
        break
    elif num_input < num:
        print("Больше")
    elif num_input > num:
        print("Меньше")