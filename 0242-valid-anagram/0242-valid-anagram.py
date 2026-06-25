class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False;
        news=sorted(s);
        newt=sorted(t);
        count=0;
        for i in range(len(news)):
           for j in range(i,i+1):
              if(news[i]==newt[j]):
                count+=1; 
        if(count==len(news)):
            return True;
        else:
            return False;               
 



       
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna