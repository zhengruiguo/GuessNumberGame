'''
猜数字游戏 by 郑瑞国
'''
import random               #引入模块random
 
print('猜数字游戏')         #打印输出'猜数字游戏'
print('''
        Game Start!!!       
        ''')                #带格式打印输出'Game Start!!!'
level = 0                   #level参数赋值为0，用来存当前为第几关
try_time = 5                #try_time参数赋值为5，用来控制可猜测次数
while level < 100:          #当小于100关时，进行循环
    level = level + 1       #关数自加一
    try_time = try_time + 1                                     #可猜测次数加一
    number = random.randint(0,10*level)                         #产生随机数
    print('level:',level,'MAX:',10*level,'try_time:',try_time)  #输出游戏参数
    try_time_number = try_time                                  #复制变量表示猜测次数
    while try_time_number:                                      #猜测次数不为0时循环
        try_time_number = try_time_number - 1                   #猜测次数减一
        num = int(input('input a int number please:'))          #等待玩家输入答案
        if number == num:            #如果相等
            print('You win')         #输出你赢了
            break                    #跳出循环进入下一关
        elif number > num:           #如果输入值小
            print('Too small')       #提示太小
        elif number < num:           #如果输入值大
            print("Too big")         #输出太大
        else:                        #如果上面所有条件都不符合
            print('input error')     #提示输入错误
    
    else:                            #如果上面所有循环中都没有猜中
        print('You are lost')        #显示你输了
        print('''
        Game Over!!!                 
        ''')                         #显示游戏结束
        break                        #跳出循环
