class Solution:
    def isValid(self, s: str) -> bool:
        se = {")": "(", "}": "{", "]": "["}
        st = []
        for i in s:
            if i in se:
                e = st.pop() if st else "#"
                if se[i] != e:
                    return False
            else:
                st.append(i)
        return not st