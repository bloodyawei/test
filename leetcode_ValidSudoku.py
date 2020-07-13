class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
        for i in range(9):
            cols = []
            for j in range(9):
                cols.append(board[j][i])
            if not self.isValidNine(cols):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                boxes = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(boxes):
                    return False
        return True

    def isValidNine(self, nums):
        nums_set = set()
        for num in nums:
            if num != ".":
                if num not in nums_set:
                    nums_set.add(num)
                else:
                    return False
        return True