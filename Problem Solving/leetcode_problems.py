# This year Sachin is participating in a Dancing competition.
# The dance performance will be done on a linear stage marked with integral positions.
# Initially, Sachin is present at position X and Sachin's dance partner is at position Y.
# Sachin can perform two kinds of dance moves.

# If Sachin is currently at position k, Sachin can:
# 1. Moonwalk to position k+2, or
# 2. Slide to position k−1

# Sachin wants to find the minimum number of moves required to reach his partner. Can you help him find this number?


def calculate_moves(x, y):
    if x > y:
        step = -2
    else:
        step = 2
    moves = 0
    for i in range(x, y, step):
        moves += 1
    if step and moves * step > y:
        moves += 1
    else:
        if abs(moves * step) < x:
            moves += 1
        else:
            moves
    print(moves)

#
# x = 0   # In this case sachin is on left side of his partner ( Moves forward)
# y = 11  # Partner is on right side
# In this case x has to move 7 steps 2-4-6-8-10-12 ( 6) and -1 so 7 steps to achieve 11

x = 11 # In this case sachin is on right side of his partner ( Moves backward )
y = 0  # Partner is on left side
# Expected Output  :- In this case x has to move total 6 steps 11-9-7-5-3-2 (5) and then -1 to achieve 11
calculate_moves(x, y)

