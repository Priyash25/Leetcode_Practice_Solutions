class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans=0
        g.sort()
        s.sort()
        for i in s:
            child_present=[x for x in g if x<=i]
            if child_present:
                ans+=1
                g.remove(min(child_present))
            else:
                continue
        return ans

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        child=0
        cookie=0

        while child < len(g) and cookie < len(s):
            if g[child]<=s[cookie]:
                child+=1
            cookie+=1
        return child
