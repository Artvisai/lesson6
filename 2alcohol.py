"""В файл Output.txt выводит максимально возможное число молекул спирта,
которые могут получиться из атомов, представленных во входных данных(Input.txt)"""
f = open('Input.txt', 'r')
a = list(f.read().split())
f.close()
for i in range(len(a)):
    a[i] = int(a[i])
if len(a) == 3:
    c, h, o = a
    f = open('Output.txt', 'w')
    f.write(f'{min(c//2, h//6, o)} molecules')
    f.close()
