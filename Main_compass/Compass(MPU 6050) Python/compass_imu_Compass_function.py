import smbus 
import math 

power_mgmt_1 = 0x6B
power_mgmt_2 = 0x6C
user_ctrl = 0x6A
int_pin_cfg = 0x37

address = 0x68 # Main MPU6050 Register 
address_mag = 0x0C #Mag = Magnetometer register 
address_setting_mag = 0x0A

bus = smbus.SMBus(1)
bus.write_byte_data(address, power_mgmt_1, 0)
bus.write_byte_data(address, user_ctrl, 0)
bus.write_byte_data(address, power_mgmt_1, 0)
bus.write_byte_data(address, int_pin_cfg, 2)


bus.write_byte_data(address, address_setting_mag, 0x12)
#-----------------------------------------#

def read_byte_mag(adr):
	return bus.read_byte_data(address, adr)

def read_word_mag(adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr-1)
	val = (high << 8) + low

	return val 

def read_word_mag_gain(adr,gain = 0.00092): #Setting gain << in their 
	val = read_word_mag(adr)
	return val*gain

def read_word_mag_sen(adr,adr_asa): #Sensitivity --> Process with measurement data 
	val = read_word_mag(adr)
	asa = read_byte_mag(adr_asa)

	val2 = (((asa - 128)*0.5)/128)+1
	return val * val2

def self_test_mag(): #For Self_test function , confirm magnetic sensor operation on end products
	bus.write_byte_data(address, address_mag, 0x40)
	return bus.read_byte_data(address, address_mag)

def fuse_access_mode_init_():
	bus.write_byte_data(address, address_setting_mag, 0x1F)
	print("Mode Change to >> FUSE ACCESS MODE << ")

def _access_mode_init_():
	bus.write_byte_data(address, address_setting_mag, 0x12)
	print("Mode Change to >> INIT ACCESS MODE << ")

#def read_word_2c(adr):
	#val = read_word(adr)
	#if(val >= 0x8000):
	#	return -((65535 - val) + 1)
	#else :
	#	return val 

#def dist(a,b):
	#return math.sqrt((a*a)+(b*b))

#def get_y_rotation(x,y,z):
	#radians = math.atan2(x, dist(y,z))
	#return -math.degrees(radians)

#def get_x_rotation(x,y,z):
	#radians = math.atan2(y, dist(x,z))
	#return math.degrees(radians)

	