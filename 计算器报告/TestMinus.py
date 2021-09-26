from unittest import TestCase
from Calc import Calc

class TestMinus(TestCase):

    def testMinus1(self):
        num1=20
        num2=10
        sum=10

        minu=Calc()
        s=minu.minus(num1,num2)

        self.assertEqual(sum,s)


    def testMinus2(self):
        num1=-20
        num2=10
        sum=-30

        minu=Calc()
        s=minu.minus(num1,num2)

        self.assertEqual(sum,s)


    def testMinus3(self):
        num1=20
        num2=-10
        sum=30

        minu=Calc()
        s=minu.minus(num1,num2)

        self.assertEqual(sum,s)


    def testMinus4(self):
        num1=-10
        num2=-10
        sum=-0

        minu=Calc()
        s=minu.minus(num1,num2)

        self.assertEqual(sum,s)
