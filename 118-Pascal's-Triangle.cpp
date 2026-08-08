class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> dp;

        for(int i=0; i<numRows; ++i){
            vector<int> row;
            row.push_back(1);
            for(int j=1; j<i ; ++j){
                row.push_back(dp[i-1][j-1] + dp[i-1][j]);
            }
            if(i > 0){
                row.push_back(1);
            }
            dp.push_back(row);
        }
        return dp;
    }
};