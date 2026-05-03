class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case: if numRows is 0, return an empty list
        if numRows == 0:
            return []
        
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        # Loop to generate the remaining rows
        for i in range(1, numRows):
            prev_row = triangle[-1]
            # Every row starts with a 1
            new_row = [1] 
            
            # Calculate the middle elements of the new row
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
                
            # Every row ends with a 1
            new_row.append(1) 
            
            # Add the completed row to the triangle
            triangle.append(new_row)
            
        return triangle