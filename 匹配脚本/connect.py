# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:19:19 2016

@author: Marsm
"""


import MySQLdb

def cmpr(e,v):
    score=0
    for i in range(0,3):
        if e[i*3+2] != 0:
            if e[i*3+2] >= v[i*3+1]:
                score+=1
            else:
                pass
        else:
            pass
        if e[i*3+3] != 0:
            if e[i*3+3] <= v[i*3+1]:
                score+=1
            else:
                pass
        else:
            pass
    you3quan2=[0,4,6,15,17,23,25]
    zi4fan3=[13,14]
    ying4biao1=[0,17]
#    dan1xiang4=[8,9,10]
    for ques in you3quan2:
        if ques in ying4biao1:
            if v[11][ques] <= e[11][ques+1]:
                score+=1
            else:
                pass
        else:
            if v[11][ques] <= e[11][ques+1]:
                score+=1
            else:
                pass
    for ques in zi4fan3:
        if v[11][ques] == e[11][ques]:
            score+=1
        else:
            pass
    if e[11][3] == u"4":
        score+=1
    else:
        if v[11][2] == e[11][3]:
            score+=1
        else:
            pass
    if e[11][30] == u"3":
        score+=1
    else:
        if v[11][29] == e[11][30]:
            score+=1
        else:
            pass
    if e[11][12] == u"4":
        score+=1
    else:
        if v[11][11] == e[11][12]:
            score+=1
        else:
            pass
    if v[11][19] == u"3":
        pass
    else:
        if e[11][20] == u"1":
            if e[11][19] == v[11][19]:
                score+=1
            else:
                pass
        elif e[11][20]== u"2":
            if e[11][19] != v[11][19]:
                score+=1
            else:
                pass
        else:
            score+=1
    if v[11][21] == u"3":
        pass
    else:
        if e[11][22] == u"1":
            if e[11][21] == v[11][21]:
                score+=1
            else:
                pass
        elif e[11][22]== u"2":
            if e[11][21] != v[11][21]:
                score+=1
            else:
                pass
        else:
            score+=1
    if e[11][28] == u"1":
        if e[11][27] == v[11][27]:
            score+=1
        else:
            pass
    else:
        score+=1
    return score

                  


conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='lilacwing',charset='utf8')
cursor=conn.cursor()


    
sq1="select * from boy"
cursor.execute(sq1)
res=cursor.fetchall()
ones_ans=[]
totlist=[]
gdict={u"大":0,u"研":4,u"博":6}
lvdict={u"一":1,u"二":2,u"三":3,u"四":4,u"五":5}

#建立标准比对表，现在内部并不含ones_os
for eachres in res:
    ones_ans.append(eachres[17])
    for i in range (0,3):
        try:
            if eachres[i][0] in gdict:#越界体现为用户无输入或者半正确输入以及较少输入
                if eachres[i][1] in lvdict:
                    ones_ans.append(gdict[eachres[i][0]]+lvdict[eachres[i][1]])
                else:
                    ones_ans.append(0)
            else:
                ones_ans.append(0)
        except:
            ones_ans.append(0)
            
    for i in range (3,9):
        try:
            temp=int(eachres[i][0:3])
            ones_ans.append(temp)
        except:
            ones_ans.append(0)
    ones_ans.append(eachres[9][0])
    ones_ans.append(eachres[9][1:])
    ones_ans.append(eachres[10])
    totlist.append(ones_ans)
    ones_ans=[]
    
conn.close()

#for e in totlist:
#    print len(e)


#print totlist
fres=[]#final result
for e in totlist:
    lt=[[0,0,0]]#list temp
    for v in totlist:
        if v[10] != e[10]:
            llt=len(lt)-1#list len temp
            score1=cmpr(e,v)
            score2=cmpr(v,e)
            sums=score1+score2
            ltt=[e[0],v[0],sums,v[12]]
            if sums >= lt[llt][len(ltt)-2]:
                lt.append(ltt)
#                print e[0]," and ",v[0]," is ",sums
            else:
                lt.insert(1,ltt)
    lltt=len(lt)
    for hollywt in range(lltt-10,lltt):
        fres.append(lt[hollywt])
#print fres


for preach in fres:
    fi=open("{0}.txt".format(preach[0]),"a")
    fi.write(u"{0}和{1}的得分是{2};\n".format(preach[0],preach[1],preach[2]))
    fi.write(u"{0}想对你说的话是: {1}\n".format(preach[1],preach[3]))
    fi.write("\n")

fi.close()

print "finished"
