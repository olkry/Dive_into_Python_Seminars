# ✔Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔Вместо чисел, кратных пяти — слово «Buzz».
# ✔Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔*Превратите решение в генераторное выражение.

list = []
for i in range(1, 101):
    if i % 3 == i % 5 == 0:
        list.append('FizzBuzz')
    elif i % 3 == 0:
        list.append('Fizz')
    elif i % 5 == 0:
        list.append('Buzz')
    else:
        list.append(i)

print(list)

# OR

output = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)]
print(output)
