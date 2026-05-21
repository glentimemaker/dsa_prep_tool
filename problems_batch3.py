# Batch 3: Problems from frequency 37.5%

_register(75,
    description="""<h3>Sort Colors</h3>
<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong>in-place</strong> so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>
<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>
<p>You must solve this problem without using the library's sort function.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [2,0,1]
Output: [0,1,2]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 &le; n &le; 300</code></li>
<li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>""",
    function_name="sortColors",
    template="""class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        # Sort in-place and return the list
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,0,2,1,1,0]}, "expected": [0,0,1,1,2,2]},
        {"input": {"nums": [2,0,1]}, "expected": [0,1,2]},
        {"input": {"nums": [0]}, "expected": [0]},
        {"input": {"nums": [1,2,0]}, "expected": [0,1,2]},
        {"input": {"nums": [2,2,1,1,0,0]}, "expected": [0,0,1,1,2,2]},
    ],
    solution="""class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
""",
    explanation="""**Approach: Dutch National Flag Algorithm**

**Time:** O(n) | **Space:** O(1)

1. Maintain three pointers: `low` (boundary of 0s), `mid` (current element), `high` (boundary of 2s).
2. If `nums[mid] == 0`: swap with `low`, advance both `low` and `mid`.
3. If `nums[mid] == 1`: just advance `mid`.
4. If `nums[mid] == 2`: swap with `high`, decrement `high` (don't advance `mid` since swapped value needs inspection).

**Why this works:** The three pointers partition the array into four regions: [0..low-1] are 0s, [low..mid-1] are 1s, [mid..high] are unknown, [high+1..end] are 2s. Each step shrinks the unknown region by one.
"""
)

_register(83,
    description="""<h3>Remove Duplicates from Sorted List</h3>
<p>Given the <code>head</code> of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.</p>
<h4>Example 1:</h4>
<pre>Input: head = [1,1,2]
Output: [1,2]</pre>
<h4>Example 2:</h4>
<pre>Input: head = [1,1,2,3,3]
Output: [1,2,3]</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes is in the range <code>[0, 300]</code>.</li>
<li><code>-100 &le; Node.val &le; 100</code></li>
<li>The list is guaranteed to be sorted in ascending order.</li>
</ul>
<p><em>Note: For simplicity, inputs/outputs are represented as lists.</em></p>""",
    function_name="deleteDuplicates",
    template="""class Solution:
    def deleteDuplicates(self, head: list[int]) -> list[int]:
        # Input/output as lists for simplicity
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [1,1,2]}, "expected": [1,2]},
        {"input": {"head": [1,1,2,3,3]}, "expected": [1,2,3]},
        {"input": {"head": []}, "expected": []},
        {"input": {"head": [1]}, "expected": [1]},
        {"input": {"head": [1,1,1,1]}, "expected": [1]},
    ],
    solution="""class Solution:
    def deleteDuplicates(self, head: list[int]) -> list[int]:
        if not head:
            return []
        result = [head[0]]
        for val in head[1:]:
            if val != result[-1]:
                result.append(val)
        return result
""",
    explanation="""**Approach: Linear Scan**

**Time:** O(n) | **Space:** O(1) extra (O(n) for output)

1. Start with the first element in the result.
2. Iterate through the rest of the list.
3. Only add an element if it differs from the last element added to the result.

**Why this works:** Since the list is sorted, duplicates are adjacent. We just skip elements that match the previous one. In a real linked list, we would adjust the `next` pointers instead of creating a new list.
"""
)

_register(100,
    description="""<h3>Same Tree</h3>
<p>Given the roots of two binary trees <code>p</code> and <code>q</code>, write a function to check if they are the same or not.</p>
<p>Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.</p>
<h4>Example 1:</h4>
<pre>Input: p = [1,2,3], q = [1,2,3]
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: p = [1,2], q = [1,null,2]
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: p = [1,2,1], q = [1,1,2]
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in both trees is in the range <code>[0, 100]</code>.</li>
<li><code>-10<sup>4</sup> &le; Node.val &le; 10<sup>4</sup></code></li>
</ul>
<p><em>Note: Trees are represented as level-order lists, e.g. [1,2,3,null,null,4,5].</em></p>""",
    function_name="isSameTree",
    template="""class Solution:
    def isSameTree(self, p: list, q: list) -> bool:
        # Trees given as level-order lists, e.g. [1,2,3,null,null,4,5]
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"p": [1,2,3], "q": [1,2,3]}, "expected": True},
        {"input": {"p": [1,2], "q": [1,None,2]}, "expected": False},
        {"input": {"p": [1,2,1], "q": [1,1,2]}, "expected": False},
        {"input": {"p": [], "q": []}, "expected": True},
        {"input": {"p": [1], "q": [1]}, "expected": True},
    ],
    solution="""class Solution:
    def isSameTree(self, p: list, q: list) -> bool:
        # Normalize: remove trailing Nones for comparison
        def normalize(tree):
            if not tree:
                return []
            t = list(tree)
            while t and t[-1] is None:
                t.pop()
            return t
        return normalize(p) == normalize(q)
""",
    explanation="""**Approach: Level-Order List Comparison**

**Time:** O(n) | **Space:** O(n)

1. Normalize both tree lists by removing trailing `None` values.
2. Compare the normalized lists directly.

**Why this works:** Two binary trees represented as level-order lists are identical if and only if their normalized representations are equal. Trailing `None`s don't affect tree structure, so we strip them before comparing.
"""
)

_register(103,
    description="""<h3>Binary Tree Zigzag Level Order Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).</p>
<h4>Example 1:</h4>
<pre>Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]</pre>
<h4>Example 2:</h4>
<pre>Input: root = [1]
Output: [[1]]</pre>
<h4>Example 3:</h4>
<pre>Input: root = []
Output: []</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
<li><code>-100 &le; Node.val &le; 100</code></li>
</ul>
<p><em>Note: Tree is represented as a level-order list, e.g. [3,9,20,null,null,15,7].</em></p>""",
    function_name="zigzagLevelOrder",
    template="""class Solution:
    def zigzagLevelOrder(self, root: list) -> list[list[int]]:
        # Tree given as level-order list, e.g. [3,9,20,null,null,15,7]
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"root": [3,9,20,None,None,15,7]}, "expected": [[3],[20,9],[15,7]]},
        {"input": {"root": [1]}, "expected": [[1]]},
        {"input": {"root": []}, "expected": []},
        {"input": {"root": [1,2,3,4,5,6,7]}, "expected": [[1],[3,2],[4,5,6,7]]},
    ],
    solution="""class Solution:
    def zigzagLevelOrder(self, root: list) -> list[list[int]]:
        if not root:
            return []
        from collections import deque
        # Build tree from list
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
        def build_tree(lst):
            if not lst:
                return None
            root = TreeNode(lst[0])
            queue = deque([root])
            i = 1
            while queue and i < len(lst):
                node = queue.popleft()
                if i < len(lst) and lst[i] is not None:
                    node.left = TreeNode(lst[i])
                    queue.append(node.left)
                i += 1
                if i < len(lst) and lst[i] is not None:
                    node.right = TreeNode(lst[i])
                    queue.append(node.right)
                i += 1
            return root
        tree_root = build_tree(root)
        if not tree_root:
            return []
        result = []
        queue = deque([tree_root])
        left_to_right = True
        while queue:
            level_size = len(queue)
            level = deque()
            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(level))
            left_to_right = not left_to_right
        return result
""",
    explanation="""**Approach: BFS with Direction Toggle**

**Time:** O(n) | **Space:** O(n)

1. Build the binary tree from the level-order list representation.
2. Perform BFS (level-order traversal) using a queue.
3. For each level, use a deque to collect values: append right for left-to-right, appendleft for right-to-left.
4. Toggle direction after each level.

**Why this works:** Standard BFS processes nodes level by level. By using a deque and toggling whether we append or appendleft, we achieve the zigzag effect without any extra passes or reversals.
"""
)

_register(118,
    description="""<h3>Pascal's Triangle</h3>
<p>Given an integer <code>numRows</code>, return the first <code>numRows</code> of Pascal's triangle.</p>
<p>In Pascal's triangle, each number is the sum of the two numbers directly above it.</p>
<h4>Example 1:</h4>
<pre>Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]</pre>
<h4>Example 2:</h4>
<pre>Input: numRows = 1
Output: [[1]]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; numRows &le; 30</code></li>
</ul>""",
    function_name="generate",
    template="""class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"numRows": 5}, "expected": [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]},
        {"input": {"numRows": 1}, "expected": [[1]]},
        {"input": {"numRows": 2}, "expected": [[1],[1,1]]},
        {"input": {"numRows": 3}, "expected": [[1],[1,1],[1,2,1]]},
    ],
    solution="""class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
""",
    explanation="""**Approach: Dynamic Programming (Row by Row)**

**Time:** O(numRows^2) | **Space:** O(numRows^2)

1. Initialize each row with all 1s.
2. For interior elements (not first or last), compute the value as the sum of the two elements above it from the previous row.
3. Append each completed row to the triangle.

**Why this works:** Pascal's triangle is defined by the recurrence `C(n,k) = C(n-1,k-1) + C(n-1,k)`. We build it row by row, using the previous row to compute the current one.
"""
)

_register(122,
    description="""<h3>Best Time to Buy and Sell Stock II</h3>
<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>
<p>On each day, you may decide to buy and/or sell the stock. You can only hold at most one share at a time. However, you can buy and immediately sell on the same day.</p>
<p>Find and return the <strong>maximum profit</strong> you can achieve.</p>
<h4>Example 1:</h4>
<pre>Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price=1), sell on day 3 (price=5), profit=4.
Then buy on day 4 (price=3), sell on day 5 (price=6), profit=3.
Total profit = 4 + 3 = 7.</pre>
<h4>Example 2:</h4>
<pre>Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1, sell on day 5, profit = 4.</pre>
<h4>Example 3:</h4>
<pre>Input: prices = [7,6,4,3,1]
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; prices.length &le; 3 * 10<sup>4</sup></code></li>
<li><code>0 &le; prices[i] &le; 10<sup>4</sup></code></li>
</ul>""",
    function_name="maxProfit",
    template="""class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"prices": [7,1,5,3,6,4]}, "expected": 7},
        {"input": {"prices": [1,2,3,4,5]}, "expected": 4},
        {"input": {"prices": [7,6,4,3,1]}, "expected": 0},
        {"input": {"prices": [2,4,1]}, "expected": 2},
    ],
    solution="""class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
""",
    explanation="""**Approach: Greedy (Collect All Upswings)**

**Time:** O(n) | **Space:** O(1)

1. Iterate through prices starting from day 2.
2. Whenever today's price is higher than yesterday's, add the difference to profit.
3. This is equivalent to buying at every local minimum and selling at every local maximum.

**Why this works:** Since we can make unlimited transactions, the optimal strategy is to capture every positive price difference. The sum of all positive consecutive differences equals the maximum profit.
"""
)

_register(127,
    description="""<h3>Word Ladder</h3>
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -&gt; s1 -&gt; s2 -&gt; ... -&gt; sk</code> such that:</p>
<ul>
<li>Every adjacent pair of words differs by a single letter.</li>
<li>Every <code>si</code> for <code>1 &le; i &le; k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
<li><code>sk == endWord</code></li>
</ul>
<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return the <strong>number of words</strong> in the shortest transformation sequence, or <code>0</code> if no such sequence exists.</p>
<h4>Example 1:</h4>
<pre>Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: hit -> hot -> dot -> dog -> cog</pre>
<h4>Example 2:</h4>
<pre>Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: endWord "cog" is not in wordList.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; beginWord.length &le; 10</code></li>
<li><code>endWord.length == beginWord.length</code></li>
<li><code>1 &le; wordList.length &le; 5000</code></li>
<li>All words have the same length and consist of lowercase English letters.</li>
</ul>""",
    function_name="ladderLength",
    template="""class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"beginWord": "hit", "endWord": "cog", "wordList": ["hot","dot","dog","lot","log","cog"]}, "expected": 5},
        {"input": {"beginWord": "hit", "endWord": "cog", "wordList": ["hot","dot","dog","lot","log"]}, "expected": 0},
        {"input": {"beginWord": "a", "endWord": "c", "wordList": ["a","b","c"]}, "expected": 2},
        {"input": {"beginWord": "hot", "endWord": "dog", "wordList": ["hot","dog"]}, "expected": 0},
    ],
    solution="""class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        from collections import deque, defaultdict
        if endWord not in wordList:
            return 0
        word_set = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word == endWord:
                        return length + 1
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))
        return 0
""",
    explanation="""**Approach: BFS (Breadth-First Search)**

**Time:** O(M^2 * N) where M is word length, N is wordList size | **Space:** O(M * N)

1. Start BFS from `beginWord` with distance 1.
2. For each word, try changing each character to every letter a-z.
3. If the new word is in the word list and unvisited, add it to the queue.
4. If we reach `endWord`, return the current distance + 1.
5. If the queue empties, return 0 (no path).

**Why this works:** BFS guarantees the shortest path in an unweighted graph. Each word is a node, and edges connect words that differ by one letter. BFS finds the shortest transformation sequence.
"""
)

_register(130,
    description="""<h3>Surrounded Regions</h3>
<p>Given an <code>m x n</code> matrix <code>board</code> containing <code>'X'</code> and <code>'O'</code>, capture all regions that are 4-directionally surrounded by <code>'X'</code>.</p>
<p>A region is captured by flipping all <code>'O'</code>s into <code>'X'</code>s in that surrounded region.</p>
<h4>Example 1:</h4>
<pre>Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: The bottom 'O' is on the border, so it is not surrounded and not flipped.</pre>
<h4>Example 2:</h4>
<pre>Input: board = [["X"]]
Output: [["X"]]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>m == board.length</code></li>
<li><code>n == board[i].length</code></li>
<li><code>1 &le; m, n &le; 200</code></li>
<li><code>board[i][j]</code> is <code>'X'</code> or <code>'O'</code>.</li>
</ul>""",
    function_name="solve",
    template="""class Solution:
    def solve(self, board: list[list[str]]) -> list[list[str]]:
        # Modify board in-place and return it
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"board": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]},
         "expected": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]},
        {"input": {"board": [["X"]]}, "expected": [["X"]]},
        {"input": {"board": [["O","O"],["O","O"]]}, "expected": [["O","O"],["O","O"]]},
        {"input": {"board": [["X","O","X"],["O","X","O"],["X","O","X"]]},
         "expected": [["X","O","X"],["O","X","O"],["X","O","X"]]},
    ],
    solution="""class Solution:
    def solve(self, board: list[list[str]]) -> list[list[str]]:
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # Safe, connected to border
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        # Mark all 'O's connected to border as safe
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)
        # Flip: 'O' -> 'X' (surrounded), 'S' -> 'O' (safe)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        return board
""",
    explanation="""**Approach: DFS from Border**

**Time:** O(m*n) | **Space:** O(m*n) recursion stack

1. Start DFS from all border 'O' cells, marking them as 'S' (safe/connected to border).
2. After DFS, any remaining 'O' is surrounded — flip it to 'X'.
3. Restore 'S' cells back to 'O'.

**Why this works:** Instead of checking if each 'O' region is surrounded (complex), we flip the logic: find all 'O's that are NOT surrounded (connected to border) and protect them. Everything else gets captured.
"""
)

_register(135,
    description="""<h3>Candy</h3>
<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>
<p>You are giving candies to these children subjected to the following requirements:</p>
<ul>
<li>Each child must have at least one candy.</li>
<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>
<p>Return the minimum number of candies you need to have to distribute the candies to the children.</p>
<h4>Example 1:</h4>
<pre>Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate [2,1,2] candies.</pre>
<h4>Example 2:</h4>
<pre>Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate [1,2,1] candies. The third child gets 1 candy because it satisfies the conditions.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == ratings.length</code></li>
<li><code>1 &le; n &le; 2 * 10<sup>4</sup></code></li>
<li><code>0 &le; ratings[i] &le; 2 * 10<sup>4</sup></code></li>
</ul>""",
    function_name="candy",
    template="""class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"ratings": [1,0,2]}, "expected": 5},
        {"input": {"ratings": [1,2,2]}, "expected": 4},
        {"input": {"ratings": [1,3,2,2,1]}, "expected": 7},
        {"input": {"ratings": [1]}, "expected": 1},
        {"input": {"ratings": [1,2,3,4,5]}, "expected": 15},
    ],
    solution="""class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        # Left to right: if rating is higher than left neighbor, give more
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # Right to left: if rating is higher than right neighbor, ensure more
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)
""",
    explanation="""**Approach: Two-Pass Greedy**

**Time:** O(n) | **Space:** O(n)

1. Initialize every child with 1 candy.
2. Left-to-right pass: if a child has a higher rating than the left neighbor, give them one more candy than that neighbor.
3. Right-to-left pass: if a child has a higher rating than the right neighbor, ensure they have at least one more candy than that neighbor.
4. Sum all candies.

**Why this works:** The two passes handle both directions independently. The left pass ensures the left-neighbor constraint, and the right pass ensures the right-neighbor constraint. Taking the max at each position satisfies both simultaneously.
"""
)

_register(137,
    description="""<h3>Single Number II</h3>
<p>Given an integer array <code>nums</code> where every element appears <strong>three times</strong> except for one, which appears <strong>exactly once</strong>. Find the single element and return it.</p>
<p>You must implement a solution with a linear runtime complexity and use only constant extra space.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,2,3,2]
Output: 3</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1,0,1,0,1,99]
Output: 99</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; nums.length &le; 3 * 10<sup>4</sup></code></li>
<li><code>-2<sup>31</sup> &le; nums[i] &le; 2<sup>31</sup> - 1</code></li>
<li>Each element appears exactly three times except for one element which appears once.</li>
</ul>""",
    function_name="singleNumber",
    template="""class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,2,3,2]}, "expected": 3},
        {"input": {"nums": [0,1,0,1,0,1,99]}, "expected": 99},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [5,5,5,7]}, "expected": 7},
        {"input": {"nums": [-2,-2,1,1,4,1,4,4,-1,-2]}, "expected": -1},
    ],
    solution="""class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
""",
    explanation="""**Approach: Bitwise State Machine**

**Time:** O(n) | **Space:** O(1)

1. Use two variables `ones` and `twos` to track bits that have appeared 1 and 2 times respectively.
2. For each number:
   - XOR with `ones`, then mask out bits in `twos` (bits appearing for the 1st or 4th time go into `ones`).
   - XOR with `twos`, then mask out bits in `ones` (bits appearing for the 2nd time go into `twos`).
3. When a bit appears 3 times, it's automatically cleared from both `ones` and `twos`.
4. The single number's bits remain in `ones`.

**Why this works:** The two variables simulate a counter modulo 3 for each bit position. After processing all numbers, bits that appeared 3k times are cleared, leaving only the single number's bits in `ones`.
"""
)

_register(139,
    description="""<h3>Word Break</h3>
<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>
<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>
<h4>Example 1:</h4>
<pre>Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".</pre>
<h4>Example 2:</h4>
<pre>Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true</pre>
<h4>Example 3:</h4>
<pre>Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; s.length &le; 300</code></li>
<li><code>1 &le; wordDict.length &le; 1000</code></li>
<li><code>1 &le; wordDict[i].length &le; 20</code></li>
</ul>""",
    function_name="wordBreak",
    template="""class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "leetcode", "wordDict": ["leet","code"]}, "expected": True},
        {"input": {"s": "applepenapple", "wordDict": ["apple","pen"]}, "expected": True},
        {"input": {"s": "catsandog", "wordDict": ["cats","dog","sand","and","cat"]}, "expected": False},
        {"input": {"s": "a", "wordDict": ["a"]}, "expected": True},
        {"input": {"s": "ab", "wordDict": ["a"]}, "expected": False},
    ],
    solution="""class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
""",
    explanation="""**Approach: Dynamic Programming**

**Time:** O(n^2 * m) where m is average word length | **Space:** O(n)

1. Create a DP array where `dp[i]` means `s[0:i]` can be segmented.
2. `dp[0] = True` (empty string is valid).
3. For each position `i`, check all possible previous positions `j`: if `dp[j]` is True and `s[j:i]` is in the dictionary, then `dp[i] = True`.
4. Return `dp[n]`.

**Why this works:** We build up from smaller subproblems. If we can segment `s[0:j]` and `s[j:i]` is a dictionary word, then we can segment `s[0:i]`. This considers all possible word boundaries.
"""
)

_register(141,
    description="""<h3>Linked List Cycle</h3>
<p>Given <code>head</code>, the head of a linked list, determine if the linked list has a cycle in it.</p>
<p>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the <code>next</code> pointer.</p>
<p>Return <code>true</code> if there is a cycle, otherwise return <code>false</code>.</p>
<h4>Example 1:</h4>
<pre>Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle, where the tail connects to the 1st node (0-indexed).</pre>
<h4>Example 2:</h4>
<pre>Input: head = [1,2], pos = 0
Output: true</pre>
<h4>Example 3:</h4>
<pre>Input: head = [1], pos = -1
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li>The number of nodes is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
<li><code>pos</code> is <code>-1</code> or a valid index in the linked list.</li>
</ul>
<p><em>Note: For simplicity, input is a list and a position. pos = -1 means no cycle.</em></p>""",
    function_name="hasCycle",
    template="""class Solution:
    def hasCycle(self, head: list[int], pos: int) -> bool:
        # head is the list of values, pos is the cycle position (-1 if no cycle)
        # Return True if there is a cycle, False otherwise
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"head": [3,2,0,-4], "pos": 1}, "expected": True},
        {"input": {"head": [1,2], "pos": 0}, "expected": True},
        {"input": {"head": [1], "pos": -1}, "expected": False},
        {"input": {"head": [], "pos": -1}, "expected": False},
        {"input": {"head": [1,2,3,4], "pos": -1}, "expected": False},
    ],
    solution="""class Solution:
    def hasCycle(self, head: list[int], pos: int) -> bool:
        # With list representation, just check if pos >= 0
        # In a real linked list, you'd use Floyd's cycle detection:
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False
        return pos >= 0
""",
    explanation="""**Approach: Floyd's Cycle Detection (Tortoise and Hare)**

**Time:** O(n) | **Space:** O(1)

1. Use two pointers: `slow` moves one step at a time, `fast` moves two steps.
2. If there is a cycle, the fast pointer will eventually meet the slow pointer.
3. If the fast pointer reaches the end (null), there is no cycle.

```
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

**Why this works:** In a cycle, the fast pointer gains one position per step on the slow pointer. Eventually, the gap closes and they meet. Without a cycle, fast reaches the end first.
"""
)

_register(152,
    description="""<h3>Maximum Product Subarray</h3>
<p>Given an integer array <code>nums</code>, find a subarray that has the largest product, and return the product.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; nums.length &le; 2 * 10<sup>4</sup></code></li>
<li><code>-10 &le; nums[i] &le; 10</code></li>
</ul>""",
    function_name="maxProduct",
    template="""class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [2,3,-2,4]}, "expected": 6},
        {"input": {"nums": [-2,0,-1]}, "expected": 0},
        {"input": {"nums": [-2]}, "expected": -2},
        {"input": {"nums": [-2,3,-4]}, "expected": 24},
        {"input": {"nums": [0,2]}, "expected": 2},
    ],
    solution="""class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = nums[0]
        cur_max = cur_min = 1
        for num in nums:
            candidates = (num, cur_max * num, cur_min * num)
            cur_max = max(candidates)
            cur_min = min(candidates)
            result = max(result, cur_max)
        return result
""",
    explanation="""**Approach: Track Min and Max Products**

**Time:** O(n) | **Space:** O(1)

1. Track both the current maximum and minimum product ending at each position.
2. We need the minimum because a negative number times a large negative gives a large positive.
3. At each step, the new max/min is the max/min of: the number itself, number * previous max, number * previous min.
4. Track the global maximum.

**Why this works:** A negative number flips the sign, so yesterday's minimum can become today's maximum. By tracking both extremes, we handle all cases: positive streaks, negative*negative = positive, and zeros resetting the subarray.
"""
)

_register(153,
    description="""<h3>Find Minimum in Rotated Sorted Array</h3>
<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return the minimum element.</p>
<p>You must write an algorithm that runs in <code>O(log n)</code> time.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [4,5,6,7,0,1,2]
Output: 0</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [11,13,15,17]
Output: 11</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 &le; n &le; 5000</code></li>
<li>All integers are <strong>unique</strong>.</li>
</ul>""",
    function_name="findMin",
    template="""class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3,4,5,1,2]}, "expected": 1},
        {"input": {"nums": [4,5,6,7,0,1,2]}, "expected": 0},
        {"input": {"nums": [11,13,15,17]}, "expected": 11},
        {"input": {"nums": [2,1]}, "expected": 1},
        {"input": {"nums": [1]}, "expected": 1},
    ],
    solution="""class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
""",
    explanation="""**Approach: Binary Search**

**Time:** O(log n) | **Space:** O(1)

1. Use binary search with `left` and `right` pointers.
2. If `nums[mid] > nums[right]`, the minimum is in the right half (rotation point is to the right), so move `left = mid + 1`.
3. Otherwise, the minimum is at `mid` or to the left, so move `right = mid`.
4. When `left == right`, we've found the minimum.

**Why this works:** In a rotated sorted array, the minimum is at the rotation point. By comparing mid with right, we can determine which half contains the rotation point and binary search towards it.
"""
)

_register(179,
    description="""<h3>Largest Number</h3>
<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it.</p>
<p>Since the result may be very large, you need to return a string instead of an integer.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [10,2]
Output: "210"</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,30,34,5,9]
Output: "9534330"</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; nums.length &le; 100</code></li>
<li><code>0 &le; nums[i] &le; 10<sup>9</sup></code></li>
</ul>""",
    function_name="largestNumber",
    template="""class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [10,2]}, "expected": "210"},
        {"input": {"nums": [3,30,34,5,9]}, "expected": "9534330"},
        {"input": {"nums": [1]}, "expected": "1"},
        {"input": {"nums": [0,0]}, "expected": "0"},
        {"input": {"nums": [10,2,9,39,17]}, "expected": "93921710"},
    ],
    solution="""class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        from functools import cmp_to_key
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
        strs = [str(n) for n in nums]
        strs.sort(key=cmp_to_key(compare))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result
""",
    explanation="""**Approach: Custom Sort with Comparator**

**Time:** O(n log n) | **Space:** O(n)

1. Convert all numbers to strings.
2. Sort with a custom comparator: compare `a+b` vs `b+a` (string concatenation).
3. If `a+b > b+a`, then `a` should come before `b`.
4. Join the sorted strings. Handle the edge case of all zeros.

**Why this works:** The comparator `a+b > b+a` determines the optimal relative ordering of any two numbers. For example, "9" vs "34": "934" > "349", so "9" comes first. This gives a total ordering that produces the largest possible number.
"""
)

# 181: SQL problem, skipped

_register(205,
    description="""<h3>Isomorphic Strings</h3>
<p>Given two strings <code>s</code> and <code>t</code>, determine if they are isomorphic.</p>
<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>
<p>All occurrences of a character must be replaced with another character while preserving the order. No two characters may map to the same character, but a character may map to itself.</p>
<h4>Example 1:</h4>
<pre>Input: s = "egg", t = "add"
Output: true</pre>
<h4>Example 2:</h4>
<pre>Input: s = "foo", t = "bar"
Output: false</pre>
<h4>Example 3:</h4>
<pre>Input: s = "paper", t = "title"
Output: true</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; s.length &le; 5 * 10<sup>4</sup></code></li>
<li><code>t.length == s.length</code></li>
<li><code>s</code> and <code>t</code> consist of any valid ASCII character.</li>
</ul>""",
    function_name="isIsomorphic",
    template="""class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "egg", "t": "add"}, "expected": True},
        {"input": {"s": "foo", "t": "bar"}, "expected": False},
        {"input": {"s": "paper", "t": "title"}, "expected": True},
        {"input": {"s": "ab", "t": "aa"}, "expected": False},
        {"input": {"s": "a", "t": "a"}, "expected": True},
    ],
    solution="""class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:
                if ct in t_to_s:
                    return False
                s_to_t[cs] = ct
                t_to_s[ct] = cs
        return True
""",
    explanation="""**Approach: Two Hash Maps (Bidirectional Mapping)**

**Time:** O(n) | **Space:** O(1) since character set is bounded

1. Maintain two mappings: `s_to_t` and `t_to_s`.
2. For each character pair `(cs, ct)`:
   - If `cs` is already mapped, check it maps to `ct`.
   - If `cs` is new, check `ct` isn't already mapped to a different character.
   - If both checks pass, add the mapping.
3. If all pairs are consistent, the strings are isomorphic.

**Why this works:** Isomorphism requires a one-to-one mapping. The two maps enforce that no two characters in `s` map to the same character in `t` (and vice versa).
"""
)

_register(207,
    description="""<h3>Course Schedule</h3>
<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you must take course <code>b<sub>i</sub></code> before course <code>a<sub>i</sub></code>.</p>
<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>
<h4>Example 1:</h4>
<pre>Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0, then course 1.</pre>
<h4>Example 2:</h4>
<pre>Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Course 0 requires course 1 and vice versa — a cycle.</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; numCourses &le; 2000</code></li>
<li><code>0 &le; prerequisites.length &le; 5000</code></li>
<li><code>prerequisites[i].length == 2</code></li>
</ul>""",
    function_name="canFinish",
    template="""class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"numCourses": 2, "prerequisites": [[1,0]]}, "expected": True},
        {"input": {"numCourses": 2, "prerequisites": [[1,0],[0,1]]}, "expected": False},
        {"input": {"numCourses": 3, "prerequisites": [[1,0],[2,1]]}, "expected": True},
        {"input": {"numCourses": 1, "prerequisites": []}, "expected": True},
        {"input": {"numCourses": 4, "prerequisites": [[1,0],[2,1],[3,2],[1,3]]}, "expected": False},
    ],
    solution="""class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses
""",
    explanation="""**Approach: Topological Sort (Kahn's Algorithm / BFS)**

**Time:** O(V + E) | **Space:** O(V + E)

1. Build an adjacency list and compute in-degrees for each course.
2. Add all courses with in-degree 0 to a queue (no prerequisites).
3. Process each course: decrement in-degrees of its dependents.
4. If a dependent's in-degree becomes 0, add it to the queue.
5. If we processed all courses (`count == numCourses`), there's no cycle.

**Why this works:** Kahn's algorithm peels off nodes with no incoming edges layer by layer. If a cycle exists, the nodes in the cycle never reach in-degree 0, so we can't process all courses.
"""
)

_register(209,
    description="""<h3>Minimum Size Subarray Sum</h3>
<p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return the <strong>minimal length</strong> of a subarray whose sum is greater than or equal to <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>
<h4>Example 1:</h4>
<pre>Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the constraint.</pre>
<h4>Example 2:</h4>
<pre>Input: target = 4, nums = [1,4,4]
Output: 1</pre>
<h4>Example 3:</h4>
<pre>Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; target &le; 10<sup>9</sup></code></li>
<li><code>1 &le; nums.length &le; 10<sup>5</sup></code></li>
<li><code>1 &le; nums[i] &le; 10<sup>4</sup></code></li>
</ul>""",
    function_name="minSubArrayLen",
    template="""class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"target": 7, "nums": [2,3,1,2,4,3]}, "expected": 2},
        {"input": {"target": 4, "nums": [1,4,4]}, "expected": 1},
        {"input": {"target": 11, "nums": [1,1,1,1,1,1,1,1]}, "expected": 0},
        {"input": {"target": 15, "nums": [5,1,3,5,10,7,4,9,2,8]}, "expected": 2},
        {"input": {"target": 3, "nums": [1,1,1,1]}, "expected": 3},
    ],
    solution="""class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = float('inf')
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
""",
    explanation="""**Approach: Sliding Window**

**Time:** O(n) | **Space:** O(1)

1. Expand the window by moving `right` and adding `nums[right]` to the sum.
2. When the sum reaches the target, try shrinking from the left to find the minimum length.
3. Keep shrinking while the sum is still >= target.
4. Track the minimum window length.

**Why this works:** Since all numbers are positive, expanding the window always increases the sum and shrinking always decreases it. This monotonic property allows the sliding window to find the optimal subarray in linear time.
"""
)

_register(210,
    description="""<h3>Course Schedule II</h3>
<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you must take course <code>b<sub>i</sub></code> before course <code>a<sub>i</sub></code>.</p>
<p>Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible, return an empty array.</p>
<h4>Example 1:</h4>
<pre>Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]</pre>
<h4>Example 2:</h4>
<pre>Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]</pre>
<h4>Example 3:</h4>
<pre>Input: numCourses = 1, prerequisites = []
Output: [0]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; numCourses &le; 2000</code></li>
<li><code>0 &le; prerequisites.length &le; numCourses * (numCourses - 1)</code></li>
</ul>""",
    function_name="findOrder",
    template="""class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"numCourses": 2, "prerequisites": [[1,0]]}, "expected": [0,1]},
        {"input": {"numCourses": 4, "prerequisites": [[1,0],[2,0],[3,1],[3,2]]}, "expected": [[0,1,2,3],[0,2,1,3]]},
        {"input": {"numCourses": 1, "prerequisites": []}, "expected": [0]},
        {"input": {"numCourses": 2, "prerequisites": [[1,0],[0,1]]}, "expected": []},
        {"input": {"numCourses": 3, "prerequisites": []}, "expected": [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]},
    ],
    solution="""class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
""",
    explanation="""**Approach: Topological Sort (Kahn's Algorithm / BFS)**

**Time:** O(V + E) | **Space:** O(V + E)

1. Build adjacency list and compute in-degrees.
2. Start with courses having in-degree 0 (no prerequisites).
3. Process each course: add to result, decrement dependents' in-degrees.
4. If a dependent reaches in-degree 0, add to queue.
5. If result contains all courses, return it; otherwise return [] (cycle detected).

**Why this works:** Same as Course Schedule, but we record the processing order. Kahn's algorithm naturally produces a valid topological ordering. If a cycle exists, some nodes never reach in-degree 0 and we return an empty list.
"""
)

_register(221,
    description="""<h3>Maximal Square</h3>
<p>Given an <code>m x n</code> binary <code>matrix</code> filled with <code>'0'</code>s and <code>'1'</code>s, find the largest square containing only <code>'1'</code>s and return its area.</p>
<h4>Example 1:</h4>
<pre>Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4</pre>
<h4>Example 2:</h4>
<pre>Input: matrix = [["0","1"],["1","0"]]
Output: 1</pre>
<h4>Example 3:</h4>
<pre>Input: matrix = [["0"]]
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 &le; m, n &le; 300</code></li>
<li><code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>""",
    function_name="maximalSquare",
    template="""class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"matrix": [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]}, "expected": 4},
        {"input": {"matrix": [["0","1"],["1","0"]]}, "expected": 1},
        {"input": {"matrix": [["0"]]}, "expected": 0},
        {"input": {"matrix": [["1","1"],["1","1"]]}, "expected": 4},
        {"input": {"matrix": [["1"]]}, "expected": 1},
    ],
    solution="""class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
""",
    explanation="""**Approach: Dynamic Programming**

**Time:** O(m*n) | **Space:** O(m*n)

1. Create a DP table where `dp[i][j]` represents the side length of the largest square with bottom-right corner at `(i-1, j-1)`.
2. If `matrix[i-1][j-1] == '1'`, then `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.
3. Track the maximum side length.
4. Return `max_side^2` (the area).

**Why this works:** A square of side `k` at position `(i,j)` exists only if there are squares of side `k-1` at the top, left, and top-left positions. The minimum of these three determines how large the current square can be.
"""
)

_register(224,
    description="""<h3>Basic Calculator</h3>
<p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return the result.</p>
<p><strong>Note:</strong> You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>
<h4>Example 1:</h4>
<pre>Input: s = "1 + 1"
Output: 2</pre>
<h4>Example 2:</h4>
<pre>Input: s = " 2-1 + 2 "
Output: 3</pre>
<h4>Example 3:</h4>
<pre>Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; s.length &le; 3 * 10<sup>5</sup></code></li>
<li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li>
<li><code>s</code> represents a valid expression.</li>
</ul>""",
    function_name="calculate",
    template="""class Solution:
    def calculate(self, s: str) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "1 + 1"}, "expected": 2},
        {"input": {"s": " 2-1 + 2 "}, "expected": 3},
        {"input": {"s": "(1+(4+5+2)-3)+(6+8)"}, "expected": 23},
        {"input": {"s": "2147483647"}, "expected": 2147483647},
        {"input": {"s": "1-(     -2)"}, "expected": 3},
    ],
    solution="""class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  # sign before parenthesis
                result += stack.pop()  # result before parenthesis
        result += sign * num
        return result
""",
    explanation="""**Approach: Stack for Parentheses**

**Time:** O(n) | **Space:** O(n)

1. Use a stack to handle parentheses. Track `result`, `num`, and `sign`.
2. When we see a digit, build the number.
3. When we see `+` or `-`, add the current number to result and update sign.
4. When we see `(`, push current result and sign onto the stack, reset for the sub-expression.
5. When we see `)`, finalize the sub-expression, pop the sign and previous result, combine.

**Why this works:** Parentheses create nested sub-expressions. The stack saves the state before each `(` so we can restore it after `)`. The sign before `(` determines whether the sub-expression is added or subtracted.
"""
)

_register(231,
    description="""<h3>Power of Two</h3>
<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of two. Otherwise, return <code>false</code>.</p>
<p>An integer <code>n</code> is a power of two if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>
<h4>Example 1:</h4>
<pre>Input: n = 1
Output: true
Explanation: 2^0 = 1</pre>
<h4>Example 2:</h4>
<pre>Input: n = 16
Output: true
Explanation: 2^4 = 16</pre>
<h4>Example 3:</h4>
<pre>Input: n = 3
Output: false</pre>
<h4>Constraints:</h4>
<ul>
<li><code>-2<sup>31</sup> &le; n &le; 2<sup>31</sup> - 1</code></li>
</ul>""",
    function_name="isPowerOfTwo",
    template="""class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 1}, "expected": True},
        {"input": {"n": 16}, "expected": True},
        {"input": {"n": 3}, "expected": False},
        {"input": {"n": 0}, "expected": False},
        {"input": {"n": -1}, "expected": False},
    ],
    solution="""class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
""",
    explanation="""**Approach: Bit Manipulation**

**Time:** O(1) | **Space:** O(1)

1. A power of two in binary has exactly one bit set: `1, 10, 100, 1000, ...`
2. `n - 1` flips all bits from the rightmost set bit downward: e.g., `1000` -> `0111`.
3. `n & (n - 1)` clears the lowest set bit. For a power of two, this results in 0.
4. Also check `n > 0` since 0 and negative numbers aren't powers of two.

**Why this works:** The expression `n & (n - 1) == 0` is true only when `n` has exactly one set bit, which is the definition of a power of two (for positive integers).
"""
)

_register(239,
    description="""<h3>Sliding Window Maximum</h3>
<p>You are given an array of integers <code>nums</code> and an integer <code>k</code> (sliding window size). Return the max value in each sliding window as it moves from left to right.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
[1  3  -1] -3  5  3  6  7      3
 1 [3  -1  -3] 5  3  6  7      3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7      5
 1  3  -1  -3 [5  3  6] 7      6
 1  3  -1  -3  5 [3  6  7]     7</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [1], k = 1
Output: [1]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; nums.length &le; 10<sup>5</sup></code></li>
<li><code>-10<sup>4</sup> &le; nums[i] &le; 10<sup>4</sup></code></li>
<li><code>1 &le; k &le; nums.length</code></li>
</ul>""",
    function_name="maxSlidingWindow",
    template="""class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,3,-1,-3,5,3,6,7], "k": 3}, "expected": [3,3,5,5,6,7]},
        {"input": {"nums": [1], "k": 1}, "expected": [1]},
        {"input": {"nums": [1,-1], "k": 1}, "expected": [1,-1]},
        {"input": {"nums": [9,11], "k": 2}, "expected": [11]},
        {"input": {"nums": [4,-2], "k": 2}, "expected": [4]},
    ],
    solution="""class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque
        dq = deque()  # stores indices
        result = []
        for i in range(len(nums)):
            # Remove indices outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            # Window is fully formed
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
""",
    explanation="""**Approach: Monotonic Deque**

**Time:** O(n) | **Space:** O(k)

1. Maintain a deque of indices in decreasing order of their values.
2. For each element:
   - Remove indices outside the current window from the front.
   - Remove indices of smaller elements from the back (they'll never be the max).
   - Add the current index.
3. The front of the deque is always the index of the maximum in the current window.

**Why this works:** The deque maintains a decreasing sequence of "candidates" for the maximum. When a larger element arrives, all smaller elements in the deque can never be the answer, so we remove them. This gives O(1) amortized time per element.
"""
)

_register(249,
    description="""<h3>Group Shifted Strings</h3>
<p>We can shift a string by shifting each of its letters to its successive letter. For example, <code>"abc"</code> can be shifted to be <code>"bcd"</code>.</p>
<p>We can keep shifting to form a sequence: <code>"abc" -&gt; "bcd" -&gt; ... -&gt; "xyz"</code>.</p>
<p>Given an array of strings <code>strings</code>, group all strings that belong to the same shifting sequence. You can return the answer in any order.</p>
<h4>Example 1:</h4>
<pre>Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]</pre>
<h4>Example 2:</h4>
<pre>Input: strings = ["a"]
Output: [["a"]]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; strings.length &le; 200</code></li>
<li><code>1 &le; strings[i].length &le; 50</code></li>
<li><code>strings[i]</code> consists of lowercase English letters.</li>
</ul>""",
    function_name="groupStrings",
    template="""class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"strings": ["abc","bcd","acef","xyz","az","ba","a","z"]},
         "expected": [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]},
        {"input": {"strings": ["a"]}, "expected": [["a"]]},
        {"input": {"strings": ["aa","bb"]}, "expected": [["aa","bb"]]},
        {"input": {"strings": ["ab","cd","ef"]}, "expected": [["ab","cd","ef"]]},
    ],
    solution="""class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            groups[key].append(s)
        return list(groups.values())
""",
    explanation="""**Approach: Hash by Shift Pattern**

**Time:** O(n * k) where k is average string length | **Space:** O(n * k)

1. For each string, compute a "shift key": the difference of each character from the first character, modulo 26.
2. For example, "abc" -> (0, 1, 2) and "bcd" -> (0, 1, 2) — same key!
3. "az" -> (0, 25) and "ba" -> (0, 25) — same key!
4. Group strings with the same key.

**Why this works:** Two strings belong to the same shift sequence if and only if the relative differences between consecutive characters are the same. Using the first character as a reference point normalizes all strings in the same group to the same key.
"""
)

_register(268,
    description="""<h3>Missing Number</h3>
<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return the only number in the range that is missing from the array.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [3,0,1]
Output: 2</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1]
Output: 2</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8</pre>
<h4>Constraints:</h4>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 &le; n &le; 10<sup>4</sup></code></li>
<li><code>0 &le; nums[i] &le; n</code></li>
<li>All numbers are <strong>unique</strong>.</li>
</ul>""",
    function_name="missingNumber",
    template="""class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [3,0,1]}, "expected": 2},
        {"input": {"nums": [0,1]}, "expected": 2},
        {"input": {"nums": [9,6,4,2,3,5,7,0,1]}, "expected": 8},
        {"input": {"nums": [0]}, "expected": 1},
        {"input": {"nums": [1]}, "expected": 0},
    ],
    solution="""class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
""",
    explanation="""**Approach: Math (Gauss Formula)**

**Time:** O(n) | **Space:** O(1)

1. The sum of numbers from 0 to n is `n * (n + 1) / 2`.
2. Subtract the actual sum of the array.
3. The difference is the missing number.

**Why this works:** If no number were missing, the sum would equal the Gauss formula. The deficit equals exactly the missing number. An alternative approach uses XOR: `xor(0..n) ^ xor(nums)`.
"""
)

_register(278,
    description="""<h3>First Bad Version</h3>
<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>
<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>
<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>
<h4>Example 1:</h4>
<pre>Input: n = 5, bad = 4
Output: 4
Explanation: isBadVersion(3) -> false, isBadVersion(5) -> true, isBadVersion(4) -> true.
So 4 is the first bad version.</pre>
<h4>Example 2:</h4>
<pre>Input: n = 1, bad = 1
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; bad &le; n &le; 2<sup>31</sup> - 1</code></li>
</ul>""",
    function_name="firstBadVersion",
    template="""class Solution:
    def firstBadVersion(self, n: int, bad: int) -> int:
        # 'bad' indicates the first bad version (used to simulate isBadVersion API)
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 5, "bad": 4}, "expected": 4},
        {"input": {"n": 1, "bad": 1}, "expected": 1},
        {"input": {"n": 10, "bad": 1}, "expected": 1},
        {"input": {"n": 10, "bad": 10}, "expected": 10},
        {"input": {"n": 100, "bad": 50}, "expected": 50},
    ],
    solution="""class Solution:
    def firstBadVersion(self, n: int, bad: int) -> int:
        def isBadVersion(version):
            return version >= bad
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
""",
    explanation="""**Approach: Binary Search**

**Time:** O(log n) | **Space:** O(1)

1. Use binary search on the version range `[1, n]`.
2. If `mid` is bad, the first bad version is at `mid` or earlier: `right = mid`.
3. If `mid` is good, the first bad version is after `mid`: `left = mid + 1`.
4. When `left == right`, we've found the first bad version.

**Why this works:** The versions form a pattern `[good, good, ..., good, bad, bad, ..., bad]`. Binary search finds the boundary between good and bad in O(log n) API calls.
"""
)

_register(287,
    description="""<h3>Find the Duplicate Number</h3>
<p>Given an array of integers <code>nums</code> containing <code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>
<p>There is only <strong>one repeated number</strong> in <code>nums</code>, return this repeated number.</p>
<p>You must solve the problem <strong>without</strong> modifying the array and using only constant extra space.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [1,3,4,2,2]
Output: 2</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [3,1,3,4,2]
Output: 3</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; n &le; 10<sup>5</sup></code></li>
<li><code>nums.length == n + 1</code></li>
<li><code>1 &le; nums[i] &le; n</code></li>
<li>Only one duplicate number, but it could be repeated more than once.</li>
</ul>""",
    function_name="findDuplicate",
    template="""class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [1,3,4,2,2]}, "expected": 2},
        {"input": {"nums": [3,1,3,4,2]}, "expected": 3},
        {"input": {"nums": [1,1]}, "expected": 1},
        {"input": {"nums": [1,1,2]}, "expected": 1},
        {"input": {"nums": [2,5,9,6,9,3,8,9,7,1]}, "expected": 9},
    ],
    solution="""class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Floyd's Tortoise and Hare (cycle detection)
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
""",
    explanation="""**Approach: Floyd's Cycle Detection**

**Time:** O(n) | **Space:** O(1)

1. Treat the array as a linked list where `nums[i]` points to index `nums[i]`.
2. Since there's a duplicate, following the chain will create a cycle.
3. Use Floyd's algorithm: slow moves one step, fast moves two steps until they meet.
4. Reset slow to start, move both one step at a time until they meet again — that's the duplicate.

**Why this works:** The duplicate value means two indices point to the same location, creating a cycle. Floyd's algorithm finds the cycle entry point, which is the duplicate number.
"""
)

_register(300,
    description="""<h3>Longest Increasing Subsequence</h3>
<p>Given an integer array <code>nums</code>, return the length of the longest <strong>strictly increasing</strong> subsequence.</p>
<h4>Example 1:</h4>
<pre>Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The LIS is [2,3,7,101], length is 4.</pre>
<h4>Example 2:</h4>
<pre>Input: nums = [0,1,0,3,2,3]
Output: 4</pre>
<h4>Example 3:</h4>
<pre>Input: nums = [7,7,7,7,7,7,7]
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; nums.length &le; 2500</code></li>
<li><code>-10<sup>4</sup> &le; nums[i] &le; 10<sup>4</sup></code></li>
</ul>""",
    function_name="lengthOfLIS",
    template="""class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"nums": [10,9,2,5,3,7,101,18]}, "expected": 4},
        {"input": {"nums": [0,1,0,3,2,3]}, "expected": 4},
        {"input": {"nums": [7,7,7,7,7,7,7]}, "expected": 1},
        {"input": {"nums": [1]}, "expected": 1},
        {"input": {"nums": [1,2,3,4,5]}, "expected": 5},
    ],
    solution="""class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        import bisect
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
""",
    explanation="""**Approach: Binary Search with Patience Sorting**

**Time:** O(n log n) | **Space:** O(n)

1. Maintain a `tails` array where `tails[i]` is the smallest tail element for an increasing subsequence of length `i+1`.
2. For each number, use binary search to find where it should go:
   - If it's larger than all tails, append it (extends the longest subsequence).
   - Otherwise, replace the first tail that's >= it (keeps tails as small as possible).
3. The length of `tails` is the LIS length.

**Why this works:** The `tails` array is always sorted, enabling binary search. By keeping the smallest possible tail for each length, we maximize the chances of extending subsequences with future elements.
"""
)

_register(304,
    description="""<h3>Range Sum Query 2D - Immutable</h3>
<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:</p>
<ul>
<li>Calculate the sum of the elements inside the rectangle defined by its upper left corner <code>(row1, col1)</code> and lower right corner <code>(row2, col2)</code>.</li>
</ul>
<p>Implement the <code>NumMatrix</code> class:</p>
<ul>
<li><code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix.</li>
<li><code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the sum of the elements inside the rectangle.</li>
</ul>
<h4>Example:</h4>
<pre>Input: ["NumMatrix","sumRegion","sumRegion","sumRegion"]
       [[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
Output: [null, 8, 11, 12]</pre>""",
    function_name="NumMatrix",
    template="""class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        # Write your solution here
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass

# Test wrapper - do not modify
class Solution:
    def numMatrix(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "NumMatrix":
                obj = NumMatrix(arg[0])
                result.append(None)
            elif op == "sumRegion":
                result.append(obj.sumRegion(arg[0], arg[1], arg[2], arg[3]))
        return result
""",
    test_cases=[
        {"input": {"operations": ["NumMatrix","sumRegion","sumRegion","sumRegion"],
                    "args": [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]},
         "expected": [None, 8, 11, 12]},
        {"input": {"operations": ["NumMatrix","sumRegion"],
                    "args": [[[[1,2],[3,4]]],[0,0,1,1]]},
         "expected": [None, 10]},
        {"input": {"operations": ["NumMatrix","sumRegion","sumRegion"],
                    "args": [[[[1]]],[0,0,0,0],[0,0,0,0]]},
         "expected": [None, 1, 1]},
    ],
    solution="""class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (matrix[i-1][j-1]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1])

class Solution:
    def numMatrix(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "NumMatrix":
                obj = NumMatrix(arg[0])
                result.append(None)
            elif op == "sumRegion":
                result.append(obj.sumRegion(arg[0], arg[1], arg[2], arg[3]))
        return result
""",
    explanation="""**Approach: 2D Prefix Sum**

**Time:** O(m*n) init, O(1) per query | **Space:** O(m*n)

1. Build a prefix sum matrix where `prefix[i][j]` = sum of all elements in `matrix[0..i-1][0..j-1]`.
2. For a query `(row1, col1, row2, col2)`, use inclusion-exclusion:
   `sum = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]`
3. This gives O(1) per query after O(m*n) preprocessing.

**Why this works:** The 2D prefix sum stores cumulative sums from the top-left corner. To get the sum of any rectangle, we add the full rectangle and subtract the extra regions using inclusion-exclusion, just like the 1D prefix sum but in two dimensions.
"""
)

_register(319,
    description="""<h3>Bulb Switcher</h3>
<p>There are <code>n</code> bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb, then you toggle every third bulb (turning on if it's off or turning off if it's on), and so on until the <code>n<sup>th</sup></code> round.</p>
<p>In the <code>i<sup>th</sup></code> round, you toggle every <code>i</code> bulb. Return the number of bulbs that are on after <code>n</code> rounds.</p>
<h4>Example 1:</h4>
<pre>Input: n = 3
Output: 1
Explanation: Round 1: [on, on, on]. Round 2: [on, off, on]. Round 3: [on, off, off].</pre>
<h4>Example 2:</h4>
<pre>Input: n = 0
Output: 0</pre>
<h4>Example 3:</h4>
<pre>Input: n = 1
Output: 1</pre>
<h4>Constraints:</h4>
<ul>
<li><code>0 &le; n &le; 10<sup>9</sup></code></li>
</ul>""",
    function_name="bulbSwitch",
    template="""class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"n": 3}, "expected": 1},
        {"input": {"n": 0}, "expected": 0},
        {"input": {"n": 1}, "expected": 1},
        {"input": {"n": 10}, "expected": 3},
        {"input": {"n": 100}, "expected": 10},
    ],
    solution="""class Solution:
    def bulbSwitch(self, n: int) -> int:
        import math
        return int(math.sqrt(n))
""",
    explanation="""**Approach: Math (Perfect Squares)**

**Time:** O(1) | **Space:** O(1)

1. Bulb `i` is toggled once for each of its divisors.
2. A bulb ends up ON if it has been toggled an odd number of times.
3. A number has an odd number of divisors only if it is a perfect square (since divisors pair up, except the square root pairs with itself).
4. The number of perfect squares from 1 to n is `floor(sqrt(n))`.

**Why this works:** For example, bulb 6 is toggled by rounds 1, 2, 3, 6 (4 times, even -> OFF). Bulb 9 is toggled by rounds 1, 3, 9 (3 times, odd -> ON). Only perfect squares have an odd number of divisors.
"""
)

_register(322,
    description="""<h3>Coin Change</h3>
<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>
<p>Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>
<p>You may assume that you have an infinite number of each kind of coin.</p>
<h4>Example 1:</h4>
<pre>Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1</pre>
<h4>Example 2:</h4>
<pre>Input: coins = [2], amount = 3
Output: -1</pre>
<h4>Example 3:</h4>
<pre>Input: coins = [1], amount = 0
Output: 0</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; coins.length &le; 12</code></li>
<li><code>1 &le; coins[i] &le; 2<sup>31</sup> - 1</code></li>
<li><code>0 &le; amount &le; 10<sup>4</sup></code></li>
</ul>""",
    function_name="coinChange",
    template="""class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"coins": [1,2,5], "amount": 11}, "expected": 3},
        {"input": {"coins": [2], "amount": 3}, "expected": -1},
        {"input": {"coins": [1], "amount": 0}, "expected": 0},
        {"input": {"coins": [1], "amount": 1}, "expected": 1},
        {"input": {"coins": [1,5,10,25], "amount": 30}, "expected": 2},
    ],
    solution="""class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
""",
    explanation="""**Approach: Dynamic Programming (Bottom-Up)**

**Time:** O(amount * len(coins)) | **Space:** O(amount)

1. Create a DP array where `dp[i]` = minimum coins needed to make amount `i`.
2. `dp[0] = 0` (zero coins for zero amount).
3. For each amount from 1 to target, try each coin: `dp[i] = min(dp[i], dp[i - coin] + 1)`.
4. If `dp[amount]` is still infinity, return -1 (impossible).

**Why this works:** For each amount, the optimal solution either doesn't use a particular coin, or uses it (reducing the problem to `amount - coin`). By building from smaller amounts up, we ensure subproblems are already solved.
"""
)

_register(344,
    description="""<h3>Reverse String</h3>
<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>
<p>You must do this by modifying the input array <strong>in-place</strong> with O(1) extra memory.</p>
<h4>Example 1:</h4>
<pre>Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]</pre>
<h4>Example 2:</h4>
<pre>Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; s.length &le; 10<sup>5</sup></code></li>
<li><code>s[i]</code> is a printable ASCII character.</li>
</ul>""",
    function_name="reverseString",
    template="""class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        # Reverse in-place and return s
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": ["h","e","l","l","o"]}, "expected": ["o","l","l","e","h"]},
        {"input": {"s": ["H","a","n","n","a","h"]}, "expected": ["h","a","n","n","a","H"]},
        {"input": {"s": ["a"]}, "expected": ["a"]},
        {"input": {"s": ["a","b"]}, "expected": ["b","a"]},
    ],
    solution="""class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
""",
    explanation="""**Approach: Two Pointers**

**Time:** O(n) | **Space:** O(1)

1. Place one pointer at the start and one at the end.
2. Swap the characters at both pointers.
3. Move pointers toward each other until they meet.

**Why this works:** Swapping from both ends simultaneously reverses the array in-place. Each element is moved exactly once, and we use no extra space beyond the two pointer variables.
"""
)

_register(345,
    description="""<h3>Reverse Vowels of a String</h3>
<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>
<p>The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in both lower and upper cases, more than once.</p>
<h4>Example 1:</h4>
<pre>Input: s = "IcesCreaam"
Output: "acesCreaIm"</pre>
<h4>Example 2:</h4>
<pre>Input: s = "leetcode"
Output: "leotcede"</pre>
<h4>Constraints:</h4>
<ul>
<li><code>1 &le; s.length &le; 3 * 10<sup>5</sup></code></li>
<li><code>s</code> consists of printable ASCII characters.</li>
</ul>""",
    function_name="reverseVowels",
    template="""class Solution:
    def reverseVowels(self, s: str) -> str:
        # Write your solution here
        pass
""",
    test_cases=[
        {"input": {"s": "IceCream"}, "expected": "aceCreIm"},
        {"input": {"s": "leetcode"}, "expected": "leotcede"},
        {"input": {"s": "hello"}, "expected": "holle"},
        {"input": {"s": "aA"}, "expected": "Aa"},
        {"input": {"s": "xyz"}, "expected": "xyz"},
    ],
    solution="""class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
""",
    explanation="""**Approach: Two Pointers**

**Time:** O(n) | **Space:** O(n) for the character array

1. Convert string to list for mutability.
2. Use two pointers from both ends.
3. Move left pointer forward until it points to a vowel.
4. Move right pointer backward until it points to a vowel.
5. Swap the two vowels and continue.

**Why this works:** We only swap vowel characters while leaving consonants in place. The two-pointer approach ensures each vowel is paired with its mirror counterpart for reversal.
"""
)

_register(359,
    description="""<h3>Logger Rate Limiter</h3>
<p>Design a logger system that receives a stream of messages along with their timestamps. Each <strong>unique</strong> message should only be printed <strong>at most every 10 seconds</strong> (i.e., a message printed at timestamp <code>t</code> will prevent other identical messages from being printed until timestamp <code>t + 10</code>).</p>
<p>All messages will come in chronological order. Several messages may arrive at the same timestamp.</p>
<p>Implement the <code>Logger</code> class:</p>
<ul>
<li><code>Logger()</code> Initializes the logger object.</li>
<li><code>bool shouldPrintMessage(int timestamp, string message)</code> Returns <code>true</code> if the message should be printed, otherwise <code>false</code>.</li>
</ul>
<h4>Example:</h4>
<pre>Input: ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
       [[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
Output: [null,true,true,false,false,false,true]</pre>""",
    function_name="Logger",
    template="""class Logger:
    def __init__(self):
        # Write your solution here
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        pass

# Test wrapper - do not modify
class Solution:
    def logger(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "Logger":
                obj = Logger()
                result.append(None)
            elif op == "shouldPrintMessage":
                result.append(obj.shouldPrintMessage(arg[0], arg[1]))
        return result
""",
    test_cases=[
        {"input": {"operations": ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"],
                    "args": [[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]},
         "expected": [None, True, True, False, False, False, True]},
        {"input": {"operations": ["Logger","shouldPrintMessage","shouldPrintMessage"],
                    "args": [[],[1,"hello"],[1,"hello"]]},
         "expected": [None, True, False]},
        {"input": {"operations": ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"],
                    "args": [[],[0,"a"],[9,"a"],[10,"a"]]},
         "expected": [None, True, False, True]},
    ],
    solution="""class Logger:
    def __init__(self):
        self.msg_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_time or timestamp - self.msg_time[message] >= 10:
            self.msg_time[message] = timestamp
            return True
        return False

class Solution:
    def logger(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "Logger":
                obj = Logger()
                result.append(None)
            elif op == "shouldPrintMessage":
                result.append(obj.shouldPrintMessage(arg[0], arg[1]))
        return result
""",
    explanation="""**Approach: Hash Map**

**Time:** O(1) per call | **Space:** O(n) where n is unique messages

1. Maintain a hash map from message to its last printed timestamp.
2. When a message arrives:
   - If never seen or enough time has passed (>= 10 seconds), print it and update the timestamp.
   - Otherwise, reject it.

**Why this works:** The hash map provides O(1) lookup for the last time each message was printed. The 10-second rule is a simple timestamp comparison.
"""
)

_register(380,
    description="""<h3>Insert Delete GetRandom O(1)</h3>
<p>Implement the <code>RandomizedSet</code> class:</p>
<ul>
<li><code>RandomizedSet()</code> Initializes the object.</li>
<li><code>bool insert(int val)</code> Inserts <code>val</code> if not present. Returns <code>true</code> if not present, <code>false</code> otherwise.</li>
<li><code>bool remove(int val)</code> Removes <code>val</code> if present. Returns <code>true</code> if present, <code>false</code> otherwise.</li>
<li><code>int getRandom()</code> Returns a random element from the set. Each element must be equally likely to be returned.</li>
</ul>
<p>You must implement the functions such that each function works in <strong>average O(1)</strong> time complexity.</p>
<h4>Example:</h4>
<pre>Input: ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
       [[],[1],[2],[2],[],[1],[2],[]]
Output: [null,true,false,true,2,true,false,2]</pre>""",
    function_name="RandomizedSet",
    template="""import random

class RandomizedSet:
    def __init__(self):
        # Write your solution here
        pass

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        pass

# Test wrapper - do not modify
class Solution:
    def randomizedSet(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "RandomizedSet":
                obj = RandomizedSet()
                result.append(None)
            elif op == "insert":
                result.append(obj.insert(arg[0]))
            elif op == "remove":
                result.append(obj.remove(arg[0]))
            elif op == "getRandom":
                result.append(obj.getRandom())
        return result
""",
    test_cases=[
        {"input": {"operations": ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"],
                    "args": [[],[1],[2],[2],[],[1],[2],[]]},
         "expected": [None, True, False, True, 2, True, False, 2]},
        {"input": {"operations": ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"],
                    "args": [[],[1],[2],[1],[3],[2],[]]},
         "expected": [None, True, True, True, True, True, 3]},
        {"input": {"operations": ["RandomizedSet","insert","insert","insert","insert","remove"],
                    "args": [[],[1],[2],[3],[1],[2]]},
         "expected": [None, True, True, True, False, True]},
    ],
    solution="""import random

class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

class Solution:
    def randomizedSet(self, operations: list[str], args: list[list]) -> list:
        result = []
        obj = None
        for op, arg in zip(operations, args):
            if op == "RandomizedSet":
                obj = RandomizedSet()
                result.append(None)
            elif op == "insert":
                result.append(obj.insert(arg[0]))
            elif op == "remove":
                result.append(obj.remove(arg[0]))
            elif op == "getRandom":
                result.append(obj.getRandom())
        return result
""",
    explanation="""**Approach: Hash Map + Dynamic Array**

**Time:** O(1) average for all operations | **Space:** O(n)

1. Use a list (`vals`) for O(1) random access and a hash map (`val_to_idx`) for O(1) lookup.
2. **Insert:** Append to list, record index in hash map.
3. **Remove:** Swap the element with the last element in the list, update the hash map, then pop the last element. This avoids O(n) shifting.
4. **GetRandom:** Use `random.choice` on the list (uniform distribution since it's a contiguous array).

**Why this works:** The key insight for O(1) removal is swapping with the last element. Since we track indices in the hash map, this swap is O(1). The list stays compact, enabling O(1) random selection.
"""
)
