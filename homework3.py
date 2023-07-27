# a =int(input('введите число: '))
# if a%5==0:
#     print(f'{a} кратно 5')
# else:
#     print(f'{a} не кратно 5')

# a = int(input('введите который час: '))
# if 5 <= a <= 11:
#     print('доброе утро')
# elif 12 <= a <= 16:
#     print('добрый день')
# elif 17 <= a <= 21:
#     print('добрый вечер')
# elif 22 <= a <= 24 or 1 <= a <=4:
#     print('спокойной ночи')
# else:
#     print('не на той планете живешь')

# a = input('введите три числа через пробел: ').split()
# b = max(a)
# print(f'наибольше число это {b}')

# a = int(input('введите положительное число: '))
# b = 0
# sum = 0
# if a > 0:
#     while b <= a:
#         sum += b
#         b +=1
#     print(f'сумма чисел от 1 до {a} равна {sum}')
# else:
#     print('написано же положительное!!!!!!!')

# with open('text.txt','r') as file:
#     a = file.read()
#     b = a.split()
#     for i in b:
#         c = [int(i)]
#     average = sum(c) // len(c)
#     print(average)

# a = input('введите список слов: ')
# with open ('text.txt','w') as file:
#     file.write(a)
#     print('текст успешно записан')

# import copy
# with open('file1.txt','r') as file:
#     c = file.read()
#     d = copy.copy(c)
# with open('file2.txt','r') as file:
#     a = file.read()
#     b = copy.copy(a)
# with open('merged.txt','w') as file:
#     f = file.write(d)
#     e = file.write(b)
#     print('текст успешно записан')
    
# a = int(input('введите высоту треугольника: '))
# b = 0
# for i in range (1,a+1):
#     print('*'*i)

# old_word = input('введите слово которое заменить: ')
# new_word = input('введите слово на которое заменить: ')
# with open('text.txt','r') as file:
#     a = file.read()
# b = a.replace(old_word,new_word)
# with open('text.txt','w') as file:
#     a = file.write(b)
# print(f'слово {old_word} было заменено на слово {new_word }')
