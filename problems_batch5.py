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
<p>A <strong>trie</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.</p>
<p>Implement <code>Trie</code> with: <code>insert(word)</code>, <code>search(word)</code>, <code>startsWith(prefix)</code>.</p>
<h4>Example:</h4>
<pre>Input: ["Trie","insert","search","search","startsWith","insert","search"]
       [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
Output: [null, null, true, false, true, null, true]</pre>
<p><em>This problem is wrapped as a function: pass <code>operations</code> and <code>arguments</code> in parallel lists. <code>None</code> in the output marks void operations.</em></p>""",
    function_name="trieOps",
    template="""class Solution:
    def trieOps(self, operations: list[str], arguments: list[list]) -> list:
        # operations: ["Trie","insert","search","startsWith",...]
        # arguments: [[], ["apple"], ["apple"], ["app"], ...]
        pass
""",
    test_cases=[
        {"input": {"operations": ["Trie","insert","search","search","startsWith","insert","search"],
                   "arguments": [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]},
         "expected": [None, None, True, False, True, None, True]},
        {"input": {"operations": ["Trie","insert","search"], "arguments": [[],["a"],["a"]]},
         "expected": [None, None, True]},
        {"input": {"operations": ["Trie","search","startsWith"], "arguments": [[],["x"],["x"]]},
         "expected": [None, False, False]},
    ],
    solution="""class Solution:
    def trieOps(self, operations: list[str], arguments: list[list]) -> list:
        class Trie:
            def __init__(self):
                self.root = {}
            def insert(self, w):
                n = self.root
                for c in w:
                    n = n.setdefault(c, {})
                n['$'] = True
            def _find(self, w):
                n = self.root
                for c in w:
                    if c not in n: return None
                    n = n[c]
                return n
            def search(self, w):
                n = self._find(w)
                return bool(n and '$' in n)
            def startsWith(self, p):
                return self._find(p) is not None
        trie = None
        out = []
        for op, args in zip(operations, arguments):
            if op == 'Trie':
                trie = Trie(); out.append(None)
            elif op == 'insert':
                trie.insert(args[0]); out.append(None)
            elif op == 'search':
                out.append(trie.search(args[0]))
            elif op == 'startsWith':
                out.append(trie.startsWith(args[0]))
        return out
""",
    explanation="""**Approach: Nested Dictionaries**

**Time:** O(L) per op, where L = word length | **Space:** O(total characters inserted)

Each trie node is a dict mapping char -> child dict. A sentinel `'$'` marks the end of an inserted word so we can distinguish "is a word" from "is a prefix only".
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
