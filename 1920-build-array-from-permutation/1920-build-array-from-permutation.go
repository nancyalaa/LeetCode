func buildArray(nums []int) []int {
    output := []int{}
    for i:=0; i<len(nums);i++{
        output = append(output, nums[nums[i]])
    }
    return output
}