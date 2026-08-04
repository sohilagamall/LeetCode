class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        for(int i=0; i<= n ;i++){
            int cnt = 0;
            int bit = i;
            while(bit){
                if( bit % 2 != 0)
                    cnt++;
                bit/=2;
            }
            ans[i] = cnt;
        }
        return ans;
    }
};