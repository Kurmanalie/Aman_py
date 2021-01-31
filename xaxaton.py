# prodoljit = 'y'
# while prodoljit == 'y':
#     f_num = int(input("Введите число: "))
#     oper = input("Введите операцию: ")
#     s_num = int(input("Введите второе число:"))
#     if oper == '+':
#         print (f_num + s_num)
#     elif oper == '-':
#         print (f_num - s_num)
#     elif oper== '*' :
#         print(f_num * s_num)
#     elif oper =='/': 
#         print (f_num / s_num)
#     else :
#         print ('Error')
#     prodoljit = input("Введите 'y', чтобы продолжить, или любую клавищу, чтобы заверщить>>")


# a1= int(input("Введите число a:"))
# b1= int(input("Введите число b:"))
# c1= int(input("Введите число c:"))

# a= a1+b1
# b= c1-a1
# c= a1+b1+c1

# print('Второе значение=', a)
# print('Второе значение=', b)
# print('Второе значение=', c)

# a = int(input("введите сторону квадрата: "))
# P = 4 * a
# S = a * a
# print("Периметр квадрата: ", P)
# print ("Площадь квадрата: ", S)


# n = int(input("Введите четырехзначное число: " ))
# a = n // 1000
# b =    (n // 100)%10
# c = (n//10)%10
# d = n%10
# v = [a,b,c,d]

# c = list(reversed(sorted(v)))
# if v == c:
#     print("да, число по убыванию")
# else:
#     print("нет, не по убыванию")

# import sys
# sequence_0 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0)
# sequence_1 = (14,10,35,45,60,70,90,0,105,150,70)
# sequence_2 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0.0)
# sequence_3 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70)


# a = sorted(sequence_0)
# for i in range(int(len(sequence_0))-1):
#     if a[i]==a[i+1]:
#         print("Posledovatelnost' ne unikalna")
#         break
#     else:
#         if (i+1) != int(len(sequence_0)-1):
#             pass
#         else:
#             print("Posledovatelnost' unikalna")
    

# a = sorted(sequence_1)
# for i in range(int(len(sequence_1))-1):
#     if a[i]==a[i+1]:
#         print("Posledovatelnost' ne unikalna")
#         break
#     else:
#         if (i+1) != int(len(sequence_1)-1):
#             pass
#         else:
#             print("Posledovatelnost' unikalna")

# a = sorted(sequence_2)
# for i in range(int(len(sequence_2))-1):
#     if a[i]==a[i+1]:
#         print("Posledovatelnost' ne unikalna")
#         break
#     else:
#         if (i+1) != int(len(sequence_2)-1):
#             pass
#         else:
#             print("Posledovatelnost' unikalna")

# a = sorted(sequence_3)
# for i in range(int(len(sequence_3))-1):
#     if a[i]==a[i+1]:
#         print("Posledovatelnost' ne unikalna")
#         break
#     else:
#         if (i+1) != int(len(sequence_3)-1):
#             pass
#         else:
#             print("Posledovatelnost'  unikalna")

import sys
def dodo():
    a = input("Kak rab f rev: ")
    a = a.split(' ')
    v = ''.join(reversed(a[0]))
    print(v)

try:
    dodo()
        
except SyntaxError:
    dodo()