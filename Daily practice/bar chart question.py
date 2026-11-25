import matplotlib.pyplot as plt
Month=["Jan","Feb","Mar","Apr","May","Jun"]
Sales=["1200","1500","900","1800","2100","1700"]
Profit=["300","400","150","500","650","450"]

plt.bar(Month,Profit)
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Bar Chart")
plt.show()