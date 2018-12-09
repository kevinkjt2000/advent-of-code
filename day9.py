from blist import blist

PLAYERS = 410
LAST_MARBLE = 72059

def solve(num_players, last_marble):
    marble_ring = blist([0])
    marble_ring_length = 1
    next_marble = 1
    current_marble_index = 0
    current_player = 0
    scores = [0] * num_players

    while next_marble <= last_marble:
        if next_marble % 23 != 0:
            insert_location = (current_marble_index + 1) % marble_ring_length + 1
            marble_ring.insert(insert_location, next_marble)
            marble_ring_length += 1
            current_marble_index = insert_location
        else:
            scores[current_player] += next_marble
            remove_location = (current_marble_index - 7) % marble_ring_length
            removed_marble = marble_ring.pop(remove_location)
            marble_ring_length -= 1
            scores[current_player] += removed_marble
            current_marble_index = remove_location

        # print(f"[{current_player + 1}]", marble_ring[current_marble_index], marble_ring)
        next_marble += 1
        current_player = (current_player + 1) % num_players

    return max(scores)


assert(solve(9, 25) == 32)
assert(solve(10, 1618) == 8317)
assert(solve(13, 7999) == 146373)
assert(solve(17, 1104) == 2764)
assert(solve(21, 6111) == 54718)
assert(solve(30, 5807) == 37305)

print(solve(PLAYERS, LAST_MARBLE))
print(solve(PLAYERS, LAST_MARBLE*100))
