""" Integers --> whole numbers
    Float    --> decimal """

num = 3
print(type(num))
num = 3.14
print(type(num))

print(3 / 2)
print(3 // 2)           # floor division = 1
print(3 ** 2)           # exponent - power
print(3 % 2)            # modulus - remainder after division

# order of operation
print(3 * 2 + 1)
print(3 * (2 + 1))

# incrementing
num = 1
num += 1
num *= 5
print(num)


print(abs(-3))          # absolute value
print(round(3.76))      # rounds to nearest integer
print(round(3.75, 1))   # round to the first digit after the decimal --> 3.8


# comparison    --> returns boolean --> T or F
num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_1)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# if we got these numbers from somewhere and their type is string ---> + will concatenate
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)
#  to fix this issue we should use casting
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)         # addition