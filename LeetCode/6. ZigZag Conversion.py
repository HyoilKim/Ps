class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        graph = [['']*len(s) for _ in range(numRows)]

        x, y = 0, 0
        down = True
        right_top = False
        for i, c in enumerate(s):
            graph[x][y] = c
            if down:
                x += 1
                if x == numRows:
                    x -= 2
                    y += 1
                    down = False
                    right_top = True
            elif right_top:
                x -= 1
                y += 1
                if x == -1:
                    x += 2
                    y -= 1
                    down = True
                    right_top = False
        
        res = ""
        for i in graph:
            res += (''.join(i))
        return res

a = Solution()
s = "ABC"
numRows = 1
res = a.convert(s, numRows)
print(res)

# best solution (가독성)
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s 
        n = len(s)
        cycle = 2*numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                    strlist.append(s[j+cycle-2*i])             
        newstr = ''.join(strlist)
        return newstr

# 공간복잡도 O(1)
class Solution(object):
    def convert(self, s, numRows):
        if s == None:
            return s
        if numRows == 0:
            return s
        if numRows == 1:
            return s
        rstr = ""
        for i in range(numRows):
            if i == 0:
                rstr += s[::numRows + (numRows-2)]
            elif i == numRows-1:
                rstr += s[i::numRows + (numRows-2)]
            else:
                spacea = 2*(numRows-i)
                spaceb = 2*i
                counter = 0
                j = i
                while j < len(s):
                    rstr += s[j]
                    if counter % 2 == 0:
                        j+= spacea
                    else:
                        j+=spaceb
                    counter +=1
        return rstr