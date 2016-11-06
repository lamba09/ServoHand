

class ServoInfo(object):

    def __init__(self, channel, min_ms, max_ms, full_ms, pin=None):
        self._position_ms = None
        self._channel = channel
        self._pin = pin
        self._calibration = {
            "min_ms": min_ms,
            "full_ms": max_ms,
            "max_ms": full_ms,
        }

    def setCalibration(self, min_ms, full_ms, max_ms):
        self._calibration["min_ms"] = min_ms
        self._calibration["full_ms"] = full_ms
        self._calibration["max_ms"] = max_ms

    def setPosition(self, position_ms):
        assert 0 <= position_ms <= 3, "Invalid servo Position (units: ms)"
        self._position_ms=position_ms
        return position_ms

    def getPosition(self):
        return self._position_ms

    def setPositionDegree(self, position_degree):
        return self.setPosition(self.convertDegreeToMs(position_degree))

    def setPositionPercent(self, position_percent):
        return self.setPosition(self.convertPercentToMs(position_percent))

    def convertDegreeToMs(self, degree):
        return 1. + 0.5*(degree-45)/45.

    def convertPercentToMs(self, percent):
        assert 0. <= percent <= 1.5
        pos_min_ms = self._calibration["min_ms"]
        pos_full_ms = self._calibration["full_ms"]
        if pos_min_ms is not None and pos_full_ms is not None:
            return pos_min_ms + (pos_full_ms - pos_min_ms) * percent
        else:
            raise ValueError("Servo not calibrated yet.")