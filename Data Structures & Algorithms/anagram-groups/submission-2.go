func groupAnagrams(strs []string) [][]string {
    anagramGroups := make(map[string][]string)
    for _, str := range strs {
        bytes := []byte(str)
        sort.Slice(bytes, func(i, j int) bool {
            return bytes[i] < bytes[j]
        })
        key := string(bytes)
        anagramGroups[key] = append(anagramGroups[key], str)
    }
    result := make([][]string, 0)
    for _, grp := range anagramGroups {
        result = append(result, grp)
    }
    return result
}
