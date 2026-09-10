#LeetCode-682 Baseball Game 

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:
            if i == 'C':
                st.pop()
            elif i == 'D':
                st.append(st[-1]*2)
            elif i == '+':
                st.append(st[-1]+st[-2])
            else:
                st.append(int(i))
        s=0
        for i in st:
            s=s+i
        return s
        
