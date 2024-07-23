class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transpose.append(row)
        return transpose

        # Simple mehtond using list comprehension 
        # transpose = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        # return transpose
