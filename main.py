import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class PumpController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoMixer V5 Test")
        self.resize(400, 300) # Makes the window big enough to easily tap

        # 1. Create a large button for your finger
        self.run_button = QPushButton("SPIN SERVO")
        self.run_button.setMinimumHeight(120) 
        
        # 2. Wire the button tap to a function
        self.run_button.clicked.connect(self.trigger_motor)

        # 3. Put the button in the middle of the screen
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def trigger_motor(self):
        # This function runs every time you tap the screen
        print("SCREEN TAPPED! Logic is working.")
        
        # Flips the button text and color back and forth
        if self.run_button.text() == "SPIN SERVO":
            self.run_button.setText("STOP SERVO")
            self.run_button.setStyleSheet("background-color: red; color: white; font-size: 24px;")
        else:
            self.run_button.setText("SPIN SERVO")
            self.run_button.setStyleSheet("font-size: 24px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PumpController()
    window.show()
    sys.exit(app.exec())