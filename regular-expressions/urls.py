import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?')
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')                  # 3 groups

matches = pattern.finditer(urls)

# for match in matches:
    # print(match)
    # print(match.group(1))
    # print(match.group(2))
    # print(match.group(3))

subbed_urls = pattern.sub(r'\2\3', urls)                    # \{1,3} back references to groups
print(subbed_urls)