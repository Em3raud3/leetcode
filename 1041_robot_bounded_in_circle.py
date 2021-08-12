class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dirx, diry = 0, 0, 0, 1

        for i in instructions:
            if i == "R": dirx, diry = diry, - dirx
            if i == "L": dirx, diry = -diry, dirx
            if i == "G": x ,y = x + dirx, y + diry

        return (x,y) == (0,0) or (dirx,diry) != (0,1)
