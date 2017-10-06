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

|Easy|Medium|Hard|
|--|--|--|
|<table> <tr><th>**1**</th><th>**3**</th><th>**4**</th></tr><tr><td>**7**</td><td>**6**</td><td>**2**</td></tr><tr><th>**8**</th><th> </th><th>**5**</th> </table>|<table> <tr><th>**2**</th><th>**8**</th><th>**1**</th></tr><tr><td> </td><td>**4**</td><td>**3**</td></tr><tr><th>**7**</th><th>**6**</th><th>**2**</th> </table>|<table> <tr><th>**2**</th><th>**8**</th><th>**1**</th></tr><tr><td>**4**</td><td> </td><td>**3**</td></tr><tr><th>**6**</th><th>**5**</th><th>**7**</th> </table>| 

# Goal Search Algorithms

# Comparison

# References
* http://www.d.umn.edu/~jrichar4/8puz.html
