class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> v;
        int n = intervals.size();
        int l=intervals[0][0], r=intervals[0][1];
        for(int i=1; i<n; i++){

            if(max(intervals[i-1][1], r) >= intervals[i][0]){
                r = max(r, intervals[i][1]);
            }
            else{
                v.push_back({l,r});
                l= intervals[i][0];
                r= intervals[i][1];
            }
        }
        v.push_back({l, r});
        return v;

    }
};