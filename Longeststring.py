class solution:
     def longestsubstring(self, s: str):
          charset = set()
          
          l =0
          result =0
          for r in range (len(s)):
               while s[r] in charset:
                    charset.remove(s[l])
                    l+=1
               charset.add(s[r])
               result =max(result, r-l+1)
          return result
                    