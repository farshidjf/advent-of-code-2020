from collections import deque

def calculate_score(player):
    return sum(i * card for i, card in zip(range(len(player),0,-1), player))

def play_combat(p1, p2, recursion=False):
    seen = {tuple(p1)}
    while min(len(p1), len(p2)) > 0:
        card1 = p1.popleft()
        card2 = p2.popleft()
        if recursion and len(p1) >= card1 and len(p2) >= card2:
            pr1 = deque(list(p1)[:card1])
            pr2 = deque(list(p2)[:card2])
            winner, _ = play_combat(pr1, pr2, recursion=True)
        else: winner = 1 if card1 > card2 else 2
        if winner == 1:
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card2)
            p2.append(card1)
        if tuple(p1) in seen:
            return 1, 0
        else: seen.add(tuple(p1))

    winner = 1 if len(p1) != 0 else 2
    score = calculate_score(p1 if winner == 1 else p2)
    return winner, score

file_names = ['small_input', 'large_input']
folder_name = './Day22/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        p1, p2 = (deque(map(int, player.splitlines()[1:])) for player in input_file.read().split('\n\n'))
        print(F'Puzzle 1 - {file_name}: ', play_combat(p1.copy(), p2.copy())[1])
        print(F'Puzzle 2 - {file_name}: ', play_combat(p1, p2, recursion=True)[1])
