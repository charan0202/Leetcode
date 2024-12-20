class solution:
     def palindrome_string(self, s: str) -> str:
          result = ""
          result_length = 0
          
          for i in range (len(s)):
               l , r = i , i 
               while l >= 0 and r < len(s) and s[l] == s[r]:
                    if(r - l + 1) > result_length:
                         res = s[r:l+1]
                         result_length = r - l + 1 
                    
                    l-=1 
                    r+=1 
               
               l , r = i , i + 1
               while l >= 0 and r < len(s) and s[l] == s[r]:
                    if(r - l + 1) > result_length:
                         res = s[r:l+1]
                         result_length = r - l + 1 
                         
                    l-=1 
                    r+=1 
          return result
               