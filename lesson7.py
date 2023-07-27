# # ФУНКЦИИ

# def название функции (аргумент):
#     pass
# блок кода 

# return результат

# def hello (a,b): позиционные аргументы
#     c = a + b
#     # print('hello')
#     return c
# print(hello(1,4))

# def hello (a=2,b=4): 
#     c = a + b
#     print('hello')
#     return c    
# print(hello())

# def hello (*args): переменная которая принимает в себя неограниченное количество позиционных аргументов
#     resul = 0
#     for i in args:
#         resul  += i
#     return resul
# print(hello(1,2,3,4))

# def hello (**kwargs): переменная которая принимает в себя неограниченное количество именованных аргументов 
#     for key , value in kwargs.items():
#         print(key + ':' ,value)
# hello(name = 'Tilek', age = '22', male = 'man')

# a = 'не хелло'
# def hello(): пример глобального и локального кода 
#     a = 'hello'
#     return a
# def ne_hello(a):
#     return a
# print(hello())
# print(ne_hello(a))

# num = lambda x,y : x+y анонимная функция без названия
# print(num(1,3))

# num = lambda n : n % 2 ==0
# print(num(4))

# функция рекурсия (вызов из самой себя)
# def fak (u):
#     if u == 0:
#         return 1
#     else:
#         return fak(u - 1) * u
# print(fak(900))