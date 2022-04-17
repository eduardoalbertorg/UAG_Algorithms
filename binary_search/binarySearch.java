class Solution {
    public int search(int[] nums, int target) {
        int leftPointer = 0;
        int rightPointer = nums.length - 1;
        while(leftPointer <= rightPointer) {
            int middleValue = (leftPointer + rightPointer) / 2;
            if (nums[middleValue] == target) {
                return middleValue;
            } else if (nums[middleValue] < target) {
                leftPointer++;
            } else if (nums[middleValue] > target) {
                rightPointer--;
            }
        }
        
        return -1;
    }
}