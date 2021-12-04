def strToByte(l):
    a = []
    for i in l:
        a.append(i.encode('utf-8'))
    return a


def byteToStr(l):
    a = []
    for i in l:
        a.append(i.decode('utf-8'))
    return a


list1 = ['Blade', '&', 'Soul']
print(f'{list1}={strToByte(list1)}')
list2 = strToByte(list1)
print(f'{list2}={byteToStr(list2)}')
