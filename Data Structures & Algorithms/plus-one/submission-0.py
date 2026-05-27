class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        d = []
        new = 0
        for i in digits:
            s += str(i)
        new = int (s)+1
        new_s = str(new)
        for i in new_s:
            d.append(int(i))
        return d


        