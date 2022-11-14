class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int>merged = nums1;
        for(int i=0; i<nums2.size();i++)merged.push_back(nums2[i]);
        sort(merged.begin(),merged.end());
        if (merged.size() % 2 != 0) return static_cast<float>(merged[merged.size()/2]);
       
        else  return(static_cast<float>(merged[merged.size()/2]+merged[merged.size()/2 -1]))/static_cast<float>(2);
            
    }
};