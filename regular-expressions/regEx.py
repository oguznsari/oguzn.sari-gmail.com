""" We will use built-in 're' module for RegEx - regular expressions
    RegEx = search for and match specific patterns of text
    extremely useful for parsing information from our data"""
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''


# print("\tTab")
# print(r"\tTab")         # raw string

# re.compile() -- method will allow us to separate our patterns into a variable
# pattern = re.compile(r'abc')
# pattern = re.compile(r'.')                          # special character
# pattern = re.compile(r'\.')                         # needs to be \escaped
# pattern = re.compile(r'coreyms\.com')

# pattern = re.compile(r'.')                          # any char except new line
# pattern = re.compile(r'\d')                         # digit (0-9)
# pattern = re.compile(r'\D')                         # not a digit, everything except digit
# pattern = re.compile(r'\w')                         # word char (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\W')                         # not a word char
# pattern = re.compile(r'\s')                         # Whitespace (space, tab, newline)
# pattern = re.compile(r'\S')                         # Not Whitespace (space, tab, newline)

# Anchors - don't matches characters rather they matches invisible positions before and after characters
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text_to_search)

# pattern = re.compile(r'^Start')
# pattern = re.compile(r'^a')                         # doesn't works because string starts with Start
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)

""" we can't do literal search for numbers because they are all different they have 
a similar pattern but nat all the same digits ----> so we'll use meta characters instead of literal characters"""

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(text_to_search)


# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# with open('regEx/data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

# pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')    # [character set: either . or -]
# matches = pattern.finditer(text_to_search)          # no need to escape . within char set

# pattern = re.compile(r'[98]00[.-]\d{3}[.-]\d{4}')     # 800 and 900
# # matches = pattern.finditer(text_to_search)
# with open('regEx/data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

# pattern = re.compile(r'[1-5]')                          # [12345] -- range
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[a-zA-Z]')                       # lowercase or uppercase
# pattern = re.compile(r'[^a-zA-Z]')                      # carot(^) - not a lowercase or uppercase
# pattern = re.compile(r'[^b]at')

pattern = re.compile(r'Mr\.')
pattern = re.compile(r'Mr\.?')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')          # (group)
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')        # (group)


# matches = pattern.finditer(text_to_search)
matches = pattern.findall(text_to_search)           # only 1st group
# if there were multiple groups then it would return a list of tuples
# and the tuples would contain all of the groups

# for match in matches:
#     print(match)                                # span=(1, 4), match='abc'
# print(text_to_search[1:4])                      # we can reach it by using string slicing functionality

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'Start')
pattern = re.compile(r'sentence')                   # none  # match
pattern = re.compile(r'dne')                        # none  # sentence
pattern = re.compile(r'start', re.IGNORECASE)       # IGNORECASE flag
pattern = re.compile(r'start', re.I)                # """""""""" flag - I is enough

# multi-lane flag ---> that allows us to use the ^ and $ to match the beginning and end of each line
#                       rather than just the beginning or end of that string

# verbose flag ---> allows to add whitespace and comments directly within pattern
#                     which could help break-up complicated patterns into easy to understand segments
#       This flag also lets you put comments within a RE that will be ignored by the engine; comments are
#       marked by a '#' that’s neither in a character class or preceded by an unescaped backslash.

charref = re.compile(r"""
    &[#]                    # start of a numeric entity reference
    (
        0[0-7]+             # octal form
      | [0-9]+              # decimal form
      | x[0-9a-fA-F]+       # hexadecimal form
      )
      ;                     # trailing semicolon
    """, re.VERBOSE)
charr= "&#1502;&#1508;&#1490;&#1513;&#1497;&#223;&#xDF;"
# charr= "&#223;"
# charr= "&#xDF;"

matches = pattern.match(sentence)                   # only matches at the beginning of the string
matches = pattern.search(sentence)                  # searches entire string
matches = charref.finditer(charr)

for m in matches:
    print(m)
    "from here print chars corresponding to those char refs"


# matches = charref.findall(charr)
# print(matches)

""" Common theme with special characters: 
    Capital letters negate whatever the lowercase version """