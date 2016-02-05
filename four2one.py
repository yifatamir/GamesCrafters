class Game:

    def __init__(self, pos, prim = 0):
        self.initial_position = pos
        self.primitive = prim #losing initial position
        
def solve(game):
    pos = game.initial_position
    prim = game.primitive
    if pos < prim:
        return 'poorly set up game'
    if pos == prim:
        return 'lose'
    else:
        chart = ['lose' for x in range(pos - prim + 1)]
        curr = 1
        while curr <= pos - prim:
            successors = [chart[curr - x] for x in generate_moves(curr, prim)]
            if 'lose' in successors:
                chart[curr] = 'win'
            curr += 1
        return chart[pos-prim]

def generate_moves(pos, prim = 0):
    if pos > prim + 1:
        return [1, 2]
    elif pos == prim + 1:
        return [1]
    else:
        return []

g = Game(100)
print(solve(g))


#initial position
#generate moves
#do moves
#primitives
