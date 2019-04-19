# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5

import unittest
from TimeSheetState import *


class Timesheet(object):
    """ A class representing a timesheet - Not specifically for the term project. """

    def __init__(self):
        self.state = TimeSheetState()
        self.state.transition(NewState)

    def get_state(self):
        return "{}".format(self.state.__class__.name)

    def add_time(self):
        self.state.transition(InProgressState)

    def submit(self):
        self.state.transition(SubmittedState)

    def accept(self):
        self.state.transition(PayrollState)

    def reject(self):
        """
        Transition to InProgress can happen from NewState or SubmittedState
        so we need to take precautions that we're not rejecting a new
        time sheet.
        """
        if self.state.name == "submitted":
            self.state.transition(InProgressState)


class TestTimeSheetState(unittest.TestCase):

    def test_time_sheet_state_initializes(self):
        ts = TimeSheetState()
        self.assertIsNotNone(ts)

    def test_timesheet_starts_in_new_state(self):
        ts = Timesheet()
        self.assertEqual("new", ts.get_state())

    def test_timesheet_new_moves_to_inprogress(self):
        ts = Timesheet()
        ts.add_time()
        self.assertEqual("in-progress", ts.get_state())

    def test_timesheet_submission_moves_to_submitted(self):
        ts = Timesheet()
        ts.add_time()
        ts.submit()
        self.assertEqual("submitted", ts.get_state())

    def test_timesheet_acceptance_moves_to_payroll(self):
        ts = Timesheet()
        ts.add_time()
        ts.submit()
        ts.accept()
        self.assertEqual("payroll", ts.get_state())

    def test_timesheet_rejection_moves_to_inprogress(self):
        ts = Timesheet()
        ts.add_time()
        ts.submit()
        ts.reject()
        self.assertEqual("in-progress", ts.get_state())

    def test_timesheet_new_cannot_be_submitted(self):
        ts = Timesheet()
        ts.submit()
        self.assertEqual("new", ts.get_state())

    def test_timesheet_new_cannot_be_rejected(self):
        ts = Timesheet()
        ts.reject()
        self.assertEqual("new", ts.get_state())

    def test_timesheet_new_cannot_be_moved_to_payroll(self):
        ts = Timesheet()
        ts.accept()
        self.assertEqual("new", ts.get_state())

    def test_timesheet_inprogress_cannot_be_moved_to_payroll(self):
        ts = Timesheet()
        ts.add_time()
        ts.accept()
        self.assertEqual("in-progress", ts.get_state())
