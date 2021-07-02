# Trie 변형
# defaultdict가 dict보다 속도가 느림
class Node:
    def __init__(self):
        self.children = {}
        self.length = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur_node = self.head
        length = len(string)
        
        if not length in cur_node.length:
            cur_node.length[length] = 1
        else:
            cur_node.length[length] += 1

        for c in string:
            if not c in cur_node.children:
                cur_node.children[c] = Node()
                
            cur_node = cur_node.children[c]
            length -= 1
            
            if not length in cur_node.length:
                cur_node.length[length] = 1
            else:
                cur_node.length[length] += 1

    def search(self, query):
        cur_node = self.head
        for i, c in enumerate(query):
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            elif c == '?' and (len(query)-i) in cur_node.length:
                return cur_node.length[len(query)-i]
            else:
                return 0


def solution(words, queries):
    trie = Trie()
    revesed_trie = Trie()

    for word in words:
        trie.insert(word)
        revesed_trie.insert(word[::-1])

    result = []
    for query in queries:
        if query[0] != '?':
            result.append(trie.search(query))
        else:
            result.append(revesed_trie.search(query[::-1]))
    return result

# BST 풀이
'''
와일드카드 부분을 a 와 z로 변경하고 bisect함수를 이용하여 해당 되는 단어가 몇개인지 구하면된다.

예를 들어 쿼리에 'pro???'  가 들어있고 단어에는 [proabc, procdd,prabcd] 가 들어 있다면,

prabcd  proaaa(?를 a로변경) proabc procdd prozzz(? 를 z로 변경) 

prozzz의 인덱스 (4) - proaaa의 인덱스 (1) - 1 = 2  -> 해당하는 가사의 갯수 2 
'''
import bisect
import collections

def func(a,left,right):
    left_idx = bisect.bisect_left(a,left)
    right_idx = bisect.bisect_right(a,right)

    return right_idx - left_idx

def solution(words, queries):
    answer = []

    # 단어 길이 순으로 분리하기위해 딕셔너리 생성
    dic = collections.defaultdict(list)
    dic_reverse = collections.defaultdict(list)

    for word in words:
        # 단어 길이 순으로 분리
        dic[len(word)].append(word)
        dic_reverse[len(word)].append(word[::-1])

    #정렬
    for key in dic.keys():
        dic[key].sort()
        dic_reverse[key].sort()

    # 쿼리를 하나씩 확인하며 처리
    for query in queries: 

        #접미사에 와일드 카드가 붙은 경우
        if query[0] != '?':
            answer.append(func(dic[len(query)],query.replace('?','a'),query.replace('?','z')))

        #접두사에 와일드 카드가 붙은 경우
        else:
            query = query[::-1]
            answer.append(func(dic_reverse[len(query)],query.replace('?','a'),query.replace('?','z')))
    
    return answer 