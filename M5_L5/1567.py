def sms_cost(slogan):

    klaviye = {
        'a': 1, 'b': 2, 'c': 3,
        'd': 1, 'e': 2, 'f': 3,
        'g': 1, 'h': 2, 'i': 3,
        'j': 1, 'k': 2, 'l': 3,
        'm': 1, 'n': 2, 'o': 3,
        'p': 1, 'q': 2, 'r': 3,
        's': 1, 't': 2, 'u': 3,
        'v': 1, 'w': 2, 'x': 3,
        'y': 1, 'z': 2,
        ' ': 1, '.': 1, ',': 2, '!': 3
    }
    

    toplam = sum(klaviye[char] for char in slogan)
    
    return toplam


slogan = input().strip()  
print(sms_cost(slogan))
