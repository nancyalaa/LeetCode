class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people)-1
        boats = 0
        while start <= end:
            boats += 1
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
        return boats