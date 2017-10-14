public class MaxSumSubarray {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE, sum = 0;
        
        for(int num : nums){
        	
            sum += num;
            if(sum > maxSum){
                maxSum = sum;
            }
            
            if(sum <= 0){
                sum = 0;
            }
        }
        return maxSum;
    }
}