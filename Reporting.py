# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5

import datetime
import io


class Report:
    _name = None  # Project Or Worker
    _start_date = None
    _end_date = None
    _time_data = None
    _buffer = io.StringIO("")

    def __init__(self, name, start_date, end_date, time_data):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._time_data = time_data

    def header(self): pass

    def body(self): pass

    def footer(self): pass

    def process(self):
        self.header()
        self.body()
        self.footer()
        return self._buffer.getvalue()


class ProjectReport(Report):

    def __init__(self, name, start_date, end_date, time_data):
        super(ProjectReport, self).__init__(name, start_date, end_date, time_data)

    def header(self):
        self._buffer.write("Project Time Report for {}\n".format(self._name))
        self._buffer.write("Start Date: {}\tEnd Date: {}\n".format(self._start_date, self._end_date))

    def body(self):
        for row in self._time_data:
            self._buffer.write("{}\n".format(row))  # TODO: Will need to elaborate once Time Data is finalized.

    def footer(self):
        self._buffer.write("Printed on {}\n".format(datetime.datetime.now()))


class TimeSheetReport(Report):

    def __init__(self, name, start_date, end_date, time_data):
        super(TimeSheetReport, self).__init__(name, start_date, end_date, time_data)

    def header(self):
        self._buffer.write("Time Sheet Report for {}\n".format(self._name))
        self._buffer.write("Start Date: {}\tEnd Date: {}\n".format(self._start_date, self._end_date))

    def body(self):
        for row in self._time_data:
            self._buffer.write("{}\n".format(row))  # TODO: Will need to elaborate once Time Data is finalized.

    def footer(self):
        self._buffer.write("Printed on {}\n".format(datetime.datetime.now()))
