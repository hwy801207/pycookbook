filename = 'spam.txt'
flag = filename.endswith('.txt')
print(flag)
flag = filename.startswith('file:')
print(flag)
url = 'http://www.baidu.com'
flag = url.startswith(('http', 'ftp', 'https'))
print(flag)

