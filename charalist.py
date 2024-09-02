from game import Game
# モンスターリストクラス
class CharaList:
    
    # モンスターリストの番号
    CHA_NO_FATHER = 0
    CHA_NO_MOTHER = 1
    CHA_NO_DAUGHTER = 2
    CHA_NO_BOY = 3
    CHA_NO_GIRL = 4
    CHA_NO_MAN = 5
    CHA_NO_WOMAN = 6
    CHA_NO_CAR = 7
    
    # モンスター情報取得関数各種
    @classmethod
    def get_chara_name(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][0]
    @classmethod
    def get_chara_image_list(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][1]
    @classmethod
    def get_chara_move_interval(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][2]
    @classmethod
    def get_chara_dir_interval(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][3]
    @classmethod
    def get_chara_stop_interval(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][4]
    @classmethod
    def get_chara_unmovable_chips(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][5]
    @classmethod
    def get_chara_attack_power(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][6]
    @classmethod
    def get_chara_hp(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][7]
    @classmethod
    def get_chara_battle_image_file(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][8]
    @classmethod
    def get_chara_battle_image_size(cls, chara_no):
        return CharaList.CHARA_LIST[chara_no][9]
    
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
    CHARA_FATHER = [
        'お父さん',
        (Game.read_image_for_square('image/father.png'),
        Game.read_image_for_square('image/father.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/father.png',
        #(440, 540)
        (440//3, 540//3)
    ]

    # モンスター２
    CHARA_MOTHER = [
        'お母さん',
        (Game.read_image_for_square('image/mother.png'),
        Game.read_image_for_square('image/mother.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/mother.png',
        #(440, 540)
        (440//3, 540//3)
    ]
    CHARA_DAUGHTER = [
        '妹',
        (Game.read_image_for_square('image/daughter.png'),
        Game.read_image_for_square('image/daughter.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/daughter.png',
        #(440, 540)
        (440//3, 540//3)
    ]
    CHARA_BOY = [
        '男の子',
        (Game.read_image_for_square('image/boy.png'),
        Game.read_image_for_square('image/boy.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/boy.png',
        (285//3, 320//3)
    ]
    CHARA_GIRL=[
        '女の子',
        (Game.read_image_for_square('image/girl.png'),
        Game.read_image_for_square('image/girl.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/girl.png',
        (285//3, 320//3)
    ]
    CHARA_MAN=[
        'お兄さん',
        (Game.read_image_for_square('image/man.png'),
        Game.read_image_for_square('image/man.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/man.png',
        (285//3, 320//3)
    ]
    CHARA_WOMAN=[
        'お姉さん',
        (Game.read_image_for_square('image/woman.png'),
        Game.read_image_for_square('image/woman.png')),
        10,
        5,
        5,
        [0,1,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        1,
        25,
        'image/woman.png',
        (285//3, 320//3)
    ]
    CHARA_CAR = [
        '車',
        (Game.read_image_for_square('image/bubu.png'),
        Game.read_image_for_square('image/bubu.png')),
        1,
        1000,
        0,
        [1,2,54,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
        1,
        25,
        'image/bubu.png',
        (285//3, 320//3)
    ]
    # モンスターリスト
    CHARA_LIST = (
        CHARA_CAR,
        CHARA_FATHER,
        CHARA_MOTHER,
        CHARA_DAUGHTER,
        CHARA_BOY,
        CHARA_GIRL,
        CHARA_MAN,
        CHARA_WOMAN

    )