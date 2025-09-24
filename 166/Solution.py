class Solution:
    def getFractionPart(self, remainder: int, denominator: int) -> str:
        fraction = []
        previous_remainders = []

        while remainder != 0:
            # Check for repeating numbers
            if remainder in previous_remainders:
                idx = previous_remainders.index(remainder)
                non_repeating = ''.join(map(str, fraction[:idx]))
                repeating = ''.join(map(str, fraction[idx:]))
                return f'{non_repeating}({repeating})'

            previous_remainders.append(remainder)

            divisor = int(remainder / denominator)
            remainder = remainder - (denominator * divisor)
            fraction.append(divisor)

            remainder *= 10

        return "".join(map(str, fraction))

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        firstDivisor = int(numerator / denominator)
        firstRemainder = numerator - (denominator * firstDivisor)

        if firstRemainder == 0:
            return str(firstDivisor)
        else:
            # Doublecheck negative sign
            negativeSign = ""
            if firstDivisor == 0 and (numerator < 0) ^ (denominator < 0):
                negativeSign = "-"

            firstRemainder *= 10
            fraction = self.getFractionPart(abs(firstRemainder), abs(denominator))
            return negativeSign + str(firstDivisor) + "." + str(fraction)


class Tester(Solution):
    def __init__(self, solution):
        self.solution = solution

    def test1(self):
        numerator, denominator = 1, 2
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0.5"

    def test2(self):
        numerator, denominator = 2, 1
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "2"

    def test3(self):
        numerator, denominator = 4, 333
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0.(012)"

    def test4(self):
        numerator, denominator = 7, 5
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "1.4"
    
    def test5(self):
        numerator, denominator = 101, 4
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "25.25"

    def test6(self):
        numerator, denominator = 22, 7
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "3.(142857)"

    def test7(self):
        numerator, denominator = -50, 8
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "-6.25"

    def test8(self):
        numerator, denominator = 50, -8
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "-6.25"
    
    def test9(self):
        numerator, denominator = 0, -5
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0"

    def test10(self):
        numerator, denominator = -1, -2147483648
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0.0000000004656612873077392578125"

    def test11(self):
        numerator, denominator = 1, 6
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0.1(6)"

    def test12(self):
        numerator, denominator = 7, -12
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "-0.58(3)"

    def test13(self):
        numerator, denominator = 89, 270
        answer = self.solution.fractionToDecimal(numerator, denominator)
        assert answer == "0.3(296)"

if __name__ == "__main__":
    tester = Tester(Solution())
    tester.test1(); print("✅ Test 1 Passed!")
    tester.test2(); print("✅ Test 2 Passed!")
    tester.test3(); print("✅ Test 3 Passed!")
    tester.test4(); print("✅ Test 4 Passed!")
    tester.test5(); print("✅ Test 5 Passed!")
    tester.test6(); print("✅ Test 6 Passed!")
    tester.test7(); print("✅ Test 7 Passed!")
    tester.test8(); print("✅ Test 8 Passed!")
    tester.test9(); print("✅ Test 9 Passed!")
    tester.test10(); print("✅ Test 10 Passed!")
    tester.test11(); print("✅ Test 11 Passed!")
    tester.test12(); print("✅ Test 12 Passed!")
    tester.test13(); print("✅ Test 13 Passed!")