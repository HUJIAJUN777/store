from unittest import TestCase
from Calc import Calc

class TestCALC(TestCase):

    def testAdd1(self):
        num1=10
        num2=10
        sum=20

        calc=Calc()
        s=calc.add(num1,num2)

        self.assertEqual(sum,s)

    def testAdd2(self):
        num1 = -10
        num2 = -10
        sum = -20

        calc = Calc()
        s = calc.add(num1, num2)

        self.assertEqual(sum, s)

    def testAdd3(self):
        num1 = -10
        num2 = 10
        sum = 0

        calc = Calc()
        s = calc.add(num1, num2)

        self.assertEqual(sum, s)

    def testAdd4(self):
        num1 = 1000000000000000000000000000
        num2 = 10
        sum = 1000000000000000000000000010

        calc = Calc()
        s = calc.add(num1, num2)

        self.assertEqual(sum, s)


    def testAdd5(self):
        num1 = 10.01
        num2 = 10.01
        sum = 20.02

        calc = Calc()
        s = calc.add(num1, num2)

        self.assertEqual(sum, s)