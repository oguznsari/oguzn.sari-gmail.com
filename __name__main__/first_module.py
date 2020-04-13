""" Whenever Python runs a code it first set a few special variables before even runs any code;
        and __name__ is one of those special variables
    When python runs a python file directly it sets __name__ = __main__
    When we import a file it is going to set __name__ = 'name of the imported file' (first_modeule)
    """

# print(f"First Module's Name: {__name__}")
print("This will always be run")

def main():
    # print("First module's name: {}".format(__name__))
    print(f"First Module's Name: {__name__}")
    print("First modules main method")

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print("Run directly")
else:
    print("Run from import")

""" Use case: There is code that we only want to run either import or directly """