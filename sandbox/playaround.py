import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

freq = 50. 
pw = 1.5
pw_percent = lambda pw_ms: pw_ms*freq/10.

GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, freq)
p.start(pw_percent(1.5))
