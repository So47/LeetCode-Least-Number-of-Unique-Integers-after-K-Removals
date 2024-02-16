class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_counter = Counter(arr)
        sorted_counter = sorted(arr_counter.items(), key= lambda x:x[1])
        
        for key,value in sorted_counter:
            if k >= value:
                k -= value
                del arr_counter[key]
                
        return len(arr_counter)        

