def accept(str):
    vowels = set("aeiou")
    s = set({})
    for char in str:
        if char in vowels:
            s.add(char)
        if len(s) == len(vowels):
            s.add(char)
    if len(s) == len(vowels) :
            print("Accepted ")
    else:

            print("not Accepted ! ")

str = input("enter the string : ")
accept(str)
