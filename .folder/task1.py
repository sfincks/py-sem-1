# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Ввод число с приглажением
a = int(input('Введите 3-х значное число: '))
# Проверка введенного числа
if a >= 100 and a < 1000:
    print(a)
else:
    print('Вы ввели не 3-х значное число')
    quit()
# Нахождение суммы цифр 3-х значного числа
sum = 0
for i in range(3):
    sum += a % 10
    a = a//10
    # print(f"sum = {sum}")
    # print(f"a = {a}")
print(int(sum))
