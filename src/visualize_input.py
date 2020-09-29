import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

query = input('Enter Type of Encoding')
path = './data/data_Binary_NRZ_RX(small).csv'
if (query == 'NRZ') :
	path = "./data/data_Binary_NRZ_RX(small).csv"
else :
	path = "./data/data_PAM4_RX(small).csv"

data = np.genfromtxt('src/data/data_Binary_NRZ_RX(small).csv', delimiter=',', names=['Time', 'ElectricalSignal'])
plt.plot(data['Time'], data['ElectricalSignal'])
plt.xlabel('Time')
plt.ylabel('Electrical Signal')
plt.title('Input Noisy Signal')
plt.show()