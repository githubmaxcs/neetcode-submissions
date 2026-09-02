class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for s in strs:
            sorted_key = "".join(sorted(s))
            lookup.setdefault(sorted_key, []).append(s)
        return list(lookup.values())