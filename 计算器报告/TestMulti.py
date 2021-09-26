from unittest import TestCase
from Calc import Calc

class TestMulti(TestCase):
    def testMulti1(self):
        num1=10
        num2=20
        sum=200

        mult=Calc()
        s=mult.multi(num1,num2)

        self.assertEqual(sum,s)

    def testMulti2(self):
        num1=10
        num2=-20
        sum=-200

        mult=Calc()
        s=mult.multi(num1,num2)

        self.assertEqual(sum,s)

    def testMulti3(self):
        num1=-10
        num2=-20
        sum=200

        mult=Calc()
        s=mult.multi(num1,num2)

        self.assertEqual(sum,s)

    def testMulti4(self):
        num1=10000000000000000
        num2=100
        sum=1000000000000000000

        mult=Calc()
        s=mult.multi(num1,num2)

        self.assertEqual(sum,s)