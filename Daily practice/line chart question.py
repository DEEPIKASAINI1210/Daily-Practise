import matplotlib.pyplot as plt
Month=["Jan","Feb","Mar","Apr","May","Jun"]
Sales=["1200","1500","900","1800","2100","1700"]
Profit=["300","400","150","500","650","450"]

plt.plot(Month,Sales,marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales")
plt.show()