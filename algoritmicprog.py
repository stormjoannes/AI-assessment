
def naam():
    n = int(input("hoe groot?"))
    t = 0

    for i in range((n * 2) - 1):
        if i < n:
            t += 1
        else:
            t -= 1

        for j in range(t):
            print("*", end="")
        print("")



naam()

def andereNaam():
    n = int(input("hoe groot? "))
    t = 0
    i = 0
    j = 0

    while i < (n * 2) - 1:
        if i < n:
            t += 1
        else:
            t -= 1

        while j < t:
            print("*", end="")
            j += 1
        print("")
        i += 1
        j = 0

andereNaam()