import smbus 
import math 
import os 

from compass_imu_Compass_function import *

first = self_test_mag()
fuse_access_mode_init_()

while(1):
	os.system('cls' if os.name == 'nt' else 'clear')

	print("SELF TEST FIRST :> " +str(first))

	print("Magnetometer Data.")
	print("----------")

	#hall_xout = read_word_mag_gain(0x04)
	#hall_yout = read_word_mag_gain(0x06)
	#hall_zout = read_word_mag_gain(0x08)

	hall_xout = read_word_mag_sen(0x04,0x10)
	hall_yout = read_word_mag_sen(0x06,0x11)
	hall_zout = read_word_mag_sen(0x08,0x12)	

	print(self_test_mag())

	print("Hall_xout: "+str(hall_xout))
	print("Hall_yout: "+str(hall_yout))
	print("Hall_zout: "+str(hall_zout))