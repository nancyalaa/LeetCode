class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int>output;
        for(int i=1;i<arr.size();i++){
             
            output.push_back(*max_element(arr.begin()+i, arr.end()));
            
        }
        output.push_back(-1);
        return output;
    }
};