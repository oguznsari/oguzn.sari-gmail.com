""" Lists and Tuples allows us to work with sequential data
    sets our unordered collections of values with no duplicates """

courses = ["History", "Math", "Physics", "CompSci"]
print(len(courses))
print(courses[0])      # 1st value at index 0
print(courses[3])
print(courses[-1])     # to get the last item
print(courses[0:2])    # 1sr two (not including index 2)
print(courses[:2])
print(courses[2:])     # the rest -- "slicing"


# courses.append("Art")
# print(courses)

# to include it at specific place(index) use insert
# courses.insert(0, "Art")
# print(courses)

courses_2 = ["Art", "Education"]
# courses.insert(0, courses_2)        # list in list
print(courses)

courses.extend(courses_2)             # extends with each individual items not with the list
print(courses)


courses.remove("Math")
# courses.pop()                         # removes the last item # useful when if we use our list like a stack or a queue
popped = courses.pop()                  # pop returns the value that it removed
print(popped)
print(courses)
""" So if we had a 'stack' or 'queue' we can keep popping off values until list is empty """

courses.insert(1, "Math")
# courses.reverse()
# print(courses)
# courses.sort()                      # sorts in alphabetical order
# print(courses)
nums = [1, 5, 2, 4, 3]
# nums.sort()                         # sorted in ascending order
nums.sort(reverse=True)             # sorted in descending order
print(nums)

print(courses)
sorted_courses = sorted(courses)    # keeps the original list (and get the sorted version without altering itself)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
print('Art' in courses)


for item in courses:
    print(item)

""" but sometimes it might be useful to also have the index of what value we're on """
for index, course in enumerate(courses):
    print(index, course)

# lets turn list[courses] into a string of comma seperated values
courses_str = ", ".join(courses)
print(courses_str)
courses_str = " - ".join(courses) # or with a hyphen
print(courses_str)

#  reverse operation
new_list = courses_str.split(" - ")
print(new_list)


""" Tuples are similar to lists but immutable """
print("Lists")
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'                   # it changes the value at list_1 and list_2 as well
print(list_1)
print(list_2)

print("Tuples")
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'                 # Tuple does not support item assignment --> immtable (no append - no remove etc.)
# print(tuple_1)
# print(tuple_2)


""" Sets are values that are un-ordered and also not have duplicates 
    1st use case - to test whether a value is part of a set   --> membership test(more efficient than lists and tuples)
    2nd use case - to remove duplicate values                 --> because sets throw away duplicates """

print("Sets")
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}                # {curly-braces}
print(cs_courses)                                                     # doesn't prints ordered

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)
print('Math' in cs_courses)                                           # sets are optimised for this


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))                 # common courses
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses))
print(cs_courses.union(art_courses))                        # to combine both of these sets


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}                                              # This isn't right! It's a dict
empty_set = set()                                   # we have to use built-in subclass with no values