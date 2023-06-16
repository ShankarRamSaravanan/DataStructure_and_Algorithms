import collections


def anagram(strs):

    res = collections.defaultdict(list)

    print(res.values)
    for i in strs:
        count = [0] * 26
        for j in i:

            count[ord(j) - ord('a')] += 1

            print(res[tuple(count)])

        res[tuple(count)].append(i)

    return res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(strs)
