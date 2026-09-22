class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen={
            ")":"(",
            "}":"{",
            "]":"["
        }
        st=[]
        for c in s:
            if c in closetoopen:
                if st and st[-1]==closetoopen[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True