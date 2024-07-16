from game import Game
# モンスターリストクラス
class MonsterList:
    
    # モンスターリストの番号
    MON_NO_LADYBUG = 0
    MON_NO_BIRD = 1
    MON_NO_DOKINCHAN = 2
    MON_NO_NIZI_NEZUMI = 3
    
    # モンスター情報取得関数各種
    @classmethod
    def get_monster_name(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][0]
    @classmethod
    def get_monster_image_list(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][1]
    @classmethod
    def get_monster_move_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][2]
    @classmethod
    def get_monster_dir_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][3]
    @classmethod
    def get_monster_stop_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][4]
    @classmethod
    def get_monster_unmovable_chips(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][5]
    @classmethod
    def get_monster_attack_power(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][6]
    @classmethod
    def get_monster_hp(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][7]
    @classmethod
    def get_monster_battle_image_file(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][8]
    @classmethod
    def get_monster_battle_image_size(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][9]
    
    # =============== モンスター情報 ===============
    # 名前
    # マップ上での画像リスト
    # 移動間隔時間
    # 方向変更間隔時間
    # 停止時間
    # 移動出来ないマップデータのリスト
    # 攻撃力
    # ＨＰ
    # 戦闘時の画像ファイル
    # 戦闘時の画像サイズ
    
    # オブジェクト
    bubu = (
        'car',
        (Game.read_image_for_square('image/bubu.png'),
        Game.read_image_for_square('image/bubu.png')),
        5,
        100,
        5,
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
        1,
        25,
        'image/bubu.png',
        (285//3, 320//3)
    )

    # モンスター２
    MONSTER_BIRD = (
        'Bird',
        (Game.read_image_for_square('image/enemy5.png'),
        Game.read_image_for_square('image/enemy5.png')),
        2,
        12,
        5,
        [],
        2,
        10,
        'image/enemy5.png',
        #(440, 540)
        (440//3, 540//3)
    )
    MONSTER_DOKINCHAN = (
        '???',
        (Game.read_image_for_square('image/enemy6.png'),
        Game.read_image_for_square('image/enemy6.png')),
        4,
        4,
        4,
        [3],
        30,
        1000,
        'image/enemy6.png',
        #(440, 540)
        (440//3, 540//3)
    )
    MONSTER_NIZI_NEZUMI = (
        'にじいろねずみ',
        (Game.read_image_for_square('image/enemy7.png'),
        Game.read_image_for_square('image/enemy7.png')),
        2,
        2,
        2,
        [3],
        5,
        1,
        'image/enemy7.png',
        #(440, 540)
        (440//3, 540//3)
    )

    # モンスターリスト
    MONSTER_LIST = (
        bubu,
        MONSTER_BIRD,
        MONSTER_DOKINCHAN,
        MONSTER_NIZI_NEZUMI
    )