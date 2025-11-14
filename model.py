
class Model:
    count = 0

    def __init__(self, name=''):
        Model.count += 1
        self.id = Model.count
        self.name = name
        self.duration = 1
        self.priority = 1
        self.deadline_day = 7
        self.deadline_slot = 5
        self.earliest_start_day = 1
        self.earliest_start_slot = 1

    def validate(self):
        if not self.name.strip():
            return f"Task {self.id}: Name cannot be empty"
        deadline = self.deadline_day * 5 + self.deadline_slot
        earliest_start = self.earliest_start_day * 5 + self.earliest_start_slot
        if earliest_start > deadline:
            return f"Task {self.id}: Earliest start date must be before deadline"
        if self.duration > deadline - earliest_start:
            return f"Task {self.id}: Duration cannot be longer than the time difference between earliest start and deadline"
        return None


