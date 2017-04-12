a = input('请输入一个字符串：')
b = input('请输入另一个字符串：')
n = len(b)
i = 0
while i < len(a):
    if a[i:n+i] == b:
        print(i, end=' ')
    i += 1