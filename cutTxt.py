# -*- coding:utf-8 -*-
import codecs
import os
import shutil
import jieba
import jieba.analyse


#Read file and cut
def read_file_cut():
    #create path
    path = "C:\\Users\\15323\\PycharmProjects\\cutWord\\bookydt\\article"
    respath = "C:\\Users\\15323\\PycharmProjects\\cutWord\\result2\\result_test"
    if os.path.isdir(respath):
        shutil.rmtree(respath, True)
    os.makedirs(respath)
    jieba.load_userdict('THUOCL_food.txt')#导入用户自定义词典
    num = 1
    while num<=2:
        name = "%d" % num
        print(name)
        fileName = path + str(name) + ".txt"
        resName = respath + str(name) + ".txt"
        source = codecs.open(fileName, 'r',encoding='UTF-8')
        if os.path.exists(resName):
            os.remove(resName)
        result = codecs.open(resName, 'w', encoding='utf-8')
        line = source.readline()
        line = line.rstrip('\n')
        stopwords = {}.fromkeys([line.strip() for line in codecs.open('chinese_stopword.txt', encoding='UTF-8')] ) # 停用词表
        while line!="":
            seglist = jieba.cut(line,cut_all=False)  #精确模式
            output='' #定义一个空字符串
            for segs in seglist:
                seg=segs.lower()            #英文字母小写
                if seg not in stopwords:    #去停用词
                    if len(seg)>1:          #去掉分词为1个字的结果
                        output += seg
                        output +='\n'
            print (output)
            result.write(output+'\r\n')
            line = source.readline()
        else:
            print ('End file: ' + str(num) )
            source.close()
            result.close()
        num = num + 1
    else:
        print ('End All')
if  __name__ == '__main__':
       read_file_cut()