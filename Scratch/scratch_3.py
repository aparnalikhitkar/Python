import  re

def check(str1):
    check_str  = re.compile('[~!@#$%^&*()_+<>{}:?;]')

    if(check_str.search(str1) == None):
        print("String Don't have any special Character ")
    else:
        print("String have a special character ")
str1 = input("Enter the String : ")
check(str1)