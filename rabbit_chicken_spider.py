aa = int(input("How many legs in this room for caluculating spider, hen, rabbit:"))
hen_n = int(aa/2)
spider_n = int(aa/8)
rabbit_n = int(aa/4)
kk = 0
print('\nTotal '+str(aa)+' legs in room')
print('spider', 'rabbit', 'chick')
for i in range(1, spider_n+1):
    for j in range(1, rabbit_n):
        re_legs = aa - i*8 - j*4
        if (re_legs > 0) :
            if (re_legs%2 == 0):
                print(i,j,int(re_legs/2))
                kk += 1
print()
