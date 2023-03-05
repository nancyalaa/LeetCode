func differenceOfSum(nums []int) int {
    elements_sum := 0
    digits_sum := 0
    for i := 0 ; i<len(nums); i++{
        elements_sum += nums[i]
        dig_sum := 0
        for nums[i] != 0{
            dig_sum += nums[i]%10
            nums[i] = nums[i]/10
        } 
        digits_sum += dig_sum
    }
    return elements_sum - digits_sum
}