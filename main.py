
from random import randint


oracle = 1.8541019663068588 # (((1/7)*3)/1.6180339887)*7
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
while True:
    num_vrai = 0
    total = 0
    print("Question:")
    question = input()
    seed = []
    for char in question:
        try:
            seed_num = str(alphabet[char.lower()]/oracle).replace('.', '')
            if len(seed_num) > 7 :
                seed_num = seed_num[0:7]
            if len(seed_num) == 7:
                seed.append(seed_num)
        except KeyError:
            pass
    if len(seed) == 1:
        break
    tab_bool = []
    add = 0
    for num in seed:
        add += int(num)
    print(add)    
    oracle_int = int(str(oracle).replace('.', ''))
    for z in range(0, int(str(add)[0:6])):
        if randint(1, oracle_int) % 2 == 0:
            tab_bool.append(False)
        else:
            num_vrai += 1
            tab_bool.append(True)
        total += 1

    percent = int(((num_vrai/total))*100)
    print(percent)
    if percent > 59:
        print("Oui")
    elif percent < 41:
        print("Non")
    else:
        print("Peut-être")
    print()


