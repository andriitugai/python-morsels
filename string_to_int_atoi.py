import re

class Solution(object):
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    _ptrn = re.compile(r'^[ ]*[+-]?[0-9]+')

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        result = 0
        sign = 1

        idx = 0
        while idx < len(str) and str[idx] == ' ':
            idx += 1

        if idx < len(str):
            if str[idx] == '-':
                sign = -1
                idx += 1
            elif str[idx] == '+':
                idx += 1

        while idx < len(str):
            if '0' <= str[idx] <= '9':
                result = result * 10 + int(str[idx])
            else:
                break
            idx += 1

        result *= sign

        return min(max(result, self.INT_MIN), self.INT_MAX)

    def myAtoi_2(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = self._ptrn.search(str)
        if result:
            return min(max(int(result.group()), self.INT_MIN), self.INT_MAX)

        return 0




def main():
    print(Solution().myAtoi(' '))
    print(Solution().myAtoi('42'))
    print(Solution().myAtoi('   42'))
    print(Solution().myAtoi('4193 with words'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('-91283472332'))

    print(Solution().myAtoi_2(' '))
    print(Solution().myAtoi_2('42'))
    print(Solution().myAtoi_2('   42'))
    print(Solution().myAtoi_2('4193 with words'))
    print(Solution().myAtoi_2('words and 987'))
    print(Solution().myAtoi_2('-91283472332'))


if __name__ == '__main__':
    main()

