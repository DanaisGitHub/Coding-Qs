class Solution:

    def isHappy(self, n: int) -> bool:
        hashset = set(int)
        infinite = False
        while True:
            n = self.split_and_square(n)
            if n == 1:
                return True
            if n in hashset:
                return False
            hashset.add(n)
        

    def split_and_square(self, n:int) ->int:
        total = 0
        while True:
            unit = n % 10
            tens = n // 10
            total += unit ** 2
            if tens < 10:
                total += tens ** 2
                break
            n //= 10
        return total

print(Solution.split_and_square("",1900000))