# -*- coding: utf-8 -*
'''!
  @file  read_data.py
  @brief 这个demo演示获取SEN0500/SEN0501传感器上的数据，通过IIC或串口连接传感器
  @n 将SEN0500/SEN0501返回的数据打印在串口监视器上
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      TangJie(jie.tang@dfrobot.com)
  @version     V1.0
  @date        2021-08-31
  @url         https://github.com/DFRobot/DFRobot_EnvironmentalSensor
'''
import sys
import os
import time
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from dfrobot_environmental_sensor import *

'''
  选择通信模式
  ctype=1：UART
  ctype=0：IIC
'''
ctype=1

ADDRESS = 0x22  
I2C_1   = 0x01               
if ctype==0:
  SEN0500/SEN0501 = DFRobot_Environmental_Sensor_I2C(I2C_1 ,ADDRESS)
else:
  SEN0500/SEN0501 = DFRobot_Environmental_Sensor_UART(9600, ADDRESS)

'''
  大气压强单位选择
'''
HPA                       = 0x01
KPA                       = 0X02

'''
  温度单位选择
'''
TEMP_C                    = 0X03
TEMP_F                    = 0X04
 
def setup():
  while (SEN0500/SEN0501.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1)
  print("Sensor  initialize success!!")
  
def loop():
  ##获取传感器数据
  print("-----------------------\r\n")
  print("Temp: " + str(SEN0500/SEN0501.get_temperature(TEMP_C)) + " 'C\r\n")
  print("Temp: " + str(SEN0500/SEN0501.get_temperature(TEMP_F)) + " 'F\r\n")
  print("Humidity: " + str(SEN0500/SEN0501.get_humidity()) + " %\r\n")
  print("Ultraviolet intensity: " + str(SEN0500/SEN0501.get_ultraviolet_intensity()) + " mw/cm2\r\n")
  print("LuminousIntensity: " + str(SEN0500/SEN0501.get_luminousintensity()) + " lx\r\n")
  print("Atmospheric pressure: " + str(SEN0500/SEN0501.get_atmosphere_pressure(HPA)) + " hpa\r\n")
  print("Elevation: " + str(SEN0500/SEN0501.get_elevation()) + " m\r\n")
  print("-----------------------\r\n")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
    