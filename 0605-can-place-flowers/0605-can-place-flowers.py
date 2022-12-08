class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        newFlowerbed = [0]
        newFlowerbed.extend(flowerbed)
        newFlowerbed.append(0)
        for i in range(1,len(newFlowerbed)-1):
            if newFlowerbed[i] == 0:
                if newFlowerbed[i-1] == 0 and newFlowerbed[i+1] == 0:
                    counter += 1
                    newFlowerbed[i] = 1
                    i += 1
                    
        if counter >= n:
            return True
        return False
            
                    
        
        