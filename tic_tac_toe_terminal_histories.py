from anytree import Node, RenderTree

root = Node("Root")


global output

win_conditions = [ {1,2,3}, {4,5,6}, {7,8,9}, {1,5,9}, {3,5,7}, {1,4,7}, {2,5,8}, {3,9,6} ]
moves = [1,2,3,4,5,6,7,8,9]
def terminal_histories(history,win_conditions,moves):

    if len(history) == 9:
        print(f"{history}, ", end="")
        return
    if history in win_conditions:
        print(f"{history}, ", end="")
        return
    else:
        for move in moves:
            if move not in history:
                history.append(move)
                terminal_histories(history, win_conditions, moves)


history = []
terminal_histories(history, win_conditions, moves)