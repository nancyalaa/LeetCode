class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int numberOfZeroes = 0;
        vector <int> temp;
        for(int i=0;i<nums.size();i++){
            
            if(nums[i] != 0){
                temp.push_back(nums[i]);
            }
            else{
                numberOfZeroes++;
            }
        }
        for(int i=0;i<numberOfZeroes;i++){
            temp.push_back(0);
        }
        nums = temp;
    }
};

