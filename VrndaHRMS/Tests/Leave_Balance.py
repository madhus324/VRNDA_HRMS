import time

import pytest
import unittest

from PageObjects.LeaveBalance import LeaveBal
from PageObjects.LeaveRequest import LeaveReq
from PageObjects.Login import Loginpage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class Test_Leavebalance(BaseTest):

    def test_leave_req(self):
        leavebal = LeaveBal(self.driver)
        leavebal.navigate_leavebal()
        leavebal.capture_leavebal()
        time.sleep(5)
