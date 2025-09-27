def sortirovka(mas):
    
    for i in range(len(mas)):
        while mas[i] > mas[i-1] and i != 0:
            mas[i], mas[i-1] = mas[i-1], mas[i]
            i -= 1
    return mas


print(sortirovka([1,2,3,4,9,2,4,0,-10,35,-90]))
