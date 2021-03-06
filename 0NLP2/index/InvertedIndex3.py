# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:InvertedIndex.py
# @time:2017/8/1 0001 13:48
#-------------------------------------------------------------------------------
# Name:        InvertedIndex
# Purpose:     倒排索引
# Created:     02/04/2013
# Copyright:   (c) neng 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
import string
#对199801.txt进行处理, 去除词性标注以、日期及一些杂质. (保留段落结构)
#输入:199801.txt
#输出:199801_new.txt
def pre_file(filename):
    print("读取语料库文件%r....."%filename)
    src_data = open(filename).read()
    # 去除词性标注、‘19980101-01-001-001’、杂质如‘[’、‘]nt’
    des_data =re.compile(r'(\/\w+)|(\d+\-\S+)|(\[)|(\]\S+)').sub('',src_data)
    des_filename = "../data/199801_new.txt"
    print("正在写入文件%r....."%des_filename)
    open(des_filename,'w').writelines(des_data)
    print("处理完成!")


#建立倒排索引
#输入:199801_new.txt
#输出:my_index.txt  格式(从0开始): word (段落号,段落中位置) ..
def create_inverted_index(filename):
    print("读取文件%r....."%filename)
    src_data = open(filename, encoding='utf-8').read()
    # 变量说明
    sub_list = [] #所有词的list,  用来查找去重等
    word = []     #词表文件
    result = {}   #输出结果 {单词:index}

    # 建立词表
    sp_data = src_data.split(',')
    sp_data = sp_data[1].split(';')
    set_data = set(sp_data)	#去重复
    word = list(set_data) #set转换成list, 否则不能索引

    src_list = src_data.split("\n") #分割成单段话vv
    extend_list = []
    # 建立索引
    for w in range(0,len(word)):
        index = []  # 记录段落及段落位置 [(段落号,位置),(段落号,位置)...]
        for i in range(0,len(src_list)):  #遍历所有段落
            print(src_list[i])
            extend_list = src_list[i].split(',')
            # index.append(extend_list[0])
            sub_list = extend_list[1].split(';')
            # print(sub_list)
            for j in range(0,len(sub_list)):  #遍历段落中所有单词
                # print(sub_list[j])
                if sub_list[j] == word[w]:
                    index.append((i,j))
            result[word[w]] = index

    des_filename = "extend_item.index"
    print("正在写入文件%r....."%des_filename)
    print(result)
    print(word)
    print(len(word))
    writefile = open(des_filename,'w')
    for k in result.keys():
        writefile.writelines(str(k)+str(result[k])+"\n")
    print("处理完成!")

#主函数
def main():
    #pre_file("data/199801.txt") #初步处理语料库, 得到199801_new.txt
    # 根据199801_new.txt建立索引, 得到myindex.txt(由于199801_new.txt太大, 建立索引时间太长, 因此只截取一部分放入199801_test.txt)
    create_inverted_index("extend_item.dict")

#运行
if __name__ == '__main__':
    main()