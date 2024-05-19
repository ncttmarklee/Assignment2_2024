import unittest
# This function takes a direction and a position and returns the new position
def move_direction(direction, x, y):
    if x < 0 or y < 0 or x > 7 or y > 7:
        raise ValueError('Invalid position')
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    elif direction == 'NE':
        x += 1
        y -= 1
    elif direction == 'NW':
        x -= 1
        y -= 1
    elif direction == 'SE':
        x += 1
        y += 1
    elif direction == 'SW':
        x -= 1
        y += 1
    else:
        raise ValueError('Invalid direction')
    return x, y
    
#your code below this line ----------------------------
class TestMoveDirection(unittest.TestCase):
    def test_move_direction(self):
        directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
        positions = [(3, 3), (3, 3), (3, 3), (3, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
        expected_results = [(3, 2), (3, 4), (4, 3), (2, 3), (4, 2), (2, 2), (4, 4), (2, 4)]
        messages = [
            'Moving North from (3, 3)',
            'Moving South from (3, 3)',
            'Moving East from (3, 3)',
            'Moving West from (3, 3)',
            'Moving Northeast from (3, 3)',
            'Moving Northwest from (3, 3)',
            'Moving Southeast from (3, 3)',
            'Moving Southwest from (3, 3)'
        ]
        for i in range(len(directions)):
            self.assertEqual(expected_results[i], move_direction(directions[i], positions[i]), messages[i])
if __name__ == '__main__':
    unittest.main()
    