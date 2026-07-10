class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            first_num = nums[i]

            # Skip duplicate first numbers
            if i > 0 and first_num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                second_num = nums[left]
                third_num = nums[right]

                total = first_num + second_num + third_num

                if total == 0:
                    answer.append([first_num, second_num, third_num])

                    left += 1
                    right -= 1

                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third numbers
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # Need a bigger number
                    left += 1

                else:
                    # Need a smaller number
                    right -= 1

        return answer