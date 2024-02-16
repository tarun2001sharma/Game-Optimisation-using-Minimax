### Artificial Intelligence Lab-1 ###
### Tarun Sharma ###
### ts5098 ###

import sys

# define class TreeNode to form a tree
class TreeNode:
    def __init__(self, label, value=None):
        self.label = label      # node name
        self.value = value      # node integer value
        self.children = []      # stores node children

# given graph file, form a tree which gives root node as output
def parse_tree_file(file_path):
    nodes = {}              # store every node
    parent_count = {}       # check no. of parents
    global Output  

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        # if line has '=', initialize node and its value
        # node_label = value
        if '=' in line:
            label, value_str = line.split('=')
            label = label.strip()
            if label not in nodes.keys():
                nodes[label] = TreeNode(label)
            nodes[label].value = int(value_str.strip())

        # if line has ':', create parent-child relation
        # parent: [child1, child2, ....]
        elif ':' in line:
            parent_label, children_str = line.split(':')
            children_str = children_str.strip('[] ')
            parent_label = parent_label.strip()
            # initialize parent node on first encounter
            if parent_label not in nodes.keys():
                nodes[parent_label] = TreeNode(parent_label)
            children = [child.strip() for child in children_str.split(',')]
            # add children
            for child_label in children:
                # initialize child node on first encounter
                if child_label not in nodes.keys():
                    nodes[child_label] = TreeNode(child_label)
                nodes[parent_label].children.append(nodes[child_label])
                parent_count[child_label] = parent_count.get(child_label, 0) + 1

    # Checks no. of nodes with no parents
    # Root node should have zero parents
    root_lst = []
    for label, node in nodes.items():
        if label not in parent_count:
            root_lst.append(node)
            
    # Throw error in case of mutiple root nodes
    if len(root_lst)>1:
        Output_str = 'multiple roots: "{}" and "{}"'.format(root_lst[0].label, root_lst[1].label)
        # print(Output_str)
        # sys.exit(1)
        raise ValueError(Output_str)
    # Return if there is only a single root
    elif len(root_lst)==1:
        root = root_lst[0]

    if not root:
        raise ValueError("No root found in the tree")

    return root

# Helper funtion to print Tree
def print_tree(node, level=0):
    if node:
        print(' ' * (level * 2) + node.label, node.value)
        for child in node.children:
            print_tree(child, level + 1)

# funtion to detect cyclic directed graph that might be present in the tree
def isDirectedCyclic(root):
    visited = set()     # initialise visited array 
    stack = set()

    # Depth-First Search algorithm
    def dfs(node):
        # Designate the present node as visited 
        # and include it in the recursive stack
        visited.add(node)
        stack.add(node)

        # Repeat the process for all neighboring nodes. If any of these neighbors 
        # have already been visited and are currently in the recursion stack, 
        # it indicates the presence of a cyclic graph.
        for child in node.children:
            if child not in visited:
                if dfs(child):
                    return True
            elif child in stack:
                return True
            
        # pop node from the recursive stack
        stack.remove(node)
        return False

    # Loop over every child and returns True if graph is cyclic else false
    for node in root.children:
        if node not in visited:
            if dfs(node):
                return True
    return False


# MiniMax algorithm implementation
def minimaxAlgo(node, alpha, beta, range, isMaxPlayer, isVerbose = False, ab = False):
    global Output

    range = abs(range)  # range for max-min cut-off
    prune = False       # var to check for pruning

    # terminating condition - return if no more children present
    if not node.children:
        return node.value
    
    # check if it is a 'max' player
    if isMaxPlayer :
        bestVal = float('-inf')     
        for child in node.children:
            # recurse to the next level, while switching the min-max player condition
            value = minimaxAlgo(child, alpha, beta, range, False, isVerbose, ab)
            # check missing leaf failure
            if value is None:
                Output_str = 'child node "{}" of "{}" not found'.format(child.label, node.label)
                raise ValueError(Output_str)
            if value>bestVal:
                selectedChild = child
                bestVal = value 
            if ab:
                alpha = max(alpha, bestVal)
                # Maximum cut-off
                if bestVal >= range:
                    break
                # alpha-beta pruning
                if beta <= alpha:
                    prune = True
                    break

        if not prune:
            node.value = bestVal
        if node.value != None:
            Output.append('max({}) chooses {} for {}'.format(node.label, selectedChild.label, selectedChild.value))
        return bestVal

    else :
        bestVal = float('inf') 
        for child in node.children:
            # recurse to the next level, while switching the min-max player condition
            value = minimaxAlgo(child, alpha, beta, range, True, isVerbose, ab)
            # check missing leaf failure.
            if value is None:
                Output_str = 'child node "{}" of "{}" not found'.format(child.label, node.label)
                raise ValueError(Output_str)
            if value<bestVal:
                selectedChild = child
                bestVal = value 
            if ab:
                beta = min(beta, bestVal)
                # Minimum cut-off
                if bestVal <= -range:
                    break
                # alpha-beta pruning
                if beta <= alpha:
                    prune = True
                    break
       
        if not prune:
            node.value = bestVal
        if node.value != None:
            Output.append('min({}) chooses {} for {}'.format(node.label, selectedChild.label, selectedChild.value))
        return bestVal


if __name__ == "__main__":

    try:
        Output = []             # List to store output 
        alpha = float('-inf')   # alpha initialized as -inf
        beta = float('inf')     # beta initialized as inf
        range = float('inf')    # range initialized as inf
        isMaxPlayer = True      # Root player intilized to be 'max'
        isVerbose = False       # Verbose mode OFF by default
        ab = False              # No alpha-beta pruning by default

        temprange = []          # temp array to store range info

        # get the command line arguments in list
        commandLst = sys.argv[1:]

        for argument in commandLst:
            # verbose mode
            if argument == '-v':
                isVerbose = True
            # alpha-beta pruning
            elif argument == '-ab':
                ab = True
            # if root player is 'min' 
            elif argument == 'min':
                isMaxPlayer = False
            # otherwise root player is defined to be 'max' 
            elif argument == 'max':
                isMaxPlayer = True
            # range and a number n
            elif argument == '-range':
                index = commandLst.index(argument)
                if commandLst[index+1].isdigit():
                    range = int(commandLst[index+1])
                    del commandLst[index+1]
            # get the graph input from text file
            elif argument[-4:] == '.txt':
                graphfile = argument
            else:
                raise ValueError('Bad Arguments passed. Please Retry')

        # Construct a tree and get the tree root node
        tree_root = parse_tree_file(graphfile)
        # print(tree_root)
        # print_tree(tree_root)

        # Check for Cyclic Directed Graphs
        if isDirectedCyclic(tree_root):
            print('Error: A cyclic directe graph detected.')

        else:
            # create new tree
            newTree = minimaxAlgo(tree_root, alpha, beta, range, isMaxPlayer, isVerbose, ab)

            # Print output
            if not isVerbose:
                print(Output[-1])
            else:
                for newline in Output:
                    print(newline)

    except Exception as e:
        print("Error:", e)
