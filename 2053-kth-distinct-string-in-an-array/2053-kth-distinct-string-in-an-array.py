class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_map = Counter(arr)
        with_one_freq = []
        map_vals = list(arr_map.values())
        map_keys = list(arr_map.keys())
        for idx in range(len(map_vals)):
            if map_vals[idx] == 1: with_one_freq.append(map_keys[idx])
        return with_one_freq[k-1] if len(with_one_freq) >= k else ""               
                
        