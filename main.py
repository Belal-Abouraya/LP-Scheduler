from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QPushButton, QScrollArea, QStackedLayout, QMessageBox
from widgets import *

app = QApplication([])
scroll = QScrollArea()
scroll.setWidgetResizable(True)
container = QWidget()
vbox = QVBoxLayout(container)
vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
vbox.setSpacing(10)

models = []
models_list = ModelList()
vbox.addLayout(models_list, 0)

add_model_button = QPushButton("Add Task")
add_model_button.setMinimumHeight(30)

def add_model():
    model = models_list.add_new_model()
    models.append(model)

add_model_button.clicked.connect(add_model)
vbox.addWidget(add_model_button)

create_schedule_button = QPushButton('Create Schedule')
create_schedule_button.setMinimumHeight(30)
create_schedule_button.setStyleSheet("background-color: #2B2D30; border: 1px solid white; border-radius: 8px;")
create_schedule_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

def create_schedule():
    # TODO
    validation = [m.validate() for m in models]
    validation = [v for v in validation if v is not None]
    if any(validation):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(validation[0])
        msg.setWindowTitle("Validation Error")
        msg.exec()
        return
    schedule_ = [[Model(f'Task {i}{j}') for j in range(1,6)] for i in range(1,8)]
    view = ScheduleView(schedule_)
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
