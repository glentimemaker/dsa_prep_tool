# Batch 5: LeetCode 75 study plan problems missing from earlier batches.
# Trees / linked lists are passed as flat list literals and reconstructed inside the solution.
# Class-based problems (Trie, RecentCounter, etc.) expose a function that replays operations.

_register(104,
    description="""<h3>104. Maximum Depth of Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, return its maximum depth.</p>
<p>A binary tree's <strong>maximum depth</strong> is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>
<h4>Example 1:</h4>
<pre>Input: root = [3,9,20,null,null,15,7]
Output: 3</pre>
<p><em>Tree is given as a level-order list with <code>None</code> for null nodes.</em></p>""",
    function_name="maxDepth",
    template="""class Solution:
    def maxDepth(self, root: list) -> int:
        # root is a level-order list, e.g. [3,9,20,None,None,15,7]
        pass
""",
    test_cases=[
        {"input": {"root": [3,9,20,None,None,15,7]}, "expected": 3},
        {"input": {"root": [1,None,2]}, "expected": 2},
        {"input": {"root": []}, "expected": 0},
        {"input": {"root": [1]}, "expected": 1},
        {"input": {"root": [1,2,3,4,5,None,None,6]}, "expected": 4},
    ],
    solution="""class Solution:
    def maxDepth(self, root: list) -> int:
        from collections import deque
        class T:
            def __init__(self, v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            root = T(next(it))
            q = deque([root])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try:
                    v2 = next(it)
                except StopIteration:
                    break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return root
        def depth(n):
            if not n: return 0
            return 1 + max(depth(n.l), depth(n.r))
        return depth(build(root))
""",
    explanation="""**Approach: Recursive DFS**

**Time:** O(n) | **Space:** O(h)

The depth of any node is `1 + max(depth(left), depth(right))`. Empty tree has depth 0. Standard recursion visits every node exactly once.
"""
)

_register(151,
    description="""<h3>151. Reverse Words in a String</h3>
<p>Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.</p>
<p>A <strong>word</strong> is defined as a sequence of non-space characters. The words in <code>s</code> will be separated by at least one space.</p>
<p>Return a string of the words in reverse order concatenated by a single space.</p>
<p><strong>Note:</strong> Your reversed string should not contain leading or trailing spaces. Reduce multiple spaces between words to a single space.</p>
<h4>Example 1:</h4>
<pre>Input: s = "the sky is blue"
Output: "blue is sky the"</pre>
<h4>Example 2:</h4>
<pre>Input: s = "  hello world  "
Output: "world hello"</pre>""",
    function_name="reverseWords",
    template="""class Solution:
    def reverseWords(self, s: str) -> str:
        pass
""",
    test_cases=[
        {"input": {"s": "the sky is blue"}, "expected": "blue is sky the"},
        {"input": {"s": "  hello world  "}, "expected": "world hello"},
        {"input": {"s": "a good   example"}, "expected": "example good a"},
        {"input": {"s": "  Bob    Loves  Alice   "}, "expected": "Alice Loves Bob"},
        {"input": {"s": "single"}, "expected": "single"},
    ],
    solution="""class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
""",
    explanation="""**Approach: Split + Reverse + Join**

**Time:** O(n) | **Space:** O(n)

`str.split()` (no arg) splits on any whitespace and drops empty tokens, handling multiple/leading/trailing spaces. Reverse and re-join with single spaces.
"""
)

_register(199,
    description="""<h3>199. Binary Tree Right Side View</h3>
<p>Given the <code>root</code> of a binary tree, imagine yourself standing on the <strong>right side</strong> of it, return the values of the nodes you can see ordered from top to bottom.</p>
<h4>Example 1:</h4>
<pre>Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]</pre>""",
    function_name="rightSideView",
    template="""class Solution:
    def rightSideView(self, root: list) -> list[int]:
        # root given as level-order list
        pass
""",
    test_cases=[
        {"input": {"root": [1,2,3,None,5,None,4]}, "expected": [1,3,4]},
        {"input": {"root": [1,None,3]}, "expected": [1,3]},
        {"input": {"root": []}, "expected": []},
        {"input": {"root": [1,2]}, "expected": [1,2]},
        {"input": {"root": [1,2,3,4]}, "expected": [1,3,4]},
    ],
    solution="""class Solution:
    def rightSideView(self, root: list) -> list[int]:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            root = T(next(it))
            q = deque([root])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return root
        r = build(root)
        if not r: return []
        out = []
        q = deque([r])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n-1: out.append(node.v)
                if node.l: q.append(node.l)
                if node.r: q.append(node.r)
        return out
""",
    explanation="""**Approach: BFS, Capture Last Node Per Level**

**Time:** O(n) | **Space:** O(w) where w is max width

Level-order traversal; the rightmost node in each level is the last one popped from that level.
"""
)

_register(208,
    description="""<h3>208. Implement Trie (Prefix Tree)</h3>
<p>A <strong>trie</strong> (pronounced as "try") or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>
<p>Implement the Trie class:</p>
<ul>
<li><code>Trie()</code> Initializes the trie object.</li>
<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
<li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
<li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>
<h4>Example 1:</h4>
<pre>Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; word.length, prefix.length &le; 2000</li>
<li>word and prefix consist only of lowercase English letters.</li>
<li>At most 3 * 10<sup>4</sup> calls in total will be made to insert, search, and startsWith.</li>
</ul>
<p><em>The test wrapper at the bottom replays a sequence of operations and arguments — do not modify it.</em></p>""",
    function_name="trie",
    template="""class Trie:
    def __init__(self):
        # Write your solution here
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# Test wrapper - do not modify
class Solution:
    def trie(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "Trie":
                obj = Trie()
                result.append(None)
            elif op == "insert":
                obj.insert(arg[0])
                result.append(None)
            elif op == "search":
                result.append(obj.search(arg[0]))
            elif op == "startsWith":
                result.append(obj.startsWith(arg[0]))
        return result
""",
    test_cases=[
        {"input": {"operations": ["Trie","insert","search","search","startsWith","insert","search"],
                   "arguments": [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]},
         "expected": [None, None, True, False, True, None, True]},
        {"input": {"operations": ["Trie","insert","search"], "arguments": [[],["a"],["a"]]},
         "expected": [None, None, True]},
        {"input": {"operations": ["Trie","search","startsWith"], "arguments": [[],["x"],["x"]]},
         "expected": [None, False, False]},
        {"input": {"operations": ["Trie","insert","insert","insert","search","search","search","startsWith","startsWith"],
                   "arguments": [[],["app"],["apple"],["beer"],["app"],["apple"],["application"],["app"],["ber"]]},
         "expected": [None, None, None, None, True, True, False, True, False]},
        {"input": {"operations": ["Trie","insert","search","insert","search"],
                   "arguments": [[],["abc"],["ab"],["ab"],["ab"]]},
         "expected": [None, None, False, None, True]},
    ],
    solution="""class Trie:
    def __init__(self):
        # Each node is a dict mapping char -> child node.
        # A node also carries an `is_end` flag (stored as the sentinel key '$').
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def _walk(self, s: str):
        # Walk along `s`; return the deepest node reached or None if a char is missing.
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.get('$', False)

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


class Solution:
    def trie(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "Trie":
                obj = Trie()
                result.append(None)
            elif op == "insert":
                obj.insert(arg[0])
                result.append(None)
            elif op == "search":
                result.append(obj.search(arg[0]))
            elif op == "startsWith":
                result.append(obj.startsWith(arg[0]))
        return result
""",
    explanation="""**Approach: Nested Hash Map per Node**

**Time:** O(L) per operation (L = string length) | **Space:** O(total characters inserted)

Each trie node is a dict whose keys are the next characters. A sentinel key (`'$'`) marks a node as the end of an inserted word so we can distinguish "this is a real word" from "this is only a prefix."

- **insert** walks/creates nodes for each char, then marks the last one with `$`.
- **search** walks the word; succeeds only if the walk completes *and* the final node has `$`.
- **startsWith** walks the prefix; succeeds if the walk completes.

A shared private helper `_walk(s)` keeps `search` and `startsWith` symmetric — they only differ in whether they check `$` at the end.

**Alternative — fixed-size arrays:** Using `children = [None]*26` per node (indexed by `ord(ch) - ord('a')`) avoids hash overhead and is what production implementations often use. Same asymptotic complexity, faster constants, more memory.

**Follow-ups worth practicing:**
- #211 Add and Search Word — Data structure design (supports `.` wildcards) — DFS over the trie at `.`.
- #212 Word Search II — Build a trie of all words, then DFS the board pruning by trie node existence.
"""
)

_register(216,
    description="""<h3>216. Combination Sum III</h3>
<p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that:</p>
<ul><li>Only numbers <code>1</code> through <code>9</code> are used.</li>
<li>Each number is used <strong>at most once</strong>.</li></ul>
<p>Return a list of all possible valid combinations.</p>
<h4>Example 1:</h4>
<pre>Input: k = 3, n = 7
Output: [[1,2,4]]</pre>
<h4>Example 2:</h4>
<pre>Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]</pre>""",
    function_name="combinationSum3",
    template="""class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        pass
""",
    test_cases=[
        {"input": {"k": 3, "n": 7}, "expected": [[1,2,4]]},
        {"input": {"k": 3, "n": 9}, "expected": [[1,2,6],[1,3,5],[2,3,4]]},
        {"input": {"k": 4, "n": 1}, "expected": []},
        {"input": {"k": 2, "n": 18}, "expected": []},
        {"input": {"k": 9, "n": 45}, "expected": [[1,2,3,4,5,6,7,8,9]]},
    ],
    solution="""class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        out = []
        def dfs(start, k_left, n_left, path):
            if k_left == 0:
                if n_left == 0: out.append(path[:])
                return
            for d in range(start, 10):
                if d > n_left: break
                path.append(d)
                dfs(d+1, k_left-1, n_left-d, path)
                path.pop()
        dfs(1, k, n, [])
        return out
""",
    explanation="""**Approach: Backtracking**

**Time:** O(C(9,k)) | **Space:** O(k)

Pick digits in increasing order to avoid duplicates. Prune when the candidate exceeds the remaining sum.
"""
)

_register(236,
    description="""<h3>236. Lowest Common Ancestor of a Binary Tree</h3>
<p>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes <code>p</code> and <code>q</code>.</p>
<p><em>Inputs: <code>root</code> as level-order list, <code>p</code> and <code>q</code> as the values of the two nodes (all node values are unique). Return the value of the LCA.</em></p>
<h4>Example 1:</h4>
<pre>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3</pre>""",
    function_name="lowestCommonAncestor",
    template="""class Solution:
    def lowestCommonAncestor(self, root: list, p: int, q: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"root": [3,5,1,6,2,0,8,None,None,7,4], "p": 5, "q": 1}, "expected": 3},
        {"input": {"root": [3,5,1,6,2,0,8,None,None,7,4], "p": 5, "q": 4}, "expected": 5},
        {"input": {"root": [1,2], "p": 1, "q": 2}, "expected": 1},
        {"input": {"root": [1,2,3,4,5], "p": 4, "q": 5}, "expected": 2},
    ],
    solution="""class Solution:
    def lowestCommonAncestor(self, root: list, p: int, q: int) -> int:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            root = T(next(it))
            qd = deque([root])
            for v in it:
                node = qd[0]
                if v is not None:
                    node.l = T(v); qd.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); qd.append(node.r)
                qd.popleft()
            return root
        def lca(n):
            if not n or n.v == p or n.v == q: return n
            L = lca(n.l); R = lca(n.r)
            if L and R: return n
            return L or R
        ans = lca(build(root))
        return ans.v if ans else -1
""",
    explanation="""**Approach: Recursive DFS**

**Time:** O(n) | **Space:** O(h)

If a node equals `p` or `q`, return it. Otherwise recurse on children; if both sides return a non-null, this node is the LCA. Otherwise propagate the non-null side up.
"""
)

_register(328,
    description="""<h3>328. Odd Even Linked List</h3>
<p>Given the <code>head</code> of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.</p>
<p>The <strong>first</strong> node is considered <strong>odd</strong>, and the second is even. Must run in O(1) extra space and O(n) time.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]</pre>""",
    function_name="oddEvenList",
    template="""# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,2,3,4,5]}, "expected": [1,3,5,2,4]},
        {"input": {"head": [2,1,3,5,6,4,7]}, "expected": [2,3,6,7,1,5,4]},
        {"input": {"head": []}, "expected": []},
        {"input": {"head": [1]}, "expected": [1]},
        {"input": {"head": [1,2]}, "expected": [1,2]},
    ],
    solution="""class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
""",
    explanation="""**Approach: Two-Pointer In-Place Re-link**

**Time:** O(n) | **Space:** O(1)

Maintain an `odd` pointer (1st, 3rd, 5th…) and an `even` pointer (2nd, 4th…). On each step, splice each pointer to its same-parity successor. At the end, attach the even chain after the odd chain.
""",
    harness={"input": {"head": "linked_list"}, "output": "linked_list"}
)

_register(334,
    description="""<h3>334. Increasing Triplet Subsequence</h3>
<p>Given an integer array <code>nums</code>, return <code>true</code> if there exists a triple of indices <code>(i, j, k)</code> such that <code>i &lt; j &lt; k</code> and <code>nums[i] &lt; nums[j] &lt; nums[k]</code>. Otherwise return <code>false</code>.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,4,5]
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [5,4,3,2,1]
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [2,1,5,0,4,6]
Output: true</pre>""",
    function_name="increasingTriplet",
    template="""class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,4,5]}, "expected": True},
        {"input": {"nums": [5,4,3,2,1]}, "expected": False},
        {"input": {"nums": [2,1,5,0,4,6]}, "expected": True},
        {"input": {"nums": [1,1,1,1]}, "expected": False},
        {"input": {"nums": [20,100,10,12,5,13]}, "expected": True},
    ],
    solution="""class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
""",
    explanation="""**Approach: Two Trailing Minimums**

**Time:** O(n) | **Space:** O(1)

Track the smallest value seen (`first`) and the smallest value seen that is strictly greater than some earlier value (`second`). Any new value strictly greater than `second` forms a valid triplet.

**Why it works:** Even if updating `first` later reflects an index after `second`, an earlier valid `first` still existed when `second` was assigned — `second` was set after some prior `first`. So when we find an `x > second`, a valid triplet exists in order.
"""
)

_register(338,
    description="""<h3>338. Counting Bits</h3>
<p>Given an integer <code>n</code>, return an array <code>ans</code> of length <code>n + 1</code> such that for each <code>i</code> (0 &le; i &le; n), <code>ans[i]</code> is the <strong>number of 1's</strong> in the binary representation of <code>i</code>.</p>
<h4>Example 1:</h4>
<pre>Input: n = 2
Output: [0,1,1]</pre>
<h4>Example 2:</h4>
<pre>Input: n = 5
Output: [0,1,1,2,1,2]</pre>""",
    function_name="countBits",
    template="""class Solution:
    def countBits(self, n: int) -> list[int]:
        pass
""",
    test_cases=[
        {"input": {"n": 2}, "expected": [0,1,1]},
        {"input": {"n": 5}, "expected": [0,1,1,2,1,2]},
        {"input": {"n": 0}, "expected": [0]},
        {"input": {"n": 8}, "expected": [0,1,1,2,1,2,2,3,1]},
    ],
    solution="""class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
""",
    explanation="""**Approach: DP via Bit Shift**

**Time:** O(n) | **Space:** O(n)

`popcount(i) == popcount(i >> 1) + (i & 1)`: dropping the low bit gives a smaller already-computed value; add 1 if that low bit was set.
"""
)

_register(374,
    description="""<h3>374. Guess Number Higher or Lower</h3>
<p>The system picks a number <code>pick</code> from <code>1</code> to <code>n</code>. Find it with as few guesses as possible.</p>
<p><em>Adapted for this runner: <code>guessNumber(n, pick)</code> takes both — your code must not look at <code>pick</code> directly, instead compare via a helper <code>guess(g)</code> already supplied. (The graded LeetCode version uses an API <code>guess(int)</code>; here it's the closure.)</em></p>
<h4>Example 1:</h4>
<pre>Input: n = 10, pick = 6
Output: 6</pre>""",
    function_name="guessNumber",
    template="""class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        # Use binary search. The hidden pick is passed in for testability.
        # In real LC you'd call guess(g) which returns -1/0/1.
        pass
""",
    test_cases=[
        {"input": {"n": 10, "pick": 6}, "expected": 6},
        {"input": {"n": 1, "pick": 1}, "expected": 1},
        {"input": {"n": 2, "pick": 1}, "expected": 1},
        {"input": {"n": 2, "pick": 2}, "expected": 2},
        {"input": {"n": 100, "pick": 73}, "expected": 73},
    ],
    solution="""class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        def guess(g):
            if g == pick: return 0
            return -1 if g > pick else 1
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            r = guess(mid)
            if r == 0: return mid
            elif r < 0: hi = mid - 1
            else: lo = mid + 1
        return -1
""",
    explanation="""**Approach: Binary Search**

**Time:** O(log n) | **Space:** O(1)

Classic binary search on the integer range [1, n], using the comparator `guess()`.
"""
)

_register(392,
    description="""<h3>392. Is Subsequence</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>s</code> is a subsequence of <code>t</code>.</p>
<h4>Example 1:</h4>
<pre>Input: s = "abc", t = "ahbgdc"
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: s = "axc", t = "ahbgdc"
Output: false</pre>""",
    function_name="isSubsequence",
    template="""class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass
""",
    test_cases=[
        {"input": {"s": "abc", "t": "ahbgdc"}, "expected": True},
        {"input": {"s": "axc", "t": "ahbgdc"}, "expected": False},
        {"input": {"s": "", "t": "abc"}, "expected": True},
        {"input": {"s": "abc", "t": ""}, "expected": False},
        {"input": {"s": "ace", "t": "abcde"}, "expected": True},
    ],
    solution="""class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)
""",
    explanation="""**Approach: Two-Pointer Walk**

**Time:** O(|t|) | **Space:** O(1)

Walk `t`, advancing a pointer in `s` whenever the current `t` character matches. If we consume all of `s`, it's a subsequence.
"""
)

_register(399,
    description="""<h3>399. Evaluate Division</h3>
<p>You are given equations <code>equations[i] = [Ai, Bi]</code> with values <code>values[i]</code>, meaning <code>Ai / Bi = values[i]</code>. You are also given queries. Return the answers; if undeterminable, return <code>-1.0</code>.</p>
<h4>Example 1:</h4>
<pre>Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]</pre>""",
    function_name="calcEquation",
    template="""class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass
""",
    test_cases=[
        {"input": {"equations": [["a","b"],["b","c"]], "values": [2.0,3.0],
                   "queries": [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]},
         "expected": [6.0, 0.5, -1.0, 1.0, -1.0]},
        {"input": {"equations": [["a","b"],["b","c"],["bc","cd"]], "values": [1.5,2.5,5.0],
                   "queries": [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]},
         "expected": [3.75, 0.4, 5.0, 0.2]},
        {"input": {"equations": [["a","b"]], "values": [0.5], "queries": [["a","b"],["b","a"],["a","c"],["x","y"]]},
         "expected": [0.5, 2.0, -1.0, -1.0]},
    ],
    solution="""class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque
        g = defaultdict(dict)
        for (a,b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1.0 / v
        def query(s, t):
            if s not in g or t not in g: return -1.0
            if s == t: return 1.0
            seen = {s}
            dq = deque([(s, 1.0)])
            while dq:
                n, prod = dq.popleft()
                if n == t: return prod
                for nb, w in g[n].items():
                    if nb not in seen:
                        seen.add(nb)
                        dq.append((nb, prod * w))
            return -1.0
        return [query(a, b) for a, b in queries]
""",
    explanation="""**Approach: Graph BFS with Multiplicative Weights**

**Time:** O(Q * (V + E)) | **Space:** O(V + E)

Treat each variable as a node and each equation `a/b = v` as edges `a -> b` (weight v) and `b -> a` (weight 1/v). Each query is a path search; multiply edge weights along the path. Unknown variable → -1.
"""
)

_register(435,
    description="""<h3>435. Non-overlapping Intervals</h3>
<p>Given an array of intervals where <code>intervals[i] = [start_i, end_i]</code>, return the minimum number of intervals you need to remove to make the rest non-overlapping.</p>
<h4>Example 1:</h4>
<pre>Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1</pre>""",
    function_name="eraseOverlapIntervals",
    template="""class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        pass
""",
    test_cases=[
        {"input": {"intervals": [[1,2],[2,3],[3,4],[1,3]]}, "expected": 1},
        {"input": {"intervals": [[1,2],[1,2],[1,2]]}, "expected": 2},
        {"input": {"intervals": [[1,2],[2,3]]}, "expected": 0},
        {"input": {"intervals": [[1,100],[11,22],[1,11],[2,12]]}, "expected": 2},
    ],
    solution="""class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        kept = 0
        for s, e in intervals:
            if s >= end:
                end = e
                kept += 1
        return len(intervals) - kept
""",
    explanation="""**Approach: Greedy by Earliest End**

**Time:** O(n log n) | **Space:** O(1)

Sort by ending time; keep each interval whose start is `>=` the last kept end. Maximizes how many we can keep; the rest must be removed.
"""
)

_register(437,
    description="""<h3>437. Path Sum III</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return the number of paths where the sum of values along the path equals <code>targetSum</code>.</p>
<p>The path does not need to start or end at the root, but it must go downwards (parent → child).</p>
<h4>Example 1:</h4>
<pre>Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3</pre>""",
    function_name="pathSum",
    template="""class Solution:
    def pathSum(self, root: list, targetSum: int) -> int:
        # root: level-order list with None for nulls
        pass
""",
    test_cases=[
        {"input": {"root": [10,5,-3,3,2,None,11,3,-2,None,1], "targetSum": 8}, "expected": 3},
        {"input": {"root": [5,4,8,11,None,13,4,7,2,None,None,5,1], "targetSum": 22}, "expected": 3},
        {"input": {"root": [], "targetSum": 0}, "expected": 0},
        {"input": {"root": [1], "targetSum": 1}, "expected": 1},
        {"input": {"root": [1,-2,-3], "targetSum": -1}, "expected": 1},
    ],
    solution="""class Solution:
    def pathSum(self, root: list, targetSum: int) -> int:
        from collections import deque, defaultdict
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            root = T(next(it))
            q = deque([root])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return root
        r = build(root)
        if not r: return 0
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        def dfs(n, cur):
            nonlocal count
            if not n: return
            cur += n.v
            count += prefix[cur - targetSum]
            prefix[cur] += 1
            dfs(n.l, cur); dfs(n.r, cur)
            prefix[cur] -= 1
        dfs(r, 0)
        return count
""",
    explanation="""**Approach: Prefix Sum + DFS**

**Time:** O(n) | **Space:** O(n)

Track running root-to-current path sum and a hashmap of prefix-sum counts. At each node, paths ending here that sum to `targetSum` correspond to prefixes equal to `cur - targetSum`. Decrement on backtrack to keep counts scoped to the current root→node path.
"""
)

_register(450,
    description="""<h3>450. Delete Node in a BST</h3>
<p>Given the <code>root</code> of a BST and a <code>key</code>, delete the node with that key and return the new root. The result should still be a valid BST.</p>
<p><em>Input/output: trees as level-order lists with <code>None</code> for nulls. Output is the new tree's level-order (trailing nulls trimmed).</em></p>
<h4>Example 1:</h4>
<pre>Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]</pre>""",
    function_name="deleteNode",
    template="""class Solution:
    def deleteNode(self, root: list, key: int) -> list:
        pass
""",
    test_cases=[
        {"input": {"root": [5,3,6,2,4,None,7], "key": 3}, "expected": [5,4,6,2,None,None,7]},
        {"input": {"root": [5,3,6,2,4,None,7], "key": 0}, "expected": [5,3,6,2,4,None,7]},
        {"input": {"root": [], "key": 0}, "expected": []},
        {"input": {"root": [1], "key": 1}, "expected": []},
        {"input": {"root": [2,1], "key": 2}, "expected": [1]},
    ],
    solution="""class Solution:
    def deleteNode(self, root: list, key: int) -> list:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            root = T(next(it))
            q = deque([root])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return root
        def serialize(r):
            if not r: return []
            out = []
            q = deque([r])
            while q:
                n = q.popleft()
                if n is None:
                    out.append(None)
                else:
                    out.append(n.v)
                    q.append(n.l); q.append(n.r)
            while out and out[-1] is None: out.pop()
            return out
        def delete(n, k):
            if not n: return None
            if k < n.v: n.l = delete(n.l, k)
            elif k > n.v: n.r = delete(n.r, k)
            else:
                if not n.l: return n.r
                if not n.r: return n.l
                succ = n.r
                while succ.l: succ = succ.l
                n.v = succ.v
                n.r = delete(n.r, succ.v)
            return n
        return serialize(delete(build(root), key))
""",
    explanation="""**Approach: Standard BST Deletion**

**Time:** O(h) | **Space:** O(h)

Recurse to find the node. If it has 0 or 1 child, return the other side. If it has 2 children, swap in the in-order successor's value and delete that successor from the right subtree.
"""
)

_register(452,
    description="""<h3>452. Minimum Number of Arrows to Burst Balloons</h3>
<p>Each balloon is an interval <code>[x_start, x_end]</code>. An arrow shot at x bursts every balloon with <code>x_start &le; x &le; x_end</code>. Return the minimum number of arrows to burst all balloons.</p>
<h4>Example 1:</h4>
<pre>Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2</pre>""",
    function_name="findMinArrowShots",
    template="""class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        pass
""",
    test_cases=[
        {"input": {"points": [[10,16],[2,8],[1,6],[7,12]]}, "expected": 2},
        {"input": {"points": [[1,2],[3,4],[5,6],[7,8]]}, "expected": 4},
        {"input": {"points": [[1,2],[2,3],[3,4],[4,5]]}, "expected": 2},
        {"input": {"points": [[1,2]]}, "expected": 1},
        {"input": {"points": []}, "expected": 0},
    ],
    solution="""class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda p: p[1])
        arrows = 1
        end = points[0][1]
        for s, e in points[1:]:
            if s > end:
                arrows += 1
                end = e
        return arrows
""",
    explanation="""**Approach: Greedy by Earliest End**

**Time:** O(n log n) | **Space:** O(1)

Sort by end. Shoot at the current earliest end; this bursts every overlapping balloon. Move to the next balloon whose start is strictly beyond the last shot's x.
"""
)

_register(547,
    description="""<h3>547. Number of Provinces</h3>
<p>Given an <code>n x n</code> matrix <code>isConnected</code> where <code>isConnected[i][j] = 1</code> if city i and j are directly connected. Return the total number of provinces (connected components).</p>
<h4>Example 1:</h4>
<pre>Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2</pre>""",
    function_name="findCircleNum",
    template="""class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        pass
""",
    test_cases=[
        {"input": {"isConnected": [[1,1,0],[1,1,0],[0,0,1]]}, "expected": 2},
        {"input": {"isConnected": [[1,0,0],[0,1,0],[0,0,1]]}, "expected": 3},
        {"input": {"isConnected": [[1,1,1],[1,1,1],[1,1,1]]}, "expected": 1},
        {"input": {"isConnected": [[1]]}, "expected": 1},
    ],
    solution="""class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        seen = [False]*n
        def dfs(i):
            seen[i] = True
            for j in range(n):
                if isConnected[i][j] and not seen[j]:
                    dfs(j)
        count = 0
        for i in range(n):
            if not seen[i]:
                dfs(i); count += 1
        return count
""",
    explanation="""**Approach: DFS Connected Components**

**Time:** O(n^2) | **Space:** O(n)

Walk each unvisited node and DFS to mark its whole component, incrementing a counter per fresh start.
"""
)

_register(605,
    description="""<h3>605. Can Place Flowers</h3>
<p>You have a flowerbed (array of 0s and 1s; 1 = planted, 0 = empty). Flowers can't be planted in adjacent plots. Given a number <code>n</code>, return <code>true</code> if it's possible to plant <code>n</code> new flowers without violating the rule.</p>
<h4>Example 1:</h4>
<pre>Input: flowerbed = [1,0,0,0,1], n = 1
Output: true</pre>""",
    function_name="canPlaceFlowers",
    template="""class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        pass
""",
    test_cases=[
        {"input": {"flowerbed": [1,0,0,0,1], "n": 1}, "expected": True},
        {"input": {"flowerbed": [1,0,0,0,1], "n": 2}, "expected": False},
        {"input": {"flowerbed": [0,0,1,0,0], "n": 1}, "expected": True},
        {"input": {"flowerbed": [0], "n": 1}, "expected": True},
        {"input": {"flowerbed": [1,0,0,0,0,1], "n": 2}, "expected": False},
        {"input": {"flowerbed": [0,0,0,0,0], "n": 3}, "expected": True},
    ],
    solution="""class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        bed = flowerbed[:]
        i = 0
        while i < len(bed):
            if bed[i] == 0 and (i == 0 or bed[i-1] == 0) and (i == len(bed)-1 or bed[i+1] == 0):
                bed[i] = 1
                n -= 1
                if n <= 0: return True
            i += 1
        return n <= 0
""",
    explanation="""**Approach: Greedy Plant When Safe**

**Time:** O(n) | **Space:** O(1) — though we copy here to avoid mutating input

Plant at every empty plot whose neighbors (if they exist) are also empty. Greedily planting at the earliest valid plot is always optimal because skipping it gains no future opportunity it would have blocked.
"""
)

_register(643,
    description="""<h3>643. Maximum Average Subarray I</h3>
<p>Find the contiguous subarray of length <code>k</code> with the maximum average. Return the maximum average value.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000</pre>""",
    function_name="findMaxAverage",
    template="""class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        pass
""",
    test_cases=[
        {"input": {"nums": [1,12,-5,-6,50,3], "k": 4}, "expected": 12.75},
        {"input": {"nums": [5], "k": 1}, "expected": 5.0},
        {"input": {"nums": [0,1,1,3,3], "k": 4}, "expected": 2.0},
        {"input": {"nums": [-1,-2,-3,-4], "k": 2}, "expected": -1.5},
    ],
    solution="""class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = sum(nums[:k])
        best = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            if s > best: best = s
        return best / k
""",
    explanation="""**Approach: Sliding Window**

**Time:** O(n) | **Space:** O(1)

Maintain the rolling sum of size-k windows. Track the maximum sum; divide by k once at the end.
"""
)

_register(649,
    description="""<h3>649. Dota2 Senate</h3>
<p>Each senator is either Radiant ('R') or Dire ('D'). In each round, every remaining senator (in turn order) may ban one opponent. The game continues until one party remains. Return <code>"Radiant"</code> or <code>"Dire"</code>.</p>
<h4>Example 1:</h4>
<pre>Input: senate = "RD"
Output: "Radiant"</pre>""",
    function_name="predictPartyVictory",
    template="""class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass
""",
    test_cases=[
        {"input": {"senate": "RD"}, "expected": "Radiant"},
        {"input": {"senate": "RDD"}, "expected": "Dire"},
        {"input": {"senate": "DDRRR"}, "expected": "Dire"},
        {"input": {"senate": "R"}, "expected": "Radiant"},
        {"input": {"senate": "DRRDRDRDRDDRDRDR"}, "expected": "Radiant"},
    ],
    solution="""class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        r = deque(); d = deque()
        n = len(senate)
        for i, c in enumerate(senate):
            (r if c == 'R' else d).append(i)
        while r and d:
            ri = r.popleft(); di = d.popleft()
            # the smaller index acts first, bans the other; survivor re-queues at end (i + n)
            if ri < di: r.append(ri + n)
            else: d.append(di + n)
        return 'Radiant' if r else 'Dire'
""",
    explanation="""**Approach: Two Queues of Indices**

**Time:** O(n) | **Space:** O(n)

Each senator's "turn" is their index. The earlier index acts first and bans the opponent. The winner re-queues with index + n to act in the next round. Whichever queue empties last wins.
"""
)

_register(700,
    description="""<h3>700. Search in a Binary Search Tree</h3>
<p>Given the root of a BST and an integer <code>val</code>, return the subtree rooted at the node with that value (as a level-order list), or an empty list if not found.</p>
<h4>Example 1:</h4>
<pre>Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]</pre>""",
    function_name="searchBST",
    template="""class Solution:
    def searchBST(self, root: list, val: int) -> list:
        pass
""",
    test_cases=[
        {"input": {"root": [4,2,7,1,3], "val": 2}, "expected": [2,1,3]},
        {"input": {"root": [4,2,7,1,3], "val": 5}, "expected": []},
        {"input": {"root": [], "val": 1}, "expected": []},
        {"input": {"root": [1], "val": 1}, "expected": [1]},
        {"input": {"root": [4,2,7,1,3], "val": 4}, "expected": [4,2,7,1,3]},
    ],
    solution="""class Solution:
    def searchBST(self, root: list, val: int) -> list:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            r = T(next(it))
            q = deque([r])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return r
        def serialize(r):
            if not r: return []
            out = []
            q = deque([r])
            while q:
                n = q.popleft()
                if n is None: out.append(None)
                else:
                    out.append(n.v); q.append(n.l); q.append(n.r)
            while out and out[-1] is None: out.pop()
            return out
        n = build(root)
        while n and n.v != val:
            n = n.l if val < n.v else n.r
        return serialize(n)
""",
    explanation="""**Approach: BST Iterative Search**

**Time:** O(h) | **Space:** O(1) for search; O(n) for serialization

Walk left if `val < node.val`, right otherwise. When we find the node (or run out), return its level-order serialization.
"""
)

_register(714,
    description="""<h3>714. Best Time to Buy and Sell Stock with Transaction Fee</h3>
<p>Maximize profit given prices and a transaction fee charged per sale.</p>
<h4>Example 1:</h4>
<pre>Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8</pre>""",
    function_name="maxProfit",
    template="""class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"prices": [1,3,2,8,4,9], "fee": 2}, "expected": 8},
        {"input": {"prices": [1,3,7,5,10,3], "fee": 3}, "expected": 6},
        {"input": {"prices": [1], "fee": 0}, "expected": 0},
        {"input": {"prices": [9,8,7,6,5], "fee": 1}, "expected": 0},
    ],
    solution="""class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return cash
""",
    explanation="""**Approach: DP with Two States**

**Time:** O(n) | **Space:** O(1)

`cash` = max profit not holding a share; `hold` = max profit currently holding. Transition each day: sell to update cash (subtract fee), or buy to update hold.
"""
)

_register(724,
    description="""<h3>724. Find Pivot Index</h3>
<p>Return the leftmost pivot index <code>i</code> where the sum of elements to the left of <code>i</code> equals the sum to the right. Return -1 if no such index exists.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,7,3,6,5,6]
Output: 3</pre>""",
    function_name="pivotIndex",
    template="""class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pass
""",
    test_cases=[
        {"input": {"nums": [1,7,3,6,5,6]}, "expected": 3},
        {"input": {"nums": [1,2,3]}, "expected": -1},
        {"input": {"nums": [2,1,-1]}, "expected": 0},
        {"input": {"nums": [-1,-1,-1,-1,-1,0]}, "expected": 2},
        {"input": {"nums": [1]}, "expected": 0},
    ],
    solution="""class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        return -1
""",
    explanation="""**Approach: Running Sums**

**Time:** O(n) | **Space:** O(1)

`right = total - left - nums[i]` at each i; the equality test is constant-time.
"""
)

_register(735,
    description="""<h3>735. Asteroid Collision</h3>
<p>Each asteroid moves at the same speed; positive = right, negative = left. If two collide, the smaller in magnitude explodes; if equal, both explode. Return the surviving asteroids.</p>
<h4>Example 1:</h4>
<pre>Input: asteroids = [5,10,-5]
Output: [5,10]</pre>""",
    function_name="asteroidCollision",
    template="""class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pass
""",
    test_cases=[
        {"input": {"asteroids": [5,10,-5]}, "expected": [5,10]},
        {"input": {"asteroids": [8,-8]}, "expected": []},
        {"input": {"asteroids": [10,2,-5]}, "expected": [10]},
        {"input": {"asteroids": [-2,-1,1,2]}, "expected": [-2,-1,1,2]},
        {"input": {"asteroids": [-2,2,1,-2]}, "expected": [-2]},
    ],
    solution="""class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for a in asteroids:
            while st and a < 0 < st[-1]:
                if st[-1] < -a:
                    st.pop()
                    continue
                elif st[-1] == -a:
                    st.pop()
                break
            else:
                st.append(a)
        return st
""",
    explanation="""**Approach: Stack**

**Time:** O(n) | **Space:** O(n)

Push each asteroid; if a leftward one collides with rightward tops, resolve until destroyed or it survives. Python's `for…else` runs the `else` only when the loop completed without `break` — used here to skip the append when the incoming asteroid was destroyed.
"""
)

_register(739,
    description="""<h3>739. Daily Temperatures</h3>
<p>Given a list of daily temperatures, return a list <code>answer</code> where <code>answer[i]</code> is the number of days until a warmer temperature. If no future day is warmer, set 0.</p>
<h4>Example 1:</h4>
<pre>Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]</pre>""",
    function_name="dailyTemperatures",
    template="""class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        pass
""",
    test_cases=[
        {"input": {"temperatures": [73,74,75,71,69,72,76,73]}, "expected": [1,1,4,2,1,1,0,0]},
        {"input": {"temperatures": [30,40,50,60]}, "expected": [1,1,1,0]},
        {"input": {"temperatures": [30,60,90]}, "expected": [1,1,0]},
        {"input": {"temperatures": [50,50,50]}, "expected": [0,0,0]},
        {"input": {"temperatures": [100]}, "expected": [0]},
    ],
    solution="""class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        out = [0] * len(temperatures)
        stack = []  # indices with strictly decreasing temperatures
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                out[j] = i - j
            stack.append(i)
        return out
""",
    explanation="""**Approach: Monotonic Stack**

**Time:** O(n) | **Space:** O(n)

Keep a stack of indices whose temperatures are still waiting for a warmer day. When today's temperature beats the top, pop and record the day-gap.
"""
)

_register(746,
    description="""<h3>746. Min Cost Climbing Stairs</h3>
<p>You pay <code>cost[i]</code> to step from stair i; from there you climb 1 or 2 steps. Start from stair 0 or 1. Return the minimum cost to reach the top (past index n-1).</p>
<h4>Example 1:</h4>
<pre>Input: cost = [10,15,20]
Output: 15</pre>""",
    function_name="minCostClimbingStairs",
    template="""class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        pass
""",
    test_cases=[
        {"input": {"cost": [10,15,20]}, "expected": 15},
        {"input": {"cost": [1,100,1,1,1,100,1,1,100,1]}, "expected": 6},
        {"input": {"cost": [0,0]}, "expected": 0},
        {"input": {"cost": [1,2]}, "expected": 1},
    ],
    solution="""class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i-1], a + cost[i-2])
        return b
""",
    explanation="""**Approach: Rolling DP**

**Time:** O(n) | **Space:** O(1)

`dp[i]` = min cost to reach stair i. `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`. Track just the last two values.
"""
)

_register(790,
    description="""<h3>790. Domino and Tromino Tiling</h3>
<p>Count the number of ways to tile a 2 × n board with dominoes and trominoes (L-shapes). Return mod 1e9 + 7.</p>
<h4>Example 1:</h4>
<pre>Input: n = 3
Output: 5</pre>""",
    function_name="numTilings",
    template="""class Solution:
    def numTilings(self, n: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"n": 1}, "expected": 1},
        {"input": {"n": 2}, "expected": 2},
        {"input": {"n": 3}, "expected": 5},
        {"input": {"n": 4}, "expected": 11},
        {"input": {"n": 5}, "expected": 24},
        {"input": {"n": 30}, "expected": 312342182},
    ],
    solution="""class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        # dp[i] = 2*dp[i-1] + dp[i-3]
        a, b, c = 1, 2, 5  # dp[1], dp[2], dp[3]
        for i in range(4, n + 1):
            a, b, c = b, c, (2*c + a) % MOD
        return c
""",
    explanation="""**Approach: Linear Recurrence**

**Time:** O(n) | **Space:** O(1)

Derive `dp[n] = 2*dp[n-1] + dp[n-3]` by case-analyzing how the last column(s) are completed. Iterate forward keeping only the last three values.
"""
)

_register(841,
    description="""<h3>841. Keys and Rooms</h3>
<p>There are n rooms (0 to n-1). You start in room 0. Each room has a list of keys to other rooms. Return <code>true</code> if you can visit every room.</p>
<h4>Example 1:</h4>
<pre>Input: rooms = [[1],[2],[3],[]]
Output: true</pre>""",
    function_name="canVisitAllRooms",
    template="""class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        pass
""",
    test_cases=[
        {"input": {"rooms": [[1],[2],[3],[]]}, "expected": True},
        {"input": {"rooms": [[1,3],[3,0,1],[2],[0]]}, "expected": False},
        {"input": {"rooms": [[]]}, "expected": True},
        {"input": {"rooms": [[1],[]]}, "expected": True},
    ],
    solution="""class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen = {0}
        stack = [0]
        while stack:
            r = stack.pop()
            for k in rooms[r]:
                if k not in seen:
                    seen.add(k); stack.append(k)
        return len(seen) == len(rooms)
""",
    explanation="""**Approach: DFS Reachability**

**Time:** O(n + total keys) | **Space:** O(n)

Start in room 0; iteratively visit every newly-keyed room. Reachable count == n means we can visit all.
"""
)

_register(872,
    description="""<h3>872. Leaf-Similar Trees</h3>
<p>Consider all leaves of a binary tree, from left to right, as forming a leaf value sequence. Two trees are leaf-similar if their sequences match.</p>
<p>Return <code>true</code> if and only if both given trees are leaf-similar. Trees given as level-order lists.</p>
<h4>Example 1:</h4>
<pre>Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true</pre>""",
    function_name="leafSimilar",
    template="""class Solution:
    def leafSimilar(self, root1: list, root2: list) -> bool:
        pass
""",
    test_cases=[
        {"input": {"root1": [3,5,1,6,2,9,8,None,None,7,4],
                   "root2": [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]}, "expected": True},
        {"input": {"root1": [1,2,3], "root2": [1,3,2]}, "expected": False},
        {"input": {"root1": [1], "root2": [1]}, "expected": True},
        {"input": {"root1": [1,2], "root2": [2,2]}, "expected": True},
    ],
    solution="""class Solution:
    def leafSimilar(self, root1: list, root2: list) -> bool:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            r = T(next(it))
            q = deque([r])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return r
        def leaves(n, acc):
            if not n: return
            if not n.l and not n.r:
                acc.append(n.v); return
            leaves(n.l, acc); leaves(n.r, acc)
        a, b = [], []
        leaves(build(root1), a); leaves(build(root2), b)
        return a == b
""",
    explanation="""**Approach: DFS Collect Leaves**

**Time:** O(n1 + n2) | **Space:** O(n1 + n2)

Walk each tree depth-first, recording values only at leaves. Compare the two sequences.
"""
)

_register(901,
    description="""<h3>901. Online Stock Span</h3>
<p>Design <code>StockSpanner</code>: <code>next(price)</code> returns the span (count of consecutive days, including today, where price &le; today's price going backwards).</p>
<p><em>Wrapped as a function: pass <code>operations</code> and parallel <code>arguments</code>. Constructor returns <code>None</code>.</em></p>
<h4>Example:</h4>
<pre>Input: ops = ["StockSpanner","next","next","next","next","next","next","next"]
       args = [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null, 1, 1, 1, 2, 1, 4, 6]</pre>""",
    function_name="stockSpannerOps",
    template="""class Solution:
    def stockSpannerOps(self, operations: list[str], arguments: list[list]) -> list:
        pass
""",
    test_cases=[
        {"input": {"operations": ["StockSpanner","next","next","next","next","next","next","next"],
                   "arguments": [[],[100],[80],[60],[70],[60],[75],[85]]},
         "expected": [None, 1, 1, 1, 2, 1, 4, 6]},
        {"input": {"operations": ["StockSpanner","next"], "arguments": [[],[5]]},
         "expected": [None, 1]},
        {"input": {"operations": ["StockSpanner","next","next","next"], "arguments": [[],[1],[2],[3]]},
         "expected": [None, 1, 2, 3]},
    ],
    solution="""class Solution:
    def stockSpannerOps(self, operations: list[str], arguments: list[list]) -> list:
        stack = []  # (price, span)
        out = []
        for op, args in zip(operations, arguments):
            if op == 'StockSpanner':
                stack = []
                out.append(None)
            else:
                p = args[0]
                span = 1
                while stack and stack[-1][0] <= p:
                    span += stack.pop()[1]
                stack.append((p, span))
                out.append(span)
        return out
""",
    explanation="""**Approach: Monotonic Stack of (price, span)**

**Time:** O(1) amortized per call | **Space:** O(n)

Each call pops every prior price that's `<= today` and folds their spans into the new entry. Each price is pushed and popped at most once.
"""
)

_register(933,
    description="""<h3>933. Number of Recent Calls</h3>
<p>Design <code>RecentCounter</code>: <code>ping(t)</code> records a new ping at time t and returns the number of pings in the inclusive range [t-3000, t]. Calls are strictly increasing in t.</p>
<h4>Example:</h4>
<pre>Input: ops = ["RecentCounter","ping","ping","ping","ping"]
       args = [[],[1],[100],[3001],[3002]]
Output: [null, 1, 2, 3, 3]</pre>""",
    function_name="recentCounterOps",
    template="""class Solution:
    def recentCounterOps(self, operations: list[str], arguments: list[list]) -> list:
        pass
""",
    test_cases=[
        {"input": {"operations": ["RecentCounter","ping","ping","ping","ping"],
                   "arguments": [[],[1],[100],[3001],[3002]]},
         "expected": [None, 1, 2, 3, 3]},
        {"input": {"operations": ["RecentCounter","ping"], "arguments": [[],[1]]},
         "expected": [None, 1]},
    ],
    solution="""class Solution:
    def recentCounterOps(self, operations: list[str], arguments: list[list]) -> list:
        from collections import deque
        q = deque()
        out = []
        for op, args in zip(operations, arguments):
            if op == 'RecentCounter':
                q = deque()
                out.append(None)
            else:
                t = args[0]
                q.append(t)
                while q and q[0] < t - 3000:
                    q.popleft()
                out.append(len(q))
        return out
""",
    explanation="""**Approach: Sliding Window Queue**

**Time:** O(1) amortized | **Space:** O(window size)

Keep timestamps in a deque; on each ping, evict the front while it's < t - 3000, then the queue length is the answer.
"""
)

_register(1071,
    description="""<h3>1071. Greatest Common Divisor of Strings</h3>
<p>For two strings <code>s</code> and <code>t</code>, define a divisor as a string <code>x</code> such that s and t can each be written as repeated x. Return the longest such divisor; "" if none.</p>
<h4>Example 1:</h4>
<pre>Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"</pre>
<h4>Example 2:</h4>
<pre>Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"</pre>""",
    function_name="gcdOfStrings",
    template="""class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass
""",
    test_cases=[
        {"input": {"str1": "ABCABC", "str2": "ABC"}, "expected": "ABC"},
        {"input": {"str1": "ABABAB", "str2": "ABAB"}, "expected": "AB"},
        {"input": {"str1": "LEET", "str2": "CODE"}, "expected": ""},
        {"input": {"str1": "ABCDEF", "str2": "ABC"}, "expected": ""},
        {"input": {"str1": "AAAAAA", "str2": "AA"}, "expected": "AA"},
    ],
    solution="""class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:gcd(len(str1), len(str2))]
""",
    explanation="""**Approach: Concatenation Test + Length GCD**

**Time:** O(n + m) | **Space:** O(n + m)

If a common divisor exists, both strings are built from the same repeating block, so `s1 + s2 == s2 + s1`. The divisor's length is `gcd(|s1|, |s2|)`.
"""
)

_register(1137,
    description="""<h3>1137. N-th Tribonacci Number</h3>
<p>T(0) = 0, T(1) = 1, T(2) = 1; T(n) = T(n-1) + T(n-2) + T(n-3) for n &ge; 3. Return T(n).</p>
<h4>Example 1:</h4>
<pre>Input: n = 4
Output: 4</pre>""",
    function_name="tribonacci",
    template="""class Solution:
    def tribonacci(self, n: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"n": 0}, "expected": 0},
        {"input": {"n": 1}, "expected": 1},
        {"input": {"n": 2}, "expected": 1},
        {"input": {"n": 4}, "expected": 4},
        {"input": {"n": 25}, "expected": 1389537},
    ],
    solution="""class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n < 3: return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
""",
    explanation="""**Approach: Rolling Recurrence**

**Time:** O(n) | **Space:** O(1)

Maintain a sliding window of the last three values.
"""
)

_register(1161,
    description="""<h3>1161. Maximum Level Sum of a Binary Tree</h3>
<p>Return the smallest level <code>x</code> (1-indexed from the root) such that the sum of all values at level x is maximal.</p>
<h4>Example 1:</h4>
<pre>Input: root = [1,7,0,7,-8,null,null]
Output: 2</pre>""",
    function_name="maxLevelSum",
    template="""class Solution:
    def maxLevelSum(self, root: list) -> int:
        pass
""",
    test_cases=[
        {"input": {"root": [1,7,0,7,-8,None,None]}, "expected": 2},
        {"input": {"root": [989,None,10250,98693,-89388,None,None,None,-32127]}, "expected": 2},
        {"input": {"root": [1]}, "expected": 1},
        {"input": {"root": [1,2,3]}, "expected": 2},
    ],
    solution="""class Solution:
    def maxLevelSum(self, root: list) -> int:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            r = T(next(it))
            q = deque([r])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return r
        r = build(root)
        if not r: return 0
        best_sum = float('-inf'); best_lvl = 0
        q = deque([r]); lvl = 0
        while q:
            lvl += 1
            s = 0
            for _ in range(len(q)):
                n = q.popleft()
                s += n.v
                if n.l: q.append(n.l)
                if n.r: q.append(n.r)
            if s > best_sum:
                best_sum = s; best_lvl = lvl
        return best_lvl
""",
    explanation="""**Approach: BFS, Track Best Level Sum**

**Time:** O(n) | **Space:** O(w)

Compute each level's sum during level-order traversal. Update best on strict `>` so the smallest level wins ties.
"""
)

_register(1207,
    description="""<h3>1207. Unique Number of Occurrences</h3>
<p>Given an array of integers, return <code>true</code> if no two values share the same occurrence count.</p>
<h4>Example 1:</h4>
<pre>Input: arr = [1,2,2,1,1,3]
Output: true</pre>""",
    function_name="uniqueOccurrences",
    template="""class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        pass
""",
    test_cases=[
        {"input": {"arr": [1,2,2,1,1,3]}, "expected": True},
        {"input": {"arr": [1,2]}, "expected": False},
        {"input": {"arr": [-3,0,1,-3,1,1,1,-3,10,0]}, "expected": True},
        {"input": {"arr": [1]}, "expected": True},
    ],
    solution="""class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import Counter
        c = Counter(arr).values()
        return len(set(c)) == len(c)
""",
    explanation="""**Approach: Counter + Set Equality**

**Time:** O(n) | **Space:** O(n)

Count occurrences, compare the count-multiset to a set of counts; equal sizes ⇒ all unique.
"""
)

_register(1268,
    description="""<h3>1268. Search Suggestions System</h3>
<p>Given a list of <code>products</code> and a <code>searchWord</code>, after typing each character of <code>searchWord</code> return up to 3 lexicographically smallest products that share that prefix.</p>
<h4>Example 1:</h4>
<pre>Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]</pre>""",
    function_name="suggestedProducts",
    template="""class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        pass
""",
    test_cases=[
        {"input": {"products": ["mobile","mouse","moneypot","monitor","mousepad"], "searchWord": "mouse"},
         "expected": [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]},
        {"input": {"products": ["havana"], "searchWord": "havana"},
         "expected": [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]},
        {"input": {"products": ["bags","baggage","banner","box","cloths"], "searchWord": "bags"},
         "expected": [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]},
    ],
    solution="""class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        from bisect import bisect_left
        products = sorted(products)
        out = []
        prefix = ''
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)
            picks = []
            for p in products[i:i+3]:
                if p.startswith(prefix): picks.append(p)
                else: break
            out.append(picks)
        return out
""",
    explanation="""**Approach: Sort + Binary Search**

**Time:** O(L*log n + total chars) | **Space:** O(n)

Sort products. For each prefix, binary-search the insertion point and check up to 3 neighbors; stop when one stops sharing the prefix.
"""
)

_register(1318,
    description="""<h3>1318. Minimum Number of Flips to Make a OR b Equal to c</h3>
<p>Given three non-negative integers a, b, c, return the minimum number of bit flips (in a or b) to make <code>(a | b) == c</code>.</p>
<h4>Example 1:</h4>
<pre>Input: a = 2, b = 6, c = 5
Output: 3</pre>""",
    function_name="minFlips",
    template="""class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"a": 2, "b": 6, "c": 5}, "expected": 3},
        {"input": {"a": 4, "b": 2, "c": 7}, "expected": 1},
        {"input": {"a": 1, "b": 2, "c": 3}, "expected": 0},
        {"input": {"a": 0, "b": 0, "c": 0}, "expected": 0},
        {"input": {"a": 7, "b": 7, "c": 0}, "expected": 6},
    ],
    solution="""class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            ab = (a & 1) | (b & 1)
            cb = c & 1
            if ab != cb:
                if cb == 0:
                    # both a-bit and b-bit that are 1 must flip to 0
                    flips += (a & 1) + (b & 1)
                else:
                    # need at least one to be 1; flip one
                    flips += 1
            a >>= 1; b >>= 1; c >>= 1
        return flips
""",
    explanation="""**Approach: Bit-by-Bit Scan**

**Time:** O(log max) | **Space:** O(1)

For each bit position, if `(a|b)` already matches `c`'s bit, 0 flips. If c's bit is 0 and one or both of a/b are 1, flip each 1. If c's bit is 1 and both a/b are 0, flip one of them.
"""
)

_register(1372,
    description="""<h3>1372. Longest ZigZag Path in a Binary Tree</h3>
<p>A zigzag path alternates between left and right child moves. Return the length (number of edges) of the longest zigzag path in the tree.</p>
<h4>Example 1:</h4>
<pre>Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3</pre>""",
    function_name="longestZigZag",
    template="""class Solution:
    def longestZigZag(self, root: list) -> int:
        pass
""",
    test_cases=[
        {"input": {"root": [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]}, "expected": 3},
        {"input": {"root": [1,1,1,None,1,None,None,1,1,None,1]}, "expected": 4},
        {"input": {"root": [1]}, "expected": 0},
        {"input": {"root": []}, "expected": 0},
    ],
    solution="""class Solution:
    def longestZigZag(self, root: list) -> int:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            r = T(next(it))
            q = deque([r])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return r
        r = build(root)
        if not r: return 0
        best = 0
        def dfs(n):
            nonlocal best
            if not n: return (0, 0)  # (going-left-ending-here, going-right-ending-here)
            ll, lr = dfs(n.l)
            rl, rr = dfs(n.r)
            # If we just stepped left into n.l: parent must have come from the right, so the
            # zigzag arriving at n.l from this node continues with .r from n.l, i.e. lr + 1.
            left_path = lr + 1 if n.l else 0
            right_path = rl + 1 if n.r else 0
            best = max(best, left_path, right_path)
            return (left_path, right_path)
        dfs(r)
        return best
""",
    explanation="""**Approach: DFS with Two States Per Node**

**Time:** O(n) | **Space:** O(h)

At each node return two values: the longest zigzag arriving via the left child (so the next step was left), and via the right child. The next step alternates, so the count uses the opposite-direction child's value plus 1.
"""
)

_register(1431,
    description="""<h3>1431. Kids With the Greatest Number of Candies</h3>
<p>Given <code>candies[i]</code> per kid and <code>extraCandies</code>, return a boolean array where each entry is <code>true</code> iff giving that kid the extra candies would make them have the greatest number among all kids.</p>
<h4>Example 1:</h4>
<pre>Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]</pre>""",
    function_name="kidsWithCandies",
    template="""class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        pass
""",
    test_cases=[
        {"input": {"candies": [2,3,5,1,3], "extraCandies": 3}, "expected": [True,True,True,False,True]},
        {"input": {"candies": [4,2,1,1,2], "extraCandies": 1}, "expected": [True,False,False,False,False]},
        {"input": {"candies": [12,1,12], "extraCandies": 10}, "expected": [True,False,True]},
    ],
    solution="""class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        return [c + extraCandies >= m for c in candies]
""",
    explanation="""**Approach: One-Pass with Max**

**Time:** O(n) | **Space:** O(n)

Compute the maximum once; each kid qualifies iff their candies + extra is at least that maximum.
"""
)

_register(1448,
    description="""<h3>1448. Count Good Nodes in Binary Tree</h3>
<p>A node is "good" if no node on the root-to-it path has a greater value. Return the number of good nodes.</p>
<h4>Example 1:</h4>
<pre>Input: root = [3,1,4,3,null,1,5]
Output: 4</pre>""",
    function_name="goodNodes",
    template="""class Solution:
    def goodNodes(self, root: list) -> int:
        pass
""",
    test_cases=[
        {"input": {"root": [3,1,4,3,None,1,5]}, "expected": 4},
        {"input": {"root": [3,3,None,4,2]}, "expected": 3},
        {"input": {"root": [1]}, "expected": 1},
        {"input": {"root": []}, "expected": 0},
    ],
    solution="""class Solution:
    def goodNodes(self, root: list) -> int:
        from collections import deque
        class T:
            def __init__(self,v): self.v=v; self.l=None; self.r=None
        def build(lst):
            if not lst: return None
            it = iter(lst)
            r = T(next(it))
            q = deque([r])
            for v in it:
                node = q[0]
                if v is not None:
                    node.l = T(v); q.append(node.l)
                try: v2 = next(it)
                except StopIteration: break
                if v2 is not None:
                    node.r = T(v2); q.append(node.r)
                q.popleft()
            return r
        r = build(root)
        if not r: return 0
        def dfs(n, mx):
            if not n: return 0
            cur = 1 if n.v >= mx else 0
            nm = max(mx, n.v)
            return cur + dfs(n.l, nm) + dfs(n.r, nm)
        return dfs(r, float('-inf'))
""",
    explanation="""**Approach: DFS with Path Maximum**

**Time:** O(n) | **Space:** O(h)

Carry the maximum seen so far on the current root-to-node path. A node is good iff `n.val >= max_so_far`.
"""
)

_register(1456,
    description="""<h3>1456. Maximum Number of Vowels in a Substring of Given Length</h3>
<p>Return the maximum number of vowel letters in any substring of length <code>k</code>.</p>
<h4>Example 1:</h4>
<pre>Input: s = "abciiidef", k = 3
Output: 3</pre>""",
    function_name="maxVowels",
    template="""class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"s": "abciiidef", "k": 3}, "expected": 3},
        {"input": {"s": "aeiou", "k": 2}, "expected": 2},
        {"input": {"s": "leetcode", "k": 3}, "expected": 2},
        {"input": {"s": "rhythms", "k": 4}, "expected": 0},
        {"input": {"s": "tryhard", "k": 4}, "expected": 1},
    ],
    solution="""class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        V = set('aeiou')
        cur = sum(1 for c in s[:k] if c in V)
        best = cur
        for i in range(k, len(s)):
            cur += (1 if s[i] in V else 0) - (1 if s[i-k] in V else 0)
            if cur > best: best = cur
        return best
""",
    explanation="""**Approach: Sliding Window**

**Time:** O(n) | **Space:** O(1)

Initialize with the first window's vowel count. Roll the window: add the entering char, drop the exiting char.
"""
)

_register(1466,
    description="""<h3>1466. Reorder Routes to Make All Paths Lead to the City Zero</h3>
<p>Cities 0..n-1 connected by n-1 directed roads (forming a tree if undirected). Reorient the minimum number of roads so every city can reach 0.</p>
<h4>Example 1:</h4>
<pre>Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3</pre>""",
    function_name="minReorder",
    template="""class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        pass
""",
    test_cases=[
        {"input": {"n": 6, "connections": [[0,1],[1,3],[2,3],[4,0],[4,5]]}, "expected": 3},
        {"input": {"n": 5, "connections": [[1,0],[1,2],[3,2],[3,4]]}, "expected": 2},
        {"input": {"n": 3, "connections": [[1,0],[2,0]]}, "expected": 0},
    ],
    solution="""class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        from collections import defaultdict, deque
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))  # 1 = directed away from a (needs flip when traversed outward from 0)
            adj[b].append((a, 0))
        seen = {0}
        dq = deque([0])
        flips = 0
        while dq:
            u = dq.popleft()
            for v, cost in adj[u]:
                if v in seen: continue
                seen.add(v)
                flips += cost
                dq.append(v)
        return flips
""",
    explanation="""**Approach: BFS on Undirected Tree, Count Outward-Pointing Edges**

**Time:** O(n) | **Space:** O(n)

Treat the graph as undirected for traversal. For each original directed edge `a -> b`, the version we record as `adj[a] -> b` carries cost 1 (it points away from 0 when we walk outward); the reverse adjacency carries cost 0. BFS from 0; each step's cost says whether we'd have had to flip the original edge.
"""
)

_register(1493,
    description="""<h3>1493. Longest Subarray of 1's After Deleting One Element</h3>
<p>Given a binary array, you must delete exactly one element. Return the size of the longest non-empty subarray containing only 1's in the resulting array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,1,0,1]
Output: 3</pre>""",
    function_name="longestSubarray",
    template="""class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        pass
""",
    test_cases=[
        {"input": {"nums": [1,1,0,1]}, "expected": 3},
        {"input": {"nums": [0,1,1,1,0,1,1,0,1]}, "expected": 5},
        {"input": {"nums": [1,1,1]}, "expected": 2},
        {"input": {"nums": [0,0,0]}, "expected": 0},
        {"input": {"nums": [1]}, "expected": 0},
    ],
    solution="""class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Sliding window allowing at most one zero; answer = window size - 1 (the one deletion).
        zeros = 0
        l = 0
        best = 0
        for r, x in enumerate(nums):
            if x == 0: zeros += 1
            while zeros > 1:
                if nums[l] == 0: zeros -= 1
                l += 1
            best = max(best, r - l)  # subtract 1 for the deletion (window length - 1)
        return best
""",
    explanation="""**Approach: Sliding Window with at Most One Zero**

**Time:** O(n) | **Space:** O(1)

Maintain the longest window with `<= 1` zero. Since we must delete one element, the answer is `(window length) - 1`. `r - l` already represents that.
"""
)

_register(1657,
    description="""<h3>1657. Determine if Two Strings Are Close</h3>
<p>Two strings are close if you can transform one to the other using these operations any number of times: (1) swap any two existing characters, (2) swap two existing-letters' frequencies. Return whether <code>word1</code> can be made into <code>word2</code>.</p>
<h4>Example 1:</h4>
<pre>Input: word1 = "abc", word2 = "bca"
Output: true</pre>""",
    function_name="closeStrings",
    template="""class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        pass
""",
    test_cases=[
        {"input": {"word1": "abc", "word2": "bca"}, "expected": True},
        {"input": {"word1": "a", "word2": "aa"}, "expected": False},
        {"input": {"word1": "cabbba", "word2": "abbccc"}, "expected": True},
        {"input": {"word1": "cabbba", "word2": "aabbss"}, "expected": False},
        {"input": {"word1": "uau", "word2": "ssx"}, "expected": False},
    ],
    solution="""class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
""",
    explanation="""**Approach: Same Letters + Same Frequency Multiset**

**Time:** O(n + m) | **Space:** O(1) (alphabet bound)

Operation (1) permutes positions (any anagram is reachable). Operation (2) permutes frequency assignments. So two strings are close iff they share the same letter set and the same multiset of frequencies.
"""
)

_register(1679,
    description="""<h3>1679. Max Number of K-Sum Pairs</h3>
<p>You may repeatedly pick two numbers whose sum equals <code>k</code> and remove them. Return the maximum number of operations.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,3,4], k = 5
Output: 2</pre>""",
    function_name="maxOperations",
    template="""class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"nums": [1,2,3,4], "k": 5}, "expected": 2},
        {"input": {"nums": [3,1,3,4,3], "k": 6}, "expected": 1},
        {"input": {"nums": [1,1,1,1], "k": 2}, "expected": 2},
        {"input": {"nums": [2,2,2,3,1,1,4,1], "k": 4}, "expected": 2},
    ],
    solution="""class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        from collections import Counter
        c = Counter(nums)
        ops = 0
        for x in list(c):
            if c[x] <= 0: continue
            y = k - x
            if y == x:
                ops += c[x] // 2
                c[x] = 0
            elif y in c:
                pair = min(c[x], c[y])
                ops += pair
                c[x] -= pair; c[y] -= pair
        return ops
""",
    explanation="""**Approach: Frequency Counter**

**Time:** O(n) | **Space:** O(n)

For each value x, match with k-x. Take the min of their counts (or //2 when x*2 == k). Zero out used counts to avoid double counting.
"""
)

_register(1732,
    description="""<h3>1732. Find the Highest Altitude</h3>
<p>The biker starts at altitude 0. <code>gain[i]</code> is the net change from point i to i+1. Return the maximum altitude reached.</p>
<h4>Example 1:</h4>
<pre>Input: gain = [-5,1,5,0,-7]
Output: 1</pre>""",
    function_name="largestAltitude",
    template="""class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        pass
""",
    test_cases=[
        {"input": {"gain": [-5,1,5,0,-7]}, "expected": 1},
        {"input": {"gain": [-4,-3,-2,-1,4,3,2]}, "expected": 0},
        {"input": {"gain": [1,2,3]}, "expected": 6},
        {"input": {"gain": [-1,-2,-3]}, "expected": 0},
    ],
    solution="""class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        cur = best = 0
        for g in gain:
            cur += g
            if cur > best: best = cur
        return best
""",
    explanation="""**Approach: Running Max of Prefix Sum**

**Time:** O(n) | **Space:** O(1)

Maintain cumulative altitude and the running max. Start altitude is 0, so the answer is at least 0.
"""
)

_register(1926,
    description="""<h3>1926. Nearest Exit from Entrance in Maze</h3>
<p>Given a maze of <code>'.'</code> (open) and <code>'+'</code> (wall) and an entrance, return the number of steps to reach the nearest exit (any border cell that isn't the entrance). Return -1 if no exit is reachable.</p>
<h4>Example 1:</h4>
<pre>Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1</pre>""",
    function_name="nearestExit",
    template="""class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        pass
""",
    test_cases=[
        {"input": {"maze": [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], "entrance": [1,2]},
         "expected": 1},
        {"input": {"maze": [["+","+","+"],[".",".","."],["+","+","+"]], "entrance": [1,0]},
         "expected": 2},
        {"input": {"maze": [[".","+"]], "entrance": [0,0]}, "expected": -1},
        {"input": {"maze": [[".","."],[".","."]], "entrance": [0,0]}, "expected": 1},
    ],
    solution="""class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        from collections import deque
        R, C = len(maze), len(maze[0])
        er, ec = entrance
        seen = [[False]*C for _ in range(R)]
        seen[er][ec] = True
        q = deque([(er, ec, 0)])
        while q:
            r, c, d = q.popleft()
            if (r != er or c != ec) and (r == 0 or r == R-1 or c == 0 or c == C-1):
                return d
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc] and maze[nr][nc] == '.':
                    seen[nr][nc] = True
                    q.append((nr, nc, d+1))
        return -1
""",
    explanation="""**Approach: BFS from Entrance**

**Time:** O(R * C) | **Space:** O(R * C)

BFS guarantees the first border cell reached (that isn't the entrance itself) is the nearest exit by step count.
"""
)

_register(2095,
    description="""<h3>2095. Delete the Middle Node of a Linked List</h3>
<p>Given the head of a linked list, delete the middle node (index <code>floor(n/2)</code>) and return the resulting head.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]</pre>""",
    function_name="deleteMiddle",
    template="""# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: 'ListNode') -> 'ListNode':
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,3,4,7,1,2,6]}, "expected": [1,3,4,1,2,6]},
        {"input": {"head": [1,2,3,4]}, "expected": [1,2,4]},
        {"input": {"head": [2,1]}, "expected": [2]},
        {"input": {"head": [1]}, "expected": []},
        {"input": {"head": []}, "expected": []},
    ],
    solution="""class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        # at end of loop, slow points to the node BEFORE the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
""",
    explanation="""**Approach: Slow/Fast Pointers**

**Time:** O(n) | **Space:** O(1)

Advance `fast` by 2 and `slow` by 1, starting `fast` two ahead so `slow` lands on the node just before the middle. Splice out `slow.next`.
""",
    harness={"input": {"head": "linked_list"}, "output": "linked_list"}
)

_register(2130,
    description="""<h3>2130. Maximum Twin Sum of a Linked List</h3>
<p>Each node at index i has a twin at index n-1-i. Return the maximum twin sum.</p>
<h4>Example 1:</h4>
<pre>Input: head = [5,4,2,1]
Output: 6</pre>""",
    function_name="pairSum",
    template="""# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: 'ListNode') -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [5,4,2,1]}, "expected": 6},
        {"input": {"head": [4,2,2,3]}, "expected": 7},
        {"input": {"head": [1,100000]}, "expected": 100001},
        {"input": {"head": [1,2,3,4,5,6]}, "expected": 7},
    ],
    solution="""class Solution:
    def pairSum(self, head):
        # Find middle with slow/fast, reversing the first half as we go.
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # `prev` now heads the reversed first half; `slow` heads the second half.
        best = 0
        a, b = prev, slow
        while a and b:
            s = a.val + b.val
            if s > best: best = s
            a = a.next
            b = b.next
        return best
""",
    explanation="""**Approach: Reverse First Half + Walk Both Halves**

**Time:** O(n) | **Space:** O(1)

While finding the middle with slow/fast, reverse the first half in place. Then walk the reversed-first-half and the second half together, summing twins.
""",
    harness={"input": {"head": "linked_list"}}
)

_register(2215,
    description="""<h3>2215. Find the Difference of Two Arrays</h3>
<p>Given two integer arrays, return a list <code>[d1, d2]</code> where <code>d1</code> contains distinct integers in <code>nums1</code> not present in <code>nums2</code>, and vice versa.</p>
<h4>Example 1:</h4>
<pre>Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]</pre>""",
    function_name="findDifference",
    template="""class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        pass
""",
    test_cases=[
        {"input": {"nums1": [1,2,3], "nums2": [2,4,6]}, "expected": [[1,3],[4,6]]},
        {"input": {"nums1": [1,2,3,3], "nums2": [1,1,2,2]}, "expected": [[3],[]]},
        {"input": {"nums1": [1,1,1], "nums2": [1,1,1]}, "expected": [[],[]]},
        {"input": {"nums1": [], "nums2": [1]}, "expected": [[],[1]]},
    ],
    solution="""class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a, b = set(nums1), set(nums2)
        return [list(a - b), list(b - a)]
""",
    explanation="""**Approach: Set Difference**

**Time:** O(n + m) | **Space:** O(n + m)

Convert to sets and take both one-sided differences.
"""
)

_register(2300,
    description="""<h3>2300. Successful Pairs of Spells and Potions</h3>
<p>For each spell s, count how many potions p satisfy <code>s * p &ge; success</code>. Return the counts.</p>
<h4>Example 1:</h4>
<pre>Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]</pre>""",
    function_name="successfulPairs",
    template="""class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pass
""",
    test_cases=[
        {"input": {"spells": [5,1,3], "potions": [1,2,3,4,5], "success": 7}, "expected": [4,0,3]},
        {"input": {"spells": [3,1,2], "potions": [8,5,8], "success": 16}, "expected": [2,0,2]},
        {"input": {"spells": [1], "potions": [1], "success": 1}, "expected": [1]},
    ],
    solution="""class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        from bisect import bisect_left
        potions.sort()
        m = len(potions)
        out = []
        for s in spells:
            # smallest p such that s * p >= success, i.e. p >= ceil(success / s)
            threshold = (success + s - 1) // s
            idx = bisect_left(potions, threshold)
            out.append(m - idx)
        return out
""",
    explanation="""**Approach: Sort Potions + Binary Search Threshold**

**Time:** O((n + m) log m) | **Space:** O(1)

Sort potions; for each spell, binary-search the smallest potion that meets the success threshold; the count is `m - idx`.
"""
)

_register(2336,
    description="""<h3>2336. Smallest Number in Infinite Set</h3>
<p>Design a set initially containing all positive integers <code>{1, 2, 3, ...}</code>. Implement <code>popSmallest()</code> and <code>addBack(num)</code>.</p>
<p><em>Wrapped as a function: pass <code>operations</code> and parallel <code>arguments</code>. Constructor returns <code>None</code>; <code>addBack</code> returns <code>None</code>.</em></p>
<h4>Example:</h4>
<pre>Input: ops = ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
       args = [[],[2],[],[],[],[1],[],[],[]]
Output: [null, null, 1, 2, 3, null, 1, 4, 5]</pre>""",
    function_name="smallestInfiniteSetOps",
    template="""class Solution:
    def smallestInfiniteSetOps(self, operations: list[str], arguments: list[list]) -> list:
        pass
""",
    test_cases=[
        {"input": {"operations": ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"],
                   "arguments": [[],[2],[],[],[],[1],[],[],[]]},
         "expected": [None, None, 1, 2, 3, None, 1, 4, 5]},
        {"input": {"operations": ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest"],
                   "arguments": [[],[],[],[1],[]]},
         "expected": [None, 1, 2, None, 1]},
    ],
    solution="""class Solution:
    def smallestInfiniteSetOps(self, operations: list[str], arguments: list[list]) -> list:
        import heapq
        # next_unused = smallest integer not yet popped from the "fresh" frontier
        # readded = min-heap of values added back below next_unused
        # in_readded set to avoid duplicate adds
        next_unused = 1
        readded = []
        in_readded = set()
        out = []
        for op, args in zip(operations, arguments):
            if op == 'SmallestInfiniteSet':
                next_unused = 1
                readded = []
                in_readded = set()
                out.append(None)
            elif op == 'popSmallest':
                if readded:
                    v = heapq.heappop(readded)
                    in_readded.discard(v)
                    out.append(v)
                else:
                    out.append(next_unused)
                    next_unused += 1
            elif op == 'addBack':
                num = args[0]
                if num < next_unused and num not in in_readded:
                    heapq.heappush(readded, num)
                    in_readded.add(num)
                out.append(None)
        return out
""",
    explanation="""**Approach: Frontier + Min-Heap for Re-Added Values**

**Time:** O(log n) per op | **Space:** O(n)

`next_unused` represents the smallest value of the infinite tail. A min-heap holds any values that were popped and added back. On pop, prefer the heap (smallest re-added), else take and advance the frontier.
"""
)

_register(2352,
    description="""<h3>2352. Equal Row and Column Pairs</h3>
<p>Given a 0-indexed n × n integer matrix <code>grid</code>, return the number of pairs <code>(R_i, C_j)</code> where row i equals column j as integer arrays.</p>
<h4>Example 1:</h4>
<pre>Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1</pre>""",
    function_name="equalPairs",
    template="""class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        pass
""",
    test_cases=[
        {"input": {"grid": [[3,2,1],[1,7,6],[2,7,7]]}, "expected": 1},
        {"input": {"grid": [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]}, "expected": 3},
        {"input": {"grid": [[1]]}, "expected": 1},
        {"input": {"grid": [[1,2],[3,4]]}, "expected": 0},
    ],
    solution="""class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        from collections import Counter
        n = len(grid)
        rows = Counter(tuple(r) for r in grid)
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += rows.get(col, 0)
        return count
""",
    explanation="""**Approach: Hash Rows, Match Each Column**

**Time:** O(n^2) | **Space:** O(n^2)

Tuple-hash each row, then for each column tuple, add the matching row count.
"""
)

_register(2390,
    description="""<h3>2390. Removing Stars From a String</h3>
<p>Each '*' removes the closest non-star character to its left. Return the string after all '*' operations are applied.</p>
<h4>Example 1:</h4>
<pre>Input: s = "leet**cod*e"
Output: "lecoe"</pre>""",
    function_name="removeStars",
    template="""class Solution:
    def removeStars(self, s: str) -> str:
        pass
""",
    test_cases=[
        {"input": {"s": "leet**cod*e"}, "expected": "lecoe"},
        {"input": {"s": "erase*****"}, "expected": ""},
        {"input": {"s": "abc"}, "expected": "abc"},
        {"input": {"s": ""}, "expected": ""},
        {"input": {"s": "a*b*c"}, "expected": "c"},
    ],
    solution="""class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == '*':
                if st: st.pop()
            else:
                st.append(c)
        return ''.join(st)
""",
    explanation="""**Approach: Stack**

**Time:** O(n) | **Space:** O(n)

Push letters; a `*` pops the most recent letter. The stack ends as the final string.
"""
)

_register(2462,
    description="""<h3>2462. Total Cost to Hire K Workers</h3>
<p>From <code>costs</code>, hire <code>k</code> workers. In each session you can pick from the first <code>candidates</code> or the last <code>candidates</code> remaining workers; choose the cheapest (ties: smallest index). Return total cost.</p>
<h4>Example 1:</h4>
<pre>Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11</pre>""",
    function_name="totalCost",
    template="""class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"costs": [17,12,10,2,7,2,11,20,8], "k": 3, "candidates": 4}, "expected": 11},
        {"input": {"costs": [1,2,4,1], "k": 3, "candidates": 3}, "expected": 4},
        {"input": {"costs": [1], "k": 1, "candidates": 1}, "expected": 1},
        {"input": {"costs": [3,2,1], "k": 1, "candidates": 1}, "expected": 1},
    ],
    solution="""class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        import heapq
        n = len(costs)
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])
        left = [(costs[i], i) for i in range(candidates)]
        right = [(costs[i], i) for i in range(n - candidates, n)]
        heapq.heapify(left); heapq.heapify(right)
        l = candidates
        r = n - candidates - 1
        total = 0
        for _ in range(k):
            if left[0] <= right[0]:
                c, _i = heapq.heappop(left)
                total += c
                if l <= r:
                    heapq.heappush(left, (costs[l], l)); l += 1
            else:
                c, _i = heapq.heappop(right)
                total += c
                if l <= r:
                    heapq.heappush(right, (costs[r], r)); r -= 1
        return total
""",
    explanation="""**Approach: Two Min-Heaps**

**Time:** O((k + candidates) log candidates) | **Space:** O(candidates)

Keep a heap for each side. Each round, pop the cheaper side (ties favor left because comparison uses original index in the tuple). Replenish from the shrinking middle of the array until pointers cross.
"""
)

_register(2542,
    description="""<h3>2542. Maximum Subsequence Score</h3>
<p>Pick any subsequence of size <code>k</code> over indices. Score = (sum of <code>nums1</code> values) * (min of corresponding <code>nums2</code> values). Return the maximum score.</p>
<h4>Example 1:</h4>
<pre>Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12</pre>""",
    function_name="maxScore",
    template="""class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pass
""",
    test_cases=[
        {"input": {"nums1": [1,3,3,2], "nums2": [2,1,3,4], "k": 3}, "expected": 12},
        {"input": {"nums1": [4,2,3,1,1], "nums2": [7,5,10,9,6], "k": 1}, "expected": 30},
        {"input": {"nums1": [1,2,3], "nums2": [3,2,1], "k": 1}, "expected": 4},
    ],
    solution="""class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        import heapq
        pairs = sorted(zip(nums1, nums2), key=lambda p: -p[1])
        heap = []
        s = 0
        best = 0
        for a, b in pairs:
            heapq.heappush(heap, a)
            s += a
            if len(heap) > k:
                s -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, s * b)
        return best
""",
    explanation="""**Approach: Sort by nums2 Descending + Min-Heap for nums1**

**Time:** O(n log n) | **Space:** O(n)

Sort pairs by descending nums2. As we sweep, the current pair's nums2 is the running minimum of any subset taken so far. Maintain a size-k min-heap of nums1 values (largest sums) and compute `sum * current_min` whenever the heap is full; track the max.
"""
)

_register(206,
    description="""<h3>206. Reverse Linked List</h3>
<p>Given the <code>head</code> of a singly linked list, reverse the list and return the reversed list.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]</pre>
<h4>Example 2:</h4>
<pre>Input: head = [1,2]
Output: [2,1]</pre>
<h4>Example 3:</h4>
<pre>Input: head = []
Output: []</pre>""",
    function_name="reverseList",
    template="""# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,2,3,4,5]}, "expected": [5,4,3,2,1]},
        {"input": {"head": [1,2]}, "expected": [2,1]},
        {"input": {"head": []}, "expected": []},
        {"input": {"head": [1]}, "expected": [1]},
        {"input": {"head": [1,2,3]}, "expected": [3,2,1]},
    ],
    solution="""class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
""",
    explanation="""**Approach: Iterative Pointer Reversal**

**Time:** O(n) | **Space:** O(1)

Walk the list with three pointers: `prev`, `curr`, `nxt`. At each step save `curr.next` into `nxt`, flip `curr.next` to point at `prev`, then advance `prev` and `curr`. When `curr` is `None`, `prev` is the new head.

**Recursive alternative:** `reverseList(head.next)` returns the new tail; set `head.next.next = head`, `head.next = None`, return the rec result. Same time, O(n) stack space.
""",
    harness={"input": {"head": "linked_list"}, "output": "linked_list"}
)

_register(92,
    description="""<h3>92. Reverse Linked List II</h3>
<p>Given the <code>head</code> of a singly linked list and two integers <code>left</code> and <code>right</code> where <code>left &le; right</code>, reverse the nodes of the list from position <code>left</code> to position <code>right</code>, and return the reversed list. Positions are 1-indexed.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]</pre>
<h4>Example 2:</h4>
<pre>Input: head = [5], left = 1, right = 1
Output: [5]</pre>""",
    function_name="reverseBetween",
    template="""# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: 'ListNode', left: int, right: int) -> 'ListNode':
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,2,3,4,5], "left": 2, "right": 4}, "expected": [1,4,3,2,5]},
        {"input": {"head": [5], "left": 1, "right": 1}, "expected": [5]},
        {"input": {"head": [1,2,3,4,5], "left": 1, "right": 5}, "expected": [5,4,3,2,1]},
        {"input": {"head": [1,2,3,4,5], "left": 1, "right": 1}, "expected": [1,2,3,4,5]},
        {"input": {"head": [3,5], "left": 1, "right": 2}, "expected": [5,3]},
        {"input": {"head": [1,2,3], "left": 2, "right": 3}, "expected": [1,3,2]},
    ],
    solution="""class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        # Walk to the node just before `left`.
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        # `curr` is the first node to reverse. Splice each subsequent node
        # to the front of the reversed sub-list.
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
""",
    explanation="""**Approach: Iterative Head-Insertion Within the Sub-Range**

**Time:** O(n) | **Space:** O(1)

Use a dummy so the `left == 1` case is uniform. Walk `prev` to the node just before position `left`. Then for each of the `right - left` steps, take `curr.next` and splice it to the front of the reversed segment (right after `prev`). `curr` itself drifts to the tail of the reversed segment, so each iteration reverses one more edge without touching anything outside the range.
""",
    harness={"input": {"head": "linked_list"}, "output": "linked_list"}
)

_register(541,
    description="""<h3>541. Reverse String II</h3>
<p>Given a string <code>s</code> and an integer <code>k</code>, reverse the first <code>k</code> characters for every <code>2k</code> characters counting from the start of the string.</p>
<ul>
<li>If there are fewer than <code>k</code> characters left, reverse all of them.</li>
<li>If there are at least <code>k</code> but fewer than <code>2k</code> left, reverse the first <code>k</code> and leave the rest as is.</li>
</ul>
<h4>Example 1:</h4>
<pre>Input: s = "abcdefg", k = 2
Output: "bacdfeg"</pre>
<h4>Example 2:</h4>
<pre>Input: s = "abcd", k = 2
Output: "bacd"</pre>""",
    function_name="reverseStr",
    template="""class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "abcdefg", "k": 2}, "expected": "bacdfeg"},
        {"input": {"s": "abcd", "k": 2}, "expected": "bacd"},
        {"input": {"s": "a", "k": 2}, "expected": "a"},
        {"input": {"s": "abcdefg", "k": 8}, "expected": "gfedcba"},
        {"input": {"s": "abcdefgh", "k": 3}, "expected": "cbadefhg"},
        {"input": {"s": "abcdefghij", "k": 3}, "expected": "cbadefihgj"},
    ],
    solution="""class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i:i + k] = chars[i:i + k][::-1]
        return ''.join(chars)
""",
    explanation="""**Approach: Stride by 2k, Reverse the First k**

**Time:** O(n) | **Space:** O(n)

Step the start index in increments of `2k`. For each window, slice-assign the first `k` characters with their reverse. Python's slice handles the "fewer than k left" cases automatically.
"""
)

_register(692,
    description="""<h3>692. Top K Frequent Words</h3>
<p>Given an array of strings <code>words</code> and an integer <code>k</code>, return the <code>k</code> most frequent strings.</p>
<p>Return the answer sorted by <strong>frequency</strong> from highest to lowest. Sort words with the same frequency by their <strong>lexicographical order</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words. "i" comes before "love" due to a lower alphabetical order.</pre>
<h4>Example 2:</h4>
<pre>Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; words.length &le; 500</li>
<li>1 &le; words[i].length &le; 10</li>
<li>words[i] consists of lowercase English letters.</li>
<li>k is in the range [1, number of unique words].</li>
</ul>""",
    function_name="topKFrequent",
    template="""class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"words": ["i","love","leetcode","i","love","coding"], "k": 2}, "expected": ["i","love"]},
        {"input": {"words": ["the","day","is","sunny","the","the","the","sunny","is","is"], "k": 4}, "expected": ["the","is","sunny","day"]},
        {"input": {"words": ["a","b","c"], "k": 3}, "expected": ["a","b","c"]},
        {"input": {"words": ["aaa","aa","a"], "k": 1}, "expected": ["a"]},
        {"input": {"words": ["car","car","bike","bike","plane"], "k": 2}, "expected": ["bike","car"]},
    ],
    solution="""class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        import heapq
        from collections import Counter
        count = Counter(words)
        # Min-heap of size k keyed by (-freq, word) so that, when we pop the
        # "smallest", we drop the least frequent / lexicographically-largest first.
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
""",
    explanation="""**Approach: Counter + Heap with Composite Key**

**Time:** O(n + m log m) | **Space:** O(m), where m = number of distinct words

1. Count word frequencies.
2. Build a heap of `(-freq, word)` tuples. Negating frequency turns Python's min-heap into a max-by-frequency heap, while `word` breaks ties in ascending lexicographic order — exactly the required sort.
3. Pop `k` times.

**Why the tie-break works:** Python compares tuples element-wise. For equal `-freq`, the smaller `word` string sorts first, so it pops earlier — matching the "same frequency → lexicographical order" rule.

**Alternative:** `sorted(count, key=lambda w: (-count[w], w))[:k]` is O(m log m) and arguably clearer; the size-k heap variant can be tightened to O(n + m log k) by capping the heap.
"""
)

_register(721,
    description="""<h3>721. Accounts Merge</h3>
<p>Given a list <code>accounts</code> where each element is a list of strings: the first element is the account holder's <strong>name</strong>, and the rest are <strong>emails</strong> representing emails of the account.</p>
<p>Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people, as people may have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.</p>
<p>After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest are emails <strong>in sorted order</strong>. The accounts themselves can be returned in <strong>any order</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: accounts =
[["John","johnsmith@mail.com","john_newyork@mail.com"],
 ["John","johnsmith@mail.com","john00@mail.com"],
 ["Mary","mary@mail.com"],
 ["John","johnnybravo@mail.com"]]
Output:
[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
 ["Mary","mary@mail.com"],
 ["John","johnnybravo@mail.com"]]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; accounts.length &le; 1000</li>
<li>2 &le; accounts[i].length &le; 10</li>
<li>1 &le; accounts[i][j].length &le; 30</li>
<li>accounts[i][0] consists of English letters.</li>
<li>accounts[i][j] (for j &gt; 0) is a valid email.</li>
</ul>""",
    function_name="accountsMerge",
    template="""class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"accounts": [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]},
         "expected": [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]},
        {"input": {"accounts": [
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]},
         "expected": [
            ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
            ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
            ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]},
        {"input": {"accounts": [["Alex","a@m.co"]]},
         "expected": [["Alex","a@m.co"]]},
        {"input": {"accounts": [
            ["A","a@m.co","b@m.co"],
            ["A","b@m.co","c@m.co"],
            ["A","c@m.co","d@m.co"]]},
         "expected": [["A","a@m.co","b@m.co","c@m.co","d@m.co"]]},
    ],
    solution="""class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Union-Find over account indices, unioned by shared email.
        parent = list(range(len(accounts)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        email_to_acct = {}
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in email_to_acct:
                    union(i, email_to_acct[email])
                else:
                    email_to_acct[email] = i

        from collections import defaultdict
        groups = defaultdict(set)
        for email, i in email_to_acct.items():
            groups[find(i)].add(email)

        result = []
        for root, emails in groups.items():
            result.append([accounts[root][0]] + sorted(emails))
        return result
""",
    explanation="""**Approach: Union-Find by Shared Email**

**Time:** O(N * K * α(N) + N * K * log(N * K)) where N = number of accounts and K = avg emails per account
**Space:** O(N * K)

1. Treat each input account as a node in a union-find structure.
2. Walk every email. The first time we see an email, record `email -> account_index`. On subsequent sightings, union the current account with the one we previously recorded — they must belong to the same person.
3. After processing all emails, group each email by the root account it belongs to.
4. Each root produces one merged account: the name (from any member of the group — `accounts[root][0]`) followed by sorted emails.

**Why union-find:** Shared-email relationships form an undirected graph between accounts; UF computes the connected components in near-linear time and is much simpler to implement than a DFS/BFS over an explicit graph here.

**Output ordering:** Emails within each account must be sorted. The order of accounts themselves can be anything — the test framework does an order-independent compare on the outer list.
"""
)

_register(252,
    description="""<h3>252. Meeting Rooms</h3>
<p>Given an array of meeting time <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, determine if a person could attend all meetings.</p>
<p>A meeting <code>[s, e)</code> is treated as a half-open interval: meetings that touch at endpoints (e.g. <code>[5, 10]</code> and <code>[10, 20]</code>) do <strong>not</strong> conflict.</p>
<h4>Example 1:</h4>
<pre>Input: intervals = [[0,30],[5,10],[15,20]]
Output: false</pre>
<h4>Example 2:</h4>
<pre>Input: intervals = [[7,10],[2,4]]
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li>0 &le; intervals.length &le; 10<sup>4</sup></li>
<li>intervals[i].length == 2</li>
<li>0 &le; start_i &lt; end_i &le; 10<sup>6</sup></li>
</ul>""",
    function_name="canAttendMeetings",
    template="""class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"intervals": [[0,30],[5,10],[15,20]]}, "expected": False},
        {"input": {"intervals": [[7,10],[2,4]]}, "expected": True},
        {"input": {"intervals": []}, "expected": True},
        {"input": {"intervals": [[1,5]]}, "expected": True},
        {"input": {"intervals": [[5,10],[10,20]]}, "expected": True},
        {"input": {"intervals": [[1,5],[5,8],[8,10]]}, "expected": True},
        {"input": {"intervals": [[1,5],[4,8]]}, "expected": False},
    ],
    solution="""class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
""",
    explanation="""**Approach: Sort by Start Time + Single Sweep**

**Time:** O(n log n) | **Space:** O(1) extra (ignoring sort buffer)

1. Sort meetings by start time.
2. Walk consecutive pairs: if any meeting begins strictly before the previous one ends (`start_i < end_{i-1}`), there's a conflict.

**Why strict <:** Meetings touch at endpoints (`[5,10]` and `[10,20]`) are treated as back-to-back, not overlapping — LeetCode's convention for this problem.

**Follow-up (#253 Meeting Rooms II):** Instead of yes/no, find the minimum number of rooms needed. A min-heap of end-times handles that in O(n log n).
"""
)

_register(2402,
    description="""<h3>2402. Meeting Rooms III</h3>
<p>You are given an integer <code>n</code>. There are <code>n</code> rooms numbered from <code>0</code> to <code>n - 1</code>.</p>
<p>You are given a 2D array <code>meetings</code> where <code>meetings[i] = [start_i, end_i]</code> means that a meeting will be held during the half-closed time interval <code>[start_i, end_i)</code>. All <code>start_i</code> values are <strong>unique</strong>.</p>
<p>Meetings are allocated to rooms in the following manner:</p>
<ol>
<li>Each meeting will take place in the <strong>unused</strong> room with the <strong>lowest</strong> number.</li>
<li>If there are no available rooms, the meeting will be <strong>delayed</strong> until a room becomes free. The delayed meeting should have the <strong>same duration</strong> as the original meeting.</li>
<li>When a room becomes unused, meetings that have an earlier original start time should be given the room.</li>
</ol>
<p>Return the <em>number of the room that held the most meetings</em>. If there are multiple such rooms, return the <strong>lowest</strong> number.</p>
<h4>Example 1:</h4>
<pre>Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- 0:  room 0 hosts [0,10).
- 1:  room 1 hosts [1,5).
- 2:  no rooms free, delay until room 1 frees at t=5; room 1 then hosts [5,10) (duration 5).
- 3:  no rooms free, delay until room 0 frees at t=10; room 0 then hosts [10,11) (duration 1).
Room 0 and 1 each held 2 meetings, so the lowest-numbered (0) wins.</pre>
<h4>Example 2:</h4>
<pre>Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; n &le; 100</li>
<li>1 &le; meetings.length &le; 10<sup>5</sup></li>
<li>meetings[i].length == 2</li>
<li>0 &le; start_i &lt; end_i &le; 5 * 10<sup>5</sup></li>
<li>All start_i are unique.</li>
</ul>""",
    function_name="mostBooked",
    template="""class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 2, "meetings": [[0,10],[1,5],[2,7],[3,4]]}, "expected": 0},
        {"input": {"n": 3, "meetings": [[1,20],[2,10],[3,5],[4,9],[6,8]]}, "expected": 1},
        {"input": {"n": 1, "meetings": [[0,5],[10,20],[30,40]]}, "expected": 0},
        {"input": {"n": 4, "meetings": [[18,19],[3,12],[17,19],[2,13],[7,10]]}, "expected": 0},
        {"input": {"n": 2, "meetings": [[0,10]]}, "expected": 0},
    ],
    solution="""class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        import heapq
        # free: min-heap of available room numbers.
        # busy: min-heap of (end_time, room_number) for rooms currently in use.
        free = list(range(n))
        heapq.heapify(free)
        busy = []
        count = [0] * n

        for start, end in sorted(meetings):
            # Release every room that's done by `start`.
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            duration = end - start
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                # No free room — delay this meeting until the earliest-ending one frees.
                # Among ties on end_time the tuple sort picks the lowest room number.
                free_at, room = heapq.heappop(busy)
                heapq.heappush(busy, (free_at + duration, room))
            count[room] += 1

        # Tie-break: lowest-numbered room with the max count.
        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        return best
""",
    explanation="""**Approach: Two Min-Heaps (Free Rooms + Busy Rooms)**

**Time:** O((m + n) log (m + n)) where m = number of meetings | **Space:** O(m + n)

1. Sort meetings by start time. (Starts are unique per the problem.)
2. Maintain two heaps:
   - `free`: available room numbers, popped lowest first.
   - `busy`: `(end_time, room_number)` for rooms in use; popping releases the earliest-ending room, breaking ties on the lowest room number.
3. Before placing each meeting, drain every `busy` entry whose `end_time &le; start` back into `free`.
4. If `free` is non-empty, pick the lowest-numbered free room. Otherwise, "delay" by reusing the earliest-ending busy room: push it back with `end_time = free_at + duration`.
5. Increment that room's meeting count.
6. Return the lowest-numbered room with the maximum count.

**Why the tie-break is automatic:** Python's heap orders tuples lexicographically, so `(end_time, room_number)` naturally produces "earliest end, then lowest number" — exactly matching rule (3) in the problem.

**Edge case:** When a room becomes free at exactly the start of the next meeting (`end == start`), we release it into `free` so the lowest-numbered preference still applies.
"""
)

_register(2101,
    description="""<h3>2101. Detonate the Maximum Bombs</h3>
<p>You are given a list of bombs. Each bomb is given by <code>bombs[i] = [x_i, y_i, r_i]</code> where <code>(x_i, y_i)</code> is its location on a 2D plane and <code>r_i</code> is its blast radius.</p>
<p>You must choose <strong>one</strong> bomb to detonate. When detonated, it will trigger all bombs that lie in its range (i.e., whose center lies <em>within or on</em> the boundary of the circle centered at the detonated bomb with its blast radius). Those bombs then detonate, triggering bombs in <em>their</em> range, and so on (chain reaction).</p>
<p>Return the <em>maximum number of bombs</em> that can be detonated if you choose the starting bomb optimally.</p>
<p><strong>Important:</strong> Triggering is <em>directional</em>. Bomb A can reach bomb B if B's center is within A's radius, but the reverse isn't automatic — B may not reach A if A's center is outside B's smaller radius.</p>
<h4>Example 1:</h4>
<pre>Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation: Detonating either bomb will trigger the other since they are within each other's range.</pre>
<h4>Example 2:</h4>
<pre>Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation: They are too far apart; detonating either triggers only itself.</pre>
<h4>Example 3:</h4>
<pre>Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation: Detonating bomb 0 triggers bombs 1, 2, 3, and 4 transitively.</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; bombs.length &le; 100</li>
<li>bombs[i].length == 3</li>
<li>1 &le; x_i, y_i, r_i &le; 10<sup>5</sup></li>
</ul>""",
    function_name="maximumDetonation",
    template="""class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"bombs": [[2,1,3],[6,1,4]]}, "expected": 2},
        {"input": {"bombs": [[1,1,5],[10,10,5]]}, "expected": 1},
        {"input": {"bombs": [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]}, "expected": 5},
        {"input": {"bombs": [[1,1,1]]}, "expected": 1},
        {"input": {"bombs": [[1,1,100000],[100,100,1]]}, "expected": 2},
        {"input": {"bombs": [[1,1,5],[1,6,1],[1,12,1]]}, "expected": 2},
    ],
    solution="""class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        from collections import defaultdict, deque
        n = len(bombs)
        # Build a directed reachability graph: i -> j iff bomb j's center
        # lies inside (or on) bomb i's blast circle.
        # Use squared distances to avoid floating-point issues.
        adj = defaultdict(list)
        for i in range(n):
            xi, yi, ri = bombs[i]
            r2 = ri * ri
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                dx = xi - xj
                dy = yi - yj
                if dx*dx + dy*dy <= r2:
                    adj[i].append(j)

        best = 0
        for start in range(n):
            seen = {start}
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            if len(seen) > best:
                best = len(seen)
                if best == n:
                    return n
        return best
""",
    explanation="""**Approach: Directed Reachability + BFS from Each Bomb**

**Time:** O(n^3) | **Space:** O(n^2) for the adjacency list in the worst case

1. **Edge construction:** For every ordered pair `(i, j)`, draw a directed edge `i -> j` iff bomb `j`'s center is within (or on) bomb `i`'s blast radius. Use **squared distances** (`dx*dx + dy*dy &le; r_i*r_i`) — comparing in squared units avoids floating-point error and is faster than `sqrt`.
2. **Search:** BFS from each bomb to count how many are reachable in the chain. Track the max.
3. **Early exit:** If a start already triggers all `n` bombs, return immediately.

**Why directed:** Reachability is asymmetric. A small bomb sitting inside a big bomb's blast radius will be triggered by the big one, but detonating the small bomb may not reach the big one's center.

**Why not Union-Find:** UF needs symmetric edges. Adding both directions for "either side covers the other" loses correctness — you'd merge bombs that aren't actually mutually reachable.

**Complexity note:** With `n &le; 100`, O(n^3) is trivially fine. For larger inputs, condensing into strongly connected components (Tarjan/Kosaraju) and counting reachable component sizes would scale better.
"""
)

_register(1804,
    description="""<h3>1804. Implement Trie II (Prefix Tree)</h3>
<p>A <strong>trie</strong> (pronounced as "try") or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>
<p>Implement the Trie class:</p>
<ul>
<li><code>Trie()</code> Initializes the trie object.</li>
<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
<li><code>int countWordsEqualTo(String word)</code> Returns the number of instances of the string <code>word</code> in the trie.</li>
<li><code>int countWordsStartingWith(String prefix)</code> Returns the number of strings in the trie that have the string <code>prefix</code> as a prefix.</li>
<li><code>void erase(String word)</code> Erases the string <code>word</code> from the trie. It is guaranteed that the word was previously inserted.</li>
</ul>
<h4>Example 1:</h4>
<pre>Input
["Trie","insert","insert","countWordsEqualTo","countWordsStartingWith","erase","countWordsEqualTo","countWordsStartingWith","erase","countWordsStartingWith"]
[[],["apple"],["apple"],["apple"],["app"],["apple"],["apple"],["app"],["apple"],["app"]]
Output
[null,null,null,2,2,null,1,1,null,0]

Explanation
Trie trie = new Trie();
trie.insert("apple");                          // Inserts "apple".
trie.insert("apple");                          // Inserts another "apple".
trie.countWordsEqualTo("apple");               // 2
trie.countWordsStartingWith("app");            // 2
trie.erase("apple");                           // Erase one "apple".
trie.countWordsEqualTo("apple");               // 1
trie.countWordsStartingWith("app");            // 1
trie.erase("apple");                           // Erase the last "apple".
trie.countWordsStartingWith("app");            // 0</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; word.length, prefix.length &le; 2000</li>
<li>word and prefix consist only of lowercase English letters.</li>
<li>At most 3 * 10<sup>4</sup> calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.</li>
<li>It is guaranteed that for any function call to erase, the string word will exist in the trie.</li>
</ul>
<p><em>The test wrapper at the bottom replays a sequence of operations and arguments — do not modify it.</em></p>""",
    function_name="trie",
    template="""class Trie:
    def __init__(self):
        # Write your solution here
        pass

    def insert(self, word: str) -> None:
        pass

    def countWordsEqualTo(self, word: str) -> int:
        pass

    def countWordsStartingWith(self, prefix: str) -> int:
        pass

    def erase(self, word: str) -> None:
        pass


# Test wrapper - do not modify
class Solution:
    def trie(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "Trie":
                obj = Trie()
                result.append(None)
            elif op == "insert":
                obj.insert(arg[0])
                result.append(None)
            elif op == "countWordsEqualTo":
                result.append(obj.countWordsEqualTo(arg[0]))
            elif op == "countWordsStartingWith":
                result.append(obj.countWordsStartingWith(arg[0]))
            elif op == "erase":
                obj.erase(arg[0])
                result.append(None)
        return result
""",
    test_cases=[
        {"input": {"operations": ["Trie","insert","insert","countWordsEqualTo","countWordsStartingWith","erase","countWordsEqualTo","countWordsStartingWith","erase","countWordsStartingWith"],
                   "arguments": [[],["apple"],["apple"],["apple"],["app"],["apple"],["apple"],["app"],["apple"],["app"]]},
         "expected": [None, None, None, 2, 2, None, 1, 1, None, 0]},
        {"input": {"operations": ["Trie","countWordsEqualTo","countWordsStartingWith"],
                   "arguments": [[],["a"],["a"]]},
         "expected": [None, 0, 0]},
        {"input": {"operations": ["Trie","insert","insert","insert","countWordsStartingWith","countWordsStartingWith","countWordsEqualTo","erase","countWordsStartingWith"],
                   "arguments": [[],["abc"],["abcd"],["abce"],["ab"],["abc"],["abc"],["abc"],["abc"]]},
         "expected": [None, None, None, None, 3, 3, 1, None, 2]},
        {"input": {"operations": ["Trie","insert","erase","countWordsEqualTo","countWordsStartingWith"],
                   "arguments": [[],["x"],["x"],["x"],["x"]]},
         "expected": [None, None, None, 0, 0]},
    ],
    solution="""class _Node:
    __slots__ = ('children', 'count', 'prefix_count')
    def __init__(self):
        self.children = {}
        self.count = 0          # number of inserted words ending exactly here
        self.prefix_count = 0   # number of inserted words passing through here


class Trie:
    def __init__(self):
        self.root = _Node()

    def insert(self, word: str) -> None:
        node = self.root
        node.prefix_count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _Node()
            node = node.children[ch]
            node.prefix_count += 1
        node.count += 1

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            nxt = node.children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node

    def countWordsEqualTo(self, word: str) -> int:
        node = self._walk(word)
        return node.count if node else 0

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._walk(prefix)
        return node.prefix_count if node else 0

    def erase(self, word: str) -> None:
        # Guaranteed the word exists; decrement counts along its path.
        node = self.root
        node.prefix_count -= 1
        path = []
        for ch in word:
            parent = node
            node = node.children[ch]
            node.prefix_count -= 1
            path.append((parent, ch, node))
        node.count -= 1
        # Optional cleanup: drop nodes that no longer carry any inserted words.
        for parent, ch, child in path:
            if child.prefix_count == 0:
                del parent.children[ch]
                break  # everything deeper is unreachable now


class Solution:
    def trie(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "Trie":
                obj = Trie()
                result.append(None)
            elif op == "insert":
                obj.insert(arg[0])
                result.append(None)
            elif op == "countWordsEqualTo":
                result.append(obj.countWordsEqualTo(arg[0]))
            elif op == "countWordsStartingWith":
                result.append(obj.countWordsStartingWith(arg[0]))
            elif op == "erase":
                obj.erase(arg[0])
                result.append(None)
        return result
""",
    explanation="""**Approach: Trie with Two Counters per Node**

**Time:** O(L) per operation (L = word length) | **Space:** O(total characters inserted, net of erasures)

Unlike #208 which only needed an end-of-word boolean, this variant needs to *count* matches. Add two counters per trie node:

- `count` — how many inserted words **end** exactly at this node.
- `prefix_count` — how many inserted words **pass through** this node.

Operations:

- **insert:** walk/create nodes; bump `prefix_count` at every node visited (including the root), then bump `count` at the final node.
- **countWordsEqualTo(word):** walk the word; return `final.count` or `0` if the path doesn't exist.
- **countWordsStartingWith(prefix):** walk the prefix; return `final.prefix_count` or `0`.
- **erase(word):** walk down, decrementing `prefix_count` at each step; decrement `count` at the final node. The problem guarantees the word exists, so we don't need defensive checks. We also prune any node whose `prefix_count` drops to 0 to keep memory bounded under heavy churn.

**Why two counters:** A trie with a single "is-end" flag (like #208) can't answer "how many" — duplicates are indistinguishable. Promoting the flag to `count` handles duplicates; `prefix_count` is what makes `countWordsStartingWith` O(L) instead of requiring a subtree walk.
"""
)

_register(79,
    description="""<h3>79. Word Search</h3>
<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> if <code>word</code> exists in the grid.</p>
<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>
<h4>Example 1:</h4>
<pre>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true</pre>
<h4>Example 3:</h4>
<pre>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li>m == board.length</li>
<li>n == board[i].length</li>
<li>1 &le; m, n &le; 6</li>
<li>1 &le; word.length &le; 15</li>
<li>board and word consist of only lowercase and uppercase English letters.</li>
</ul>""",
    function_name="exist",
    template="""class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "word": "ABCCED"}, "expected": True},
        {"input": {"board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "word": "SEE"}, "expected": True},
        {"input": {"board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "word": "ABCB"}, "expected": False},
        {"input": {"board": [["a"]], "word": "a"}, "expected": True},
        {"input": {"board": [["a"]], "word": "b"}, "expected": False},
        {"input": {"board": [["a","b"],["c","d"]], "word": "acdb"}, "expected": True},
        {"input": {"board": [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "word": "aaaaaaaaaaaaa"}, "expected": False},
    ],
    solution="""class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            # Mark visited by overwriting; restore on backtrack.
            saved = board[r][c]
            board[r][c] = '#'
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            board[r][c] = saved
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
""",
    explanation="""**Approach: DFS Backtracking with In-Place Visited Marking**

**Time:** O(m * n * 4^L) worst case, where L = len(word) | **Space:** O(L) recursion depth

1. Try every cell as a starting point — but only if it matches `word[0]`.
2. From a matching cell, DFS in all four directions, advancing through the word one character per step.
3. Mark the current cell as used by overwriting it with a sentinel (`'#'`). Restore on backtrack so the rest of the search tree sees the original board.

**Why in-place marking instead of a `visited` set:** Avoids allocating O(m * n) extra memory per call and is slightly faster — set membership has hash overhead, a single-character overwrite is a direct array write. Some interviewers consider mutating input poor style; the alternative is a `set` of `(r, c)` you add on entry and discard on backtrack.

**Pruning matters at scale:** Without early termination on mismatch (`board[r][c] != word[i]`), the 4-direction recursion would blow up exponentially. The early return collapses huge swaths of the search tree.
"""
)

_register(303,
    description="""<h3>303. Range Sum Query - Immutable</h3>
<p>Given an integer array <code>nums</code>, handle multiple queries of the following type:</p>
<ol>
<li>Calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong>, where <code>left &le; right</code>.</li>
</ol>
<p>Implement the <code>NumArray</code> class:</p>
<ul>
<li><code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
<li><code>int sumRange(int left, int right)</code> Returns the sum of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> inclusive (i.e. <code>nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>
<h4>Example 1:</h4>
<pre>Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>4</sup></li>
<li>-10<sup>5</sup> &le; nums[i] &le; 10<sup>5</sup></li>
<li>0 &le; left &le; right &lt; nums.length</li>
<li>At most 10<sup>4</sup> calls will be made to sumRange.</li>
</ul>
<p><em>The test wrapper at the bottom replays a sequence of operations and arguments — do not modify it.</em></p>""",
    function_name="numArray",
    template="""class NumArray:
    def __init__(self, nums: list[int]):
        # Write your solution here
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


# Test wrapper - do not modify
class Solution:
    def numArray(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "NumArray":
                obj = NumArray(arg[0])
                result.append(None)
            elif op == "sumRange":
                result.append(obj.sumRange(arg[0], arg[1]))
        return result
""",
    test_cases=[
        {"input": {"operations": ["NumArray","sumRange","sumRange","sumRange"],
                   "arguments": [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]},
         "expected": [None, 1, -1, -3]},
        {"input": {"operations": ["NumArray","sumRange"], "arguments": [[[5]], [0, 0]]},
         "expected": [None, 5]},
        {"input": {"operations": ["NumArray","sumRange","sumRange","sumRange","sumRange"],
                   "arguments": [[[1,2,3,4,5]], [0,4], [1,3], [2,2], [0,0]]},
         "expected": [None, 15, 9, 3, 1]},
        {"input": {"operations": ["NumArray","sumRange","sumRange"], "arguments": [[[-1,-2,-3]], [0,2], [1,1]]},
         "expected": [None, -6, -2]},
    ],
    solution="""class NumArray:
    def __init__(self, nums: list[int]):
        # prefix[i] = sum of nums[0:i]; prefix[0] = 0 so prefix[i] - prefix[j] = sum(nums[j:i]).
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


class Solution:
    def numArray(self, operations: list[str], arguments: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, arguments):
            if op == "NumArray":
                obj = NumArray(arg[0])
                result.append(None)
            elif op == "sumRange":
                result.append(obj.sumRange(arg[0], arg[1]))
        return result
""",
    explanation="""**Approach: Prefix Sum**

**Time:** O(n) preprocessing in `__init__`, O(1) per `sumRange` | **Space:** O(n)

Build `prefix[i] = nums[0] + ... + nums[i-1]` once at construction (with `prefix[0] = 0` so we don't have to special-case `left == 0`). Then any range sum is `prefix[right + 1] - prefix[left]` — a single subtraction.

**Why offset by 1:** Storing the empty-prefix sentinel at index 0 makes `sumRange(0, r)` use the same formula as `sumRange(l, r)` with no branching. It's a cleaner invariant than two separate cases.

**Why prefix sums for "immutable":** The array doesn't change, so we pay the O(n) preprocessing cost once and amortize across many queries. With Q queries on an n-element array, total work is O(n + Q) vs. O(n * Q) for naive per-query sums. For mutable arrays, see #307 — a segment tree or Fenwick tree gets you O(log n) updates.
"""
)


_register(496,
    description="""<h3>496. Next Greater Element I</h3>
<p>The <strong>next greater element</strong> of some element <code>x</code> in an array is the <strong>first greater</strong> element that is <strong>to the right</strong> of <code>x</code> in the same array.</p>
<p>You are given two <strong>distinct 0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code>, where <code>nums1</code> is a subset of <code>nums2</code>.</p>
<p>For each <code>0 &le; i &lt; nums1.length</code>, find the index <code>j</code> such that <code>nums1[i] == nums2[j]</code> and determine the <strong>next greater element</strong> of <code>nums2[j]</code> in <code>nums2</code>. If there is no next greater element, the answer for this query is <code>-1</code>.</p>
<p>Return an array <code>ans</code> of length <code>nums1.length</code> such that <code>ans[i]</code> is the <strong>next greater element</strong> as described above.</p>
<h4>Example 1:</h4>
<pre>Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
- 4 is in nums2 at index 2. No element to the right is greater -> -1.
- 1 is in nums2 at index 0. 3 is the first greater to the right -> 3.
- 2 is in nums2 at index 3. No element to the right -> -1.</pre>
<h4>Example 2:</h4>
<pre>Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums1.length &le; nums2.length &le; 1000</li>
<li>0 &le; nums1[i], nums2[i] &le; 10<sup>4</sup></li>
<li>All integers in <code>nums1</code> and <code>nums2</code> are <strong>unique</strong>.</li>
<li>All the integers of <code>nums1</code> also appear in <code>nums2</code>.</li>
</ul>
<p><strong>Follow up:</strong> Could you find an O(nums1.length + nums2.length) solution?</p>""",
    function_name="nextGreaterElement",
    template="""class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}, "expected": [-1, 3, -1]},
        {"input": {"nums1": [2, 4], "nums2": [1, 2, 3, 4]}, "expected": [3, -1]},
        {"input": {"nums1": [1], "nums2": [1]}, "expected": [-1]},
        {"input": {"nums1": [3, 1, 5, 7], "nums2": [3, 1, 5, 7, 9, 2, 4]}, "expected": [5, 5, 7, 9]},
        {"input": {"nums1": [9, 8, 7], "nums2": [7, 8, 9]}, "expected": [-1, 9, 8]},
    ],
    solution="""class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Monotonic decreasing stack: pop while current beats the top, mapping each
        # popped value to the current as its next-greater. Anything left in the stack
        # at the end has no next-greater. Since values are unique, a value -> nextGreater
        # dict works as a clean lookup for nums1.
        next_greater = {}
        stack = []  # monotonically decreasing from bottom to top
        for x in nums2:
            while stack and stack[-1] < x:
                next_greater[stack.pop()] = x
            stack.append(x)
        return [next_greater.get(v, -1) for v in nums1]
""",
    explanation="""**Approach: Monotonic Decreasing Stack**

**Time:** O(n + m) where n = len(nums2), m = len(nums1) | **Space:** O(n)

Scan `nums2` once. Maintain a stack whose values strictly decrease from bottom to top — this is the invariant. When we see a new value `x`:

- Anything on the stack smaller than `x` has just found its next-greater (it's `x`). Pop and record in a dict.
- Push `x`. The stack remains decreasing.

After the pass, anything still on the stack has no next-greater; those entries are simply absent from the dict. Build the answer by looking up each `nums1[i]` (defaulting to `-1`).

**Why monotonic stack:** Each element is pushed once and popped at most once, so the total work is O(n) despite the inner `while`. Brute force is O(n*m).

**Why a dict (not indices):** The problem guarantees uniqueness across both arrays, so value -> nextGreater is unambiguous. With duplicates we'd need to use indices.
"""
)


_register(503,
    description="""<h3>503. Next Greater Element II</h3>
<p>Given a <strong>circular</strong> integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em>the <strong>next greater number</strong> for every element in</em> <code>nums</code>.</p>
<p>The <strong>next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return <code>-1</code> for this number.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; nums.length &le; 10<sup>4</sup></li>
<li>-10<sup>9</sup> &le; nums[i] &le; 10<sup>9</sup></li>
</ul>""",
    function_name="nextGreaterElements",
    template="""class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1, 2, 1]}, "expected": [2, -1, 2]},
        {"input": {"nums": [1, 2, 3, 4, 3]}, "expected": [2, 3, 4, -1, 4]},
        {"input": {"nums": [5, 4, 3, 2, 1]}, "expected": [-1, 5, 5, 5, 5]},
        {"input": {"nums": [1, 1, 1, 1]}, "expected": [-1, -1, -1, -1]},
        {"input": {"nums": [100]}, "expected": [-1]},
        {"input": {"nums": [-1, 0, -2, 1, -3]}, "expected": [0, 1, 1, -1, -1]},
    ],
    solution="""class Solution:
    def nextGreaterElements(self, nums):
        # Circular trick: walk the array twice (2n iterations) using i % n to index.
        # The stack holds indices (not values) so we can write the answer in place.
        # Only push real indices on the first pass; on the second pass we just pop
        # — anything not resolved by then truly has no next-greater.
        n = len(nums)
        result = [-1] * n
        stack = []  # indices, values monotonically decreasing
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)
        return result
""",
    explanation="""**Approach: Monotonic Stack over a Doubled Index Range**

**Time:** O(n) — each index is pushed at most once and popped at most once | **Space:** O(n)

The circular twist on #496 is handled by simulating two passes: iterate `i` from `0` to `2n - 1` and use `nums[i % n]`. Two laps are enough because any element that hasn't found its next-greater after one full wraparound never will.

Two key choices:

1. **Stack stores indices, not values.** We need to write into `result[stack.pop()]`, so the index is what matters. Comparisons are still on `nums[stack[-1]]`.
2. **Only push during the first pass (`if i < n`).** The second pass exists solely to *resolve* indices left over from the first; pushing again would double-count and even cause infinite resolution loops in some shapes.

**Why two laps suffice:** For index `j`, the worst case is the next greater sits at `j - 1` (just behind in circular order). Walking from `j` to `j + n - 1` (i.e., `2n - 1` in the doubled range when `j = n - 1`) covers every other position exactly once.

**Why not store the actual element value?** With duplicates allowed, value -> nextGreater isn't unique — indexing keeps each occurrence distinct.
"""
)


_register(305,
    description="""<h3>305. Number of Islands II</h3>
<p>You are given an empty 2D binary grid <code>grid</code> of size <code>m x n</code>. The grid represents a map where <code>0</code>'s represent water and <code>1</code>'s represent land. Initially, all the cells of <code>grid</code> are water cells (i.e., all the cells are <code>0</code>'s).</p>
<p>We may perform an add land operation which turns the water at position into a land. You are given an array <code>positions</code> where <code>positions[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> is the position <code>(r<sub>i</sub>, c<sub>i</sub>)</code> at which we should operate the <code>i<sup>th</sup></code> operation.</p>
<p>Return <em>an array of integers</em> <code>answer</code> <em>where</em> <code>answer[i]</code> <em>is the number of islands after turning the cell</em> <code>(r<sub>i</sub>, c<sub>i</sub>)</code> <em>into a land</em>.</p>
<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>
<h4>Example 1:</h4>
<pre>Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
- Add land at (0,0): island count = 1
- Add land at (0,1): merges with (0,0), count stays 1
- Add land at (1,2): new isolated island, count = 2
- Add land at (2,1): new isolated island, count = 3</pre>
<h4>Example 2:</h4>
<pre>Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; m, n, m * n &le; 10<sup>4</sup></li>
<li>1 &le; positions.length &le; 10<sup>4</sup></li>
<li>0 &le; r<sub>i</sub> &lt; m</li>
<li>0 &le; c<sub>i</sub> &lt; n</li>
</ul>
<p><strong>Follow up:</strong> Could you solve it in time complexity <code>O(k log(m * n))</code>, where <code>k</code> is the length of <code>positions</code>?</p>""",
    function_name="numIslands2",
    template="""class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"m": 3, "n": 3, "positions": [[0,0],[0,1],[1,2],[2,1]]},
         "expected": [1, 1, 2, 3]},
        {"input": {"m": 1, "n": 1, "positions": [[0,0]]},
         "expected": [1]},
        {"input": {"m": 3, "n": 3, "positions": [[0,0],[0,0],[0,1]]},
         "expected": [1, 1, 1]},
        {"input": {"m": 3, "n": 3, "positions": [[0,1],[1,2],[2,1],[1,0],[1,1]]},
         "expected": [1, 2, 3, 4, 1]},
        {"input": {"m": 2, "n": 2, "positions": [[0,0],[1,1],[0,1],[1,0]]},
         "expected": [1, 2, 1, 1]},
        {"input": {"m": 3, "n": 3, "positions": []},
         "expected": []},
    ],
    solution="""class Solution:
    def numIslands2(self, m, n, positions):
        # Union-Find with path compression and union-by-rank.
        # Key insight: rather than rebuilding islands per query (O(k * m * n) flood fill),
        # incrementally maintain island count. Each new land starts as +1 island; each union
        # with an existing land neighbor (only if currently in a DIFFERENT component) is -1.
        parent = [-1] * (m * n)  # -1 sentinel = still water
        rank = [0] * (m * n)

        def find(x):
            # iterative with path compression
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        result = []
        count = 0
        for r, c in positions:
            idx = r * n + c
            if parent[idx] != -1:
                # Already land — duplicate position; count is unchanged.
                result.append(count)
                continue
            parent[idx] = idx  # initialize as its own root
            count += 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nidx = nr * n + nc
                    if parent[nidx] != -1 and union(idx, nidx):
                        count -= 1
            result.append(count)
        return result
""",
    explanation="""**Approach: Incremental Union-Find**

**Time:** O(k * alpha(m * n)) per operation -> essentially O(k) total; O(k log(m * n)) is the textbook bound | **Space:** O(m * n)

The brute-force approach is to re-flood-fill the entire grid after every operation — O(k * m * n). Union-Find flips this around: we don't recount islands; we maintain the count incrementally.

**The trick — "diffs", not totals:**

- A new land cell is, on its own, +1 island.
- For each of the (up to 4) neighboring cells that's already land:
  - If `union(new, neighbor)` succeeds (they were in *different* components), -1 island.
  - If they were already in the *same* component, no change. This is what `find` is for.

So `delta = 1 - successful_unions`. A cell joining 3 distinct neighbors goes +1 - 3 = -2 islands.

**Implementation details:**

- **`parent[i] = -1` as a "water" sentinel.** Saves a separate `seen` set. Initializing `parent[idx] = idx` is the moment a cell "exists" in the DSU.
- **Path compression + union by rank.** Together they give near-O(1) amortized per operation (inverse Ackermann). One without the other still works but is slower.
- **Duplicate positions.** LC allows the same cell in `positions` more than once. We must NOT add to the count; just append the current count and skip. Forgetting this is the most common bug.
- **Row-major index `r * n + c`.** A flat parent array beats `dict[(r,c)] -> (r,c)` on both speed and memory.

**Why not BFS/DFS per step?** Each step is O(m * n) flood fill, so total is O(k * m * n). With k = m * n = 10^4, that's 10^8 ops vs ~10^4 for DSU. The difference matters on the LC hard test cases.
"""
)


_register(133,
    description="""<h3>133. Clone Graph</h3>
<p>Given a reference of a node in a <strong>connected</strong> undirected graph.</p>
<p>Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy">deep copy</a> (clone) of the graph.</p>
<p>Each node in the graph contains a value (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>
<pre>class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}</pre>
<p><strong>Test case format:</strong></p>
<p>For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with <code>val == 1</code>, the second node with <code>val == 2</code>, and so on. The graph is represented in the test case using an adjacency list.</p>
<p>An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.</p>
<p>The given node will always be the first node with <code>val = 1</code>. You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</p>
<h4>Example 1:</h4>
<pre>Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).</pre>
<h4>Example 2:</h4>
<pre>Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.</pre>
<h4>Example 3:</h4>
<pre>Input: adjList = []
Output: []
Explanation: This is an empty graph, it does not have any nodes.</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in the graph is in the range <code>[0, 100]</code>.</li>
<li>1 &le; Node.val &le; 100</li>
<li><code>Node.val</code> is unique for each node.</li>
<li>There are no repeated edges and no self-loops in the graph.</li>
<li>The graph is connected and all nodes can be visited starting from the given node.</li>
</ul>
<p><em>Note: the test harness converts the input adjacency list into <code>Node</code> objects before calling your function, and converts your returned <code>Node</code> back into an adjacency list for comparison. You write against the <code>Node</code> class as-is — neighbors lists in the comparison are sorted, so neighbor ordering doesn't matter.</em></p>""",
    function_name="cloneGraph",
    template="""# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"node": [[2, 4], [1, 3], [2, 4], [1, 3]]},
         "expected": [[2, 4], [1, 3], [2, 4], [1, 3]]},
        {"input": {"node": [[]]}, "expected": [[]]},
        {"input": {"node": []}, "expected": []},
        {"input": {"node": [[2], [1]]}, "expected": [[2], [1]]},
        {"input": {"node": [[2, 3], [1, 3], [1, 2]]},
         "expected": [[2, 3], [1, 3], [1, 2]]},
        {"input": {"node": [[2], [1, 3], [2, 4], [3, 5], [4]]},
         "expected": [[2], [1, 3], [2, 4], [3, 5], [4]]},
    ],
    solution="""class Solution:
    def cloneGraph(self, node):
        # DFS with a memo dict: original_node -> cloned_node. The memo serves two
        # purposes: (1) cycle prevention — without it, recursing into neighbors loops
        # forever on any back-edge; (2) identity — two paths reaching the same original
        # node must return the SAME clone, not two copies.
        if node is None:
            return None
        clones = {}

        def dfs(orig):
            if orig in clones:
                return clones[orig]
            copy = Node(orig.val)
            clones[orig] = copy  # MUST register before recursing into neighbors
            copy.neighbors = [dfs(nb) for nb in orig.neighbors]
            return copy

        return dfs(node)
""",
    explanation="""**Approach: DFS with a memo (original -> clone)**

**Time:** O(V + E) | **Space:** O(V) for the memo + recursion stack

The whole problem is about preserving graph structure across the clone:

1. **Don't double-create.** If two paths reach the same original node, they must yield the same clone, not two distinct copies. The memo `clones[orig] = copy` enforces this.
2. **Don't loop forever.** Any cycle (and an undirected graph always has 2-cycles via A<->B) needs cycle detection. The memo doubles as the visited set.

**The critical ordering — register clone BEFORE recursing into neighbors:**

```python
copy = Node(orig.val)
clones[orig] = copy            # <-- this line MUST come before the next
copy.neighbors = [dfs(nb) for nb in orig.neighbors]
```

If you set `copy.neighbors` first and THEN insert into `clones`, the recursive call for a neighbor that points back at `orig` won't find it in the memo, will create a second clone, and you'll get either infinite recursion or a corrupted graph.

**BFS is equally valid:** queue + same memo. Pick BFS if recursion depth is a concern (graph with 10^5 nodes in a chain).

**Why a dict keyed on the original Node object:** Identity, not equality. `dict` uses `__hash__`/`__eq__` which default to identity for objects without overrides, so each original node gets its own memo slot.
"""
,
    harness={"input": {"node": "graph"}, "output": "graph"}
)


_register(269,
    description="""<h3>269. Alien Dictionary</h3>
<p>There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.</p>
<p>You are given a list of strings <code>words</code> from the alien language's dictionary. Now it is claimed that the strings in <code>words</code> are <strong>sorted lexicographically</strong> by the rules of this new language.</p>
<p>If this claim is incorrect, and the given arrangement of string in <code>words</code> cannot correspond to any order of letters, return <code>""</code>.</p>
<p>Otherwise, return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language's rules</em>. If there are multiple solutions, return <strong>any of them</strong>.</p>
<h4>Example 1:</h4>
<pre>Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"</pre>
<h4>Example 2:</h4>
<pre>Input: words = ["z","x"]
Output: "zx"</pre>
<h4>Example 3:</h4>
<pre>Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".</pre>
<h4>Constraints:</h4>
<ul>
<li>1 &le; words.length &le; 100</li>
<li>1 &le; words[i].length &le; 100</li>
<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>
<p><em>Note: tests accept any valid ordering by checking that the result respects all derived precedence constraints AND uses exactly the set of letters that appear in the input.</em></p>""",
    function_name="alienOrder",
    template="""class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"words": ["wrt","wrf","er","ett","rftt"]}, "expected": "wertf"},
        {"input": {"words": ["z","x"]}, "expected": "zx"},
        {"input": {"words": ["z","x","z"]}, "expected": ""},
        {"input": {"words": ["abc","ab"]}, "expected": ""},
        {"input": {"words": ["ab","adc"]}, "expected": ["abcd", "abdc", "acbd", "bacd", "badc", "bcad", "bcda", "bdac", "bdca", "cabd", "cbad", "cbda"]},
        {"input": {"words": ["ac","ab","zc","zb"]}, "expected": ["acbz", "aczb", "azcb", "cabz", "cazb", "cbaz"]},
        {"input": {"words": ["a"]}, "expected": "a"},
        {"input": {"words": ["aa","aa"]}, "expected": ["a"]},
    ],
    solution="""class Solution:
    def alienOrder(self, words):
        from collections import defaultdict, deque
        # Step 1: seed in-degree for every letter that actually appears. Letters
        # with no constraints still need to show up in the output.
        in_degree = {c: 0 for w in words for c in w}
        graph = defaultdict(set)

        # Step 2: derive one edge per adjacent word pair from the first differing char.
        # Edge a -> b means "a comes before b". If a word is a strict prefix of the
        # PREVIOUS word (e.g., "abc" before "ab"), the ordering is impossible.
        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    if w2[i] not in graph[w1[i]]:
                        graph[w1[i]].add(w2[i])
                        in_degree[w2[i]] += 1
                    break

        # Step 3: Kahn's BFS topological sort.
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        order = []
        while queue:
            c = queue.popleft()
            order.append(c)
            for nb in graph[c]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    queue.append(nb)

        # If a cycle exists, we couldn't drain every letter.
        return "".join(order) if len(order) == len(in_degree) else ""
""",
    explanation="""**Approach: Build a precedence graph from adjacent word pairs, then topological sort**

**Time:** O(C) where C = total characters across all words | **Space:** O(U + E), U = unique letters

The algorithm is short but every step has a trap:

**1. Seed in-degree for every letter that appears.** Letters with no precedence constraints (e.g., "z" in `["z","x"]` has no incoming edge from the comparison, only outgoing) still need to appear in the output. A common bug is initializing in-degree only from edges — letters with no edges get dropped silently.

**2. One edge per adjacent word pair.** Compare consecutive words; the FIRST differing character gives you exactly one ordering constraint. Don't try to derive more from a single pair — `"abc"` < `"bcd"` only tells you `a < b`, not anything about `b` vs `c`.

**3. The prefix-is-impossible case.** If `w1` is longer than `w2` and `w1` starts with `w2` (e.g., `"abc","ab"`), then by lexicographic rules `w2` should have come first. This input is invalid; return `""`. Easy to forget — without this check, the prefix case falls through with no edges added and you'd return a spuriously valid ordering.

**4. Deduplicate edges.** Multiple word pairs can yield the same edge (e.g., `a -> b` from `("ab","bc")` and again from `("ax","bx")`). Adding it twice double-counts in-degree, making the destination unreachable. Use a `set` for adjacency or check before incrementing.

**5. Kahn's BFS for the topo sort.** Start from letters with in-degree 0, drain dependents. If the output has fewer letters than the unique-letter count, there's a cycle (`""`). DFS with three-color marking is an equally valid alternative.

**Why a graph at all, not just sort the letters?** The input gives you a *partial* order, not a total one. Some letter pairs are unconstrained — any valid topological sort is acceptable. That's also why the LC problem statement says "if there are multiple solutions, return any".
"""
)


_register(112,
    description="""<h3>112. Path Sum</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a <strong>root-to-leaf</strong> path such that adding up all the values along the path equals <code>targetSum</code>.</p>
<p>A <strong>leaf</strong> is a node with no children.</p>
<h4>Example 1:</h4>
<pre>Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with sum 22 is: 5 -> 4 -> 11 -> 2.</pre>
<h4>Example 2:</h4>
<pre>Input: root = [1,2,3], targetSum = 5
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: root = [], targetSum = 0
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes is in the range <code>[0, 5000]</code>.</li>
<li>-1000 &le; Node.val &le; 1000</li>
<li>-1000 &le; targetSum &le; 1000</li>
</ul>
<p><em>The test harness builds a <code>TreeNode</code> tree from the level-order list (with <code>None</code> for null) before calling your function. Write against real <code>TreeNode</code> objects with <code>.val</code>, <code>.left</code>, <code>.right</code>.</em></p>""",
    function_name="hasPathSum",
    template="""# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"root": [5,4,8,11,None,13,4,7,2,None,None,None,1], "targetSum": 22}, "expected": True},
        {"input": {"root": [1,2,3], "targetSum": 5}, "expected": False},
        {"input": {"root": [], "targetSum": 0}, "expected": False},
        {"input": {"root": [1,2], "targetSum": 1}, "expected": False},
        {"input": {"root": [1,2], "targetSum": 3}, "expected": True},
        {"input": {"root": [-2,None,-3], "targetSum": -5}, "expected": True},
        {"input": {"root": [1,-2,-3,1,3,-2,None,-1], "targetSum": 3}, "expected": False},
        {"input": {"root": [1], "targetSum": 1}, "expected": True},
        {"input": {"root": [0,1,1], "targetSum": 1}, "expected": True},
    ],
    solution="""class Solution:
    def hasPathSum(self, root, targetSum):
        # Recursive DFS with running remainder. At each leaf, check if the
        # remaining sum equals the leaf's own value (we haven't subtracted it yet).
        if root is None:
            return False
        # Leaf: this is the only place we accept. Internal nodes can't be path ends.
        if root.left is None and root.right is None:
            return targetSum == root.val
        rem = targetSum - root.val
        return self.hasPathSum(root.left, rem) or self.hasPathSum(root.right, rem)
""",
    explanation="""**Approach: Recursive DFS with running remainder**

**Time:** O(n) | **Space:** O(h) for recursion stack (h = tree height, worst case n)

**The two traps:**

1. **"Path" means root-to-LEAF.** Not root-to-any-node. So you only accept at a leaf — a node whose `left` AND `right` are both `None`. A common bug: returning early at a node whose value equals the remaining sum without checking that it's a leaf.
2. **Empty tree returns false, even if `targetSum == 0`.** "No root-to-leaf path exists" trumps the sum check. The recursion handles this because `None` returns false immediately.

**Why the remainder pattern (not accumulating)?** Either works, but subtracting from `targetSum` as we descend means the leaf-check is a single equality `remaining == node.val` rather than `accumulated + node.val == targetSum` with a separate accumulator. Less to track.

**Iterative BFS alternative:** queue of `(node, remaining)` pairs. Same complexity, avoids recursion depth issues on a 5000-node degenerate (linked-list-shaped) tree.
"""
,
    harness={"input": {"root": "tree"}}
)


_register(113,
    description="""<h3>113. Path Sum II</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>all <strong>root-to-leaf</strong> paths where the sum of the node values in the path equals</em> <code>targetSum</code>. Each path should be returned as a list of the node <strong>values</strong>, not node references.</p>
<p>A <strong>root-to-leaf</strong> path is a path starting from the root and ending at any leaf node. A <strong>leaf</strong> is a node with no children.</p>
<h4>Example 1:</h4>
<pre>Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]</pre>
<h4>Example 2:</h4>
<pre>Input: root = [1,2,3], targetSum = 5
Output: []</pre>
<h4>Example 3:</h4>
<pre>Input: root = [1,2], targetSum = 0
Output: []</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes is in the range <code>[0, 5000]</code>.</li>
<li>-1000 &le; Node.val &le; 1000</li>
<li>-1000 &le; targetSum &le; 1000</li>
</ul>
<p><em>The test harness builds a <code>TreeNode</code> tree from the level-order list before calling your function. Write against real <code>TreeNode</code> objects with <code>.val</code>, <code>.left</code>, <code>.right</code>.</em></p>""",
    function_name="pathSum",
    template="""# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"root": [5,4,8,11,None,13,4,7,2,None,None,5,1], "targetSum": 22},
         "expected": [[5,4,11,2],[5,8,4,5]]},
        {"input": {"root": [1,2,3], "targetSum": 5}, "expected": []},
        {"input": {"root": [1,2], "targetSum": 0}, "expected": []},
        {"input": {"root": [], "targetSum": 0}, "expected": []},
        {"input": {"root": [1,2], "targetSum": 3}, "expected": [[1,2]]},
        {"input": {"root": [1,-2,-3,1,3,-2,None,-1], "targetSum": -1}, "expected": [[1,-2,1,-1]]},
        {"input": {"root": [0,1,1], "targetSum": 1}, "expected": [[0,1],[0,1]]},
        {"input": {"root": [1], "targetSum": 1}, "expected": [[1]]},
    ],
    solution="""class Solution:
    def pathSum(self, root, targetSum):
        # Backtracking DFS. Maintain ONE shared path list; push on entry, pop on exit.
        # When we find a matching leaf, snapshot the path (path.copy() / list(path)).
        # Without the copy, the result would alias the shared list and all entries
        # would end up identical (and empty) after backtracking.
        result = []
        def dfs(node, remaining, path):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None and remaining == node.val:
                result.append(path.copy())
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            path.pop()

        dfs(root, targetSum, [])
        return result
""",
    explanation="""**Approach: Backtracking DFS with a shared path buffer**

**Time:** O(n^2) worst case | **Space:** O(h) for the recursion + path; O(n^2) if you count result storage

**The path-copy invariant.** This is THE bug everyone writes first:

```python
def dfs(node, remaining, path):
    path.append(node.val)
    if leaf and matches:
        result.append(path)          # BUG: aliases the shared list
    dfs(...); dfs(...)
    path.pop()
```

Append-without-copy stores a reference to the live `path` list. By the time the function returns, every `pop` along the way mutates that same list — every entry in `result` ends up pointing at the SAME `[]`. Fix: `result.append(path.copy())` (or `list(path)`, or pass `path + [node.val]` instead of mutating).

**Why O(n^2) worst case?** A balanced tree can have ~n/2 leaves, each path of length log n -> O(n log n). A degenerate "every path leads to a match" tree could give n paths of length n -> O(n^2) just to copy them all.

**Why backtrack instead of `path + [node.val]`?** Both work. The immutable variant allocates O(h) per recursive call vs O(1) for backtracking. For deep trees the difference matters.

**Path = root to LEAF.** Same trap as #112 — accept only when both children are `None`.
"""
,
    harness={"input": {"root": "tree"}}
)


_register(102,
    description="""<h3>102. Binary Tree Level Order Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes' values</em>. (i.e., from left to right, level by level).</p>
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
<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
<li>-1000 &le; Node.val &le; 1000</li>
</ul>
<p><em>The test harness builds a <code>TreeNode</code> tree from the level-order list before calling your function. Write against real <code>TreeNode</code> objects with <code>.val</code>, <code>.left</code>, <code>.right</code>.</em></p>""",
    function_name="levelOrder",
    template="""# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"root": [3,9,20,None,None,15,7]}, "expected": [[3],[9,20],[15,7]]},
        {"input": {"root": [1]}, "expected": [[1]]},
        {"input": {"root": []}, "expected": []},
        {"input": {"root": [1,2,3,4,5,6,7]}, "expected": [[1],[2,3],[4,5,6,7]]},
        {"input": {"root": [1,None,2,None,3,None,4]}, "expected": [[1],[2],[3],[4]]},
        {"input": {"root": [1,2,None,3,None,4,None,5]}, "expected": [[1],[2],[3],[4],[5]]},
        {"input": {"root": [0,-1,1]}, "expected": [[0],[-1,1]]},
    ],
    solution="""class Solution:
    def levelOrder(self, root):
        # BFS with a "level size" snapshot at the top of each iteration. The snapshot
        # is the trick: it freezes the count of nodes belonging to the CURRENT level,
        # so children appended during this iteration don't bleed into it.
        from collections import deque
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
""",
    explanation="""**Approach: BFS with per-level size snapshot**

**Time:** O(n) | **Space:** O(w) where w is the maximum width of the tree (the queue never holds more than one level + the next at any moment)

The whole problem is "BFS, but group output by level." Plain BFS produces a flat sequence; we need brackets. Two clean ways to do it:

**1. Size-snapshot (shown above).** At the start of each iteration, `level_size = len(queue)` freezes how many nodes are on the current level. The inner `for _ in range(level_size)` drains exactly those nodes — children we append during the loop don't get pulled in because the range was fixed BEFORE we started appending.

**2. Sentinel-based.** Push a `None` separator after each level. When you pop the sentinel, close the current level and push a new sentinel (if the queue isn't empty). Works, but the size-snapshot version avoids the sentinel bookkeeping and the edge case of "did I just push the last separator?"

**Why not DFS with a depth parameter?** That works too — recurse with `depth`, append `node.val` to `result[depth]`, growing `result` as you go deeper. But it's preorder, not strict level-order — DFS will visit a deep node before a shallow sibling. Final output is the same when grouped by depth, but BFS more closely matches the "level by level" framing the problem asks for.

**Empty tree returns `[]`, not `[[]]`.** No levels exist, so there's no list to wrap. Easy off-by-one.
"""
,
    harness={"input": {"root": "tree"}}
)


_register(286,
    description="""<h3>286. Walls and Gates</h3>
<p>You are given an <code>m x n</code> grid <code>rooms</code> initialized with these three possible values.</p>
<ul>
<li><code>-1</code> A wall or an obstacle.</li>
<li><code>0</code> A gate.</li>
<li><code>INF</code> Infinity means an empty room. We use the value <code>2<sup>31</sup> - 1 = 2147483647</code> to represent <code>INF</code> as you may assume that the distance to a gate is less than <code>2147483647</code>.</li>
</ul>
<p>Fill each empty room with the distance to its <em>nearest gate</em>. If it is impossible to reach a gate, it should be filled with <code>INF</code>.</p>
<h4>Example 1:</h4>
<pre>Input: rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]</pre>
<h4>Example 2:</h4>
<pre>Input: rooms = [[-1]]
Output: [[-1]]</pre>
<h4>Constraints:</h4>
<ul>
<li>m == rooms.length</li>
<li>n == rooms[i].length</li>
<li>1 &le; m, n &le; 250</li>
<li><code>rooms[i][j]</code> is <code>-1</code>, <code>0</code>, or <code>2<sup>31</sup> - 1</code>.</li>
</ul>
<p><em>LC asks you to modify <code>rooms</code> in-place and return nothing. For testing here, mutate in-place AND return <code>rooms</code> so the runner can verify the result.</em></p>""",
    function_name="wallsAndGates",
    template="""class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> list[list[int]]:
        # Mutate rooms in-place, then return rooms (for the test runner).
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"rooms": [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]
        ]}, "expected": [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]},
        {"input": {"rooms": [[-1]]}, "expected": [[-1]]},
        {"input": {"rooms": [[2147483647]]}, "expected": [[2147483647]]},
        {"input": {"rooms": [[0]]}, "expected": [[0]]},
        {"input": {"rooms": [[0, 2147483647, 2147483647, 2147483647]]},
         "expected": [[0, 1, 2, 3]]},
        {"input": {"rooms": [
            [0, 2147483647],
            [2147483647, 2147483647]
        ]}, "expected": [
            [0, 1],
            [1, 2]
        ]},
        {"input": {"rooms": [
            [2147483647, 2147483647],
            [2147483647, 0]
        ]}, "expected": [
            [2, 1],
            [1, 0]
        ]},
        {"input": {"rooms": [
            [0, -1, 2147483647],
            [-1, -1, 2147483647],
            [2147483647, 2147483647, 2147483647]
        ]}, "expected": [
            [0, -1, 2147483647],
            [-1, -1, 2147483647],
            [2147483647, 2147483647, 2147483647]
        ]},
    ],
    solution="""class Solution:
    def wallsAndGates(self, rooms):
        # Multi-source BFS from ALL gates at once. Seeding every gate into the queue
        # before starting means each cell is reached via the SHORTEST path from
        # SOME gate — exactly the per-cell minimum we need. No per-source loops.
        from collections import deque
        if not rooms or not rooms[0]:
            return rooms
        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                # Only walk into INF cells. Walls (-1) are blocked; gates (0)
                # are sources; any cell already < INF was reached by a closer
                # gate and shouldn't be overwritten.
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
        return rooms
""",
    explanation="""**Approach: Multi-source BFS**

**Time:** O(m * n) — each cell is enqueued at most once | **Space:** O(m * n) for the queue

**The key insight: seed all gates first.** The naive read of the problem is "for each empty room, BFS to the nearest gate" — that's O(m * n * (m + n)) or worse. Multi-source BFS inverts the search: push EVERY gate into the queue at distance 0, then expand outward together. Each empty cell is discovered by the FIRST wave that reaches it — which is necessarily the closest gate.

**The "only walk into INF" check is doing three jobs at once:**

1. **Bounds + walls** — `-1` is not `INF`, so walls block automatically; no separate wall check.
2. **Gates as sources, not destinations** — a `0` cell is not `INF`, so we never overwrite a gate's distance with `1`.
3. **Visited marking** — once a cell is updated to `dist`, it stops being `INF`, so a later wave from a farther gate can't overwrite it. The cell *is* its own visited marker.

This collapses what would normally be a `visited` set + four separate guards into a single equality check.

**Why BFS, not DFS?** BFS expands in distance order — the first time you touch a cell, you've reached it via the shortest path. DFS can revisit and would need a "current best distance" check at every step.

**Watch for:**
- Empty grid: `[]` or `[[]]`. The `if not rooms or not rooms[0]` guard handles both.
- Unreachable rooms (walled off from every gate): they stay `INF`. The algorithm naturally produces this — no special case needed; if BFS never reaches them, they aren't touched.
"""
)


_register(490,
    description="""<h3>490. The Maze</h3>
<p>There is a ball in a <code>maze</code> with empty spaces (represented as <code>0</code>) and walls (represented as <code>1</code>). The ball can go through the empty spaces by rolling <strong>up, down, left or right</strong>, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.</p>
<p>Given the <code>m x n</code> <code>maze</code>, the ball's <code>start</code> position and the <code>destination</code>, where <code>start = [start<sub>row</sub>, start<sub>col</sub>]</code> and <code>destination = [destination<sub>row</sub>, destination<sub>col</sub>]</code>, return <code>true</code> if the ball can stop at the destination, otherwise return <code>false</code>.</p>
<p>You may assume that <strong>the borders of the maze are all walls</strong> (see examples).</p>
<h4>Example 1:</h4>
<pre>Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is: left -> down -> left -> down -> right -> down -> right.</pre>
<h4>Example 2:</h4>
<pre>Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.</pre>
<h4>Example 3:</h4>
<pre>Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li>m == maze.length</li>
<li>n == maze[i].length</li>
<li>1 &le; m, n &le; 100</li>
<li><code>maze[i][j]</code> is <code>0</code> or <code>1</code>.</li>
<li>start.length == 2, destination.length == 2</li>
<li>0 &le; start[0], destination[0] &lt; m</li>
<li>0 &le; start[1], destination[1] &lt; n</li>
<li>Both the ball and the destination exist in an empty space, and they will not be in the same position initially.</li>
<li>The maze contains <strong>at least 2 empty spaces</strong>.</li>
</ul>""",
    function_name="hasPath",
    template="""class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"maze": [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
                   "start": [0,4], "destination": [4,4]}, "expected": True},
        {"input": {"maze": [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
                   "start": [0,4], "destination": [3,2]}, "expected": False},
        {"input": {"maze": [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
                   "start": [4,3], "destination": [0,1]}, "expected": False},
        {"input": {"maze": [[0,0]], "start": [0,0], "destination": [0,1]}, "expected": True},
        {"input": {"maze": [[0,1],[0,0]], "start": [0,0], "destination": [1,1]}, "expected": True},
        {"input": {"maze": [[0,0,0],[1,1,0],[0,0,0]], "start": [0,0], "destination": [2,0]}, "expected": True},
        {"input": {"maze": [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
                   "start": [0,0], "destination": [2,2]}, "expected": False},
    ],
    solution="""class Solution:
    def hasPath(self, maze, start, destination):
        # BFS over STOP POINTS (not individual cells). At each pop, try all 4
        # directions; for each, roll until we hit a wall or boundary, then enqueue
        # the resting position if unvisited. The key shift from a normal grid BFS
        # is that one BFS step covers an entire roll, not a single cell.
        from collections import deque
        m, n = len(maze), len(maze[0])
        dest = (destination[0], destination[1])
        visited = {(start[0], start[1])}
        queue = deque([(start[0], start[1])])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue:
            r, c = queue.popleft()
            if (r, c) == dest:
                return True
            for dr, dc in directions:
                # Roll until the NEXT step would hit a wall or boundary.
                nr, nc = r, c
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False
""",
    explanation="""**Approach: BFS over stop points**

**Time:** O(m * n * max(m, n)) — each cell is a stop at most once (m * n), and each roll from that stop traverses up to max(m, n) cells | **Space:** O(m * n) for the visited set + queue

**The mental model shift.** Normal grid BFS treats each cell as a state. Here, the rolling rule means a cell is only a *state* if the ball actually STOPS there. Passing through doesn't count. So:

- A "state" is a stop point (a cell where the ball came to rest because the next cell would have been a wall or boundary).
- A "transition" is a roll: pick a direction, slide all the way until forced to stop.

So a single BFS step covers an entire roll, not one cell. Visited is keyed on stop points, not on cells the ball passed through.

**The destination trap.** The problem says the ball must STOP at destination. A roll that *passes over* destination but stops elsewhere doesn't count as success. The clean way to enforce this: only check `(r, c) == dest` when you POP from the queue (i.e., a confirmed stop point) — never mid-roll.

**The rolling inner loop.** The condition `maze[nr + dr][nc + dc] == 0` peeks at the NEXT cell:

- If the next cell is a wall or out of bounds, we stop. `(nr, nc)` is the resting cell — which is still `0` (empty), because we only advanced into `0` cells.
- The loop terminates when we can't advance further. We do NOT include the wall cell in our stop position.

Off-by-one common bug: `while maze[nr][nc] == 0: nr += dr; nc += dc` — this advances past the wall and indexes out of bounds. Always peek before stepping.

**Why BFS over DFS?** Either works for this reachability problem. BFS gives you the fewest-rolls path "for free" if you wanted it (this is exactly #505 Maze II's setup but with cost instead of distance). DFS uses less memory.
"""
)
