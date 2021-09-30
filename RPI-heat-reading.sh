#!/bin/bash
#temp_read = vcgencmd measure_temp

ssh pi@raspberrypi.local

sleep 10

raspberry

sleep 10

while :
do
	vcgencmd measure_temp
	sleep 30
done

