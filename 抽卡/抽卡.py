import main
from time import sleep


symbol = True

print('正在加载配置文件...')
sleep(1)
print('欢迎使用《原神》模拟抽卡系统，随时输入q以退出')
while symbol:
    print('请输入对应字母以进入相应功能：\n[A]开始祈愿\t[B]祈愿记录\t[q]退出')
    msg = input('')
    if msg.title() == 'A':
        yi = input('请选择：\n[A]祈愿1次\t[B]祈愿10次\n')
        if yi.title() == 'A':
            main.extract()
            continue
        elif yi.title() == 'B':
            main.ten()
            continue
        elif yi.title() == 'q':
            break
        else:
            print('请输入正确的选项！')
            continue
    if msg.title() == 'B':
        num = len(main.have)
        print('您已进行' + str(num) + '次祈愿')
        print(main.have)
        print('其中有:')
        main.remember()
        sleep(2)
        continue
    if msg == 'q':
        break
print('感谢您使用模拟抽卡系统，祝您游戏愉快！')
sleep(1.5)
