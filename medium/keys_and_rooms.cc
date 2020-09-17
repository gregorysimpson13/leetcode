class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        if(rooms[0].empty()) return rooms.size() == 1;
        set<int> visited;
        visited.insert(0);
        queue<int> open; open.push(0);
        while(!open.empty()) {
            int room = open.front();
            for(auto &r : rooms[room]){
                if(visited.find(r) == visited.end()) {
                    // cout << rooms[0].size() << " " << r << endl;
                    visited.insert(r);
                    open.push(r);
                }
            }
            open.pop();
        }
        // cout << visited.size() << " " << rooms.size() << endl;
        return visited.size() == rooms.size();
    }
};