class Solution {
  public:
      bool is_integer(string s, set<char>& digits, bool sign){
          int i = 0, n = s.size();
          if ( (n==0) || ((n==1) & (s=="+" || s=="-") ) ) {return false;}
          if ( sign & (s[0]=='+'||s[0]=='-')) {i++;}
          while (i<n){
              if (digits.find(s[i])==digits.end()){return false;} // s[i] is not a digits
              i++;
          }
          return true;
      }
      bool is_decimal(string s, set<char>& digits, bool sign){
          int n = s.size();
          if (is_integer(s,digits,true)) { return true;} // s is an integer
          if ((n==0) || ((n==1) & (s=="+" || s=="-"))) {return false;} 
          if (s[0]=='+'||s[0]=='-') {s = s.substr(1);n--;} // optional sign
          if ((s[0]=='.') & (is_integer(s.substr(1),digits,false))){return true;}
          if ((s[n-1]=='.') & (is_integer(s.substr(0,n-1),digits,false))){return true;}
          for (int i=0;i<n;i++) {
              if (s[i]=='.'){
                  if (is_integer(s.substr(0,i),digits,false) & is_integer(s.substr(i+1),digits,false)){ return true;}
                  else { return false;}
              }
          }
          return false;
  
      }
      bool isNumber(string s) {
          set<char> digits = {'0','1','2','3','4','5','6','7','8','9'};
          int n = s.size();
          string left,right;
          if (is_decimal(s,digits,true)) {return true;} // s represents a decimal number
          for (int i=0;i<n;i++){
              if (s[i]=='e'|| s[i]=='E'){
                  left = s.substr(0,i);
                  right = s.substr(i+1);
                  if (is_decimal(left,digits,true) & is_integer(right,digits,true)){return true;}
                  else { return false;}
              }
          }
          return false;
          
      }
};
