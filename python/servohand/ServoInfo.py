

class ServoInfo(object):

    def __init__(self):
        self._position_ms = None
        self._calibration = {
            "min_ms": 1.5,
            "full_ms": 1.5,
            "max_ms": 1.5,
        }

    def setCalibration(self, min_ms, full_ms, max_ms):
        self._calibration["min_ms"] = min_ms
        self._calibration["full_ms"] = full_ms
        self._calibration["max_ms"] = max_ms

    def setPosition(self, position_ms):
        assert 0 <= position_ms <= 3, "Invalid servo Position (units: ms)"
        self._position_ms=position_ms