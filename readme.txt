Artifiical Intelligence Lab 1
Name: Tarun Sharma
NetID: ts5098
Collaborators: tgd8275, rk4748

Python version - Python 3.11.4

1.  Save the code to a Python file, e.g., Minimax.py.

2.  Run the code with the following command-line arguments:

    -v (Optional): Enables verbose mode, which displays additional information 
    about each step of the MiniMax algorithm.
    By default it is turned OFF.

    -ab (Optional): Enables alpha-beta pruning to improve performance.
    By default it is turned OFF.

    Player Type: Specify either 'max' or 'min' to indicate whether the root player 
    aims to maximize or minimize the score.
    By default root node is asigned to be a 'max' player.
    On multiple instances of min/max input by user, the program takes into account
    the latest argument.

    Range (Optional): Specify a numerical range that defines the maximum allowable difference 
    between max and min values. The algorithm will stop exploring branches when 
    this range is reached.
    Note the user must input range as '-range<space>num'.
    By default the range is defined to be [-inf, inf].
    On multiple instances of 'range' input by user, the program takes into account
    the latest argument.

    Input Graph File: Provide the path to the text file that describes the 
    parent-child relationships and values of nodes in the tree.
    Note that text file folder directory should be the same as the code directory.

    All other possible input arguments by the user will throw an error stating -
    'Bad Arguments passed. Please Retry'

3.  Command line input example:
    Go to the folder directory and write -
    python Minimax.py -v max -ab 5 input_graph.txt
