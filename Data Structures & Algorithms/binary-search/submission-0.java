class Solution {
    public int search(int[] nums, int target) {
        int mid = nums.length/2;
        int lower = 0;
        int upper = nums.length-1;

        while(lower <= upper){
            if(target > nums[mid]){
                lower = mid+1;
                mid = (lower+upper)/2;
                if(nums[mid] == target){
                    return (lower+upper)/2;
                }
            }
            else if(target < nums[mid]){
                upper = mid-1;
                mid = (lower+upper)/2;
                if(nums[mid] == target){
                    return (lower+upper)/2;
                }
            }
            else{
                return mid;
            }
        }
     
        return -1;
    }
}
