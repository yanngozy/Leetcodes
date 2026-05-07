Class Solution {
public:
    static bool comparison(vector<int>& x, vector<int>& y){
        return x[0]<y[0];
    }
    int maxArea(vector<int>& height) {
        vector<vector<int>> arr;
        int n = height.size(),res = 0;
        // create a new vector whith height and position
        for(int i=0;i<n;i++){
            vector<int> new_elt = {height[i],i};
            arr.push_back(new_elt);
        }
       // sort in non decreasing order by the height
        sort(arr.begin(),arr.end(),comparison);
        int M = arr[n-1][1],m = arr[n-1][1];

        for(int i=n-2;i>=0;i--){
            int h = arr[i][0], j = arr[i][1];
            res = max(res,h*max(j-m,M-j));
            m = min(m,j);
            M = max(M,j);
        }
        return res;
    }
};
// Space complexity : O(n), Time complexity : O(nlog(n))
