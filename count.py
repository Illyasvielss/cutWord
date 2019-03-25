# -*- coding: utf-8 -*-
# coding=utf-8

# import collections
# 字频统计
# # 读取文本文件，把所有的汉字拆成一个list
# f = open("C:\\Users\\15323\\PycharmProjects\\cutWord\\result2\\result_test1.txt", 'r', encoding='utf8')  # 打开文件，并读取要处理的大段文字
# txt1 = f.read()
#
# mylist = list(txt1)
# mycount = collections.Counter(mylist)
# for key, val in mycount.most_common(10):  # 有序（返回前10个）
#     print(key, val)

import jieba
import jieba.analyse

from collections import Counter
# text = ''
# #jieba.load_userdict("jieba_dict.txt")  # 用户自定义词典 （用户可以自己在这个文本文件中，写好自定制词汇）
# f = open('C:\\Users\\15323\\PycharmProjects\\cutWord\\result2\\result_test1.txt', 'r', encoding='utf8')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
# lines = f.readlines()
# for line in lines:
#     text += line
#
# # seg_list = jieba.cut(text, cut_all=False)  #精确模式（默认是精确模式）
# seg_list = jieba.cut(text)  # 精确模式（默认是精确模式）
# print("[精确模式]: ", "/ ".join(seg_list))
#
# # seg_list2 = jieba.cut(text, cut_all=True)    #全模式
# # print("[全模式]: ", "/ ".join(seg_list2))
#
# # seg_list3 = jieba.cut_for_search(text)    #搜索引擎模式
# # print("[搜索引擎模式]: ","/ ".join(seg_list3))
#
# tags = jieba.analyse.extract_tags(text, topK=5)
# print("关键词:    ", " / ".join(tags))

# ! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
from collections import Counter


def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(50):
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))
    alreadyin = {}.fromkeys([line.strip() for line in codecs.open('ik_dictionary.txt', encoding='UTF-8')])
    print('新词')
    for (k, v) in c.most_common(100):
        if k not in alreadyin:
           print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))

if __name__ == '__main__':
    with codecs.open('C:\\Users\\15323\\PycharmProjects\\cutWord\\result2\\result_test1.txt', 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)