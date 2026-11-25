import matplotlib.pyplot as plt
Month=["Jan","Feb","Mar","Apr","May","Jun"]
Sales=[1200,1500,900,1800,2100,1700]
Profit=[300,400,150,500,650,450]
plt.pie(Sales, labels=Month,autopct="%1.1f%%")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Pie Chart")
plt.show()