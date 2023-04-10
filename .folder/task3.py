import random
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

s = int(input("Введите шестизначное число: "))
# s = random.randint(100000, 1000000)

if s >= 100_000 and s < 1_000_000:
    print(f"Ваш билетик {s}")
else:
    print("Вы ввели не шестизначное число")
    quit

half1 = s // 1000
half2 = s % 1000
# print(f"half1 = {half1}")
# print(f"half2 = {half2}")
sum1 = 0
sum2 = 0
for i in range(3):
    sum1 += half1 % 10
    sum2 += half2 % 10
    half1 = half1//10
    half2 = half2//10
# print(f"sum1 = {sum1}")
# print(f"sum2 = {sum2}")

print('Проверка билетика')

if sum1 == sum2:
    print("\033[1m \033[95m Кангратулатион!" +
          '\033[0m \033[94m Боги рандома сжалились над вами \033[0m')
else:
    print("В этот раз не повезло")




# if sum1 == sum2:
#     print("\033[1m \033[95m Кангратулатион!" +
#           '\033[0m \033[94m Боги рандома сжалились над вами \033[0m')
# else:
#     print("В этот раз не повезло")
#     count = 0
#     while sum1 != sum2:
#         count += 1
#         print(f"попытка № {count}")
#         s = random.randint(100_000, 1_000_000)        
#         half1 = s // 1000
#         half2 = s % 1000
#         for i in range(3, 0, -1):
#             sum1 += half1 % 10
#             sum2 += half2 % 10
#             half1 = half1//10
#             half2 = half2//10
#     if sum1 == sum2:
#         print("\033[1m \033[95m Кангратулатион!" +
#               '\033[0m \033[94m Боги рандома сжалились над вами \033[0m')
#         print(
#             f"Вы получили счастливый билетик с \033[91m{count}\033[0m попытки")
