class FindTheOddInt:
    def getOddInt(self, numArray):
        counted = []
        for i in numArray:
            if i in counted:
                counted.remove(i)
            else:
                counted.append(i)
        return counted[0]
