class Solution {
  public:
      static bool validpuzzle(vector<vector<int>>& arr, int i, int j){
          for (int k=0;k<arr.size();k++){
              if(arr[k][1]==j){return false;}
              else if (arr[k][1]-j==arr[k][0]-i){return false;}
              else if (arr[k][1]-j==i-arr[k][0]){return false;}
          }
          return true;
      }
      vector<string> init(int n){
          vector<string> arr ;
          string tmp;
          for (int i=0;i<n;i++){
              tmp = "";
              for (int j=0;j<n;j++){
                  tmp +=".";
              }
              arr.push_back(tmp);
          }
          return arr;
      }
      void completepuzzle(vector<vector<int>>& arr, int i, int n,vector<vector<string>>& alls){
          if(i==n){
              vector<string> new_elt = init(n);
              int pos_x,pos_y;
              for (int k = 0; k < arr.size(); k++) {
                  pos_x = arr[k][0];
                  pos_y = arr[k][1];
                  new_elt[pos_x][pos_y] = 'Q';
              }
              alls.push_back(new_elt);
          }
          for (int j=0;j<n;j++){
              if (validpuzzle(arr,i,j)){
                  vector<vector<int>> new_arr = arr;
                  new_arr.push_back({i,j});
                  completepuzzle(new_arr,i+1,n,alls);
              }
          }
      }
      vector<vector<string>> solveNQueens(int n) {
          vector<vector<string>> alls;
          vector<vector<int>> arr;
          completepuzzle(arr,0,n,alls);
          return alls;
     
      }
};
// Time complexity O(n^n) ans spade complexity(n!)
