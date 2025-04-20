
# -*- coding: GBK -*-
import os
import json
Version="MHtool(8.8)"
#提高整数限制
import sys
from unicodedata import digit
sys.set_int_max_str_digits(1000000000)
#初始化函数
def init_files():
    # 初始化文件列表及默认值
    files = {
        "number saved.json": "0",          
        "mode.json": "0",                               
        "history.json": ["prepare done"],
        "reply.json": []
    }
    
    # 遍历创建文件
    for filename, default in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="GBK") as f:
                json.dump(default, f, ensure_ascii=False)
init_files()#初始化
#写入版本号函数
def version(version_code):
    INPUT="history"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("history.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("history.json","w") as f:
            json.dump(kk,f)
    INPUT="reply"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("reply.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("reply.json","w") as f:
            json.dump(kk,f)
version(Version)        
#保存函数（存在程序所在处）
import json
with open("mode.json","r") as qu:
    qi=json.load(qu)
    if qi=="0":
        box=int(input("您是否需要启用保存计算结果功能？（是按1，不是按2，按2将永久禁用计算结果保存）"))
        if box==1:
            with open("mode.json","w") as z:
                json.dump("1",z)
        if box==2:
            with open("mode.json","w") as z:
                json.dump("2",z)
        quququ=input("程序需要重启，键入任意键继续")
        exit()
    if qi == "1":
        def saved(quqi, p):
            c12 = str(input("您是否要保存结果？（是按1，不是按2）"))
            if c12 == "1":
                with open("number saved.json", "r") as zz:
                    tt = json.load(zz)
                # 确保reply.json内容为列表
                try:
                    with open("reply.json", "r") as g:
                        ee = json.load(g)
                    if not isinstance(ee, list):  # 若非列表，重置为空列表
                        ee = []
                except (json.JSONDecodeError, FileNotFoundError):
                    ee = []            
                ee.extend([quqi, p])  # 追加结果
                with open("reply.json", "w") as f:
                    json.dump(ee, f, ensure_ascii=False)
                print("完成，已存至reply.json")
                with open("number saved.json", "w") as zz:
                    json.dump(str(len(ee) // 2), zz)  # 更新保存次数
    if qi=="2":
        def saved(quqi,p):
            q=quqi
            q=p
            q=0#因为用户禁用了saved函数的功能，这里使saved函数被定义为“废”函数，这段代码没有实际意义
#文件导出函数
def export_file(filename):
    import json
    with open(filename+".json", "r") as f:
        history_data = json.load(f)
    with open(filename+".txt", "w", encoding="GBK") as f:
        for entry in history_data:
            f.write(str(entry) + "\n")
#历史记录函数
def history(quqi):
    ww=[]
    with open("history.json","r") as g:
        ee=json.load(g)
        ww.append(ee)
        ww.append(quqi)
    with open("history.json","w") as f:
        json.dump(ww,f)
#求平方根函数
def Squareroot(number,y):
    x = number
    precision = y
    v = 1.0  # 初始猜测值
    k = 1.0  # 初始步长
    current_best = 0.0  # 记录当前最佳近似值
    u=[]
    for _ in range(precision):
        for _ in range(10):  # 每轮尝试10次调整
            b = v * v
            if b < x:
                current_best = v  # 更新为当前下界
                v += k
            if b==x:
                u.append(v)
                e = len(u)
                for q in range(e-1):
                    u.pop()
            if b>x:
                v = current_best  # 回退到前一个有效值
                k /= 10          # 缩小步长
                v += k           # 继续逼近
                break            # 跳出内层循环
    if u==[]:
        return(current_best)
    else:
        pre = u[0]
        return(pre)
#质因数分解函数
def prime_factor(on):
    a = on
    factors = []
    if a == 1:
        factors.append(1)
        return(factors)
    if a <= 0:
        return("none")
    else:
        b = 101
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        Break = 0
        while Break == 0:
            for i in range(len(primes)):
                while a % primes[i] == 0:
                    factors.append(primes[i])
                    a = a // primes[i]  
                    if a == 1:
                        Break = 1
                        break
                if Break == 1:
                    break
            if Break == 1:
                break
            if a > 1:
                b = b * 2
                primes = []
                for num in range(2, b):
                    is_prime = True
                    for p in primes:
                        if p * p > num:
                            break
                        if num % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(num)
        return(factors)
#阶乘函数
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
history("turn on*")
print("Hello^=^")
#前端
j1=0
menu="0是生成质数表,1是翻倍运算，2是计算算术平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率,8是找零程序（贪心算法），9是统计，10是绘制函数图像，11是考试成绩数据整理，12是绘制正弦/余弦函数图像，13是求解二次方程，14是计算阶乘，15是极坐标转换,16是字符串频数统计&定位,17是质因数分解，18是计算GCD与LCM，19是十进制转二进制，20是计算排列组合，输入timer启动计时器，输入exit关闭程序，输入menu查看功能菜单，输入rr查看历史计算结果，输入er导出历史计算结果，输入cr清空历史计算结果，输入rh查看操作历史，输入eh导出操作历史,输入ch清空操作历史,输入version查看版本"
while True:
    import string
    import math
    if j1>0:
        a = input("请输入指令(输入exit关闭程序，输入menu查看功能菜单)：")
    else:
        print("功能菜单:"+menu)
        a = input("请输入指令:")
        j1+=1
    #生成质数表
    if a=="0":
        mode=input("请选择方法（普通方法输1，埃式筛法输2）")
        if mode=="1":
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
            saved("the reply from function 0[1]",d)
            history("0[1]*")
        if mode=="2":
            b = int(input("请输入您要生成的质数表范围（注意要加一）:"))   
            primes = []
            for num in range(2, b): 
                is_prime = True
                for p in primes:
                    if p*p > num:   
                        break
                    if num % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)   
            print("共找到", len(primes), "个质数")
            print(primes)
            saved("the reply from function 0[2]", primes)
            history("0[2]*")
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
        saved("the reply from function 1",w)
        history("1*")
    #计算算数平方根
    if a == "2":
        INPUT=input("请选择计算方法（输入1为逐次逼近法，输入2为牛顿迭代法)")
        if INPUT=="1":
            x = float(input("请输入需要求算术平方根的数："))
            precision = int(input("请输入迭代次数（值越大越精确，推荐10000）："))
            v = 1.0  # 初始猜测值
            k = 1.0  # 初始步长
            current_best = 0.0  # 记录当前最佳近似值
            u=[]
            for _ in range(precision):
                for _ in range(10):  # 每轮尝试10次调整
                    b = v * v
                    if b < x:
                        current_best = v  # 更新为当前下界
                        v += k
                    if b==x:
                        u.append(v)
                        e = len(u)
                        for q in range(e-1):
                            u.pop()
                    if b>x:
                        v = current_best  # 回退到前一个有效值
                        k /= 10          # 缩小步长
                        v += k           # 继续逼近
                        break            # 跳出内层循环
            if u==[]:
                print("算术平方根约为：", current_best)
                saved("the reply from function 2[1]", current_best)
                saved("the square root of",x)
            else:
                pre = u[0]
                print("算术平方根是：", pre)
                saved("the reply from function 2[1]",pre)
                saved("the square root of",x)
            history("2[1]*")
        if INPUT=="2":
            def sqrt_newton(x, max_iter=1000, precision=1e-10):
                guess = x / 2  # 初始猜测值
                for _ in range(max_iter):
                    guess = (guess + x / guess) / 2
                    if abs(guess * guess - x) < precision:
                        break
                return guess
            x = float(input("请输入需要求算术平方根的数："))
            precision = int(input("请输入迭代次数（值越大越精确，推荐10）："))
            result = sqrt_newton(x, max_iter=precision)
            print("算术平方根约为：", result)
            saved("the reply from function 2[2]",result)
            saved("the square root of",x)
            history("2[2]*")
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
            saved("the reply from function 3",d)
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
            saved("the reply from function 3",t)
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
            saved("the reply from function 3",qu)
            history("3(3)*")
    #求n次方
    if a=="4":
        s = int(input("请输入底数"))
        h = int(input("请输入指数"))
        u=s
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            u=u*w   
        print("结果是", u)
        saved("the reply from function 4",s)
        ll=ll+1
        saved("^",h)
        saved("=",u)
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
            saved("the reply from function 5[1]",b)
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
            saved("the reply from function 5[2]",e)
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
            saved("the reply from function 5[3]",h)
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
            saved("the reply from function 5[4]",l)
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
        saved("the reply from function 6",d)
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
        saved("the reply from function 7",v)
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
        saved("the reply from function 8",saved1)
        history("8*")
    #统计
    if a=="9":
        b=int(input("输入1求平均值，输入2求加权平均值，输入3求方差，输入4求标准差，输入5求中位数,输入6求众数："))
        if b==1:
            c=[]
            d=[]
            f=2
            while f>0:
                e=input("请输入数据（一次一个，输入完毕输f)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("错误：未输入数据！")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("输入错误！")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                print("平均值为",w4)
                saved("the reply from function9(1)",w4)
                history("9(1)*")
        if b==2:
            c=[]
            w1=[]
            f=2
            while f>0:
                e=input("请输入数据（一次一个，输入完毕输f)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("错误：未输入数据！")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("输入错误！")
            f=2
            while f>0:
                e=input("请输入权重（一次一个，输入完毕输f)")
                if e=="f":
                    f=0
                    if len(w1)==0:
                        print("错误：未输入权重！")
                        break
                else:
                    try:
                        w1.append(float(e))
                    except:
                        print("输入错误！")
            # 校验数量
            if len(c)!=len(w1):
                print("错误：数据和权重数量不同！")
            else:
                w11=0.0
                w12=0.0
                for w7 in range(len(c)):
                    w8=c[w7]
                    w9=w1[w7] 
                    w11 += w8*w9
                    w12 += w9
                if w12==0:
                    print("错误：权重总和为0！")
                else:
                    w14=w11/w12
                    print("加权平均数为",w14)
                    saved("the reply from function9(2)",w14)
                    history("9(2)*")
        if b==3:
            c=[]
            f=2
            while f>0:
                e=input("请输入数据（一次一个，输入完毕输f)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("错误：未输入数据！")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("输入错误！")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):  
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)): 
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                print("方差为",w9)
                saved("the reply from function9(3)",w9)
                history("9(3)*")

        if b==4:
            c=[]
            f=2
            while f>0:
                e=input("请输入数据（一次一个，输入完毕输f)")
                if e=="f":
                    f=0
                    if len(c)==0:
                        print("错误：未输入数据！")
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print("输入错误！")
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)):
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                x = w9
                d = int(input("需要的精确度（输入整数）:"))
                current = 0.0
                step = 1.0
                for _ in range(d):  # 限制循环次数
                    while (current + step) * (current + step) <= x:
                        current += step
                    step = step / 10
                print("标准差约为", round(current, 5))  # 限制小数位数
                saved("the reply from function9(4)",current)
                history("9(4)*")
        if b==5:
            DATA=[]
            Answer=0
            M1=0
            M2=0
            Break=0
            while True:
                data=input("依次输入数据，输入完毕输f")
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print("非法参数")
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                continue
            List=DATA
            def selection_sort(List):
                for i in range(len(List)):
                    index=i
                    for x in range(i+1,len(List)):
                        if List[x]<List[i]:
                            index=x
                    List[i],List[index]=List[index],List[i]
            selection_sort(List)
            if ((len(DATA)+1)/2)%1==0:
                Answer=DATA[int((len(DATA)+1)/2-1)]
            else:
                M1=DATA[int((len(DATA)+1)/2-1.5)]
                M2=DATA[int((len(DATA)+1)/2-0.5)]
                Answer=(M1+M2)/2
                print("中位数为",Answer)
                saved("the reply from function9(5)",Answer)
                history("9(5)*")
        if b==6:
            DATA=[]
            Frequency={}
            Answer=0
            M1=0
            M2=0
            Break=0
            MAX=0
            MAX2=[]
            nMAX=0
            OL=0
            Answer=""
            while True:
                data=input("依次输入数据，输入完毕输f")
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print("非法参数")
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                history("9(6)[error]")
                continue
            for index in range(len(DATA)):
                if DATA[index] in Frequency:
                    Frequency[DATA[index]]=Frequency[DATA[index]]+1
                else:
                    Frequency[DATA[index]]=1
            OL=len(DATA)
            DATA=list(set(DATA))
            AL=len(DATA)
            DI=OL-AL
            for index2 in DATA:
                if Frequency[index2]>MAX:
                    MAX=Frequency[index2]
                    MAX2.clear()
                    MAX2.append(index2)
                if Frequency[index2]==MAX:
                    nMAX=nMAX+1
            if nMAX==OL-DI:
                print("不存在众数")
                saved("the reply from function9(6)","none")
            else:
                if len(MAX2) != 1:
                    print("存在多个众数，为",MAX2)
                    saved("the reply from function9(6)",MAX2)
                else:
                    print("存在唯一众数，为",MAX2[0])
                    saved("the reply from function9(6)",MAX2[0])
            history("9[6]")
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
            history("10(2)")
#计时器
    if a=="timer":
        import time
        import math
        import keyboard
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
                    print(t2,"秒","按下a键结束计时")
                if t2>1:
                    print(t2,"秒","按下a键结束计时")
            if t3>1:
                mine=t3
                s=t2-60*t3
                print(mine,"分",s,"秒","按下a键结束计时")
            if t3==1:
                mine=t3
                s=t2-60*t3
                print(mine,"分",s,"秒","按下a键结束计时")
            if keyboard.is_pressed('a'):
                break
        history("timer")
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
        saved("the reply from function 11","max")
        saved(Max,"min")
        saved(Min,"all")
        saved(Sum,"pingjun")
        saved(average," ")
        history("11")
#绘制正弦/余弦函数图像
    if a=="12":
        mode=input("请选择模式（正弦输入1，余弦输入2）")
        Pa=mode
        pi=3.1415926535
        acc1=float(input("输入模拟角度(推荐1）"))
        acc2=int(input("输入步进（推荐100）"))
        acc3=int(input("输入缩放系数（推荐10000）"))
        acc4=int(input("设置图像X轴起点（正弦推荐-300，余弦推荐-250）"))
        acc5=int(input("设置图像Y轴起点（正弦推荐0，余弦推荐-10000）"))
        acc6=acc3/((360/acc1*acc2)/(2*pi))
        step=int(2*pi*acc2/(360/acc1))
        Y_co=[]           
        import turtle
        turtle.speed(0)
        turtle.penup()
        turtle.goto((360/acc1*acc2)/(2*pi),0)
        turtle.pendown()
        turtle.left(90)
        for i in range(int(360/acc1)):
            turtle.forward(step)
            turtle.left(acc1)
            Pos=turtle.pos()
            Pos1=str(Pos)
            Pos2=Pos1.split("(")
            Pos3=Pos2[1].split(")")
            Pos4=Pos3[0].split(",")
            if Pa=="1":
                Pos5=Pos4[1]
            if Pa=="2":
                Pos5=Pos4[0]
            Y_co.append(float(Pos5))
            print("采样中，",i+1,"/",int(360/acc1))
        turtle.clearscreen()
        for r in range(int(360/acc1)):
            step1=r*acc6
            step2=acc6*float(Y_co[r])
            turtle.penup()
            turtle.goto(acc4+step1,acc5+step2)
            turtle.pendown()
            turtle.forward(1)
        history("12")
    #求解二次方程
    if a=="13":
        answer1=0
        answer2=0
        Answer=[]
        Coefficients=[]
        Precision=int(input("输入精度（数字越大越精确，推荐输入100）"))
        while True:
            Coefficient=input("依次输入每项的系数，从二次项到常数项(若不存在该项则输入0)，输入完毕输f")
            if Coefficient=="f":
                break
            else:
                try:
                    float(Coefficient)
                except:
                    print("非法参数")
                    break
                Coefficients.append(float(Coefficient))
        length=len(Coefficients)
        if length != 3:
            print("系数数量错误！")
        else:
            discriminant = (Coefficients[1] ** 2) - (4 * Coefficients[0] * Coefficients[2])
            if discriminant<0:
                Answer.append("no solution")
            else:
                answer1=((-Coefficients[1])+Squareroot(discriminant,Precision))/(2*Coefficients[0])
                answer2=((-Coefficients[1])-Squareroot(discriminant,Precision))/(2*Coefficients[0])
                if answer1==answer2:
                    Answer.append(answer1)
                else:
                    Answer.append(answer1)
                    Answer.append(answer2)
            print("方程的解为：",Answer)
            saved("the reply from function 13",Answer)
            history("13")
    #计算阶乘
    if a == "14":
        n = int(input("请输入正整数n："))
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        result = factorial(n)
        print(f"{n}! = {result}")
        saved("the reply from function 14", result)
        history("14*")
    #极坐标转换
    if a == "15":
        import math
        mode = input("请选择转换方向（1: 笛卡尔坐标 → 极坐标，2: 极坐标 → 笛卡尔坐标）")
        
        try:
            if mode == "1":
                x = float(input("请输入x坐标: "))
                y = float(input("请输入y坐标: "))
                r = math.sqrt(x**2 + y**2)
                theta = math.degrees(math.atan2(y, x))  # 角度制输出
                result = f"Polar coordinates: ({round(r, 4)}, {round(theta, 4)}°)"
                
            elif mode == "2":
                r = float(input("请输入半径r: "))
                theta = math.radians(float(input("请输入角度θ(°): ")))  # 转换为弧度
                x = r * math.cos(theta)
                y = r * math.sin(theta)
                result = f"Cartesian coordinate: ({round(x, 4)}, {round(y, 4)})"
                
            else:
                print("输入错误！")
                history("15*[error]")
                continue
                
            print(result)
            saved("the reply from function 15", result)
            history("15*")
            
        except ValueError:
            print("错误：请输入有效数字！")
            history("15*[invalid_input]")
    #字符串频数统计&定位
    if a=="16":
        INPUT=input("请输入您要查找的json文件的名称（例：查找file.json输入file)")
        b=input("请输入您需要查找的文本或数值：")
        Unit_length=len(b)
        with open(INPUT+".json","r") as OF:
            File=json.load(OF)
            Str_File=str(File)      
        number=0
        for i in range(len(Str_File)-Unit_length+1):
            if Str_File[i:i+Unit_length]==b:
                number=number+1
                print("找到啦,在",INPUT,".json","中的索引位置为",i,"至",i+Unit_length-1)
        print(b,"在",INPUT,".json","中出现了",number,"次")
        saved("the reply from function 16",b)
        saved(number,"times")
        saved("in",INPUT+".json")
        history("16")
    #质因数分解
    if a=="17":
        a = int(input("请输入需要分解的数"))
        if a == 1:
            print("质因数为", 1)
            saved("the reply from function 16", "factor")
            saved(":", "1")
        if a <= 0:
            print("0和负数没有质因数")
            saved("the reply from function 16", "factor")
            saved(":", "none")
        else:
            b = 101
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            factors = []
            Break = 0
            while Break == 0:
                for i in range(len(primes)):
                    while a % primes[i] == 0:
                        factors.append(primes[i])
                        a = a // primes[i]  
                        if a == 1:
                            Break = 1
                            break
                    if Break == 1:
                        break
                if Break == 1:
                    break
                if a > 1:
                    print("您提供的数字的质因数过大，正在拓展搜索范围，请稍等")
                    b = b * 2
                    primes = []
                    for num in range(2, b):
                        is_prime = True
                        for p in primes:
                            if p * p > num:
                                break
                            if num % p == 0:
                                is_prime = False
                                break
                        if is_prime:
                            primes.append(num)
            print("质因数为", factors)
            saved("the reply from function 16","factor(s)")
            saved(":",factors)
        history("17")
    #计算GCD与LCM
    if a == "18":
        choice = input("请选择计算模式：1为最大公因数（GCD），2为最小公倍数（LCM）: ")   
        UserInput = []
        print("开始输入数字（输入完毕后输入f）:")
        while True:
            Input = input("请输入一个正整数（或输入f结束）: ")
            if Input.lower() == 'f':
                break
            try:
                num = int(Input)
                if num <= 0:
                    print("错误：请输入正整数！")
                    continue
                UserInput.append(num)
            except ValueError:
                print("输入无效，请输入数字或输入f结束！")
                continue
        if len(UserInput) < 2:
            print("错误：至少需要两个数字！")
            history("18*[error]")
        else:
            nums = UserInput  
        
            # 质因数分解验证
            factors_list = []
            valid = True
            for num in nums:
                factors = prime_factor(num)
                if factors == "none":
                    print(f"错误：数字 {num} 无法分解质因数！")
                    valid = False
                    break
                factors_list.append(factors)
        
            if valid:
                # 统计每个数的质因数次数
                from collections import defaultdict
                counts_list = []
                for factors in factors_list:
                    counts = defaultdict(int)
                    for p in factors:
                        counts[p] += 1
                    counts_list.append(counts)
            
                # 计算GCD或LCM
                if choice == "1":
                    # 计算GCD
                    common_primes = set(counts_list[0].keys())
                    for cnt in counts_list[1:]:
                        common_primes.intersection_update(cnt.keys())
                    gcd = 1
                    for prime in common_primes:
                        min_power = min(cnt[prime] for cnt in counts_list)
                        gcd *= prime ** min_power
                    print(f"最大公因数（GCD）为：{gcd}")
                    saved("the reply from function 18[GCD]", gcd)
                    history("18[GCD]*")
            
                elif choice == "2":
                    # 计算LCM
                    all_primes = set()
                    for cnt in counts_list:
                        all_primes.update(cnt.keys())
                    lcm = 1
                    for prime in all_primes:
                        max_power = max(cnt.get(prime, 0) for cnt in counts_list)
                        lcm *= prime ** max_power
                    print(f"最小公倍数（LCM）为：{lcm}")
                    saved("the reply from function 18[LCM]", lcm)
                    history("18[LCM]*")
            
                else:
                    print("无效的选择！")
                    history("18*[invalid]")
    #十进制转二进制
    if a=="19":
        INPUT=input("请输入十进制整数")
        digits=[]
        reverse=[]
        result=""
        try:
            int(INPUT)
        except:
            print("无效输入")
            history("19([error]")
            continue
        else:
            ten=int(INPUT)
        if ten==0:
            result="0"           
        else:
            while ten>=1:
                digit=ten%2
                digits.append(int(digit))
                ten=ten//2
            reverse=list(reversed(digits))
            for index2 in range(len(reverse)):
                result=result+str(reverse[index2])
        print(INPUT+"所对应的二进制数是",result)
        saved("the reply from function 19", "Decimal:"+INPUT)
        saved("Binary:", result)
        history("19")
    # 计算排列组合
    if a == "20":
        import math
        mode = input("请选择模式（1为排列数nPr，2为组合数nCr）: ")
        try:
            n = int(input("请输入正整数n: "))
            r = int(input("请输入正整数r（r ≤ n）: "))
            if n < 0 or r < 0 or r > n:
                print("输入无效！")
                history("20*[error]")
            else:
                if mode == "1":
                    # 计算排列数 nPr = n! / (n-r)!
                    result = factorial(n) // factorial(n - r)
                    print(str(n)+"P"+str(r)+"=",result)
                    saved("the reply from function 20[nPr]", str(n)+"P"+str(r)+"="+str(result))
                    history("20[nPr]*")
                elif mode == "2":
                    # 计算组合数 nCr = n! / (r!(n-r)!)
                    result = factorial(n) // (factorial(r) * factorial(n - r))
                    print(str(n)+"C"+str(r)+"=",result)
                    saved("the reply from function 20[nCr]",str(n)+"C"+str(r)+"="+str(result))
                    history("20[nCr]*")
                else:
                    print("模式无效！")
                    history("20*[invalid]")
        except ValueError:
            print("错误：请输入有效整数！")
            history("20*[invalid_input]")
#菜单
    if a=="menu":
        print(menu)
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
        history("turn off")
        break
#读取操作历史
    if a=="rh":
        with open("history.json","r") as yy:
            o1=json.load(yy)
        print(o1)
#清空操作历史
    if a=="ch":
        with open("history.json","w") as yy:
            json.dump("prepare done ",yy)
        print("已清空")
#导出操作历史
    if a=="eh":
        export_file("history")
        print("已将操作历史导出为history.txt")
#导出历史计算结果
    if a=="er":
        export_file("reply")
        print("已将历史计算结果导出为reply.txt") 
#查看版本
    if a=="version":
        print("您当前正在使用的是"+Version+" by QU QI")
print("再见")
print("hope to see you again")