
def find_substring(s, n):
    if len(s) < 1:
        return 0
    result = []
    for i in range(n):
        for j in range(i+1,n+1):
            if s[i:j] not in result:
                result.append(s[i:j])
    return result


s = "pwwkew"
s = "abcabcbb"
n = len(s)

print(find_substring(s, n))