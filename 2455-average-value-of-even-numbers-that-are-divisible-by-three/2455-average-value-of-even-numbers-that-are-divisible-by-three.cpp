class Solution {
public:
    int averageValue(vector<int>& nums) {
        vector<int>res;
        for(int i=0; i<nums.size();i++){
            if(nums[i]%6==0)
                res.push_back(nums[i]);
        }
         if(res.size()>0) return accumulate(res.begin(), res.end(),0)/res.size();
         return 0;

    }
       
};