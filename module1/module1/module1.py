from PyQt6.QtWidgets import QProgressBar
import numpy as np

class Ore:
    Coal = 1
    Diamond = 1
    Emerald = 1
    Iron = 1
    Copper = "Copper"
    Gold = 1
    Nether_Gold = "Nether Gold"
    Nether_Quartz = 1
    Lapis = "Lapis"
    Amethyst = 4

class FortuneOre:
    def __init__(self, level:float, ore:Ore):
        self.ore = ore
        self.level = level

    def calculate(self, number:int, progressbar:QProgressBar):
        multiplier = (float(1) / (self.level + float(2))) + ((self.level + float(1)) / float(2))
        numberores = []
        i = 1
        numberore = self.ore
        if isinstance(self.ore, str):
            numberore = 0
            if self.ore == "Copper":
                numberores = np.random.randint(2,4, size=number)
            elif self.ore == "Nether Gold":
                numberores = np.random.randint(2,7, size=number)
            elif self.ore == "Lapis":
                numberores = np.random.randint(4,10, size=number)
            for row in numberores:
                numberore = float(numberore) + (float(row) * float(multiplier))
                i = i + 1
                progressbar.setValue(i)
        else:
            numberore = (float(numberore) * float(multiplier)) * float(number)
        return str(int(numberore))