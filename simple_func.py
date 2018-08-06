# -*- coding:utf-8 -*-
# some simple functions

import re
import math
from collections import Counter


def compute_cosine(text_a, text_b):
    # 计算两英文文本的余弦相似度,返回的结果保留两位小数
    # 余弦计算相似度度量 http://blog.csdn.net/u012160689/article/details/15341303

    # 找单词及词频
    words1 = text_a.split(' ')
    words2 = text_b.split(' ')
    words1_dict = {}
    words2_dict = {}
    for word in words1:
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word != '' and word in words1_dict:
            num = words1_dict[word]
            words1_dict[word] = num + 1
        elif word != '':
            words1_dict[word] = 1
        else:
            continue
    for word in words2:
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word != '' and word in words2_dict:
            num = words2_dict[word]
            words2_dict[word] = num + 1
        elif word != '':
            words2_dict[word] = 1
        else:
            continue
    dic1 = sorted(words1_dict.iteritems(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words2_dict.iteritems(), key=lambda asd: asd[1], reverse=True)

    # 得到词向量
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])  # 向数组中添加元素
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            # print 'has_key', dic2[i][0]
            pass
        else:  # 合并
            words_key.append(dic2[i][0])

    vec1 = []
    vec2 = []
    for word in words_key:
        if word in words1_dict:
            vec1.append(words1_dict[word])
        else:
            vec1.append(0)
        if word in words2_dict:
            vec2.append(words2_dict[word])
        else:
            vec2.append(0)

    # 计算余弦相似度
    sum_up = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vec1)):
        sum_up += vec1[i] * vec2[i]
        sq1 += pow(vec1[i], 2)
        sq2 += pow(vec2[i], 2)
    try:
        result = round(float(sum_up) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0

    return result


def count_list(some_list, cond='all'):
    # 对一个list中出现的元素个数进行统计,cond为整数则表示选个数最多的cond个,最终返回一个dict
    if cond == 'all':
        return_dict = dict(Counter(some_list))
    elif isinstance(cond, int):
        return_dict = dict(Counter(some_list).most_common(cond))
    else:
        return 'please check your para!'
    return return_dict


if __name__ == '__main__':
    # text1 = "This game is one of the very best. games ive  played. the  ;pictures? " \
    #         "cant descripe the real graphics in the game."
    # text2 = "this game have/ is3 one of the very best. games ive  played. the  ;pictures? " \
    #         "cant descriPe now the real graphics in the game."
    # print(compute_cosine(text1, text2))

    # print(count_list(['a', 'b', 'c', 'b', 'a']))
    # print(count_list(['a', 'b', 'c', 'd', 'c', 'a', 'c'], 2))
    pass
