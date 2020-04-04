import os
from datetime import datetime

""" OS module allows us to interact with the underlying operating system in several different ways
    - navigate the file system
    - get file information
    - look-up and change the environment variables
    - can move files around ....etc."""

# print(dir(os))           # when working new modules do this to explore attributes and methods that we've access to
# for each in dir(os):
#     print(each)

# print(os.getcwd())                                  # linux -pwd- equivalent
# os.chdir(r'C:\Users\oguzhan.sari\Desktop')          # change directory
# print(os.getcwd())
# print(os.listdir())                                 # lists files and folders


# os.chdir(r'C:\Python35\python-ml\python\python-cs\os-module')
# os.mkdir('os-module-2')
# os.makedirs(r'os-module-3\dir-1')                           # use while creates a directory that'a few levels deep
# os.makedirs(r'os-module-3\dir-2\dirs-3')                    # so it creates all of the intermediate directories too
# os.mkdir('os-module-1')
# os.rmdir('os-module-2')                                     # doesn't delete intermediate directories
# os.removedirs()                                             # deletes directories recursively - be carefull
# print(os.listdir(r'C:\Python35\python-ml\python\python-cs\os-module'))

# print(os.stat('os-module.py'))
# print(os.stat('os-module.py').st_size)
# print(os.stat('os-module.py').st_mtime)                             # modification time (time-stamp)
# print(datetime.fromtimestamp((os.stat('os-module.py').st_mtime)))   # returned human readable format

# """ entire directory tree and files within Desktop == traverse the director file and print all of the dirs and files """
os.chdir(r'C:\Users\oguzhan.sari\Desktop')
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):           # yields a 3 value tuple
#     print("Current path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
#     print()

# for env in os.environ:
#     print(env)
# print(os.environ.get('USERDNSDOMAIN'))
# print(os.environ.get('USERDOMAIN'))
# print(os.environ.get('USERNAME'))
# print(os.environ.get('USERPROFILE'))
# print(os.environ.get('HOMEPATH'))

# '''use os.path module instead of concatinating paths'''
# file_path = os.path.join(os.environ.get('HOMEPATH'), r'Desktop\test.txt')
# print(file_path)
#
# with open(file_path, 'w') as f:
#     f.writelines(os.environ.get('USERDNSDOMAIN') + '\n')
#     f.writelines(os.environ.get('USERDOMAIN') + '\n')
#     f.writelines(os.environ.get('USERNAME') + '\n')
#     f.writelines(os.environ.get('USERPROFILE') + '\n')
#     f.writelines(os.environ.get('HOMEPATH'))

print(os.path.basename(r'\tmp\test.txt'))
print(os.path.dirname(r'\tmp\test.txt'))
print(os.path.splitext(r'\tmp\test.txt'))               # gives both --> dirname, basename
print(os.path.exists(r'\tmp\test.txt'))
print(os.path.isfile(r'\tmp\test.txt'))
print(os.path.isdir(r'\tmp\test.txt'))
print(os.path.splitext(r'\tmp\test.txt'))
# root of the path, and the extention  --->  much easier than parsing out the extension using string slicing
print(dir(os.path))                         # see whats available in os.path (attributes or methods)