class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 2 pointer solution, l,r pointer
        # start at each end if n[l] + n[r] < target the l++ until r>l
        lp, rp, tempSum = 0, len(numbers)-1, 0
        while lp < rp:
            tempSum = numbers[lp] + numbers[rp]
            if tempSum == target:
                return [lp+1, rp+1]
            if tempSum < target:
                lp += 1
            else:
                rp -= 1


print(Solution.twoSum("", [2, 7, 11, 15], 9))
