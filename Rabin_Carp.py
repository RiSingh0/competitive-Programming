class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        pas, cur = 0, 0
        l = len(needle)
        for i in range(len(needle)):
            pas += ord(needle[i])
            cur += ord(haystack[i])
        for i in range(len(needle),len(haystack)):
            if cur == pas:
                for j in range(len(needle)):
                    if needle[j] != haystack[i - (l-j)]:
                        break
                else:
                    return i-l
            cur -= ord(haystack[i-(l)])
            cur += ord(haystack[i])
        if cur  == pas:
            for j in range(len(needle)):
                if needle[j] != haystack[len(haystack) - (l-j)]:
                    break
            else:
                return len(haystack)-l
        return -1