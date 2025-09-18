def gcdex(a, b):
    if b==0: #если b = 0 то НОД = a
        return a, 1, 0 #вывод 1)это НОД 2,3)сколько a и b нужно для того чтобы получить НОД
    else:
        d, x, y = gcdex(b,a%b) 
        return d,y,x-y*(a//b)


a = int(input()) 
b = int(input())
print(gcdex(a,b))