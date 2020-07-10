#!/usr/bin/env python
# coding: utf-8

# # IDS

# - [The board](#The-board)
# - [Utils](#Utils)
# - [Main logic](#Main-logic)
# - [Example #1](#Example-1)
# - [Example #2](#Example-2)
# - [Example #3](#Example-3)

# ## The board

# In[1]:


target_board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]
allowed_moves = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7]
]


# # Utils

# In[2]:


def print_board(board):
    for index in range(3):
        print('{} | {} | {}'.format(board[3 * index + 0], board[3 * index + 1], board[3 * index + 2]))
        
        if index < 2:
            print('---------')
            

def trace_route(final):
    if final:
        final.reverse()
        
        print('Total steps: {}\n'.format(len(final)-1))
        for i, node in enumerate(final):
            print('Step #{}'.format(i))
            print_board(node)
            print()
        
    else:
        print('Not possible')


# In[3]:


print_board(target_board)


# ## Main logic

# In[4]:


def adyacencies(src):
    pos = src.index(0)
    adys = []
    
    for move in allowed_moves[pos]:
        new_board = src.copy()
        new_board[pos] = new_board[move]
        new_board[move] = 0
        adys.append(new_board)
    
    return adys

def IDS(src, dest, limit):
    total_operations = 0
    for i in range(limit):
        ops, value, route = ids(src, dest, i)
        total_operations = total_operations + ops
        if value:
            return total_operations, True, route
            print('DONE')
    
    print('Not able to find')
    return total_operations, False, []

    
def ids(src, dest, limit):
    ops = 1
    
    if src == dest:
        return ops, True, [src]
    
    if limit <= 0:
        return ops, False, []
    
    for ady in adyacencies(src):
        ops_r, value, route = ids(ady, dest, limit - 1)
        if value:
            ops = ops + ops_r
            route.append(src)
            return ops, True, route
    
    return ops, False, []


# # Example 1

# In[5]:


initial_board_1 = [
    1, 2, 3,
    0, 4, 5,
    7, 8, 6
]
operations_performed, final, route = IDS(initial_board_1, target_board, 25)
print('Operations performed = {}'.format(operations_performed))
trace_route(route)


# # Example 2

# In[6]:


initial_board_2 = [
    1, 2, 0,
    4, 5, 3,
    7, 8, 6
]
operations_performed, final, route = IDS(initial_board_2, target_board, 25)
print('Operations performed = {}'.format(operations_performed))
trace_route(route)


# # Example 3

# In[7]:


initial_board_3 = [
    0, 1, 2,
    4, 5, 3,
    7, 8, 6
]
operations_performed, final, route = IDS(initial_board_3, target_board, 25)
print('Operations performed = {}'.format(operations_performed))
trace_route(route)


# In[ ]:




