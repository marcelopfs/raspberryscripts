import RPi.GPIO as GPIO
import time
import os

# Return CPU temperature as float
def getCPUtemp():
	cTemp = os.popen('vcgencmd measure_temp').readline()
	return float(cTemp.replace("temp=","").replace("'C\n",""))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
#GPIO.setwarnings(False)

print "Turn off..."

p=GPIO.PWM(3,150)
p.start(100)

print "Turn on..."

minutes = 0.5;
time.sleep(minutes * 60)

while True:
	CPU_temp = getCPUtemp()
	if CPU_temp > 70.0:
		p.ChangeDutyCycle(100)
		print "Temperature is over than 70ºc. Fan was set to 100%" 
	elif CPU_temp > 50.0:
		p.ChangeDutyCycle(90)		
		print "Temperature is over than 50ºc. Fan was set to 90%."
	elif CPU_temp > 40.0:
                p.ChangeDutyCycle(80)
		print "Temperature is over than 40ºc. Fan was set to 80%."
        elif CPU_temp > 30.0:
                p.ChangeDutyCycle(30)
		print "Temperature is over than 30ºc. Fan was set to 30%."
	else:
		p.ChangeDutyCycle(0)
		p.stop()
		print "Temperature is under 30ºc. Turning off..."
	time.sleep(minutes * 60);

GPIO.cleanup()
