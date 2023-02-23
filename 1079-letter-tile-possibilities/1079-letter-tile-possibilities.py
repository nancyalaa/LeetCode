class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        output = set()
        for idx in range(1, len(tiles)+1):
            output.update(permutations(tiles, idx))
        return len(output)
        
        
        
        
            
        