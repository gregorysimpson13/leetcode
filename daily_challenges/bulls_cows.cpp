class Solution {
public:
    string getHint(string secret, string guess) {
        map<char,int> secret_map, guess_map;
        int a = 0, b = 0;
        for(int i=0; i<secret.length(); i++){
            if(secret[i] == guess[i]){a++;}
            else{
                add_to_map(secret[i], secret_map);
                add_to_map(guess[i], guess_map);
            }
        }
        for(map<char,int>::iterator it=secret_map.begin(); it!=secret_map.end(); ++it){
            if(guess_map.find(it->first) == guess_map.end()) continue;
            b += min(it->second, guess_map[it->first]);
        }
        stringstream ss;
        ss << a << "A" << b << "B";
        return ss.str();
    }
private:
    void add_to_map(char c, map<char,int>& m){
        if(m.find(c) == m.end()){m[c] = 1;}
        else{m[c]++;}
    }
};