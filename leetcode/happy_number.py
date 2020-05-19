# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 8^2 + 2^2 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

def happy_number(num):
    def do_calc(n):
        result = 0
        while n > 0:
            result += (n % 10)**2
            n = n // 10

        return result

    counts = set()
    while True:
        count = do_calc(num)
        if count == 1:
            return True
        else:
            if count in counts:
                return False
            else:
                counts.add(count)
                num = count

    return 0


def main():
    num = 20
    print(happy_number(num))
    num = 19
    print(happy_number(num))


if __name__ == '__main__':
    main()
