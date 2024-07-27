class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped = [[0] * c for _ in range(r)] # initialize a 2D array
        size = len(mat) * len(mat[0])
        mat_liner = [0] * size

        if size != r * c or (len(mat) == r and len(mat[0]) == c):
            return mat

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat_liner[(len(mat[0]) * i) + j] = mat[i][j]

        for s in range(size):
            reshaped[s//c][s%c] = mat_liner[s]
            
        return reshaped