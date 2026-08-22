class Solution {
public:
    bool checkDivisibility(int n) {
        int num1= 0, num2=n ,sum =0, prod = 1;
        while(n > 0){
            num1 = n % 10;
            sum += num1;
            prod *= num1;
            n/=10;
        }
        if((num2 % (sum+prod) ) == 0) return true;
        else return false;
    }
};