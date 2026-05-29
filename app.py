import csv
import json
import subprocess
import sys
import tempfile
import os
import textwrap
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load questions from CSV
QUESTIONS = []
def load_questions():
    global QUESTIONS
    csv_path = os.path.join(os.path.dirname(__file__), 'three-months.csv')
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            QUESTIONS.append({
                'id': int(row['ID']),
                'url': row['URL'],
                'title': row['Title'],
                'difficulty': row['Difficulty'],
                'acceptance': row['Acceptance %'],
                'frequency': row['Frequency %'],
            })

load_questions()

# User solutions storage
USER_SOLUTIONS_PATH = os.path.join(os.path.dirname(__file__), 'user_solutions.json')

def load_user_solutions():
    if os.path.exists(USER_SOLUTIONS_PATH):
        with open(USER_SOLUTIONS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_user_solutions(solutions):
    with open(USER_SOLUTIONS_PATH, 'w', encoding='utf-8') as f:
        json.dump(solutions, f, indent=2)

SOLVED_PROBLEMS_PATH = os.path.join(os.path.dirname(__file__), 'solved_problems.json')

def load_solved():
    if os.path.exists(SOLVED_PROBLEMS_PATH):
        with open(SOLVED_PROBLEMS_PATH, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_solved(solved):
    with open(SOLVED_PROBLEMS_PATH, 'w', encoding='utf-8') as f:
        json.dump(sorted(solved), f, indent=2)

# LeetCode 75 study plan (https://leetcode.com/studyplan/leetcode-75/)
LC75_IDS = {
    1768, 1071, 1431, 605, 345, 151, 238, 334, 443,
    283, 392, 11, 1679,
    643, 1456, 1004, 1493,
    1732, 724,
    2215, 1207, 1657, 2352,
    2390, 735, 394,
    933, 649,
    2095, 328, 206, 2130,
    104, 872, 1448, 437, 1372, 236,
    199, 1161,
    700, 450,
    841, 547, 1466, 399,
    1926, 994,
    215, 2336, 2542, 2462,
    374, 2300, 162, 875,
    17, 216,
    1137, 746, 198, 790,
    62, 1143, 714, 72,
    338, 136, 1318,
    208, 1268,
    435, 452,
    739, 901,
}

# Problem bank: test cases + solution + description for known problems
# We pre-populate the most common ones; the frontend can request more via API
PROBLEM_BANK = {}

def _register(lid, description, function_name, template, test_cases, solution, explanation, follow_ups=None, harness=None):
    """Register a problem with its metadata.

    harness (optional) lets the runner transform inputs/outputs around the user's call:
        {"input": {"head": "linked_list"}, "output": "linked_list"}
    Supported transforms: "linked_list" (list <-> ListNode chain).
    """
    PROBLEM_BANK[lid] = {
        'description': description,
        'function_name': function_name,
        'template': template,
        'test_cases': test_cases,
        'solution': solution,
        'explanation': explanation,
        'follow_ups': follow_ups or [],
        'harness': harness,
    }

# --- Problem definitions ---

_register(1,
    description="""<h3>Two Sum</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers</em> such that they add up to <code>target</code>.</p>
<p>You may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice.</p>
<p>You can return the answer in any order.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,2,4], target = 6
Output: [1,2]</pre>
<h4>Constraints:</h4>
<ul>
<li>2 &le; nums.length &le; 10<sup>4</sup></li>
<li>-10<sup>9</sup> &le; nums[i] &le; 10<sup>9</sup></li>
<li>-10<sup>9</sup> &le; target &le; 10<sup>9</sup></li>
<li>Only one valid answer exists.</li>
</ul>""",
    function_name="twoSum",
    template="""class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,7,11,15], "target": 9}, "expected": [0,1]},
        {"input": {"nums": [3,2,4], "target": 6}, "expected": [1,2]},
        {"input": {"nums": [3,3], "target": 6}, "expected": [0,1]},
        {"input": {"nums": [1,5,3,7,2], "target": 9}, "expected": [3,4]},
    ],
    solution="""class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
""",
    explanation="""**Approach: Hash Map (One Pass)**

**Time:** O(n) | **Space:** O(n)

1. Create a hash map to store each number and its index as we iterate.
2. For each number, compute `complement = target - num`.
3. If the complement is already in the hash map, we found our pair — return both indices.
4. Otherwise, store the current number and index in the hash map.

**Why this works:** Instead of checking every pair (O(n²)), we use a hash map for O(1) lookups, reducing the problem to a single pass through the array.
""",
    follow_ups=[
        {"type": "interview", "question": "What if the array is already sorted? Can you do better than O(n) space?", "hint": "Use two pointers from both ends — O(1) space. See problem 167."},
        {"type": "interview", "question": "What if you need to return all pairs, not just one?", "hint": "Use a hash map but collect all matches instead of returning early."},
        {"type": "interview", "question": "What if duplicates are allowed in the input and you need all unique pairs?", "hint": "Sort first, then use two pointers with skip logic. Similar to 3Sum."},
        {"type": "related", "title": "3Sum", "id": 15, "reason": "Extension to three numbers summing to zero"},
        {"type": "related", "title": "4Sum", "id": 18, "reason": "Extension to four numbers"},
        {"type": "related", "title": "Two Sum II - Input Array Is Sorted", "id": 167, "reason": "Same problem but input is sorted — use two pointers"},
    ]
)

_register(2,
    description="""<h3>Add Two Numbers</h3>
<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.</p>
<h4>Example 1:</h4>
<pre>Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.</pre>
<h4>Example 2:</h4>
<pre>Input: l1 = [0], l2 = [0]
Output: [0]</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in each linked list is in the range [1, 100].</li>
<li>0 &le; Node.val &le; 9</li>
</ul>
<p><em>Note: For simplicity, inputs/outputs are represented as lists.</em></p>""",
    function_name="addTwoNumbers",
    template="""class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        # Input/output as lists (representing linked list values in reverse order)
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"l1": [2,4,3], "l2": [5,6,4]}, "expected": [7,0,8]},
        {"input": {"l1": [0], "l2": [0]}, "expected": [0]},
        {"input": {"l1": [9,9,9,9,9,9,9], "l2": [9,9,9,9]}, "expected": [8,9,9,9,0,0,0,1]},
    ],
    solution="""class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        result = []
        carry = 0
        i = 0
        while i < len(l1) or i < len(l2) or carry:
            val = carry
            if i < len(l1):
                val += l1[i]
            if i < len(l2):
                val += l2[i]
            carry, digit = divmod(val, 10)
            result.append(digit)
            i += 1
        return result
""",
    explanation="""**Approach: Elementary Math**

**Time:** O(max(m, n)) | **Space:** O(max(m, n))

1. Iterate through both lists simultaneously, summing corresponding digits plus any carry.
2. Use `divmod` to get the new digit and carry.
3. Continue until both lists are exhausted and carry is 0.

**Why this works:** Just like grade-school addition — add digit by digit from right to left (which is left to right here since digits are reversed), carrying over when sum ≥ 10.
""",
    follow_ups=[
        {"type": "interview", "question": "What if the digits are stored in non-reversed order (most significant digit first)?", "hint": "Reverse both lists first, add, then reverse the result. Or use a stack."},
        {"type": "interview", "question": "Can you solve it without extra space (modifying input lists)?", "hint": "Use one list to store the result in-place, but you'd need to handle different lengths."},
        {"type": "related", "title": "Add Binary", "id": 67, "reason": "Same carry-based addition but with binary strings"},
        {"type": "related", "title": "Add Strings", "id": 415, "reason": "Same idea with decimal digit strings"},
    ]
)

_register(3,
    description="""<h3>Longest Substring Without Repeating Characters</h3>
<p>Given a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.</p>
<h4>Example 1:</h4>
<pre>Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.</pre>
<h4>Example 2:</h4>
<pre>Input: s = "bbbbb"
Output: 1</pre>
<h4>Example 3:</h4>
<pre>Input: s = "pwwkew"
Output: 3</pre>
<h4>Constraints:</h4>
<ul>
<li>0 &le; s.length &le; 5 * 10<sup>4</sup></li>
<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>""",
    function_name="lengthOfLongestSubstring",
    template="""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "abcabcbb"}, "expected": 3},
        {"input": {"s": "bbbbb"}, "expected": 1},
        {"input": {"s": "pwwkew"}, "expected": 3},
        {"input": {"s": ""}, "expected": 0},
        {"input": {"s": "dvdf"}, "expected": 3},
    ],
    solution="""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
""",
    explanation="""**Approach: Sliding Window with Hash Map**

**Time:** O(n) | **Space:** O(min(m, n)) where m is charset size

1. Maintain a window [left, right] and a hash map of character → last seen index.
2. Expand `right` one character at a time.
3. If the character was seen before and its last index is within our window, move `left` past that index.
4. Track the maximum window size.

**Why this works:** The sliding window ensures we always have a valid substring (no repeats). By jumping `left` forward when we hit a duplicate, we skip over all substrings that would contain the duplicate.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you need to return the actual substring, not just its length?", "hint": "Track start index alongside max_len. Return s[start:start+max_len]."},
        {"type": "interview", "question": "What if the string contains only lowercase letters? Can you optimize space?", "hint": "Use a fixed-size array of 26 instead of a hash map."},
        {"type": "related", "title": "Longest Repeating Character Replacement", "id": 424, "reason": "Sliding window with at most k replacements"},
        {"type": "related", "title": "Minimum Window Substring", "id": 76, "reason": "Harder sliding window — find smallest window containing all target chars"},
    ]
)

_register(5,
    description="""<h3>Longest Palindromic Substring</h3>
<p>Given a string <code>s</code>, return the longest palindromic substring in <code>s</code>.</p>
<h4>Example 1:</h4>
<pre>Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.</pre>
<h4>Example 2:</h4>
<pre>Input: s = "cbbd"
Output: "bb"</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; s.length &le; 1000</li>
<li><code>s</code> consist of only digits and English letters.</li>
</ul>""",
    function_name="longestPalindrome",
    template="""class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "babad"}, "expected": ["bab", "aba"]},
        {"input": {"s": "cbbd"}, "expected": "bb"},
        {"input": {"s": "a"}, "expected": "a"},
        {"input": {"s": "ac"}, "expected": ["a", "c"]},
    ],
    solution="""class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
""",
    explanation="""**Approach: Expand Around Center**

**Time:** O(n²) | **Space:** O(1)

1. For each index, try expanding a palindrome centered at that index (odd length) and between index and index+1 (even length).
2. Expand outward while characters match.
3. Track the longest palindrome found.

**Why this works:** Every palindrome has a center. By checking every possible center and expanding, we find all palindromes. There are 2n-1 centers (n single + n-1 between pairs).
""",
    follow_ups=[
        {"type": "interview", "question": "Can you solve this in O(n) time?", "hint": "Manacher's algorithm achieves O(n) by reusing previously computed palindrome info."},
        {"type": "interview", "question": "What if you only need to check if a palindromic substring of length k exists?", "hint": "Binary search on length + rolling hash, or just expand around center and early-exit."},
        {"type": "related", "title": "Palindromic Substrings", "id": 647, "reason": "Count all palindromic substrings instead of finding the longest"},
        {"type": "related", "title": "Shortest Palindrome", "id": 214, "reason": "Find shortest palindrome by prepending characters"},
    ]
)

_register(4,
    description="""<h3>Median of Two Sorted Arrays</h3>
<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return the median of the two sorted arrays.</p>
<p>The overall run time complexity should be O(log (m+n)).</p>
<h4>Example 1:</h4>
<pre>Input: nums1 = [1,3], nums2 = [2]
Output: 2.0</pre>
<h4>Example 2:</h4>
<pre>Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5</pre>""",
    function_name="findMedianSortedArrays",
    template="""class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums1": [1,3], "nums2": [2]}, "expected": 2.0},
        {"input": {"nums1": [1,2], "nums2": [3,4]}, "expected": 2.5},
        {"input": {"nums1": [], "nums2": [1]}, "expected": 1.0},
        {"input": {"nums1": [2], "nums2": []}, "expected": 2.0},
    ],
    solution="""class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return float(max(left1, left2))
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0
""",
    explanation="""**Approach: Binary Search**

**Time:** O(log(min(m,n))) | **Space:** O(1)

1. Binary search on the shorter array to find a partition.
2. The partition divides both arrays such that all left elements ≤ all right elements.
3. The median is derived from the max of left elements and min of right elements.

**Why this works:** We're finding the correct split point where the left half of the combined array equals the right half, using binary search for efficiency.
""",
    follow_ups=[
        {"type": "interview", "question": "What if there are duplicates in the arrays?", "hint": "The binary search approach still works — duplicates don't affect the partition logic."},
        {"type": "interview", "question": "Can you find the kth smallest element instead of median?", "hint": "Binary search on both arrays, eliminating k/2 elements each step — O(log k)."},
        {"type": "related", "title": "Kth Largest Element in an Array", "id": 215, "reason": "Find kth element using quickselect or heap"},
    ]
)

_register(11,
    description="""<h3>Container With Most Water</h3>
<p>Given <code>n</code> non-negative integers <code>height</code> where each represents a point at coordinate <code>(i, height[i])</code>, find two lines that together with the x-axis form a container that holds the most water.</p>
<h4>Example 1:</h4>
<pre>Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49</pre>
<h4>Example 2:</h4>
<pre>Input: height = [1,1]
Output: 1</pre>""",
    function_name="maxArea",
    template="""class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"height": [1,8,6,2,5,4,8,3,7]}, "expected": 49},
        {"input": {"height": [1,1]}, "expected": 1},
        {"input": {"height": [4,3,2,1,4]}, "expected": 16},
        {"input": {"height": [1,2,1]}, "expected": 2},
    ],
    solution="""class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
""",
    explanation="""**Approach: Two Pointers**

**Time:** O(n) | **Space:** O(1)

1. Start with two pointers at the ends of the array.
2. Calculate the area between them.
3. Move the pointer pointing to the shorter line inward.

**Why this works:** Moving the shorter line inward is the only way to potentially find a taller line that could increase the area (despite the decreased width). Moving the taller line can never increase the area.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you prove the two-pointer approach is correct? Why doesn't it miss the optimal pair?", "hint": "The shorter line bounds the area. Moving the taller line can only decrease width without increasing height, so no optimal pair is skipped."},
        {"type": "related", "title": "Trapping Rain Water", "id": 42, "reason": "Similar two-pointer technique on height array, but trapping water between bars"},
    ]
)

_register(14,
    description="""<h3>Longest Common Prefix</h3>
<p>Write a function to find the longest common prefix string amongst an array of strings.</p>
<p>If there is no common prefix, return an empty string <code>""</code>.</p>
<h4>Example 1:</h4>
<pre>Input: strs = ["flower","flow","flight"]
Output: "fl"</pre>
<h4>Example 2:</h4>
<pre>Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; strs.length &le; 200</li>
<li>0 &le; strs[i].length &le; 200</li>
<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>""",
    function_name="longestCommonPrefix",
    template="""class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"strs": ["flower","flow","flight"]}, "expected": "fl"},
        {"input": {"strs": ["dog","racecar","car"]}, "expected": ""},
        {"input": {"strs": ["a"]}, "expected": "a"},
        {"input": {"strs": ["","b"]}, "expected": ""},
        {"input": {"strs": ["cir","car"]}, "expected": "c"},
        {"input": {"strs": ["abc","abc","abc"]}, "expected": "abc"},
    ],
    solution="""class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
""",
    explanation="""**Approach: Horizontal Scanning**

**Time:** O(S) where S is the sum of all characters | **Space:** O(1)

1. Take the first string as the initial prefix.
2. For each subsequent string, shrink the prefix from the right until it matches the start of that string.
3. If the prefix becomes empty, return "".

**Why this works:** The common prefix can only get shorter as we compare more strings. By trimming one character at a time from the right, we find the longest prefix that works for all strings.

**Alternative — Vertical Scanning:** Compare characters column by column across all strings. Stop at the first mismatch. This is better when strings share a very short prefix, since it exits early without scanning full strings.
""",
    follow_ups=[
        {"type": "interview", "question": "What if the list of strings is very large? Can you use divide and conquer?", "hint": "Split the list in half, find LCP of each half, then find LCP of those two results. O(S) time, O(m log n) space."},
        {"type": "interview", "question": "What if you need to answer many LCP queries on the same set of strings?", "hint": "Build a Trie — the LCP is the path from root to the first branching node."},
    ]
)

_register(15,
    description="""<h3>3Sum</h3>
<p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>
<p>Notice that the solution set must not contain duplicate triplets.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1,1]
Output: []</pre>""",
    function_name="threeSum",
    template="""class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [-1,0,1,2,-1,-4]}, "expected": [[-1,-1,2],[-1,0,1]]},
        {"input": {"nums": [0,1,1]}, "expected": []},
        {"input": {"nums": [0,0,0]}, "expected": [[0,0,0]]},
        {"input": {"nums": [-2,0,1,1,2]}, "expected": [[-2,0,2],[-2,1,1]]},
    ],
    solution="""class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
""",
    explanation="""**Approach: Sort + Two Pointers**

**Time:** O(n²) | **Space:** O(1) (ignoring output)

1. Sort the array.
2. Fix one element, then use two pointers to find pairs that sum to its negation.
3. Skip duplicates at each level to avoid duplicate triplets.

**Why this works:** Sorting enables both duplicate detection and the two-pointer technique. For each fixed element, the two-pointer scan is O(n), giving O(n²) total.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you solve this without sorting?", "hint": "Use a hash set for the third element lookup, but handling duplicates becomes trickier."},
        {"type": "interview", "question": "What if you need the closest sum to a target instead of exactly zero?", "hint": "Same approach but track the minimum difference. See problem 16."},
        {"type": "related", "title": "Two Sum", "id": 1, "reason": "Simpler version with two numbers"},
        {"type": "related", "title": "3Sum Closest", "id": 16, "reason": "Find triplet with sum closest to target"},
        {"type": "related", "title": "4Sum", "id": 18, "reason": "Extension to four numbers"},
    ]
)

_register(20,
    description="""<h3>Valid Parentheses</h3>
<p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>
<p>An input string is valid if:</p>
<ol>
<li>Open brackets must be closed by the same type of brackets.</li>
<li>Open brackets must be closed in the correct order.</li>
<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>
<h4>Example 1:</h4>
<pre>Input: s = "()"
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: s = "()[]{}"
Output: true</pre>
<h4>Example 3:</h4>
<pre>Input: s = "(]"
Output: false</pre>""",
    function_name="isValid",
    template="""class Solution:
    def isValid(self, s: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "()"}, "expected": True},
        {"input": {"s": "()[]{}"}, "expected": True},
        {"input": {"s": "(]"}, "expected": False},
        {"input": {"s": "([)]"}, "expected": False},
        {"input": {"s": "{[]}"}, "expected": True},
    ],
    solution="""class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
""",
    explanation="""**Approach: Stack**

**Time:** O(n) | **Space:** O(n)

1. Use a stack to track opening brackets.
2. When we see a closing bracket, check if it matches the top of the stack.
3. If it doesn't match or the stack is empty, return False.
4. At the end, the stack should be empty.

**Why this works:** The stack enforces the correct nesting order — the most recent unmatched opening bracket must match the next closing bracket.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you also need to handle other characters between brackets?", "hint": "Just skip non-bracket characters during iteration."},
        {"type": "interview", "question": "What if you need to find the longest valid parentheses substring?", "hint": "Use a stack storing indices, not characters. See problem 32."},
        {"type": "related", "title": "Generate Parentheses", "id": 22, "reason": "Generate all valid combinations instead of validating"},
        {"type": "related", "title": "Longest Valid Parentheses", "id": 32, "reason": "Find the longest valid substring"},
    ]
)

_register(42,
    description="""<h3>Trapping Rain Water</h3>
<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.</p>
<h4>Example 1:</h4>
<pre>Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6</pre>
<h4>Example 2:</h4>
<pre>Input: height = [4,2,0,3,2,5]
Output: 9</pre>""",
    function_name="trap",
    template="""class Solution:
    def trap(self, height: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"height": [0,1,0,2,1,0,1,3,2,1,2,1]}, "expected": 6},
        {"input": {"height": [4,2,0,3,2,5]}, "expected": 9},
        {"input": {"height": [1,0,1]}, "expected": 1},
        {"input": {"height": [3,0,0,2,0,4]}, "expected": 10},
    ],
    solution="""class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
""",
    explanation="""**Approach: Two Pointers**

**Time:** O(n) | **Space:** O(1)

1. Use two pointers starting from both ends.
2. Track the max height seen from each side.
3. Water at any position = min(left_max, right_max) - height[i].
4. Move the pointer with the smaller max inward.

**Why this works:** The water level at any point is determined by the shorter of the two tallest bars on either side. By moving the pointer with the smaller max, we guarantee the water level is determined by that side.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you solve this using a stack?", "hint": "Use a monotonic decreasing stack. When a taller bar appears, pop and compute water for the valley formed."},
        {"type": "interview", "question": "What about the 2D version (trapping rain water on a height map)?", "hint": "Use a min-heap (priority queue) starting from the borders, processing inward. See problem 407."},
        {"type": "related", "title": "Container With Most Water", "id": 11, "reason": "Similar two-pointer on heights, but maximizing container area"},
        {"type": "related", "title": "Largest Rectangle in Histogram", "id": 84, "reason": "Stack-based approach on height bars"},
        {"type": "related", "title": "Trapping Rain Water II", "id": 407, "reason": "3D version using min-heap"},
    ]
)

_register(53,
    description="""<h3>Maximum Subarray</h3>
<p>Given an integer array <code>nums</code>, find the subarray with the largest sum, and return its sum.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1]
Output: 1</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [5,4,-1,7,8]
Output: 23</pre>""",
    function_name="maxSubArray",
    template="""class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]}, "expected": 6},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [5,4,-1,7,8]}, "expected": 23},
        {"input": {"nums": [-1]}, "expected": -1},
        {"input": {"nums": [-2,-1]}, "expected": -1},
    ],
    solution="""class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            max_sum = max(max_sum, current)
        return max_sum
""",
    explanation="""**Approach: Kadane's Algorithm**

**Time:** O(n) | **Space:** O(1)

1. Track the current subarray sum and the global maximum.
2. At each element, decide: extend the current subarray or start a new one.
3. Update the global maximum.

**Why this works:** If the running sum drops below the current element, it's better to start fresh. This greedy choice is provably optimal.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you also need to return the subarray itself, not just the sum?", "hint": "Track the start index — reset it when you start a new subarray. Record start and end when you update max."},
        {"type": "interview", "question": "Can you solve this with divide and conquer?", "hint": "Split in half. Max subarray is in left half, right half, or crossing the midpoint. O(n log n)."},
        {"type": "related", "title": "Maximum Product Subarray", "id": 152, "reason": "Same idea but with products — need to track both min and max"},
        {"type": "related", "title": "Maximum Sum Circular Subarray", "id": 918, "reason": "Extension where the array is circular"},
    ]
)

_register(56,
    description="""<h3>Merge Intervals</h3>
<p>Given an array of <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.</p>
<h4>Example 1:</h4>
<pre>Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]</pre>
<h4>Example 2:</h4>
<pre>Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]</pre>""",
    function_name="merge",
    template="""class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"intervals": [[1,3],[2,6],[8,10],[15,18]]}, "expected": [[1,6],[8,10],[15,18]]},
        {"input": {"intervals": [[1,4],[4,5]]}, "expected": [[1,5]]},
        {"input": {"intervals": [[1,4],[0,4]]}, "expected": [[0,4]]},
        {"input": {"intervals": [[1,4],[2,3]]}, "expected": [[1,4]]},
    ],
    solution="""class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
""",
    explanation="""**Approach: Sort + Linear Scan**

**Time:** O(n log n) | **Space:** O(n)

1. Sort intervals by start time.
2. Iterate through, merging overlapping intervals by extending the end time.
3. If no overlap, add the interval as-is.

**Why this works:** After sorting, overlapping intervals are adjacent. We only need to check if the current interval overlaps with the last merged one.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you need to insert a new interval into already-merged intervals?", "hint": "Binary search for the insert position, then merge overlapping neighbors. See problem 57."},
        {"type": "interview", "question": "How would you handle this if intervals are streaming in?", "hint": "Use a balanced BST or interval tree for O(log n) insert and merge."},
        {"type": "related", "title": "Insert Interval", "id": 57, "reason": "Insert and merge a new interval into sorted list"},
        {"type": "related", "title": "Meeting Rooms II", "id": 253, "reason": "Count overlapping intervals — how many rooms needed"},
        {"type": "related", "title": "Non-overlapping Intervals", "id": 435, "reason": "Min removals to make intervals non-overlapping"},
    ]
)

_register(121,
    description="""<h3>Best Time to Buy and Sell Stock</h3>
<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the i<sup>th</sup> day.</p>
<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy and a <strong>single day</strong> in the future to sell.</p>
<p>Return the maximum profit. If no profit is possible, return 0.</p>
<h4>Example 1:</h4>
<pre>Input: prices = [7,1,5,3,6,4]
Output: 5</pre>
<h4>Example 2:</h4>
<pre>Input: prices = [7,6,4,3,1]
Output: 0</pre>""",
    function_name="maxProfit",
    template="""class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"prices": [7,1,5,3,6,4]}, "expected": 5},
        {"input": {"prices": [7,6,4,3,1]}, "expected": 0},
        {"input": {"prices": [2,4,1]}, "expected": 2},
        {"input": {"prices": [1]}, "expected": 0},
    ],
    solution="""class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
""",
    explanation="""**Approach: One Pass**

**Time:** O(n) | **Space:** O(1)

1. Track the minimum price seen so far.
2. At each price, calculate the profit if we sold today.
3. Update the maximum profit.

**Why this works:** The best profit for selling on day i is price[i] - min(price[0..i-1]). We track the running minimum to compute this in one pass.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you can make multiple transactions (buy/sell many times)?", "hint": "Collect all positive differences between consecutive days. See problem 122."},
        {"type": "interview", "question": "What if you can make at most 2 transactions?", "hint": "Track best profit from left and right for each split point. See problem 123."},
        {"type": "related", "title": "Best Time to Buy and Sell Stock II", "id": 122, "reason": "Unlimited transactions"},
        {"type": "related", "title": "Best Time to Buy and Sell Stock III", "id": 123, "reason": "At most 2 transactions"},
        {"type": "related", "title": "Best Time to Buy and Sell Stock with Transaction Fee", "id": 714, "reason": "Unlimited transactions with a fee"},
    ]
)

_register(200,
    description="""<h3>Number of Islands</h3>
<p>Given an <code>m x n</code> 2D binary grid which represents a map of <code>'1'</code>s (land) and <code>'0'</code>s (water), return the number of islands.</p>
<p>An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.</p>
<h4>Example 1:</h4>
<pre>Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1</pre>
<h4>Example 2:</h4>
<pre>Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3</pre>""",
    function_name="numIslands",
    template="""class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"grid": [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]}, "expected": 1},
        {"input": {"grid": [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]}, "expected": 3},
        {"input": {"grid": [["1"]]}, "expected": 1},
        {"input": {"grid": [["0"]]}, "expected": 0},
    ],
    solution="""class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
""",
    explanation="""**Approach: DFS Flood Fill**

**Time:** O(m×n) | **Space:** O(m×n) worst case for recursion stack

1. Scan the grid for '1's.
2. When found, increment the island count and DFS to mark all connected land as '0' (visited).
3. Each cell is visited at most once.

**Why this works:** Each DFS call "sinks" an entire island by marking all its cells as water. The number of DFS initiations equals the number of islands.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you can't modify the grid?", "hint": "Use a separate visited set, or use BFS with a queue instead."},
        {"type": "interview", "question": "What if the grid is too large for recursion? (stack overflow risk)", "hint": "Use iterative BFS with a queue to avoid deep recursion."},
        {"type": "interview", "question": "What about counting islands in a stream of additions?", "hint": "Use Union-Find. Each new land cell unions with adjacent land cells."},
        {"type": "related", "title": "Surrounded Regions", "id": 130, "reason": "Flood fill from borders to find non-surrounded regions"},
        {"type": "related", "title": "Max Area of Island", "id": 695, "reason": "Find the largest island by area"},
    ]
)

_register(206,
    description="""<h3>Reverse Linked List</h3>
<p>Given the head of a singly linked list, reverse the list, and return the reversed list.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]</pre>
<h4>Example 2:</h4>
<pre>Input: head = [1,2]
Output: [2,1]</pre>
<p><em>Note: For simplicity, inputs/outputs are represented as lists.</em></p>""",
    function_name="reverseList",
    template="""class Solution:
    def reverseList(self, head: list[int]) -> list[int]:
        # Input/output as lists for simplicity
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,2,3,4,5]}, "expected": [5,4,3,2,1]},
        {"input": {"head": [1,2]}, "expected": [2,1]},
        {"input": {"head": []}, "expected": []},
        {"input": {"head": [1]}, "expected": [1]},
    ],
    solution="""class Solution:
    def reverseList(self, head: list[int]) -> list[int]:
        return head[::-1]
        # Real linked list solution:
        # prev = None
        # curr = head
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # return prev
""",
    explanation="""**Approach: Iterative Pointer Reversal**

**Time:** O(n) | **Space:** O(1)

1. Maintain three pointers: prev (None), curr (head), next.
2. At each step: save next, point curr.next to prev, advance prev and curr.
3. When curr is None, prev is the new head.

```
prev = None
curr = head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
return prev
```

**Why this works:** We reverse each link one at a time, turning `A→B→C` into `A←B←C`. The prev pointer always points to the head of the already-reversed portion.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you do it recursively?", "hint": "Recurse to the end, then reverse links on the way back. Base case: node is null or last node."},
        {"type": "interview", "question": "What if you only need to reverse a portion of the list (from position m to n)?", "hint": "Navigate to position m, reverse until n, reconnect the ends. See problem 92."},
        {"type": "related", "title": "Reverse Linked List II", "id": 92, "reason": "Reverse a sublist from position m to n"},
        {"type": "related", "title": "Reverse Nodes in k-Group", "id": 25, "reason": "Reverse every k consecutive nodes"},
        {"type": "related", "title": "Palindrome Linked List", "id": 234, "reason": "Reverse half the list to check palindrome"},
    ]
)

_register(146,
    description="""<h3>LRU Cache</h3>
<p>Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.</p>
<p>Implement the <code>LRUCache</code> class:</p>
<ul>
<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size capacity.</li>
<li><code>int get(int key)</code> Return the value of the key if the key exists, otherwise return -1.</li>
<li><code>void put(int key, int value)</code> Update or insert the value. When the cache reaches capacity, evict the least recently used key.</li>
</ul>
<h4>Example:</h4>
<pre>Input: ["LRUCache","put","put","get","put","get","put","get","get","get"]
       [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,null,-1,3,4]</pre>""",
    function_name="lruCache",
    template="""class LRUCache:
    def __init__(self, capacity: int):
        # Write your solution here
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

# Test wrapper - do not modify
class Solution:
    def lruCache(self, operations: list[str], args: list[list[int]]) -> list:
        result = []
        cache = None
        for op, arg in zip(operations, args):
            if op == "LRUCache":
                cache = LRUCache(arg[0])
                result.append(None)
            elif op == "get":
                result.append(cache.get(arg[0]))
            elif op == "put":
                cache.put(arg[0], arg[1])
                result.append(None)
        return result
""",
    test_cases=[
        {"input": {"operations": ["LRUCache","put","put","get","put","get","put","get","get","get"],
                    "args": [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]},
         "expected": [None,None,None,1,None,-1,None,-1,3,4]},
    ],
    solution="""from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class Solution:
    def lruCache(self, operations: list[str], args: list[list[int]]) -> list:
        result = []
        cache = None
        for op, arg in zip(operations, args):
            if op == "LRUCache":
                cache = LRUCache(arg[0])
                result.append(None)
            elif op == "get":
                result.append(cache.get(arg[0]))
            elif op == "put":
                cache.put(arg[0], arg[1])
                result.append(None)
        return result
""",
    explanation="""**Approach: OrderedDict (Hash Map + Doubly Linked List)**

**Time:** O(1) for both get and put | **Space:** O(capacity)

1. Use Python's `OrderedDict` which maintains insertion order.
2. On `get`: move the accessed key to the end (most recently used).
3. On `put`: add/update the key at the end; if over capacity, pop the first item (least recently used).

**Why this works:** OrderedDict combines a hash map (O(1) lookup) with a doubly linked list (O(1) reordering). `move_to_end` and `popitem` are both O(1).
""",
    follow_ups=[
        {"type": "interview", "question": "Implement this without using OrderedDict — build the doubly linked list yourself.", "hint": "Hash map for O(1) lookup + doubly linked list for O(1) insert/remove. Use sentinel head/tail nodes."},
        {"type": "interview", "question": "What if you need an LFU (Least Frequently Used) cache instead?", "hint": "Add a frequency counter per key. Use a min-heap or a frequency-to-keys mapping."},
        {"type": "related", "title": "Design Hit Counter", "id": 362, "reason": "Another time-based data structure design"},
    ]
)

_register(70,
    description="""<h3>Climbing Stairs</h3>
<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</p>
<h4>Example 1:</h4>
<pre>Input: n = 2
Output: 2
Explanation: 1+1, 2</pre>
<h4>Example 2:</h4>
<pre>Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1</pre>""",
    function_name="climbStairs",
    template="""class Solution:
    def climbStairs(self, n: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 2}, "expected": 2},
        {"input": {"n": 3}, "expected": 3},
        {"input": {"n": 1}, "expected": 1},
        {"input": {"n": 5}, "expected": 8},
        {"input": {"n": 10}, "expected": 89},
    ],
    solution="""class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
""",
    explanation="""**Approach: Dynamic Programming (Fibonacci)**

**Time:** O(n) | **Space:** O(1)

1. The number of ways to reach step n = ways(n-1) + ways(n-2).
2. This is the Fibonacci sequence! Base cases: ways(1)=1, ways(2)=2.
3. Use two variables instead of an array for O(1) space.

**Why this works:** To reach step n, you either came from step n-1 (1 step) or step n-2 (2 steps). The total ways is the sum of both.
""",
    follow_ups=[
        {"type": "interview", "question": "What if you can climb 1, 2, or 3 steps at a time?", "hint": "dp[n] = dp[n-1] + dp[n-2] + dp[n-3]. Same approach, wider recurrence."},
        {"type": "interview", "question": "What if the cost of each step varies?", "hint": "Track min cost to reach each step. See problem 746 (Min Cost Climbing Stairs)."},
        {"type": "related", "title": "House Robber", "id": 198, "reason": "Similar DP recurrence — choose to include or skip each element"},
        {"type": "related", "title": "Fibonacci Number", "id": 509, "reason": "Same recurrence relation"},
    ]
)

_register(238,
    description="""<h3>Product of Array Except Self</h3>
<p>Given an integer array <code>nums</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>
<p>You must write an algorithm that runs in O(n) time and without using the division operation.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,4]
Output: [24,12,8,6]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]</pre>""",
    function_name="productExceptSelf",
    template="""class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,4]}, "expected": [24,12,8,6]},
        {"input": {"nums": [-1,1,0,-3,3]}, "expected": [0,0,9,0,0]},
        {"input": {"nums": [2,3]}, "expected": [3,2]},
    ],
    solution="""class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
""",
    explanation="""**Approach: Prefix and Suffix Products**

**Time:** O(n) | **Space:** O(1) (output array doesn't count)

1. First pass (left to right): store the running prefix product at each index.
2. Second pass (right to left): multiply by the running suffix product.
3. Each position ends up with the product of all other elements.

**Why this works:** product_except_self[i] = (product of all left of i) × (product of all right of i). Two passes compute both halves.
""",
    follow_ups=[
        {"type": "interview", "question": "What if the array contains zeros?", "hint": "The solution already handles this. Think about what happens: if one zero, only that position is non-zero. If two+ zeros, all products are zero."},
        {"type": "interview", "question": "What if division were allowed?", "hint": "Compute total product, divide by each element. Handle zeros as special cases."},
        {"type": "related", "title": "Trapping Rain Water", "id": 42, "reason": "Similar prefix/suffix pattern — compute left max and right max"},
    ]
)

_register(49,
    description="""<h3>Group Anagrams</h3>
<p>Given an array of strings <code>strs</code>, group the anagrams together. You can return the answer in any order.</p>
<h4>Example 1:</h4>
<pre>Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]</pre>
<h4>Example 2:</h4>
<pre>Input: strs = [""]
Output: [[""]]</pre>""",
    function_name="groupAnagrams",
    template="""class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"strs": ["eat","tea","tan","ate","nat","bat"]}, "expected": [["eat","tea","ate"],["tan","nat"],["bat"]]},
        {"input": {"strs": [""]}, "expected": [[""]]},
        {"input": {"strs": ["a"]}, "expected": [["a"]]},
    ],
    solution="""from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
""",
    explanation="""**Approach: Hash Map with Sorted Key**

**Time:** O(n·k log k) where k is max string length | **Space:** O(n·k)

1. For each string, sort its characters to create a canonical key.
2. Group strings with the same sorted key together in a hash map.
3. Return all groups.

**Why this works:** Two strings are anagrams if and only if their sorted versions are identical. Sorting provides a canonical form for comparison.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you do this in O(n·k) instead of O(n·k log k)?", "hint": "Use a tuple of character counts (26-element tuple) as the hash key instead of sorting."},
        {"type": "interview", "question": "What about grouping shifted strings (e.g., 'abc' and 'bcd')?", "hint": "Compute the differences between consecutive characters as the key. See problem 249."},
        {"type": "related", "title": "Valid Anagram", "id": 242, "reason": "Check if two strings are anagrams"},
        {"type": "related", "title": "Find All Anagrams in a String", "id": 438, "reason": "Find all anagram substrings using sliding window"},
        {"type": "related", "title": "Group Shifted Strings", "id": 249, "reason": "Group by shift pattern instead of character frequency"},
    ]
)

_register(102,
    description="""<h3>Binary Tree Level Order Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).</p>
<h4>Example 1:</h4>
<pre>Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]</pre>
<h4>Example 2:</h4>
<pre>Input: root = [1]
Output: [[1]]</pre>
<h4>Example 3:</h4>
<pre>Input: root = []
Output: []</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in the tree is in the range [0, 2000].</li>
<li>-1000 &le; Node.val &le; 1000</li>
</ul>
<p><em>Note: Tree is represented as a level-order list, e.g. [3,9,20,null,null,15,7].</em></p>""",
    function_name="levelOrder",
    template="""class Solution:
    def levelOrder(self, root: list) -> list[list[int]]:
        # root is a level-order list, e.g. [3,9,20,null,null,15,7]
        # Return list of lists, each inner list is one level
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"root": [3,9,20,None,None,15,7]}, "expected": [[3],[9,20],[15,7]]},
        {"input": {"root": [1]}, "expected": [[1]]},
        {"input": {"root": []}, "expected": []},
        {"input": {"root": [1,2,3,4,5]}, "expected": [[1],[2,3],[4,5]]},
        {"input": {"root": [1,None,2,None,3]}, "expected": [[1],[2],[3]]},
    ],
    solution="""class Solution:
    def levelOrder(self, root: list) -> list[list[int]]:
        if not root:
            return []
        # Build tree from level-order list
        from collections import deque
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        nodes = [TreeNode(v) if v is not None else None for v in root]
        child_idx = 1
        for node in nodes:
            if node is None:
                continue
            if child_idx < len(nodes):
                node.left = nodes[child_idx]
                child_idx += 1
            if child_idx < len(nodes):
                node.right = nodes[child_idx]
                child_idx += 1

        # BFS level order traversal
        result = []
        queue = deque([nodes[0]])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
""",
    explanation="""**Approach: BFS with Queue**

**Time:** O(n) | **Space:** O(n)

1. Build the binary tree from the level-order list representation.
2. Use a queue (deque) for BFS. Start with the root.
3. For each level, process all nodes currently in the queue, collecting their values.
4. Add children of processed nodes to the queue for the next level.
5. Append each level's values as a list to the result.

**Why this works:** BFS naturally processes nodes level by level. By tracking the queue size at the start of each level, we know exactly how many nodes belong to the current level.
""",
    follow_ups=[
        {"type": "interview", "question": "Can you do this with DFS instead of BFS?", "hint": "Use DFS with a depth parameter. Append to result[depth]. Pre-order traversal works — just ensure result has enough sublists."},
        {"type": "interview", "question": "What if you need zigzag order (alternating left-right, right-left)?", "hint": "Same BFS, but reverse every other level. See problem 103."},
        {"type": "interview", "question": "What if you need bottom-up level order (leaves first)?", "hint": "Do normal level order, then reverse the result list."},
        {"type": "related", "title": "Binary Tree Zigzag Level Order Traversal", "id": 103, "reason": "Zigzag variation of level order"},
        {"type": "related", "title": "Maximum Level Sum of a Binary Tree", "id": 1161, "reason": "Find the level with maximum sum"},
        {"type": "related", "title": "Binary Tree Right Side View", "id": 199, "reason": "Return only the rightmost node at each level"},
    ]
)

# Load additional problem batches
for _batch_file in ['problems_batch1.py', 'problems_batch2.py', 'problems_batch3.py', 'problems_batch4.py', 'problems_batch5.py']:
    _batch_path = os.path.join(os.path.dirname(__file__), _batch_file)
    if os.path.exists(_batch_path):
        with open(_batch_path, encoding='utf-8') as _f:
            exec(_f.read())

# ---- API Routes ----

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    solved = load_solved()
    return jsonify([
        {**q, 'solved': q['id'] in solved, 'lc75': q['id'] in LC75_IDS}
        for q in QUESTIONS
    ])

@app.route('/api/question/<int:question_id>')
def get_question(question_id):
    # Find the question in our list
    question = None
    for q in QUESTIONS:
        if q['id'] == question_id:
            question = q
            break
    if not question:
        return jsonify({'error': 'Question not found'}), 404

    # Get problem details from bank
    problem = PROBLEM_BANK.get(question_id)
    user_solutions = load_user_solutions()
    saved_code = user_solutions.get(str(question_id))

    if problem:
        result = {
            **question,
            'description': problem['description'],
            'function_name': problem['function_name'],
            'template': problem['template'],
            'test_cases': problem['test_cases'],
            'has_solution': True,
            'follow_ups': problem.get('follow_ups', []),
        }
    else:
        result = {
            **question,
            'description': f'<h3>{question["title"]}</h3><p>Problem details not yet loaded. Visit <a href="{question["url"]}" target="_blank">LeetCode</a> to see the full problem.</p>',
            'template': f'class Solution:\n    def solve(self):\n        # Visit {question["url"]} for the full problem\n        pass\n',
            'test_cases': [],
            'has_solution': False,
            'follow_ups': [],
        }

    if saved_code is not None:
        result['saved_code'] = saved_code
    return jsonify(result)

@app.route('/api/save/<int:question_id>', methods=['POST'])
def save_code(question_id):
    data = request.get_json()
    code = data.get('code', '')
    passed = bool(data.get('passed', False))
    solutions = load_user_solutions()
    solutions[str(question_id)] = code
    save_user_solutions(solutions)
    newly_solved = False
    if passed:
        solved = load_solved()
        if question_id not in solved:
            solved.add(question_id)
            save_solved(solved)
            newly_solved = True
    return jsonify({'status': 'saved', 'solved': passed, 'newly_solved': newly_solved})

@app.route('/api/solution/<int:question_id>')
def get_solution(question_id):
    problem = PROBLEM_BANK.get(question_id)
    if not problem:
        return jsonify({'error': 'Solution not available for this problem'}), 404
    return jsonify({
        'solution': problem['solution'],
        'explanation': problem['explanation'],
    })

_HARNESS_PREAMBLE = """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _list_to_ll(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    for v in lst[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def _ll_to_list(head):
    out = []
    seen = set()
    while head is not None:
        if id(head) in seen:
            break
        seen.add(id(head))
        out.append(head.val)
        head = head.next
    return out
"""

@app.route('/api/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    test_cases = data.get('test_cases', [])
    function_name = data.get('function_name', '')
    question_id = data.get('question_id')

    if not test_cases:
        return jsonify({'error': 'No test cases available for this problem'})

    harness = None
    if question_id is not None:
        problem = PROBLEM_BANK.get(question_id)
        if problem:
            harness = problem.get('harness')

    results = []
    for i, tc in enumerate(test_cases):
        test_input = tc['input']
        expected = tc['expected']

        in_transforms = (harness or {}).get('input', {})
        out_transform = (harness or {}).get('output')

        # Build the test runner script
        runner = ""
        if harness:
            runner += _HARNESS_PREAMBLE
        runner += code + "\n\n"
        runner += "import json, sys\n"
        runner += "sol = Solution()\n"

        arg_parts = []
        for k, v in test_input.items():
            xform = in_transforms.get(k)
            if xform == 'linked_list':
                runner += f"_arg_{k} = _list_to_ll({repr(v)})\n"
                arg_parts.append(f"{k}=_arg_{k}")
            else:
                arg_parts.append(f"{k}={repr(v)}")
        runner += f"result = sol.{function_name}({', '.join(arg_parts)})\n"

        if out_transform == 'linked_list':
            runner += "result = _ll_to_list(result)\n"

        runner += "print(json.dumps(result))\n"

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(runner)
                tmp_path = f.name

            proc = subprocess.run(
                [sys.executable, tmp_path],
                capture_output=True, text=True, timeout=10
            )
            os.unlink(tmp_path)

            if proc.returncode != 0:
                results.append({
                    'test_case': i + 1,
                    'input': test_input,
                    'expected': expected,
                    'actual': None,
                    'passed': False,
                    'error': '\n'.join(proc.stderr.strip().split('\n')[-3:]) if proc.stderr else 'Runtime error',
                })
            else:
                actual = json.loads(proc.stdout.strip())
                # Handle multiple valid answers (actual is a single string, expected is a list of acceptable answers)
                if isinstance(expected, list) and len(expected) > 0 and isinstance(expected[0], str) and not isinstance(actual, list):
                    passed = actual in expected
                elif isinstance(expected, list) and isinstance(actual, list):
                    if len(expected) > 0 and all(isinstance(x, list) for x in expected):
                        # nested list output (e.g., 3Sum): order of sub-lists and within each don't matter
                        try:
                            passed = sorted([sorted(x) for x in actual]) == sorted([sorted(x) for x in expected])
                        except TypeError:
                            passed = actual == expected
                    elif actual == expected:
                        passed = True
                    else:
                        # fall back to sorted comparison only for numeric flat lists (e.g., Two Sum indices)
                        try:
                            if all(isinstance(x, (int, float)) for x in expected) and all(isinstance(x, (int, float)) for x in actual):
                                passed = sorted(actual) == sorted(expected)
                            else:
                                passed = False
                        except TypeError:
                            passed = False
                else:
                    passed = actual == expected

                results.append({
                    'test_case': i + 1,
                    'input': test_input,
                    'expected': expected,
                    'actual': actual,
                    'passed': passed,
                    'error': None,
                })
        except subprocess.TimeoutExpired:
            try:
                os.unlink(tmp_path)
            except:
                pass
            results.append({
                'test_case': i + 1,
                'input': test_input,
                'expected': expected,
                'actual': None,
                'passed': False,
                'error': 'Time Limit Exceeded (10s)',
            })
        except Exception as e:
            results.append({
                'test_case': i + 1,
                'input': test_input,
                'expected': expected,
                'actual': None,
                'passed': False,
                'error': str(e),
            })

    all_passed = all(r['passed'] for r in results)
    return jsonify({
        'results': results,
        'all_passed': all_passed,
        'summary': f"{'All' if all_passed else sum(1 for r in results if r['passed'])}/{len(results)} test cases passed"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5050)
