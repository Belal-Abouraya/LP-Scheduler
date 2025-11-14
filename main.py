from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QPushButton, QScrollArea, QStackedLayout, QMessageBox
from widgets import *


models = []
blocked_slots_models = []

app = QApplication([])
scroll = QScrollArea()
scroll.setWidgetResizable(True)
container = QWidget()
vbox = QVBoxLayout(container)
vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
vbox.setSpacing(20)

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


vbox.addWidget(QLabel('Blocked Slots', alignment=Qt.AlignmentFlag.AlignCenter))
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
create_schedule_button.setStyleSheet("background-color: #2B2D30; border: 1px solid white; border-radius: 8px;")
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
    view = ScheduleView(schedule)
    main_layout.addWidget(view)
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
