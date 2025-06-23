class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        keys={"type":0,"color":1,"name":2}
        return len([item for item in items if item[keys[ruleKey]] == ruleValue])
        

sol=Solution()
arr=[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
print(sol.countMatches(arr,"type","phone"))