#!/usr/bin/env python
# coding: utf-8

# # Bidirectional Search

# - [The board](#The-board)
# - [Utils](#Utils)
# - [Main logic](#Main-logic)
# - [Example #1](#Example-#1)
# - [Example #2](#Example-#2)
# - [Example #3](#Example-#3)

# ## The board

# In[1]:


target_board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]
allowed_moves = {}
allowed_moves[0] = [1, 3]
allowed_moves[1] = [0, 2, 4]
allowed_moves[2] = [1, 5]
allowed_moves[3] = [0, 4, 6]
allowed_moves[4] = [1, 3, 5, 7]
allowed_moves[5] = [2, 4, 8]
allowed_moves[6] = [3, 7]
allowed_moves[7] = [4, 6, 8]
allowed_moves[8] = [5, 7]


# ## Utils

# In[2]:


def print_board(board):
    for index in range(3):
        print('{} | {} | {}'.format(board[3 * index + 0], board[3 * index + 1], board[3 * index + 2]))
        
        if index < 2:
            print('---------')


# In[3]:


print_board(target_board)


# In[4]:


def convert_list_to_string(board):
    return ''.join(str(box) for box in board)

def convert_string_to_list(board):
    return [int(box) for box in board]

def get_adyacent_boards(board):
    print('\nInitial board')
    print_board(board)
    index_empty_box = board.index(0)
    indexes_to_place_empty_box = allowed_moves[index_empty_box]
    adjacent_boards = []
    
    for index in indexes_to_place_empty_box:
        new_board = board[:]
        new_board[index_empty_box] = new_board[index]
        new_board[index] = 0
        print('\nNew board')
        print_board(new_board)
        new_board_string = convert_list_to_string(new_board)
        adjacent_boards.append(new_board_string)
        
    return adjacent_boards


# ## Main logic

# In[5]:


def bfs_reconstruct_path(parents, source, target):
    path = [target]
    previous = parents[target]
    
    while previous != source:
        path.append(previous)
        previous = parents[previous]
    
    path.append(source)
    path.reverse()
    return path

def bfs_solve(source, target):
    initial = convert_list_to_string(source)
    target = convert_list_to_string(target)
    
    # Set queues
    next_nodes_1 = []
    visited_nodes_1 = set()
    parents_1 = {} # To recreat path
    next_nodes_2 = []
    visited_nodes_2 = set()
    parents_2 = {} # To recreat path
    
    # Add source node first
    next_nodes_1.append(initial)
    visited_nodes_1.add(initial)
    
    next_nodes_2.append(target)
    visited_nodes_2.add(target)
    
    operations_performed = 0
    cycles = 0
    
    while next_nodes_1 and next_nodes_2:
        cycles += 1
        operations_performed += 1
        print('\n-------------------- {}'.format(cycles))
        print('next_nodes_1 = {}'.format(next_nodes_1))
        print('visited_nodes_1 = {}'.format(visited_nodes_1))
        node_1 = next_nodes_1.pop(0)
        
        if (node_1 == target):
            print('\n* Target reached!')
            return operations_performed, parents_1, 1
        
        for adjacent_node in get_adyacent_boards(convert_string_to_list(node_1)):
            if adjacent_node not in visited_nodes_1:
                operations_performed += 1
                next_nodes_1.append(adjacent_node)
                visited_nodes_1.add(adjacent_node)
                parents_1[adjacent_node] = node_1
                
        print('\n\nnext_nodes_2 = {}'.format(next_nodes_2))
        print('visited_nodes_2 = {}'.format(visited_nodes_2))
        node_2 = next_nodes_2.pop(0)
        print('node_2 = {}'.format(node_2))
        print('source = {}'.format(initial))
        
        if (node_2 == initial):
            print('\n* Source reached!')
            return operations_performed, parents_2, 2
        
        for adjacent_node in get_adyacent_boards(convert_string_to_list(node_2)):
            if adjacent_node not in visited_nodes_2:
                operations_performed += 1
                next_nodes_2.append(adjacent_node)
                visited_nodes_2.add(adjacent_node)
                parents_2[adjacent_node] = node_2
        
    return operations_performed, [], 0

def bfs(source, target):
    operations_performed, parents, path = bfs_solve(source, target)
    steps = []
    
    if path == 1:
        steps = bfs_reconstruct_path(parents, convert_list_to_string(source), convert_list_to_string(target))
    elif path == 2:
        steps = bfs_reconstruct_path(parents, convert_list_to_string(target), convert_list_to_string(source))
        steps.reverse()

    return operations_performed, steps, path


# ## Example 1

# In[6]:


initial_board_1 = [
    1, 2, 3,
    0, 4, 5,
    7, 8, 6
]
operations_performed, steps, path = bfs(initial_board_1, target_board)


# In[7]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(len(steps)):
    print('Paso #{}'.format(index))
    print_board(steps[index])
    print('\n')


# ## Example 2

# In[8]:


initial_board_2 = [
    1, 2, 0,
    4, 5, 3,
    7, 8, 6
]
operations_performed, steps, path = bfs(initial_board_2, target_board)


# In[9]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(len(steps)):
    print('Paso #{}'.format(index))
    print_board(steps[index])
    print('\n')


# ## Example 3

# In[10]:


initial_board_3 = [
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
]
operations_performed, steps, path = bfs(initial_board_3, target_board)


# In[11]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(len(steps)):
    print('Paso #{}'.format(index))
    print_board(steps[index])
    print('\n')


# In[ ]:




