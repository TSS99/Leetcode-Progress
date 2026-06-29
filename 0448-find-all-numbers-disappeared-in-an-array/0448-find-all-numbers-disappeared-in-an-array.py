class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        # What this line is doing is basically, it is removing all the repeated/duplicate items in the "nums" array

        answer = []
        # What this line is doing is, it is creating an empty array called answer, that will be an empty array.

        for i in range(1, len(nums) + 1):
        #This line is what is doing is bacically creating a loop, which will be running from 1 to the length of the array+1 , since the loop is starting from 1 and not from zero. also the limit is set such that, i will be running from 1 to lenth of the array+1 because it includes the first element but excludes the last element3,4,5,6

            if i not in seen:
            # Then it is manually checking whether i is not in the list seen then, 
                answer.append(i)
                # Add the i in the answer list, that is what it is doing, and keep on adding
        return answer
        # And finally the function is returning the answer.