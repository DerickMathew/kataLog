class RomanNumeralsToInt:
    def getIntFromChar(self, romanChar):
        convertionChart = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if romanChar in convertionChart.keys():
            return convertionChart[romanChar]
        return 0

    def getNum(self, romanString):
        outNum = 0;
        nums = []
        getNumWithSign = lambda x, y : -x if x < y else x
        for char in romanString:
            nums.append(self.getIntFromChar(char))
        for i in range(len(nums) - 1):
            outNum += getNumWithSign(nums[i], nums[i+1])
        outNum += nums[-1]
        return outNum
