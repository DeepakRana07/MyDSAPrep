class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = SortedList()

        count=0;

        i=0;

        for j in range(len(nums)):
            window.add(nums[j]);

            while(window[-1]-window[0]>2):
                window.remove(nums[i]);
                i+=1;
            count+=j-i+1;
        return count;        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna