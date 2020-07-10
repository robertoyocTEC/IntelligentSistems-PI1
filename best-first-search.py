#!/usr/bin/env python
# coding: utf-8

# # Best First Search

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


def bfs_get_minimum(initial, next_nodes):
    minimum = 1000000
    minimum_node = ''
    
    for next_node in next_nodes:
        cost = 9
        for index in range(9):
            if initial[index] == next_node[index]:
                cost -= 1
        
        #print('next_node = {}. cost = {}'.format(next_node, cost))
        if cost < minimum:
            minimum = cost
            minimum_node = next_node
    
    #print('')
    #print_board(convert_string_to_list(minimum_node))
    #print(minimum_node)
    next_nodes.remove(minimum_node)
    return minimum_node
            
        
    
def bfs(initial_board, target_board):
    initial = convert_list_to_string(initial_board)
    target = convert_list_to_string(target_board)
    
     # Set queues
    next_nodes = []
    visited_nodes = set()
    steps = [] # To recreate path
    
    # Add source node first
    next_nodes.append(initial)
    visited_nodes.add(initial)
    
    operations_performed = 0
        
    while next_nodes:
        print('\n--------------------')
        print('next_nodes = {}'.format(next_nodes))
        print('visited_nodes = {}'.format(visited_nodes))
        node = bfs_get_minimum(target, next_nodes)
        steps.append(node)
        operations_performed += 1
    
        if (node == target):
            print('\n* Target reached!')
            return operations_performed, steps
        
        for adjacent_node in get_adyacent_boards(convert_string_to_list(node)): 
            if adjacent_node not in visited_nodes:
                operations_performed += 1
                next_nodes.append(adjacent_node)
                visited_nodes.add(adjacent_node)
    
    return operations_performed, steps


# ## Example #1

# In[6]:


initial_board_1 = [
    1, 2, 3,
    0, 4, 5,
    7, 8, 6
]
operations_performed, steps = bfs(initial_board_1, target_board)


# In[7]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(len(steps)):
    print('Step #{}'.format(index))
    print_board(steps[index])
    print('\n')


# <img src="best-first-search-steps.png" />

# ## Example #2

# In[8]:


initial_board_2 = [
    1, 2, 0,
    4, 5, 3,
    7, 8, 6
]
operations_performed, steps = bfs(initial_board_2, target_board)


# In[9]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(len(steps)):
    print('Step #{}'.format(index))
    print_board(steps[index])
    print('\n')


# ## Example #3

# In[10]:


initial_board_3 = [
    0, 1, 2,
    4, 5, 3,
    7, 8, 6
]
operations_performed, steps = bfs(initial_board_3, target_board)


# In[11]:


print('Operations performed = {}'.format(operations_performed))
print('Total steps = {}\n'.format(len(steps) - 1))

for index in range(1, len(steps)):
    print('Step #{}'.format(index))
    print_board(steps[index])
    print('\n')


# In[ ]:




