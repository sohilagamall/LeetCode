class Solution {
public:
    int xorOperation(int n, int start) {
        vector<int> v(n+1);
    
        for(int i=0 ; i < n ; ++i){
            v[i] = start + 2 * i;
        }

        vector<int> prefixXor(n);
        prefixXor[0] = v[0];
        for(int i = 1; i < n ; ++i){
            prefixXor[i] = prefixXor[i-1] ^ v[i];
        }
        return prefixXor[n-1];
    }
};