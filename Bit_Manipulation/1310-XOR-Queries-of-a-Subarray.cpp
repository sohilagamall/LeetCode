class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        
        vector<int> prefiXOR(n);
        prefiXOR[0] = arr[0];
        for(int i=1; i<n ; i++){
            prefiXOR[i] = prefiXOR[i-1] ^ arr[i];
        }

        vector<int> ans(queries.size());
        for(int i=0; i< queries.size(); i++){ // row index
            int l = queries[i][0];
            int r = queries[i][1];
            ans[i] = (l == 0) ? prefiXOR[r] : prefiXOR[r] ^ prefiXOR[l-1];
        }

        return ans;
    }
};