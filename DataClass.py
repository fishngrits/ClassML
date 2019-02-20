import numpy as np
import matplotlib.pyplot as plt

bombers = 500
fighters = 500

#Average wingspan of a bomber we are saying is 28 feet
#Average for a fighter is 24 feet
#Going to look at adding in some plus/minus 4 feet to differnent types of planes
bWings = 28 + 4 * np.random.randn(bombers)
fWings = 24 + 4 * np.random.randn(fighters)


#Visualizzing the data in a histogram
#bomber in blue fighters in red

plt.hist([bWings, fWings], stacked=True, color=['b', 'r'])
plt.show()