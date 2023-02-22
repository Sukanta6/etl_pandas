
# Create a Virtual ENV: cd d:\CODE\Proj_Data
# Install VENV: pip install pipenv
# pipenv install requests

# Upgrade pip Version : python.exe -m pip install --upgrade pip
# Install Library: python -m pip install matplotlib 
# python -m pip install numpy

import matplotlib.pyplot as plt
import numpy as np

def test():
 x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
 plt.plot(x, np.sin(x))       # Plot the sine of each x point
 plt.show()                   # Display the plot

 
