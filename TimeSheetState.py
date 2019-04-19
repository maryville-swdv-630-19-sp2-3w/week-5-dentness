# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5

class TimeSheetState(object):
    name = "uninitiated"
    next_states = ['new']

    def transition(self, to_state):
        if to_state.name in self.next_states:
            print(self, ' => ', to_state.name)
            self.__class__ = to_state
        else:
            print(self, ' => switching to', to_state.name, 'not possible.')

    def __str__(self):
        return self.name


class NewState(TimeSheetState):
    name = "new"
    next_states = ['in-progress']


class InProgressState(TimeSheetState):
    name = "in-progress"
    next_states = ['submitted']


class SubmittedState(TimeSheetState):
    name = "submitted"
    next_states = ['payroll', 'in-progress']


class PayrollState(TimeSheetState):
    name = "payroll"
    next_states = []



