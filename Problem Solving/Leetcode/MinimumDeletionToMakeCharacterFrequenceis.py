def freq(s):
    res = {}
    for key in s :
        res[key] = res.get(key, 0) + 1
    print(res)
    print(sorted(res.items(), reverse=True, key=lambda x: x[1]))
    count = 0
    resulting_dict = {}
    for k,v in sorted(res.items(), reverse=True, key=lambda x: x[1]):
        if res[k] not in resulting_dict.values():
            resulting_dict[k] = v
        else:
            resulting_dict[k] = v - 1
            count  = count + 1


    print(resulting_dict)
    print(count )


# s = "ceabaacb"
# s = "aaabbbcc"
# s = "aab"
s= "abcabc"
freq(s)



