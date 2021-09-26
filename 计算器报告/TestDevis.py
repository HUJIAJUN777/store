from unittest import TestCase
from Calc import Calc

class TestCalc(TestCase):
    def testdevision1(self):
        num1=10
        num2=20
        sum=0.5

        mult=Calc()
        s=mult.devision(num1,num2)

        self.assertEqual(sum,s)

    def testdevision2(self):
        num1=10
        num2=-20
        sum=-0.5

        mult=Calc()
        s=mult.devision(num1,num2)

        self.assertEqual(sum,s)

    def testdevision3(self):
        num1=-10
        num2=-20
        sum=0.5

        mult=Calc()
        s=mult.devision(num1,num2)

        self.assertEqual(sum,s)

    def testdevision4(self):
        num1=10000000000000000
        num2=100
        sum=100000000000000

        mult=Calc()
        s=mult.devision(num1,num2)

        self.assertEqual(sum,s)