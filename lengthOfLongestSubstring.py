import sys  
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ans=0
        i=0
        j=0
        dic={}
        while j<n:
            if dic.__contains__(s[j]):
                i=max(dic.get(s[j]),i)
            ans=max(ans, j - i + 1)
            dic[s[j]]= j + 1
            j=j+1
        return ans
        
        
    

#def stringToString(input):
 #   return input[1:-1].decode('string_escape')

def main():     
    line= sys.stdin.readline()
    line=line.strip('\n')           
    ret = Solution().lengthOfLongestSubstring(line)
    out = str(ret)
    print(out)
if __name__=="__main__":
    main()