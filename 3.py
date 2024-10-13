class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour, self.minute, self.second = hour, minute, second

    def nextSecond(self):
        self.second = (self.second + 1) % 60
        if self.second == 0:
            self.minute = (self.minute + 1) % 60
            if self.minute == 0:
                self.hour = (self.hour + 1) % 24
        return self

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"


time = Time(23, 59, 59)
print(time)
print("After next second:", time.nextSecond())