# -*- coding: utf-8 -*-
import re
# python 中的正则表达式, 字符串使用 r'' 开头，则引号里面的字符串不需要转义

"""
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.
"""
# 匹配成功返回 match 对象，失败返回 None, 可以通过 if re.match(r'', text) 判断
print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}-\d{3,8}$', '010 - 12345'))

# 正则表达式切分字符
print('a b   c'.split(" "))  # 无法识别连续的字符
print(re.split(r'[\s]+', 'a b c  d'))
print(re.split(r'[\s\,]+', 'a b c,f'))
