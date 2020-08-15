#
# @lc app=leetcode.cn id=299 lang=python
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #定义公牛数和奶牛数
        Bulls = Cows = 0
        #定义用于查找的列表
        lookup = []
        #将secret数存入该列表
        for i in range(len(secret)):
            #若位置对应，则公牛数加一
            if secret[i] == guess[i]:
                Bulls += 1
            #已经确实是公牛数的数字用else避免算入奶牛数
            else:
                lookup.append(secret[i])
        print(lookup)
        #找到出现的数，并用不是公牛数的位置去查找
        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i]:
                Cows += 1
                lookup.remove(guess[i])
        #按字符串输出
        return str(Bulls) + 'A' + str(Cows) + 'B'        
# @lc code=end

