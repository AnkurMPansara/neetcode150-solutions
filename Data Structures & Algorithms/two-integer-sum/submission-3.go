func twoSum(nums []int, target int) []int {
    counter := make(map[int][]int)
    for i, num := range(nums) {
        if _, ok := counter[num]; ok {
            counter[num] = append(counter[num], i);
        }
        counter[num] = []int{i}
    }
    for i, num := range(nums) {
        if idx, ok := counter[target-num]; ok {
            for _, j := range idx {
                if i != j {
                    return []int{i, j}
                }
            }
        }
    }
    return []int{}
}
