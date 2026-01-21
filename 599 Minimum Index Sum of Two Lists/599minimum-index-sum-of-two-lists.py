class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        ans=[]
        for i in list1:
            for j in list2:
                if i==j:
                    s=list1.index(i)+list2.index(i)
                    d[i]=s
        mini=min(d.values())
        for i in d:
            if d[i]==mini:
                ans.append(i)
        return ans
