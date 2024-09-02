import pygame
from pygame.locals import Rect, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_RETURN
import time
from character import Character
from game import Game, Phase
import field
import chip
from chara import Chara
import selif
from charalist import CharaList

# Pygameの初期化
pygame.init()
epi_flg_list=[1,"","","","","","",""]
# フォントの初期化
selif_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 24)
# mac
# selif_font = pygame.font.Font('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 24)
# プレイヤークラス
class Player(Character):
    # 移動不能チップの番号リスト（チップの番号と合わせること）
    UNMOVABLE_CHIP_LIST = [1, 7, 10,12, 14, 4, 18, 19, 20, 21, 22, 23, 25, 30, 31, 32, 33, 40, 41, 42, 43,45,47,48,52,54,57,58,65,67]
    FIELD_DAMEGE_LIST = [3,55,56]
    SLOW_LIST = [3]
    CHARA_UNMOVABLE_CHIP_LIST = [0, 2, 3]
    epi_LIST = [44]
    QUAKE_LIST= [26,46]
    DOURO_LIST = [0]
    SUNAHAMA_LIST = [2,13,26,46,3,53]
    OTOSHICHARAO_LIST = [8]
    HAKUSEN_LIST = [16]
    HAKUSEN_LIST2 = [49]
    HAKUSEN_LIST3 = [50]
    HAKUSEN_LIST4 = [51]
    TOUBOKU_LIST_R = [34]
    TOUBOKU_LIST_L = [35]
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
    MAP4_flg = 0
    MAP5_flg = 0
    QUAKE_flg = 0
    QUAKE = 0
    SUNAHAMA_LIST
    COUNT_DOWN = 0
    start_time = 0
    end_time = 0
    TSUNAMI_flg = 0
    TOUBOKU_flg = 0
    clear_flg = 0
    MAP8_flg = 0
    doku_flg = 0
    epi_flg = 0
    otoshichao_flg = 0
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
    selif_num =0
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

        # if self.epi_flg == 1:
        #     field.Field.MAP5[5][6] = 2
        #     field.Field.MAP5[5][7] = 2
        #     field.Field.MAP5[5][8] = 2

        if Game.on_downkey():
            dy += Character.MOVE_STEP*0.5
            self.doku_flg += 1
        elif Game.on_upkey():
            dy -= Character.MOVE_STEP*0.5
            self.doku_flg += 1
        elif Game.on_rightkey():
            dx += Character.MOVE_STEP*0.5
            self.doku_flg += 1
        elif Game.on_leftkey():
            dx -= Character.MOVE_STEP*0.5
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










            if int("".join(map(str,epi_flg_list)))== 10000000 :
                field.Field.MAP4[10][2] = 44
                Player.MAP4_flg = 1
                epi_flg_list.append(1)
                
            if Player.MAP4_flg ==1:
                if not self.check_chara_move(posx, posy, dx, dy, Player.epi_LIST):
                    if Game.on_enterkey() and not self.enter_key_pressed:
                        field.Field.MAP5[5][6] = 11
                        field.Field.MAP5[5][7] = 11
                        field.Field.MAP5[5][8] = 11
                        field.Field.MAP4[10][2] = 13
                        Player.MAP5_flg = 1
                        Player.QUAKE_flg = 1
                        field.Field.MAP4[10][8] = 46
                        field.Field.MAP4[9][8] = 26
                        field.Field.MAP4[8][8] = 26
                        field.Field.MAP4[7][8] = 26
                        field.Field.MAP4[6][8] = 26
                        field.Field.MAP4[10][9] = 46
                        field.Field.MAP4[9][9] = 26
                        field.Field.MAP4[8][9] = 26
                        field.Field.MAP4[7][9] = 26
                        field.Field.MAP4[6][9] = 26
                        field.Field.MAP4[10][10] = 46
                        field.Field.MAP4[9][10] = 26
                        field.Field.MAP4[8][10] = 26
                        field.Field.MAP4[7][10] = 26
                        field.Field.MAP4[6][10] = 26
                        if Game.field.map_no == 4:
                            Game.field.map_no = 4
                            Game.field.new_field = field.Field.MAP_LIST[4]
                            Game.field.read_map_info()
                            Game.field.draw()
                            Player.MAP4_flg =0
                       
            if Player.TSUNAMI_flg == 0:             
                if not self.check_chara_move(posx, posy, dx, dy, Player.QUAKE_LIST):
                    if Player.QUAKE_flg == 1: 
                        if not Player.start_time ==0:
                            Player.end_time = time.time()
                        if 0 <= Player.end_time - Player.start_time <=5:
                                Player.QUAKE = 1

                                field.Field.chip_list = [[field.Chip() for _ in range(Game.FIELD_WIDTH)] \
                                                for _ in range(Game.FIELD_HEIGHT)]
                                for y in range(Game.FIELD_HEIGHT):
                                    for x in range(Game.FIELD_WIDTH):
                                        # Ａ－２３）位置と初期画像を指定
                                        field.Field.chip_list[y][x].set_pos(x+1, y+0.5)
                                        field.Field.chip_list[y][x].set_chip_no(0)
                                pygame.mixer.music.load('bgm.mp3')
                                pygame.display.update()
                                Player.selif_num = 1
                                Game.surface.blit(selif_font.render("お兄さん",
                                                                True, (255, 255, 255)), (1000, 230))
                                Game.surface.blit(selif_font.render("地震だー！！",
                                                                True, (255, 255, 255)), (1000, 280))
                                Game.surface.blit(selif_font.render("お姉さん",
                                                                True, (255, 255, 255)), (1000, 330))
                                Game.surface.blit(selif_font.render("津波が来るわよ！",
                                                                True, (255, 255, 255)), (1000, 380))
                                if 0 == Player.start_time:
                                    Player.start_time = time.time()
                                Player.COUNT_DOWN = 0
                                field.Field.MAP4[3][5] = 48
                                field.Field.MAP4[1][0] = 48
                                field.Field.MAP4[2][1] = 48
                                field.Field.MAP4[3][1] = 48
                                field.Field.MAP4[3][8] = 48
                                field.Field.MAP4[1][9] = 48
                                field.Field.MAP5[3][5] = 48
                                field.Field.MAP5[1][3] = 48
                                field.Field.MAP5[2][3] = 48
                                field.Field.MAP5[3][8] = 48
                                field.Field.MAP5[2][8] = 48
                                field.Field.MAP5[3][8] = 48
                                field.Field.MAP5[2][6] = 48

                                field.Field.MAP5[2][1] = 48
                                field.Field.MAP5[3][9] = 48
                                field.Field.MAP5[2][11] = 48
                                field.Field.MAP5[3][14] = 48
                                field.Field.MAP5[2][13] = 48
                                field.Field.MAP4[1][14] = 48
                                field.Field.MAP6[1][0] = 48
                                field.Field.MAP5[1][11] = 48
                                field.Field.MAP5[3][1] = 48
                                field.Field.MAP5[3][5] = 48
                                field.Field.MAP4[1][11] = 48
                                field.Field.MAP6[1][2] = 48
                                field.Field.MAP6[3][5] = 48
                                field.Field.MAP6[1][9] = 48
                                field.Field.MAP6[3][5] = 48
                                field.Field.MAP6[1][12] = 47
                                field.Field.MAP6[2][12] = 47
                                field.Field.MAP6[3][12] = 47
                                Game.field.new_field = field.Field.MAP_LIST[4]
                                Game.field.read_map_info()
                                Game.field.draw()
                                pygame.display.update()

                                try:
                                    pygame.mixer.init()
                                    pygame.mixer.music.load('BGM2.mp3')   #BGMをロード
                                    pygame.mixer.music.play(-1)

                                except:
                                    print("ファイルが見当たらないか、オーディオ機器が接続されていません")

            if Player.TSUNAMI_flg == 0   :                      
                if Player.QUAKE_flg == 1:
                    if not self.check_chara_move(posx, posy, dx, dy, Player.SUNAHAMA_LIST):
                        if Game.field.map_no == 5 or Game.field.map_no == 6 or Game.field.map_no == 4:
                            if    field.Field.MAP6[3][12] == 47:
                                Game.surface.blit(selif_font.render("お父さん",
                                                                        True, (255, 255, 255)), (1000, 230))
                                Game.surface.blit(selif_font.render("こっちだー",
                                                                        True, (255, 255, 255)), (1000, 280))
                                Game.surface.blit(selif_font.render("お母さん",
                                                                        True, (255, 255, 255)), (1000, 330))
                                Game.surface.blit(selif_font.render("高い場所まで逃げてー",
                                                                        True, (255, 255, 255)), (1000, 380))

                            
            if Player.TSUNAMI_flg == 0 :            
                    # if not self.check_chara_move(posx, posy, dx, dy, Player.DOURO_LIST):
                    #     if field.Field.MAP5[5][6] == 45 or field.Field.MAP5[8][0] == 3 :
                    #         return
                    #     else:
                    #         # field.Field.MAP5[5][6] = 45
                    #         # field.Field.MAP5[5][7] = 45
                    #         # field.Field.MAP5[5][8] = 45
                    #         if field.Field.MAP5[10][1] == 13:
                    #             for i in range(15):
                    #                 if i==0:
                    #                     field.Field.MAP5[10][i] = 3
                    #                     field.Field.MAP6[10][i] = 3
                    #                     field.Field.MAP5[9][i] = 13
                    #                     field.Field.MAP6[9][i] = 13
                    #                 elif i==9 or i==10 or i==11 or i==12 or i==13:
                    #                     field.Field.MAP4[10][i] = 3
                    #                     field.Field.MAP5[10][i] = 3
                    #                     field.Field.MAP4[9][i] = 13
                    #                     field.Field.MAP5[9][i] = 13
                    #                 else:    
                    #                     field.Field.MAP4[10][i] = 3
                    #                     field.Field.MAP5[10][i] = 3
                    #                     field.Field.MAP6[10][i] = 3
                    #                     field.Field.MAP4[9][i] = 13
                    #                     field.Field.MAP5[9][i] = 13
                    #                     field.Field.MAP6[9][i] = 13
                    #         Game.field.new_field = field.Field.MAP_LIST[5]
                    #         Game.field.read_map_info()
                    #         Game.field.draw()  
                    #         pygame.display.update()
                    if not Player.start_time ==0:
                        Player.end_time = time.time()
                        if 10 <= Player.end_time - Player.start_time < 11:
                            if field.Field.MAP5[10][1] == 13:    
                                for i in range(15):
                                    if i==0:
                                        field.Field.MAP5[10][i] = 3
                                        field.Field.MAP6[10][i] = 3
                                        field.Field.MAP5[9][i] = 13
                                        field.Field.MAP6[9][i] = 13
                                    elif i==9 or i==10 or i==11 or i==12 or i==13:
                                        field.Field.MAP4[10][i] = 3
                                        field.Field.MAP5[10][i] = 3
                                        field.Field.MAP4[9][i] = 13
                                        field.Field.MAP5[9][i] = 13
                                    else:    
                                        field.Field.MAP4[10][i] = 3
                                        field.Field.MAP5[10][i] = 3
                                        field.Field.MAP6[10][i] = 3
                                        field.Field.MAP4[9][i] = 13
                                        field.Field.MAP5[9][i] = 13
                                        field.Field.MAP6[9][i] = 13
                            Game.field.new_field = field.Field.MAP_LIST[5]
                            Game.field.read_map_info()
                            Game.field.draw()  
                            pygame.display.update()  
                                         
            if   15 <= Player.end_time - Player.start_time < 16:
                if Player.TSUNAMI_flg == 0: 
                        if field.Field.MAP5[9][0] == 3:
                            return
                        else:
                            if field.Field.MAP5[9][1] == 13: 
                                for i in range(15):
                                    if i==0:
                                        field.Field.MAP5[9][i] = 3
                                        field.Field.MAP6[9][i] = 3
                                        field.Field.MAP5[8][i] = 13
                                        field.Field.MAP6[8][i] = 13
                                    elif i==9 or i==10 or i==11 or i==12 or i==13:
                                        field.Field.MAP4[9][i] = 3
                                        field.Field.MAP5[9][i] = 3
                                        field.Field.MAP4[8][i] = 13
                                        field.Field.MAP5[8][i] = 13
                                    else:    
                                        field.Field.MAP4[9][i] = 3
                                        field.Field.MAP5[9][i] = 3
                                        field.Field.MAP6[9][i] = 3
                                        field.Field.MAP4[8][i] = 13
                                        field.Field.MAP5[8][i] = 13
                                        field.Field.MAP6[8][i] = 13
                                Game.field.new_field = field.Field.MAP_LIST[5]
                                Game.field.read_map_info()
                                Game.field.draw()  
                                pygame.display.update()
                
            if   20 <= Player.end_time - Player.start_time < 21:
                if Player.TSUNAMI_flg == 0 :
                        if field.Field.MAP5[8][0] == 3:
                            return
                        else:
                            if field.Field.MAP5[8][1] == 13:
                                for i in range(15):
                                    if i==0:
                                        field.Field.MAP5[8][i] = 3
                                        field.Field.MAP6[8][i] = 3
                                        field.Field.MAP5[7][i] = 13
                                        field.Field.MAP6[7][i] = 13
                                    elif i==9 or i==10 or i==11 or i==12 or i==13:
                                        field.Field.MAP4[8][i] = 3
                                        field.Field.MAP5[8][i] = 3
                                        field.Field.MAP4[7][i] = 13
                                        field.Field.MAP5[7][i] = 13
                                    else:    
                                        field.Field.MAP4[8][i] = 3
                                        field.Field.MAP5[8][i] = 3
                                        field.Field.MAP6[8][i] = 3
                                        field.Field.MAP4[7][i] = 13
                                        field.Field.MAP5[7][i] = 13
                                        field.Field.MAP6[7][i] = 13
                                Game.field.new_field = field.Field.MAP_LIST[5]
                                Game.field.read_map_info()
                                Game.field.draw()  
                                pygame.display.update()
            if   25 <= Player.end_time - Player.start_time < 26:    
                if Player.TSUNAMI_flg == 0 :
                        if field.Field.MAP5[7][0] == 3:
                            return
                        else:
                            if field.Field.MAP5[7][1] == 13:
                                for i in range(15):
                                    if i==0:
                                        field.Field.MAP5[7][i] = 3
                                        field.Field.MAP6[7][i] = 3
                                        field.Field.MAP5[6][i] = 13
                                        field.Field.MAP6[6][i] = 13
                                    elif i==9 or i==10 or i==11 or i==12 or i==13:
                                        field.Field.MAP4[7][i] = 3
                                        field.Field.MAP5[7][i] = 3
                                        field.Field.MAP4[6][i] = 13
                                        field.Field.MAP5[6][i] = 13
                                    else:    
                                        field.Field.MAP4[7][i] = 3
                                        field.Field.MAP5[7][i] = 3
                                        field.Field.MAP6[7][i] = 3
                                        field.Field.MAP4[6][i] = 13
                                        field.Field.MAP5[6][i] = 13
                                        field.Field.MAP6[6][i] = 13
                                Game.field.new_field = field.Field.MAP_LIST[5]
                                Game.field.read_map_info()
                                Game.field.draw()  
                                pygame.display.update()
            
            if 30 <= Player.end_time - Player.start_time < 31:            
                if Player.TSUNAMI_flg == 0 :

                        if field.Field.MAP5[6][0] == 3:
                            return
                        else:
                            for i in range(15):
                                    if i==0:
                                        field.Field.MAP5[6][i] = 3
                                        field.Field.MAP6[6][i] = 3
                                        field.Field.MAP5[5][i] = 52
                                        field.Field.MAP6[5][i] = 52
                                    elif i==9 or i==10 or i==11 or i==12 or i==13:
                                        field.Field.MAP4[6][i] = 3
                                        field.Field.MAP5[6][i] = 3
                                        field.Field.MAP4[5][i] = 52
                                        field.Field.MAP5[5][i] = 52
                                    else:    
                                        field.Field.MAP4[6][i] = 3
                                        field.Field.MAP5[6][i] = 3
                                        field.Field.MAP6[6][i] = 3
                                        field.Field.MAP4[5][i] = 52
                                        field.Field.MAP5[5][i] = 52
                                        field.Field.MAP6[5][i] = 52
                                        field.Field.MAP5[5][6] = 53
                            field.Field.MAP5[5][7] = 53
                            field.Field.MAP5[5][8] = 53            
                            Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]
                            Game.field.read_map_info()
                            Game.field.draw()  
                            pygame.display.update()
            if 35 <= Player.end_time - Player.start_time < 36:
                if Player.TSUNAMI_flg == 0 :    
                                for i in range(3,7):
                                    for j in range(14):
                                        for k in range(15):
                                            
                                            if field.Field.MAP_LIST[i][j][k] == 14:
                                                field.Field.MAP_LIST[i][j][k] = 57
                                            if field.Field.MAP_LIST[i][j][k] == 0:
                                                field.Field.MAP_LIST[i][j][k] = 55
                                            if field.Field.MAP_LIST[i][j][k] == 16:
                                                field.Field.MAP_LIST[i][j][k] = 56
                                            if field.Field.MAP_LIST[i][j][k] == 48:
                                                field.Field.MAP_LIST[i][j][k] = 58
                                            if field.Field.MAP_LIST[i][j][k] == 52:
                                                field.Field.MAP_LIST[i][j][k] = 3
                                            if field.Field.MAP_LIST[i][j][k] == 53:
                                                field.Field.MAP_LIST[i][j][k] = 3
                                            if field.Field.MAP_LIST[i][j][k] == 12:
                                                field.Field.MAP_LIST[i][j][k] = 54
                                            if field.Field.MAP_LIST[i][j][k] == 49:
                                                field.Field.MAP_LIST[i][j][k] = 56
                                            if field.Field.MAP_LIST[i][j][k] == 50:
                                                field.Field.MAP_LIST[i][j][k] = 56 
                                            if field.Field.MAP_LIST[i][j][k] == 51:
                                                field.Field.MAP_LIST[i][j][k] = 56   
                                            if field.Field.MAP_LIST[i][j][k] == 47:
                                                field.Field.MAP_LIST[i][j][k] = 54
                                            if field.Field.MAP_LIST[i][j][k] == 17:
                                                field.Field.MAP_LIST[i][j][k] = 55 
                                            if field.Field.MAP_LIST[i][j][k] == 10:
                                                field.Field.MAP_LIST[i][j][k] = 54                                  
                                            if field.Field.MAP_LIST[i][j][k] == 8:
                                                field.Field.MAP_LIST[i][j][k] = 59
                                            if field.Field.MAP_LIST[i][j][k] == 11:
                                                field.Field.MAP_LIST[i][j][k] = 53    
                                            if field.Field.MAP_LIST[i][j][k] in [20,21,22,23,30,31,32,33,40,41,42,43]:
                                                field.Field.MAP_LIST[i][j][k] += 40
                            # if field.Field.MAP5[6][1] == 13:


                                Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]
                                Game.field.read_map_info()
                                Game.field.draw()  
                                pygame.display.update()
                                # Player.TSUNAMI_flg = 1
                                # Player.end_time = 0
                                # Player.start_time = time.time()
            # if Player.TSUNAMI_flg == 0:
            #     # Player.end_time = time.time()
            #     if not self.check_chara_move(posx, posy, dx, dy, Player.HAKUSEN_LIST4) or  30 <= Player.end_time - Player.start_time < 31:

            #         if field.Field.MAP5[0][0] == 57:
            #             return
            #         else:
            #             for i in range(3,7):
            #                 for j in range(14):
            #                     for k in range(15):
                                    
            #                         if field.Field.MAP_LIST[i][j][k] == 14:
            #                             field.Field.MAP_LIST[i][j][k] = 57
            #                         if field.Field.MAP_LIST[i][j][k] == 0:
            #                             field.Field.MAP_LIST[i][j][k] = 55
            #                         if field.Field.MAP_LIST[i][j][k] == 16:
            #                             field.Field.MAP_LIST[i][j][k] = 56
            #                         if field.Field.MAP_LIST[i][j][k] == 48:
            #                             field.Field.MAP_LIST[i][j][k] = 58
            #                         if field.Field.MAP_LIST[i][j][k] == 52:
            #                             field.Field.MAP_LIST[i][j][k] = 3
            #                         if field.Field.MAP_LIST[i][j][k] == 53:
            #                             field.Field.MAP_LIST[i][j][k] = 3
            #                         if field.Field.MAP_LIST[i][j][k] == 12:
            #                             field.Field.MAP_LIST[i][j][k] = 54
            #                         if field.Field.MAP_LIST[i][j][k] == 49:
            #                             field.Field.MAP_LIST[i][j][k] = 56
            #                         if field.Field.MAP_LIST[i][j][k] == 50:
            #                             field.Field.MAP_LIST[i][j][k] = 56 
            #                         if field.Field.MAP_LIST[i][j][k] == 51:
            #                             field.Field.MAP_LIST[i][j][k] = 56   
            #                         if field.Field.MAP_LIST[i][j][k] == 47:
            #                             field.Field.MAP_LIST[i][j][k] = 54
            #                         if field.Field.MAP_LIST[i][j][k] == 17:
            #                             field.Field.MAP_LIST[i][j][k] = 55 
            #                         if field.Field.MAP_LIST[i][j][k] == 10:
            #                             field.Field.MAP_LIST[i][j][k] = 54                                  
            #                         if field.Field.MAP_LIST[i][j][k] == 8:
            #                             field.Field.MAP_LIST[i][j][k] = 59
            #                         if field.Field.MAP_LIST[i][j][k] == 11:
            #                             field.Field.MAP_LIST[i][j][k] = 53    
            #                         if field.Field.MAP_LIST[i][j][k] in [20,21,22,23,30,31,32,33,40,41,42,43]:
            #                             field.Field.MAP_LIST[i][j][k] += 40
            #             Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]               
            #             Game.field.read_map_info
            #             Game.field.draw()  
            #             pygame.display.update()
            
            if not self.check_chara_move(posx, posy, dx, dy, Player.TOUBOKU_LIST_R): 
                if Player.TSUNAMI_flg == 0:        
                    if field.Field.MAP_LIST[Game.field.map_no][posy][posx] == 34:  #左
                        
                        field.Field.MAP_LIST[Game.field.map_no][posy][posx] = 66
                        field.Field.MAP_LIST[Game.field.map_no][posy][posx-1] = 65
                        Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]             
                        Game.field.read_map_info
                        Game.field.draw()  
                        self.hp -= 5
                        Player.TOUBOKU_flg = 1
            if not self.check_chara_move(posx, posy, dx, dy, Player.TOUBOKU_LIST_L): 
                if Player.TSUNAMI_flg == 0:    
                    if field.Field.MAP1[posy][posx] == 35:  #右
                        field.Field.MAP1[posy][posx] = 68
                        field.Field.MAP1[posy][posx+1] = 67
                        Game.field.new_field = field.Field.MAP_LIST[Game.field.map_no]             
                        Game.field.read_map_info
                        Game.field.draw()  
                        self.hp -= 5 
                        Player.TOUBOKU_flg = 1



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

            for cha in Game.charas:
                if cha.coli_flg > 0:
                    if not self.check_chara_move(posx, posy, dx, dy, Player.QUAKE_LIST) and Player.QUAKE_flg == 1:
                            continue
                    else:   
                        Game.surface.fill((0, 0, 0))
                        if Game.field.map_no ==  4:
                            if cha.coli_flg == 1 or cha.coli_flg == 2 or cha.coli_flg == 3 or cha.coli_flg == 4 or cha.coli_flg == 5:
                                continue 
                        if Game.field.map_no ==  5:
                            if cha.coli_flg == 4  or cha.coli_flg == 5 or cha.coli_flg ==6 or cha.coli_flg == 7:
                                continue   

                        if Game.field.map_no ==  6:
                            if cha.coli_flg == 1 or cha.coli_flg == 2 or cha.coli_flg == 3 or cha.coli_flg ==6 or cha.coli_flg == 7:
                                continue   
                        Game.surface.blit(selif_font.render(cha.name,
                                                                True, (255, 255, 255)), (1000, 230))
                        if self.selif_flg >= 1:
                
                                Game.surface.blit(selif_font.render(selif.list[cha.coli_flg][Player.selif_num],
                                                                    True, (255, 255, 255)), (1000, 280))
                                epi_flg_list[cha.coli_flg] = 0
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
