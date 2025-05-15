class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        if ruleKey == "color":
            for t,c,n in items:
                if c == ruleValue:
                    count+=1
            return count
        elif ruleKey == "type":
            for t,c,n in items:
                if t == ruleValue:
                    count+=1
            return count
        elif ruleKey== "name":
            for t,c,n in items:
                if n == ruleValue:
                    count+=1
            return count
        

sol=Solution()
arr=[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
print(sol.countMatches(arr,"type","phone"))