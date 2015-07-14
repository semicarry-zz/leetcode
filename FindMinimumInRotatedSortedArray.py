class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        i = 0
        j = len(num) - 1
        while( i < j):
            #print i,j,num[i],num[j]
            if num[i] < num[j]:
                j = i
                i = i - 1
            elif num[i] > num[j]:
                if i == j - 1:
                    break
                i = (i + j)/2
            else:
                for k in range(0,len(num)):
                    if num[k] < num[i]:
                        j = k
                        i = j - 1
                if i == j - 1:
                    break
                i = (i + j)/2
        #print "===,",i,j,num[i],num[j]
        if num[i] < num[j]:
            num[j] = num[i]
        return num[j]

if __name__ == '__main__':
    a = [1,1]
    a = [7,8,9,9,0,2,5,5,6]
    a = [1,2,1]
    a = [3,3,1,3]
    a = [10,1,10,10,10]
    a = [3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3]

    print Solution().findMin( a)
