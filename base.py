import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PyQt6.QtCore import QDate

class CalendarApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calendar App")
        self.setGeometry(200,200,400,300)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        self.date_label = QLabel()
        layout.addWidget(self.date_label)

        self.event_label = QLabel()
        layout.addWidget(self.event_label)

        self.setLayout(layout)

        # events list
        self.events = {
            "1-1": "New Year ",
            "26-1": "Republic Day 🇮🇳",
            "15-8": "Independence Day 🇮🇳",
            "2-10": "Gandhi Jayanti"
        }

        self.check_today()

    def check_today(self):
        today = QDate.currentDate()

        day = today.day()
        month = today.month()
        year = today.year()

        self.date_label.setText(f"Today: {day}/{month}/{year}")

        key = f"{day}-{month}"

        if key in self.events:
            self.event_label.setText(self.events[key])
        else:
            self.event_label.setText("Nothing special today 🙂")


app = QApplication(sys.argv)
window = CalendarApp()
window.show()
sys.exit(app.exec())
