class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        str_list = [str(x) for x in digits]
        for i in range(len(str_list)):
            string+= str_list[i]
        total = int(string) +1
        return [int(digit) for digit in str(total)]