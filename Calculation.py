#-*- encoding: utf-8 -*-
import re
s = {'number':'3*5/2-(8*3/(20+3/2-5)+4/(3-2)*3)'}
k_n=s['number'].count('(')
def s_b(string):
    tage_number=string.count('(') #统计括号个数
    i = 0
    start_l=0
    start=0
    start_list = []    #定义开始括号的下标存储列表
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

def cheng(b):
    sums = 1
    for i in re.split('[+,/,\-]',b):
        if i.find('*') >=0:
            su=i.split('*')
            sums = reduce(lambda x,y:int(x)*int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def chu(b):
    sums = 1
    for i in re.split('[*,\-,+]',b):
        if i.find('/') >=0:
            su=i.split('/')
            sums = reduce(lambda x,y:int(x)/int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def jia(b):
    sums = 0
    for i in re.split('[\-,*,/]',b):
        if i.find('+') >=0:
            su=i.split('+')
            sums = reduce(lambda x,y:int(x)+int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums
def jian(b):
    sums = 0
    for i in re.split('[+,*,/]',b):
        if i.find('\-') >=0:
            su=i.split('\-')
            sums = reduce(lambda x,y:int(x)-int(y),su)
            s['number'] = s['number'].replace(i,str(sums))
    return sums

def cal(j):
    if j.find('*') >=0:
        return cheng(j)
    elif j.find('/') >=0:
        return chu(j)
    elif j.find('+') >=0:
        return jia(j)
    elif j.find('\-') >=0:
        return jian(j)

while k_n >= 1:
    jieguo=s_b(s['number'])
    print jieguo
    feng = cal(jieguo)
    s['number'] = s['number'].replace('('+str(feng)+')',str(feng))
    print s['number']
    k_n -= 1

'''
number_len=len(re.split('[+,\-,*,/]',s['number']))

while number_len > 1:
    if '*' in s['number']:
        cheng(s['number'])
        number_len -=1
    elif '/' in s['number']:
        chu(s['number'])
        number_len -=1
    elif '+' in s['number']:
        jia(s['number'])
        number_len -=1
    elif '-' in s['number']:
        jian(s['number'])
        number_len -=1
    else:
        print s['number']
        break
print s['number']
'''
