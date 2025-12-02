from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QPushButton, QScrollArea, QStackedLayout, QMessageBox
from widgets import *


models = []
blocked_slots_models = []

app = QApplication([])
app.setFont(QFont('Arial', 14))
app.setStyleSheet("""
    QPushButton {
        background-color: white;
        border: 1px solid #444;
        border-radius: 6px;
    }
""")
scroll = QScrollArea()
scroll.setWidgetResizable(True)
container = QWidget()
vbox = QVBoxLayout(container)
vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
vbox.setSpacing(20)

vbox.addWidget(Heading('Tasks'))
models_list = ModelList()
vbox.addLayout(models_list, 0)

add_model_button = QPushButton("Add Task")
add_model_button.setMinimumHeight(30)

def add_model():
    model = models_list.add_new_model()
    models.append(model)

add_model_button.clicked.connect(add_model)
vbox.addWidget(add_model_button)

max_no_continuous_slots_view = MaxNoContinuousSLotsView()
vbox.addLayout(max_no_continuous_slots_view)


vbox.addWidget(Heading('Blocked Slots'))
blocked_slots_list = BlockedSlotModelList()
vbox.addLayout(blocked_slots_list)
add_blocked_slot_button = QPushButton("Add Blocked Slot")
add_blocked_slot_button.setMinimumHeight(30)

def add_new_blocked_slot():
    model = blocked_slots_list.add_new_model()
    blocked_slots_models.append(model)

add_blocked_slot_button.clicked.connect(add_new_blocked_slot)
vbox.addWidget(add_blocked_slot_button)

create_schedule_button = QPushButton('Create Schedule')
create_schedule_button.setMinimumHeight(30)
create_schedule_button.setStyleSheet("background-color: #DCDDE1; border: 1px solid white; border-radius: 8px;")
create_schedule_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

def show_msg(title, details):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setText(details)
    msg.setWindowTitle(title)
    msg.exec()

def create_schedule():
    validation = [_m.validate() for _m in models]
    validation = [v for v in validation if v is not None]
    if any(validation):
        show_msg("Validation Error", validation[0])
        return

    max_no_continuous_slots = max_no_continuous_slots_view.get_max_no_continuous()
    schedule = get_schedule(models, blocked_slots_models, max_no_continuous_slots)
    schedule_container = QWidget()
    layout = QVBoxLayout(schedule_container)
    view = ScheduleView(schedule)
    layout.addWidget(view)
    back_button = QPushButton('Back')
    back_button.setMinimumHeight(30)
    back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    back_button.clicked.connect(lambda: main_layout.removeWidget(schedule_container))
    layout.addWidget(back_button)
    main_layout.addWidget(schedule_container)
    main_layout.setCurrentIndex(1)
    view.fade()

create_schedule_button.clicked.connect(create_schedule)
vbox.addWidget(create_schedule_button)
vbox.addStretch(1)
scroll.setWidget(container)

add_model()

window = QWidget()
main_layout = QStackedLayout(window)
main_layout.addWidget(scroll)
window.resize(1200, 500)
window.show()

app.exec()
