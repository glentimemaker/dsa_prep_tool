# Batch 1: Problems from frequency 62.5% and 50%

# 7: Reverse Integer (Medium)
_register(7,
    description="""<h3>7. Reverse Integer</h3>
<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code> with its digits reversed.
If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range
<code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>
<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>
<h4>Example 1:</h4>
<pre>Input: x = 123
Output: 321</pre>
<h4>Example 2:</h4>
<pre>Input: x = -123
Output: -321</pre>
<h4>Example 3:</h4>
<pre>Input: x = 120
Output: 21</pre>
<h4>Constraints:</h4>
<ul><li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li></ul>""",
    function_name="reverse",
    template="""class Solution:
    def reverse(self, x: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"x": 123}, "expected": 321},
        {"input": {"x": -123}, "expected": -321},
        {"input": {"x": 120}, "expected": 21},
        {"input": {"x": 0}, "expected": 0},
        {"input": {"x": 1534236469}, "expected": 0},
    ],
    solution="""class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if result > (INT_MAX - digit) // 10:
                return 0
            result = result * 10 + digit
        result *= sign
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
""",
    explanation="""## Approach: Math — Digit-by-Digit Reversal

**Time Complexity:** O(log₁₀(x)) — we process each digit once
**Space Complexity:** O(1)

### Steps:
1. Record the sign and work with the absolute value.
2. Extract the last digit using `x % 10`.
3. Build the reversed number by multiplying the current result by 10 and adding the digit.
4. Before each multiplication, check whether the result would overflow a 32-bit signed integer.
5. Restore the sign at the end.

### Why this works:
We reverse the number mathematically without converting to a string. The overflow check
`result > (INT_MAX - digit) // 10` ensures we never exceed the 32-bit boundary, satisfying
the constraint that we cannot use 64-bit storage."""
)

# 9: Palindrome Number (Easy)
_register(9,
    description="""<h3>9. Palindrome Number</h3>
<p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a
<strong>palindrome</strong>, and <code>false</code> otherwise.</p>
<p><strong>Follow up:</strong> Could you solve it without converting the integer to a string?</p>
<h4>Example 1:</h4>
<pre>Input: x = 121
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left it becomes 121-. Therefore it is not a palindrome.</pre>
<h4>Example 3:</h4>
<pre>Input: x = 10
Output: false</pre>
<h4>Constraints:</h4>
<ul><li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li></ul>""",
    function_name="isPalindrome",
    template="""class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"x": 121}, "expected": True},
        {"input": {"x": -121}, "expected": False},
        {"input": {"x": 10}, "expected": False},
        {"input": {"x": 0}, "expected": True},
        {"input": {"x": 12321}, "expected": True},
    ],
    solution="""class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10
""",
    explanation="""## Approach: Reverse Half the Number

**Time Complexity:** O(log₁₀(x))
**Space Complexity:** O(1)

### Steps:
1. Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes.
2. Reverse only the second half of the number by extracting digits.
3. Stop when the reversed half is greater than or equal to the remaining number.
4. Compare: for even-length numbers, `x == reversed_half`; for odd-length, `x == reversed_half // 10`.

### Why this works:
By only reversing half the digits, we avoid potential overflow issues and efficiently check
palindrome symmetry without converting to a string."""
)

# 13: Roman to Integer (Easy)
_register(13,
    description="""<h3>13. Roman to Integer</h3>
<p>Given a roman numeral, convert it to an integer.</p>
<p>Roman numerals are represented by seven symbols: I(1), V(5), X(10), L(50), C(100), D(500), M(1000).</p>
<p>When a smaller value appears before a larger value, it is subtracted (e.g., IV = 4, IX = 9).</p>
<h4>Example 1:</h4>
<pre>Input: s = "III"
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: s = "LVIII"
Output: 58</pre>
<h4>Example 3:</h4>
<pre>Input: s = "MCMXCIV"
Output: 1994</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= s.length &lt;= 15</code></li>
<li><code>s</code> contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')</li>
<li>It is guaranteed that <code>s</code> is a valid roman numeral in the range [1, 3999].</li>
</ul>""",
    function_name="romanToInt",
    template="""class Solution:
    def romanToInt(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "III"}, "expected": 3},
        {"input": {"s": "LVIII"}, "expected": 58},
        {"input": {"s": "MCMXCIV"}, "expected": 1994},
        {"input": {"s": "IV"}, "expected": 4},
        {"input": {"s": "IX"}, "expected": 9},
    ],
    solution="""class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result
""",
    explanation="""## Approach: Left-to-Right Pass with Subtraction Rule

**Time Complexity:** O(n), where n is the length of the string
**Space Complexity:** O(1)

### Steps:
1. Create a mapping of roman symbols to their integer values.
2. Iterate through the string from left to right.
3. If the current value is less than the next value, subtract it (subtractive notation like IV, IX).
4. Otherwise, add it to the result.

### Why this works:
The subtraction rule in Roman numerals only applies when a smaller value precedes a larger one.
By checking each character against its neighbor, we handle both additive and subtractive cases."""
)

# 26: Remove Duplicates from Sorted Array (Easy)
_register(26,
    description="""<h3>26. Remove Duplicates from Sorted Array</h3>
<p>Given an integer array <code>nums</code> sorted in non-decreasing order, remove the duplicates
<strong>in-place</strong> such that each unique element appears only once. The relative order of the
elements should be kept the same. Then return the number of unique elements in <code>nums</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
<li><code>nums</code> is sorted in non-decreasing order.</li>
</ul>""",
    function_name="removeDuplicates",
    template="""class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 1, 2]}, "expected": 2},
        {"input": {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]}, "expected": 5},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [1, 2, 3]}, "expected": 3},
    ],
    solution="""class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
""",
    explanation="""## Approach: Two Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Use a slow pointer starting at index 0 to track the position of the last unique element.
2. Use a fast pointer to scan through the array.
3. When `nums[fast] != nums[slow]`, increment slow and copy the new unique value.
4. Return `slow + 1` as the count of unique elements.

### Why this works:
Since the array is sorted, duplicates are adjacent. The slow pointer marks the boundary of unique
elements, and we only advance it when a new unique value is found."""
)

# 66: Plus One (Easy)
_register(66,
    description="""<h3>66. Plus One</h3>
<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>,
where each <code>digits[i]</code> is the i<sup>th</sup> digit of the integer. The digits are ordered
from most significant to least significant in left-to-right order. The large integer does not contain
any leading 0's.</p>
<p>Increment the large integer by one and return the resulting array of digits.</p>
<h4>Example 1:</h4>
<pre>Input: digits = [1,2,3]
Output: [1,2,4]</pre>
<h4>Example 2:</h4>
<pre>Input: digits = [4,3,2,1]
Output: [4,3,2,2]</pre>
<h4>Example 3:</h4>
<pre>Input: digits = [9]
Output: [1,0]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= digits.length &lt;= 100</code></li>
<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
<li><code>digits</code> does not contain any leading 0's.</li>
</ul>""",
    function_name="plusOne",
    template="""class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"digits": [1, 2, 3]}, "expected": [1, 2, 4]},
        {"input": {"digits": [4, 3, 2, 1]}, "expected": [4, 3, 2, 2]},
        {"input": {"digits": [9]}, "expected": [1, 0]},
        {"input": {"digits": [9, 9, 9]}, "expected": [1, 0, 0, 0]},
        {"input": {"digits": [0]}, "expected": [1]},
    ],
    solution="""class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
""",
    explanation="""## Approach: Right-to-Left Carry Propagation

**Time Complexity:** O(n)
**Space Complexity:** O(1) amortized (O(n) only when all digits are 9)

### Steps:
1. Start from the rightmost digit and move left.
2. If the current digit is less than 9, increment it and return immediately (no carry).
3. If it is 9, set it to 0 and continue to the next digit (carry).
4. If all digits were 9, prepend a 1 to the array.

### Why this works:
We only need to propagate a carry when a digit is 9. The moment we find a digit less than 9,
we can stop because there is no further carry."""
)

# 128: Longest Consecutive Sequence (Medium)
_register(128,
    description="""<h3>128. Longest Consecutive Sequence</h3>
<p>Given an unsorted array of integers <code>nums</code>, return the length of the longest
consecutive elements sequence.</p>
<p>You must write an algorithm that runs in <strong>O(n)</strong> time.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9</pre>
<h4>Constraints:</h4>
<ul>
<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>""",
    function_name="longestConsecutive",
    template="""class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [100, 4, 200, 1, 3, 2]}, "expected": 4},
        {"input": {"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}, "expected": 9},
        {"input": {"nums": []}, "expected": 0},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [1, 2, 0, 1]}, "expected": 3},
    ],
    solution="""class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
""",
    explanation="""## Approach: HashSet with Sequence Start Detection

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Put all numbers into a HashSet for O(1) lookups.
2. For each number, check if it is the start of a sequence (i.e., `num - 1` is not in the set).
3. If it is a start, count the length of the consecutive sequence by checking `num + 1`, `num + 2`, etc.
4. Track the maximum streak found.

### Why this works:
By only starting counts from sequence beginnings (numbers without a predecessor), each number
is visited at most twice total, giving us O(n) time despite the nested loop."""
)

# 169: Majority Element (Easy)
_register(169,
    description="""<h3>169. Majority Element</h3>
<p>Given an array <code>nums</code> of size <code>n</code>, return the <strong>majority element</strong>.</p>
<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times.
You may assume that the majority element always exists in the array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,2,3]
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [2,2,1,1,1,2,2]
Output: 2</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>""",
    function_name="majorityElement",
    template="""class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3, 2, 3]}, "expected": 3},
        {"input": {"nums": [2, 2, 1, 1, 1, 2, 2]}, "expected": 2},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [6, 5, 5]}, "expected": 5},
    ],
    solution="""class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
""",
    explanation="""## Approach: Boyer-Moore Voting Algorithm

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Initialize a candidate and a count of 0.
2. For each element: if count is 0, set the current element as the candidate.
3. Increment count if the element matches the candidate, decrement otherwise.
4. The candidate at the end is the majority element.

### Why this works:
The majority element appears more than n/2 times. Every time we "cancel" a non-majority
element against the majority, there are still more majority elements remaining. The last
candidate standing is guaranteed to be the majority."""
)

# 560: Subarray Sum Equals K (Medium)
_register(560,
    description="""<h3>560. Subarray Sum Equals K</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return the total
number of subarrays whose sum equals to <code>k</code>.</p>
<p>A subarray is a contiguous non-empty sequence of elements within an array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,1,1], k = 2
Output: 2</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,3], k = 3
Output: 2</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>""",
    function_name="subarraySum",
    template="""class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 1, 1], "k": 2}, "expected": 2},
        {"input": {"nums": [1, 2, 3], "k": 3}, "expected": 2},
        {"input": {"nums": [1], "k": 1}, "expected": 1},
        {"input": {"nums": [1, -1, 0], "k": 0}, "expected": 3},
    ],
    solution="""class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
        return count
""",
    explanation="""## Approach: Prefix Sum with HashMap

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Maintain a running prefix sum and a hashmap of prefix sum frequencies.
2. Initialize the map with `{0: 1}` to handle subarrays starting from index 0.
3. For each element, add it to the prefix sum.
4. Check if `prefix_sum - k` exists in the map; if so, those many subarrays ending here sum to k.
5. Update the prefix sum frequency in the map.

### Why this works:
If `prefix_sum[j] - prefix_sum[i] == k`, the subarray from `i+1` to `j` sums to k.
By storing prefix sum frequencies, we count all valid starting points in O(1) per element."""
)

# 1929: Concatenation of Array (Easy)
_register(1929,
    description="""<h3>1929. Concatenation of Array</h3>
<p>Given an integer array <code>nums</code> of length <code>n</code>, you want to create an array
<code>ans</code> of length <code>2n</code> where <code>ans[i] == nums[i]</code> and
<code>ans[i + n] == nums[i]</code> for <code>0 &lt;= i &lt; n</code> (0-indexed).</p>
<p>Specifically, <code>ans</code> is the <strong>concatenation</strong> of two <code>nums</code> arrays.</p>
<p>Return the array <code>ans</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 &lt;= n &lt;= 1000</code></li>
<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>""",
    function_name="getConcatenation",
    template="""class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 1]}, "expected": [1, 2, 1, 1, 2, 1]},
        {"input": {"nums": [1, 3, 2, 1]}, "expected": [1, 3, 2, 1, 1, 3, 2, 1]},
        {"input": {"nums": [1]}, "expected": [1, 1]},
    ],
    solution="""class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
""",
    explanation="""## Approach: Simple Concatenation

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Return `nums + nums` which creates a new list that is the concatenation of nums with itself.

### Why this works:
Python's list concatenation operator `+` creates a new list containing all elements of both
operands in order, which is exactly what the problem asks for."""
)

# 21: Merge Two Sorted Lists (Easy)
_register(21,
    description="""<h3>21. Merge Two Sorted Lists</h3>
<p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>
<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>
<p>Return the head of the merged linked list.</p>
<h4>Example 1:</h4>
<pre>Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]</pre>
<h4>Example 2:</h4>
<pre>Input: list1 = [], list2 = []
Output: []</pre>
<h4>Example 3:</h4>
<pre>Input: list1 = [], list2 = [0]
Output: [0]</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
<li>Both lists are sorted in non-decreasing order.</li>
</ul>""",
    function_name="mergeTwoLists",
    template="""# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: 'ListNode', list2: 'ListNode') -> 'ListNode':
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"list1": [1, 2, 4], "list2": [1, 3, 4]}, "expected": [1, 1, 2, 3, 4, 4]},
        {"input": {"list1": [], "list2": []}, "expected": []},
        {"input": {"list1": [], "list2": [0]}, "expected": [0]},
        {"input": {"list1": [1], "list2": [2]}, "expected": [1, 2]},
        {"input": {"list1": [1,3,5,7], "list2": [2,4,6,8]}, "expected": [1,2,3,4,5,6,7,8]},
    ],
    solution="""class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
""",
    explanation="""## Approach: Splice Nodes with a Dummy Head

**Time Complexity:** O(n + m) | **Space Complexity:** O(1) (no new nodes allocated)

### Steps:
1. Create a `dummy` node whose `.next` will be the head of the merged list; `tail` tracks the last spliced node.
2. While both lists have nodes, attach the one with the smaller value to `tail.next` and advance that list's pointer.
3. When one list runs out, splice the other's remaining tail wholesale onto `tail.next`.
4. Return `dummy.next`.

### Why this works:
Because both inputs are sorted, the smaller of the two front nodes is always the next correct node in the merged sequence. The dummy head removes the special case for picking the first node, and we re-use existing nodes (no allocations) — exactly what "splicing together the nodes" means in the problem.""",
    harness={"input": {"list1": "linked_list", "list2": "linked_list"}, "output": "linked_list"}
)

# 22: Generate Parentheses (Medium)
_register(22,
    description="""<h3>22. Generate Parentheses</h3>
<p>Given <code>n</code> pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.</p>
<h4>Example 1:</h4>
<pre>Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]</pre>
<h4>Example 2:</h4>
<pre>Input: n = 1
Output: ["()"]</pre>
<h4>Constraints:</h4>
<ul><li><code>1 &lt;= n &lt;= 8</code></li></ul>""",
    function_name="generateParenthesis",
    template="""class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 3}, "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"]},
        {"input": {"n": 1}, "expected": ["()"]},
        {"input": {"n": 2}, "expected": ["(())", "()()"]},
    ],
    solution="""class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        backtrack('', 0, 0)
        return result
""",
    explanation="""## Approach: Backtracking

**Time Complexity:** O(4^n / sqrt(n)) — the n-th Catalan number
**Space Complexity:** O(n) for recursion depth

### Steps:
1. Use backtracking to build valid parentheses strings character by character.
2. We can add an open parenthesis if we haven't used all n of them.
3. We can add a close parenthesis only if the number of close parens is less than open parens.
4. When the string reaches length 2n, it's a valid combination — add to results.

### Why this works:
The two constraints (open < n, close < open) ensure we only generate valid combinations.
We never have more closing parens than opening ones at any prefix, which is the definition
of well-formed parentheses."""
)

# 27: Remove Element (Easy)
_register(27,
    description="""<h3>27. Remove Element</h3>
<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences
of <code>val</code> in <code>nums</code> <strong>in-place</strong>. The order of the elements may
be changed. Then return the number of elements in <code>nums</code> which are not equal to <code>val</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>0 &lt;= nums.length &lt;= 100</code></li>
<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>""",
    function_name="removeElement",
    template="""class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3, 2, 2, 3], "val": 3}, "expected": 2},
        {"input": {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2}, "expected": 5},
        {"input": {"nums": [], "val": 0}, "expected": 0},
        {"input": {"nums": [1], "val": 1}, "expected": 0},
        {"input": {"nums": [1], "val": 2}, "expected": 1},
    ],
    solution="""class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
""",
    explanation="""## Approach: Two Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Use pointer `k` to track the position for the next non-val element.
2. Iterate through the array with pointer `i`.
3. If `nums[i] != val`, copy it to position `k` and increment `k`.
4. Return `k` as the count of remaining elements.

### Why this works:
We overwrite elements equal to `val` by shifting non-val elements forward. The first `k`
elements of the array will contain all non-val elements."""
)

# 31: Next Permutation (Medium)
_register(31,
    description="""<h3>31. Next Permutation</h3>
<p>A <strong>permutation</strong> of an array of integers is an arrangement of its members into a
sequence or linear order.</p>
<p>The <strong>next permutation</strong> of an array of integers is the next lexicographically
greater permutation of its integer. If the array is the last permutation, rearrange it as the
lowest possible order (sorted in ascending order).</p>
<p>The replacement must be <strong>in place</strong> and use only constant extra memory.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3]
Output: [1,3,2]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,2,1]
Output: [1,2,3]</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,1,5]
Output: [1,5,1]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 100</code></li>
<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>""",
    function_name="nextPermutation",
    template="""class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Write your solution here (modify nums in-place)
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3]}, "expected": [1, 3, 2]},
        {"input": {"nums": [3, 2, 1]}, "expected": [1, 2, 3]},
        {"input": {"nums": [1, 1, 5]}, "expected": [1, 5, 1]},
        {"input": {"nums": [1, 3, 2]}, "expected": [2, 1, 3]},
        {"input": {"nums": [1]}, "expected": [1]},
    ],
    solution="""class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # Step 2: Find the smallest element larger than nums[i] from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        # Step 4: Reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
""",
    explanation="""## Approach: Find Pivot and Swap

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. From the right, find the first index `i` where `nums[i] < nums[i+1]` (the pivot).
2. From the right, find the first index `j` where `nums[j] > nums[i]`.
3. Swap `nums[i]` and `nums[j]`.
4. Reverse the suffix starting at `i + 1`.
5. If no pivot exists (array is fully descending), just reverse the entire array.

### Why this works:
The suffix after the pivot is in descending order. By swapping the pivot with the smallest
larger element in the suffix and then reversing the suffix, we get the next lexicographically
greater permutation with minimal change."""
)

# 33: Search in Rotated Sorted Array (Medium)
_register(33,
    description="""<h3>33. Search in Rotated Sorted Array</h3>
<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong>
values). Prior to being passed to your function, <code>nums</code> is possibly rotated at an unknown
pivot index.</p>
<p>Given the array <code>nums</code> after the possible rotation and an integer <code>target</code>,
return the index of <code>target</code> if it is in <code>nums</code>, or <code>-1</code> if it is not.</p>
<p>You must write an algorithm with <strong>O(log n)</strong> runtime complexity.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1], target = 0
Output: -1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
<li>All values of <code>nums</code> are unique.</li>
<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>""",
    function_name="search",
    template="""class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, "expected": 4},
        {"input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3}, "expected": -1},
        {"input": {"nums": [1], "target": 0}, "expected": -1},
        {"input": {"nums": [1], "target": 1}, "expected": 0},
        {"input": {"nums": [3, 1], "target": 1}, "expected": 1},
    ],
    solution="""class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
""",
    explanation="""## Approach: Modified Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Steps:
1. Use standard binary search with left and right pointers.
2. At each step, determine which half is sorted by comparing `nums[left]` with `nums[mid]`.
3. If the left half is sorted and the target falls in that range, search left; otherwise search right.
4. If the right half is sorted and the target falls in that range, search right; otherwise search left.

### Why this works:
In a rotated sorted array, at least one half around the midpoint is always sorted. By identifying
the sorted half, we can determine whether the target lies in that range and eliminate half the
search space each iteration."""
)

# 34: Find First and Last Position of Element in Sorted Array (Medium)
_register(34,
    description="""<h3>34. Find First and Last Position of Element in Sorted Array</h3>
<p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting
and ending position of a given <code>target</code> value.</p>
<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>
<p>You must write an algorithm with <strong>O(log n)</strong> runtime complexity.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [], target = 0
Output: [-1,-1]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
<li><code>nums</code> is a non-decreasing array.</li>
<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>""",
    function_name="searchRange",
    template="""class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [5, 7, 7, 8, 8, 10], "target": 8}, "expected": [3, 4]},
        {"input": {"nums": [5, 7, 7, 8, 8, 10], "target": 6}, "expected": [-1, -1]},
        {"input": {"nums": [], "target": 0}, "expected": [-1, -1]},
        {"input": {"nums": [1], "target": 1}, "expected": [0, 0]},
    ],
    solution="""class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return [findLeft(nums, target), findRight(nums, target)]
""",
    explanation="""## Approach: Two Binary Searches

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Steps:
1. Perform binary search to find the leftmost (first) occurrence: when found, record and search left.
2. Perform binary search to find the rightmost (last) occurrence: when found, record and search right.
3. Return both positions.

### Why this works:
Standard binary search stops at any occurrence. By continuing to search in one direction after
finding the target, we find the boundary positions. Two O(log n) searches remain O(log n) overall."""
)

# 46: Permutations (Medium)
_register(46,
    description="""<h3>46. Permutations</h3>
<p>Given an array <code>nums</code> of distinct integers, return all the possible permutations.
You can return the answer in <strong>any order</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1]
Output: [[0,1],[1,0]]</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1]
Output: [[1]]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 6</code></li>
<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
<li>All the integers of <code>nums</code> are unique.</li>
</ul>""",
    function_name="permute",
    template="""class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3]}, "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]},
        {"input": {"nums": [0, 1]}, "expected": [[0, 1], [1, 0]]},
        {"input": {"nums": [1]}, "expected": [[1]]},
    ],
    solution="""class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(current, remaining):
            if not remaining:
                result.append(current[:])
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()
        backtrack([], nums)
        return result
""",
    explanation="""## Approach: Backtracking

**Time Complexity:** O(n! * n)
**Space Complexity:** O(n) for recursion depth

### Steps:
1. Use backtracking with a current permutation and remaining elements.
2. At each level, try each remaining element as the next choice.
3. Add it to the current permutation, recurse with the remaining elements, then backtrack.
4. When no elements remain, we have a complete permutation — add a copy to results.

### Why this works:
By systematically trying each unused element at each position and backtracking, we explore
all n! possible orderings without repetition."""
)

# 51: N-Queens (Hard)
_register(51,
    description="""<h3>51. N-Queens</h3>
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an
<code>n x n</code> chessboard such that no two queens attack each other.</p>
<p>Given an integer <code>n</code>, return <em>all distinct solutions to the n-queens puzzle</em>.
Each solution contains a distinct board configuration of the n-queens' placement, where <code>'Q'</code>
and <code>'.'</code> both indicate a queen and an empty space, respectively.</p>
<h4>Example 1:</h4>
<pre>Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]</pre>
<h4>Example 2:</h4>
<pre>Input: n = 1
Output: [["Q"]]</pre>
<h4>Constraints:</h4>
<ul><li><code>1 &lt;= n &lt;= 9</code></li></ul>""",
    function_name="solveNQueens",
    template="""class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 4}, "expected": [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]},
        {"input": {"n": 1}, "expected": [["Q"]]},
        {"input": {"n": 2}, "expected": []},
        {"input": {"n": 3}, "expected": []},
    ],
    solution="""class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result
""",
    explanation="""## Approach: Backtracking with Constraint Sets

**Time Complexity:** O(n!)
**Space Complexity:** O(n^2) for the board

### Steps:
1. Place queens row by row using backtracking.
2. Track occupied columns and both diagonals using sets.
3. For each row, try each column. Skip if the column or either diagonal is occupied.
4. Place the queen, recurse to the next row, then backtrack.
5. When all rows are filled, record the board configuration.

### Why this works:
By placing one queen per row and tracking constraints via sets, we efficiently prune invalid
placements. The diagonal constraints use `row - col` (anti-diagonal) and `row + col` (main diagonal)
as unique identifiers for each diagonal line."""
)

# 54: Spiral Matrix (Medium)
_register(54,
    description="""<h3>54. Spiral Matrix</h3>
<p>Given an <code>m x n</code> <code>matrix</code>, return all elements of the <code>matrix</code>
in spiral order.</p>
<h4>Example 1:</h4>
<pre>Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]</pre>
<h4>Example 2:</h4>
<pre>Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 &lt;= m, n &lt;= 10</code></li>
<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>""",
    function_name="spiralOrder",
    template="""class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5]},
        {"input": {"matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]}, "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]},
        {"input": {"matrix": [[1]]}, "expected": [1]},
        {"input": {"matrix": [[1, 2], [3, 4]]}, "expected": [1, 2, 4, 3]},
    ],
    solution="""class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result
""",
    explanation="""## Approach: Layer-by-Layer Simulation

**Time Complexity:** O(m * n)
**Space Complexity:** O(1) excluding the output

### Steps:
1. Maintain four boundaries: top, bottom, left, right.
2. Traverse right along the top row, then shrink top.
3. Traverse down along the right column, then shrink right.
4. If rows remain, traverse left along the bottom row, then shrink bottom.
5. If columns remain, traverse up along the left column, then shrink left.
6. Repeat until all elements are visited.

### Why this works:
We peel off one layer of the matrix at a time in spiral order. The boundary checks
prevent double-counting when the matrix is not square."""
)

# 67: Add Binary (Easy)
_register(67,
    description="""<h3>67. Add Binary</h3>
<p>Given two binary strings <code>a</code> and <code>b</code>, return their sum as a binary string.</p>
<h4>Example 1:</h4>
<pre>Input: a = "11", b = "1"
Output: "100"</pre>
<h4>Example 2:</h4>
<pre>Input: a = "1010", b = "1011"
Output: "10101"</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
<li><code>a</code> and <code>b</code> consist only of '0' or '1' characters.</li>
<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>""",
    function_name="addBinary",
    template="""class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"a": "11", "b": "1"}, "expected": "100"},
        {"input": {"a": "1010", "b": "1011"}, "expected": "10101"},
        {"input": {"a": "0", "b": "0"}, "expected": "0"},
        {"input": {"a": "1", "b": "111"}, "expected": "1000"},
    ],
    solution="""class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))
""",
    explanation="""## Approach: Digit-by-Digit Addition with Carry

**Time Complexity:** O(max(m, n)), where m and n are the lengths of a and b
**Space Complexity:** O(max(m, n)) for the result

### Steps:
1. Start from the rightmost digits of both strings.
2. Add corresponding digits along with the carry.
3. The current digit is `total % 2`, and the new carry is `total // 2`.
4. Continue until both strings are exhausted and there is no carry.
5. Reverse the result since we built it from least significant to most significant.

### Why this works:
This simulates the standard binary addition algorithm, processing digits from right to left
and propagating carries, just like adding numbers by hand."""
)

# 72: Edit Distance (Medium)
_register(72,
    description="""<h3>72. Edit Distance</h3>
<p>Given two strings <code>word1</code> and <code>word2</code>, return the minimum number of
operations required to convert <code>word1</code> to <code>word2</code>.</p>
<p>You have the following three operations permitted on a word:</p>
<ul>
<li>Insert a character</li>
<li>Delete a character</li>
<li>Replace a character</li>
</ul>
<h4>Example 1:</h4>
<pre>Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse -> rose -> ros</pre>
<h4>Example 2:</h4>
<pre>Input: word1 = "intention", word2 = "execution"
Output: 5</pre>
<h4>Constraints:</h4>
<ul>
<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>""",
    function_name="minDistance",
    template="""class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"word1": "horse", "word2": "ros"}, "expected": 3},
        {"input": {"word1": "intention", "word2": "execution"}, "expected": 5},
        {"input": {"word1": "", "word2": "abc"}, "expected": 3},
        {"input": {"word1": "abc", "word2": ""}, "expected": 3},
        {"input": {"word1": "", "word2": ""}, "expected": 0},
    ],
    solution="""class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete
                        dp[i][j - 1],      # insert
                        dp[i - 1][j - 1]   # replace
                    )
        return dp[m][n]
""",
    explanation="""## Approach: Dynamic Programming (2D Table)

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

### Steps:
1. Create a DP table where `dp[i][j]` = min operations to convert `word1[:i]` to `word2[:j]`.
2. Base cases: converting empty string to length-j string costs j insertions, and vice versa.
3. If characters match (`word1[i-1] == word2[j-1]`), no operation needed: `dp[i][j] = dp[i-1][j-1]`.
4. Otherwise, take the minimum of insert (`dp[i][j-1]`), delete (`dp[i-1][j]`), or replace (`dp[i-1][j-1]`), plus 1.

### Why this works:
Each cell represents the optimal edit distance for a subproblem. By building up from smaller
subproblems, we guarantee the global optimum via the principle of optimal substructure."""
)

# 78: Subsets (Medium)
_register(78,
    description="""<h3>78. Subsets</h3>
<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return all possible
subsets (the power set).</p>
<p>The solution set must not contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0]
Output: [[],[0]]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 10</code></li>
<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
<li>All the numbers of <code>nums</code> are unique.</li>
</ul>""",
    function_name="subsets",
    template="""class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3]}, "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]},
        {"input": {"nums": [0]}, "expected": [[], [0]]},
        {"input": {"nums": [1, 2]}, "expected": [[], [1], [2], [1, 2]]},
    ],
    solution="""class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
""",
    explanation="""## Approach: Iterative Expansion

**Time Complexity:** O(n * 2^n)
**Space Complexity:** O(n * 2^n) for storing all subsets

### Steps:
1. Start with the empty subset `[[]]`.
2. For each number in nums, take every existing subset and create a new subset by adding the number.
3. Add all new subsets to the result.
4. After processing all numbers, result contains all 2^n subsets.

### Why this works:
Each element has two choices: included or not. By iteratively doubling the subsets (once with
the new element, once without), we systematically generate the full power set."""
)

# 84: Largest Rectangle in Histogram (Hard)
_register(84,
    description="""<h3>84. Largest Rectangle in Histogram</h3>
<p>Given an array of integers <code>heights</code> representing the histogram's bar height where the
width of each bar is <code>1</code>, return the area of the largest rectangle in the histogram.</p>
<h4>Example 1:</h4>
<pre>Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area = 10 units (from heights[2] and heights[3]).</pre>
<h4>Example 2:</h4>
<pre>Input: heights = [2,4]
Output: 4</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    function_name="largestRectangleArea",
    template="""class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"heights": [2, 1, 5, 6, 2, 3]}, "expected": 10},
        {"input": {"heights": [2, 4]}, "expected": 4},
        {"input": {"heights": [1]}, "expected": 1},
        {"input": {"heights": [2, 1, 2]}, "expected": 3},
        {"input": {"heights": [0]}, "expected": 0},
    ],
    solution="""class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area
""",
    explanation="""## Approach: Monotonic Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Maintain a stack of (index, height) pairs in increasing height order.
2. For each bar, while the stack top is taller, pop it and calculate the area it can form.
3. The width extends from the popped bar's index to the current index.
4. Push the current bar with the earliest valid start index.
5. After processing all bars, calculate areas for remaining stack entries (they extend to the end).

### Why this works:
A monotonic increasing stack tracks potential left boundaries. When we encounter a shorter bar,
all taller bars in the stack can no longer extend right, so we finalize their areas. Each bar
is pushed and popped at most once, giving O(n) time."""
)

# 85: Maximal Rectangle (Hard)
_register(85,
    description="""<h3>85. Maximal Rectangle</h3>
<p>Given a <code>rows x cols</code> binary matrix filled with <code>'0'</code>s and <code>'1'</code>s,
find the largest rectangle containing only <code>'1'</code>s and return its area.</p>
<h4>Example 1:</h4>
<pre>Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6</pre>
<h4>Example 2:</h4>
<pre>Input: matrix = [["0"]]
Output: 0</pre>
<h4>Example 3:</h4>
<pre>Input: matrix = [["1"]]
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>rows == matrix.length</code></li>
<li><code>cols == matrix[i].length</code></li>
<li><code>1 &lt;= rows, cols &lt;= 200</code></li>
<li><code>matrix[i][j]</code> is '0' or '1'.</li>
</ul>""",
    function_name="maximalRectangle",
    template="""class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"matrix": [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]}, "expected": 6},
        {"input": {"matrix": [["0"]]}, "expected": 0},
        {"input": {"matrix": [["1"]]}, "expected": 1},
        {"input": {"matrix": [["0", "0"]]}, "expected": 0},
    ],
    solution="""class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            # Apply largest rectangle in histogram
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    max_area = max(max_area, height * (i - idx))
                    start = idx
                stack.append((start, h))
            for idx, height in stack:
                max_area = max(max_area, height * (cols - idx))
        return max_area
""",
    explanation="""## Approach: Histogram per Row + Monotonic Stack

**Time Complexity:** O(rows * cols)
**Space Complexity:** O(cols)

### Steps:
1. Build a histogram of heights for each row: if `matrix[r][c] == '1'`, height increases by 1; otherwise resets to 0.
2. For each row's histogram, apply the "Largest Rectangle in Histogram" algorithm (problem 84).
3. Track the maximum area across all rows.

### Why this works:
Each row can be viewed as the base of a histogram where the bar heights represent consecutive
1s above. The largest rectangle in any of these histograms is the answer. This reduces a 2D
problem to repeated 1D histogram problems."""
)

# 88: Merge Sorted Array (Easy)
_register(88,
    description="""<h3>88. Merge Sorted Array</h3>
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in non-decreasing
order, and two integers <code>m</code> and <code>n</code>, representing the number of elements in
<code>nums1</code> and <code>nums2</code> respectively.</p>
<p>Merge <code>nums2</code> into <code>nums1</code> as one sorted array.</p>
<p>The final sorted array should not be returned by the function, but instead be stored inside the
array <code>nums1</code>. To accommodate this, <code>nums1</code> has a length of <code>m + n</code>,
where the last <code>n</code> elements are set to 0 and should be ignored.</p>
<h4>Example 1:</h4>
<pre>Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]</pre>
<h4>Example 2:</h4>
<pre>Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>nums1.length == m + n</code></li>
<li><code>nums2.length == n</code></li>
<li><code>0 &lt;= m, n &lt;= 200</code></li>
</ul>""",
    function_name="merge",
    template="""class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Write your solution here (modify nums1 in-place)
        pass
""",
    test_cases=[
        {"input": {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}, "expected": [1, 2, 2, 3, 5, 6]},
        {"input": {"nums1": [1], "m": 1, "nums2": [], "n": 0}, "expected": [1]},
        {"input": {"nums1": [0], "m": 0, "nums2": [1], "n": 1}, "expected": [1]},
        {"input": {"nums1": [4, 5, 6, 0, 0, 0], "m": 3, "nums2": [1, 2, 3], "n": 3}, "expected": [1, 2, 3, 4, 5, 6]},
    ],
    solution="""class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
""",
    explanation="""## Approach: Three Pointers from the End

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

### Steps:
1. Start three pointers at the end: `p1` at the last real element of nums1, `p2` at the end of nums2, `p` at the end of nums1's total space.
2. Compare elements at `p1` and `p2`; place the larger one at position `p`.
3. Decrement the appropriate pointers.
4. Continue until all of nums2 is placed.

### Why this works:
By filling from the back, we avoid overwriting elements in nums1 that haven't been processed
yet. The extra space at the end of nums1 is exactly enough to accommodate the merge."""
)

# 125: Valid Palindrome (Easy)
_register(125,
    description="""<h3>125. Valid Palindrome</h3>
<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.</p>
<p>Given a string <code>s</code>, return <code>true</code> if it is a palindrome, or <code>false</code> otherwise.</p>
<h4>Example 1:</h4>
<pre>Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.</pre>
<h4>Example 2:</h4>
<pre>Input: s = "race a car"
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: s = " "
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>""",
    function_name="isPalindrome",
    template="""class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "A man, a plan, a canal: Panama"}, "expected": True},
        {"input": {"s": "race a car"}, "expected": False},
        {"input": {"s": " "}, "expected": True},
        {"input": {"s": "0P"}, "expected": False},
    ],
    solution="""class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
""",
    explanation="""## Approach: Two Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Use two pointers at the start and end of the string.
2. Skip non-alphanumeric characters from both ends.
3. Compare characters (case-insensitive) at the two pointers.
4. If any mismatch is found, return False.
5. If the pointers cross without mismatch, return True.

### Why this works:
By skipping non-alphanumeric characters and comparing case-insensitively, we check only the
relevant characters. Two pointers meeting in the middle confirms the palindrome property."""
)

# 136: Single Number (Easy)
_register(136,
    description="""<h3>136. Single Number</h3>
<p>Given a <strong>non-empty</strong> array of integers <code>nums</code>, every element appears
<em>twice</em> except for one. Find that single one.</p>
<p>You must implement a solution with a linear runtime complexity and use only constant extra space.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,2,1]
Output: 1</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [4,1,2,1,2]
Output: 4</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1]
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>""",
    function_name="singleNumber",
    template="""class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2, 2, 1]}, "expected": 1},
        {"input": {"nums": [4, 1, 2, 1, 2]}, "expected": 4},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [0, 1, 0]}, "expected": 1},
    ],
    solution="""class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
""",
    explanation="""## Approach: Bit Manipulation (XOR)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Initialize result to 0.
2. XOR every number in the array with the result.
3. Return the final result.

### Why this works:
XOR has these properties: `a ^ a = 0` and `a ^ 0 = a`. Since every number except one appears
twice, all pairs cancel out to 0, leaving only the single number."""
)

# 160: Intersection of Two Linked Lists (Easy)
_register(160,
    description="""<h3>160. Intersection of Two Linked Lists</h3>
<p>Given the heads of two singly linked-lists <code>headA</code> and <code>headB</code>, return the
node at which the two lists intersect. If the two linked lists have no intersection, return null.</p>
<p><em>Note: For this practice environment, linked lists are represented as plain Python lists.
Return the index where they start sharing elements, or -1 if no intersection.</em></p>
<h4>Example 1:</h4>
<pre>Input: headA = [4,1,8,4,5], headB = [5,6,1,8,4,5], shared_start_a = 2, shared_start_b = 3
Output: 2
Explanation: The intersected node's value is 8, at index 2 in listA.</pre>
<h4>Example 2:</h4>
<pre>Input: headA = [2,6,4], headB = [1,5], shared_start_a = -1, shared_start_b = -1
Output: -1
Explanation: The two lists do not intersect.</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes of listA is in the m.</li>
<li>The number of nodes of listB is in the n.</li>
<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
</ul>""",
    function_name="getIntersectionNode",
    template="""class Solution:
    def getIntersectionNode(self, headA: list[int], headB: list[int]) -> int:
        # Return the index in headA where intersection starts, or -1
        # Two lists intersect if their tails are identical
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"headA": [4, 1, 8, 4, 5], "headB": [5, 6, 1, 8, 4, 5]}, "expected": 2},
        {"input": {"headA": [2, 6, 4], "headB": [1, 5]}, "expected": -1},
        {"input": {"headA": [1, 2, 3], "headB": [1, 2, 3]}, "expected": 0},
        {"input": {"headA": [1], "headB": [1]}, "expected": 0},
    ],
    solution="""class Solution:
    def getIntersectionNode(self, headA: list[int], headB: list[int]) -> int:
        # Find intersection by comparing tails
        lenA, lenB = len(headA), len(headB)
        # Check if tails match (lists must share a common suffix to intersect)
        min_len = min(lenA, lenB)
        if min_len == 0:
            return -1
        # Find the longest common suffix
        intersection_idx = -1
        for i in range(1, min_len + 1):
            if headA[lenA - i] == headB[lenB - i]:
                intersection_idx = lenA - i
            else:
                break
        return intersection_idx
""",
    explanation="""## Approach: Common Suffix Detection

**Time Complexity:** O(min(m, n))
**Space Complexity:** O(1)

### Steps:
1. Compare elements from the end of both lists moving backward.
2. As long as elements match, they are part of the shared intersection.
3. When they stop matching, the last matching index in headA is the intersection start.
4. If no elements match at the tail, return -1.

### Why this works:
In the list-based representation, two linked lists that intersect share a common suffix.
By comparing from the end, we find where the shared portion begins."""
)

# 162: Find Peak Element (Medium)
_register(162,
    description="""<h3>162. Find Peak Element</h3>
<p>A peak element is an element that is strictly greater than its neighbors.</p>
<p>Given a 0-indexed integer array <code>nums</code>, find a peak element, and return its index. If
the array contains multiple peaks, return the index to <strong>any</strong> of the peaks.</p>
<p>You may imagine that <code>nums[-1] = nums[n] = -infinity</code>.</p>
<p>You must write an algorithm that runs in <strong>O(log n)</strong> time.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
<li><code>nums[i] != nums[i + 1]</code> for all valid <code>i</code>.</li>
</ul>""",
    function_name="findPeakElement",
    template="""class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3, 1]}, "expected": 2},
        {"input": {"nums": [1]}, "expected": 0},
        {"input": {"nums": [1, 2]}, "expected": 1},
        {"input": {"nums": [2, 1]}, "expected": 0},
    ],
    solution="""class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
""",
    explanation="""## Approach: Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

### Steps:
1. Use binary search with left and right pointers.
2. Compare `nums[mid]` with `nums[mid + 1]`.
3. If `nums[mid] > nums[mid + 1]`, the peak is at mid or to the left, so move right to mid.
4. Otherwise, the peak is to the right, so move left to mid + 1.
5. When left == right, we've found a peak.

### Why this works:
Since `nums[-1] = nums[n] = -infinity`, there's always a peak. If `nums[mid] < nums[mid+1]`,
the increasing direction guarantees a peak exists on the right side (it must eventually decrease).
This allows binary search to converge on a peak in O(log n)."""
)

# 167: Two Sum II - Input Array Is Sorted (Medium)
_register(167,
    description="""<h3>167. Two Sum II - Input Array Is Sorted</h3>
<p>Given a <strong>1-indexed</strong> array of integers <code>numbers</code> that is already sorted
in non-decreasing order, find two numbers such that they add up to a specific <code>target</code>
number.</p>
<p>Return the indices of the two numbers, <strong>index1</strong> and <strong>index2</strong>,
<em>added by one</em> as an integer array <code>[index1, index2]</code> of length 2.</p>
<p>You may not use the same element twice. Your solution must use only constant extra space.</p>
<h4>Example 1:</h4>
<pre>Input: numbers = [2,7,11,15], target = 9
Output: [1,2]</pre>
<h4>Example 2:</h4>
<pre>Input: numbers = [2,3,4], target = 6
Output: [1,3]</pre>
<h4>Example 3:</h4>
<pre>Input: numbers = [-1,0], target = -1
Output: [1,2]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
<li>numbers is sorted in non-decreasing order.</li>
<li>It is guaranteed that there is exactly one solution.</li>
</ul>""",
    function_name="twoSum",
    template="""class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"numbers": [2, 7, 11, 15], "target": 9}, "expected": [1, 2]},
        {"input": {"numbers": [2, 3, 4], "target": 6}, "expected": [1, 3]},
        {"input": {"numbers": [-1, 0], "target": -1}, "expected": [1, 2]},
        {"input": {"numbers": [1, 2, 3, 4, 4, 9, 56, 90], "target": 8}, "expected": [4, 5]},
    ],
    solution="""class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
""",
    explanation="""## Approach: Two Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Place one pointer at the start and one at the end of the sorted array.
2. Compute the sum of the two pointed elements.
3. If the sum equals the target, return the 1-indexed positions.
4. If the sum is too small, move the left pointer right to increase the sum.
5. If the sum is too large, move the right pointer left to decrease the sum.

### Why this works:
Since the array is sorted, moving the left pointer right increases the sum and moving the
right pointer left decreases it. This guarantees we find the unique solution in one pass."""
)

# 175: SQL problem, skipped

# 189: Rotate Array (Medium)
_register(189,
    description="""<h3>189. Rotate Array</h3>
<p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps,
where <code>k</code> is non-negative.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>""",
    function_name="rotate",
    template="""class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # Write your solution here (modify nums in-place)
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}, "expected": [5, 6, 7, 1, 2, 3, 4]},
        {"input": {"nums": [-1, -100, 3, 99], "k": 2}, "expected": [3, 99, -1, -100]},
        {"input": {"nums": [1, 2], "k": 3}, "expected": [2, 1]},
        {"input": {"nums": [1], "k": 0}, "expected": [1]},
    ],
    solution="""class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
""",
    explanation="""## Approach: Three Reversals

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Normalize k by taking `k % n` to handle k larger than the array length.
2. Reverse the entire array.
3. Reverse the first k elements.
4. Reverse the remaining n-k elements.

### Why this works:
Reversing the entire array puts the last k elements at the front (but reversed). Then
reversing each segment restores the correct order within each part. For example:
`[1,2,3,4,5,6,7]` -> reverse all: `[7,6,5,4,3,2,1]` -> reverse first 3: `[5,6,7,4,3,2,1]`
-> reverse last 4: `[5,6,7,1,2,3,4]`."""
)

# 198: House Robber (Medium)
_register(198,
    description="""<h3>198. House Robber</h3>
<p>You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent
houses have security systems connected and <strong>it will automatically contact the police if two
adjacent houses were broken into on the same night</strong>.</p>
<p>Given an integer array <code>nums</code> representing the amount of money of each house, return
the maximum amount of money you can rob tonight <strong>without alerting the police</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total = 2 + 9 + 1 = 12.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 100</code></li>
<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>""",
    function_name="rob",
    template="""class Solution:
    def rob(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3, 1]}, "expected": 4},
        {"input": {"nums": [2, 7, 9, 3, 1]}, "expected": 12},
        {"input": {"nums": [0]}, "expected": 0},
        {"input": {"nums": [2, 1]}, "expected": 2},
        {"input": {"nums": [1, 3, 1, 3, 100]}, "expected": 103},
    ],
    solution="""class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2 = 0
        prev1 = 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1
""",
    explanation="""## Approach: Dynamic Programming with Space Optimization

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Steps:
1. Track two variables: `prev1` (max money including up to the previous house) and `prev2` (max money up to two houses back).
2. For each house, decide: either skip it (take `prev1`) or rob it (take `prev2 + current house value`).
3. Update the variables and move forward.

### Why this works:
At each house, the optimal decision depends only on the last two states: rob the current house
plus the best from two houses ago, or skip it and keep the best from one house ago. This is
the classic DP recurrence `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` optimized to O(1) space."""
)

# 202: Happy Number (Easy)
_register(202,
    description="""<h3>202. Happy Number</h3>
<p>Write an algorithm to determine if a number <code>n</code> is happy.</p>
<p>A <strong>happy number</strong> is a number defined by the following process:</p>
<ul>
<li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
<li>Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.</li>
<li>Those numbers for which this process ends in 1 are happy.</li>
</ul>
<p>Return <code>true</code> if <code>n</code> is a happy number, and <code>false</code> if not.</p>
<h4>Example 1:</h4>
<pre>Input: n = 19
Output: true
Explanation: 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1</pre>
<h4>Example 2:</h4>
<pre>Input: n = 2
Output: false</pre>
<h4>Constraints:</h4>
<ul><li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li></ul>""",
    function_name="isHappy",
    template="""class Solution:
    def isHappy(self, n: int) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 19}, "expected": True},
        {"input": {"n": 2}, "expected": False},
        {"input": {"n": 1}, "expected": True},
        {"input": {"n": 7}, "expected": True},
        {"input": {"n": 4}, "expected": False},
    ],
    solution="""class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
""",
    explanation="""## Approach: HashSet Cycle Detection

**Time Complexity:** O(log n) per step, bounded number of steps
**Space Complexity:** O(log n) for the set

### Steps:
1. Compute the sum of squares of digits to get the next number.
2. Track all seen numbers in a set.
3. If we reach 1, the number is happy.
4. If we see a repeated number, there's a cycle — the number is not happy.

### Why this works:
The sequence of digit-square sums either reaches 1 or enters a cycle. By detecting the cycle
with a set, we can determine which case we're in. (Alternatively, Floyd's cycle detection
with slow/fast pointers works with O(1) space.)"""
)

# 215: Kth Largest Element in an Array (Medium)
_register(215,
    description="""<h3>215. Kth Largest Element in an Array</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the
<code>k<sup>th</sup></code> largest element in the array.</p>
<p>Note that it is the k<sup>th</sup> largest element in the sorted order, not the k<sup>th</sup>
distinct element.</p>
<p>Can you solve it without sorting?</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,2,1,5,6,4], k = 2
Output: 5</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    function_name="findKthLargest",
    template="""class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3, 2, 1, 5, 6, 4], "k": 2}, "expected": 5},
        {"input": {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4}, "expected": 4},
        {"input": {"nums": [1], "k": 1}, "expected": 1},
        {"input": {"nums": [2, 1], "k": 2}, "expected": 1},
    ],
    solution="""class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]
""",
    explanation="""## Approach: Min-Heap of Size K

**Time Complexity:** O(n log k)
**Space Complexity:** O(k)

### Steps:
1. Use Python's `heapq.nlargest(k, nums)` to find the k largest elements.
2. Return the last (smallest) of those k elements, which is the kth largest overall.

### Why this works:
`heapq.nlargest` internally maintains a min-heap of size k, efficiently tracking the k largest
elements seen so far. The smallest element in this heap is the kth largest element. An alternative
approach is Quickselect with O(n) average time."""
)

# 217: Contains Duplicate (Easy)
_register(217,
    description="""<h3>217. Contains Duplicate</h3>
<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears
<strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,1]
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,3,4]
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>""",
    function_name="containsDuplicate",
    template="""class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3, 1]}, "expected": True},
        {"input": {"nums": [1, 2, 3, 4]}, "expected": False},
        {"input": {"nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]}, "expected": True},
        {"input": {"nums": [1]}, "expected": False},
    ],
    solution="""class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
""",
    explanation="""## Approach: HashSet

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Convert the array to a set, which removes duplicates.
2. Compare the length of the set with the original array.
3. If they differ, duplicates exist.

### Why this works:
A set only contains unique elements. If the set is smaller than the array, at least one
element appeared more than once. This is the most Pythonic and efficient approach."""
)

# 219: Contains Duplicate II (Easy)
_register(219,
    description="""<h3>219. Contains Duplicate II</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code>
if there are two <strong>distinct</strong> indices <code>i</code> and <code>j</code> in the array
such that <code>nums[i] == nums[j]</code> and <code>abs(i - j) &lt;= k</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,1], k = 3
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,0,1,1], k = 1
Output: true</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,2,3,1,2,3], k = 2
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>""",
    function_name="containsNearbyDuplicate",
    template="""class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 3, 1], "k": 3}, "expected": True},
        {"input": {"nums": [1, 0, 1, 1], "k": 1}, "expected": True},
        {"input": {"nums": [1, 2, 3, 1, 2, 3], "k": 2}, "expected": False},
        {"input": {"nums": [1], "k": 1}, "expected": False},
        {"input": {"nums": [1, 2, 1], "k": 0}, "expected": False},
    ],
    solution="""class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
""",
    explanation="""## Approach: HashMap (Last Seen Index)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### Steps:
1. Use a dictionary to store the most recent index of each value.
2. For each element, check if it was seen before and if the distance to its last occurrence is at most k.
3. If so, return True.
4. Update the stored index to the current position.

### Why this works:
We only need to check the most recent occurrence of each value because if an older occurrence
was within k distance, we would have already found it. Storing just the last index keeps the
solution simple and efficient."""
)
