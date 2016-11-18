from servohand.ServoControlBoard import ServoControlBoard
from servohand.ServoInfo import ServoInfo

import RPi.GPIO as GPIO


class RaspberryPiBoard(ServoControlBoard):

    def __init__(self):
        super(RaspberryPiBoard, self).__init__()
        GPIO.setmode(GPIO.BOARD)
        self.SERVO_PWM_FREQ = 50.

        self._channel_gpio_pin_map = {
            0: 7,
            1: 11,
            2: 12,
            3: 13,
            4: 15,
        }
        self._gpio_pins = {}

    def __del__(self):
        GPIO.cleanup()
        print "GPIO cleanup complete."

    def _convertMsToDutyCycle(self, ms):
        return ms * self.SERVO_PWM_FREQ / 10.

    def move(self, channel, position):
        print "move() in Raspberry Pi Board CH ", channel, "to positions: ", position
        position_ms = self._servo_info[channel].convertPercentToMs(position)
        print "   --> position_ms = ", position_ms
        self._gpio_pins[channel].ChangeDutyCycle(self._convertMsToDutyCycle(position_ms))
        print "   --> duty cycle  = ", self._convertMsToDutyCycle(position_ms)
        self._servo_info[channel].setPosition(position_ms)

    def _addServoConnection(self, channel):
        assert channel in [0,1,2,3,4], "Invalid Servo Channel: {0}".format(channel)
        if not self._servo_info.has_key(channel):
            gpio_pin = self._channel_gpio_pin_map[channel]
            GPIO.setup(gpio_pin, GPIO.OUT)
            self._gpio_pins[channel] = GPIO.PWM(gpio_pin, self.SERVO_PWM_FREQ)
            servo_info = ServoInfo(channel, 0.5, 2.0, 1.5, gpio_pin)
            self._servo_info[channel] = servo_info
            self._gpio_pins[channel].start(self._convertMsToDutyCycle(1.5))
            self._servo_info[channel].setPosition(1.5)
            self._finger_calibrations[channel] = calibration