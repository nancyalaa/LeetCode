class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    counter += 1
                    flowerbed[i] = 1
                    i += 1
                    
        if counter >= n:
            return True
        return False
            
                    
        
        