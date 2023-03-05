func numIdenticalPairs(nums []int) int {
    number_of_good_pairs := 0
    for i := 0 ; i <len(nums)-1 ; i++{
        for j := i+1 ; j <len(nums); j++{
            if nums[i] == nums[j]{
                number_of_good_pairs++
            }
        }
    }
    return number_of_good_pairs
}