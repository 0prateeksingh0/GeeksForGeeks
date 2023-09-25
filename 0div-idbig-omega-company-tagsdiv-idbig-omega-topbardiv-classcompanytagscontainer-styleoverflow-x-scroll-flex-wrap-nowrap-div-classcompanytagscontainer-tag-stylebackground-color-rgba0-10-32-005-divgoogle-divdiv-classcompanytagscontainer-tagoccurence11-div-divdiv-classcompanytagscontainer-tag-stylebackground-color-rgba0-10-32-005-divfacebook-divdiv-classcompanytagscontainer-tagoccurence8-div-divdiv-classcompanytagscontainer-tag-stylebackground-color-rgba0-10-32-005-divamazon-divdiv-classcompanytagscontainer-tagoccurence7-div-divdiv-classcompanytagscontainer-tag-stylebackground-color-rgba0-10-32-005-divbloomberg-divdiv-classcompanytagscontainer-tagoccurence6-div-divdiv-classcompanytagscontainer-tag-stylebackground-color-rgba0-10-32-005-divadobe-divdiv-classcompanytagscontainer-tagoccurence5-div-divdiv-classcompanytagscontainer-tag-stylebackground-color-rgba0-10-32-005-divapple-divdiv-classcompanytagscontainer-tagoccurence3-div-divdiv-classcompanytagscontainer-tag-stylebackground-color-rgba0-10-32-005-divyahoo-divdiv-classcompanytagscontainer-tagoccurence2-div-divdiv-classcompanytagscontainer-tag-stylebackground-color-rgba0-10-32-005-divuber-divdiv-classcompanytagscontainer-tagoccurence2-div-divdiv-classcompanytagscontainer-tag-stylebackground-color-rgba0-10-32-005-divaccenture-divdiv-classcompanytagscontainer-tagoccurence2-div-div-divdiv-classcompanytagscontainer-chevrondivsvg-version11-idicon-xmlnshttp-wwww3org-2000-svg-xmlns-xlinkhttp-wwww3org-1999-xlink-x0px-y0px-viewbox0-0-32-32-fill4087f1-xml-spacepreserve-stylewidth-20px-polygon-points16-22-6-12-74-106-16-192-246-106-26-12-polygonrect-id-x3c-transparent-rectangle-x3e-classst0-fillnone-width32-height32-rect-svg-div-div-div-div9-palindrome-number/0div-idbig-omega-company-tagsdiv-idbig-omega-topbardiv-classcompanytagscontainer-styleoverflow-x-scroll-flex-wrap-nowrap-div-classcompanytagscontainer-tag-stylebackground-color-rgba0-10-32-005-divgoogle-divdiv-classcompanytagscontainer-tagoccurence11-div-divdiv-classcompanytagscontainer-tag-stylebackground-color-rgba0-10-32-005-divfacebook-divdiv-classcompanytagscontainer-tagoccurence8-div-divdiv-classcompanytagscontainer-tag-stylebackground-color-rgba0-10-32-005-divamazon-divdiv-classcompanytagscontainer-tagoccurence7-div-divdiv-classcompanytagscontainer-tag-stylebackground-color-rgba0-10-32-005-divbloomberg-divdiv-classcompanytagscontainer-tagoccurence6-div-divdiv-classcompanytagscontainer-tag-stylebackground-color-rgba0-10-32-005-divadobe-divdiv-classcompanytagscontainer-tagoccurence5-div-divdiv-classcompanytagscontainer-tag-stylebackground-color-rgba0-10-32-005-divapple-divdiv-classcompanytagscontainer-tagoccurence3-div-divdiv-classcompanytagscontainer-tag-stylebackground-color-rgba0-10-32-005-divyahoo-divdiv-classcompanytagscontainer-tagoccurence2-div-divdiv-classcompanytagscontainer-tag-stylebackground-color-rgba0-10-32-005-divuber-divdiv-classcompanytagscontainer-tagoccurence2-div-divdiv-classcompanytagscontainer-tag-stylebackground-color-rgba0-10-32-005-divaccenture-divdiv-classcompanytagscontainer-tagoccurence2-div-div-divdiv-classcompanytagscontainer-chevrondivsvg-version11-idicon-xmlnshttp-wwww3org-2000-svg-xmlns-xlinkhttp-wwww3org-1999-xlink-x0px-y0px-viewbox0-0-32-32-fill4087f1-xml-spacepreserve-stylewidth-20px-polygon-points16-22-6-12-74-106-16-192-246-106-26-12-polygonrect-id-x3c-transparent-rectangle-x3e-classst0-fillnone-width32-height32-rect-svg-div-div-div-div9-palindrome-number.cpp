class Solution {
public:
    bool isPalindrome(int x) {
        long long num = x, reversed = 0;
        while(x > 0){
            int digit = x % 10 ;
            reversed = (reversed * 10) + digit ; 
            x /= 10 ;
        }
        return num == reversed ;
    }
};