s = input('请输入字符串：')
a = b = c = d = 0
for i in s:
    if str.isalpha(i):
        a += 1
    elif str.isdecimal(i):
        b += 1
    elif str.isspace(i):
        c += 1
    else:
        d += 1

print('''字符的总数为：{}
字母出现的次数为：{}
数字出现的次数为：{}
空格出现的次数为:{}
其他字符出现的次数为：{}'''.format(len(s), a, b, c, d))
