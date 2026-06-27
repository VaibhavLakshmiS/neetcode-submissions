class Solution:

    def encode(self, strs: List[str]) -> str:
        str_new =""
        for i in strs:
            length = len(i)
            str_new+=str(length)+"#"+i
        return str_new


    def decode(self, s: str) -> List[str]:
        new = []
        i = 0

        while i < len(s):
            j = i

            # find the #
            while s[j] != "#":
                j += 1

            # length is before #
            length = int(s[i:j])

            # word starts after #
            word_start = j + 1
            word_end = word_start + length

            new.append(s[word_start:word_end])

            # jump to next encoded word
            i = word_end

        return new
        

               

        
