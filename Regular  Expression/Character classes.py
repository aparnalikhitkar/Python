import re
#\d is equivalent to [0-9]
print("***************************\d***************************")
p = re.compile('\d')
print(p.findall("I went to him  at 11 A.M on 4th July 1886 "))

#\d+ will match a group on[0-9], group of one or greater size
print("***************************\d+***************************")
p= re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886 "))

print("***************************\w***************************")
#\w is equivalent to [a-z A-Z 0-9]
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

print("***************************\w+***************************")
#\w+ matches to group of alphanumeric character
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., He said * in some_lang."))

print("***************************\W***************************")
#\w matches to non alphanumeric characters .
p = re.compile('\W')
print(p.findall("he said *** in some language "))


#Return a list containing every occurrence of a character

txt = "The rain in Spain "
x = re.findall("ai",txt)
print(x)

# '*' replaces the no. of occurrence of a chareacter
p = re.compile('ab*')
print(p.findall("ababbbasdbbab"))

#Check if "Portugal" is in the string
x= re.findall("in",txt)
print(x)
if(x):
    print("yes , there is at least one match! ")
else:
    print("No match")