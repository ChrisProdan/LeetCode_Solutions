class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1,len(s)+1):
            dp.insert(0,False)
            for word in wordDict:
                if len(word) <= i and dp[len(word)] == True and (word == s[-i:] or word == s[-i:-i+len(word)]):
                    dp[0] = True
                    break
        return dp[0]
        
        