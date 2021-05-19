import unittest

import p1
import p3
from Turing import Turing
from Input import Input_Tester
from Report import RTester
from falsemain import fmain

class Test_Turing(unittest.TestCase):
    def setUp(self):
        self.tms = [
        {
            "estados": p1.Estado,
            "alfabeto": p1.Alfabeto,
            "tb": p1.tb,
            "ok": ["", "a", "aaaaaa", "ba"],
            "reject": ["b", "ab", "aaaaaaaaaaaab"]
        },
        {
            "estados": p3.Estado,
            "alfabeto": p3.Alfabeto,
            "tb": p3.tb,
            "ok": ["b", "a", "ab", "aaaaaaaaaaaaab"],
            "reject": ["aa", "ba", "aaaaaaaaaaaaaaaa"]
        }]
        self.input_m = Input_Tester()

    def test_accept(self):
        for tm in self.tms:
            reporter = RTester()
            for string in tm["ok"]:
                t = Turing(tm["tb"], tm["estados"].get_init_st(), tm["alfabeto"], reporter)
                self.assertTrue(fmain(t, reporter, self.input_m, inp=string))

    def test_reject(self):
        for tm in self.tms:
            reporter = RTester()
            for string in tm["reject"]:
                t = Turing(tm["tb"], tm["estados"].get_init_st(), tm["alfabeto"], reporter)
                self.assertFalse(fmain(t, reporter, self.input_m, inp=string))
