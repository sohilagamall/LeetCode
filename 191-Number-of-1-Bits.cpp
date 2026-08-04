class Solution {
public:
    int hammingWeight(int n) {
        int cnt = 0; 
        while(n){
            if(n % 2 != 0) cnt++;
            n/=2;
        }
        return cnt;
    }
};