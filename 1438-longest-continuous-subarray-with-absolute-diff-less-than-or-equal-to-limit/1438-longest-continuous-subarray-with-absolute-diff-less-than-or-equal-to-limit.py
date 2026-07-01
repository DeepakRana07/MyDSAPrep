class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # currentmax=0;
        # currentmin=0;
        # maxlength=1;

        # for i in range(len(nums)):
        #     currentmax=nums[i];
        #     currentmin=nums[i];

        #     for j in range(i,len(nums)):

        #         currentmax=max(currentmax,nums[j]);
        #         currentmin=min(currentmin,nums[j]);

        #         if(currentmax- currentmin<=limit):
        
        #             maxlength=max(maxlength,j-i+1);
       
        # return maxlength;

        window=SortedList();

        i=0;
        ans=0;

        for j in range(len(nums)):
            window.add(nums[j]);
            while(window[-1]-window[0]>limit):
                window.remove(nums[i]);
                i+=1;
            ans=max(ans,j-i+1);

        return ans;        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna