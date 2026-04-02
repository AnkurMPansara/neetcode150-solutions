class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            anagrams.computeIfAbsent(String.valueOf(charArray), key -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(anagrams.values());
    }
}
