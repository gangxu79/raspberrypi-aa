#!/usr/bin/env python
#
# Reads temperature and barometric pressure from BMP180 SPI sensor
# Posts results to http://plot.ly
#


import Adafruit_BMP.BMP085 as BMP085
import PlotlyWrapper
import time

sensor = BMP085.BMP085()
plotter = PlotlyWrapper.TempPresPlotlyWrapper()

for i in range(0, 60):
    temp = sensor.read_temperature()
    pressure_kPa = sensor.read_pressure()/1000
    print 'Temp = {0:0.2f} *C'.format(temp)
    print 'Pressure = {0:0.2f} kPa'.format(pressure_kPa)
    plotter.addTemperaturePressure(temp, pressure_kPa)
    time.sleep(60)

    
    