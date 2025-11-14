from scheduler import Scheduler

NO_OF_DAYS = 7
NO_OF_SLOTS_PER_DAY = 5
MAX_PRIORITY = 10
MAX_DURATION = 10
MAX_NO_CONTINUOUS_SLOTS = 10

class Model:
    count = 0

    def __init__(self, name=''):
        Model.count += 1
        self.id = Model.count
        self.name = name
        self.duration = 1
        self.priority = 1
        self.deadline_day = NO_OF_DAYS
        self.deadline_slot = NO_OF_SLOTS_PER_DAY
        self.earliest_start_day = 1
        self.earliest_start_slot = 1

    def validate(self):
        if not self.name.strip():
            return f"Task {self.id}: Name cannot be empty"
        deadline = self.get_deadline()
        earliest_start = self.get_earliest_start()
        if earliest_start > deadline:
            return f"Task {self.id}: Earliest start date must be before deadline"
        if self.duration > deadline - earliest_start + 1:
            return f"Task {self.id}: Duration cannot be longer than the time difference between earliest start and deadline"
        return None


    def get_deadline(self):
        """Zero Based; Flatten"""
        return (self.deadline_day - 1) * NO_OF_SLOTS_PER_DAY + (self.deadline_slot - 1)

    def get_earliest_start(self):
        """Zero Based; Flatten"""
        return (self.earliest_start_day - 1) * NO_OF_SLOTS_PER_DAY + (self.earliest_start_slot - 1)

    def get_slot_block_constraint(self):
        constraint = [0 for _ in range(NO_OF_DAYS * NO_OF_SLOTS_PER_DAY)]
        for i in range(self.get_earliest_start(), self.get_deadline() + 1):
            constraint[i] = 1
        return constraint


class BlockedSlotModel:
    def __init__(self):
        self.day = 1
        self.slot = 1

    def get_blocked_slot(self):
        """Zero Based; Flatten"""
        return (self.day - 1) * NO_OF_SLOTS_PER_DAY + (self.slot - 1)



def get_schedule(models, blocked_slots_models, max_no_continuous_slots):
    slot_block_constraints = [_m.get_slot_block_constraint() for _m in models]
    blocked_slots = [1 for _ in range(NO_OF_DAYS * NO_OF_SLOTS_PER_DAY)]
    for _m in blocked_slots_models:
        blocked_slots[_m.get_blocked_slot()] = 0
    durations = [_m.duration for _m in models]
    priorities = [_m.priority for _m in models]
    print(max_no_continuous_slots)
    print(slot_block_constraints)
    print(blocked_slots)
    print(durations)
    print(priorities)
    scheduler = Scheduler(
        len(models),
        NO_OF_SLOTS_PER_DAY * NO_OF_DAYS,
        max_no_continuous_slots,
        slot_block_constraints,
        blocked_slots,
        durations,
        priorities
    )
    schedule_model = scheduler.get_model()
    schedule_model.solve()
    schedule_x = scheduler.get_x()
    schedule: list[list[Model | None]] = [[None for _ in range(0, NO_OF_SLOTS_PER_DAY)] for _ in range(0, NO_OF_DAYS)]
    n = len(models)
    m = NO_OF_DAYS * NO_OF_SLOTS_PER_DAY
    f = scheduler.get_f()
    x = schedule_x
    for i in range(n):
        print(f[i].value())

    for i in range(n):
        for j in range(m):
            print(x[i][j].value(), end=' ')
        print()
    for ind in range(len(models)):
        for i in range(0, NO_OF_DAYS):
            for j in range(0, NO_OF_SLOTS_PER_DAY):
                if schedule_x[ind][i * NO_OF_SLOTS_PER_DAY + j].value() == 1:
                    schedule[i][j] = models[ind]
    return schedule