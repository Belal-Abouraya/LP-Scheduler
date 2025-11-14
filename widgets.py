from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QPoint
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QComboBox, QHBoxLayout, QLabel, \
    QTableWidget, QTableWidgetItem, QGridLayout, QHeaderView

from model import *
import model as m

class NameField(QTextEdit):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setText(model.name)
        self.textChanged.connect(self.on_name_change)
        self.setMaximumHeight(30)

    def on_name_change(self):
        self.model.name = self.toPlainText()


class DurationField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'{i}' for i in range(1, m.MAX_DURATION + 1)])
        self.setCurrentIndex(model.duration - 1)
        self.currentIndexChanged.connect(self.on_duration_change)
        self.setMinimumHeight(30)

    def on_duration_change(self):
        self.model.duration = self.currentIndex() + 1


class PriorityField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'{i}' for i in range(1, m.MAX_PRIORITY + 1)])
        self.setCurrentIndex(model.priority - 1)
        self.currentIndexChanged.connect(self.on_priority_change)
        self.setMinimumHeight(30)

    def on_priority_change(self):
        self.model.priority = self.currentIndex() + 1


class DeadlineDayField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Day {i}' for i in range(1, m.NO_OF_DAYS + 1)])
        self.setCurrentIndex(model.deadline_day - 1)
        self.currentIndexChanged.connect(self.on_deadline_day_change)
        self.setMinimumHeight(30)

    def on_deadline_day_change(self):
        self.model.deadline_day = self.currentIndex() + 1


class DeadlineSlotField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Slot {i}' for i in range(1, m.NO_OF_SLOTS_PER_DAY + 1)])
        self.setCurrentIndex(model.deadline_slot - 1)
        self.currentIndexChanged.connect(self.on_deadline_slot_change)
        self.setMinimumHeight(30)

    def on_deadline_slot_change(self):
        self.model.deadline_slot = self.currentIndex() + 1


class EarliestStartDayField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Day {i}' for i in range(1, m.NO_OF_DAYS + 1)])
        self.setCurrentIndex(model.earliest_start_day - 1)
        self.currentIndexChanged.connect(self.on_earliest_start_day_change)
        self.setMinimumHeight(30)

    def on_earliest_start_day_change(self):
        self.model.earliest_start_day = self.currentIndex() + 1


class EarliestStartSlotField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Slot {i}' for i in range(1, m.NO_OF_SLOTS_PER_DAY + 1)])
        self.setCurrentIndex(model.earliest_start_slot - 1)
        self.currentIndexChanged.connect(self.on_earliest_start_slot_change)
        self.setMinimumHeight(30)

    def on_earliest_start_slot_change(self):
        self.model.earliest_start_slot = self.currentIndex() + 1


class ModelFields(QHBoxLayout):
    def __init__(self, model):
        super().__init__()
        id_label = QLabel(f'{model.id}')
        self.addWidget(id_label, 1)
        self.addWidget(NameField(model), 8)
        self.addWidget(DurationField(model), 4)
        self.addWidget(PriorityField(model), 4)
        self.addWidget(DeadlineDayField(model), 4)
        self.addWidget(DeadlineSlotField(model), 4)
        self.addWidget(EarliestStartDayField(model), 4)
        self.addWidget(EarliestStartSlotField(model), 4)


class ModelList(QVBoxLayout):
    def __init__(self):
        super().__init__()
        id_label = QLabel('ID')
        name_label = QLabel('Task Name')
        duration_label = QLabel('Duration (slots)')
        priority_label = QLabel('Priority')
        deadline_label = QLabel('Deadline')
        earliest_start_date_label = QLabel('Earliest Start Date')
        id_label.setMinimumWidth(30)
        name_label.setMinimumWidth(30*8)
        duration_label.setMinimumWidth(30*4)
        priority_label.setMinimumWidth(30*4)
        deadline_label.setMinimumWidth(30*8)
        earliest_start_date_label.setMinimumWidth(30*8)
        labels_box = QHBoxLayout()
        labels_box.addWidget(id_label, 1)
        labels_box.addWidget(name_label, 8)
        labels_box.addWidget(duration_label, 4)
        labels_box.addWidget(priority_label, 4)
        labels_box.addWidget(deadline_label, 8)
        labels_box.addWidget(earliest_start_date_label, 8)
        self.addLayout(labels_box)
        self.setStretch(0, 0)
        self.setAlignment(Qt.AlignmentFlag.AlignTop)

    def add_new_model(self):
        model = Model()
        self.addLayout(ModelFields(model))
        return model


class MaxNoContinuousSLotsView(QHBoxLayout):
    def __init__(self):
        super().__init__()
        label = QLabel('Max Number of Continuous Slots')
        label.setMinimumHeight(30)
        label.setMinimumWidth(200)
        label.setMinimumWidth(200)
        self.input = QComboBox()
        self.input.setMinimumHeight(30)
        self.input.setMinimumWidth(150)
        self.input.setMinimumWidth(150)
        self.input.addItems([f'{i}' for i in range(1, m.MAX_NO_CONTINUOUS_SLOTS + 1)])
        self.input.setCurrentIndex(0)
        self.addWidget(label, 0)
        self.addWidget(self.input, 0)
        self.addStretch(1)

    def get_max_no_continuous(self):
        return self.input.currentIndex() + 1

class BlockedSlotDayField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Day {i}' for i in range(1, m.NO_OF_DAYS + 1)])
        self.setCurrentIndex(model.day - 1)
        self.currentIndexChanged.connect(self.on_day_change)
        self.setMinimumHeight(30)
        self.setMinimumWidth(150)

    def on_day_change(self):
        self.model.day = self.currentIndex() + 1


class BlockedSlotSlotField(QComboBox):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.addItems([f'Slot {i}' for i in range(1, m.NO_OF_SLOTS_PER_DAY + 1)])
        self.setCurrentIndex(model.slot - 1)
        self.currentIndexChanged.connect(self.on_slot_change)
        self.setMinimumHeight(30)
        self.setMinimumWidth(150)

    def on_slot_change(self):
        self.model.slot = self.currentIndex() + 1

class BlockedSlotModelFields(QHBoxLayout):
    def __init__(self, model):
        super().__init__()
        day_label = QLabel('Day')
        slot_label = QLabel('Slot')
        day_label.setMinimumWidth(150)
        day_label.setMinimumHeight(30)
        slot_label.setMinimumWidth(150)
        slot_label.setMinimumHeight(30)
        self.addWidget(day_label, 0)
        self.addWidget(BlockedSlotDayField(model), 0)
        self.addWidget(slot_label, 0)
        self.addWidget(BlockedSlotSlotField(model), 0)
        self.addStretch(1)


class BlockedSlotModelList(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setStretch(0, 0)
        self.setAlignment(Qt.AlignmentFlag.AlignTop)

    def add_new_model(self):
        model = BlockedSlotModel()
        self.addLayout(BlockedSlotModelFields(model))
        return model


class ScheduleView(QWidget):
    def __init__(self, schedule: list[list[Model|None]]):
        super().__init__()
        days_container = QWidget()
        days_container.setStyleSheet("background: qlineargradient(x1: 0, y1: 0,x2: 0, y2: 1,stop: 0 #1E1E1E,stop: 0.5 #2D2D2D,stop: 1 #1E1E1E);")
        days_list = QVBoxLayout(days_container)
        for i in range(1, m.NO_OF_DAYS + 1):
            label = QLabel(f'Day {i}', alignment=Qt.AlignmentFlag.AlignCenter)
            label.setMinimumSize(QSize(150, 30))
            days_list.addWidget(label)
        slots_container = QWidget()
        slots_container.setStyleSheet("background: qlineargradient(x1: 0, y1: 0,x2: 1, y2: 0,stop: 0 #1E1E1E,stop: 0.5 #2D2D2D,stop: 1 #1E1E1E);")
        slots_list = QHBoxLayout(slots_container)
        for i in range(1,m.NO_OF_SLOTS_PER_DAY + 1):
            label = QLabel(f'Slot {i}', alignment=Qt.AlignmentFlag.AlignCenter)
            label.setMinimumSize(QSize(150, 30))
            slots_list.addWidget(label)
        schedule_view = QTableWidget(m.NO_OF_DAYS, m.NO_OF_SLOTS_PER_DAY)
        schedule_view.horizontalHeader().setVisible(False)
        schedule_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        schedule_view.verticalHeader().setVisible(False)
        schedule_view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        for d in range(1, m.NO_OF_DAYS + 1):
            for s in range(1, m.NO_OF_SLOTS_PER_DAY + 1):
                schedule_view.setItem(d-1, s-1, QTableWidgetItem(schedule[d-1][s-1].name if schedule[d-1][s-1] is not None else ''))
                schedule_view.item(d-1, s-1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        grid = QGridLayout(self)
        grid.addWidget(QWidget(), 0, 0)
        grid.addWidget(days_container, 1, 0)
        grid.addWidget(slots_container, 0, 1)
        grid.addWidget(schedule_view, 1, 1)
        self.anim = None

    def fade(self):
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(300)
        anim .setStartValue(QPoint(self.width(), 0))
        anim.setEndValue(QPoint(0, 0))
        anim.start()
        self.anim = anim


class Heading(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-size: 20px;font-weight: bold;font-family: Arial;")