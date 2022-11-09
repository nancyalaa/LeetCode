class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int>expected = heights;
        sort(expected.begin(),expected.end());
        int output = 0;
        for(int i=0; i<heights.size();i++){
            if(heights[i] != expected[i])output++;
        }
        return output;
    }
};