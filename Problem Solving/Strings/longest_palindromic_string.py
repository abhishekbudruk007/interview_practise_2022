def longestPalindrome(s):
    if len(s) == 1 or len(s) == 2:
        return s
    res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    print(res)
    res = [i for i in res if len(i) > 1 and i == i[::-1]]
    print(res)
    print(max(res))
    return max(res)

s= "abcabcbb"
print(longestPalindrome(s))