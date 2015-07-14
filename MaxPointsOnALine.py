'''
for every line L consists of only two points (p1,p2):
    if p1.x!=p2.x:
        line must cross y axis
        y(0)=y1-(y2-y1)/(x2-x1)*x1
        key(L)=(y(0),(p2.y-p1.y)/(p2.x-p1.x))
    elif p1.x==p2.x:
        line must cross x axis
        x(0)=x1-(x2-x1)/(y2-y1)*y1
        key(L)=(x(0),Infinity)
'''

import time
#Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = float(a)
        self.y = float(b)
        self.copy=1

    def __repr__(self):
        return str((self.x,self.y,self.copy))

    def tuple(self):
        return (self.x,self.y,self.copy)

class Line:
    def __init__(self,p1=None,p2=None):
        self.p1=p1
        self.p2=p2

    def __repr__(self):
        return str((self.p1,self.p2))

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):

        #calculate duplicates
        uniquePoints={}
        for point in points:
            key=(point.x,point.y)
            if uniquePoints.__contains__(key):
                uniquePoints[key].copy=uniquePoints[key].copy+1
            else:
                uniquePoints[key]=point
        points=list(uniquePoints.values())
        #print('unique points:',points)

        if len(points)<1:
            return 0
        if len(points)==1:
            return points[0].copy

        #calculate lines with two points
        lines=[]
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                line=Line(points[i],points[j])
                lines.append(line)
        #print('line pairs:',lines)

        #calculate line key
        #print len(uniquePoints)
        #print len(lines)
        lineSets={}
        for line in lines:
            a = time.time()
            p1=line.p1
            p2=line.p2
            if p1.x!=p2.x:
                ka=p1.y-(p2.y-p1.y)/(p2.x-p1.x)*p1.x
                kb=(p2.y-p1.y)/(p2.x-p1.x)
            else:
                ka=p1.x-(p2.x-p1.x)/(p2.y-p1.y)*p1.y
                kb=None
            key=(ka,kb)
            if lineSets.__contains__(key)==False:
                lineSets[key]=set()
            lineSets[key].add(p1.tuple())
            lineSets[key].add(p2.tuple())
            b = time.time()
        #print('lineSets:',lineSets)

        #calculate line sizes
        lineSizes=map(lambda s:sum(map(lambda e:e[2],s)),lineSets.values())
        #print(lineSizes)
        return max(lineSizes)
if __name__ == '__main__':
    lList = []
    #pList = [Point(1,2), Point(2,3), Point(3,1),Point(3,5),Point(3,1),Point(3,1)]
    #lList.append(pList)
    pList = [Point(-54,-297),Point(-36,-222),Point(3,-2),Point(30,53),Point(-5,1),Point(-36,-222),Point(0,2),Point(1,3),Point(6,-47),Point(0,4),Point(2,3),Point(5,0),Point(48,128),Point(24,28),Point(0,-5),Point(48,128),Point(-12,-122),Point(-54,-297),Point(-42,-247),Point(-5,0),Point(2,4),Point(0,0),Point(54,153),Point(-30,-197),Point(4,5),Point(4,3),Point(-42,-247),Point(6,-47),Point(-60,-322),Point(-4,-2),Point(-18,-147),Point(6,-47),Point(60,178),Point(30,53),Point(-5,3),Point(-42,-247),Point(2,-2),Point(12,-22),Point(24,28),Point(0,-72),Point(3,-4),Point(-60,-322),Point(48,128),Point(0,-72),Point(-5,3),Point(5,5),Point(-24,-172),Point(-48,-272),Point(36,78),Point(-3,3)]
    #pList = [Point(-240,-657),Point(-27,-188),Point(-616,-247),Point(-264,-311),Point(-352,-393),Point(-270,-748),Point(3,4),Point(-308,-87),Point(150,526),Point(0,-13),Point(-7,-40),Point(-3,-10),Point(-531,-892),Point(-88,-147),Point(4,-3),Point(-873,-555),Point(-582,-360),Point(-539,-207),Point(-118,-206),Point(970,680),Point(-231,-47),Point(352,263),Point(510,143),Point(295,480),Point(-590,-990),Point(-236,-402),Point(308,233),Point(-60,-111),Point(462,313),Point(-270,-748),Point(-352,-393),Point(-35,-148),Point(-7,-40),Point(440,345),Point(388,290),Point(270,890),Point(10,-7),Point(60,253),Point(-531,-892),Point(388,290),Point(-388,-230),Point(340,85),Point(0,-13),Point(770,473),Point(0,73),Point(873,615),Point(-42,-175),Point(-6,-8),Point(49,176),Point(308,222),Point(170,27),Point(-485,-295),Point(170,27),Point(510,143),Point(-18,-156),Point(-63,-316),Point(-28,-121),Point(396,304),Point(472,774),Point(-14,-67),Point(-5,7),Point(-485,-295),Point(118,186),Point(-154,-7),Point(-7,-40),Point(-97,-35),Point(4,-9),Point(-18,-156),Point(0,-31),Point(-9,-124),Point(-300,-839),Point(-308,-352),Point(-425,-176),Point(-194,-100),Point(873,615),Point(413,676),Point(-90,-202),Point(220,140),Point(77,113),Point(-236,-402),Point(-9,-124),Point(63,230),Point(-255,-118),Point(472,774),Point(-56,-229),Point(90,228),Point(3,-8),Point(81,196),Point(970,680),Point(485,355),Point(-354,-598),Point(-385,-127),Point(-2,7),Point(531,872),Point(-680,-263),Point(-21,-94),Point(-118,-206),Point(616,393),Point(291,225),Point(-240,-657),Point(-5,-4),Point(1,-2),Point(485,355),Point(231,193),Point(-88,-147),Point(-291,-165),Point(-176,-229),Point(154,153),Point(-970,-620),Point(-77,33),Point(-60,-111),Point(30,162),Point(-18,-156),Point(425,114),Point(-177,-304),Point(-21,-94),Point(-10,9),Point(-352,-393),Point(154,153),Point(-220,-270),Point(44,-24),Point(-291,-165),Point(0,-31),Point(240,799),Point(-5,-9),Point(-70,-283),Point(-176,-229),Point(3,8),Point(-679,-425),Point(-385,-127),Point(396,304),Point(-308,-352),Point(-595,-234),Point(42,149),Point(-220,-270),Point(385,273),Point(-308,-87),Point(-54,-284),Point(680,201),Point(-154,-7),Point(-440,-475),Point(-531,-892),Point(-42,-175),Point(770,473),Point(118,186),Point(-385,-127),Point(154,153),Point(56,203),Point(-616,-247)]
    lList.append(pList)
    #pList = [Point(1,1), Point(1,1), Point(2,2),Point(2,2),Point(3,1),Point(3,1)]
    #lList.append(pList)
    #pList = [Point(1,1), Point(1,1), Point(2,2),Point(2,2),Point(3,1),Point(3,1)]
    #lList.append(pList)
    #pList = [Point(1,1), Point(1,1), Point(1,1)]
    #lList.append(pList)
    #pList = [Point(3,10), Point(0,2), Point(0,2),Point(3,10)]
    #lList.append(pList)
    #pList = [Point(-4,1), Point(-7,7), Point(-1,5),Point(9,-25)]
    #lList.append(pList)
    for ll in lList:
        b = time.time()
        print Solution().maxPoints( ll)
        a = time.time()
        print a - b
