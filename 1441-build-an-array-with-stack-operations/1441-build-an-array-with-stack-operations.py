class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        res = []
        target_s = set(target)
        max_target = target[-1]
        for i in range(1, max_target + 1):
            res.append("Push")
            if i not in target_s:
                res.append("Pop")
        return res
