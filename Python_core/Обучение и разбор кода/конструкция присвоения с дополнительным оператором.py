print("Использование сложения и вычитания: конструкция присвоения с дополнительным оператором")

a = 30
b = 50

# b = b + 1
b += 1
print('b =', b)

# a = a + b
a += b
print('a =', a)

# a = a + 100
a += 100
print('a =', a)

# b = b - a
b -= a
print('b =', b)

# a = a - 80
a -= 80
print('a =', a)

print('умножения и деления')

a = 3

# a = a * 10
a *= 10
print('a =', a)

b = 5
# a = a * b
a *= b
print('a =', a)

# a = a / b
a /= b
print('a =', a)

print(' Оставшиеся операции ')

a = 3
# a = a ** 4
a **= 4
print('a =', a)
b = 10
  
# a = a % b
a %= b
print('a =', a)


# b = b // 4
b //= 4
  
print('b =', b)