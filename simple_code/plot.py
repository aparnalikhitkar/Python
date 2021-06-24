

from matplotlib import pyplot as plt
#%matplotlib inline
#plotting to our canvas 

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2= [6,15,7]
#plt.plot(x, y)

plt.plot(x,y,'g',label="girls",linewidth  = 3)
plt.plot(x2,y2,'r',label="boys",linewidth  = 3)

#plt.plot([1,2,9],[1,9,6],[1,9,6])
#showing waht we plotted
plt.title("first line chart ") 
plt.xlabel("Student roll number ")
plt.ylabel("Age of  Student  ")
plt.legend()
plt.grid(True,color="b")
plt.show()

