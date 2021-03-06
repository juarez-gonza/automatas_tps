import unittest

import p1
import p2
import p3

from Turing import Turing
from Input import Input_Tester
from Report import RTester
from falsemain import fmain

class Test_Turing(unittest.TestCase):
    def setUp(self):
        self.tms = [
        {
            "estados": p1.Estados,
            "alfabeto": p1.Alfabeto,
            "tb": p1.tb,
            "ok": ["", "a", "aaaaaa", "ba"],
            "reject": ["b", "ab", "aaaaaaaaaaaab"]
        },
        {
            "estados": p2.Estados,
            "alfabeto": p2.Alfabeto,
            "tb": p2.tb,
            "ok": ["", "x", "yx", "xyx", "xyxxyxyx"],
            "reject": ["xy", "xxy", "y"]
        },
        {
            "estados": p3.Estados,
            "alfabeto": p3.Alfabeto,
            "tb": p3.tb,
            "ok": ["b", "a", "ab", "aaaaaaaaaaaaab"],
            "reject": ["aa", "ba", "aaaaaaaaaaaaaaaa"]
        }
        ]
        self.input_m = Input_Tester()

    def test_accept(self):
        for tm in self.tms:
            reporter = RTester()
            for string in tm["ok"]:
                t = Turing(tm["tb"], tm["estados"], tm["alfabeto"], reporter)
                out = fmain(t, reporter, self.input_m, inp=string)
                self.assertTrue(out)

    def test_reject(self):
        for tm in self.tms:
            reporter = RTester()
            for string in tm["reject"]:
                t = Turing(tm["tb"], tm["estados"], tm["alfabeto"], reporter)
                out = fmain(t, reporter, self.input_m, inp=string)
                self.assertFalse(out)

if __name__ == "__main__":
    unittest.main()
