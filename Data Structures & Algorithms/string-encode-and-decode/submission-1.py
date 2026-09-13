class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])
    def decode(self, s: str) -> List[str]:
        strs = []
        def safe_index(strs, target):
            return strs.index(target) if target in strs else None
        while(safe_index(s, "#")):
            strs.append(s[(safe_index(s, "#") + 1):(safe_index(s,"#") + 1 + int(s[:safe_index(s, "#")]))])
            s = s[(safe_index(s,"#") + 1 + int(s[:safe_index(s,"#")])):]
        return strs