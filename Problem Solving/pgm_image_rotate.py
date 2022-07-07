from pprint import pprint

with open("feep.ascii.pbm", "r", encoding="cp437") as f:
    lines = f.readlines()
    # print(lines)
    arr = []
    for line in lines[3:]:
        t = list(map(int, line.strip().split()))
        arr.append(t)

pprint(arr)