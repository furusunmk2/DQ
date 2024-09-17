import random
from game import Game, Phase
from character import Character
from charalist import CharaList
import field
import pygame
pos_num_list=[(),(),(),(),(),(),(),(),()]
# モンスタークラス
class Chara(Character):
    # 移動方向リスト
    MOVE_DIR_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    MOVE_DIR_LIST2 = [(-1, 0), (0, 1), (0, -1)]
    MOVE_DIR_LIST_FIRE = [(1, 0), (-1, 0),  (0, -1)]
    DIR_flg = 0
    FIRE_DIR = 0
    # コンストラクタ
    def __init__(self, pos, chara_no):
        # Ｈ－９６最初）親クラスのコンストラクタを呼び出し
        super().__init__()
        # Ｈ－９７）モンスター番号を設定
        self.chara_no = chara_no
        
        # Ｈ－９８）モンスターの位置を設定（親クラスのメソッド）
        self.set_pos(pos[0], pos[1])
        # Ｈ－９９）次移動開始時間
        self.next_move_count = 0
        # Ｈ－１００）移動方向
        self.move_x, self.move_y = 0, 0
        # Ｈ－１０１下へ）残り移動回数
        self.remain_move_time = 0
        # コリジョンふらぐ
        self.coli_flg = 0
        # ===== CharaList クラスから、モンスターの情報を取得する =====
        # モンスターの画像を作成＆設定
        cha_images = CharaList.get_chara_image_list(chara_no)
        self.set_image_list(cha_images)
        # 名前
        self.name = CharaList.get_chara_name(chara_no)
        # 攻撃力
        self.attack_power = CharaList.get_chara_attack_power(chara_no)
        # ヒットポイント
        self.hp = CharaList.get_chara_hp(chara_no)
        # 移動不能チップリスト
        self.unmovable_chips = CharaList.get_chara_unmovable_chips(chara_no)
        # 移動インターバル
        self.move_interval = CharaList.get_chara_move_interval(chara_no)
        # 移動方向変更タイミング
        self.direction_interval = CharaList.get_chara_dir_interval(chara_no)
        # 移動後停止時間
        self.stop_interval = CharaList.get_chara_stop_interval(chara_no)
        # 戦闘時の画像
        self.battle_image_file = CharaList.get_chara_battle_image_file(chara_no)
        # 戦闘時の画像サイズ
        self.battle_image_size = CharaList.get_chara_battle_image_size(chara_no)

    # マップ移動チェック
    # プレイヤーのマップ移動チェックと同様だが、
    # マップ外に出る場合にマップを変更しない
    def check_map_move(self, posx, posy, dx, dy):
        # 右マップへ移動してしまう（一番右＋dxが正）
        if posx == Game.FIELD_WIDTH - 1 and dx > 0:
            self.set_pos(-100, -100)
            self.set_dpos(0, 0)
            return
        # 左マップへ移動（一番左より左）
        if posx < 0:
            self.set_pos(-100, -100)
            self.set_dpos(0, 0)
            return
        # 下マップへ移動（一番下＋dyが正）
        if posy == Game.FIELD_HEIGHT - 1 and dy > 0:
            self.set_pos(-100, -100)
            self.set_dpos(0, 0)
            return
        # 上マップへ移動（一番上より上）
        if posy < 0:
            self.set_pos(-100, -100)
            self.set_dpos(0, 0)
            return
        return True

    # １フレームごとにする画像・処理
    def frame_process_img(self):
        # Ｉ－１０６最初）移動中でない場合
        if self.move_x == 0 and self.move_y == 0:
            # Ｉ－１０７）移動タイミングを超えている場合
            if self.next_move_count <= Game.count:
                # Ｉ－１０８）移動方向をランダムに設定
                if self.chara_no == 7:
                    self.move_x, self.move_y = (-1, 0)
                elif field.Field.MAP4[3][5] in [48]:
                    if Game.field.map_no == 5:
                        if Chara.DIR_flg == 1:
                            self.move_x, self.move_y = (-1, 0)
                        else:
                            if self.chara_no == 5 :
                                if 0 <= self.pos[0] <= 14 :
                                    if not self.check_chara_move(self.pos[0],self.pos[1], self.dxy[0], self.dxy[1], [95,97]):
                                        self.move_x, self.move_y = (-1, 0)
                                        Chara.DIR_flg = 1
                                    else:
                                        self.move_x, self.move_y = (0, -1)
                            if self.chara_no == 6 :
                                if 0 <= self.pos[0] <= 14 :
                                    
                                        self.move_x, self.move_y = (0, -1)   
                        if self.chara_no == 3 or self.chara_no == 4:
                                self.move_x, self.move_y = (-1, 0)       
                    elif Game.field.map_no == 4:
                        self.move_x, self.move_y = (1, 0)
                    
                elif Game.field.map_no == 1: 
                        if Game.player.map1_flg == 0:
                            self.move_x, self.move_y = (1, 0)
                        elif Game.player.map1_flg == 1:
                            if 0 <= self.pos[1] <= 13 :
                                if not self.check_chara_move(self.pos[0],self.pos[1], self.dxy[0], self.dxy[1], [99]):
                                    self.move_x, self.move_y = (0, -1)
                            
                            else:
                                self.move_x, self.move_y = (-1, 0)
                        
                     
                elif Game.field.map_no == 2:
                        Game.player.map1_flg = 1
                        if  self.chara_no in [0,1,2,3,4,5,6]:
                            self.move_x, self.move_y = (-1, 0)
                        else:
                            if self.FIRE_DIR == 0:
                                self.move_x, self.move_y = random.choice(Chara.MOVE_DIR_LIST_FIRE)
                                self.FIRE_DIR = 1
                            elif self.FIRE_DIR == 1:
                                self.move_x, self.move_y = random.choice(Chara.MOVE_DIR_LIST_FIRE)
                                self.FIRE_DIR = 2    
                            elif self.FIRE_DIR == 2:
                                self.move_x, self.move_y = random.choice(Chara.MOVE_DIR_LIST_FIRE)
                                self.FIRE_DIR = 3      
                            else:
                                self.move_x, self.move_y = (-1,0)
                                self.FIRE_DIR = 0
                
                elif  Game.field.MAP5_flg2 == 1:
                    self.move_x, self.move_y = (0, 1) 
                else:
                    self.move_x, self.move_y = random.choice(Chara.MOVE_DIR_LIST)
                # Ｉ－１０９）残り移動回数を設定
                self.remain_move_time = self.direction_interval
        # Ｉ－１１０）移動中の場合
        else:
            # Ｉ－１１１）移動タイミングを超えている場合
            if self.next_move_count <= Game.count:
                # Ｉ－１１２）現在位置を取得
                posx, posy = self.get_pos()
                dx, dy = self.get_dpos()
                # Ｉ－１１３）移動方向に仮移動
                dx += Character.MOVE_STEP * self.move_x
                dy += Character.MOVE_STEP * self.move_y
                if self.chara_no == 8:
                    if 0<= posy <=14 and 0<= posx <= 15:
                        if field.Field.MAP2[posy][posx] in [74,8]:
                            field.Field.MAP2[posy][posx] = 69
                            Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]
                            Game.field.read_map_info()
                            Game.field.draw()  
                            pygame.display.update()
                        if field.Field.MAP2[posy][posx] ==  105:
                            field.Field.MAP2[posy][posx] = 94
                            Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]
                            Game.field.read_map_info()
                            Game.field.draw()  
                            pygame.display.update()    
                        if field.Field.MAP2[posy][posx] in [20,21,22,23,30,31,32,33,40,41,42,43] :
                            field.Field.MAP2[posy][posx] += 70
                            Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]
                            Game.field.read_map_info()
                            Game.field.draw()  
                            pygame.display.update()
                    
                    
                # Ｊ－１３２Fieldから）モンスターとプレイヤーの四角を取得
                chara_rect = self.get_rect()
                player_rect = Game.player.get_rect()
                pos_num_list[self.chara_no]=self.pos
                # for rect_other in range(len(pos_num_list)):
                #     if self.chara_no==rect_other:
                #         continue

                #     elif self.pos == pos_num_list[rect_other]:
                #         dx -= Character.MOVE_STEP * self.move_x *3
                #         dy -= Character.MOVE_STEP * self.move_y *3
                        
                        
                    
                # Ｊ－１３３）重なった場合
                if chara_rect.colliderect(player_rect):
                    self.coli_flg = self.chara_no
                    return
                    
                else:
                    self.coli_flg = 7
                    # Ｉ－１１４）加算後の値で、位置を計算
                    posx, posy, dx, dy = self.calc_chara_pos(posx, posy, dx, dy)
                    # Ｉ－１１５）マップ移動チェックで移動可能な場合
                    # ※Charaクラスのマップ移動チェックは用意済み
                    # Playerと同様だが、マップ移動してしまう場合は移動不可としている
                    if self.check_map_move(posx, posy, dx, dy):
                        # Ｉ－１１６）移動可能チェックで移動可能の場合
                        if self.check_chara_move(posx, posy, dx, dy, self.unmovable_chips):
                            # Ｉ－１１７）移動後の位置を設定する（移動不可なら位置を変更しない）
                            self.set_pos(posx, posy)
                            self.set_dpos(dx, dy)

                # Ｉ－１１８）残り移動回数を１減算
                self.remain_move_time -= 1
                # Ｉ－１１９）移動回数が０になったら
                if self.remain_move_time == 0:
                    # Ｉ－１２０）次の移動タイミングを停止時間後に設定
                    self.next_move_count = Game.count + self.stop_interval
                    # Ｉ－１２１）移動方向をなしに
                    self.move_x, self.move_y = 0, 0
                # Ｉ－１２２）移動回数が０でない場合
                else:
                    # Ｉ－１２３最後）次の移動タイミングを設定
                    self.next_move_count = Game.count + self.move_interval
        
        # Ｊ－１３２Fieldから）モンスターとプレイヤーの四角を取得
        chara_rect = self.get_rect()
        
        player_rect = Game.player.get_rect()
        # Ｊ－１３３）重なった場合キャラは動かなくなる
        if chara_rect.colliderect(player_rect):
            self.move_x, self.move_y = 0, 0
            self.coli_flg = self.chara_no
 
        #     # Ｊ－１３４）モンスターを画面外に
        #     # （画面外に設定すると、移動チェックで出てこれなくなる）
        #     self.set_pos(-100, -100)
        #     self.set_dpos(0, 0)
            # # Ｋ－１３７最初）戦闘フェイズにする
            # Game.phase = Phase.IN_BATTLE
            # # Ｋ－１３８）戦闘処理の初期化
            # Game.battle.init_data()
            # # Ｌ－１４８最初Battleへ）戦闘クラスに、モンスター情報を設定
            # Game.battle.set_chara(self)
            
            # # # Ｋ－１３９Battleへ）戦闘画面化するので、下の処理をコメントにする
            # # # Ｊ－１３５）プレイヤーのHPをモンスターの攻撃力分減らす
            # # Game.player.hp -= self.attack_power
            # # # Ｊ－１３６最後）プレイヤーのHPが０以下になったら、フェイズをゲームオーバーにする
            # # if Game.player.hp <= 0:
            # #     Game.phase = Phase.GAME_OVER
        
        # Ｈ－１０２mainへ）キャラクターの画像設定
        self.set_chara_animation()
