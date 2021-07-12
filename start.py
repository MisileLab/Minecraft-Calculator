from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys
from module1.module1 import module1 as md1
from module1.module1.module1 import Ore

class ItsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.setWindowIcon(QIcon("profile.png"))
        self.setWindowTitle("Minecraft Calculator")
        self.Calculate.clicked.connect(lambda: self.calculateclicked())

    def calculateclicked(self):
        self.FortuneProgressBar.setValue(0)
        self.FortuneProgressBar.setMinimum(0)
        a = None
        currenttext = self.Ore.currentText()
        try:
            level = float(self.FortuneLevel.text())
        except ValueError:
            print("Error: level is not number")
        else:
            if currenttext == "Coal Ore":
                a = md1.FortuneOre(level, Ore.Coal)
            elif currenttext == "Diamond Ore":
                a = md1.FortuneOre(level, Ore.Diamond)
            elif currenttext == "Emerald Ore":
                a = md1.FortuneOre(level, Ore.Emerald)
            elif currenttext == "Iron Ore":
                a = md1.FortuneOre(level, Ore.Iron)
            elif currenttext == "Copper Ore":
                a = md1.FortuneOre(level, Ore.Copper)
            elif currenttext == "Gold Ore":
                a = md1.FortuneOre(level, Ore.Gold)
            elif currenttext == "Nether Gold Ore":
                a = md1.FortuneOre(level, Ore.Nether_Gold)
            elif currenttext == "Nether Quartz Ore":
                a = md1.FortuneOre(level, Ore.Nether_Quartz)
            elif currenttext == "Lapis Lazuil Ore":
                a = md1.FortuneOre(level, Ore.Lapis)
            elif currenttext == "Amethyst Cluster":
                a = md1.FortuneOre(level, Ore.Amethyst)
            try:
                self.FortuneProgressBar.setMaximum(int(self.CalculateNumber.text()))
                self.result.setText(a.calculate(int(self.CalculateNumber.text()), self.FortuneProgressBar))
            except ValueError:
                print("Error: range is not integer")

app = QApplication(sys.argv)
myapp = ItsWindow()
myapp.show()

sys.exit(app.exec())
