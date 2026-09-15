#导入库区
from random import randint#导入随机数模块
from time import sleep#导入时间库

#初始化变量区
max_human = 12#限载人数
now_inside_human = 0#初始化目前在电梯内的人数
go_out_human = 0#初始化离开电梯的人数
waiting_time_for_every_floor = 1#设置每层楼的等待时间
loader = '-------------------------------------------------'
floor_now = 1#初始化当前楼层
floor_going = 0#初始化即将前往的楼层
floors = 20#设置层数
waiting_time = 0#初始化等待时间（总）

#函数/模块定义区
def update_info():#当前版本更新信息
    print('Beta2.0.2更新说明(Oct 26th 2023)')
    print('修复了同楼层的判断问题')
    print('优化了内存占用')
    print('优化了内部结构')
def update_info_history():#版本更新历史信息
    print('Beta2.0.1更新说明(Oct 24th 2023)')
    print('修复了目前在电梯内总人数计算错误的问题')
def welcome():#欢迎信息
    print('欢迎使用电梯模拟器！')
    print('一款模拟电梯的模拟器！')
    #print('帮助：电梯不可超载哦！运载的人越多，金币更多，同时电梯也会老化哦！使用金币可以维修和升级电梯哦！！！限载12人哦！')
    #这是历史,但也可能是未来.
    #update_info()
    print(loader)
def random_events():#随机事件
    events = randint(1,10)
    pass
def set_human_numbers():
    global now_inside_human
    global enter_human
    global go_out_human
    enter_human = randint(0, max_human - now_inside_human)  # 设置进入电梯人数
    go_out_human = randint(0, now_inside_human)  # 设置离开电梯人数
    now_inside_human = now_inside_human - go_out_human + enter_human  # 计算电梯内的人数

def set_floors_and_judge():
    global floor_going
    global floor_now
    global waiting_time
    floor_going = randint(1,floors)
    if floor_now > floor_going:
        waiting_time = waiting_time_for_every_floor *(floor_now - floor_going)
    elif floor_now == floor_going:
        pass
    else:
        waiting_time = waiting_time_for_every_floor * (floor_going - floor_now)

def set_user_settings():
    pass

def output():
    pass

#主程序
print(loader)
welcome()
while True:
    set_human_numbers()
    set_floors_and_judge()
    print('当前正在第'+str(floor_now)+'层楼')
    print('有' + str(enter_human) + '人进入了电梯')
    print('有' + str(go_out_human) + '人离开了电梯')
    print('共有'+ str(now_inside_human)+'人在电梯内')#这几个print负责输出
    print('正前往第'+str(floor_going)+'层楼')
    print('请耐心等待'+str(waiting_time)+'秒钟')
    print(loader)#分割线
    sleep(waiting_time)#等待时间
    floor_now = floor_going#设置当前楼层



    
        

