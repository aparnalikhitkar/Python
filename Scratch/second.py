def remove(st):
    return "".join(set(st))
st = input("Enter a String ")
print("after removing dulplicates from string  : " , remove(st))