class IntToRomanNumerals:
    def replaceN(self, divisor, replacementString, integer, romanNumeral):
        if integer >= divisor:
            integer -= divisor
            romanNumeral = romanNumeral + replacementString
            return self.replaceN(
                divisor,
                replacementString,
                integer,
                romanNumeral
            )
        return {
            'integer': integer,
            'romanNumeral': romanNumeral
        }

    def getRomanNumeral(self, num):
        replace1000 = lambda x: self.replaceN(1000, 'M', x['integer'], x['romanNumeral'])
        replace900 = lambda x: self.replaceN(900, 'CM', x['integer'], x['romanNumeral'])
        replace500 = lambda x: self.replaceN(500, 'D', x['integer'], x['romanNumeral'])
        replace400 = lambda x: self.replaceN(400, 'CD', x['integer'], x['romanNumeral'])
        replace100 = lambda x: self.replaceN(100, 'C', x['integer'], x['romanNumeral'])
        replace90 = lambda x: self.replaceN(90, 'XC', x['integer'], x['romanNumeral'])
        replace50 = lambda x: self.replaceN(50, 'L', x['integer'], x['romanNumeral'])
        replace40 = lambda x: self.replaceN(40, 'XL', x['integer'], x['romanNumeral'])
        replace10 = lambda x: self.replaceN(10, 'X', x['integer'], x['romanNumeral'])
        replace9 = lambda x: self.replaceN(9, 'IX', x['integer'], x['romanNumeral'])
        replace5 = lambda x: self.replaceN(5, 'V', x['integer'], x['romanNumeral'])
        replace4 = lambda x: self.replaceN(4, 'IV', x['integer'], x['romanNumeral'])
        replace1 = lambda x: self.replaceN(1, 'I', x['integer'], x['romanNumeral'])
        returnValue = (
            replace1(
            replace4(
            replace5(
            replace9(
            replace10(
            replace40(
            replace50(
            replace90(
            replace100(
            replace400(
            replace500(
            replace900(
            replace1000({
                'integer': num,
                'romanNumeral': ''
            })))))))))))))
        )
        return returnValue['romanNumeral']
