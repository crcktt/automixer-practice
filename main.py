import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from gpiozero import Servo
from time import sleep

class PumpController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoMixer V5 Test")
        self.resize(400, 300)

        # 1. Setup the physical servo on GPIO 18
        self.my_servo = Servo(18) 
        self.my_servo.mid()

        # 2. UI Setup
        self.run_button = QPushButton("SPIN SERVO MAX")
        self.run_button.setMinimumHeight(120) 
        self.run_button.clicked.connect(self.trigger_motor)

        # 3. Layout Setup
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def trigger_motor(self):
        # 4. The Hardware Logic
        print("SCREEN TAPPED! Moving motor...")
        
        if self.run_button.text() == "SPIN SERVO MAX":
            self.my_servo.max() 
            self.run_button.setText("SPIN SERVO MIN")
            self.run_button.setStyleSheet("background-color: red; color: white; font-size: 24px;")
        else:
            self.my_servo.min() 
            self.run_button.setText("SPIN SERVO MAX")
            self.run_button.setStyleSheet("font-size: 24px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PumpController()
    window.show()
    sys.exit(app.exec())