#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        import bisect

        new = []
        last_displacement = 0
        direction = 0
        
        for i, c in enumerate(commands):
            if c < 0:
                if c == -1:
                    direction = -((abs(direction)-1)%4)
                elif c == -2:
                    direction = -((abs(direction)+1)%4)
                if last_displacement > 0:
                    new.append(last_displacement)
                
                last_displacement = 0
            else:
                new.append(direction)

                last_displacement += c

            if i == len(commands)-1 and last_displacement > 0:
                new.append(last_displacement)
        
        direction = 0
        o_x = sorted(obstacles)
        o_y = sorted([y, x] for [x, y] in obstacles)
        x, y = 0, 0
        max_distance = 0

        for c in new:
            if c <= 0:
                direction = abs(c)
            else:
                if direction == 3:
                    insertion = bisect_left(o_y, [y, x])
                    
                    if len(obstacles) == 0:
                        x += c
                    else:
                        if insertion >= len(o_y):
                            x += c
                        else:
                            if o_y[insertion][0] != y:
                                x += c
                            else:
                                x += min(c, o_y[insertion][1]-1)
                elif direction == 0:
                    insertion = bisect_left(o_x, [x, y])
                    
                    if len(obstacles) == 0:
                        y += c
                    else:
                        if insertion >= len(o_x):
                            y += c
                        else:
                            if o_x[insertion][0] != x:
                                y += c
                            else:
                                y += min(c, o_x[insertion][1]-1)
                elif direction == 1:
                    insertion = bisect_left(o_y, [y, x])
                    
                    if len(obstacles) == 0:
                        x -= c
                    else:
                        if insertion >= len(o_y):
                            if o_y[insertion-1][0] != y:
                                x -= c
                            else:
                                x += max(-c, o_y[insertion-1][1]+1)
                        else:
                            x -= c
                elif direction == 2:
                    insertion = bisect_left(o_x, [x, y])
                    
                    if len(obstacles) == 0:
                        y -= c
                    else:
                        print(insertion)
                        print(o_x)
                        if insertion < len(o_x):
                            if o_x[insertion-1][0] != x:
                                y -= c
                            else:
                                print([-c, o_x[insertion-1][1]+1])
                                y += max(-c, o_x[insertion-1][1]+1)
                        else:
                            y -= c
            print(new)
            print(x,y)
            max_distance = max(max_distance, x**2+y**2) # TODO: Optimize by change


        return max_distance

# TODO: Finish this disgusting shit
# @lc code=end

