import random


"""卡池内容（未设置四星up角色）"""
up = '魈'
st5 = [up, up, up, up, up, '刻晴', '莫娜', '七七', '迪卢克', '琴']
cha_4 = ['安柏', '丽莎', '凯亚', '芭芭拉', '雷泽', '菲谢尔', '班尼特', '诺艾尔', '菲谢尔', '砂糖',
         '迪奥娜', '北斗', '凝光', '香菱', '行秋', '重云', '辛焱']
weapon_4 = ['弓藏', '祭礼弓', '绝弦', '西风猎弓', '昭心', '祭礼残章', '流浪乐章', '西风秘典', '西风长枪',
            '雨裁', '匣里灭辰', '祭礼大剑', '钟剑', '西风大剑', '匣里龙吟', '祭礼剑', '笛剑', '西风剑', '岩盔丘丘王']
st4 = weapon_4 + cha_4
get = []
have = []


class Stats:
    """跟踪游戏统计信息"""
    def __init__(self):
        self.total = 0
        self.up_num = 0
        self.num_4 = 0
        self.num_5 = 0


def single():
    """不保底时的抽奖"""
    i = random.randint(1, 10001)
    if i in range(1, 61):
        a = random.randint(1, 6)
        star = st5[a]
        stat.num_5 = 0
    elif i in range(61, 316):
        cha = random.randint(1, len(cha_4)+1)
        star = cha_4[cha]
        stat.num_4 = 0
    elif i in range(316, 571):
        wea = random.randint(1, len(weapon_4)+1)
        star = weapon_4[wea]
        stat.num_4 = 0
    elif i in range(571, 10001):
        star = '三星'
    else:
        return None
    if star == up:
        stat.num_5 = 0
        stat.up_num = 0
    add(star)


def add(star):
    """每次抽卡完毕的常规操作"""
    record(star)
    get.append(star)
    have.append(star)
    stat.total += 1


def check_up():
    """检查保底"""
    if stat.up_num < 179:
        if stat.num_5 < 89:
            if stat.num_4 < 9:
                single()
            else:
                o_4 = random.randint(0, len(st4) - 1)
                star = st4[o_4]
                add(star)
                stat.num_4 = 0
        else:
            o_5 = random.randint(0, len(st5) - 1)
            star = st5[o_5]
            add(star)
            stat.num_5 = 0
    else:
        star = up
        add(star)
        stat.up_num = 0


def record(star):
    """记录数据变化"""
    if star != '魈':
        stat.up_num += 1
    if star not in st4:
        stat.num_4 += 1
    if star not in st5:
        stat.num_5 += 1


def extract():
    """单抽"""
    del get[:]
    check_up()
    print(get)


def ten():
    """十连函数"""
    del get[:]
    for num in range(0, 10):
        check_up()
    print(get)


def remember():
    value_cnt = {}
    for h in have:
        value_cnt[h] = value_cnt.get(h, 0) + 1
    print(value_cnt)


stat = Stats()
