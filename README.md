# Graph Traversal and Game Playing
The language used for implementation was Python 2.7.

# Graph Traversal
## Problem Statement
Problem Statement: The 8-puzzle problem can be represented by a tree where a single node represents the game state and the child nodes are next possible game states for each permissible move.  In order for the initial state to reach the solved state, 6 Graph traversal algorithms (BFS, DFS, IDS, Greedy Best First Search, A \* and IDA \*)  were considered and a comparative analysis of the traversal algorithms was carried out.

## About
The aim of this part of the Project is to draw a comparison between 6 different types of Goal Search Algorithms namely
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Iterative-Deepening Search (IDS)
* Greedy-Best-First Search (GBFS)
* A-Star Heuristic Search (A \*)
* Iterative-Deepening-A–Star Heuristic Search (IDA \*)

These 6 Algorithms were applied to the 8-Puzzle search problem.

## The 8-Puzzle search problem
An 8 puzzle is a simple game consisting of a 3 x 3 grid (containing 9 squares). One of the squares is empty. 
The object is to move to squares around into different positions and having the numbers displayed in the "goal state".

A solved state of the problem is shown below.

| **1** | **2** | **3** |
|:--|:--|:--|
| **4** | **5** | **6** |
| **7** | **8** |  |

The goal of the algorithms is to make a tile in the grid move in any direction (&larr;, &uarr;, &rarr; and &darr;) that is permissible for the given state of the grid. In the example shown above, (8) &rarr; or (6) &darr; are permissible moves.

A **Game State** refers to any vaild state of the grid where the numbers are in a scambled order. Depending on the optimal number of moves it takes for any game state to return to the solved state, they can be classified into 3 diffculty levels i.e.

|Easy|Medium|Hard|
|--|--|--|
|<table> <tr><th>**1**</th><th>**3**</th><th>**4**</th></tr><tr><td>**7**</td><td>**6**</td><td>**2**</td></tr><tr><th>**8**</th><th> </th><th>**5**</th> </table>|<table> <tr><th>**2**</th><th>**8**</th><th>**1**</th></tr><tr><td> </td><td>**4**</td><td>**3**</td></tr><tr><th>**7**</th><th>**6**</th><th>**2**</th> </table>|<table> <tr><th>**2**</th><th>**8**</th><th>**1**</th></tr><tr><td>**4**</td><td> </td><td>**3**</td></tr><tr><th>**6**</th><th>**5**</th><th>**7**</th> </table>| 

## Graph Traversal Algorithms
Let us look at each algorithm in more detail and understand the differences in their approach. With respect to the 8-Puzzle search problem, each game state corresponds to a node in a tree constituting of several game states. The root of this tree is the initial state and the leaf is the solved state. Each child of a particular node

### 1. Breadth-First Search (BFS)
The BFS algorithm traverses a tree in a horizontal fashion, covering all the nodes at the same level before proceeding to the next level. 

![](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

### 2. Depth-First Search (DFS)
The DFS algorithm traverses a tree in a vertical taking the left-most child node from each node.

![](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

### 3. Iterative-Deepening Search (IDS)
In the IDS method for search, a threshold level of K is specified and DFS search is applied upto nodes at the Kth level. If the goal node is not found till level K, it is incremented to K+1 and the process is repeated until the tree is exhausted or the goal node is found.

### 4. Greedy-Best-First Search (GBFS)
The GBFS algorithm follows a particular heurisitc function h(n). It looks at all the next possible moves and takes the one that maximizes the heuristic h(n). In other words, it takes the step that is the best possible one towards reaching the goal.

### 5. A-Star Heuristic Search (A \*)
The A \* search method also uses a heursitic function but with a modification. A \* heuristic is given by f(n) = g(n) + h(n) where g(n) is the cost of choosing a paricular choice and h(n) is the regular heuristic. It is an improvement over the GBFS method since the latter assumes the cost of taking any of the permissible choices is equal.

### 6. Iterative-Deepening-A–Star Heuristic Search (IDA \*)
This is similar to A\* but is applied upto a threshold level K (similar to IDFS). It does not use dynamic programming, hence many nodes are searched over again during each iteration.

## Comparison
The following table compares attributes of each graph traversal algorithm.

## References
* http://www.d.umn.edu/~jrichar4/8puz.html

# Game Playing
## Problem Statement


## Minimax Strategy:
We employ a minimax game playing strategy where we

## Alpha-Beta Pruning:
This method is applied where we want to reduce the no. of nodes traversed in a tree, and save a lot of running time when it comes to making decisions for players (of a game). To do this, we first use the utility values of the leaf nodes, and work our way upwards to find out the minimax values of each node of the tree. Based on that we do two tests:

### For a Min state node:

* **Case1:** If the child vertices are lesser than the minimax (Beta) value of the node AND the child vertices are greater than the current Max value of the super-ancestor node (parent of the parent node), then we copy the value of the child onto the parent.

* **Case2:** If the child vertices are greater than the minimax value of the node, then we move on to the next child vertex

* **Case3:** If the child vertices are greater than the minimax value of the parent node, BUT they are lesser than the Max value of the super-ancestor; It means that no other child vertex can be preferred to be copied onto the parent. Hence we PRUNE the other nodes, and move on to another sub-tree. The same logic can be conversely applied for a Max state node having a minimax value(Alpha).

In this way we, we are able to ignore a lot of unnecessary nodes and traverse the entire tree in a faster way to get the (Alpha, Beta) values of the root node. Then we can backtrack our path based on the same values which got us to the root node, and get the optimal game playing decision sets for a particular side.
