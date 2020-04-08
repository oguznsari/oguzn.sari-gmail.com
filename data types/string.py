""" If you have a single quote(') in your string use double quotes(") or escape \' and vice versa
    or use three quotes
    Think of a string as a string of individual characters """

message = "Hello World!"
print(message)
print(len(message))
print(message[:5])
print(message[-6:])

print(message.lower())              # lowercase method
print(message.upper())              # uppercase
print(message.count('l'))           # 3
print(message.find('World!'))       # 6 --> start index
print(message.find('Universe'))     # -1 does not contains

message = message.replace('World', 'Universe')
print(message)


# concatenating
greeting = 'Hello'
name = 'Michael'
# message = greeting + ', ' + name + '. Welcome!'
# message = '{}, {}. Welcome!'.format(greeting, name)     # format string
message = f'{greeting}, {name}. Welcome!'            # f string --> easy format string Python 3.6 and higher
print(message)
message = f'{greeting}, {name.upper()}. Welcome!'    # f strings are reaaly useful
print(message)


print(dir(name))            # all of the attributes and methods that we have access to
for utils in dir(name):
    print(utils)


print(help(str))
print(help(str.lower))


# A bit of string formatting
for i in range(1, 11):
    sentence = 'This value is {:03}'.format(i)              # 0 pads all the way up to 3 digits
    print(sentence)

pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)               # 2 decimal places
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)    # comma(,) separated values
print(sentence)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)    # comma(,) separated values and 2 decimal places
print(sentence)

import datetime
my_date = datetime.datetime(1993, 2, 28, 12, 30, 45)
print(my_date)
# February 28th, 1993
sentence = '{:%B %dth, %Y}'.format(my_date)
print(sentence)

# February 28th, 1993 fell on a Sunday and was the 059 day of the year
sentence = '{0:%B %dth, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)