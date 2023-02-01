#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        origin_letter = ord('a')
        for letter in key:
            if letter != ' ' and letter not in mapping:
                mapping[letter] = chr(origin_letter)
                origin_letter += 1
        decrypted_message = ''
        for letter in message:
            if letter != ' ':
                decrypted_message += mapping[letter]
            else:
                decrypted_message += ' '
        return decrypted_message
# @lc code=end

