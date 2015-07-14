# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        globalMinK = [0]
        def minK( dungeon, m, n, maxM, maxN, globalMinK):
            km = kn = None
            if m < maxM:
                km = dungeon[m][n] + minK( dungeon, m + 1, n, maxM, maxN, globalMinK)
            if n < maxN:
                kn = dungeon[m][n] + minK( dungeon, m, n + 1, maxM, maxN, globalMinK)
            #print m, n, globalMinK
            if km is None and kn is None:
                result = dungeon[m][n]
                #globalMinK[0] = 1
            elif km is None:
                result = kn
            elif kn is None:
                result = km
            elif km < kn:
                result = kn
            else:
                result = km
            if len(globalMinK) <= 1:
                globalMinK.append(result)
            elif globalMinK[1] > result:
                globalMinK[1] = result
            #if globalMinK[0] == 1:
                #globalMinK[0] = 0
                #if len(globalMinK) <= 2:
                    #globalMinK.append( globalMinK[1])
                #elif globalMinK[2] < globalMinK[1]:
                    #globalMinK[2] = globalMinK[1]
            return result
        maxM = len( dungeon) - 1
        maxN = len( dungeon[0]) - 1
        result = minK( dungeon, 0, 0, maxM, maxN, globalMinK)
        #result = globalMinK[1]
        if result > 0:
            result = 1
        elif result <= 0:
            result = 1 - result
        return result


if  __name__ == '__main__':
    llist = [[-1,-2,-3,-4,5],[-1,-2,-3,-4,-5],[-1,-2,-3,-4,5]]
    print Solution().calculateMinimumHP( llist)
