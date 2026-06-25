class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with the first row
        triangle = []
        
        for i in range(numRows):
            # Create a row of '1's with length (i + 1)
            row = [1] * (i + 1)
            
            # Update the middle elements (excluding the first and last elements)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            # Add the completed row to our triangle
            triangle.append(row)
            
        return triangle