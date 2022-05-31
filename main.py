def shifrator(str1, cod1, number1):
    code_1 = list(map(int, cod1))
    lenstr = len(str1)
    lencode = len(cod1)
    if number1 == 1:
        str1 = str1.ljust(lenstr + (lencode - lenstr % lencode) % lencode, "\0")
        lenstr = len(str1)
    count = int(lenstr / lencode)
    x1 = 0
    x2 = lencode
    str2 = ''
    if number1 == 2:
        for i in range(count):
            a = 0
            helpstr1 = list(str1[x1:x2])
            helpstr2 = list(str1[x1:x2])
            for j in cod1:
                helpstr1[j] = helpstr2[a]
                a += 1
            x1 = x2
            x2 = x2 + lencode
            str2 += ''.join(helpstr1)
        while str2[-1] == ' ':
            str2 = str2[:-1]
    else:
        for i in range(count):
            helpstr = str1[x1:x2]
            for j in cod1:
                str2 += str(helpstr[j])
            x1 = x2
            x2 = x2 + lencode
    return str2
def shifrator_1(str1, cod1, number1):
    code_1 = list(map(int, cod1))
    lencode = len(cod1)
    if number1 == 1:
        str1 = str1.split()
        lenstr = len(str1)
        while len(str1) != lenstr + (lencode - lenstr % lencode) % lencode:
            str1.append('\0')
    elif number1 == 2:
        str1 = list(str1.replace('  ', ' ').split(' '))
    lenstr = len(str1)
    count = int(lenstr / lencode)
    x1 = 0
    x2 = lencode
    str2 = []
    str3 = ''
    print(str1)
    if number1 == 2:
        for i in range(count):
            a = 0
            helpstr1 = list(str1[x1:x2])
            helpstr2 = list(str1[x1:x2])
            for j in cod1:
                helpstr1[j] = helpstr2[a]
                a += 1
            x1 = x2
            x2 = x2 + lencode
            str2 += helpstr1
        str3 += ' '.join(str2)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            helpstr = str1[x1:x2]
            for j in cod1:
                str2.append(str(helpstr[j]))
            x1 = x2
            x2 = x2 + lencode
        str3 = ' '.join(str2)
    return str3


def shifrator_2(str1, cod1, number1, lenb1):
    cod1 = list(map(int, cod1))
    lencode = len(cod1)
    lenstr = len(str1)
    count_symbols = (lenb1 - lenstr % lenb1) % lenb1 + ((lencode - lenstr % lencode) % lencode)
    str1 += '\0' * count_symbols
    lenstr = len(str1)
    block = ''
    temporary = lenb1
    str2 = []
    for i in range(lenstr):
        if temporary == 0:
            str2.append(block)
            block = ''
            temporary = lenb1
        block += str1[i]
        temporary -= 1
    str2.append(block)
    lenstr = len(str2)
    count = int(lenstr / lencode)
    x1 = 0
    x2 = lencode
    str3 = ''
    str4 = []
    if number1 == 2:
        for i in range(count):
            a = 0
            helpstr1 = list(str2[x1:x2])
            helpstr2 = list(str2[x1:x2])
            for j in cod1:
                helpstr1[j] = helpstr2[a]
                a += 1
            x1 = x2
            x2 = x2 + lencode
            str4 += helpstr1
        str3 += ''.join(str4)
        while str3[-1] == ' ':
            str3 = str3[:-1]
    else:
        for i in range(count):
            helpstr = str2[x1:x2]
            for j in cod1:
                str3 += str(helpstr[j])
            x1 = x2
            x2 = x2 + lencode
    return str3


def check_code(cod1):
    if len(cod1) == 0:
        print('Вы ничего не ввели.')
        return False
    else:
        try:
            cod1 = list(map(int, cod1))
        except ValueError:
            print('Некорректные данные. Ключ должен состоять из чисел.')
            return False
        maxa = max(cod1)
    if len(set(cod1)) != maxa + 1:
        print('Некорректные данные. В ключе пропущены числа или есть повтор')
        return False
    return True

