# LeetCode:-1598 Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for i in logs:
            if i == './':
                continue
            elif i == '../':
                if st:
                    st.pop()
            else:
                st.append(i)
        return len(st)