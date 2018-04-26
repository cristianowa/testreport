
from unittest import TestCase

class TestReport(TestCase):
    def __init__(self, *args, **kwargs):
        self.__report_info__ = []
        super(TestReport, self).__init__(*args, **kwargs)
    def __del__(self):
        super(TestReport, self).__del__()
    def title(self, title):
        pass
    def explanation(self, text):
        pass
    def tip(self, text):
        pass
    def code(self, text):
        pass

