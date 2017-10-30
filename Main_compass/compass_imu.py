import smbus 
import math 

from compass_imu_function import *

power_mgmt_1 = 0x6B
power_mgmt_2 = 0x6C
address = 0x68 

bus = smbus.SMBus(1)
bus.write_byte_data(address, power_mgmt_1, 0)

print("Gyro Data.")
print("----------")

gyro_xout = read_word_2c(0x43)
gyro_yout = read_word_2c(0x45)
gyro_zout = read_word_2c(0x47)

print("gyro_xout: "+str(gyro_xout)+" scaled: " +str(gyro_xout/131))
print("gyro_yout: "+str(gyro_yout)+" scaled: " +str(gyro_yout/131))
print("gyro_zout: "+str(gyro_zout)+" scaled: " +str(gyro_zout/131))
print()

print("Accelerometer data")
print("------------------")

accel_xout = read_word_2c(0x3B)
accel_yout = read_word_2c(0x3D)
accel_zout = read_word_2c(0x3F)

accel_xout_scaled = accel_xout / 16384.0
accel_yout_scaled = accel_yout / 16384.0
accel_zout_scaled = accel_zout / 16384.0

print("Accel_xout: "+str(accel_xout)+" scaled: "+ str(accel_xout_scaled))
print("Accel_yout: "+str(accel_yout)+" scaled: "+ str(accel_yout_scaled))
print("Accel_zout: "+str(accel_zout)+" scaled: "+ str(accel_zout_scaled))

print("X rotation: " + str(get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)))
print("Y rotation: " + str(get_y_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)))