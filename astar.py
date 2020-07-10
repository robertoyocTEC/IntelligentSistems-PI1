#!/usr/bin/env python
# coding: utf-8

# # A*

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
        route = []
        while 'parent' in final:
            route.append(final['node'])
            final = final['parent']
        route.append(final['node'])
        route.reverse()
        
        print('Total steps: {}\n'.format(len(route)-1))
        for i, node in enumerate(route):
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

def pop_min(queue):
    queue.sort(key=lambda x:x['h'])
    return queue.pop(0)

def d(node, current_node):
    cost = 9
    for index in range(9):
        if node[index] == current_node[index]:
            cost -= 1
    return cost

def AStar(src, dest):
    total_operations = 0
    opened = [{
        'h': 0,
        'node': src
    }]
    closed = []
    
    while len(opened) > 0:
        q = pop_min(opened)
        total_operations = total_operations + 1
        if q['node'] == dest:
            return q, total_operations
        for ady in adyacencies(q['node']):
            if ady not in closed:
                g = d(dest, q['node'])
                f = d(src, q['node'])
                h = g + f
                opened.append({
                    'h': h,
                    'node': ady,
                    'parent': q
                })
        closed.append(q['node'])
    
    return None


# ## Example 1

# In[5]:


initial_board_1 = [
    1, 2, 3,
    0, 4, 5,
    7, 8, 6
]
final, operations = AStar(initial_board_1, target_board)
print('Operations performed = {}'.format(operations))
trace_route(final)


# ## Example 2

# In[6]:


initial_board_2 = [
    1, 2, 0,
    4, 5, 3,
    7, 8, 6
]
final, operations = AStar(initial_board_2, target_board)
print('Operations performed = {}'.format(operations))
trace_route(final)


# ## Example 3

# In[7]:


initial_board_3 = [
    0, 1, 2,
    4, 5, 3,
    7, 8, 6
]
final, operations = AStar(initial_board_3, target_board)
print('Operations performed = {}'.format(operations))
trace_route(final)


# In[ ]:




