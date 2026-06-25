class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        map={};

        if(len(s)!=len(t)):
            return False;

        for i in range(len(s)):
            if(s[i] in map):
                map[s[i]]+=1;
            else:
                map[s[i]]=1;

        for i in range(len(t)):
            if(t[i] in map):
                map[t[i]]-=1;
            else:
                map[s[i]]=1;                

        for values in map.items():
            if(values[1]!=0):
                return False;       
        return True;



       
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna