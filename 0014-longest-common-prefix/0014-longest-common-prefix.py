class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        # Start by assuming the entire first word is the prefix
        prefix = strs[0]
        
        # Compare the prefix with every other word in the list
        for word in strs[1:]:
            # Shorten the prefix until the current word starts with it
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                # If it becomes empty, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix