from unittest import TestCase
import functions


class Test(TestCase):
    def test_isAnIntInt(self):
        result = functions.isAInt(20)
        self.assertTrue(result)

    def test_isAnIntString(self):
        result = functions.isAInt("string")
        self.assertFalse(result)

    def test_isValidChoice1(self):
        result = functions.isValidChoice("1")
        self.assertTrue(result)

    def test_isValidChoice2(self):
        result = functions.isValidChoice("2")
        self.assertTrue(result)

    def test_isValidChoice3(self):
        result = functions.isValidChoice("3")
        self.assertTrue(result)

    def test_isValidChoice4(self):
        result = functions.isValidChoice("4")
        self.assertTrue(result)

    def test_isValidChoice5(self):
        result = functions.isValidChoice("5")
        self.assertTrue(result)

    def test_isValidChoice6(self):
        result = functions.isValidChoice("6")
        self.assertTrue(result)

    def test_isValidChoiceInv(self):
        result = functions.isValidChoice("0")
        self.assertFalse(result)

    def test_isValidChoiceInt(self):
        result = functions.isValidChoice(5)
        self.assertFalse(result)

    def test_isValidName0(self):
        result = functions.isValidName("")
        self.assertFalse(result)

    def test_isValidName1(self):
        result = functions.isValidName("a")
        self.assertTrue(result)

    def test_isValidName15(self):
        result = functions.isValidName("qwertyuiopasdfg")
        self.assertTrue(result)

    def test_isValidName30(self):
        result = functions.isValidName("qwertyuiopasdfghjklzxcvbnmqwer")
        self.assertTrue(result)

    def test_isValidName31(self):
        result = functions.isValidName("qwertyuiopasdfghjklzxcvbnmqwert")
        self.assertFalse(result)

    def test_isValidPositionGuard(self):
        self.assertTrue(functions.isValidPosition("Guard"))

    def test_isValidPositionForward(self):
        self.assertTrue(functions.isValidPosition("Forward"))

    def test_isValidPositionCentre(self):
        self.assertTrue(functions.isValidPosition("Centre"))

    def test_isValidPositionOther(self):
        self.assertFalse(functions.isValidPosition("Other"))

    def test_isValidPositionInt(self):
        self.assertFalse(functions.isValidPosition(25))

    def test_isValidInputNumberLower(self):
        self.assertTrue(functions.isValidInputNumber(5, 5, 20))

    def test_isValidInputNumberMid(self):
        self.assertTrue(functions.isValidInputNumber(15, 5, 20))

    def test_isValidInputNumberUpper(self):
        self.assertTrue(functions.isValidInputNumber(20, 5, 20))

    def test_isValidInputNumberUnder(self):
        self.assertFalse(functions.isValidInputNumber(4, 5, 20))

    def test_isValidInputNumberOver(self):
        self.assertFalse(functions.isValidInputNumber(21, 5, 20))
