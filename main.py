def shifrator( str1,cod1, number1):
    cod1 = list(map(int, cod1))
    lengthstr = len(str1)
    lengthcode = len(cod1)
    if number1 == 1:
        str1 = str1.ljust(lengthstr + (lengthcode - lengthstr % lengthcode) % lengthcode, "\0")
        lengthstr = len(str1)
    count = int(lengthstr / lengthcode)
    x1 = 0
    x2 = lengthcode
    str2 = ''
    if number1 == 2:
        for i in range(count):
            x = 0
            hstr1 = list(str1[x1:x2])
            hstr2 = list(str1[x1:x2])
            for n in cod1:
                hstr1[n] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lengthcode
            str2 += ''.join(hstr1)
        while str2[-1] == ' ':
            str2 = str2[:-1]
    else:
        for i in range(count):
            hstr = str1[x1:x2]
            for n in cod1:
                str2 += str(hstr[n])
            x1 = x2
            x2 = x2 + lengthcode
    return str2


def shifrator_1(str1, cod1, number1):
    cod1 = list(map(int, cod1))
    lengthcode = len(cod1)
    if number1 == 1:
        str1 = str1.split()
        lengthstr = len(str1)
        while len(str1) != lengthstr + (lengthcode - lengthstr % lengthcode) % lengthcode:
            str1.append('\0')
    elif number1 == 2:
        str1 = list(str1.replace('  ', ' ').split(' '))
    lengthstr = len(str1)
    count = int(lengthstr / lengthcode)
    x1 = 0
    x2 = lengthcode
    str2 = []
    str3 = ''
    print(str1)
    if number1 == 2:
        for i in range(count):
            x = 0
            hstr_1 = list(str1[x1:x2])
            hstr2 = list(str1[x1:x2])
            for j in cod1:
                hstr_1[j] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lengthcode
            str2 += hstr_1
        str3 += ' '.join(str2)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            hstr = str1[x1:x2]
            for j in cod1:
                str2.append(string(hstr[j]))
            x1 = x2
            x2 = x2 + lengthcode
        str3 = ' '.join(str2)
    return str3


def shifrator_2(str1, cod1, number1, lenu1):
    cod1 = list(map(int, cod1))
    lengthcode = len(cod1)
    lengthstr = len(str1)
    count_symbols = (lenu1 - lengthstr % lenu1) % lenu1 + ((lengthcode - lengthstr % lengthcode) % lengthcode)
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
    count = int(lengthstr / lengthcode)
    x1 = 0
    x2 = lengthcode
    str3 = ''
    str4 = []
    if number1 == 2:
        for i in range(count):
            x = 0
            hstr1 = list(str2[x1:x2])
            hstr2 = list(str2[x1:x2])
            for j in cod1:
                hstr1[j] = hstr2[x]
                x += 1
            x1 = x2
            x2 = x2 + lengthcode
            str4 += hstr1
        str3 += ''.join(str4)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            hstr = str2[x1:x2]
            for j in cod1:
                str3 += string(hstr[j])
            x1 = x2
            x2 = x2 + lengthcode
    return str3


def check_cod(cod1):
    if len(cod1) == 0:
        print('Вы ничего не ввели')
        return False
    else:
        try:
            cod1 = list(map(int, cod1))
        except ValueError:
            print('Некорректные данные')
            return False
        maxx = max(cod1)
    if len(set(cod1)) != maxx + 1:
        print('Некорректные данные (пропущены числа/есть повторяющиеся)')
        return False
    return True


def check_num(number1):
    if len(number1) == 0:
        print('Вы ничего не ввели.')
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
        print('Вы ничего не ввели.')
        return False
    return True


def check_b(b1):
    if len(b1) == 0:
        print('Вы ничего не ввели.')
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
        print(' Ничего не введено.')
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
    if check_num(number):
        number = int(number)
        if number == 1 or number == 2:
            string = input('Введите сообщение\n')
            if check_string(string):
                if number == 1:
                    print('Как вы хотите зашифровать сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                else:
                    print('Как было зашифровано сообщение?\n1 - посимвольно \n2 - по словам \n3 - по блокам')
                b = input()
                if check_b(b):
                    b = int(b)
                    cod = input('Введите ключ (каждое число через пробел)\n').split()
                    if check_cod(cod):
                        if b == 1:
                            print(shifrator(string, cod, number))
                        elif b == 2:
                            print(shifrator_1(string, cod, number))
                        else:
                            lenu = input('Введите длину блока\n')
                            if check_lenb(lenu):
                                lenu = int(lenu)
                                print(shifrator_2(string, cod, number, lenu))
        else:
            exit()