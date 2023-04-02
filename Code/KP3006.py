# PyQuest Collection
# Some inspiration to assist with your solution to KP3006
# Soft9000.com
# Group: https://www.facebook.com/PythonVideo/

import math

class SineWave:
    def __init__(self):
        self.screen = []

    def plot(self, x, y):
        y = int((y + 100)/3) # scale it down
        self.screen.append(' ' * y + '*')
        
    def sine_wave(self):
        for angle in range(1, 360*10, 4): # smooth it out
            y = math.sin(math.radians(angle))
            self.plot(angle, int(y * 100))
        return self.screen

for line in SineWave().sine_wave():
    print(line)


