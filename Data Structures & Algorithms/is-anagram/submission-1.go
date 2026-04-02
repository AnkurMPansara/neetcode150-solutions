func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counter := make(map[byte]int, 26)
	for i := range(len(s)) {
		counter[s[i]] += 1
		counter[t[i]] -= 1
	}
	for _, val := range(counter) {
		if val != 0 {
			return false
		}
	}
	return true
}
