# Задание №1
print('Задание №1')
a = [5 , 'a', 10, 7]
a1 = a
a2 = a1
print("Идентификатор 'a': ", {id(a)})
print("Идентификатор 'a1':", {id(a1)})
print("Идентификатор 'a2':" , {id(a2)})


# Задание №2
print( '\nЗадание №2')
a3 = float(5.123)
a4 = int(a3)
print("Идентификатор 'a3':", {id(a3)})
print("Идентификатор 'a4':", {id(a4)})

#Задание №3
print('\nЗадание №3')

a = "Hi, World"
a1 = list(a)
a2 = tuple(a1)
a3 = 10.5
a4 = float(a3)

print(f"Идентификатор 'a', после изменения: ", {id(a)})
print(f"Идентификатор 'a1', после изменения:", {id(a1)})
print(f"Идентификатор 'a2', после изменения:" , {id(a2)})
print(f"Идентификатор 'a3', после изменения:", {id(a3)})
print(f"Идентификатор 'a4', после изменения:", {id(a4)})



# Задание 4
print ('\n Задание №4')

u1 = input("Введите произвольную строку: ")
tu1 = u1.strip()

ec1 = "".join(char for char in tu1 if ord(char) % 2 == 0)
oc1 = "".join(char for char in tu1 if ord(char) % 2 != 0)

print(f'Введенная строка "{tu1}"')
print()
print(f'Переменная с четными символами:     {ec1}')
print(f'Переменная с нечетными символами:  {oc1}')
print("\n!!!" * 3)







