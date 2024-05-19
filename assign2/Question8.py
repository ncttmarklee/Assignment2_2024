import unittest
def fastest_racer(name_one, name_two, top_speed_one, top_speed_two, acceleration_one, acceleration_two): 
    # This function takes in the top speed and acceleration of two racers and returns the name of the racer that hits their top speed fastest
    # If both racers reach their top speed at the same time, the function returns "Tie"
    # If the inputs are invalid, the function returns "Invalid Input"
    # Check if the inputs are valid
    if top_speed_one <= 0 or top_speed_two <= 0 or acceleration_one <= 0 or acceleration_two <= 0:
        return "Invalid Input"
    # Calculate the time taken for each racer to reach their top speed
    time_one = top_speed_one / acceleration_one
    time_two = top_speed_two / acceleration_two
    # Check which racer is faster
    if time_one < time_two:
        return name_one
    elif time_two < time_one:
        return name_two
    else:
        return "Tie"
    
# your code goes below this line ----------------------------------------------
class TestFastestRacer(unittest.TestCase):
    def test_fastest_racer(self):
        name_one = ["Racer 1", "Racer 1", "Racer 1", "Racer 1"]
        name_two = ["Racer 2", "Racer 2", "Racer 2", "Racer 2"]
        top_speed_one = [100, 90, 100, 100]
        top_speed_two = [90, 100, 100, 100]
        acceleration_one = [10, 9, 10, -10]
        acceleration_two = [9, 10, 10, 10]
        expected_results = ["Racer 1", "Racer 2", "Tie", "Invalid Input"]
        msg = ['Racer 1!', 'Racer 2!', 'Tie!', 'Invalid Input!']
        for i in range(len(name_one)):  # Fixed variable name
            self.assertEqual(expected_results[i], fastest_racer(name_one[i], name_two[i], \
                top_speed_one[i], top_speed_two[i], acceleration_one[i], acceleration_two[i]), msg[i])  # Fixed argument

if __name__ == '__main__':
    unittest.main()
    