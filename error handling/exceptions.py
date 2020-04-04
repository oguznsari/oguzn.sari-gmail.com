""" Handling errors and exceptions in Python """

# f = open('testfile.txt')
try:
    # f = open('testfile.txt')
    f = open('test_file.txt')
    f = open("corrupt_file.txt")
    # if f.name == "corrupt_file.txt":
    #     raise Exception
    # var = bad_var                                   # so we should be more precise
# except Exception:
# except FileNotFoundError:
#     print('Sorry, this file does not exist')        # custom error for users rather than verbose Phyton error
# except Exception:                        # use more specific exceptions at the top and the general ones at the bottom
#     print('Sorry, something went wrong')

except FileNotFoundError as e:                        # instead of custom messages print exception that we hit
    print(e)
except Exception as e:
    # print(e)
    print('Error!')                                   # for raising manual Exception

else:                                      # runs code needs to be executed if try Clause doesn't raise an Exception
    print(f.read())
    f.close()

finally:                # runs code needs to be run no matter what happens(either throwing Exception or Successful case)
    print("Execution Finally....")                    # for example: closing down the databse
                                        # something that need to be done regardless if the code is successful or not


