class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
        if(nums.size()>=3)return nums[nums.size()-3];
        return nums[nums.size()-1];
    }
};