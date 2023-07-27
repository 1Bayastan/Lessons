# Декораторы

# def my_decorator(func):
    # def wrapper():
        # print('до вызова функции')
#         func()
#         print('после вызова функции')
#     return wrapper
# @my_decorator
# def hello():
#     print('привет, это между вызовами')
# hello()        
        
# декоратор с аргументами       

# def in_num(n):
#   def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in renge(n):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator
# @in_num(5)
# def hello(name):
#     print('hello', name)
# hello('tilek')

@classmethod
@property
@staticmethod






