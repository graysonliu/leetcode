# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 这题主要练了一下map/reduce
        if not digits:
            return []

        digit_letter_dict = {'2': 'abc', '3': 'def',
                             '4': 'ghi', '5': 'jkl', '6': 'mno',
                             '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def digit_to_letter_one_by_one(current_list, index):
            new_list = []
            for l in current_list:
                for letter in digit_letter_dict[digits[index]]:
                    l[index] = letter
                    new_list.append(list(l))  # 浅拷贝（l只有一层所以不需要深拷贝），不能直接写l，否则还是指向l，l变化也会跟着变
                    # 对于list，要理解引用拷贝、浅拷贝、深拷贝
                    # python中的str是不可变对象，字符串的修改都是重新创建了一个新字符串
            return new_list

        from functools import reduce
        # reduce的关键字参数initial是初始元素，其作用详见文档
        ans = reduce(digit_to_letter_one_by_one, range(len(digits)), [list(digits)])
        # ans = reduce(digit_to_letter_one_by_one, range(len(digits)), initial=[list(digits)])
        """
        有意思的是，如果在调用reduce函数时写了"initial="会报错"reduce() takes no keyword arguments"
        如果去掉"initial="就可以运行，之前居然从来没遇到过
        网上的说法是，python很多内置函数的底层用C语言实现，C语言仅支持位置参数，不支持关键字参数
        很多内置函数即使文档中有关键字，调用时也不能写关键字
        """

        def list_to_str(l):
            return reduce(lambda a, b: a + b, iter(l))

        return list(map(list_to_str, ans))

    # leetcode上最快的solution
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = ['']
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for i in range(len(digits)):
            letters = phone[ord(digits[i]) - ord('2')]  # ord()将字符转为整型（ASCII码），反过来用chr()
            while len(res[0]) == i:
                cur = res.pop(0)  # pop()删除该位置的元素并返回该元素的值
                for c in letters:
                    res.append(cur + c)
        return res


if __name__ == '__main__':
    print(list(map(Solution().letterCombinations, ["23", "44"])))
