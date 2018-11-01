# 经典问题 从数组中找出一对数使得XOR值最大
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# Could you do this in O(n) runtime?
# 
# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.

# Method 1: Brute Force:
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            check = nums[i] ^ nums[j]
            if check >answer:
                answer = check
    return answer

# Method 2: Build tiel tree (01 tree)
# Time Complexity:
# insert node: O(log n) worse: O(n)
# search time: O(log n) worse: O(n)
# Spcae Complexity: O(n)
def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    root = TrieNode()
    # build the tree
    for num in nums:
        node = root
        for j in range (31, -1, -1):
            tmp = num & 1 << j
            if tmp:
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero
    # query the tree
    # for each num, check each position, if current position is 1, then we choose 0 in the tree, vice versa.
    ans = 0
    for num in nums:
        node = root
        tmp_val = 0
        for j in range (31, -1, -1):
            tmp = num & 1 << j
            if node.one and node.zero:
                if tmp:
                    node = node.zero
                else:
                    node = node.one
                tmp_val += 1 << j
            else:
                if (node.zero and tmp) or (node.one and not tmp):
                    tmp_val += 1 << j
                node = node.one or node.zero
        ans = max(ans, tmp_val)
    return ans

# Method 3:
# Time complexity: O(n)
# Space complexity: O(n)
#
# The key idea is just build the maximal answer bit by bit, so that we want to add a '1' to every bit, but without changing the previous bits.

# By using XOR, how do we get 1: just find two numbers, one has a 1 on this bit, the other has 0 (or they are opposite on this bit).

# How do we guarantee that these two numbers are exactly the same two who construct the previous part of this answer? If we denote the two numbers as a and b, then the previous answer shall be a^b. We also know a and b should exist in the set prefix, and a^b^a=b. The next part is fairly simple: using just try answer ^ a for all a in prefix, if the result still exists in prefix, then the result must be b.
#
# So actually this answer^1^p test two things:
# 1. find the two elements in nums that constructs the previous answer
# 2. check this two elements have opposite bits at current position
def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = 0
    for i in range(32)[::-1]:
        answer <<= 1
        prefixes = {num >> i for num in portfolios}

        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer
