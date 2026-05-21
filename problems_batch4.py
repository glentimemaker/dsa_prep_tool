# Batch 4: Problems from frequency 37.5%

_register(383,
    description="""<h3>383. Ransom Note</h3>
<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code> if <code>ransomNote</code> can be constructed by using the letters from <code>magazine</code> and <code>false</code> otherwise.</p>
<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>
<h4>Example 1:</h4>
<pre>Input: ransomNote = "a", magazine = "b"
Output: false</pre>
<h4>Example 2:</h4>
<pre>Input: ransomNote = "aa", magazine = "ab"
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: ransomNote = "aa", magazine = "aab"
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; ransomNote.length, magazine.length &le; 10<sup>5</sup></li>
<li>ransomNote and magazine consist of lowercase English letters.</li>
</ul>""",
    function_name="canConstruct",
    template="""class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"ransomNote": "a", "magazine": "b"}, "expected": False},
        {"input": {"ransomNote": "aa", "magazine": "ab"}, "expected": False},
        {"input": {"ransomNote": "aa", "magazine": "aab"}, "expected": True},
        {"input": {"ransomNote": "", "magazine": "abc"}, "expected": True},
        {"input": {"ransomNote": "abc", "magazine": "aabbcc"}, "expected": True},
    ],
    solution="""class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] <= 0:
                return False
            mag_count[ch] -= 1
        return True
""",
    explanation="""**Approach: Character Counting**

**Time:** O(m + n) | **Space:** O(1) (at most 26 letters)

1. Count the frequency of each character in `magazine`.
2. Iterate through `ransomNote`, decrementing counts for each character.
3. If any character count drops below zero, we can't construct the note.

**Why this works:** We need each character in the ransom note to appear at least as many times in the magazine. Counting ensures we track available characters efficiently.
"""
)

_register(387,
    description="""<h3>387. First Unique Character in a String</h3>
<p>Given a string <code>s</code>, find the first non-repeating character in it and return its index. If it does not exist, return <code>-1</code>.</p>
<h4>Example 1:</h4>
<pre>Input: s = "leetcode"
Output: 0</pre>
<h4>Example 2:</h4>
<pre>Input: s = "loveleetcode"
Output: 2</pre>
<h4>Example 3:</h4>
<pre>Input: s = "aabb"
Output: -1</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; s.length &le; 10<sup>5</sup></li>
<li>s consists of only lowercase English letters.</li>
</ul>""",
    function_name="firstUniqChar",
    template="""class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "leetcode"}, "expected": 0},
        {"input": {"s": "loveleetcode"}, "expected": 2},
        {"input": {"s": "aabb"}, "expected": -1},
        {"input": {"s": "a"}, "expected": 0},
        {"input": {"s": "aadadaad"}, "expected": -1},
    ],
    solution="""class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
""",
    explanation="""**Approach: Hash Map Counting**

**Time:** O(n) | **Space:** O(1) (at most 26 letters)

1. Count the frequency of each character in the string.
2. Iterate through the string again, returning the index of the first character with count 1.
3. If no unique character is found, return -1.

**Why this works:** Two passes through the string -- first to count, second to find the earliest unique character. The hash map provides O(1) lookups.
"""
)

_register(410,
    description="""<h3>410. Split Array Largest Sum</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, split <code>nums</code> into <code>k</code> non-empty subarrays such that the largest sum of any subarray is minimized.</p>
<p>Return the minimized largest sum of the split.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum is 18.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,3,4,5], k = 2
Output: 9</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,4,4], k = 3
Output: 4</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 1000</li>
<li>0 &le; nums[i] &le; 10<sup>6</sup></li>
<li>1 &le; k &le; min(50, nums.length)</li>
</ul>""",
    function_name="splitArray",
    template="""class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [7,2,5,10,8], "k": 2}, "expected": 18},
        {"input": {"nums": [1,2,3,4,5], "k": 2}, "expected": 9},
        {"input": {"nums": [1,4,4], "k": 3}, "expected": 4},
        {"input": {"nums": [10], "k": 1}, "expected": 10},
        {"input": {"nums": [1,2,3,4,5], "k": 1}, "expected": 15},
    ],
    solution="""class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    count += 1
                    current = num
                else:
                    current += num
            return count <= k

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
""",
    explanation="""**Approach: Binary Search on Answer**

**Time:** O(n * log(sum - max)) | **Space:** O(1)

1. The answer lies between `max(nums)` (each element in its own subarray) and `sum(nums)` (single subarray).
2. Binary search on the maximum subarray sum. For each candidate `mid`, check if we can split into at most `k` subarrays.
3. The greedy check: iterate through `nums`, accumulating a running sum. When adding the next element exceeds `mid`, start a new subarray.
4. If the number of subarrays needed is <= k, `mid` is feasible; try smaller. Otherwise, try larger.

**Why this works:** The feasibility check is monotonic -- if a max sum `x` works, any `x' > x` also works. This allows binary search to efficiently find the minimum feasible value.
"""
)

_register(414,
    description="""<h3>414. Third Maximum Number</h3>
<p>Given an integer array <code>nums</code>, return the <strong>third distinct maximum</strong> number in this array. If the third maximum does not exist, return the <strong>maximum</strong> number.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,2,1]
Output: 1
Explanation: The first distinct maximum is 3. The second is 2. The third is 1.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2]
Output: 2
Explanation: The third distinct maximum does not exist, so the maximum (2) is returned.</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [2,2,3,1]
Output: 1
Explanation: The first distinct maximum is 3. The second is 2 (both 2's count as one). The third is 1.</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>4</sup></li>
<li>-2<sup>31</sup> &le; nums[i] &le; 2<sup>31</sup> - 1</li>
</ul>""",
    function_name="thirdMax",
    template="""class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3,2,1]}, "expected": 1},
        {"input": {"nums": [1,2]}, "expected": 2},
        {"input": {"nums": [2,2,3,1]}, "expected": 1},
        {"input": {"nums": [1,1,1]}, "expected": 1},
        {"input": {"nums": [5,2,2]}, "expected": 5},
    ],
    solution="""class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique = sorted(set(nums), reverse=True)
        if len(unique) >= 3:
            return unique[2]
        return unique[0]
""",
    explanation="""**Approach: Sort Unique Values**

**Time:** O(n log n) | **Space:** O(n)

1. Remove duplicates by converting to a set.
2. Sort the unique values in descending order.
3. If there are at least 3 distinct values, return the third one.
4. Otherwise, return the maximum (first element).

**Why this works:** By deduplicating first, we ensure we're looking at distinct maximums. Sorting makes it trivial to pick the third largest.
"""
)

_register(443,
    description="""<h3>443. String Compression</h3>
<p>Given an array of characters <code>chars</code>, compress it using the following algorithm:</p>
<p>Begin with an empty string <code>s</code>. For each group of consecutive repeating characters in <code>chars</code>:</p>
<ul>
<li>If the group's length is 1, append the character to <code>s</code>.</li>
<li>Otherwise, append the character followed by the group's length.</li>
</ul>
<p>The compressed string <code>s</code> should not be returned separately, but instead, be stored in the input character array <code>chars</code>. Note that group lengths that are 10 or longer will be split into multiple characters in <code>chars</code>.</p>
<p>After you are done modifying the input array, return the new length of the array.</p>
<h4>Example 1:</h4>
<pre>Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The first 6 characters of the input array should be: ["a","2","b","2","c","3"]</pre>
<h4>Example 2:</h4>
<pre>Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it's a single character.</pre>
<h4>Example 3:</h4>
<pre>Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The first 4 characters of the input array should be: ["a","b","1","2"]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; chars.length &le; 2000</li>
<li>chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.</li>
</ul>""",
    function_name="compress",
    template="""class Solution:
    def compress(self, chars: list[str]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"chars": ["a","a","b","b","c","c","c"]}, "expected": 6},
        {"input": {"chars": ["a"]}, "expected": 1},
        {"input": {"chars": ["a","b","b","b","b","b","b","b","b","b","b","b","b"]}, "expected": 4},
        {"input": {"chars": ["a","a","a","a","a","a","a","a","a","a"]}, "expected": 3},
        {"input": {"chars": ["a","b","c"]}, "expected": 3},
    ],
    solution="""class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            ch = chars[read]
            count = 0
            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
""",
    explanation="""**Approach: Two Pointers (In-Place)**

**Time:** O(n) | **Space:** O(1)

1. Use a `read` pointer to scan groups of consecutive identical characters.
2. Use a `write` pointer to overwrite the array in-place with compressed data.
3. For each group, write the character. If the count is > 1, also write the digits of the count.
4. Return the `write` pointer as the new length.

**Why this works:** Since the compressed representation is always <= the original length, we can safely overwrite the array in-place without losing unprocessed data.
"""
)

_register(448,
    description="""<h3>448. Find All Numbers Disappeared in an Array</h3>
<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return an array of all the integers in the range <code>[1, n]</code> that do not appear in <code>nums</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,1]
Output: [2]</pre>
<h4>Constraints:</h4>
<ul>
<li>n == nums.length</li>
<li>1 &le; n &le; 10<sup>5</sup></li>
<li>1 &le; nums[i] &le; n</li>
</ul>""",
    function_name="findDisappearedNumbers",
    template="""class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [4,3,2,7,8,2,3,1]}, "expected": [5,6]},
        {"input": {"nums": [1,1]}, "expected": [2]},
        {"input": {"nums": [1,2,3]}, "expected": []},
        {"input": {"nums": [2,2]}, "expected": [1]},
        {"input": {"nums": [1]}, "expected": []},
    ],
    solution="""class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
""",
    explanation="""**Approach: Index Marking (In-Place)**

**Time:** O(n) | **Space:** O(1) (excluding output)

1. For each number `num`, mark the element at index `|num| - 1` as negative.
2. After marking, indices that still have positive values correspond to missing numbers.
3. Return `i + 1` for each index `i` where `nums[i]` is still positive.

**Why this works:** Each present number `x` marks position `x-1`. Missing numbers leave their corresponding positions unmarked (positive). Using absolute values avoids issues with already-marked positions.
"""
)

_register(485,
    description="""<h3>485. Max Consecutive Ones</h3>
<p>Given a binary array <code>nums</code>, return the maximum number of consecutive <code>1</code>'s in the array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,0,1,1,0,1]
Output: 2</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>5</sup></li>
<li>nums[i] is either 0 or 1.</li>
</ul>""",
    function_name="findMaxConsecutiveOnes",
    template="""class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,1,0,1,1,1]}, "expected": 3},
        {"input": {"nums": [1,0,1,1,0,1]}, "expected": 2},
        {"input": {"nums": [0]}, "expected": 0},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [1,1,1,1,1]}, "expected": 5},
    ],
    solution="""class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
""",
    explanation="""**Approach: Single Pass Counter**

**Time:** O(n) | **Space:** O(1)

1. Maintain a running counter of consecutive 1s.
2. When we see a 1, increment the counter and update the maximum.
3. When we see a 0, reset the counter to 0.
4. Return the maximum count seen.

**Why this works:** A simple linear scan tracking the current streak of 1s. Resetting on 0 ensures we only count consecutive runs.
"""
)

_register(518,
    description="""<h3>518. Coin Change II</h3>
<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>
<p>Return the number of combinations that make up that amount. If that amount cannot be made up by any combination of the coins, return <code>0</code>.</p>
<p>You may assume that you have an infinite number of each kind of coin.</p>
<h4>Example 1:</h4>
<pre>Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1</pre>
<h4>Example 2:</h4>
<pre>Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.</pre>
<h4>Example 3:</h4>
<pre>Input: amount = 10, coins = [10]
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; coins.length &le; 300</li>
<li>1 &le; coins[i] &le; 5000</li>
<li>0 &le; amount &le; 5000</li>
</ul>""",
    function_name="change",
    template="""class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"amount": 5, "coins": [1,2,5]}, "expected": 4},
        {"input": {"amount": 3, "coins": [2]}, "expected": 0},
        {"input": {"amount": 10, "coins": [10]}, "expected": 1},
        {"input": {"amount": 0, "coins": [1,2]}, "expected": 1},
        {"input": {"amount": 5, "coins": [1]}, "expected": 1},
    ],
    solution="""class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
""",
    explanation="""**Approach: Dynamic Programming (Unbounded Knapsack)**

**Time:** O(n * amount) | **Space:** O(amount)

1. Create a `dp` array where `dp[i]` = number of ways to make amount `i`.
2. Base case: `dp[0] = 1` (one way to make amount 0: use no coins).
3. For each coin, update `dp[x] += dp[x - coin]` for all `x >= coin`.
4. By iterating coins in the outer loop, we avoid counting permutations (only combinations).

**Why this works:** Processing one coin type at a time ensures each combination is counted exactly once. The inner loop allows unlimited use of the current coin (unbounded knapsack).
"""
)

_register(636,
    description="""<h3>636. Exclusive Time of Functions</h3>
<p>On a single-threaded CPU, we execute a program containing <code>n</code> functions. Each function has a unique ID between <code>0</code> and <code>n-1</code>.</p>
<p>Function calls are stored in a log, where each entry is a string in the format <code>"{function_id}:{start|end}:{timestamp}"</code>.</p>
<p>Return the exclusive time of each function in an array, where the value at index <code>i</code> is the exclusive time of the function with ID <code>i</code>.</p>
<h4>Example 1:</h4>
<pre>Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]</pre>
<h4>Example 2:</h4>
<pre>Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:end:6"]
Output: [7]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; n &le; 100</li>
<li>1 &le; logs.length &le; 500</li>
<li>0 &le; function_id &lt; n</li>
<li>0 &le; timestamp &le; 10<sup>9</sup></li>
<li>Logs are in chronological order.</li>
<li>Start and end logs always come in pairs.</li>
</ul>""",
    function_name="exclusiveTime",
    template="""class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 2, "logs": ["0:start:0","1:start:2","1:end:5","0:end:6"]}, "expected": [3,4]},
        {"input": {"n": 1, "logs": ["0:start:0","0:start:2","0:end:5","0:end:6"]}, "expected": [7]},
        {"input": {"n": 2, "logs": ["0:start:0","0:end:0","1:start:1","1:end:1"]}, "expected": [1,1]},
        {"input": {"n": 1, "logs": ["0:start:0","0:end:0"]}, "expected": [1]},
    ],
    solution="""class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            parts = log.split(':')
            fid = int(parts[0])
            typ = parts[1]
            time = int(parts[2])
            if typ == 'start':
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return result
""",
    explanation="""**Approach: Stack Simulation**

**Time:** O(L) where L = number of logs | **Space:** O(n)

1. Use a stack to track which function is currently running.
2. For each log entry, compute the elapsed time since the previous event.
3. On `start`: add elapsed time to the function currently on top of the stack, push new function.
4. On `end`: add elapsed time (+1 since end is inclusive) to the popped function, set prev_time to time+1.

**Why this works:** The stack tracks the call hierarchy. When a function starts, the previous function's exclusive time pauses. When it ends, time resumes for the caller. The +1 adjustment handles the inclusive end timestamp.
"""
)

_register(645,
    description="""<h3>645. Set Mismatch</h3>
<p>You have a set of integers <code>s</code>, which originally contains all the numbers from <code>1</code> to <code>n</code>. Unfortunately, due to some error, one of the numbers in <code>s</code> got duplicated to another number in the set, which results in <strong>repetition of one</strong> number and <strong>loss of another</strong> number.</p>
<p>You are given an integer array <code>nums</code> representing the data status of this set after the error.</p>
<p>Find the number that occurs twice and the number that is missing and return them in the form of an array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,2,4]
Output: [2,3]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,1]
Output: [1,2]</pre>
<h4>Constraints:</h4>
<ul>
<li>2 &le; nums.length &le; 10<sup>4</sup></li>
<li>1 &le; nums[i] &le; n</li>
</ul>""",
    function_name="findErrorNums",
    template="""class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,2,4]}, "expected": [2,3]},
        {"input": {"nums": [1,1]}, "expected": [1,2]},
        {"input": {"nums": [2,2]}, "expected": [2,1]},
        {"input": {"nums": [3,2,3,4,6,5]}, "expected": [3,1]},
        {"input": {"nums": [1,5,3,2,2,7,6,4]}, "expected": [2,8]},
    ],
    solution="""class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_set = set()
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]
""",
    explanation="""**Approach: Set + Math**

**Time:** O(n) | **Space:** O(n)

1. Find the duplicate by adding numbers to a set; the first repeat is the duplicate.
2. Compute the expected sum `n*(n+1)/2` and the actual sum.
3. The missing number = expected_sum - actual_sum + duplicate.

**Why this works:** The difference between expected and actual sums equals `missing - duplicate`. Since we know the duplicate, we can solve for the missing number directly.
"""
)

_register(695,
    description="""<h3>695. Max Area of Island</h3>
<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An <strong>island</strong> is a group of <code>1</code>'s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.</p>
<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>
<p>Return the <em>maximum area</em> of an island in <code>grid</code>. If there is no island, return <code>0</code>.</p>
<h4>Example 1:</h4>
<pre>Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.</pre>
<h4>Example 2:</h4>
<pre>Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li>m == grid.length</li>
<li>n == grid[i].length</li>
<li>1 &le; m, n &le; 50</li>
<li>grid[i][j] is either 0 or 1.</li>
</ul>""",
    function_name="maxAreaOfIsland",
    template="""class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"grid": [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                            [0,1,1,0,1,0,0,0,0,0,0,0,0],
                            [0,1,0,0,1,1,0,0,1,0,1,0,0],
                            [0,1,0,0,1,1,0,0,1,1,1,0,0],
                            [0,0,0,0,0,0,0,0,0,0,1,0,0],
                            [0,0,0,0,0,0,0,1,1,1,0,0,0],
                            [0,0,0,0,0,0,0,1,1,0,0,0,0]]}, "expected": 6},
        {"input": {"grid": [[0,0,0,0,0,0,0,0]]}, "expected": 0},
        {"input": {"grid": [[1]]}, "expected": 1},
        {"input": {"grid": [[1,1],[1,1]]}, "expected": 4},
        {"input": {"grid": [[1,0,1],[0,0,0],[1,0,1]]}, "expected": 1},
    ],
    solution="""class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0  # mark visited in place
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, dfs(r, c))
        return best
""",
    explanation="""**Approach: DFS Flood Fill**

**Time:** O(m * n) | **Space:** O(m * n) recursion stack worst case

1. Scan every cell. When you hit a `1`, launch a DFS that returns the size of that connected component.
2. Inside DFS, mark visited by overwriting the cell to `0` (avoids a separate `visited` set).
3. Each DFS returns `1 + sum(dfs neighbors)`; track the running max.

**Why this works:** Each land cell is visited at most once because we zero it out on first touch, so the total work is bounded by the grid size. The 4-direction connectivity is enforced by only recursing up/down/left/right.

**Alternative:** Iterative BFS with a queue avoids deep recursion if the grid is very large (Python's default recursion limit is ~1000).
"""
)

_register(743,
    description="""<h3>743. Network Delay Time</h3>
<p>You are given a network of <code>n</code> nodes, labeled from <code>1</code> to <code>n</code>. You are also given <code>times</code>, a list of travel times as directed edges <code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>, where <code>u<sub>i</sub></code> is the source node, <code>v<sub>i</sub></code> is the target node, and <code>w<sub>i</sub></code> is the time it takes for a signal to travel from source to target.</p>
<p>We will send a signal from a given node <code>k</code>. Return the <strong>minimum time</strong> it takes for all the <code>n</code> nodes to receive the signal. If it is impossible for all the <code>n</code> nodes to receive the signal, return <code>-1</code>.</p>
<h4>Example 1:</h4>
<pre>Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2</pre>
<h4>Example 2:</h4>
<pre>Input: times = [[1,2,1]], n = 2, k = 1
Output: 1</pre>
<h4>Example 3:</h4>
<pre>Input: times = [[1,2,1]], n = 2, k = 2
Output: -1</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; k &le; n &le; 100</li>
<li>1 &le; times.length &le; 6000</li>
<li>0 &le; w<sub>i</sub> &le; 100</li>
</ul>""",
    function_name="networkDelayTime",
    template="""class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"times": [[2,1,1],[2,3,1],[3,4,1]], "n": 4, "k": 2}, "expected": 2},
        {"input": {"times": [[1,2,1]], "n": 2, "k": 1}, "expected": 1},
        {"input": {"times": [[1,2,1]], "n": 2, "k": 2}, "expected": -1},
        {"input": {"times": [[1,2,1],[2,3,2],[1,3,4]], "n": 3, "k": 1}, "expected": 3},
        {"input": {"times": [[1,2,1],[2,1,3]], "n": 2, "k": 2}, "expected": 3},
    ],
    solution="""class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + w, nei))
        if len(dist) == n:
            return max(dist.values())
        return -1
""",
    explanation="""**Approach: Dijkstra's Algorithm**

**Time:** O(E log V) | **Space:** O(V + E)

1. Build an adjacency list from the edge list.
2. Run Dijkstra's algorithm from node `k` using a min-heap.
3. Track shortest distances to each node. Skip already-visited nodes.
4. If all `n` nodes are reached, return the maximum distance. Otherwise return -1.

**Why this works:** Dijkstra finds the shortest path from source to all reachable nodes. The answer is the maximum of these shortest paths, since all nodes must receive the signal.
"""
)

_register(778,
    description="""<h3>778. Swim in Rising Water</h3>
<p>You are given an <code>n x n</code> integer matrix <code>grid</code> where each value <code>grid[i][j]</code> represents the elevation at that point <code>(i, j)</code>.</p>
<p>The rain starts to fall. At time <code>t</code>, the depth of the water everywhere is <code>t</code>. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most <code>t</code>.</p>
<p>Return the least time until you can reach the bottom right square <code>(n - 1, n - 1)</code> starting from the top left square <code>(0, 0)</code>.</p>
<h4>Example 1:</h4>
<pre>Input: grid = [[0,2],[1,3]]
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16</pre>
<h4>Constraints:</h4>
<ul>
<li>n == grid.length == grid[i].length</li>
<li>1 &le; n &le; 50</li>
<li>0 &le; grid[i][j] &lt; n<sup>2</sup></li>
<li>Each value in grid is unique.</li>
</ul>""",
    function_name="swimInWater",
    template="""class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"grid": [[0,2],[1,3]]}, "expected": 3},
        {"input": {"grid": [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]}, "expected": 16},
        {"input": {"grid": [[0]]}, "expected": 0},
        {"input": {"grid": [[3,2],[0,1]]}, "expected": 3},
    ],
    solution="""class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        import heapq
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1
""",
    explanation="""**Approach: Modified Dijkstra / Min-Heap BFS**

**Time:** O(n^2 log n) | **Space:** O(n^2)

1. Use a min-heap priority queue, starting at `(grid[0][0], 0, 0)`.
2. The priority is the minimum time needed to reach each cell: `max(current_time, grid[nr][nc])`.
3. Always expand the cell reachable at the earliest time.
4. When we reach `(n-1, n-1)`, we have the minimum time.

**Why this works:** This is essentially finding the path where the maximum elevation along the path is minimized (minimax path). The heap ensures we always explore the lowest-cost option first.
"""
)

_register(799,
    description="""<h3>799. Champagne Tower</h3>
<p>We stack glasses in a pyramid, where the first row has <code>1</code> glass, the second row has <code>2</code> glasses, and so on until the 100th row. Each glass holds one cup of champagne.</p>
<p>Then, some champagne is poured into the first glass at the top. When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it. When those glasses become full, any excess overflows similarly.</p>
<p>Now after pouring some non-negative integer cups of champagne, return how much champagne is in the <code>j</code>-th glass of the <code>i</code>-th row (both 0-indexed).</p>
<h4>Example 1:</h4>
<pre>Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000</pre>
<h4>Example 2:</h4>
<pre>Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000</pre>
<h4>Example 3:</h4>
<pre>Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000</pre>
<h4>Constraints:</h4>
<ul>
<li>0 &le; poured &le; 10<sup>9</sup></li>
<li>0 &le; query_glass &le; query_row &lt; 100</li>
</ul>""",
    function_name="champagneTower",
    template="""class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"poured": 1, "query_row": 1, "query_glass": 1}, "expected": 0.0},
        {"input": {"poured": 2, "query_row": 1, "query_glass": 1}, "expected": 0.5},
        {"input": {"poured": 100000009, "query_row": 33, "query_glass": 17}, "expected": 1.0},
        {"input": {"poured": 0, "query_row": 0, "query_glass": 0}, "expected": 0.0},
        {"input": {"poured": 1, "query_row": 0, "query_glass": 0}, "expected": 1.0},
    ],
    solution="""class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured
        for row in range(query_row):
            for col in range(len(tower[row])):
                overflow = (tower[row][col] - 1.0) / 2.0
                if overflow > 0:
                    tower[row + 1][col] += overflow
                    tower[row + 1][col + 1] += overflow
        return min(1.0, tower[query_row][query_glass])
""",
    explanation="""**Approach: Simulation**

**Time:** O(query_row^2) | **Space:** O(query_row^2)

1. Create a 2D array representing the tower up to `query_row`.
2. Pour all champagne into `tower[0][0]`.
3. For each glass, if it overflows (holds > 1 cup), distribute the excess equally to the two glasses below.
4. The answer is `min(1.0, tower[query_row][query_glass])` since a glass can hold at most 1 cup.

**Why this works:** We simulate the physical process. Excess champagne flows down the pyramid, and we track cumulative flow into each glass. Capping at 1.0 gives the actual fill level.
"""
)

# 843: Requires special API interaction, skipped

_register(904,
    description="""<h3>904. Fruit Into Baskets</h3>
<p>You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the type of fruit the <code>i</code>th tree produces.</p>
<p>You want to collect as much fruit as possible. However, the owner has some strict rules:</p>
<ul>
<li>You only have <strong>two baskets</strong>, and each basket can only hold a <strong>single type</strong> of fruit.</li>
<li>Starting from any tree, you must pick exactly one fruit from every tree while moving to the right. You must stop when you encounter a tree with fruit that cannot fit in your baskets.</li>
</ul>
<p>Return the maximum number of fruits you can pick.</p>
<h4>Example 1:</h4>
<pre>Input: fruits = [1,2,1]
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: fruits = [0,1,2,2]
Output: 3</pre>
<h4>Example 3:</h4>
<pre>Input: fruits = [1,2,3,2,2]
Output: 4</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; fruits.length &le; 10<sup>5</sup></li>
<li>0 &le; fruits[i] &lt; fruits.length</li>
</ul>""",
    function_name="totalFruit",
    template="""class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"fruits": [1,2,1]}, "expected": 3},
        {"input": {"fruits": [0,1,2,2]}, "expected": 3},
        {"input": {"fruits": [1,2,3,2,2]}, "expected": 4},
        {"input": {"fruits": [3,3,3,1,2,1,1,2,3,3,4]}, "expected": 5},
        {"input": {"fruits": [1]}, "expected": 1},
    ],
    solution="""class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
""",
    explanation="""**Approach: Sliding Window**

**Time:** O(n) | **Space:** O(1) (at most 3 types in the map)

1. Use a sliding window with `left` and `right` pointers.
2. Expand `right`, adding fruits to a frequency map.
3. When the map has more than 2 types, shrink from `left` until we have at most 2 types.
4. Track the maximum window size.

**Why this works:** This is the "longest subarray with at most 2 distinct elements" problem. The sliding window efficiently maintains the constraint while maximizing the window size.
"""
)

_register(961,
    description="""<h3>961. N-Repeated Element in Size 2N Array</h3>
<p>You are given an integer array <code>nums</code> with the following properties:</p>
<ul>
<li><code>nums.length == 2 * n</code></li>
<li><code>nums</code> contains <code>n + 1</code> unique elements.</li>
<li>Exactly one element of <code>nums</code> is repeated <code>n</code> times.</li>
</ul>
<p>Return the element that is repeated <code>n</code> times.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,3]
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [2,1,2,5,3,2]
Output: 2</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [5,1,5,2,5,3,5,4]
Output: 5</pre>
<h4>Constraints:</h4>
<ul>
<li>2 &le; n &le; 5000</li>
<li>nums.length == 2 * n</li>
<li>0 &le; nums[i] &le; 10<sup>4</sup></li>
</ul>""",
    function_name="repeatedNTimes",
    template="""class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,3]}, "expected": 3},
        {"input": {"nums": [2,1,2,5,3,2]}, "expected": 2},
        {"input": {"nums": [5,1,5,2,5,3,5,4]}, "expected": 5},
        {"input": {"nums": [9,5,6,9]}, "expected": 9},
    ],
    solution="""class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
""",
    explanation="""**Approach: Hash Set**

**Time:** O(n) | **Space:** O(n)

1. Iterate through the array, tracking seen elements in a set.
2. The first element we see a second time is the repeated element.
3. This works because there are n+1 unique elements and one is repeated n times, so the repeated element must appear early.

**Why this works:** Since half the array is the repeated element and the other half has all unique elements, we're guaranteed to find a duplicate quickly.
"""
)

_register(977,
    description="""<h3>977. Squares of a Sorted Array</h3>
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return an array of <strong>the squares of each number</strong> sorted in non-decreasing order.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>4</sup></li>
<li>-10<sup>4</sup> &le; nums[i] &le; 10<sup>4</sup></li>
<li>nums is sorted in non-decreasing order.</li>
</ul>""",
    function_name="sortedSquares",
    template="""class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [-4,-1,0,3,10]}, "expected": [0,1,9,16,100]},
        {"input": {"nums": [-7,-3,2,3,11]}, "expected": [4,9,9,49,121]},
        {"input": {"nums": [0,1,2]}, "expected": [0,1,4]},
        {"input": {"nums": [-5,-3,-1]}, "expected": [1,9,25]},
        {"input": {"nums": [1]}, "expected": [1]},
    ],
    solution="""class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result
""",
    explanation="""**Approach: Two Pointers**

**Time:** O(n) | **Space:** O(n)

1. Use two pointers at the start and end of the array.
2. Compare absolute values: the larger one produces the larger square.
3. Place the larger square at the end of the result array, working backwards.
4. Move the corresponding pointer inward.

**Why this works:** The largest squares come from either the most negative or most positive numbers (at the extremes of the sorted array). By comparing from both ends, we fill the result from largest to smallest in O(n).
"""
)

_register(992,
    description="""<h3>992. Subarrays with K Different Integers</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the number of <strong>good subarrays</strong> of <code>nums</code>.</p>
<p>A good subarray is a subarray where the number of different integers in that subarray is exactly <code>k</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 2 * 10<sup>4</sup></li>
<li>1 &le; nums[i], k &le; nums.length</li>
</ul>""",
    function_name="subarraysWithKDistinct",
    template="""class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,1,2,3], "k": 2}, "expected": 7},
        {"input": {"nums": [1,2,1,3,4], "k": 3}, "expected": 3},
        {"input": {"nums": [1,1,1,1], "k": 1}, "expected": 10},
        {"input": {"nums": [1,2,3], "k": 3}, "expected": 1},
        {"input": {"nums": [2,1,1,1,2], "k": 1}, "expected": 8},
    ],
    solution="""class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def at_most_k(k):
            from collections import defaultdict
            count = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result
        return at_most_k(k) - at_most_k(k - 1)
""",
    explanation="""**Approach: Sliding Window (Exactly K = AtMost(K) - AtMost(K-1))**

**Time:** O(n) | **Space:** O(n)

1. Define a helper `at_most_k(k)` that counts subarrays with at most `k` distinct integers using a sliding window.
2. For each window `[left, right]`, the number of valid subarrays ending at `right` is `right - left + 1`.
3. The answer for exactly `k` distinct = `at_most_k(k) - at_most_k(k-1)`.

**Why this works:** Counting "exactly k" is hard with a single sliding window, but "at most k" is straightforward. The difference between "at most k" and "at most k-1" gives exactly "exactly k".
"""
)

_register(994,
    description="""<h3>994. Rotting Oranges</h3>
<p>You are given an <code>m x n</code> grid where each cell can have one of three values:</p>
<ul>
<li><code>0</code> representing an empty cell,</li>
<li><code>1</code> representing a fresh orange, or</li>
<li><code>2</code> representing a rotten orange.</li>
</ul>
<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>
<p>Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return <code>-1</code>.</p>
<h4>Example 1:</h4>
<pre>Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4</pre>
<h4>Example 2:</h4>
<pre>Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1</pre>
<h4>Example 3:</h4>
<pre>Input: grid = [[0,2]]
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li>m == grid.length</li>
<li>n == grid[i].length</li>
<li>1 &le; m, n &le; 10</li>
<li>grid[i][j] is 0, 1, or 2.</li>
</ul>""",
    function_name="orangesRotting",
    template="""class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"grid": [[2,1,1],[1,1,0],[0,1,1]]}, "expected": 4},
        {"input": {"grid": [[2,1,1],[0,1,1],[1,0,1]]}, "expected": -1},
        {"input": {"grid": [[0,2]]}, "expected": 0},
        {"input": {"grid": [[0]]}, "expected": 0},
        {"input": {"grid": [[2,2],[1,1],[0,0],[2,0]]}, "expected": 1},
    ],
    solution="""class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes - 1 if fresh == 0 else -1
""",
    explanation="""**Approach: Multi-source BFS**

**Time:** O(m * n) | **Space:** O(m * n)

1. Find all initially rotten oranges and add them to a queue. Count fresh oranges.
2. Perform BFS level by level. Each level represents one minute.
3. For each rotten orange, rot all adjacent fresh oranges and add them to the queue.
4. After BFS, if fresh oranges remain, return -1. Otherwise return the number of minutes.

**Why this works:** BFS from all rotten oranges simultaneously simulates the rotting process. Each BFS level is one minute of spread. We subtract 1 from minutes because the last level processes but doesn't add new oranges.
"""
)

_register(1004,
    description="""<h3>1004. Max Consecutive Ones III</h3>
<p>Given a binary array <code>nums</code> and an integer <code>k</code>, return the maximum number of consecutive <code>1</code>'s in the array if you can flip at most <code>k</code> <code>0</code>'s.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1] -- bolded are flipped</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>5</sup></li>
<li>nums[i] is either 0 or 1.</li>
<li>0 &le; k &le; nums.length</li>
</ul>""",
    function_name="longestOnes",
    template="""class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,1,1,0,0,0,1,1,1,1,0], "k": 2}, "expected": 6},
        {"input": {"nums": [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], "k": 3}, "expected": 10},
        {"input": {"nums": [0,0,0,0], "k": 0}, "expected": 0},
        {"input": {"nums": [1,1,1,1], "k": 0}, "expected": 4},
        {"input": {"nums": [0,0,0], "k": 3}, "expected": 3},
    ],
    solution="""class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
""",
    explanation="""**Approach: Sliding Window**

**Time:** O(n) | **Space:** O(1)

1. Maintain a sliding window `[left, right]` tracking the number of zeros inside.
2. Expand `right`. If the new element is 0, increment zero count.
3. If zero count exceeds `k`, shrink from `left` until zeros <= k.
4. Track the maximum window size.

**Why this works:** The window represents the longest contiguous subarray achievable by flipping at most `k` zeros. The sliding window efficiently maintains this constraint.
"""
)

_register(1015,
    description="""<h3>1015. Smallest Integer Divisible by K</h3>
<p>Given a positive integer <code>k</code>, you need to find the <strong>length</strong> of the <strong>smallest</strong> positive integer <code>n</code> such that <code>n</code> is divisible by <code>k</code>, and <code>n</code> only contains the digit <code>1</code>.</p>
<p>Return the length of <code>n</code>. If there is no such <code>n</code>, return <code>-1</code>.</p>
<p><strong>Note:</strong> <code>n</code> may not fit in a 64-bit signed integer.</p>
<h4>Example 1:</h4>
<pre>Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.</pre>
<h4>Example 2:</h4>
<pre>Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2 that only contains 1s.</pre>
<h4>Example 3:</h4>
<pre>Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; k &le; 10<sup>5</sup></li>
</ul>""",
    function_name="smallestRepunitDivByK",
    template="""class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"k": 1}, "expected": 1},
        {"input": {"k": 2}, "expected": -1},
        {"input": {"k": 3}, "expected": 3},
        {"input": {"k": 7}, "expected": 6},
        {"input": {"k": 5}, "expected": -1},
    ],
    solution="""class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
""",
    explanation="""**Approach: Remainder Tracking**

**Time:** O(k) | **Space:** O(1)

1. If `k` is divisible by 2 or 5, return -1 (repunits always end in 1, so they can't be divisible by 2 or 5).
2. Build the repunit incrementally: `remainder = (remainder * 10 + 1) % k`.
3. If remainder becomes 0, we found a repunit divisible by k; return its length.
4. By pigeonhole principle, if no solution is found within k iterations, return -1.

**Why this works:** We only track remainders mod k, avoiding huge number arithmetic. There are at most k distinct remainders, so by the pigeonhole principle, we either find a solution or detect a cycle within k steps.
"""
)

_register(1101,
    description="""<h3>1101. The Earliest Moment When Everyone Become Friends</h3>
<p>There are <code>n</code> people in a social group labeled from <code>0</code> to <code>n - 1</code>. You are given an array <code>logs</code> where <code>logs[i] = [timestamp<sub>i</sub>, x<sub>i</sub>, y<sub>i</sub>]</code> indicates that <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> will be friends at the time <code>timestamp<sub>i</sub></code>.</p>
<p>Friendship is <strong>symmetric</strong> and <strong>transitive</strong>. Return the <strong>earliest time</strong> for which every person became acquainted with every other person. If there is no such earliest time, return <code>-1</code>.</p>
<h4>Example 1:</h4>
<pre>Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301</pre>
<h4>Example 2:</h4>
<pre>Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3</pre>
<h4>Constraints:</h4>
<ul>
<li>2 &le; n &le; 100</li>
<li>1 &le; logs.length &le; 10<sup>4</sup></li>
<li>logs[i].length == 3</li>
<li>0 &le; x<sub>i</sub>, y<sub>i</sub> &le; n - 1</li>
<li>x<sub>i</sub> != y<sub>i</sub></li>
</ul>""",
    function_name="earliestAcq",
    template="""class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"logs": [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], "n": 6}, "expected": 20190301},
        {"input": {"logs": [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], "n": 4}, "expected": 3},
        {"input": {"logs": [[0,0,1]], "n": 3}, "expected": -1},
        {"input": {"logs": [[0,0,1],[1,1,2]], "n": 3}, "expected": 1},
    ],
    solution="""class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        logs.sort()
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            nonlocal components
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            components -= 1

        for timestamp, x, y in logs:
            union(x, y)
            if components == 1:
                return timestamp
        return -1
""",
    explanation="""**Approach: Union-Find (Disjoint Set Union)**

**Time:** O(L log L + L * alpha(n)) where L = logs length | **Space:** O(n)

1. Sort logs by timestamp to process friendships chronologically.
2. Use Union-Find to merge friend groups.
3. Track the number of connected components. Start with `n` components.
4. After each union that merges two different groups, decrement the component count.
5. When components reaches 1, everyone is connected; return the current timestamp.

**Why this works:** Union-Find efficiently tracks connected components. Processing in time order ensures we find the earliest moment all people are transitively connected.
"""
)

_register(1143,
    description="""<h3>1143. Longest Common Subsequence</h3>
<p>Given two strings <code>text1</code> and <code>text2</code>, return the length of their <strong>longest common subsequence</strong>. If there is no common subsequence, return <code>0</code>.</p>
<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>
<h4>Example 1:</h4>
<pre>Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.</pre>
<h4>Example 2:</h4>
<pre>Input: text1 = "abc", text2 = "abc"
Output: 3</pre>
<h4>Example 3:</h4>
<pre>Input: text1 = "abc", text2 = "def"
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; text1.length, text2.length &le; 1000</li>
<li>text1 and text2 consist of only lowercase English characters.</li>
</ul>""",
    function_name="longestCommonSubsequence",
    template="""class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"text1": "abcde", "text2": "ace"}, "expected": 3},
        {"input": {"text1": "abc", "text2": "abc"}, "expected": 3},
        {"input": {"text1": "abc", "text2": "def"}, "expected": 0},
        {"input": {"text1": "a", "text2": "a"}, "expected": 1},
        {"input": {"text1": "oxcpqrsvwf", "text2": "shmtulqrypy"}, "expected": 2},
    ],
    solution="""class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
""",
    explanation="""**Approach: Dynamic Programming (2D Table)**

**Time:** O(m * n) | **Space:** O(m * n)

1. Create a 2D DP table where `dp[i][j]` = LCS length of `text1[:i]` and `text2[:j]`.
2. If characters match (`text1[i-1] == text2[j-1]`), extend the LCS: `dp[i][j] = dp[i-1][j-1] + 1`.
3. Otherwise, take the best from excluding one character: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
4. Return `dp[m][n]`.

**Why this works:** The DP table systematically considers all possible subsequences by building up from smaller subproblems. Each cell represents the optimal solution for the corresponding prefixes.
"""
)

_register(1200,
    description="""<h3>1200. Minimum Absolute Difference</h3>
<p>Given an array of <strong>distinct</strong> integers <code>arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.</p>
<p>Return a list of pairs in ascending order (with respect to pairs), each pair <code>[a, b]</code> follows:</p>
<ul>
<li><code>a, b</code> are from <code>arr</code></li>
<li><code>a &lt; b</code></li>
<li><code>b - a</code> equals the minimum absolute difference of any two elements in <code>arr</code></li>
</ul>
<h4>Example 1:</h4>
<pre>Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]</pre>
<h4>Example 2:</h4>
<pre>Input: arr = [1,3,6,10,15]
Output: [[1,3]]</pre>
<h4>Example 3:</h4>
<pre>Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]</pre>
<h4>Constraints:</h4>
<ul>
<li>2 &le; arr.length &le; 10<sup>5</sup></li>
<li>-10<sup>6</sup> &le; arr[i] &le; 10<sup>6</sup></li>
</ul>""",
    function_name="minimumAbsDifference",
    template="""class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"arr": [4,2,1,3]}, "expected": [[1,2],[2,3],[3,4]]},
        {"input": {"arr": [1,3,6,10,15]}, "expected": [[1,3]]},
        {"input": {"arr": [3,8,-10,23,19,-4,-14,27]}, "expected": [[-14,-10],[19,23],[23,27]]},
        {"input": {"arr": [1,2]}, "expected": [[1,2]]},
    ],
    solution="""class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
        return result
""",
    explanation="""**Approach: Sort and Scan**

**Time:** O(n log n) | **Space:** O(1) (excluding output)

1. Sort the array. The minimum absolute difference must occur between adjacent elements in sorted order.
2. First pass: find the minimum difference among all adjacent pairs.
3. Second pass: collect all pairs with that minimum difference.

**Why this works:** Sorting guarantees that the closest elements are adjacent. We then make two passes: one to find the minimum gap, and one to collect all pairs matching that gap.
"""
)

# 1339: Complex tree problem, skipped

_register(1470,
    description="""<h3>1470. Shuffle the Array</h3>
<p>Given the array <code>nums</code> consisting of <code>2n</code> elements in the form <code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code>.</p>
<p>Return the array in the form <code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; n &le; 500</li>
<li>nums.length == 2n</li>
<li>1 &le; nums[i] &le; 10<sup>3</sup></li>
</ul>""",
    function_name="shuffle",
    template="""class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,5,1,3,4,7], "n": 3}, "expected": [2,3,5,4,1,7]},
        {"input": {"nums": [1,2,3,4,4,3,2,1], "n": 4}, "expected": [1,4,2,3,3,2,4,1]},
        {"input": {"nums": [1,1,2,2], "n": 2}, "expected": [1,2,1,2]},
        {"input": {"nums": [1,2], "n": 1}, "expected": [1,2]},
    ],
    solution="""class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
""",
    explanation="""**Approach: Direct Interleave**

**Time:** O(n) | **Space:** O(n)

1. Iterate from `i = 0` to `n - 1`.
2. For each `i`, append `nums[i]` (from the first half) and `nums[i + n]` (from the second half).
3. This interleaves the two halves as required.

**Why this works:** The first half contains x values at indices 0..n-1 and the second half contains y values at indices n..2n-1. Pairing them by offset produces the desired interleaved output.
"""
)

_register(1480,
    description="""<h3>1480. Running Sum of 1d Array</h3>
<p>Given an array <code>nums</code>. We define a running sum of an array as <code>runningSum[i] = sum(nums[0]...nums[i])</code>.</p>
<p>Return the running sum of <code>nums</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,4]
Output: [1,3,6,10]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 1000</li>
<li>-10<sup>6</sup> &le; nums[i] &le; 10<sup>6</sup></li>
</ul>""",
    function_name="runningSum",
    template="""class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,4]}, "expected": [1,3,6,10]},
        {"input": {"nums": [1,1,1,1,1]}, "expected": [1,2,3,4,5]},
        {"input": {"nums": [3,1,2,10,1]}, "expected": [3,4,6,16,17]},
        {"input": {"nums": [5]}, "expected": [5]},
    ],
    solution="""class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
""",
    explanation="""**Approach: Prefix Sum (In-Place)**

**Time:** O(n) | **Space:** O(1)

1. Starting from index 1, add the previous element to the current element.
2. Each element becomes the sum of all elements up to and including itself.
3. Return the modified array.

**Why this works:** Each position accumulates the sum of all previous positions. By modifying in-place from left to right, `nums[i-1]` already contains the running sum up to `i-1`, so adding it to `nums[i]` gives the running sum up to `i`.
"""
)

_register(1752,
    description="""<h3>1752. Check if Array Is Sorted and Rotated</h3>
<p>Given an array <code>nums</code>, return <code>true</code> if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return <code>false</code>.</p>
<p>There may be <strong>duplicates</strong> in the original array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] then rotate 3 positions.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [2,1,3,4]
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [1,2,3]
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 100</li>
<li>1 &le; nums[i] &le; 100</li>
</ul>""",
    function_name="check",
    template="""class Solution:
    def check(self, nums: list[int]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3,4,5,1,2]}, "expected": True},
        {"input": {"nums": [2,1,3,4]}, "expected": False},
        {"input": {"nums": [1,2,3]}, "expected": True},
        {"input": {"nums": [1,1,1]}, "expected": True},
        {"input": {"nums": [2,1]}, "expected": True},
    ],
    solution="""class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
""",
    explanation="""**Approach: Count Inversions**

**Time:** O(n) | **Space:** O(1)

1. Count the number of times `nums[i] > nums[(i+1) % n]` (wrap around to compare last with first).
2. A sorted-and-rotated array has at most 1 such "break point".
3. If count <= 1, the array is valid; otherwise it's not.

**Why this works:** A sorted array has 0 break points. Rotating it creates exactly 1 break point (where the rotation wraps). Using modular indexing handles the wrap-around comparison between the last and first elements.
"""
)

_register(1877,
    description="""<h3>1877. Minimize Maximum Pair Sum in Array</h3>
<p>The <strong>pair sum</strong> of a pair <code>(a, b)</code> is equal to <code>a + b</code>. The <strong>maximum pair sum</strong> is the largest pair sum in a list of pairs.</p>
<p>Given an array <code>nums</code> of <strong>even</strong> length <code>n</code>, pair up the elements into <code>n / 2</code> pairs such that:</p>
<ul>
<li>Each element of <code>nums</code> is in <strong>exactly one</strong> pair, and</li>
<li>The <strong>maximum pair sum</strong> is <strong>minimized</strong>.</li>
</ul>
<p>Return the minimized maximum pair sum after optimally pairing up the elements.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,5,2,3]
Output: 7
Explanation: The optimal pairing is (2,5) and (3,3) with max pair sum = 5+2 = 7... actually max(2+5, 3+3) = max(7,6) = 7.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: Optimal pairing: (2,6), (3,5), (4,4). Max pair sum = max(8,8,8) = 8.</pre>
<h4>Constraints:</h4>
<ul>
<li>n == nums.length</li>
<li>2 &le; n &le; 10<sup>5</sup></li>
<li>n is even.</li>
<li>1 &le; nums[i] &le; 10<sup>5</sup></li>
</ul>""",
    function_name="minPairSum",
    template="""class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3,5,2,3]}, "expected": 7},
        {"input": {"nums": [3,5,4,2,4,6]}, "expected": 8},
        {"input": {"nums": [1,2]}, "expected": 3},
        {"input": {"nums": [4,1,5,1,2,5,1,5,5,4]}, "expected": 8},
    ],
    solution="""class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
        return max_sum
""",
    explanation="""**Approach: Sort and Pair Extremes**

**Time:** O(n log n) | **Space:** O(1)

1. Sort the array.
2. Pair the smallest with the largest, second smallest with second largest, etc.
3. The answer is the maximum of all these pair sums.

**Why this works:** Pairing extremes balances the sums. If we paired two large numbers together, their sum would be very large. By pairing large with small, we distribute the "weight" evenly, minimizing the maximum pair sum.
"""
)

_register(1925,
    description="""<h3>1925. Count Square Sum Triples</h3>
<p>A <strong>square triple</strong> <code>(a, b, c)</code> is a triple where <code>a</code>, <code>b</code>, and <code>c</code> are integers and <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code>.</p>
<p>Given an integer <code>n</code>, return the number of <strong>square triples</strong> such that <code>1 &le; a, b, c &le; n</code>.</p>
<h4>Example 1:</h4>
<pre>Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).</pre>
<h4>Example 2:</h4>
<pre>Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; n &le; 250</li>
</ul>""",
    function_name="countTriples",
    template="""class Solution:
    def countTriples(self, n: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 5}, "expected": 2},
        {"input": {"n": 10}, "expected": 4},
        {"input": {"n": 1}, "expected": 0},
        {"input": {"n": 15}, "expected": 8},
    ],
    solution="""class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = set(i * i for i in range(1, n + 1))
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                if a * a + b * b in squares:
                    count += 2 if a != b else 1
        return count
""",
    explanation="""**Approach: Hash Set of Squares**

**Time:** O(n^2) | **Space:** O(n)

1. Precompute all perfect squares up to n^2 into a set.
2. For each pair (a, b) with a <= b, check if a^2 + b^2 is in the set AND c <= n.
3. If a != b, count both (a,b,c) and (b,a,c). If a == b, count once.

**Why this works:** Using a set for O(1) lookup of perfect squares avoids computing square roots. We only iterate pairs with a <= b to avoid double-counting, then add 2 for each valid pair (since order of a,b matters).
"""
)

_register(1975,
    description="""<h3>1975. Maximum Matrix Sum</h3>
<p>You are given an <code>n x n</code> integer <code>matrix</code>. You can do the following operation any number of times:</p>
<ul>
<li>Choose any two <strong>adjacent</strong> elements of <code>matrix</code> and <strong>multiply each of them by -1</strong>.</li>
</ul>
<p>Return the <strong>maximum sum</strong> of the matrix's elements using the operation.</p>
<h4>Example 1:</h4>
<pre>Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow these steps to reach sum 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.</pre>
<h4>Example 2:</h4>
<pre>Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16</pre>
<h4>Constraints:</h4>
<ul>
<li>n == matrix.length == matrix[i].length</li>
<li>2 &le; n &le; 250</li>
<li>-10<sup>5</sup> &le; matrix[i][j] &le; 10<sup>5</sup></li>
</ul>""",
    function_name="maxMatrixSum",
    template="""class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"matrix": [[1,-1],[-1,1]]}, "expected": 4},
        {"input": {"matrix": [[1,2,3],[-1,-2,-3],[1,2,3]]}, "expected": 16},
        {"input": {"matrix": [[1,-1],[2,-2]]}, "expected": 6},
        {"input": {"matrix": [[-1,0],[-1,1]]}, "expected": 3},
    ],
    solution="""class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    neg_count += 1
        if neg_count % 2 == 0:
            return total
        return total - 2 * min_abs
""",
    explanation="""**Approach: Greedy (Parity of Negatives)**

**Time:** O(n^2) | **Space:** O(1)

1. Sum the absolute values of all elements.
2. Count the number of negative values.
3. If the count of negatives is even, we can make all values positive -- return the total sum of absolute values.
4. If odd, one negative must remain. To minimize the loss, keep the element with the smallest absolute value as negative. Subtract `2 * min_abs` from the total.

**Why this works:** Each operation flips two adjacent elements' signs. We can "move" a negative sign anywhere by chaining operations. With an even number of negatives, all cancel out. With odd, we're stuck with one negative, so we minimize its impact.
"""
)

# 2188: Complex problem with tire degradation, skipped

_register(2235,
    description="""<h3>2235. Add Two Integers</h3>
<p>Given two integers <code>num1</code> and <code>num2</code>, return the <strong>sum</strong> of the two integers.</p>
<h4>Example 1:</h4>
<pre>Input: num1 = 12, num2 = 5
Output: 17</pre>
<h4>Example 2:</h4>
<pre>Input: num1 = -10, num2 = 4
Output: -6</pre>
<h4>Constraints:</h4>
<ul>
<li>-100 &le; num1, num2 &le; 100</li>
</ul>""",
    function_name="sum",
    template="""class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"num1": 12, "num2": 5}, "expected": 17},
        {"input": {"num1": -10, "num2": 4}, "expected": -6},
        {"input": {"num1": 0, "num2": 0}, "expected": 0},
        {"input": {"num1": -100, "num2": 100}, "expected": 0},
    ],
    solution="""class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
""",
    explanation="""**Approach: Direct Addition**

**Time:** O(1) | **Space:** O(1)

1. Return the sum of the two integers.

**Why this works:** This is a straightforward addition problem. Python's `+` operator handles all integer cases including negatives.
"""
)

_register(3010,
    description="""<h3>3010. Divide an Array Into Subarrays With Minimum Cost I</h3>
<p>You are given an array of integers <code>nums</code> of length <code>n</code>.</p>
<p>The cost of an array is the value of its <strong>first element</strong>. For example, the cost of <code>[1,2,3]</code> is <code>1</code> while the cost of <code>[3,4,1]</code> is <code>3</code>.</p>
<p>You need to divide <code>nums</code> into <strong>3 disjoint contiguous subarrays</strong>.</p>
<p>Return the <strong>minimum</strong> possible sum of the cost of these subarrays.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,12]
Output: 6
Explanation: The best way: [1,2], [3], [12] with costs 1 + 3 + 12... Actually: [1], [2], [3,12] with costs 1 + 2 + 3 = 6.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [5,4,3]
Output: 12
Explanation: The only way: [5], [4], [3] with costs 5 + 4 + 3 = 12.</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [10,3,1,1]
Output: 12
Explanation: [10], [3,1], [1] with costs 10 + 3 + 1 = 14. Or [10,3], [1], [1] with costs 10 + 1 + 1 = 12.</pre>
<h4>Constraints:</h4>
<ul>
<li>3 &le; nums.length &le; 50</li>
<li>1 &le; nums[i] &le; 50</li>
</ul>""",
    function_name="minimumCost",
    template="""class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,12]}, "expected": 6},
        {"input": {"nums": [5,4,3]}, "expected": 12},
        {"input": {"nums": [10,3,1,1]}, "expected": 12},
        {"input": {"nums": [1,1,1]}, "expected": 3},
        {"input": {"nums": [5,1,2,1,3]}, "expected": 7},
    ],
    solution="""class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        # First element is always the cost of the first subarray.
        # We need to pick 2 split points from nums[1:], and the cost
        # is nums[0] + the two smallest elements in nums[1:].
        rest = sorted(nums[1:])
        return nums[0] + rest[0] + rest[1]
""",
    explanation="""**Approach: Greedy (First Element + Two Smallest)**

**Time:** O(n log n) | **Space:** O(n)

1. The first subarray always starts at index 0, so its cost is `nums[0]` (fixed).
2. The other two subarrays each contribute their first element as cost.
3. To minimize total cost, we want the two smallest elements from `nums[1:]` as the starting elements of the other two subarrays.
4. We can always arrange splits to achieve this.

**Why this works:** Since we're splitting into contiguous subarrays, each split point determines the first element of the next subarray. The first subarray's cost is fixed. For the other two, picking the two smallest values from the remaining elements minimizes the total.
"""
)

# 3637: Recent problem, details uncertain, skipped

# 3721: Recent problem, details uncertain, skipped
