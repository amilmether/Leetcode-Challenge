class Solution(object):
    def capitalizeTitle(self, title):
        final=[]
        word=title.split()
        for i in word:
            if len(i) <= 2:
                final.append(i.lower())
                pass
            else:
                u=i.lower()
                final.append(u.capitalize())
        return ' '.join(final)
sol=Solution()
arr="First leTTeR of EACH Word"
print(sol.capitalizeTitle(arr))
        