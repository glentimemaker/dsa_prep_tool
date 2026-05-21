# Batch 2: Problems from frequency 50% and 37.5%

# 242: Valid Anagram
_register(242,
    description="""<h3>242. Valid Anagram</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise.</p>
<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "anagram", t = "nagaram"
Output: true</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "rat", t = "car"
Output: false</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></li>
<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>""",
    function_name="isAnagram",
    template="""class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "anagram", "t": "nagaram"}, "expected": True},
        {"input": {"s": "rat", "t": "car"}, "expected": False},
        {"input": {"s": "a", "t": "a"}, "expected": True},
        {"input": {"s": "ab", "t": "ba"}, "expected": True},
        {"input": {"s": "ab", "t": "a"}, "expected": False},
    ],
    solution="""class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)
""",
    explanation="""### Approach: Hash Map / Counter

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 26 letters)

1. If the two strings have different lengths, they cannot be anagrams — return False immediately.
2. Count the frequency of each character in both strings using a Counter (hash map).
3. Compare the two counters. If they are equal, every character appears the same number of times, so `t` is an anagram of `s`.

**Why this works:** An anagram is simply a rearrangement of the same letters. Two strings are anagrams if and only if they contain exactly the same characters with the same frequencies."""
)

# 253: Meeting Rooms II
_register(253,
    description="""<h3>253. Meeting Rooms II</h3>
<p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, return the <em>minimum number of conference rooms required</em>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: intervals = [[7,10],[2,4]]
Output: 1</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= intervals.length &lt;= 10<sup>4</sup></li>
<li>0 &lt;= start_i &lt; end_i &lt;= 10<sup>6</sup></li>
</ul>""",
    function_name="minMeetingRooms",
    template="""class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"intervals": [[0,30],[5,10],[15,20]]}, "expected": 2},
        {"input": {"intervals": [[7,10],[2,4]]}, "expected": 1},
        {"input": {"intervals": [[1,5],[2,6],[3,7],[4,8]]}, "expected": 4},
        {"input": {"intervals": [[1,2],[3,4],[5,6]]}, "expected": 1},
        {"input": {"intervals": [[1,10]]}, "expected": 1},
    ],
    solution="""class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort()
        rooms = 0
        max_rooms = 0
        for _, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        return max_rooms
""",
    explanation="""### Approach: Sweep Line / Event Sorting

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

1. Create a list of events: each meeting start is +1 (a room is needed) and each meeting end is -1 (a room is freed).
2. Sort events by time. When times are equal, ends (-1) come before starts (+1) because a room freed at time t can be reused by a meeting starting at time t.
3. Sweep through the events, maintaining a running count of rooms in use.
4. The maximum value of the running count is the answer.

**Why this works:** At any point in time, the number of rooms needed equals the number of ongoing meetings. The sweep line efficiently tracks this count by processing starts and ends in chronological order."""
)

# 283: Move Zeroes
_register(283,
    description="""<h3>283. Move Zeroes</h3>
<p>Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.</p>
<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [0,1,0,3,12]
Output: [0,1,0,3,12] -> [1,3,12,0,0]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [0]
Output: [0]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
<li>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</li>
</ul>""",
    function_name="moveZeroes",
    template="""class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        # Write your solution here (modify nums in-place and return it)
        pass
""",
    test_cases=[
        {"input": {"nums": [0,1,0,3,12]}, "expected": [1,3,12,0,0]},
        {"input": {"nums": [0]}, "expected": [0]},
        {"input": {"nums": [1,2,3]}, "expected": [1,2,3]},
        {"input": {"nums": [0,0,0,1]}, "expected": [1,0,0,0]},
        {"input": {"nums": [1]}, "expected": [1]},
    ],
    solution="""class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        return nums
""",
    explanation="""### Approach: Two Pointers (Swap)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

1. Maintain a `write` pointer starting at index 0. This pointer tracks where the next non-zero element should go.
2. Iterate through the array with a `read` pointer.
3. When a non-zero element is found, swap it with the element at the `write` pointer, then increment `write`.
4. After the loop, all non-zero elements are at the front in their original order, and all zeros are at the end.

**Why this works:** The `write` pointer always points to the leftmost zero (or the next available position). Swapping ensures non-zero elements move forward while zeros accumulate at the end, preserving relative order of non-zero elements."""
)

# 347: Top K Frequent Elements
_register(347,
    description="""<h3>347. Top K Frequent Elements</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k</code> most frequent elements. You may return the answer in <strong>any order</strong>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [1], k = 1
Output: [1]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
<li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
<li><code>k</code> is in the range [1, the number of unique elements].</li>
<li>It is guaranteed that the answer is unique.</li>
</ul>""",
    function_name="topKFrequent",
    template="""class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,1,1,2,2,3], "k": 2}, "expected": [1,2]},
        {"input": {"nums": [1], "k": 1}, "expected": [1]},
        {"input": {"nums": [4,4,4,1,1,2,2,2,3], "k": 2}, "expected": [4,2]},
        {"input": {"nums": [3,3,3,3], "k": 1}, "expected": [3]},
    ],
    solution="""class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        # Bucket sort: index = frequency, value = list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
""",
    explanation="""### Approach: Bucket Sort

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Count the frequency of each element using a Counter.
2. Create buckets where index `i` holds all elements that appear exactly `i` times. The max frequency is at most `n` (length of the array).
3. Iterate from the highest frequency bucket down, collecting elements until we have `k` elements.

**Why this works:** By using bucket sort on frequencies, we avoid the O(n log n) cost of sorting. The bucket at index `i` contains all numbers appearing `i` times, so iterating from high to low gives us the most frequent elements first."""
)

# 354: Russian Doll Envelopes
_register(354,
    description="""<h3>354. Russian Doll Envelopes</h3>
<p>You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w_i, h_i]</code> represents the width and the height of an envelope.</p>
<p>One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.</p>
<p>Return the <em>maximum number of envelopes you can Russian doll</em> (i.e., put one inside the other).</p>
<p><strong>Note:</strong> You cannot rotate an envelope.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= envelopes.length &lt;= 10<sup>5</sup></li>
<li>envelopes[i].length == 2</li>
<li>1 &lt;= w_i, h_i &lt;= 10<sup>5</sup></li>
</ul>""",
    function_name="maxEnvelopes",
    template="""class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"envelopes": [[5,4],[6,4],[6,7],[2,3]]}, "expected": 3},
        {"input": {"envelopes": [[1,1],[1,1],[1,1]]}, "expected": 1},
        {"input": {"envelopes": [[1,2],[2,3],[3,4],[4,5]]}, "expected": 4},
        {"input": {"envelopes": [[1,1]]}, "expected": 1},
        {"input": {"envelopes": [[4,5],[4,6],[6,7],[2,3],[1,1]]}, "expected": 4},
    ],
    solution="""class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        import bisect
        # Sort by width ascending, then by height descending for same width
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # LIS on heights
        dp = []
        for _, h in envelopes:
            pos = bisect.bisect_left(dp, h)
            if pos == len(dp):
                dp.append(h)
            else:
                dp[pos] = h
        return len(dp)
""",
    explanation="""### Approach: Sort + Longest Increasing Subsequence (LIS)

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

1. Sort envelopes by width ascending. For envelopes with the same width, sort by height **descending**.
2. Extract the heights and find the Longest Increasing Subsequence (LIS) using binary search (patience sorting).
3. The descending sort on height for equal widths prevents selecting two envelopes with the same width (since a decreasing sequence in heights can never form an increasing subsequence).

**Why this works:** After sorting by width, we only need to find the LIS of heights. The descending height trick ensures we never pick two envelopes with equal width. The binary search LIS algorithm runs in O(n log n)."""
)

# 394: Decode String
_register(394,
    description="""<h3>394. Decode String</h3>
<p>Given an encoded string, return its decoded string.</p>
<p>The encoding rule is: <code>k[encoded_string]</code>, where the <code>encoded_string</code> inside the square brackets is being repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "3[a]2[bc]"
Output: "aaabcbc"</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "3[a2[c]]"
Output: "accaccacc"</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length &lt;= 30</li>
<li><code>s</code> consists of lowercase English letters, digits, and square brackets.</li>
<li><code>s</code> is guaranteed to be a valid input.</li>
<li>All integers in <code>s</code> are in the range [1, 300].</li>
</ul>""",
    function_name="decodeString",
    template="""class Solution:
    def decodeString(self, s: str) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "3[a]2[bc]"}, "expected": "aaabcbc"},
        {"input": {"s": "3[a2[c]]"}, "expected": "accaccacc"},
        {"input": {"s": "2[abc]3[cd]ef"}, "expected": "abcabccdcdcdef"},
        {"input": {"s": "abc"}, "expected": "abc"},
        {"input": {"s": "10[a]"}, "expected": "aaaaaaaaaa"},
    ],
    solution="""class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += ch
        return current_str
""",
    explanation="""### Approach: Stack

**Time Complexity:** O(n * max_k) where max_k is the maximum repeat count
**Space Complexity:** O(n)

1. Iterate through the string character by character.
2. If it's a digit, build up the current number (handling multi-digit numbers).
3. If it's `[`, push the current string and number onto the stack, then reset them.
4. If it's `]`, pop the previous string and repeat count from the stack, and build the decoded string.
5. If it's a letter, append it to the current string.

**Why this works:** The stack naturally handles nested encodings. Each `[` saves the context (previous string and repeat count), and each `]` restores it while applying the repetition. This mimics the recursive structure of the encoding."""
)

# 424: Longest Repeating Character Replacement
_register(424,
    description="""<h3>424. Longest Repeating Character Replacement</h3>
<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English letter. You can perform this operation at most <code>k</code> times.</p>
<p>Return the length of the longest substring containing the same letter you can get after performing the above operations.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "ABAB", k = 2
Output: 4</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "AABABBA", k = 1
Output: 4</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length &lt;= 10<sup>5</sup></li>
<li><code>s</code> consists of only uppercase English letters.</li>
<li>0 &lt;= k &lt;= s.length</li>
</ul>""",
    function_name="characterReplacement",
    template="""class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "ABAB", "k": 2}, "expected": 4},
        {"input": {"s": "AABABBA", "k": 1}, "expected": 4},
        {"input": {"s": "AAAA", "k": 0}, "expected": 4},
        {"input": {"s": "ABCD", "k": 0}, "expected": 1},
        {"input": {"s": "ABBB", "k": 2}, "expected": 4},
    ],
    solution="""class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            # Window size - max freq char count = chars to replace
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
""",
    explanation="""### Approach: Sliding Window

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 26 characters)

1. Use a sliding window with `left` and `right` pointers.
2. Track the count of each character in the window and the maximum frequency of any single character (`max_freq`).
3. The number of replacements needed in the current window is `window_size - max_freq`.
4. If replacements needed exceed `k`, shrink the window from the left.
5. Track the maximum valid window size.

**Why this works:** In any window, the optimal strategy is to keep the most frequent character and replace all others. If the number of characters to replace exceeds `k`, the window is invalid and must be shrunk. The `max_freq` optimization works because we only care about finding a longer valid window."""
)

# 540: Single Element in a Sorted Array
_register(540,
    description="""<h3>540. Single Element in a Sorted Array</h3>
<p>You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.</p>
<p>Return the single element that appears only once.</p>
<p>Your solution must run in <code>O(log n)</code> time and <code>O(1)</code> space.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [3,3,7,7,10,11,11]
Output: 10</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
<li>0 &lt;= nums[i] &lt;= 10<sup>5</sup></li>
</ul>""",
    function_name="singleNonDuplicate",
    template="""class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,1,2,3,3,4,4,8,8]}, "expected": 2},
        {"input": {"nums": [3,3,7,7,10,11,11]}, "expected": 10},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [1,1,2]}, "expected": 2},
        {"input": {"nums": [1,2,2]}, "expected": 1},
    ],
    solution="""class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # Single element is to the right
                lo = mid + 2
            else:
                # Single element is at mid or to the left
                hi = mid
        return nums[lo]
""",
    explanation="""### Approach: Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

1. Use binary search on the array.
2. At each step, ensure `mid` is even (if odd, decrement by 1).
3. If `nums[mid] == nums[mid + 1]`, the pairs before `mid` are intact, so the single element must be to the right. Move `lo = mid + 2`.
4. Otherwise, a pair is broken at or before `mid`, so the single element is at `mid` or to the left. Move `hi = mid`.
5. When `lo == hi`, we've found the single element.

**Why this works:** In a sorted array where every element appears twice, pairs start at even indices (0-1, 2-3, ...). The single element disrupts this pattern. By checking whether the pair at an even index is intact, we can determine which half contains the single element."""
)

# 704: Binary Search
_register(704,
    description="""<h3>704. Binary Search</h3>
<p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>
<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
<li>-10<sup>4</sup> &lt; nums[i], target &lt; 10<sup>4</sup></li>
<li>All the integers in <code>nums</code> are unique.</li>
<li><code>nums</code> is sorted in ascending order.</li>
</ul>""",
    function_name="search",
    template="""class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [-1,0,3,5,9,12], "target": 9}, "expected": 4},
        {"input": {"nums": [-1,0,3,5,9,12], "target": 2}, "expected": -1},
        {"input": {"nums": [5], "target": 5}, "expected": 0},
        {"input": {"nums": [5], "target": -5}, "expected": -1},
        {"input": {"nums": [2,5], "target": 5}, "expected": 1},
    ],
    solution="""class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
""",
    explanation="""### Approach: Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

1. Initialize two pointers `lo = 0` and `hi = len(nums) - 1`.
2. While `lo <= hi`, compute `mid = lo + (hi - lo) // 2`.
3. If `nums[mid] == target`, return `mid`.
4. If `nums[mid] < target`, the target is in the right half: `lo = mid + 1`.
5. If `nums[mid] > target`, the target is in the left half: `hi = mid - 1`.
6. If the loop ends without finding the target, return -1.

**Why this works:** Binary search works on sorted arrays by repeatedly halving the search space. Each comparison eliminates half of the remaining elements, achieving O(log n) time complexity."""
)

# 875: Koko Eating Bananas
_register(875,
    description="""<h3>875. Koko Eating Bananas</h3>
<p>Koko loves to eat bananas. There are <code>n</code> piles of bananas, the <code>i<sup>th</sup></code> pile has <code>piles[i]</code> bananas. The guards have gone and will come back in <code>h</code> hours.</p>
<p>Koko can decide her bananas-per-hour eating speed of <code>k</code>. Each hour, she chooses some pile of bananas and eats <code>k</code> bananas from that pile. If the pile has less than <code>k</code> bananas, she eats all of them and will not eat any more bananas during this hour.</p>
<p>Return the minimum integer <code>k</code> such that she can eat all the bananas within <code>h</code> hours.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: piles = [3,6,7,11], h = 8
Output: 4</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: piles = [30,11,23,4,20], h = 5
Output: 30</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: piles = [30,11,23,4,20], h = 6
Output: 23</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= piles.length &lt;= 10<sup>4</sup></li>
<li>piles.length &lt;= h &lt;= 10<sup>9</sup></li>
<li>1 &lt;= piles[i] &lt;= 10<sup>9</sup></li>
</ul>""",
    function_name="minEatingSpeed",
    template="""class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"piles": [3,6,7,11], "h": 8}, "expected": 4},
        {"input": {"piles": [30,11,23,4,20], "h": 5}, "expected": 30},
        {"input": {"piles": [30,11,23,4,20], "h": 6}, "expected": 23},
        {"input": {"piles": [1], "h": 1}, "expected": 1},
        {"input": {"piles": [1000000000], "h": 2}, "expected": 500000000},
    ],
    solution="""class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        import math
        def can_finish(k):
            return sum(math.ceil(p / k) for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
""",
    explanation="""### Approach: Binary Search on Answer

**Time Complexity:** O(n * log(max(piles)))
**Space Complexity:** O(1)

1. Binary search on the eating speed `k` in the range `[1, max(piles)]`.
2. For each candidate speed `mid`, check if Koko can finish all bananas in `h` hours by computing the total hours needed: `sum(ceil(pile / mid) for pile in piles)`.
3. If she can finish, try a smaller speed: `hi = mid`.
4. If she cannot finish, she needs a faster speed: `lo = mid + 1`.
5. When `lo == hi`, we've found the minimum valid speed.

**Why this works:** The feasibility function is monotonic: if Koko can finish at speed `k`, she can also finish at any speed > `k`. This makes binary search applicable. We search for the smallest `k` where the total hours needed is at most `h`."""
)

# 912: Sort an Array
_register(912,
    description="""<h3>912. Sort an Array</h3>
<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>
<p>You must solve the problem without using any built-in functions in <code>O(n log n)</code> time complexity and with the smallest space complexity possible.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [5,2,3,1]
Output: [1,2,3,5]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></li>
<li>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></li>
</ul>""",
    function_name="sortArray",
    template="""class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [5,2,3,1]}, "expected": [1,2,3,5]},
        {"input": {"nums": [5,1,1,2,0,0]}, "expected": [0,0,1,1,2,5]},
        {"input": {"nums": [1]}, "expected": [1]},
        {"input": {"nums": [3,3,3]}, "expected": [3,3,3]},
        {"input": {"nums": [-1,5,3,-2,0]}, "expected": [-2,-1,0,3,5]},
    ],
    solution="""class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
""",
    explanation="""### Approach: Merge Sort

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

1. **Divide:** Split the array into two halves.
2. **Conquer:** Recursively sort each half.
3. **Merge:** Merge the two sorted halves by comparing elements one by one and building a new sorted array.

**Why this works:** Merge sort guarantees O(n log n) time in all cases (best, average, worst). The divide step takes O(1), the merge step takes O(n), and there are O(log n) levels of recursion. It is a stable sort that maintains relative order of equal elements."""
)

# 1502: Can Make Arithmetic Progression From Sequence
_register(1502,
    description="""<h3>1502. Can Make Arithmetic Progression From Sequence</h3>
<p>A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.</p>
<p>Given an array of numbers <code>arr</code>, return <code>true</code> if the array can be rearranged to form an <strong>arithmetic progression</strong>. Otherwise, return <code>false</code>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] with difference 2.</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: arr = [1,2,4]
Output: false</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>2 &lt;= arr.length &lt;= 1000</li>
<li>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></li>
</ul>""",
    function_name="canMakeArithmeticProgression",
    template="""class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"arr": [3,5,1]}, "expected": True},
        {"input": {"arr": [1,2,4]}, "expected": False},
        {"input": {"arr": [1,1,1,1]}, "expected": True},
        {"input": {"arr": [7,1,4]}, "expected": True},
        {"input": {"arr": [0,0]}, "expected": True},
    ],
    solution="""class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
""",
    explanation="""### Approach: Sort and Check

**Time Complexity:** O(n log n)
**Space Complexity:** O(1) (in-place sort)

1. Sort the array in ascending order.
2. Compute the common difference as `arr[1] - arr[0]`.
3. Check that every consecutive pair has the same difference.
4. If any pair differs, return False. Otherwise return True.

**Why this works:** An arithmetic progression has a constant difference between consecutive terms. After sorting, if the array forms an AP, all consecutive differences must be equal. Sorting lets us check this in a single pass."""
)

# 1757: Recyclable and Low Fat Products - SQL problem, skipped

# 1768: Merge Strings Alternately
_register(1768,
    description="""<h3>1768. Merge Strings Alternately</h3>
<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>
<p>Return the merged string.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= word1.length, word2.length &lt;= 100</li>
<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>""",
    function_name="mergeAlternately",
    template="""class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"word1": "abc", "word2": "pqr"}, "expected": "apbqcr"},
        {"input": {"word1": "ab", "word2": "pqrs"}, "expected": "apbqrs"},
        {"input": {"word1": "abcd", "word2": "pq"}, "expected": "apbqcd"},
        {"input": {"word1": "a", "word2": "b"}, "expected": "ab"},
        {"input": {"word1": "a", "word2": "bcdef"}, "expected": "abcdef"},
    ],
    solution="""class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
""",
    explanation="""### Approach: Two Pointers / Interleave

**Time Complexity:** O(n + m)
**Space Complexity:** O(n + m)

1. Use a single index `i` to iterate through both strings simultaneously.
2. At each step, append the character from `word1[i]` (if it exists) then `word2[i]` (if it exists).
3. Continue until both strings are exhausted.
4. Join the result list into a string.

**Why this works:** By alternating between the two strings at each index, we naturally interleave the characters. When one string is exhausted, we continue appending from the longer string, which handles unequal lengths gracefully."""
)

# 1944: Number of Visible People in a Queue
_register(1944,
    description="""<h3>1944. Number of Visible People in a Queue</h3>
<p>There are <code>n</code> people standing in a queue, and they are numbered from <code>0</code> to <code>n - 1</code> in left to right order. You are given an array <code>heights</code> where <code>heights[i]</code> represents the height of the <code>i<sup>th</sup></code> person.</p>
<p>A person can <strong>see</strong> another person to their right if everybody in between is shorter than both of them. More formally, person <code>i</code> can see person <code>j</code> (where <code>i &lt; j</code>) if <code>min(heights[i], heights[j]) &gt; max(heights[i+1], ..., heights[j-1])</code>.</p>
<p>Return an array <code>answer</code> of length <code>n</code> where <code>answer[i]</code> is the number of people the <code>i<sup>th</sup></code> person can see to their right in the queue.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>n == heights.length</li>
<li>1 &lt;= n &lt;= 10<sup>5</sup></li>
<li>1 &lt;= heights[i] &lt;= 10<sup>5</sup></li>
<li>All the values of <code>heights</code> are unique.</li>
</ul>""",
    function_name="canSeePersonsCount",
    template="""class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"heights": [10,6,8,5,11,9]}, "expected": [3,1,2,1,1,0]},
        {"input": {"heights": [5,1,2,3,10]}, "expected": [4,1,1,1,0]},
        {"input": {"heights": [1,2,3,4,5]}, "expected": [1,1,1,1,0]},
        {"input": {"heights": [5,4,3,2,1]}, "expected": [1,1,1,1,0]},
        {"input": {"heights": [3]}, "expected": [0]},
    ],
    solution="""class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = [0] * n
        stack = []  # monotonic decreasing stack of indices
        for i in range(n - 1, -1, -1):
            # Pop all shorter people - current person can see them
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                answer[i] += 1
            # If stack not empty, current person can also see the first taller person
            if stack:
                answer[i] += 1
            stack.append(i)
        return answer
""",
    explanation="""### Approach: Monotonic Stack (Decreasing)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Traverse the array from right to left, maintaining a monotonic decreasing stack of indices.
2. For each person `i`, pop all people from the stack who are shorter than `heights[i]`. Each popped person is visible to person `i`, so increment `answer[i]`.
3. After popping, if the stack is not empty, the top of the stack is the first person taller than or equal to person `i`, who is also visible. Add 1 more to `answer[i]`.
4. Push `i` onto the stack.

**Why this works:** A person can see everyone shorter than them until blocked by someone taller. The monotonic stack maintains a decreasing sequence of heights looking right. Popping shorter people counts them as visible, and the remaining top (if any) is the first blocking taller person, who is also visible."""
)

# 2667: Create Hello World Function - JS problem, skipped

# 3453: Separate Squares I
_register(3453,
    description="""<h3>3453. Separate Squares I</h3>
<p>You are given a 2D integer array <code>squares</code>. Each <code>squares[i] = [x_i, y_i, l_i]</code> represents a square with bottom-left corner at <code>(x_i, y_i)</code> and side length <code>l_i</code>.</p>
<p>Find the minimum <code>y</code>-coordinate value of a horizontal line such that the total area of squares above the line is as close as possible to the total area of squares below the line.</p>
<p>Return the <code>y</code>-coordinate value as a floating point number.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: squares = [[0,0,1],[2,2,1]]
Output: 1.0
Explanation: Total area = 2. The line y = 1.0 splits into equal halves.</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: squares = [[0,0,2],[1,1,1]]
Output: 1.0
Explanation: Total area = 5. The line y = 1.0 gives area below = 2.5 and area above = 2.5.</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= squares.length &lt;= 5000</li>
<li>squares[i] = [x_i, y_i, l_i]</li>
<li>0 &lt;= x_i, y_i &lt;= 10<sup>9</sup></li>
<li>1 &lt;= l_i &lt;= 10<sup>9</sup></li>
</ul>""",
    function_name="separateSquares",
    template="""class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"squares": [[0,0,1],[2,2,1]]}, "expected": 1.0},
        {"input": {"squares": [[0,0,2],[1,1,1]]}, "expected": 1.0},
        {"input": {"squares": [[0,0,4]]}, "expected": 2.0},
        {"input": {"squares": [[0,0,1],[0,1,1],[0,2,1]]}, "expected": 1.5},
    ],
    solution="""class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        half = total_area / 2.0

        # Binary search on y
        lo = min(y for _, y, _ in squares)
        hi = max(y + l for _, y, l in squares)

        for _ in range(100):  # sufficient iterations for precision
            mid = (lo + hi) / 2.0
            area_below = 0.0
            for x, y, l in squares:
                if mid <= y:
                    # Square entirely above
                    pass
                elif mid >= y + l:
                    # Square entirely below
                    area_below += l * l
                else:
                    # Square is split
                    area_below += l * (mid - y)
            if area_below < half:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2.0
""",
    explanation="""### Approach: Binary Search on Y-coordinate

**Time Complexity:** O(n * log(range / epsilon))
**Space Complexity:** O(1)

1. Compute the total area of all squares and find the target: `total_area / 2`.
2. Binary search on the y-coordinate between the lowest bottom edge and the highest top edge.
3. For each candidate y value, compute the area below the line by checking each square:
   - If the square is entirely below (y >= top of square), add its full area.
   - If the square is entirely above (y <= bottom of square), add nothing.
   - If the line cuts through the square, add `width * (y - bottom)`.
4. If area below is less than half, move the line up. Otherwise, move it down.
5. After ~100 iterations, the precision is sufficient (about 30 decimal digits).

**Why this works:** The area below the line is a monotonically increasing function of y. Binary search finds the exact y-coordinate where the area below equals half the total area."""
)

# 6: Zigzag Conversion
_register(6,
    description="""<h3>6. Zigzag Conversion</h3>
<p>The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this:</p>
<pre>P   A   H   N
A P L S I I G
Y   I   R</pre>
<p>And then read line by line: <code>"PAHNAPLSIIGYIR"</code></p>
<p>Write the code that will take a string and make this conversion given a number of rows.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: s = "A", numRows = 1
Output: "A"</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length &lt;= 1000</li>
<li>1 &lt;= numRows &lt;= 1000</li>
</ul>""",
    function_name="convert",
    template="""class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "PAYPALISHIRING", "numRows": 3}, "expected": "PAHNAPLSIIGYIR"},
        {"input": {"s": "PAYPALISHIRING", "numRows": 4}, "expected": "PINALSIGYAHRPI"},
        {"input": {"s": "A", "numRows": 1}, "expected": "A"},
        {"input": {"s": "AB", "numRows": 1}, "expected": "AB"},
        {"input": {"s": "ABC", "numRows": 2}, "expected": "ACB"},
    ],
    solution="""class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        return ''.join(rows)
""",
    explanation="""### Approach: Simulate Row by Row

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Create an array of strings, one per row.
2. Iterate through the string, assigning each character to the current row.
3. Zigzag movement: go down from row 0 to `numRows - 1`, then go up from `numRows - 1` to row 0, and repeat.
4. Reverse direction when hitting the top (row 0) or bottom (row `numRows - 1`).
5. Concatenate all rows to get the result.

**Why this works:** The zigzag pattern is simply characters distributed across rows in a bouncing pattern. By tracking which row each character belongs to and concatenating rows in order, we reconstruct the zigzag reading."""
)

# 10: Regular Expression Matching
_register(10,
    description="""<h3>10. Regular Expression Matching</h3>
<p>Given an input string <code>s</code> and a pattern <code>p</code>, implement regular expression matching with support for <code>'.'</code> and <code>'*'</code> where:</p>
<ul>
<li><code>'.'</code> Matches any single character.</li>
<li><code>'*'</code> Matches zero or more of the preceding element.</li>
</ul>
<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "aa", p = "a"
Output: false</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "aa", p = "a*"
Output: true</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: s = "ab", p = ".*"
Output: true</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length &lt;= 20</li>
<li>1 &lt;= p.length &lt;= 20</li>
<li><code>s</code> contains only lowercase English letters.</li>
<li><code>p</code> contains only lowercase English letters, <code>'.'</code>, and <code>'*'</code>.</li>
<li>It is guaranteed for each appearance of <code>'*'</code>, there will be a previous valid character to match.</li>
</ul>""",
    function_name="isMatch",
    template="""class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "aa", "p": "a"}, "expected": False},
        {"input": {"s": "aa", "p": "a*"}, "expected": True},
        {"input": {"s": "ab", "p": ".*"}, "expected": True},
        {"input": {"s": "aab", "p": "c*a*b"}, "expected": True},
        {"input": {"s": "mississippi", "p": "mis*is*ip*."}, "expected": True},
    ],
    solution="""class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
""",
    explanation="""### Approach: Dynamic Programming

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

1. Create a DP table where `dp[i][j]` means `s[:i]` matches `p[:j]`.
2. Base case: `dp[0][0] = True` (empty string matches empty pattern).
3. Initialize first row for patterns like `a*`, `a*b*` that can match the empty string.
4. For each cell, handle two cases:
   - If `p[j-1]` is `*`: either use zero occurrences (`dp[i][j-2]`) or, if the preceding character matches, use one more occurrence (`dp[i-1][j]`).
   - If `p[j-1]` is `.` or matches `s[i-1]`: carry forward the diagonal `dp[i-1][j-1]`.
5. Answer is `dp[m][n]`.

**Why this works:** The DP table exhaustively considers every possible way to match prefixes of `s` and `p`. The `*` operator creates branching: either skip the pattern pair entirely (zero matches) or consume one more character from `s` (if it matches)."""
)

# 12: Integer to Roman
_register(12,
    description="""<h3>12. Integer to Roman</h3>
<p>Given an integer, convert it to a roman numeral.</p>
<p>Roman numerals are formed by appending the conversions of decimal place values from largest to smallest. Converting a decimal place value into a Roman numeral has the following rules:</p>
<ul>
<li>Symbol: I=1, V=5, X=10, L=50, C=100, D=500, M=1000</li>
<li>Subtractive forms: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900</li>
</ul>
<p><strong>Example 1:</strong></p>
<pre>Input: num = 3749
Output: "MMMDCCXLIX"</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: num = 58
Output: "LVIII"</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: num = 1994
Output: "MCMXCIV"</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= num &lt;= 3999</li>
</ul>""",
    function_name="intToRoman",
    template="""class Solution:
    def intToRoman(self, num: int) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"num": 3749}, "expected": "MMMDCCXLIX"},
        {"input": {"num": 58}, "expected": "LVIII"},
        {"input": {"num": 1994}, "expected": "MCMXCIV"},
        {"input": {"num": 1}, "expected": "I"},
        {"input": {"num": 3999}, "expected": "MMMCMXCIX"},
    ],
    solution="""class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = []
        for val, sym in zip(values, symbols):
            while num >= val:
                result.append(sym)
                num -= val
        return ''.join(result)
""",
    explanation="""### Approach: Greedy with Value Table

**Time Complexity:** O(1) (bounded by max value 3999)
**Space Complexity:** O(1)

1. Create two parallel arrays: one with values (1000, 900, 500, ..., 1) and one with corresponding Roman numeral symbols.
2. Include the subtractive forms (900=CM, 400=CD, 90=XC, 40=XL, 9=IX, 4=IV) as separate entries.
3. Greedily subtract the largest possible value and append its symbol, repeating until the number reaches 0.

**Why this works:** Roman numerals are inherently greedy. By including the subtractive combinations in the value table, we naturally handle cases like 4 (IV) and 9 (IX) without special logic. The greedy approach always produces the correct shortest Roman numeral representation."""
)

# 16: 3Sum Closest
_register(16,
    description="""<h3>16. 3Sum Closest</h3>
<p>Given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>, find three integers in <code>nums</code> such that the sum is closest to <code>target</code>.</p>
<p>Return the sum of the three integers.</p>
<p>You may assume that each input would have exactly one solution.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [0,0,0], target = 1
Output: 0</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>3 &lt;= nums.length &lt;= 500</li>
<li>-1000 &lt;= nums[i] &lt;= 1000</li>
<li>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></li>
</ul>""",
    function_name="threeSumClosest",
    template="""class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [-1,2,1,-4], "target": 1}, "expected": 2},
        {"input": {"nums": [0,0,0], "target": 1}, "expected": 0},
        {"input": {"nums": [1,1,1,0], "target": -100}, "expected": 2},
        {"input": {"nums": [-1,0,1,1,55], "target": 3}, "expected": 2},
        {"input": {"nums": [1,2,3], "target": 6}, "expected": 6},
    ],
    solution="""class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    lo += 1
                elif total > target:
                    hi -= 1
                else:
                    return total
        return closest
""",
    explanation="""### Approach: Sort + Two Pointers

**Time Complexity:** O(n^2)
**Space Complexity:** O(1) (ignoring sort space)

1. Sort the array.
2. For each element `nums[i]`, use two pointers (`lo`, `hi`) on the remaining subarray.
3. Compute the three-sum. If it's closer to the target than the current best, update.
4. If the sum is less than target, move `lo` right to increase the sum. If greater, move `hi` left to decrease it. If equal, return immediately.

**Why this works:** Sorting enables the two-pointer technique. For a fixed first element, the two pointers efficiently search for the best pair sum. The total complexity is O(n^2), which is optimal for this problem since we must consider all triplets in the worst case."""
)

# 17: Letter Combinations of a Phone Number
_register(17,
    description="""<h3>17. Letter Combinations of a Phone Number</h3>
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>
<p>A mapping of digits to letters (just like on the telephone buttons):</p>
<pre>2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz</pre>
<p><strong>Example 1:</strong></p>
<pre>Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: digits = ""
Output: []</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: digits = "2"
Output: ["a","b","c"]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>0 &lt;= digits.length &lt;= 4</li>
<li><code>digits[i]</code> is a digit in the range ['2', '9'].</li>
</ul>""",
    function_name="letterCombinations",
    template="""class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"digits": "23"}, "expected": ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
        {"input": {"digits": ""}, "expected": []},
        {"input": {"digits": "2"}, "expected": ["a","b","c"]},
        {"input": {"digits": "9"}, "expected": ["w","x","y","z"]},
        {"input": {"digits": "22"}, "expected": ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]},
    ],
    solution="""class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []
        def backtrack(idx, path):
            if idx == len(digits):
                result.append(''.join(path))
                return
            for letter in phone[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return result
""",
    explanation="""### Approach: Backtracking

**Time Complexity:** O(4^n * n) where n is the length of digits
**Space Complexity:** O(n) for recursion depth

1. Map each digit to its corresponding letters.
2. Use backtracking to explore all combinations.
3. At each position, try every letter mapped to the current digit.
4. When we've processed all digits, add the current combination to the result.

**Why this works:** Each digit maps to 3-4 letters, and we need all possible combinations. Backtracking systematically explores every branch of the decision tree, building combinations character by character and undoing choices (backtracking) to explore all paths."""
)

# 18: 4Sum
_register(18,
    description="""<h3>18. 4Sum</h3>
<p>Given an array <code>nums</code> of <code>n</code> integers, return an array of all the <strong>unique</strong> quadruplets <code>[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>
<ul>
<li>0 &lt;= a, b, c, d &lt; n</li>
<li>a, b, c, d are <strong>distinct</strong></li>
<li>nums[a] + nums[b] + nums[c] + nums[d] == target</li>
</ul>
<p>You may return the answer in <strong>any order</strong>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 200</li>
<li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
<li>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></li>
</ul>""",
    function_name="fourSum",
    template="""class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,0,-1,0,-2,2], "target": 0}, "expected": [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]},
        {"input": {"nums": [2,2,2,2,2], "target": 8}, "expected": [[2,2,2,2]]},
        {"input": {"nums": [0,0,0,0], "target": 0}, "expected": [[0,0,0,0]]},
        {"input": {"nums": [1,2,3,4], "target": 10}, "expected": [[1,2,3,4]]},
        {"input": {"nums": [1,2,3,4], "target": 100}, "expected": []},
    ],
    solution="""class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if total == target:
                        result.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif total < target:
                        lo += 1
                    else:
                        hi -= 1
        return result
""",
    explanation="""### Approach: Sort + Two Pointers (k-Sum Generalization)

**Time Complexity:** O(n^3)
**Space Complexity:** O(1) (ignoring output)

1. Sort the array.
2. Fix the first two elements with nested loops (indices `i` and `j`).
3. Use two pointers (`lo`, `hi`) for the remaining two elements.
4. Skip duplicates at every level to avoid duplicate quadruplets.
5. When the sum equals the target, record the quadruplet and skip duplicates.

**Why this works:** This extends the 3Sum approach by adding one more loop. Sorting allows duplicate skipping and two-pointer optimization. The two-pointer technique reduces the innermost search from O(n^2) to O(n), giving O(n^3) overall."""
)

# 19: Remove Nth Node From End of List
_register(19,
    description="""<h3>19. Remove Nth Node From End of List</h3>
<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>
<p>For this problem, use plain lists (e.g., [1,2,3,4,5]) as input/output.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: head = [1], n = 1
Output: []</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: head = [1,2], n = 1
Output: [1]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>The number of nodes in the list is <code>sz</code>.</li>
<li>1 &lt;= sz &lt;= 30</li>
<li>0 &lt;= Node.val &lt;= 100</li>
<li>1 &lt;= n &lt;= sz</li>
</ul>""",
    function_name="removeNthFromEnd",
    template="""class Solution:
    def removeNthFromEnd(self, head: list[int], n: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,2,3,4,5], "n": 2}, "expected": [1,2,3,5]},
        {"input": {"head": [1], "n": 1}, "expected": []},
        {"input": {"head": [1,2], "n": 1}, "expected": [1]},
        {"input": {"head": [1,2], "n": 2}, "expected": [2]},
        {"input": {"head": [1,2,3], "n": 3}, "expected": [2,3]},
    ],
    solution="""class Solution:
    def removeNthFromEnd(self, head: list[int], n: int) -> list[int]:
        idx = len(head) - n
        return head[:idx] + head[idx + 1:]
""",
    explanation="""### Approach: Direct Index (Plain List)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Since we're using plain lists, compute the index of the node to remove: `len(head) - n`.
2. Return a new list with that element removed by slicing.

Note: In the traditional linked list version, you would use the two-pointer technique with a fast pointer `n` steps ahead of the slow pointer. When the fast pointer reaches the end, the slow pointer is at the node before the one to delete.

**Why this works:** The nth node from the end is at index `len - n` from the beginning. With plain lists, we can directly remove it by index."""
)

# 23: Merge k Sorted Lists
_register(23,
    description="""<h3>23. Merge k Sorted Lists</h3>
<p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>
<p>Merge all the linked-lists into one sorted linked-list and return it.</p>
<p>For this problem, use plain lists of lists (e.g., [[1,4,5],[1,3,4],[2,6]]) as input and a plain list as output.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: lists = []
Output: []</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: lists = [[]]
Output: []</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>k == lists.length</li>
<li>0 &lt;= k &lt;= 10<sup>4</sup></li>
<li>0 &lt;= lists[i].length &lt;= 500</li>
<li>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></li>
<li>lists[i] is sorted in ascending order.</li>
<li>The sum of lists[i].length will not exceed 10<sup>4</sup>.</li>
</ul>""",
    function_name="mergeKLists",
    template="""class Solution:
    def mergeKLists(self, lists: list[list[int]]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"lists": [[1,4,5],[1,3,4],[2,6]]}, "expected": [1,1,2,3,4,4,5,6]},
        {"input": {"lists": []}, "expected": []},
        {"input": {"lists": [[]]}, "expected": []},
        {"input": {"lists": [[1],[2],[3]]}, "expected": [1,2,3]},
        {"input": {"lists": [[5,6,7],[1,2,3]]}, "expected": [1,2,3,5,6,7]},
    ],
    solution="""class Solution:
    def mergeKLists(self, lists: list[list[int]]) -> list[int]:
        import heapq
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], i, 0))
        result = []
        while heap:
            val, list_idx, elem_idx = heapq.heappop(heap)
            result.append(val)
            if elem_idx + 1 < len(lists[list_idx]):
                heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
        return result
""",
    explanation="""### Approach: Min Heap (Priority Queue)

**Time Complexity:** O(N log k) where N is total elements, k is number of lists
**Space Complexity:** O(k) for the heap

1. Initialize a min heap with the first element from each non-empty list. Store tuples of (value, list_index, element_index).
2. Repeatedly extract the minimum from the heap and add it to the result.
3. Push the next element from the same list (if available) into the heap.
4. Continue until the heap is empty.

**Why this works:** The min heap always gives us the smallest element across all k lists in O(log k) time. Since each of the N total elements is pushed and popped exactly once, the total time is O(N log k), which is optimal for this problem."""
)

# 28: Find the Index of the First Occurrence in a String
_register(28,
    description="""<h3>28. Find the Index of the First Occurrence in a String</h3>
<p>Given two strings <code>haystack</code> and <code>needle</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: haystack = "sadbutsad", needle = "sad"
Output: 0</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: haystack = "leetcode", needle = "leeto"
Output: -1</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></li>
<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>""",
    function_name="strStr",
    template="""class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"haystack": "sadbutsad", "needle": "sad"}, "expected": 0},
        {"input": {"haystack": "leetcode", "needle": "leeto"}, "expected": -1},
        {"input": {"haystack": "hello", "needle": "ll"}, "expected": 2},
        {"input": {"haystack": "a", "needle": "a"}, "expected": 0},
        {"input": {"haystack": "abc", "needle": "c"}, "expected": 2},
    ],
    solution="""class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
""",
    explanation="""### Approach: Built-in String Search (or Sliding Window)

**Time Complexity:** O(n * m) worst case (O(n) average with good implementations)
**Space Complexity:** O(1)

1. Use Python's built-in `str.find()` which returns the index of the first occurrence, or -1 if not found.

Alternatively, for an interview, you could implement:
1. Slide a window of size `len(needle)` over `haystack`.
2. At each position, compare the substring with `needle`.
3. Return the first matching position, or -1 if no match is found.

**Why this works:** `str.find()` internally uses an optimized search algorithm. The sliding window approach compares the needle against every possible starting position in the haystack."""
)

# 32: Longest Valid Parentheses
_register(32,
    description="""<h3>32. Longest Valid Parentheses</h3>
<p>Given a string containing just the characters <code>'('</code> and <code>')'</code>, return the length of the longest valid (well-formed) parentheses substring.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: s = ""
Output: 0</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></li>
<li><code>s[i]</code> is '(' or ')'.</li>
</ul>""",
    function_name="longestValidParentheses",
    template="""class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "(()"}, "expected": 2},
        {"input": {"s": ")()())"}, "expected": 4},
        {"input": {"s": ""}, "expected": 0},
        {"input": {"s": "()()"}, "expected": 4},
        {"input": {"s": "(()())"}, "expected": 6},
    ],
    solution="""class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Stack stores indices; -1 is the base
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # New base
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
""",
    explanation="""### Approach: Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Initialize a stack with `-1` as a base index (represents the position before the start of a valid substring).
2. For each character:
   - If `(`, push its index onto the stack.
   - If `)`, pop from the stack.
     - If the stack becomes empty, push the current index as the new base.
     - Otherwise, compute the length of the current valid substring as `i - stack[-1]` and update the maximum.
3. Return the maximum length found.

**Why this works:** The stack always keeps track of the boundary of the last unmatched position. When we find a matching `)`, the distance from the current index to the top of the stack gives the length of the valid substring ending at the current position."""
)

# 35: Search Insert Position
_register(35,
    description="""<h3>35. Search Insert Position</h3>
<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>
<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [1,3,5,6], target = 5
Output: 2</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [1,3,5,6], target = 2
Output: 1</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: nums = [1,3,5,6], target = 7
Output: 4</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
<li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
<li><code>nums</code> contains distinct values sorted in ascending order.</li>
<li>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></li>
</ul>""",
    function_name="searchInsert",
    template="""class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,3,5,6], "target": 5}, "expected": 2},
        {"input": {"nums": [1,3,5,6], "target": 2}, "expected": 1},
        {"input": {"nums": [1,3,5,6], "target": 7}, "expected": 4},
        {"input": {"nums": [1,3,5,6], "target": 0}, "expected": 0},
        {"input": {"nums": [1], "target": 1}, "expected": 0},
    ],
    solution="""class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
""",
    explanation="""### Approach: Binary Search (bisect_left)

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

1. Use binary search to find the leftmost position where `target` should be inserted.
2. Initialize `lo = 0` and `hi = len(nums)` (note: `hi` is past the end).
3. If `nums[mid] < target`, target belongs to the right: `lo = mid + 1`.
4. Otherwise, target belongs at `mid` or to the left: `hi = mid`.
5. When `lo == hi`, that's the insertion position.

**Why this works:** This is equivalent to Python's `bisect_left`. It finds the leftmost index where `target` could be inserted while maintaining sorted order. If the target exists, it returns its index; otherwise, it returns where it would be inserted."""
)

# 37: Sudoku Solver
_register(37,
    description="""<h3>37. Sudoku Solver</h3>
<p>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>
<p>A sudoku solution must satisfy <strong>all of the following rules</strong>:</p>
<ul>
<li>Each of the digits <code>1-9</code> must occur exactly once in each row.</li>
<li>Each of the digits <code>1-9</code> must occur exactly once in each column.</li>
<li>Each of the digits <code>1-9</code> must occur exactly once in each of the 9 <code>3x3</code> sub-boxes of the grid.</li>
</ul>
<p>The <code>'.'</code> character indicates empty cells.</p>
<p><strong>Example:</strong></p>
<pre>Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: (solved board)</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>board.length == 9</li>
<li>board[i].length == 9</li>
<li>board[i][j] is a digit or '.'.</li>
<li>It is guaranteed that the input board has only one solution.</li>
</ul>""",
    function_name="solveSudoku",
    template="""class Solution:
    def solveSudoku(self, board: list[list[str]]) -> list[list[str]]:
        # Write your solution here (modify board in-place and return it)
        pass
""",
    test_cases=[
        {"input": {"board": [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]},
         "expected": [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],
                      ["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],
                      ["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
                      ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],
                      ["3","4","5","2","8","6","1","7","9"]]},
    ],
    solution="""class Solution:
    def solveSudoku(self, board: list[list[str]]) -> list[list[str]]:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    d = board[i][j]
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[(i // 3) * 3 + j // 3].add(d)

        def backtrack(idx):
            if idx == len(empty):
                return True
            r, c = empty[idx]
            box_id = (r // 3) * 3 + c // 3
            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_id]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box_id].add(d)
                    if backtrack(idx + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box_id].remove(d)
            return False

        backtrack(0)
        return board
""",
    explanation="""### Approach: Backtracking with Constraint Tracking

**Time Complexity:** O(9^m) where m is the number of empty cells (much faster in practice due to pruning)
**Space Complexity:** O(m) for recursion depth

1. Preprocess the board: record which digits are in each row, column, and 3x3 box. Collect all empty cells.
2. For each empty cell, try digits 1-9. Only attempt digits that don't violate any constraint.
3. If a digit is valid, place it and recurse to the next empty cell.
4. If no digit works, backtrack (undo the placement) and try the next option.
5. Return the board when all cells are filled.

**Why this works:** Backtracking systematically tries all valid digit placements. The constraint sets (rows, cols, boxes) enable O(1) validity checks, dramatically pruning the search space. Since the puzzle has a unique solution, the algorithm will find it."""
)

# 39: Combination Sum
_register(39,
    description="""<h3>39. Combination Sum</h3>
<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return a list of all <strong>unique combinations</strong> of <code>candidates</code> where the chosen numbers sum to <code>target</code>. You may return the combinations in <strong>any order</strong>.</p>
<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= candidates.length &lt;= 30</li>
<li>2 &lt;= candidates[i] &lt;= 40</li>
<li>All elements of <code>candidates</code> are distinct.</li>
<li>1 &lt;= target &lt;= 40</li>
</ul>""",
    function_name="combinationSum",
    template="""class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"candidates": [2,3,6,7], "target": 7}, "expected": [[2,2,3],[7]]},
        {"input": {"candidates": [2,3,5], "target": 8}, "expected": [[2,2,2,2],[2,3,3],[3,5]]},
        {"input": {"candidates": [2], "target": 1}, "expected": []},
        {"input": {"candidates": [1], "target": 3}, "expected": [[1,1,1]]},
        {"input": {"candidates": [7,3,2], "target": 7}, "expected": [[2,2,3],[7]]},
    ],
    solution="""class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return result
""",
    explanation="""### Approach: Backtracking

**Time Complexity:** O(n^(target/min)) where min is the smallest candidate
**Space Complexity:** O(target/min) for recursion depth

1. Sort the candidates for early termination.
2. Use backtracking starting from each candidate. Since we can reuse elements, recurse with the same index `i` (not `i + 1`).
3. If the remaining target is 0, we found a valid combination — add a copy of the path to results.
4. If the current candidate exceeds the remaining target, break (since candidates are sorted, all subsequent ones are also too large).

**Why this works:** By starting each recursive call at the current index (allowing reuse) and iterating forward (preventing duplicates), we systematically explore all valid combinations. Sorting enables the early break optimization."""
)

# 48: Rotate Image
_register(48,
    description="""<h3>48. Rotate Image</h3>
<p>You are given an <code>n x n</code> 2D <code>matrix</code> representing an image, rotate the image by <strong>90 degrees</strong> (clockwise).</p>
<p>You have to rotate the image <strong>in-place</strong>, which means you have to modify the input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the rotation.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>n == matrix.length == matrix[i].length</li>
<li>1 &lt;= n &lt;= 20</li>
<li>-1000 &lt;= matrix[i][j] &lt;= 1000</li>
</ul>""",
    function_name="rotate",
    template="""class Solution:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        # Write your solution here (modify matrix in-place and return it)
        pass
""",
    test_cases=[
        {"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "expected": [[7,4,1],[8,5,2],[9,6,3]]},
        {"input": {"matrix": [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]}, "expected": [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]},
        {"input": {"matrix": [[1]]}, "expected": [[1]]},
        {"input": {"matrix": [[1,2],[3,4]]}, "expected": [[3,1],[4,2]]},
    ],
    solution="""class Solution:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
        return matrix
""",
    explanation="""### Approach: Transpose + Reverse

**Time Complexity:** O(n^2)
**Space Complexity:** O(1)

1. **Transpose** the matrix: swap `matrix[i][j]` with `matrix[j][i]` for all `i < j`.
2. **Reverse** each row.

The composition of these two operations is equivalent to a 90-degree clockwise rotation.

**Why this works:** A 90-degree clockwise rotation maps position `(i, j)` to `(j, n-1-i)`. Transposing maps `(i, j)` to `(j, i)`, and then reversing each row maps `(j, i)` to `(j, n-1-i)`. The two operations together achieve the desired transformation in-place."""
)

# 55: Jump Game
_register(55,
    description="""<h3>55. Jump Game</h3>
<p>You are given an integer array <code>nums</code>. You are initially positioned at the array's <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>
<p>Return <code>true</code> if you can reach the last index, or <code>false</code> otherwise.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
<li>0 &lt;= nums[i] &lt;= 10<sup>5</sup></li>
</ul>""",
    function_name="canJump",
    template="""class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,3,1,1,4]}, "expected": True},
        {"input": {"nums": [3,2,1,0,4]}, "expected": False},
        {"input": {"nums": [0]}, "expected": True},
        {"input": {"nums": [2,0,0]}, "expected": True},
        {"input": {"nums": [1,1,1,1,1]}, "expected": True},
    ],
    solution="""class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
""",
    explanation="""### Approach: Greedy

**Time Complexity:** O(n)
**Space Complexity:** O(1)

1. Track `max_reach`, the farthest index we can reach so far.
2. Iterate through the array. At each index `i`:
   - If `i > max_reach`, we can't reach this index, so return False.
   - Otherwise, update `max_reach = max(max_reach, i + nums[i])`.
3. If we iterate through the entire array without returning False, the last index is reachable.

**Why this works:** At each position, we greedily extend our maximum reach. If at any point we're at an index beyond our maximum reach, we're stuck. This single-pass greedy approach works because if we can reach index `i`, we can also reach all indices before `i`."""
)

# 57: Insert Interval
_register(57,
    description="""<h3>57. Insert Interval</h3>
<p>You are given an array of non-overlapping intervals <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code> represent the start and the end of the <code>i<sup>th</sup></code> interval and <code>intervals</code> is sorted in ascending order by <code>start_i</code>. You are also given an interval <code>newInterval = [start, end]</code> that represents the interval to be inserted.</p>
<p>Insert <code>newInterval</code> into <code>intervals</code> such that <code>intervals</code> is still sorted in ascending order by <code>start_i</code> and <code>intervals</code> still does not have any overlapping intervals (merge overlapping intervals if necessary).</p>
<p>Return <code>intervals</code> after the insertion.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>0 &lt;= intervals.length &lt;= 10<sup>4</sup></li>
<li>intervals[i].length == 2</li>
<li>0 &lt;= start_i &lt;= end_i &lt;= 10<sup>5</sup></li>
<li><code>intervals</code> is sorted by start_i in ascending order.</li>
<li>newInterval.length == 2</li>
<li>0 &lt;= start &lt;= end &lt;= 10<sup>5</sup></li>
</ul>""",
    function_name="insert",
    template="""class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"intervals": [[1,3],[6,9]], "newInterval": [2,5]}, "expected": [[1,5],[6,9]]},
        {"input": {"intervals": [[1,2],[3,5],[6,7],[8,10],[12,16]], "newInterval": [4,8]}, "expected": [[1,2],[3,10],[12,16]]},
        {"input": {"intervals": [], "newInterval": [5,7]}, "expected": [[5,7]]},
        {"input": {"intervals": [[1,5]], "newInterval": [2,3]}, "expected": [[1,5]]},
        {"input": {"intervals": [[1,5]], "newInterval": [6,8]}, "expected": [[1,5],[6,8]]},
    ],
    solution="""class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        # Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
""",
    explanation="""### Approach: Linear Scan and Merge

**Time Complexity:** O(n)
**Space Complexity:** O(n) for the result

1. Add all intervals that end before the new interval starts (no overlap).
2. Merge all intervals that overlap with the new interval by expanding the new interval's start and end.
3. Add the merged new interval to the result.
4. Add all remaining intervals that start after the new interval ends.

**Why this works:** Since intervals are sorted by start time and non-overlapping, we can process them in three phases: before overlap, during overlap (merge), and after overlap. The merging phase extends the new interval to encompass all overlapping intervals."""
)

# 58: Length of Last Word
_register(58,
    description="""<h3>58. Length of Last Word</h3>
<p>Given a string <code>s</code> consisting of words and spaces, return the length of the <strong>last</strong> word in the string.</p>
<p>A <strong>word</strong> is a maximal substring consisting of non-space characters only.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: s = "Hello World"
Output: 5</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: s = "   fly me   to   the moon  "
Output: 4</pre>
<p><strong>Example 3:</strong></p>
<pre>Input: s = "luffy is still joyboy"
Output: 6</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= s.length &lt;= 10<sup>4</sup></li>
<li><code>s</code> consists of only English letters and spaces <code>' '</code>.</li>
<li>There is at least one word in <code>s</code>.</li>
</ul>""",
    function_name="lengthOfLastWord",
    template="""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "Hello World"}, "expected": 5},
        {"input": {"s": "   fly me   to   the moon  "}, "expected": 4},
        {"input": {"s": "luffy is still joyboy"}, "expected": 6},
        {"input": {"s": "a"}, "expected": 1},
        {"input": {"s": "   hello   "}, "expected": 5},
    ],
    solution="""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
""",
    explanation="""### Approach: Strip and Split

**Time Complexity:** O(n)
**Space Complexity:** O(n)

1. Strip trailing spaces from the string.
2. Split by spaces and take the last element.
3. Return its length.

Alternatively, iterate from the end: skip trailing spaces, then count characters until the next space or the beginning.

**Why this works:** `strip()` removes trailing spaces that could cause issues. `split()` breaks the string into words, and the last element of the resulting list is the last word."""
)

# 62: Unique Paths
_register(62,
    description="""<h3>62. Unique Paths</h3>
<p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>
<p>Given the two integers <code>m</code> and <code>n</code>, return the number of possible unique paths that the robot can take to reach the bottom-right corner.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: m = 3, n = 7
Output: 28</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: m = 3, n = 2
Output: 3</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>1 &lt;= m, n &lt;= 100</li>
</ul>""",
    function_name="uniquePaths",
    template="""class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"m": 3, "n": 7}, "expected": 28},
        {"input": {"m": 3, "n": 2}, "expected": 3},
        {"input": {"m": 1, "n": 1}, "expected": 1},
        {"input": {"m": 1, "n": 5}, "expected": 1},
        {"input": {"m": 7, "n": 3}, "expected": 28},
    ],
    solution="""class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]
""",
    explanation="""### Approach: Dynamic Programming (Space Optimized)

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

1. Create a 1D DP array of size `n`, initialized to 1 (the first row has only one path to each cell).
2. For each subsequent row, update each cell: `dp[j] += dp[j-1]`. This adds the paths from above (already in `dp[j]`) and from the left (`dp[j-1]`).
3. The answer is `dp[n-1]`.

**Why this works:** The number of paths to any cell is the sum of paths from the cell above and the cell to the left (since the robot can only move right or down). The 1D array reuses space: `dp[j]` before update holds the value from the previous row (paths from above), and `dp[j-1]` is already updated for the current row (paths from the left)."""
)

# 69: Sqrt(x)
_register(69,
    description="""<h3>69. Sqrt(x)</h3>
<p>Given a non-negative integer <code>x</code>, return the <em>square root of <code>x</code></em> rounded down to the nearest integer. The returned integer should be <strong>non-negative</strong> as well.</p>
<p>You <strong>must not</strong> use any built-in exponent function or operator.</p>
<p><strong>Example 1:</strong></p>
<pre>Input: x = 4
Output: 2</pre>
<p><strong>Example 2:</strong></p>
<pre>Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.</pre>
<p><strong>Constraints:</strong></p>
<ul>
<li>0 &lt;= x &lt;= 2<sup>31</sup> - 1</li>
</ul>""",
    function_name="mySqrt",
    template="""class Solution:
    def mySqrt(self, x: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"x": 4}, "expected": 2},
        {"input": {"x": 8}, "expected": 2},
        {"input": {"x": 0}, "expected": 0},
        {"input": {"x": 1}, "expected": 1},
        {"input": {"x": 2147483647}, "expected": 46340},
    ],
    solution="""class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 1, x // 2
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
""",
    explanation="""### Approach: Binary Search

**Time Complexity:** O(log x)
**Space Complexity:** O(1)

1. Handle edge cases: if `x < 2`, return `x`.
2. Binary search in the range `[1, x // 2]` (the square root of `x >= 2` is always `<= x // 2`).
3. For each `mid`, compute `mid * mid`:
   - If it equals `x`, return `mid` (exact square root).
   - If it's less than `x`, the answer might be larger: `lo = mid + 1`.
   - If it's greater than `x`, the answer is smaller: `hi = mid - 1`.
4. When the loop ends, `hi` is the largest integer whose square is `<= x`.

**Why this works:** We're searching for the largest integer `k` such that `k^2 <= x`. Binary search efficiently narrows the range. When the loop exits with `lo > hi`, `hi` holds the floor of the square root."""
)
