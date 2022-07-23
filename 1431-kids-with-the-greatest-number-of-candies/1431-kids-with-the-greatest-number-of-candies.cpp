class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        

        int mx = candies[0];
        for(int i=0;i<candies.size();i++)
        {
            if(candies[i]>=mx)
                mx = candies[i];
        }
        for(int i=0; i<candies.size(); i++)
        {
            if(candies[i] + extraCandies >= mx)
                result.push_back(true);
            else
                result.push_back(false);
            
        
        }
       return result; 
    }
};