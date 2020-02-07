lst = [1, 2, 3, 4, 5, 6, 7]
a = 0
for x in lst:
    a += x
b = a / len(lst)
print(b)

n = int(input("Nummer: "))
lstt = []
for i in range(0, n):
    getal = int(input("Nummer: "))
    lstt.append(getal)
c = sum(lst) / n
print("Het gemiddelde is: ", c)