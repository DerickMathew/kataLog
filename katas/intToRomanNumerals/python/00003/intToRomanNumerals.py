class IntToRomanNumerals:
    def replaceN(self, replacerObjArr, num):
        returnVal = ''
        if len(replacerObjArr) == 0:
            return returnVal

        replacerObj = replacerObjArr[0]
        if num >= replacerObj['integer']:
            times = int(num / replacerObj['integer'])
            num -= (times * replacerObj['integer'])
            returnVal = replacerObj['romanNumeral'] * times

        return returnVal + self.replaceN(replacerObjArr[1:], num)

    def getRomanNumeral(self, num):
        return self.replaceN(
            [
                {
                    'integer': 1000,
                    'romanNumeral': 'M'
                }, {
                    'integer': 900,
                    'romanNumeral': 'CM'
                }, {
                    'integer': 500,
                    'romanNumeral': 'D'
                }, {
                    'integer': 400,
                    'romanNumeral': 'CD'
                }, {
                    'integer': 100,
                    'romanNumeral': 'C'
                }, {
                    'integer': 90,
                    'romanNumeral': 'XC'
                }, {
                    'integer': 50,
                    'romanNumeral': 'L'
                }, {
                    'integer': 40,
                    'romanNumeral': 'XL'
                }, {
                    'integer': 10,
                    'romanNumeral': 'X'
                }, {
                    'integer': 9,
                    'romanNumeral': 'IX'
                }, {
                    'integer': 5,
                    'romanNumeral': 'V'
                }, {
                    'integer': 4,
                    'romanNumeral': 'IV'
                }, {
                    'integer': 1,
                    'romanNumeral': 'I'
                },
            ],
            num
        )
