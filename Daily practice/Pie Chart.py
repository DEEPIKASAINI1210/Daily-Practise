import matplotlib.pyplot as plt
labels=["Chole","Paneer","Roti","Daal","Manchurian"]
data=[5,40,10,80,15]

plt.pie(data, labels=labels,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()