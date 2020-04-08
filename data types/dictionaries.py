""" Dictionaries allow us to work with key-value pairs
    you may heard aboout hash-maps or associative arrays
    keys - could be any immutable datatypes
    values - can be anything """

student = {'name':'John', 'age':'25', 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['courses'])

print(student.get('name'))
print(student.get('names'))                 # use get method since it returns None doesn't generates error
print(student.get('names', 'Not Found'))    # specified default return 'Not Found' for the keys doesn't exists


student['phone'] = '555-5555'               # assign new key and value
print(student.get('phone'))
# student['name'] = 'Jane'                    # updated a value
# print(student)

""" or use update method """
student.update({'name': 'Jane', 'age': 26, 'phone':'555-5555'})     # both update and insertion
print(student)

# del student['age']
# print(student)
# age = student.pop('age')                      # popped off and assigned to age
# print(student)
# print(age)

""" How many keyd do we have? -->len """
print(len(student))
print(student.keys())
print(student.values())
print(student.items())                          # both keys and values ---> key-value pairs

for key, value in student.items():
    print(key, value)