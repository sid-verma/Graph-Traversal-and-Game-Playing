# About
The aim of this part of the Project is to draw a comparison between 6 different types of Goal Search Algorithms namely
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Greedy-Best-First Search (GBFS)
* A Star Heuristic Search (A Star)
* Iterative-Deepening-A–Star Heuristic Search (IDA Star)

These 6 Algorithms were applied to the 8-Puzzle search problem.

# The 8-Puzzle search problem
An 8 puzzle is a simple game consisting of a 3 x 3 grid (containing 9 squares). One of the squares is empty. 
The object is to move to squares around into different positions and having the numbers displayed in the "goal state".

A solved state of the problem is shown below.

| **1** | **2** | **3** |
|:--|:--|:--|
| **4** | **5** | **6** |
| **7** | **8** |  |

The goal of the algorithms is to make a tile in the grid move in any direction (&larr;, &uarr;, &rarr; and &darr;) that is permissible for the given state of the grid. In the example shown above, (8) &rarr; or (6) &darr; are permissible moves.

A **Game State** refers to any vaild state of the grid where the numbers are in a scambled order. Depending on the optimal number of moves it takes for any game state to return to the solved state, they can be classified into 3 diffculty levels i.e.

### Easy
An example is as shown.

| **1** | **3** | **4** |
|:--|:--|:--|
| **7** | **6** | **2** |
| **8** |  | **5** |

### Medium
An example is as shown.

| **2** | **8** | **1** |
|:--|:--|:--|
|  | **4** | **3** |
| **7** | **6** | **2** |
### Hard
An example is as shown.

| **2** | **8** | **1** |
|:--|:--|:--|
| **4** |  | **3** |
| **6** | **5** | **6** |

# Goal Search Algorithms

# Comparison

# References
* http://www.d.umn.edu/~jrichar4/8puz.html
