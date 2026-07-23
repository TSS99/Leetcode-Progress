class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, visited):
            # Base case: if path length matches nums length, we found a complete permutation
            if len(path) == len(nums):
                res.append(path[:])  # Append a copy of path
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # Make a choice
                visited[i] = True
                path.append(nums[i])
                
                # Recurse
                backtrack(path, visited)
                
                # Undo the choice (Backtrack)
                path.pop()
                visited[i] = False

        backtrack([], [False] * len(nums))
        return res