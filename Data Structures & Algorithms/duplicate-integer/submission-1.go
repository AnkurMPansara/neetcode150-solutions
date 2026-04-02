func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool, len(nums))
    for _, num := range nums {
        if _, ok := seen[num]; ok {
            return true
        }
        seen[num] = true
    }
    return false
}
