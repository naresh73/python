def printmax(a,b):
    if a>b:
        print(a,"is maximum")
    elif a==b:
        print(a,"is equal to",b)
    else:
        print(b,"is maximum")
printmax(int(input()),int(input()))