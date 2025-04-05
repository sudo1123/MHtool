j1=0
#保存函数（存在程序所在处）
import json
with open("number saved.json","r") as jj:
    tt=json.load(jj)
with open("mode.json","r") as qu:
    qi=json.load(qu)
    if qi=="0":
        box=int(input("您是否需要保存计算结果？（是按1，不是按2，按2将永久禁用计算结果保存）"))
        if box==1:
            with open("mode.json","w") as z:
                json.dump("1",z)
        if box==2:
            with open("mode.json","w") as z:
                json.dump("2",z)
        quququ=input("程序需重启，输入任意键重启")
        exit()
    if qi=="1":
        def saved(quqi,p):
            c12=str(input("您是否要保存结果？（是按1，不是按2）"))
            if c12=="1":
                ww=[]
                if tt=="0":
                    with open("reply.json","w") as z:
                        json.dump("*",z)
                    with open("number saved.json","w") as zz:
                        json.dump("1",zz)
                with open("reply.json","r") as g:
                    ee=json.load(g)
                    ww.append(ee)
                    ww.append(quqi)
                    ww.append(p)
                with open("reply.json","w") as f:
                    json.dump(ww,f)
                print("完成，已存至reply.json")
            if c12=="2":
                z=1
    if qi=="2":
        def saved(quqi,p):
            q=quqi
            q=p
            q=0
def history(quqi):
    ww=[]
    with open("history.json","r") as g:
        ee=json.load(g)
        ww.append(ee)
        ww.append(quqi)
    with open("history.json","w") as f:
        json.dump(ww,f)
history("turn on*")
print("hello")
#前端        
while True:
    import string
    import math
    if j1>0:
        a = input("请输入需要选择的功能的代码(输入exit关闭程序，输入help查看使用指南)")
    else:
        a = input("请输入需要选择的功能的代码(0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率,8是找零程序（贪心算法），9是统计，10是绘制函数图像，11是考试成绩数据整理，输入clock启动计时器，输入exit关闭程序，输入help查看使用指南,输入rr查看历史计算结果，输入cr清空历史计算结果，输入history查看操作历史，输入ch清空操作历史）")
        j1+=1
    #生成质数表
    if a=="0":
        b = int(input("请输入您要生成的质数表范围：（注意要加一）:"))
        def prime(b):
            number = (b)
            if number == 1:
                print(number, "不是质数")
                return False
            for c in range(2, int(math.sqrt(number))+1):
                if number % c == 0:
                    return False
            return True

        d = []
        for e in range(2, b):
            if prime(e):
                d.append(e)
        print("共找到", len(d), "个质数")
        print(d)
        saved("the reply from fuction 0",d)
        history("0*")
    #翻倍运算
    if a=="1":
        e = int(input("请输入您需要翻倍的数值"))
        f = int(input("请输入您需要翻倍的次数"))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print("现在数值为", j, ",这是第", h, "次翻倍.")
            w=j
        saved("the reply from fuction 1",w)
        history("1*")
    #计算算数平方根
    if a=="2":
        x = float(input("请输入需要求算术平方根的数："))
        b = 0
        z = 0
        v = z+1
        k = 1
        w = 0
        d = int(input("需要的精确度（输入的整数数值越高计算无限小数型的算术平方根数值越精确，如果不能确定是否为无限不循环小数，推荐输入10000）："))
        u = []
        e = 0
        pre=0
        for y in range(d):
            for i in range(10):
                b = v*v
                if b < x:
                    v = v+k
                    d = d+1000
                if b > x:
                    print("这个数的算术平方根是无限小数，现在精确到：", v)
                    w = v
                    v = v/10
                    k = k/10
                if b == x:
                    u.append(v)
                    e = len(u)
                    for q in range(e-1):
                        u.pop()
            if u == []:
                w22=90
            else:
                pre = u[0]
                print("这个数的算术平方根是：", pre)
        saved("the reply from fuction 2",pre)
        saved("genhao",x)
        history("2*")
    #计算圆周率
    if a =="3":
        c=int(input("请选择使用代数法还是几何法（代数法按1，几何法按2,蒙特卡洛法按3）"))
        if c==1:#代数法
            a=0
            b=1
            d=0
            e=int(input("请输入您需要的范围（10的倍数）"))
            for c in range(1,e):
                d=2*c-1
                if b==1:
                    a+=1/d
                else:
                    a-=1/d
                print("圆周率约等于",4*a)
                b=b*-1
                d=4*a
            saved("the reply from fuction 3",d)
            history("3(1)*")
        if c==2:#几何法
            import turtle
            myPen = turtle.Pen()
            Pos =0
            o = 0
            k = 0
            c = 0
            j = int(input("请输入需要的精度（10的倍数）"))
            r = 360*j
            py = r/2
            myPen.speed(0)
            for i in range(int(py)):
                print(i+1)
                myPen.forward(0.0001)
                myPen.left(1/j)
                o = o+1
                if o == r/2:
                    Pos=(myPen.pos())
            Pos1=str(Pos)
            Pos2=Pos1.split("(")
            Pos3=Pos2[1].split(")")
            Pos4=Pos3[0].split(",")
            Pos5=Pos4[1]
            m = float(Pos5)
            q1=r/10000
            t = q1/m
            print("圆周率约等于",t)
            saved("the reply from fuction 3",t)
            history("3(2)*")
        if c==3:#蒙特卡洛法
            import random
            import math
            d=0
            e=int(input("请输入取点数量"))
            print("请稍等")
            for i in range(e):
                a=random.uniform(0,1)
                b=random.uniform(0,1)
                c=math.sqrt(a*a+b*b)
                if c<1:
                    d=d+1
            print("圆周率约为",d/e*4)
            qu=d/e*4
            saved("the reply from fuction 3",qu)
            history("3(3)*")
    #求n次方
    if a=="4":
        s = int(input("请输入底数"))
        h = int(input("请输入指数"))
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            s=s*w   
        print("结果是", s)
        saved("the reply from fuction 4",s)
        ll=ll+1
        saved("^",h)
        saved("=",s)
        history("4*")
    #四则运算
    if a=="5":
        s = int(input("请输入您选择的模式（1代表加法运算,2代表减法运算,3代表除法运算,4代表乘法运算）"))
        if s == 1:
            b = int(input("请输入一个加数"))
            c = int(input("请输入另一个加数"))
            d = c+b
            print("结果是", d)
            ee=0
            saved("the reply from fuction 5[1]",b)
            ee=ee+1
            saved("+",c)
            saved("=",d)
            ee=0
            history("5(1)*")
        if s == 2:
            e = int(input("请输入被减数"))
            f = int(input("请输入减数"))
            g = e-f
            print("结果是", g)
            ff=0
            saved("the reply from fuction 5[2]",e)
            ff=ff+1
            saved("-",f)
            saved("=",g)
            ff=0
            history("5(2)*")
        if s == 3:
            h = int(input("请输入被除数"))
            j = int(input("请输入除数"))
            if j == 0:
                print("您输入的除数是0，0不能作为除数")
            else:
                k = h/j
                print("结果是", k)
            jj=0
            saved("the reply from fuction 5[3]",h)
            jj=jj+1
            saved("/",j)
            saved("=",k)
            jj=0
            history("5(3)*")
        if s == 4:
            l = int(input("请输入一个乘数"))
            m = int(input("请输入另一个乘数"))
            n = l*m
            print("结果是", n)
            gg=0
            saved("the reply from fuction 5[4]",l)
            gg=gg+1
            saved("*",m)
            saved("=",n)
            history("5(4)*")
    #生成斐波那契数列
    if a =="6":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        print(d)
        saved("the reply from fuction 6",d)
        history("6*")
    #计算黄金分割率
    if a =="7":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        s=len(d)
        v=d[s-2]/d[s-1]
        print("黄金分割率约为",v)
        saved("the reply from fuction 7",v)
        history("7*")
    #贪心算法
    if a=="8":
        target= Input=float(input("请输入您需要找的钱数：（人民币）"))
        money=[100,50,20,10,5,1,0.5,0.1]
        number=[0,0,0,0,0,0,0,0,0]
        saved1=[]

        for i in range(8):
            number[i]=target//money[i]
            target=target%money[i]
        for i in range(8):
            print(money[i],"元的张数为",number[i],"张")
            saved1.append(money[i])
            saved1.append(number[i])
        saved("the reply from fuction 8",saved1)
        history("8*")
    if a=="9":
        b=int(input("输入1求平均值，输入2求加权平均值，输入3求方差，输入4求标准差"))
        if b==1:
            c=[]
            d=[]
            f=2
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    f=0
                    c.pop()
            for i in range(len(c)):
                d.append(float(c[i]))
            w1=0
            w2=0
            for w3 in range(len(d)):
                w1=d[i]
                w2=w2+w1
            w4=w2/len(d)
            print(d,"的平均值为",w4)
            saved("the reply from fuction9(1)",w4)
            history("9(1)*")
        if b==2:
            c=[]
            d=[]
            f=2
            o=2
            w1=[]
            w4=[]
            w6=[]
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    c.pop()
                    f=0
            while 0<o:
                w2=input("请输入权（一次一个，输入完毕输f)")
                w1.append(w2)
                if w2=="f":
                    w1.pop()
                    o=0
            for w3 in range(len(c)):
                w4.append(float(w1[w3]))
            for w5 in range(len(w1)):
                w6.append(float(w1[w5]))
            w11=0
            w12=0
            w14=0
            for w7 in range(len(w1)):
                w8=w4[w7]
                w9=w6[w7]
                w10=w8*w9
                w11=w11+w10
                w12=w12+w9
                w14=w11/w12
            print("加权平均数为",w14)
            saved("the reply from fuction9(2)",w14)
            history("9(2)*")
        if b==3:
             c=[]
             d=[]
             f=2
             while 0<f:
                 e=input("请输入数据（一次一个，输入完毕输f)")
                 c.append(e)
                 if e=="f":
                     f=0
                     c.pop()
             for i in range(len(c)):
                 d.append(float(c[i]))
             w1=0
             w2=0
             for w3 in range(len(d)):
                 w1=d[i]
                 w2=w2+w1
             w4=w2/len(d)
             w6=0
             for w7 in range(len(d)):
                 w8=d[w7]-w4
                 w8=w8*w8
                 w6=w6+w8
             w9=w6/len(d)
             print("方差为",w9)
             saved("the reply from fuction9(3)",w9)
             history("9(3)*")
        if b==4:
            c=[]
            d=[]
            f=2
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    f=0
                    c.pop()
            for i in range(len(c)):
                d.append(float(c[i]))
            w1=0
            w2=0
            for w3 in range(len(d)):
                w1=d[w3]
                w2=w2+w1
            w4=w2/len(d)
            w6=0
            for w7 in range(len(d)):
                w8=d[w7]-w4
                w8=w8*w8
                w6=w6+w8
            w9=w6/len(d)
            x = w9
            b = 0
            z = 0
            v = z+1
            k = 1
            w = 0
            d = int(input("需要的精确度（输入的整数数值,越高计算越精确"))
            u = []
            e = 0
            pre=0
            for y in range(d):
                for i in range(10):
                    b = v*v
                    if b < x:
                        v = v+k
                        d = d+1000
                    if b > x:
                        print("标准差是无限小数，现在精确到：", v)
                        w = v
                        v = v/10
                        k = k/10
                    if b == x:
                        u.append(v)
                        e = len(u)
                        for q in range(e-1):
                            u.pop()
                if u == []:
                    print()
                else:
                    pre = u[0]
                    print("标准差是", pre)
            saved("the reply from fuction9(4)",pre)
            history("9(4)")
#绘制函数图像
    if a=="10":
        x=int(input("请输入选择模式（1为一次函数，2为二次函数）"))
        if x==1:
            import turtle
            myPen=turtle.Pen()
            b=float(input("请输入一次项系数"))
            c=float(input("请输入常数项"))
            e=0
            f=int(input("请输入取点数量"))
            j=float(input("请输入取点间距"))
            d=0-f/2
            for i in range(f):
                e=d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            myPen.penup()
            myPen.goto(0,0)
            myPen.pendown()
            myPen.write("0")
            myPen.goto(e,0)
            myPen.write("x")
            myPen.goto(0-e,0)
            myPen.penup()
            myPen.goto(0,0)
            myPen.pendown()
            myPen.goto(0,e)
            myPen.write("y")
            myPen.goto(0,0-e)
            turtle.done
            history("10(1)")
        if x==2:
            import turtle
            myPen=turtle.Pen()
            a=float(input("请输入二次项系数"))
            b=float(input("请输入一次项系数"))
            c=float(input("请输入常数项"))
            e=0
            f=int(input("请输入取点数量"))
            j=float(input("请输入取点间距"))
            d=0-f/2
            for i in range(f):
                e=d*d*a+d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            myPen.penup()
            myPen.goto(0,0)
            myPen.pendown()
            myPen.write("0")
            myPen.goto(e,0)
            myPen.write("x")
            myPen.goto(0-e,0)
            myPen.penup()
            myPen.goto(0,0)
            myPen.pendown()
            myPen.goto(0,e)
            myPen.write("y")
            myPen.goto(0,0-e)
            turtle.done
            history("10(2)")
#计时器
    if a=="clock":
        import time
        import math
        mine=0
        s=0
        start=time.time()
        t2=0
        t3=0
        mine=0
        s=0
        while True:
            end=time.time()
            t=end-start
            t2=t//1
            t3=t2//60
            if t3<1:
                if t2==1:
                    print(t2,"秒")
                if t2>1:
                    print(t2,"秒")
            if t3>1:
                mine=t3
                s=t2-60*t3
                print(mine,"分",s,"秒")
            if t3==1:
                mine=t3
                s=t2-60*t3
                print(mine,"分",s,"秒")
        history("clock")
#考试成绩数据整理
    if a=="11":
        s=2
        Sum=0
        average=0
        Max=0
        Min=0
        Dict={}
        while s>1:
            qu=input("请输入学生名")
            qi=input("请输入学生成绩,全部录入按f")
            if qi=="f":
                s=0
            else:
                Dict[qu]=float(qi)
        keys=[]
        z=[]
        x=0
        y=[]
        name=""
        Max=0
        Sum=0
        average=0
        for l in Dict:
            keys.append(l)
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]>Max:
                Max=z[i]
                x=i
                name=keys[x]
            y.append(i)
        print(name,"的成绩最高，为",Max,"分")
        Min=Max
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]<Min:
                Min=z[i]
                x=i
                name=keys[x]
        print(name,"的成绩最低，为",Min,"分")
        for l in Dict:
            Sum=Sum+Dict[l]
            average=Sum/len(keys)
        print("这个班的总分为",Sum,"分")
        print("这个班的平均分为",average,"分")
        saved("the reply from fuction 11","max")
        saved(Max,"min")
        saved(Min,"all")
        saved(Sum,"pingjun")
        saved(average," ")
        history("11")
#帮助
    if a=="help":
        print("请输入需要选择的功能的代码(0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率,8是找零程序（贪心算法），9是统计，10是绘制函数图像，11是考试成绩数据整理，输入clock启动计时器，输入exit关闭程序，输入help查看使用指南，输入rr查看历史计算结果，输入cr清空历史计算结果，输入history查看操作历史，输入ch清空操作历史)")
#读取计算结果
    if a=="rr":
        with open("reply.json","r") as gu:
            eue=json.load(gu)
            print(eue)
#清空计算结果
    if a=="cr":
        with open("reply.json","w") as gu:
            eue=json.dump("*",gu)
        print("已清空")
#终止运行
    if a =="exit":
        break
        history("turn off")
#读取操作历史
    if a=="history":
        with open("history.json","r") as yy:
            o1=json.load(yy)
        print(o1)
#清空操作历史
    if a=="ch":
        with open("history.json","w") as yy:
            json.dump("prepare done ",yy)
        print("已清空")
print("再见")
print("hope to see you again")
