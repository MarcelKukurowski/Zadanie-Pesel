import sys

a = sys.argv[1]
suma = 0
keys = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

for i in range(len(keys)):
    result = keys[i] * int(a[i])
    if result > 10:
        result = str(result)[1]
    suma += int(result)
    
suma = int(str(suma)[1])

wynik = 10 - suma

print(wynik)

