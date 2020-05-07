class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = None
        for c in s:
            result += map[c]
            if ((c == 'V' or c == 'X') and prev == 'I') or \
                ((c == 'L' or c == 'C') and prev == 'X') or \
                ((c == 'D' or c == 'M') and prev == 'C') :
                result -= (2 * map[prev])
            prev = c
        return result


def main():
    print(Solution().romanToInt('XIV'))
    print(Solution().romanToInt('MCMXCIV'))


if __name__ == '__main__':
    main()


