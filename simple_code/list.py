my_list = ['a','b','c','d','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])

m_list = ["welcome",[2,8,1,5],"Aparna"]

print(m_list[0][0])
print(m_list[0][1])
print(m_list[0][2])
print(m_list[0][3])
print(m_list[0][4])
print(m_list[0][5])
print(m_list[0][6])
print(m_list[1][3])
print(m_list[2][0])
print(my_list[-1])
print (my_list[-5])
my_list = ['p','r','o','g','r','a','m','i','n','g']
print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])

#Appending list 
odd = [1,3,5]
print("Oringnal list",odd)
odd.append(7)
print(odd)
odd.extend([9,11,13])
print(odd)


y_list = ['p','r','o','g','r','a','m','i','n','g']
y_list.remove('p')

print(y_list)

print(y_list.pop(1))

print(y_list)

print(y_list.pop())

print(y_list)

y_list.clear()

print(y_list)
