n = int(input('Введите длину ряда: '))
f1 = f2 = 1
print(f1, f2, end=' ')

i = 2
while i < n:
	f1, f2 = f2, f1 + f2 # f1 приравнивается к f2, f2 приравнивается к f1 + f2
	print(f2, end=' ') # Выводится f2
	i += 1
print()
