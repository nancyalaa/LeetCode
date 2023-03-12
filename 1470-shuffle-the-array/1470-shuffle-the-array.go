func shuffle(nums []int, n int) []int {
    first_slice := nums[:n]
    second_slice := nums[n:]
    output := []int{}
    for i := 0 ; i < len(first_slice); i++{
        output = append(output, first_slice[i], second_slice[i])
    }
    return output
}