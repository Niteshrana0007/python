# print alphabets pattern
lastnumber = 6
asciinumber = 65
for i in range(0,lastnumber):
    for j in range(0,i+1):
        character = chr(asciinumber)
        print(character,end='')
        asciinumber+=1
    print('')


'''
val = 65
for i in range(0, 5):
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val + 1
    print()'''













'''
output:
A
BC
DEF
GHIJ
KLMNO
PQRSTU'''
