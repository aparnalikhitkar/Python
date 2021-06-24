def printWords(a):
    a = a.split(' ')
    for word in a:
        if len(word)%2==0:
            print(word)
a = input("Please enter any string : ")
printWords(a)