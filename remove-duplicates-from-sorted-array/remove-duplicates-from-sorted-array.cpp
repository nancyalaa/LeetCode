class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
    sort(nums.begin(), nums.end());
    nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
    return nums.size();
        
    }
};