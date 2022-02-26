class Data:
    def __init__(self, date, value, consumption, isValid):
        self.date = date
        self.value = value
        self.consumption = consumption
        self.valid = isValid

    def isValid(self):
        if self.consumption < 0:
            return False
        return True
