class MathClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def __add__(self, other):
        self.hours = (self.hours + (self.minutes + other) // 60) % 24
        self.minutes = (self.minutes + other) % 60
        return self

    def __sub__(self, other):
        if self.minutes - other < 0:
            if self.hours - abs(self.minutes - other) // 60 - 1 < 0:
                self.hours = 24 - abs(self.hours - abs(self.minutes - other) // 60 - 1) % 24
            else:
                self.hours = abs(self.hours - abs(self.minutes - other) // 60 - 1) % 24
            self.minutes = 60 - (other - self.minutes)
        else:
            self.minutes = self.minutes - other

        return self

    def __mul__(self, other):
        self.hours = (self.hours + other) % 24
        return self

    def __truediv__(self, other):
        if self.hours - other < 0:
            self.hours = 24 - abs(self.hours - other) % 24
        else:
            self.hours = abs(self.hours - other) % 24

        return self

    def get_time(self):
        if self.hours // 10 == 0:
            str_hours = '0' + str(self.hours)
        else:
            str_hours = str(self.hours)

        if self.minutes // 10 == 0:
            str_minutes = '0' + str(self.minutes)
        else:
            str_minutes = str(self.minutes)

        return str_hours + ':' + str_minutes


