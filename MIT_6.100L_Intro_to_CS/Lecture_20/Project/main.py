# 02/05/2025

from dateutil import parser

class Workout:
    """A simple workout class with getters and setters."""

    cal_per_hr = 200 # cal per hr class var

    def __init__(self, start, end, calories=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories # may be None
        self.icon = 'temporary' # placeholder
        self.kind = 'Workout'

    def get_calories(self):
        if (self.calories == None):
            return Workout.cal_per_hr * (self.end - self.start).total_seconds()/3600
        else:
            return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end


my_workout = Workout('9/30/2021 1:35PM', '9/30/2025 1:57PM', 200)

print(Workout.__dict__.keys()) # prints class state dictionary:

# lists all methods associated with our Workout class

# dict_keys(['__module__', '__firstlineno__', '__init__', 'get_calories', 
# 'get_start', 'get_end', 'set_calories', 'set_start', 'set_end', 
# '__static_attributes__', '__dict__', '__weakref__', '__doc__'])
