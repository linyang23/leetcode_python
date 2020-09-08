#
# @lc app=leetcode.cn id=482 lang=python
#
# [482] 密钥格式化
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # upper()，将小写字母劝募转为大写字母,replce模块将'-'去掉
        st = S.replace('-', '').upper()
        st_l = len(st)
        if not st_l:
            return ''
        b = st_l % K
        # 若st_l % K == 0，则说明刚好可以分成多段且每段都为K个字符
        if not b:
            # c即为出去第一段的段落数，因为第一段和其他段要求不同，所以分开操作
            c = st_l // K - 1
            b = K
        else:
            # 与上同理
            c = st_l // K
        # 找到第一段字符串
        s = st[:b]
        #加上后面的段
        while c != 0:
            s += '-' + st[b: b + K]
            b = b + K
            c -= 1
        return s
# @lc code=end
