class Solution {
public:
    string largestTimeFromDigits(vector<int>& A) {
        initialize(A);
        result[2] = ':';
        for(int d_0=2; d_0>=0; d_0--){
            if(!hasDigit(d_0)) continue;
            int d_1=d_0==2?3:9;
            insertNum(d_0, 0);
            for(d_1; d_1>=0; d_1--) {
                if(!hasDigit(d_1)) continue;
                insertNum(d_1, 1);
                for(int d_2=5; d_2>=0; d_2--) {
                    if(!hasDigit(d_2)) continue;
                    insertNum(d_2, 3);
                    for(int d_3=9; d_3>=0; d_3--) {
                        if(hasDigit(d_3)){
                            insertNum(d_3, 4);
                            return string(result);
                        }
                    }
                }
                removeNum(d_1);
            }
            removeNum(d_0);
        }
        return "";
    }
    void initialize(vector<int>& A){
        for(int i=0; i<A.size(); i++){
            if(digits.find(A[i]) == digits.end()){
                digits[A[i]] = 0;
            }
            digits[A[i]]++;
        }
    }
    bool hasDigit(int num){
        return digits.find(num) != digits.end() && digits[num] > 0;
    }
    void insertNum(int num, int pos) {
        result[pos] = '0' + num;
        digits[num]--;
    }
    void removeNum(int num) {
        digits[num]++;
    }
private:
    map<int,int> digits;
    char result[5];
};