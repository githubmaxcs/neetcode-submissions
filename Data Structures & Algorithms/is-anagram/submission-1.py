class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_lookup = {}
        t_lookup = {}
        for i in range(len(s)):
            s_lookup[s[i]] = s_lookup.get(s[i], 0) + 1
            t_lookup[t[i]] = t_lookup.get(t[i], 0) + 1
        return s_lookup == t_lookup