#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #创建两个hash表，字符串分词后存入列表
        lookup_1 = {}
        lookup_2 = {}
        wordList = str.split(' ', -1)   
        #若pattern的长度和分词后的列表长度不同，则判定不同
        if len(pattern) != len(wordList):
            return False
        for i in range(len(pattern)):
            #若lookup_1中有pattern[i]，即说明pattern字符中出现重复的情况
            if lookup_1.get(pattern[i]):
                #若这时wordList
                if lookup_1[pattern[i]] != wordList[i]:
                    return False
            #若lookup_1中无pattern[i]，即说明还没有重复的情况出现
            else:
                #这时候将pattern-wordList对存入lookup_1
                lookup_1[pattern[i]] = wordList[i]
                
            #与上面同理,用两个hash表的原因是防止只单向可查，比如abba->bbbb的情况
            if lookup_2.get(wordList[i]):
                if lookup_2[wordList[i]] != pattern[i]:
                    return False
            else:
                lookup_2[wordList[i]] = pattern[i]
        
        return True
        
# @lc code=end

