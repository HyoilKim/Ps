# my solution
# time - O(N^2)
# spcae - O(N)
class Solution:
    def partitionLabels(self, s): 
        result = []
        l, r = 0, 1
        while l < len(s):
            left, right = set(s[l:r]), set(s[r:])
            if left & right:
                r += 1
                continue
            else:
                result.append(r-l)
                l, r = r, r+1
        return result

# sliding window solution
# time - O(N)
# space - O(1) / O(26)
'''
Figure out the rightmost index first and use it to denote the start of the next section.
Reset the left pointer at the start of each new section.
Store the difference of right and left pointers + 1 as in the result for each section.
'''
def partition_labels(S):
	rightmost = {c:i for i, c in enumerate(S)}
	left, right = 0, 0

	result = []
	for i, letter in enumerate(S):

		right = max(right,rightmost[letter])
	
		if i == right:
			result += [right-left + 1]
			left = i+1

	return result