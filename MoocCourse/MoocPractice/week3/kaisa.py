while True:
    z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = input()
    for i in x:
        if i.upper() != i:
            print(z[(z.index(i.upper()) + 3) % 26].lower(), end='')
        elif i not in z:
            print(i, end='')
            continue
        elif i.upper()==i:
            print(z[(z.index(i)+3) % 26],end = '')

