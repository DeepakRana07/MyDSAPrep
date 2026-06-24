from collections import defaultdict;
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # count=0;

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #          if(abs(nums[i]-nums[j])==k):
        #               count+=1;
        # return count; 

        map=defaultdict(int);
        count=0;
   
        for i in range(len(nums)):
             number=nums[i];

             count+=map[number-k];
             count+=map[number+k];

             map[nums[i]]+=1; 
        return count;                       

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna