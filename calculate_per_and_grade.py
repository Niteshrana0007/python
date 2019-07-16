maths = int(input('enter the markas of maths: '))
phy = int(input('enter the markas of physics: '))
chem = int(input('enter the markas of chemistry: '))
bio = int(input('enter the markas of bio: '))
m = int(input('enter the markas of computer: '))

per = (maths+phy+chem+bio+m)/5
print('percentage: ',per)
if per>=90 :
    print('A')
elif per<90 and per>=80 :
    print('B')
elif per<80 and per>=70 :
    print('C')
elif per<70 and per>=60 :
    print('D')
elif per<60 and per>=50 :
    print('E')
else:
    print('F')
