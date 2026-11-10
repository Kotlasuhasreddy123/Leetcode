class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        tri = [[1]]
        for _ in range(1, numRows):
            prev = [0] + tri[-1] + [0]
            row = [prev[i] + prev[i+1] for i in range(len(prev) - 1)]
            tri.append(row)
        return tri