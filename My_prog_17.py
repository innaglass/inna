def parse_int(string):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
             'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
             'one hundred', 'one thousand', 'ten thousand', 'one hundred thousand',
             'one million'] #список цифр словами
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17,
               18, 19, 20, 30, 40, 50, 60, 70,
               80, 90, 100, 1000, 10000,
               100000, 1000000] #список цифр цифрами
    arr_Number = []
    
    #определение, есть ли исходный текст в списке цифр словами целиком
    if string in words:
        Number = numbers[words.index(string)]
        return Number
    
    string_mod = string
    
    while ' ' in string_mod:      
    #получаем последние цифры, проверяем на наличие "-",
    #если есть, добавляем в результирующий массив в виде цифр
        tuple_string = string_mod.rpartition(' ')
        
        if '-' in list(tuple_string)[2]:
            string1 = list(tuple_string[2].rpartition('-'))[2]
            string2 = list(tuple_string[2].rpartition('-'))[0]
            arr_Number.append(str(numbers[words.index(string1)]))
            arr_Number.append(str(numbers[words.index(string2)]))
        elif list(tuple_string)[2] in words:
            arr_Number.append(str(numbers[words.index(list(tuple_string)[2])]))
        string_mod = list(tuple_string)[0]
        
    if '-' not in string_mod:
        arr_Number.append(str(numbers[words.index(string_mod)]))
    else:
        string1 = list(string_mod.rpartition('-'))[2]
        string2 = list(string_mod.rpartition('-'))[0]
        arr_Number.append(str(numbers[words.index(string1)]))
        arr_Number.append(str(numbers[words.index(string2)]))        
    
    arr_Number.reverse()
    
    x1 = []
    for i in arr_Number:
        j = int(i)
        if j % 10 != 0:
            x1.append(j)
        else:
            while j % 10 == 0:
                j = j / 10
            x1.append(int(j))
    x2 = ''
    for i in x1:
        x2 = x2 + str(i)
   

    return int(x2)
# one hundred twenty-three thousand four hundred fifty-six 123456
# one hundred one 101
# two thousand 2000
# thirty-five thousand 35000
# seven hundred thousand 700000
# two hundred thousand three 200003
# two hundred three thousand 203000
# two hundred eighty-two thousand five hundred ten 282510
# five hundred thousand three hundred 500300
