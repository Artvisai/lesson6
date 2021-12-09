def strToByte(l):
    """Функция преобразующая список строк в список байт кодов."""
    a = []
    for i in l:
        a.append(i.encode('utf-8'))
    return a


def byteToStr(l):
    """Функция преобразующая список байт кодов в список строк."""
    a = []
    for i in l:
        a.append(i.decode('utf-8'))
    return a


"""Проверка"""
list1 = ['Blade', '&', 'Soul']
print(f'{list1}={strToByte(list1)}')
list2 = strToByte(list1)
print(f'{list2}={byteToStr(list2)}')
