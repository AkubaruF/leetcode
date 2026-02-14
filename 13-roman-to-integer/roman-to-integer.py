class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        sum = 0
        skip = False
        for i in range(len(s)):
            if skip:
                skip = False
                continue

            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                sum += roman[s[i+1]] - roman[s[i]]
                skip = True
            else:
                sum += roman[s[i]]
        return sum