import math
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        #print tokens
        num = []
        oper = []
        opernum = 0
        value = 0
        for var in tokens:
            if var in ['+', '-', '*', '/']:
                oper.append(var)
                opernum = opernum + 1
            else:
                num.append( int(var))
                value = value + 1
            #print value,opernum
            if value >= 2 and opernum >= 1:
                right = num.pop()
                left = num.pop()
                operation = oper.pop()
                #print left,operation,right
                if operation == '+':
                    result = left + right
                elif operation == '-':
                    result = left - right
                elif operation == '*':
                    result = left * right
                elif operation == '/':
                    if left*right < 0:
                        result = int(- math.floor(abs(left)/abs(right)))
                    else:
                        result = int(math.floor(abs(left) / abs(right)))
                #print result
                num.append( result)
                value = value - 1
                opernum = 0
        return num.pop()

if __name__ == '__main__':
    l = ["4", "13", "5", "/", "+"]
    l = ["2", "1", "+", "3", "*"]
    l = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    l = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    print Solution().evalRPN(l)
