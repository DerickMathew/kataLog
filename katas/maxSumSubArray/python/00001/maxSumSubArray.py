class MaxSumSubArray:
    def maxSum(self, array):
        max = runSum = array[0]
        for num in array[1:]:
            runSum += num
            if(num > runSum):
                runSum = num
            if (max < runSum):
                max = runSum
        return max

if __name__ == '__main__':
    maxSumSubArray = MaxSumSubArray()
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    print (maxSumSubArray.maxSum(array))
