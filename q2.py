def replace_char(str, k):
    re = set()       #定义一个集合 去重
    result = []

    for i, char in enumerate(str):
        #如果字符在集合中出现过则在结果中加入-
        if char in re:
            result.append('-')
        else:
            result.append(char)

        # 更新集合，只保留当前字符前的k个字符
        if i >= k:
            re.discard(str[i - k])#删除最前面的第i-k个字符
        re.add(char)
    return ''.join(result)


# 测试
input_str = "abcdefaxcqwertba"
k = 10
output_str = replace_char(input_str, k)
print(output_str)