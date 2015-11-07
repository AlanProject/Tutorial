#-*- encoding: utf-8 -*-
#导入re正则模块
import re
#定义要运算的程式
s = {'number':'3+5/2+(8+3/(20+3/2-5)+4/(3-2)*3)'}

#################################            括号处理函数                 ##########################
def s_b(string):
    tage_number=string.count('(') #统计括号个数
    start_l=0 #定义最深层括号的起始位置的初始值
    start=0 #定义查询括号下标位的初始位置
    start_list = []    #定义开始括号的下标存储列表
    i = 0
    try:
        while i < tage_number:
            sd=string.index('(',start_l)
            start_list.append(sd)
            start_l = sd+1
            i += 1
        end = string.index(')') #最深层括弧的结尾下标（其实就是第一个"）" ）
        for i in start_list:  #根据括号下标找到和最深层“）”匹配的括号
            if i < end:
                start=i
        return string[start+1:end] #根据最深括号的下标取出括号内的表达式 并返回
    except ValueError:
        pass
#################################            运算符运算函数               ##########################
def cheng(b):
    sums = 1
    for i in re.split('[+,\-,/]',b):
        if i.find('*') >=0:
            su=i.split('*')
            #剔除列表中的空格
            while su.count('') > 0:
                su.remove('')
            sums = reduce(lambda x,y:int(x)*int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def chu(b):
    sums = 1
    for i in re.split('[*,\-,+]',b):
        #判断元素中是否包含'/' 如果包含则进行下一步计算
        if i.find('/') >=0:
            su=i.split('/')
            #剔除列表中的空格
            while su.count('') > 0:
                su.remove('')
            #计算除法
            sums = reduce(lambda x,y:int(x)/int(y),su)
            #将计算出的结果替换表达式中对应的部分
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def jia(b):
    sums = 0
    for i in re.split('[*,\-,/]',b):
        if i.find('+') >=0:
            su=i.split('+')
            #剔除列表中的空格
            while su.count('') > 0:
                su.remove('')
            sums = reduce(lambda x,y:int(x)+int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def jian(b):
    sums = 0
    for i in re.split('[+,*,/]',b):
        if i.find('-') >=0:
            su=i.split('-')
            #剔除列表中的空格
            while su.count('') > 0:
                su.remove('')
            sums = reduce(lambda x,y:int(x)-int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
#################################            计算函数调用运算符函数               ##########################
#定义加减乘除运算方法
def cal(j):
    if j.find('/') >=0:
        return chu(j)
    elif j.find('*') >=0:
        return cheng(j)
    elif j.find('+') >=0:
        return jia(j)
    elif j.find('-') >=0:
        return jian(j)
#通过判断括号的数量来判断计算式中是否还包含括号 如果包含则进行括号运算
#################################  利用括号处理函数 和 运算函数进行括号处理以及值运算 ##########################
while s['number'].count('(') >=1 :
    jieguo=s_b(s['number'])
    feng = cal(jieguo)
    s['number'] = s['number'].replace('('+str(feng)+')',str(feng))
#################################            计算括号处理之后的程式              ##########################
#剔除剩余字符串中所有运算符 通过len统计列表长度来判断是否还有运算符要进行运算
number_len=len(re.split('[+,\-,*,/]',s['number']))
while number_len > 1:
    if '/' in s['number']:
        chu(s['number'])
        number_len -=1
    elif '*' in s['number']:
        cheng(s['number'])
        number_len -=1
    elif '+' in s['number']:
        jia(s['number'])
        number_len -=1
    elif '-' in s['number']:
        jian(s['number'])
        number_len -=1
    else:
        break
#输出最终结果
print s['number']
