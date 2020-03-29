# File objects
# If you're working with files from different directories -> have to pass the path to that file into open command

# f = open('test.txt', 'r')   # 'r': reading, 'w': write, 'a': append, 'r+' read and write
# print(f.name)
# print(f.mode)
# f.close()                   # have to explicitly close the file if you open like this

# better approach: using context managers
""" Benefit of using context managers is that they allows us to work files within this block 
    and after we exit this block of code, it'll automatically close the file (no to worry for close()
    this will also close the file if there is any exceptions thrown or anything like that) """

with open('test.txt', 'r') as f:
    pass
    # f_contents = f.read()
    # f_contents = f.readlines()

    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:                # 1 line per operation no need to worry about memory
    #     print(line, end='')

    # f_contents = f.read(100)        # 100 characters
    # print(f_contents, end='\n')
    # f_contents = f.read(100)
    # print(f_contents, end='')

    # size_to_read = 20
    # f_contents = f.read(size_to_read)
    # # while len(f_contents) > 0:
    # #     print(f_contents, end='*')
    # #     f_contents = f.read(size_to_read)       # increment operaion
    # #     print(f.tell())
    #
    # print(f_contents, end='')
    # f.seek(0)                                 # to start at the beginning of the file
    # f_contents = f.read(size_to_read)
    # print(f_contents)

# with open('test2.txt', 'w') as f:               # if using a file that already exist be careful
#     f.write('Test')                             # to use 'a' append instead of 'w' write
#     f.write('Test')
#     f.seek(0)
#     f.write('Oguzhan')

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('headshot.jpg', 'rb') as rf:          # 'rb' - read binary ---- not text
#     with open('copy.jpg', 'wb') as wf:          # 'wr' - write binary ---- not text
#         for line in rf:
#             wf.write(line)

with open('headshot.jpg', 'rb') as rf:          # 'rb' - read binary ---- not text
    with open('chunk_copy.jpg', 'wb') as wf:          # 'wr' - write binary ---- not text
        chunk_size = 600
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
