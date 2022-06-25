"""
    Problem Statment Link :- https://leetcode.com/problems/determine-color-of-a-chessboard-square/
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        blocks = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        x = int(coordinates.replace(coordinates[0],str(blocks[coordinates[0]])))
        total=0
        while x!=0:
            total = total + (x%10)
            x = x // 10
        if total % 2 == 0:
            return False
        else:
            return True
        