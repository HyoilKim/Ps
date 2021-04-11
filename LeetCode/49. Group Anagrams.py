# my solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for st in strs:
            word = tuple(sorted(list(st))) 
            if dic.get(word, "") == "":
                dic[word] = [st]
            else:
                dic[word].append(st)
        return list(dic.values())

# another solution
# short code, same algorithms
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()