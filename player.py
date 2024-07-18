import pygame
from pygame.locals import Rect, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_RETURN
import time
from character import Character
from game import Game, Phase
import field
import chip
import monster
import selif

# Pygameの初期化
pygame.init()

# フォントの初期化
selif_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 24)

# プレイヤークラス
class Player(Character):
    # 移動不能チップの番号リスト（チップの番号と合わせること）
    UNMOVABLE_CHIP_LIST = [1, 3, 7, 10, 12, 14, 4, 18, 19, 20, 21, 22, 23, 25, 30, 31, 32, 33, 40, 41, 42, 43]
    FIELD_DAMEGE_LIST = [4]
    MONSTER_UNMOVABLE_CHIP_LIST = [0, 2, 3]
    TAKARABAKO_LIST = [5]
    OTOSHIMONO_LIST = [8]
    DOOR_LIST = [7]
    END_LIST = [6]

    # 初期レベル
    PLAYER_LV_1ST = 1
    # 初期ヒットポイント
    if PLAYER_LV_1ST == 1:
        PLAYER_HP_1ST = 13
    else:
        PLAYER_HP_1ST = 10

    epi_flg = 0
    start_flg = 0
    event_flg = 0
    end_flg = 0
    MAP2_flg = 0
    MAP5_flg = 0
    MAP8_flg = 0
    doku_flg = 0
    takarabako_flg = 0
    otoshimono_flg = 0
    door_flg = 0
    item_flg1 = 0
    item_flg2 = 0
    item_flg3 = 0
    kagi_flg = 0
    kutsu_flg = 0
    mapnumber = 1
    MAP8_flg2 = 0
    end_flg = 0
    selif_flg = 0  # セリフフラグの初期化
    enter_key_pressed = False  # エンターキー押下状態のフラグ

    # コンストラクタ
    def __init__(self):
        super().__init__()
        self.set_pos(Game.START_PLAYER_POS_X, Game.START_PLAYER_POS_Y)
        self.level = Player.PLAYER_LV_1ST
        self.hp = Player.PLAYER_HP_1ST
        pl_images = (Game.read_image_for_square('image/hero1.png'),
                     Game.read_image_for_square('image/hero2.png'))
        self.set_image_list(pl_images)

    # １フレームごとにする画像・処理
    def frame_process_img(self):
        posx, posy = self.get_pos()
        dx, dy = self.get_dpos()

        if self.epi_flg == 1:
            field.Field.MAP5[5][6] = 2
            field.Field.MAP5[5][7] = 2
            field.Field.MAP5[5][8] = 2

        if Game.on_downkey():
            dy += Character.MOVE_STEP
            self.doku_flg += 1
        elif Game.on_upkey():
            dy -= Character.MOVE_STEP
            self.doku_flg += 1
        elif Game.on_rightkey():
            dx += Character.MOVE_STEP
            self.doku_flg += 1
        elif Game.on_leftkey():
            dx -= Character.MOVE_STEP
            self.doku_flg += 1

        posx, posy, dx, dy = self.calc_chara_pos(posx, posy, dx, dy)
        posx, posy, dx, dy, is_changed = self.check_map_move(posx, posy, dx, dy)

        if not is_changed:
            if self.check_chara_move(posx, posy, dx, dy, Player.UNMOVABLE_CHIP_LIST):
                self.set_pos(posx, posy)
                self.set_dpos(dx, dy)
            if not self.check_chara_move_damege(posx, posy, dx, dy, Player.FIELD_DAMEGE_LIST):
                print(self.doku_flg)
                if self.doku_flg > 10:
                    print(1234567890)
                    se = pygame.mixer.Sound("doku.mp3")
                    se.play()
                    self.hp -= 1
                    self.doku_flg = 0
                    if self.hp <= 0:
                        Game.on_enterkey() or Game.on_spacekey()
                        Game.phase = Phase.GAME_OVER
                        pygame.mixer.init()
                        pygame.mixer.music.load('game_over.mp3')
                        pygame.mixer.music.play(-1)

            if Player.kagi_flg == 1:
                if not self.check_chara_move(posx, posy, dx, dy, Player.DOOR_LIST):
                    field.Field.MAP8[4][1] = 0
                    field.Field.MAP8[5][1] = 0
                    Player.MAP8_flg = 1
                    Player.item_flg3 = 1
            if Player.end_flg == 1:
                if not self.check_chara_move(posx, posy, dx, dy, Player.END_LIST):
                    field.Field.MAP8[4][5] = 9
                    Player.MAP8_flg2 = 1
                    se = pygame.mixer.Sound("kaifuku.mp3")
                    se.play()
                    Game.phase = Phase.GAME_CLEAR

            for mon in Game.monsters:
                if mon.coli_flg > 0:
                    if self.selif_flg >= 1:
                        Game.surface.blit(selif_font.render(selif.list[mon.coli_flg][0],
                                                            True, (255, 255, 255)), (1000, 230))
                        if Game.on_enterkey() and not self.enter_key_pressed:
                            self.selif_flg = 0
                            self.enter_key_pressed = True
                    elif Game.on_enterkey() and not self.enter_key_pressed:
                        self.selif_flg += 1
                        self.enter_key_pressed = True
                if not Game.on_enterkey():
                    self.enter_key_pressed = False
        else:
            self.set_pos(posx, posy)
            self.set_dpos(dx, dy)

        self.set_chara_animation()


    # マップ移動チェック
    def check_map_move(self, posx, posy, dx, dy):
        # Ｆ－６９Fieldから）マップ変更フラグ
        is_changed = True
        # Ｆ－７０）右マップへ移動（一番右＋dxが正）
        if posx == Game.FIELD_WIDTH - 1 and dx > 0:
            # Ｆ－７１）マップを右へ、プレイヤー位置を左へ
            Game.field.change_field(1, 0)
            posx, dx = 0, 0
        # Ｆ－７２）左マップへ移動（一番左より左）
        elif posx < 0:
            # Ｆ－７３）マップを左へ、プレイヤー位置を右へ
            Game.field.change_field(-1, 0)
            posx, dx = Game.FIELD_WIDTH - 1, 0
        # Ｆ－７４）下マップへ移動（一番下＋dyが正）
        elif posy == Game.FIELD_HEIGHT - 1 and dy > 0:
            # Ｆ－７５）マップを下へ、プレイヤー位置を上へ
            Game.field.change_field(0, 1)
            posy, dy = 0, 0
        # Ｆ－７６）上マップへ移動（一番上より上）
        elif posy < 0:
            # Ｆ－７７）マップを上へ、プレイヤー位置を下へ
            Game.field.change_field(0, -1)
            posy, dy = Game.FIELD_HEIGHT - 1, 0
        # Ｆ－７８）どれにも当てはまらない場合
        else:
            # Ｆ－７９）マップ変更なし
            is_changed = False

        # Ｆ－８０上へ）マップ変更後（変更してない場合も）の位置と変更フラグを返却
        return posx, posy, dx, dy, is_changed
