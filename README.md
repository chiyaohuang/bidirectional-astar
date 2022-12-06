# Bi-directional Heuristic Search

This repo is the final team project for ASU CSE571.

Our report: [Bidirectional search in the Pac-Man Domain](link)

## Introduction

This project aims to implement the bidirectional heuristic search algorithm guaranteed to meet in the middle (MM) and compare its properties with others (DFS, BFS, UCS A* search, and bidirectional brute-force search) in the Pac-Man domain. By designing the priority function properly, MM expands the nodes from the start state and the goal state bidirectionally and connects the forward and backward paths in the middle. We provide the technical approach and apply MM to search for the optimal path to the target. The result matches the description of MM. We make multiple experiments to validate the algorithm and provide our viewpoints on the bidirectional heuristic search. In addition, we also try to solve the corner problem via MM. 


## Installation

The repo can only work on python3.6 or python3.7.

Download the code:

```
git clone https://github.com/chiyaohuang/bidirectional_astar.git
```

If you cannot directly run DEMO as follow, you can consider to use [anaconda](https://www.anaconda.com/). It will take few minutes to build the environment.

```
conda env create -f Bi-Astar.yaml
conda activate Bi-Astar
```


## Demo

You can select {searching algorithm} and {layout}, and run the following command.

{searching algorithm}: bfs, dfs, ucs, astar, MM

{layout}: tinyMaze, smallMaze, mediumMaze, bigMaze,...

All layouts we discuss in the report are stored in 'bidirectional_astar/layout/'. You can easily reproduce our experiment results by

```
python pacman.py -l {layout} -p SearchAgent -a fn={searching algorithm}
```

For the example of MM0

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=mm
```

For the example of MM

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=mm,heuristic=manhattanHeuristic
```

For the example of A*

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## T-Test

You can run over our layouts by

```
python script.py
```

The result will be stored in 'bidirectional_astar/finalresult.csv'

You can also reproduce the T-Test by

For the T-Test of the optimal cost

```
python ttest_cost.py
```

For the T-Test of the expanded nodes

```
python ttest_nodes.py
```

For the T-Test of the scores

```
python ttest_scores.py
```

The result will be stored in 'bidirectional_astar/ttest_mm.csv', 'bidirectional_astar/ttest_mm0.csv', and 'bidirectional_astar/ttest_mm_mm0.csv' 


## Members

Chi-Yao Huang [(cy.huang@asu.edu)](cy.huang@asu.edu)

De-Ru Tsai [(dtsai1@asu.edu)](dtsai1@asu.edu)

Syed Asad Husain [(shusain6@asu.edu)](shusain6@asu.edu)

Krithish Goli [(kgoli1@asu.edu)](kgoli1@asu.edu)
