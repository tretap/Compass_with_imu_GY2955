import smbus 
import math 

#-------------------------------------------------------#

"""
This Class create for easy to use MPC6050 (IMU) with get information 
magnetometer , gyroscope , acceletometer form sensor . 

it free to use & edit .

create by. trethep promwiset 

"""

#-------------------------------------------------------#


class prism_mpu_6050():

	def __init__(self,main_address = 0x68):
		self.address = main_address
		self.address_mag = 0x0C # Mag = Magnetometer Register 
		self.power_mgmt_1 = 0x6B
		self.power_mgmt_2 = 0x6C

		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(address, power_mgmt_1, 0)

	def __seting__init__(self):
		#For manual seting example seting 0x0A Operation mode setting, 
		#Output bit setting 
		pass
