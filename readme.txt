# Minimax Solver for Game Optimization

## Introduction

This project is an implementation of the Minimax algorithm with optional alpha-beta pruning, designed for an Artificial Intelligence course. The Minimax algorithm is a decision rule used for minimizing the possible loss while maximizing the potential gain in a game or decision situation. This implementation focuses on its application in a game scenario, exploring how it can be used to determine the optimal move for a player under the assumption that the opponent is also playing optimally.

## Features

- **Minimax Algorithm:** Core implementation that recursively determines the optimal move by minimizing the potential loss in a worst-case scenario.
- **Alpha-Beta Pruning:** Optional feature that reduces the number of nodes evaluated by the Minimax algorithm, significantly improving performance without affecting the final outcome.
- **Verbose Mode:** Provides detailed step-by-step insights into the algorithm's decision-making process, useful for debugging and learning purposes.
- **Range Limitation:** Allows users to define a numerical range to limit the exploration of branches, further optimizing the performance in large decision trees.
- **Dynamic Player Roles:** Supports specifying whether the root player aims to maximize or minimize the score, offering flexibility in simulating different game scenarios.
- **Error Handling:** Robust error checking for input validation, ensuring the integrity of the game's decision tree structure.

## Environment

- **Language:** Python 3.11.4
- **Dependencies:** None, standard Python libraries only.

## Usage

1. Save the code to a Python file, e.g., `Minimax.py`.
2. Run the code using the command line with the following structure:

```bash
python Minimax.py [options] [Player Type] [Range] [Input Graph File]
```

### Options:

- `-v`: Enables verbose mode to display detailed information about each step (Optional).
- `-ab`: Enables alpha-beta pruning for performance optimization (Optional).

### Player Type:

- Specify either `max` or `min` to indicate the root player's objective.

### Range:

- Use `-range [num]` to specify the maximum allowable difference between max and min values (Optional).

### Input Graph File:

- Provide the path to the text file describing the game's decision tree.

### Example:

```bash
python Minimax.py -v -ab max -range 5 input_graph.txt
```

## Implementation Details

The project simulates a game scenario where two players (maximizer and minimizer) take turns to play. The game tree, represented as a decision tree, is parsed from a provided text file describing the parent-child relationships and node values.

- **Tree Construction:** Parses the input file to construct the game's decision tree, identifying root and leaf nodes.
- **Minimax Algorithm:** Recursively explores the tree to determine the optimal path, considering both maximizing and minimizing strategies.
- **Alpha-Beta Pruning:** Optionally applies pruning to eliminate branches that cannot possibly influence the final decision, based on the current alpha and beta values.
- **Verbose Output:** In verbose mode, each decision step, including node evaluation and pruning actions, is outputted for educational and debugging purposes.

## Testing

The implementation has been thoroughly tested with various input graphs representing different game scenarios, including balanced and unbalanced trees, to ensure accuracy and performance. Users are encouraged to experiment with different game trees and settings to explore the algorithm's behavior.

## Acknowledgments

This project was developed as part of an Artificial Intelligence course, under the guidance of esteemed professors and in collaboration with peers who provided valuable insights and feedback.

## Detailed Implementation in a Game

The Minimax algorithm is best understood through its application in a two-player game, such as Tic-Tac-Toe or Chess, where players take turns. For simplicity, let's consider a generic game with a finite game tree.

### Game Tree Structure

The game tree is a representation of all possible moves in the game, starting from the initial state (root) to the final states (leaves). Each node represents a game state, and the edges represent the possible moves from one state to another.

### Minimax Decision Rule

The Minimax algorithm recursively explores the game tree to find the optimal move for the maximizing player under the assumption that the opponent is playing optimally as well. The algorithm evaluates the leaf nodes using a utility function, which scores the game outcomes from the perspective of the maximizer.

- **Max Nodes:** In "max" layers, the algorithm chooses the move that leads to the highest score.
- **Min Nodes:** In "min" layers, the algorithm assumes the opponent will choose the move that minimizes the maximizer's score.

### Alpha-Beta Pruning

Alpha-Beta pruning is an optimization technique that reduces the number of nodes evaluated. It maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured and the maximum score that the minimizing player is assured, respectively. By updating these values and pruning branches that cannot influence the final decision, the algorithm improves efficiency without affecting the outcome.
