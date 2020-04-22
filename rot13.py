print('ROT13 converter')
while True:
    a=input('Enter: ')
    if a==' ':
        break
    elif a=='h':
        print('|-------------------------|')
        print('|A|B|C|D|E|F|G|H|I|J|K|L|M|')
        print('|-------------------------|')
        print('|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|')
        print('|-------------------------|')
        print()
        print('1. Na - Sodium')
        print('2. Bore - "Bo" and "Re"')
        print('3. PC/CP - Personal Computer and you know it')
        print('4. Qd - Quad/Quadrilateral')
        print('5. SF - SourceForge/Science Fiction')
        print('6. GT - GTA/GT Racing')
        print('7. HU - Happy Unhappy/Unhealthy')
        print('8. VI - VI/VIM')
        print('9. JW - John Wick')
        print('10. XK - XKeyScore')
        print('11. LY - LaZy')
        print('12. MZ - MaZe')
        continue
    for i in a:
        c=ord(i)
        if ord(i)>64 and ord(i)<91:
            if ord(i)>64 and ord(i)<78:
                c=ord(i)+13
            elif ord(i)>77 and ord(i)<91:
                c=ord(i)-13
        elif ord(i)>96 and ord(i)<123:
            if ord(i)>96 and ord(i)<110:
                c=ord(i)+13
            elif ord(i)>109 and ord(i)<123:
                c=ord(i)-13
        print(chr(c), end='')
    print()
