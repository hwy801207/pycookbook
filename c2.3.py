from fnmatch import fnmatch, fnmatchcase , filter

ret = filter(['a.txt', 'b.txt', 'x.exe'], '*.txt')
print(ret)
