# работа с файлами

# file = open(имя файла, режим доступа к файлу) за открытие файла

# 'r' - read() за чтение файла
# 'w' - write() запись с удалением уже существующих данных
# 'a' - append() запись без удаления уже существующих данных в файле в новой строке
# 'x' - ...() создание файла если его нет
# rb - wb - чтение и запись в бинарном виде

# file = open('text.txt','a')
# text = file.read()
# print(text)
# file.close()

# with open('image.jpg','rb') as file:
#     data = file.read()
# print(data)

# a = input('Введите текст: ')
# with open('text.txt','w') as file:
#     file.write(a)
# print('текст успешно записан')

# with open('text.txt','r') as file:
#     a = file.read()
#     b = len(a.split())
# print(b)

# with open('text.txt','r') as file:
#     a = file.read()
#     c = a.replace(" ", "")
#     b = len(c)
# print(b)

# b  = input('введите слово: ')
# with open('text.txt','r') as file:
#     a = file.read()
#     if b in a:
#         print('есть')
#     else:
#         print('нет')
    
with open('text.txt','r') as file:
    a = file.read()
print(a)
