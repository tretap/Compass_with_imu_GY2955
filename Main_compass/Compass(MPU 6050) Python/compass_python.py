import smbus 
import math 
import os 

from compass_imu_Compass_function import *

while(1):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Magnetometer Data.")
	print("----------")

	hall_xout = read_word_mag_gain(0x04)
	hall_yout = read_word_mag_gain(0x06)
	hall_zout = read_word_mag_gain(0x08)

	print("Hall_xout: "+str(hall_xout))
	print("Hall_yout: "+str(hall_yout))
	print("Hall_zout: "+str(hall_zout))