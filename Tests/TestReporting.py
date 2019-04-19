# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5

import unittest
from Reporting import ProjectReport
from Reporting import TimeSheetReport


class TestProjectReport(unittest.TestCase):

    def test_create_project_report(self):
        r = ProjectReport("Super Project", "01/01/2010", "12/31/2010", ["a", "b", "c"])

        output = r.process()

        self.assertIsNotNone(output)
        self.assertTrue(output.startswith("Project Time Report for Super Project"))

    def test_create_time_sheet_report(self):
        r = TimeSheetReport("Billy", "01/01/2010", "12/31/2010", ["a", "b", "c"])

        output = r.process()

        self.assertIsNotNone(output)
        self.assertTrue(output.startswith("Time Sheet Report for Billy"))

