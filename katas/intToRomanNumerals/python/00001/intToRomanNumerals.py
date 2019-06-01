class IntToRomanNumerals:
    def countInI(self, n):
        romanOut = ''
        for i in range(n):
            romanOut = romanOut + 'I'
        return romanOut

    def getRomanNumeral(self, num):
        basicRomanNum = self.countInI(num)
        replace5 = lambda s : s.replace('IIIII', 'V')
        replace4 = lambda s : s.replace('IIII', 'IV')
        replace10 = lambda s : s.replace('VV', 'X')
        replace9 = lambda s : s.replace('VIV', 'IX')
        replace50 = lambda s : s.replace('XXXXX', 'L')
        replace40 = lambda s : s.replace('XXXX', 'XL')
        replace100 = lambda s : s.replace('LL', 'C')
        replace90 = lambda s : s.replace('LXL', 'XC')
        replace500 = lambda s : s.replace('CCCCC', 'D')
        replace400 = lambda s : s.replace('CCCC', 'CD')
        replace1000 = lambda s : s.replace('DD', 'M')
        replace900 = lambda s : s.replace('DCD', 'CM')

        officialRomanNumeral = (
            replace900(
            replace1000(
            replace400(
            replace500(
            replace90(
            replace100(
            replace40(
            replace50(
            replace9(
            replace10(
            replace4(
            replace5(
                basicRomanNum
            ))))))))))))
        )
        return officialRomanNumeral
