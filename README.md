 def shifrator(number1, str1, key1, ):
    key1 = list(map(int, key1))
    lenkey = len(key1)
    lengthstr = len(str1)

    if number1 == 1:
        str1 = str1.ljust(lengthstr + (lenkey - lengthstr % lenkey) % lenkey, "\0")
        lengthstr = len(str1)
    count = int(lengthstr / lenkey)
    str2 = ''
    x1 = 0
    x2 = lenkey

    if number1 == 2:
        for i in range(count):
            x = 0
            hstr1 = list(str1[x1:x2])
            hstr2 = list(str1[x1:x2])
            for n in key1:
                hstr1[n] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lenkey
            str2 += ''.join(hstr1)
        while str2[-1] == ' ':
            str2 = str2[:-1]
    else:
        for i in range(count):
            hstr = str1[x1:x2]
            for n in key1:
                str2 += str(hstr[n])
            x2 = x2 + lenkey
            x1 = x2

    return str2


def shifrator_1(number1,str1, key1):
    key1 = list(map(int, key1))
    lenkey = len(key1)
    if number1 == 1:
        str1 = str1.split()
        lengthstr = len(str1)
        while len(str1) != lengthstr + (lenkey - lengthstr % lenkey) % lenkey:
            str1.append('\0')
    elif number1 == 2:
        str1 = list(str1.replace('  ', ' ').split(' '))
    lengthstr = len(str1)
    count = int(lengthstr / lenkey)
    x1 = 0
    x2 = lenkey
    str2 = []
    str3 = ''
    print(str1)
    if number1 == 2:
        for i in range(count):
            x = 0
            hstr_1 = list(str1[x1:x2])
            hstr2 = list(str1[x1:x2])
            for n in key1:
                hstr_1[n] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lenkey
            str2 += hstr_1
        str3 += ' '.join(str2)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            hstr = str1[x1:x2]
            for n in key1:
                str2.append(string(hstr[n]))
            x1 = x2
            x2 = x2 + lenkey
        str3 = ' '.join(str2)
    return str3


def shifrator_2(number1,str1, key1, lenu1):
    key1 = list(map(int, key1))
    lenkey = len(key1)
    lengthstr = len(str1)
    count_symbols = (lenu1 - lengthstr % lenu1) % lenu1 + ((lenkey - lengthstr % lenkey) % lenkey)
    str1 += '\0' * count_symbols
    lengthstr = len(str1)
    unit= ''
    interim = lenu1
    str2 = []
    for i in range(lengthstr):
        if interim == 0:
            str2.append(unit)
            unit= ''
            interim = lenu1
        unit += str1[i]
        interim -= 1
    str2.append(unit)
    lengthstr = len(str2)
    count = int(lengthstr / lenkey)
    x1 = 0
    x2 = lenkey
    str3 = ''
    str4 = []
    if number1 == 2:
        for i in range(count):
            x = 0
            hstr1 = list(str2[x1:x2])
            hstr2 = list(str2[x1:x2])
            for n in key1:
                hstr1[n] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lenkey
            str4 += hstr1
        str3 += ''.join(str4)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            hstr = str2[x1:x2]
            for n in key1:
                str3 += string(hstr[n])
            x1 = x2
            x2 = x2 + lenkey
    return str3


def check_cod(key1):
    if len(key1) == 0:
        print('Данные не введены')
        return False
    else:
        try:
            key1 = list(map(int, key1))
        except ValueError:
            print(' Некорректные данные ')
            return False
        maxx = max(key1)
    if len(set(key1)) != maxx + 1:
        print('Некорректные данные (пропущены числа/есть повторяющиеся)')
        return False
    return True


def check_num(number1):
    if len(number1) == 0:
        print('Данные не введены')
        return False
    else:
        try:
            number1 = int(number1)
        except ValueError:
            print('Некорректные данные')
            return False
    if number1 != 0 and number1 != 1 and number1 != 2:
        return False
    return True


def check_string(str1):
    if len(str1) == 0:
        print('Данные не введены')
        return False
    return True


def check_b(b1):
    if len(b1) == 0:
        print('Данные не введены')
        return False
    else:
        try:
            b1 = int(b1)
        except ValueError:
            print('Некорректные данные')
            return False
    if b1 != 1 and b1 != 2 and b1 != 3:
        return False
    return True


def check_lenb(lenu1):
    if len(lenu1) == 0:
        print(' Данные не введены')
        return False
    else:
        try:
            lenu1 = int(lenu1)
        except ValueError:
            print('Некорректные данные')
            return False
    return True


while True:
    print('1 - зашифровать сообщение\n2 - расшифровать сообщение\n0 - выход')
    number = input()
    if check_number(number):
        number = int(number)
        if number == 2 or number == 1:
            string = input('Введите сообщение\n')
            if check_string(string):
                if number == 1:
                    print('Как вы хотите зашифровать сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                else:
                    print('Как было зашифровано сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                b = input()
                if check_b(b):
                    b = int(b)
                    key = input('Введите ключ (каждое число через пробел)\n').split()
                    if check_key(key):
                        if b == 1:
                            print(shifrator(string, key, number))
                        elif b == 2:
                            print(shifrator_1(string, key, number))
                        else:
                            lenu = input('Введите длину блока\n')
                            if check_lenu(lenu):
                                lenu = int(lenu)
                                print(shifrator_2(string, key, number, lenu))
        else:
            excuse()
