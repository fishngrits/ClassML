import numpy as np
import matplotlib.pyplot as plt

yonko = 200
admirals = 200

print("What we are doing here is making our own data set. We are comparing the power levels of Yonko vs Admirals.")
print("Once we have made our data set we are using an histogram to visualize it.")
#Average power level of a yonko we are saying is 590
#Average for a admirals is 580
#Going to look at adding in some plus/minus 4 power level to differnent types of people
yPower = 590 + 4 * np.random.randn(yonko)
aPower = 580 + 4 * np.random.randn(admirals)


#Visualizzing the data in a histogram
#yonko in blue admirals in red

plt.hist([yPower, aPower], stacked=True, color=['b', 'g'])
plt.show()