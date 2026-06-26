class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num % 2 == 0:
                if num not in count:
                    count[num] = 0
                count[num] += 1

        answer = -1
        max_count = 0

        for num in count:
            if count[num] > max_count:
                max_count = count[num]
                answer = num

            elif count[num] == max_count and num < answer:
                answer = num

        return answer