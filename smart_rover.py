import time
import os
# directions = ["N" , "E" , "S" , "W"]
# Rover = R
class Rover:
    def __init__(self , name , direction , maze , current_position = (0, 0)):
        self.name = name
        self.current_position = current_position
        self.direction = direction
        self.maze = maze
        self.previous_positions = []
        self.spy_memory_success = []
        self.spy_memory_fail = []
    def memory(self):
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        self.spy_memory_success = []
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.maze[current_position[0]][current_position[1]] == 2:
                self.spy_memory_success.append(current_path)
                continue
            if current_step == 4:
                self.spy_memory_success.append(current_path)
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.maze) and 0 <= new_position[1] < len(self.maze[0]):
                    is_passable = (self.maze[new_position[0]][new_position[1]] == 0) or (self.maze[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.spy_memory_fail and \
                           new_position not in self.previous_positions and \
                           new_position not in current_path and \
                           new_position != self.current_position:
                           new_path = current_path + [new_position]
                           current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
    def explore(self):
        if len(self.spy_memory_success) > 0:
            next_route = self.spy_memory_success[0]
            next_position = next_route[0]
            self.previous_positions.append(self.current_position)
            self.current_position = next_position
            return True
        else:
            return False
    def backtrack(self):
        if len(self.previous_positions) > 0:
            self.spy_memory_fail.append(self.current_position)
            previous_position = self.previous_positions.pop()
            self.current_position = previous_position
            return True
        else:
            return False
            


maze_str = """
0000100000100000100000100000100000100000
0110101110101110101110101110101110101110
0100001000001000001000001000001000001000
0101111011111011111011111011111011111011
0101000010000010000010000010000010000010
0101011110111110111110111110111110111110
0001010000100000100000100000100000100000
1101010111101111101111101111101111101110
0000010100001000001000001000001000001000
0111110101111011111011111011111011111011
0100000101000010000010000010000010000010
0101111101011110111110111110111110111110
0101000001010000100000100000100000100000
0101011111010111101111101111101111101110
0101010000010100001000001000001000001000
0101010111110101111011111011111011111011
0101010100000101000010000010000010000010
0101010101111101011110111110111110111110
0101010101000001010000100000100000100000
0101010101011111010111101111101111101110
0101010101010000010100001000001000001000
0101010101010111110101111011111011111011
0101010101010100000101000010000010000010
0101010101010101111101011110111110111110
0101010101010101000001010000100000100000
0101010101010101011111010111101111101110
0101010101010101010000010100001000001000
0101010101010101010111110101111011111011
0101010101010101010100000101000010000010
0101010101010101010101111101011110111110
0101010101010101010101000001010000100000
0101010101010101010101011111010111101110
0101010101010101010101010000010100001000
0101010101010101010101010111110101111010
0101010101010101010101010100000101000010
0101010101010101010101010101111101011110
0100010001000100010001000101000001010000
1111011111011111011111011111011111010111
0000000000000000000000000000000000010002
1111111111111111111111111111111111111111
"""

test_maze = [[int(char) for char in line] for line in maze_str.strip().split("\n")]

my_rover = Rover(name= "Curious Rover" , direction = "N" , maze = test_maze , current_position = (0, 0))

print("Rover is starting at position " + str(my_rover.current_position))
time.sleep(2)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if test_maze[my_rover.current_position[0]][my_rover.current_position[1]] == 2:
        print("\n🏆 GÖREV TAMAMLANDI! HEDEFE ULAŞILDI! 🏆")
        break
    my_rover.memory()
    is_moved = my_rover.explore()
    if is_moved == False:
        my_rover.backtrack()
    for r in range(len(test_maze)):
        looking_of_row = ""
        for c in range(len(test_maze[0])):
            if (r, c) == my_rover.current_position:
                looking_of_row += "🤖"
            elif test_maze[r][c] == 2:        
                looking_of_row += "🎯"       
            elif (r,c) in my_rover.spy_memory_fail:
                looking_of_row += "❌"
            elif (r,c) in my_rover.previous_positions:
                looking_of_row += "👣"
            elif test_maze[r][c] == 1:
                looking_of_row += "⬛"
            else:
                looking_of_row += "⬜"
        print(looking_of_row)
    print("STATUS: Rover is at position " + str(my_rover.current_position))
    print(f"STATUS: Visited failed positions: {my_rover.spy_memory_fail}")
    time.sleep(0.4)





        




            




        






