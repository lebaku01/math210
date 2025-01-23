from anytree import Node, RenderTree

root = Node("Root")
child1 = Node("Child 1", parent=root)
child2 = Node("Child 2", parent=root)

global output

win_conditions = [ {1,2,3}, {4,5,6}, {7,8,9}, {1,5,9}, {3,5,7}, {1,4,7}, {2,5,8}, {3,9,6} ]
moves = [1,2,3,4,5,6,7,8,9]
def terminal_histories(history,win_conditions,moves):
    if len(history) == 9:
        return
    if history in win_conditions:
        return
    else:
        for move in moves:
            terminal_histories(history.append(move), win_conditions, moves)


