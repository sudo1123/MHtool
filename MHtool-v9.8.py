# -*- coding: UTF-8 -*-
# Copyright (c) 2025 QU QI
# MIT Licensed (https://opensource.org/licenses/MIT)
import os
import json
import decimal
import string
import math
import os
os.system("")#解决转义序列不生效问题（原理玄学）
Version="MHtool v9.8"
#提高整数限制
try:
    import sys
    from unicodedata import digit
    sys.set_int_max_str_digits(1000000000)
except:
    pass
#初始化函数
def init_files():
    # 初始化文件列表及默认值
    files = {
        "number saved.json": "0",          
        "mode.json": "0",                               
        "history.json": ["prepare done"],
        "result.json": [],
        "No_History.json": "0",
        "picture_choice.json":"0"
    }   
    # 遍历创建文件
    for filename, default in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="UTF-8") as f:
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
    INPUT="result"
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
        with open("result.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("result.json","w") as f:
            json.dump(kk,f)
version(Version)  
#检验是否启用操作历史保存
import json
with open("No_History.json","r") as NH2:
    NH4=json.load(NH2)
    if NH4=="0":
        Choice=input("请选择是否保存操作历史(输入1为是，输入2为否）")
        with open("No_History.json","w") as NH3:
            WR=NH3
            if Choice=="2":
                json.dump("2",WR)
            if Choice=="1":
                json.dump("1",WR)
    else:
        pass
#保存结果函数
with open("mode.json","r") as qu:
    qi=json.load(qu)
    if qi=="0":
        box=int(input("您是否需要启用保存计算结果功能？（是按1，不是按2，按2将永久禁用计算结果保存）:"))
        if box==1:
            with open("mode.json","w") as z:
                json.dump("1",z)
        if box==2:
            with open("mode.json","w") as z:
                json.dump("2",z)
    if qi == "1":
        def saved(quqi, p):
            c12 = str(input("您是否要保存结果？（是按1，不是按2）:"))
            if c12 == "1":
                with open("number saved.json", "r") as zz:
                    tt = json.load(zz)
                # 确保reply.json内容为列表
                try:
                    with open("result.json", "r") as g:
                        ee = json.load(g)
                    if not isinstance(ee, list):  # 若非列表，重置为空列表
                        ee = []
                except (json.JSONDecodeError, FileNotFoundError):
                    ee = []            
                ee.extend([quqi, p])  # 追加结果
                with open("result.json", "w") as f:
                    json.dump(ee, f, ensure_ascii=False)
                print("完成，已存至result.json")
                with open("number saved.json", "w") as zz:
                    json.dump(str(len(ee) // 2), zz)  # 更新保存次数
    if qi=="2":
        def saved(quqi,p):
            pass
#文件导出函数
def export_file(filename):
    import json
    with open(filename+".json", "r") as f:
        history_data = json.load(f)
    with open(filename+".txt", "w", encoding="UTF-8") as f:
        for entry in history_data:
            f.write(str(entry) + "\n")
#历史记录函数
with open("No_History.json","r")as NH:
    NO=json.load(NH)
    if NO=="1":
        def history(quqi):
            ww=[]
            with open("history.json","r") as g:
                ee=json.load(g)
                ww.append(ee)
                ww.append(quqi)
            with open("history.json","w") as f:
                json.dump(ww,f)
    else:
        def history(oo):
            pass
#turtle资源管理函数
try:
    import turtle
    def reset_turtle():
        try:
            import turtle
            # 关闭窗口（如果存在）
            if hasattr(turtle.Screen(), "_root") and turtle.Screen()._root:
                turtle.bye()
            # 清除所有画笔和画布
            turtle.clearscreen()
            # 强制重置模块内部状态
            turtle.TurtleScreen._RUNNING = False
            turtle.Turtle._pen = None
            turtle.Turtle._screen = None
        except (ImportError, AttributeError, turtle.Terminator):
            pass
except ImportError:
    def reset_turtle():
        pass
#保存图像函数
with open("picture_choice.json","r") as pic:
    pict=json.load(pic)
    if pict !="3":
        try:
            import turtle
        except ImportError:
            with open("picture_choice.json","w") as o:
                json.dump("3",o)
                bre=input("当前环境不支持图形,程序需重启,输入任意键继续")
                exit()
    if pict=="0":
        Inputs=input("您是否要启用图像保存功能（输1启用，输2则永久禁用）")
        if Inputs=="1":
            with open("picture_choice.json","w") as o:
                    json.dump("1",o)
        if Inputs=="2":
            with open("picture_choice.json","w") as o:
                    json.dump("2",o)
        Bre=input("程序需重启,输入任意键继续")
        exit()
    if pict=="1":
        import time
        def saved_picture():
            Choice=input("您是否要保存当前图像（输入1为是，输入2为否）")
            if Choice=="1":
                timestamp = time.time()
                canvas = turtle.getcanvas().postscript(file="MHtool_picture"+str(int(timestamp))+".eps")
                print("已保存图像为MHtool_picture"+str(int(timestamp))+".eps")
            else:
                pass
    if pict=="2":
        def saved_picture():
            pass
    if pict=="3":
        try:
            import turtle
            with open("picture_choice.json","w") as o:
                json.dump("0",o)
                Input=input("检测到运行环境发生更改，程序需重启，请输入任意键继续")
                exit()
        except ImportError:
            def saved_picture():
                pass
#用户操作提示函数
def reminder(te):
    print("您正在使用",str(te),"功能")
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
        answer=1
        for index in range(n):
            kook=index+1
            answer=answer*kook
        return answer
#三角函数计算函数
def tri_function(IN,IN2,MODE,Precision):
    k=decimal.Decimal(IN/IN2*3.1415926535897)
    answer=0
    if MODE=="1":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index+1)
            IC=decimal.Decimal(k**(2*index+1))
            term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
            answer=answer+term
        return(str(answer))
    if MODE=="2":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index)
            IC=decimal.Decimal(k**(2*index))
            term=(decimal.Decimal(I/IB))*IC
            answer=answer+term
        return(str(answer))
    if MODE=="3":
        Sin=0
        Cos=0
        if 2*IN%IN2==0 and (2*IN//IN2)%2 !=0:
            return("DNE")
        else:
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index+1)
                IC=decimal.Decimal(k**(2*index+1))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Sin=decimal.Decimal(answer)
            answer=0
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index)
                IC=decimal.Decimal(k**(2*index))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Cos=decimal.Decimal(answer)
            answer=Sin/Cos
            return(str(answer))
#用户交互
history("turn on*")
print("Hello^=^")
page="1"
menu=""
menu1="1:生成质数表，2:计算算术平方根，3:计算圆周率\n4:求n次幂，5:四则运算，6:生成斐波那契数列\n7:计算黄金分割率，8:找零程序（贪心算法)，9:统计\n"
menu2="10:绘制函数图像，11:考试成绩数据整理，12:绘制三角函数图像\n13:求解二次方程，14:计算阶乘，15:极坐标转换\n16:字符串频数统计&定位,17:质因数分解，18:计算GCD与LCM\n"
menu3="19:十进制转二进制，20:计算排列组合，21:计算三角函数值\n22:弧度角度制转换，23:质数检测，24:向量模长计算\n25:计算任意三角形面积，26:向量点乘，27:十进制转十六进制\n"
menuf="timer:启动计时器,rr:查看历史计算结果，er:导出历史计算结果\ncr:清空历史计算结果，rh:查看操作历史，eh:导出操作历史\nch:清空操作历史，cs:清空屏幕，version:查看版本\n"
menu=menu1
page="1"
while True:
    a = input("请输入指令(输入exit关闭程序,输入menu查看功能菜单,输入amenu列出所有功能):")
    #菜单
    if a=="amenu":
        print(menu1+menu2+menu3+menuf)
    if a=="menu":
        while True:
            if page=="1":
                print("功能菜单\n"+"当前是第"+str(page)+"页,共"+"4"+"面\n"+menu+"\n查看下一页请输np")
            elif page=="f":
                print("功能菜单\n"+"当前是第"+str(page)+"页,共"+"4"+"面\n"+menu+"\n查看上一页请输pp")
            else:
                print("功能菜单\n"+"当前是第"+str(page)+"页,共"+"4"+"面\n"+menu+"\n查看上一页请输pp,查看下一页请输np")
            E=input("翻页命令:(退出功能菜单输quit)")
            if E=="pp":
                if page=="1":
                    print("已经是第一页")
                    continue
                if page=="2":
                    menu=menu1
                    page="1"
                    continue
                if page=="3":
                    menu=menu2
                    page="2"
                    continue
                if page=="f":
                    menu=menu3
                    page="3"
                    continue
            if E=="np":
                if page=="1":
                    menu=menu2
                    page="2"
                    continue
                if page=="2":
                    menu=menu3
                    page="3"
                    continue
                if page=="3":
                    menu=menuf
                    page="f"
                    continue
                if page=="f":
                    print("已经是最后一面")
                    continue
            if E=="quit":
                break
    #生成质数表
    if a=="1":
        reminder("生成质数表")
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
            saved("the reply from function 1[1]",str(len(d))+" "+"prime numbers:"+str(d))
            history("1[1]*")
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
            saved("the reply from function 1[2]",str(len(primes))+" "+"prime numbers:"+str(primes))
            history("1[2]*")
    #计算算术平方根
    if a == "2":
        reminder("计算算术平方根")
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
                saved("the reply from function 2[1]", str(current_best)+", ,"+"the square root of"+str(x))
            else:
                pre = u[0]
                print("算术平方根是：", pre)
                saved("the reply from function 2[1]",str(pre)+", ,"+"the square root of"+str(x))
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
            saved("the reply from function 2[2]",str(result)+", ,"+"the square root of"+str(x))
            history("2[2]*")
    #计算圆周率
    if a =="3":
        reminder("计算圆周率")
        c=int(input("请选择算法（莱布尼茨级数法输1，几何法输2,蒙特卡洛法输3，拉马努金公式法输4）"))
        if c==1:#莱布尼茨级数法
            a=0
            b=1
            d=0
            e=int(input("请输入需要的精度（10的倍数）"))
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
            reset_turtle()
            try:
                import turtle
            except ImportError:
                print("turtle模块不可用。")
                continue
            myPen = turtle.Turtle()
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
            turtle.bye()
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
        if c==4:#拉马努金公式法
            acc=int(input("请输入精度"))
            root2=Squareroot(2,acc)
            coe=root2*2/9801
            latter=0
            for index in range(acc):
                v1=4*index
                v2=factorial(v1)*(1103+26390*index)
                v3=factorial(index)**4
                v4=396**(4*index)
                v5=v3*v4
                v6=v2/v5
                latter=latter+v6
            r=coe*latter
            answer=r**(-1)
            print("圆周率约为",answer)
            saved("the reply from function 3",answer)
            history("3(4)*")
    #求n次幂
    if a=="4":
        reminder("求n次幂")
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
        saved("the reply from function 4",str(s)+"^"+str(h)+"="+str(u))
        ll=ll+1
        history("4*")
    #四则运算
    if a=="5":
        reminder("四则运算")
        s = int(input("请输入您选择的模式（1代表加法运算,2代表减法运算,3代表除法运算,4代表乘法运算）"))
        if s == 1:
            b = int(input("请输入一个加数"))
            c = int(input("请输入另一个加数"))
            d = c+b
            print("结果是", d)
            ee=0
            saved("the reply from function 5[1]",str(b)+"+"+str(c)+"="+str(d))
            ee=ee+1
            ee=0
            history("5(1)*")
        if s == 2:
            e = int(input("请输入被减数"))
            f = int(input("请输入减数"))
            g = e-f
            print("结果是", g)
            ff=0
            saved("the reply from function 5[2]",str(e)+"-"+str(f)+"="+str(g))
            ff=ff+1
            ff=0
            history("5(2)*")
        if s == 3:
            h = int(input("请输入被除数"))
            j = int(input("请输入除数"))
            if j == 0:
                print("您输入的除数是0，0不能作为除数")
                saved("the reply from function 5[3]","error")
                history("5(3)(error)")
                continue
            else:
                k = h/j
                print("结果是", k)
            jj=0
            saved("the reply from function 5[3]",str(h)+"/"+str(j)+"="+str(k))
            jj=jj+1
            jj=0
            history("5(3)*")
        if s == 4:
            l = int(input("请输入一个乘数"))
            m = int(input("请输入另一个乘数"))
            n = l*m
            print("结果是", n)
            gg=0
            saved("the reply from function 5[4]",str(l)+"*"+str(m)+"="+str(n))
            gg=gg+1
            history("5(4)*")
    #生成斐波那契数列
    if a =="6":
        reminder("生成斐波那契数列")
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
            print("计算中"+str(e+1)+"/"+str(a))
        print("数列为"+str(d))
        saved("the reply from function 6",d)
        history("6*")
    #计算黄金分割率
    if a =="7":
        reminder("计算黄金分割率")
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
            print("计算中"+str(e+1)+"/"+str(a))
        s=len(d)
        v=d[s-2]/d[s-1]
        print("黄金分割率约为",v)
        saved("the reply from function 7",v)
        history("7*")
    #贪心算法
    if a=="8":
        reminder("贪心算法")
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
        reminder("统计")
        b=int(input("输入1求平均值，输入2求加权平均值，输入3求方差，输入4求标准差，输入5求中位数，输入6求众数："))
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
        reminder("绘制函数图像")
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print("turtle模块不可用。")
            continue
        x=int(input("请输入选择模式（1为一次函数，2为二次函数）"))
        if x==1:
            myPen=turtle.Turtle()
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
            print("绘制完成")
            saved_picture()
            turtle.done()
            history("10(1)")
        if x==2:
            myPen=turtle.Turtle()
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
            print("绘制完成")
            saved_picture()
            turtle.done()
            history("10(2)")
#计时器
    if a=="timer":
        import time
        import math
        try:
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
        except:
            print("当前环境暂不支持计时器功能")
            history("timer(environment not support)")
            continue
#考试成绩数据整理
    if a=="11":
        reminder("考试成绩数据整理")
        s=2
        Sum=0
        average=0
        Max=0
        Min=0
        Dict={}
        while s>1:
            qu=input("请输入学生名,全部录入输f")
            if qu=="f":
                s=0
            else:
                qi=input("请输入学生成绩")
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
        saved("the reply from function 11","max:"+str(Max)+" min:"+str(Min)+" all:"+str(Sum)+" average:"+str(average))
        history("11")
#绘制三角函数图像
    if a=="12":
        reminder("绘制三角函数图像")
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print("turtle模块不可用。")
            continue
        print("注意：正切函数只能使用代数算法绘制！")
        Method=input("请输入您要选择的算法（输入1为几何算法，输入2为代数算法）")
        mode=input("请选择模式（正弦输入1，余弦输入2，正切输入3）")
        acc4=int(input("设置图像X轴起点（正弦&正切推荐-300，余弦推荐-250）"))
        acc5=int(input("设置图像Y轴起点（正弦&正切&代数法余弦推荐0，几何法余弦推荐-10000）"))
        Pa=mode
        pi=3.1415926535 
        if Method=="1":#几何法
            myPen=turtle.Turtle()
            acc1=float(input("输入模拟角度(推荐1）"))
            acc2=int(input("输入步进（推荐100）"))
            acc3=int(input("输入几何法缩放系数（推荐10000）"))
            if Pa=="3":
                print("几何算法无法绘制tan图像，请使用代数算法")
                history("12[error]")
                continue
            acc6=acc3/((360/acc1*acc2)/(2*pi))
            step=int(2*pi*acc2/(360/acc1))
            Y_co=[]
            myPen.speed(0)
            myPen.penup()
            myPen.goto((360/acc1*acc2)/(2*pi),0)
            myPen.pendown()
            myPen.left(90)
            for i in range(int(360/acc1)):
                myPen.forward(step)
                myPen.left(acc1)
                Pos=myPen.pos()
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
            print("绘制中...")
            for r in range(int(360/acc1)):
                step1=r*acc6
                step2=acc6*float(Y_co[r])
                myPen.penup()
                myPen.goto(acc4+step1,acc5+step2)
                myPen.pendown()
                myPen.dot(2)
            print("绘制完成")
            saved_picture()
            turtle.done()
            history("12[1]")
        if Method=="2":#代数法
            Coordinates_Y=[]
            acc6=int(input("请输入计算精度（整数）（推荐100）"))
            acc7=int(input("请输入取点数量（推荐360）"))
            acc8=int(input("请输入代数法缩放系数（推荐2）"))
            C1=2
            C2=acc7
            C3=0
            acc9=acc8*acc7/(2*pi)
            for index in range(acc7):
                try:
                    Coordinates_Y.append(float(tri_function(C3,C2,mode,acc6)))#本处的except意外捕获了原本应该出现的invalidoperation错误，但不意味着问题得到了解决
                except:
                    Coordinates_Y.append("DNE")
                print("计算采样中:"+str(index+1)+"/"+str(acc7))
                C3=C3+C1
            turtle.clearscreen()
            print("绘制中...")
            for r in range(acc7):
                step1=acc8*r
                try:
                    step2=acc9*Coordinates_Y[r]
                except:
                    continue
                turtle.speed(0)
                turtle.penup()
                turtle.goto(acc4+step1,acc5+step2)
                turtle.pendown()
                turtle.dot(2)
            print("绘制完成")
            saved_picture()
            turtle.done()
            history("12[2]")
    #求解二次方程
    if a=="13":
        reminder("求解二次方程")
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
        reminder("计算阶乘")
        n = int(input("请输入正整数n："))
        result = factorial(n)
        print(f"{n}! = {result}")
        saved("the reply from function 14", result)
        history("14*")
    #极坐标转换
    if a == "15":
        reminder("极坐标转换")
        import math
        mode = input("请选择转换方向（1: 笛卡尔坐标至极坐标，2: 极坐标至笛卡尔坐标）")
        
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
        reminder("字符串频数统计&定位")
        INPUT=input("请输入您要查找的json文件的名称（例：查找file.json输入file)")
        b=input("请输入您需要查找的文本或数值：")
        Unit_length=len(b)
        try:
            with open(INPUT+".json","r") as OF:
                File=json.load(OF)
                Str_File=str(File)      
            number=0
            for i in range(len(Str_File)-Unit_length+1):
                if Str_File[i:i+Unit_length]==b:
                    number=number+1
                    print("找到啦,在",INPUT,".json","中的索引位置为",i,"至",i+Unit_length-1)
            print(b,"在",INPUT,".json","中出现了",number,"次")
            saved("the reply from function 16","“"+str(b)+"”"+" "+str(number)+" "+"times"+" "+"in"+" "+"“"+str(INPUT)+".json"+"”")
            history("16")
        except:
            print("文件不存在")
            saved("the reply from function 16","file not exist")
            history("16[error]")
    #质因数分解
    if a=="17":
        reminder("质因数分解")
        a = int(input("请输入需要分解的数"))
        if a == 1:
            print("质因数为", 1)
            saved("the reply from function 17","factor"+":"+"1")
            history("17")
            continue
        if a <= 0:
            print("0和负数没有质因数")
            saved("the reply from function 17","factor"+":"+"none")
            history("17[none]")
            continue
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
            saved("the reply from function 17","factor(s)"+":"+str(factors))
            history("17")
    #计算GCD与LCM
    if a == "18":
        reminder("计算GCD与LCM")
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
        reminder("十进制转二进制")
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
        saved("the reply from function 19", "Decimal:"+str(INPUT)+" "+"Binary:"+str(result))
        history("19")
    # 计算排列组合
    if a == "20":
        reminder("计算排列组合")
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
    #计算三角函数值
    if a=="21":
        reminder("计算三角函数值")
        print("请输入请输入需要求值的角度（弧度制下pi的系数的分数形式，例如360度请在分子输入2，分母输入1）")
        IN=int(input("请输入分子"))
        IN2=int(input("请输入分母"))
        MODE=input("请选择计算模式（sin为1，cos为2，tan为3)")
        Precision=int(input("请输入展开的项数（越大越精确）"))
        if MODE=="1":
            if IN==0:
                answer="0"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print("sin"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","sin"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[1]")
        if MODE=="2":
            if IN==0:
                answer="1"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print("cos"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","cos"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[2]")
        if MODE=="3":
            if IN==0:
                answer="0"
            else:
                answer=answer=tri_function(IN,IN2,MODE,Precision)
            print("tan"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            saved("the reply from function 21","tan"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[3]")
    #弧度角度制转换
    if a=="22":
        reminder("弧度角度制转换")
        MODE=input("请选择模式（角度转弧度输1，弧度转角度输2）")
        if MODE=="1":
            INPUT=input("请输入角度值")
            k=float(INPUT)/180
            print(INPUT+"°"+"="+str(k)+"pi")
            saved("the reply from function 22",INPUT+"°"+"="+str(k)+"pi")
            history("22[1]")
        if MODE=="2":
            print("请输入弧度制下pi的系数，如pi/2请在分子输1，分母输2")
            INPUT=int(input("请输入分子"))
            INPUT2=int(input("请输入分母"))
            INPUT3=INPUT/INPUT2
            k=INPUT3*180
            print(str(INPUT)+"/"+str(INPUT2)+"pi"+"="+str(k)+"°")
            saved("the reply from function 22",str(INPUT)+"/"+str(INPUT2)+"pi"+"="+str(k)+"°")
            history("22[2]")
    #质数检测
    if a=="23":
        reminder("质数检测")
        num = int(input("输入待检测的正整数："))
        def prime_check(num):
            res=""
            if num == 1:
                res = "1"
            else:
                factors = prime_factor(num)
                if len(factors) == 1:
                    res = "prime number" 
                else: 
                    res = "composite number"
            return res
        resu=prime_check(num)
        if resu=="1":
            print("1既非质数也非合数")
            saved("the reply from function 23",str(num)+":"+"neither a prime number nor a composite number")          
        if resu=="prime number":
            print(str(num)+"是质数")
            saved("the reply from function 23",str(num)+":"+"prime number")
        if resu=="composite number":
            print(str(num)+"是合数")
            saved("the reply from function 23",str(num)+":"+"composite number")
        history("23")
#向量模长计算
    if a=="24":
        reminder("向量模长计算")
        inp=input("请输入x")
        inp2=input("请输入y")
        answer1=(decimal.Decimal(inp)**2)+(decimal.Decimal(inp2)**2)
        answerf=Squareroot(answer1,1000)
        print("当前向量的模长为"+str(answerf))
        saved("the reply from function 24","("+str(inp)+","+str(inp2)+")"+"=>"+str(answerf))
        history("24")
#计算任意三角形面积
    if a=="25":
        reminder("计算任意三角形面积")
        Mode=input("请选择计算方式(三边计算输1,底-高计算输2):")
        if Mode=="1":
            L1=input("请输入三角形的第一个边长")
            L2=input("请输入三角形的第二个边长")
            L3=input("请输入三角形的第三个边长")
            ACC=input("请输入精度(推荐输入100)")
            try:
                a=decimal.Decimal(L1)
                b=decimal.Decimal(L2)
                c=decimal.Decimal(L3)
            except:
                print("输入有误")
                history("25[error]")
                continue
            if a+b<=c or a+c<=b or b+c<=a:
                print("您输入的边长数据不能构成三角形")
                history("25[invalid]")
                continue
            else:
                p=decimal.Decimal((a+b+c)/2)
                S1=p*(p-a)*(p-b)*(p-c)
                S=Squareroot(S1,int(ACC))
                print("三角形的面积为"+str(S))
                saved("the reply from function 25[1]",str(S))
                history("25[1]")
        if Mode=="2":
            L=input("请输入三角形的底边长")
            H=input("请输入三角形的高")
            Answer=decimal.Decimal(L)*decimal.Decimal(H)/2
            print("三角形的面积为"+str(Answer))
            saved("the reply from function 25[2]",str(Answer))
            history("25[2]")
    #向量点乘
    if a=="26":
        reminder("向量点乘")
        Input1=input("输入第一个模长")
        Input2=input("输入第二个模长")
        Angle1=input("请输入分子(弧度制下pi的系数的分子，如180度输入2)")
        Angle2=input("请输入分母(弧度制下pi的系数的分母，如180度输入1)")
        Pre=input("请输入精度")
        Answer=float(Input1)*float(Input2)*float(tri_function(float(Angle1),float(Angle2),"2",int(Pre)))
        print(Answer)
        saved("the reply from function 26",str(Answer))
        history("26")
    #十进制转十六进制
    if a=="27":
        reminder("十进制转十六进制")
        INPUT=input("请输入您要转换的十进制数")
        def decimal_to_hex(n):
            hex_digits = "0123456789ABCDEF"
            if n == 0:
                return "0"
            hex_str = ""
            while n > 0:
                hex_str = hex_digits[n % 16] + hex_str
                n = n // 16
            return hex_str
        Answer=decimal_to_hex(int(INPUT))
        print(INPUT+"所对应的十六进制数为"+str(Answer))
        saved("the reply from function 27",INPUT+" "+"=>"+" "+str(Answer))
        history("27")
#读取计算结果
    if a=="rr":
        with open("result.json","r") as gu:
            eue=json.load(gu)
            print(eue)
#清空计算结果
    if a=="cr":
        with open("result.json","w") as gu:
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
        export_file("result")
        print("已将历史计算结果导出为result.txt")
#清屏
    if a=="cs":
        print("\033c", end="")
#查看版本
    if a=="version":
        print("您当前正在使用的是"+Version+" by QU QI")
#翻倍计算（已隐藏）
    if a=="benchmark":   
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
        saved("the reply from function benchmark",w)
        history("894*")
print("再见")
print("Good-bye!")