import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

SERVO_PWM_FREQ = 50.

def _pwmPulsewithFromMS(ms):
    return ms * SERVO_PWM_FREQ / 10.



GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, SERVO_PWM_FREQ)
p.start(_pwmPulsewithFromMS(1.5))



