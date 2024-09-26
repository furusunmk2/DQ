#-*- coding: utf-8 -*-
from dataclasses import field
import pygame
from game import Game, Phase
from field import Field
from player import Player
from chara import Chara
from charalist import CharaList
import random


# pythonの基本処理
pygame.init()
Game.surface = pygame.display.set_mode([1360, 960])
clock = pygame.time.Clock()
pygame.display.set_caption('*** Sample RPG ***')

    
# windows ver
# 描画用フォント（等幅フォントを使用しているので、使えなかったら変えてください）
smallfont = pygame.font.SysFont('Courier', 36)   # 小さい文字用のフォント
largefont = pygame.font.SysFont(None, 120)   # 大きい文字用のフォント
item_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 24)
# mac ver
# smallfont = pygame.font.Font('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 24)
# largefont = pygame.font.Font('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 24)
# item_font = pygame.font.Font('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 24)
# ゲーム情報初期化処理
def init_game_info():
    # フィールド表示をスタート状態とする
    Game.phase = Phase.IN_FIELD
    # Ａ－２６Fieldから）フィールド・インスタンスを作成して、ゲームクラスの変数に設定
    Game.field = Field()
    # Ｃ－４４Playerから）プレイヤー・インスタンスを作成して、ゲームクラスの変数に設定
    Game.player = Player()
    # Ｈ－１０３Charaから)モンスター・インスタンスのリストを作成して、ゲームクラスの変数に設定
    Game.charas = []
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_FATHER))
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_MOTHER))
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_DAUGHTER))
    Game.charas.append(Chara((8, 5), CharaList.CHA_NO_BOY))
    Game.charas.append(Chara((8, 4), CharaList.CHA_NO_GIRL))
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_MAN))
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_WOMAN))
    Game.charas.append(Chara((0, 0), CharaList.CHA_NO_CAR))

    
    for m_no,chara in enumerate(Game.charas):                  
            # Ｊ－１２７）マスのピッタリの位置に配置する
            
            if Game.field.map_no ==  4:
                if m_no == 0 or m_no == 1 or m_no == 2 or m_no == 3 or m_no == 4:
                    continue
                if Player.QUAKE_flg == 1:
                    continue
            if Game.field.map_no ==  5 and Player.QUAKE_flg == 0:
                if m_no == 3  or m_no == 4 or m_no ==5 or m_no == 6:
                    continue
                
            if not Game.field.map_no ==  2:
                if m_no == 8 or m_no == 9 or m_no == 10 or m_no ==11 or m_no == 12 or m_no == 13 or m_no == 14 or m_no == 15 or m_no ==16 or m_no == 17:
                    continue
               
            if Game.field.map_no ==  6:
                if m_no == 0 or m_no == 1 or m_no == 2 or m_no ==5 or m_no == 6:
                    continue
                if Player.QUAKE_flg == 1:
                    continue
            if not Game.field.map_no == 5:
                if Game.field.QUAKE == 2:
                    continue
            dx, dy = 0, 0
            # Ｊ－１２８）配置できるまでループする
            # （※無限ループしてしまわないように、100回で諦める）
            for _ in range(200):
                # Ｊ－１２９）プレイヤーが端からくるので、外側の２マスには配置しない
                posx = random.randint(2, Game.FIELD_WIDTH - 3)
                posy = random.randint(2, Game.FIELD_HEIGHT - 3)
                # Ｊ－１３０）モンスターが移動できない位置に配置されてしまった場合はやり直し
                if not chara.check_chara_move(posx, posy, dx, dy,
                                                chara.unmovable_chips):
                    continue
                # Ｊ－１３１Charaへ）移動できる位置ならそこに配置
                chara.set_pos(posx, posy)
                chara.set_dpos(dx, dy)
            
    # # Ｋ－１４６Battleから）戦闘画面
    # Game.battle = Battle()

# 基本描画処理
def basic_draw():
    # Ａ－２７最後）フィールドの描画
    Game.field.draw()
    # 出現キャラ操作（fieldも同様に）
    
    if Game.field.QUAKE == 1:
        if Game.field.map_no ==5:
                    for i in CharaList.CHARA_LIST:
                        Game.charas = []
                        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4: 
                            i[2] = 1
                            i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78,  80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                
                    Game.charas.append(Chara((4, 1), CharaList.CHA_NO_FATHER))
                    Game.charas.append(Chara((5, 1), CharaList.CHA_NO_MOTHER))
                    Game.charas.append(Chara((6, 1), CharaList.CHA_NO_DAUGHTER))
                    Game.charas.append(Chara((4, 1), CharaList.CHA_NO_BOY))
                    Game.charas.append(Chara((5, 1), CharaList.CHA_NO_GIRL))
                    Game.charas.append(Chara((7, 7), CharaList.CHA_NO_MAN))
                    Game.charas.append(Chara((7, 7), CharaList.CHA_NO_WOMAN))        
                    Game.field.QUAKE = 2
                    print(Game.field.QUAKE)
    if Game.field.QUAKE == 2:
        
            if  Game.field.map_no ==1:
                    for i in CharaList.CHARA_LIST:
                        Game.charas = []
                        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4: 
                            i[2] = 1
                            i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78,  80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                
                    Game.charas.append(Chara((8, 5), CharaList.CHA_NO_FATHER))
                    Game.charas.append(Chara((10, 5), CharaList.CHA_NO_MOTHER))
                    Game.charas.append(Chara((10, 5), CharaList.CHA_NO_DAUGHTER))
                    Game.charas.append(Chara((13, 5), CharaList.CHA_NO_BOY))
                    Game.charas.append(Chara((13, 4), CharaList.CHA_NO_GIRL))
                    Game.charas.append(Chara((7, 5), CharaList.CHA_NO_MAN))
                    Game.charas.append(Chara((7, 5), CharaList.CHA_NO_WOMAN))
                    Game.field.QUAKE = 3
                    print(Game.field.QUAKE)

    if Game.field.QUAKE == 3:  
        if Game.field.map_no ==2:
                for i in CharaList.CHARA_LIST:
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i== 5 or i== 6: 
                        i[2] = 1
                        i[5] = []
                        i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,34,35,36,37,38,39,40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                Game.charas = []
                Game.charas.append(Chara((8, 5), CharaList.CHA_NO_FATHER))
                Game.charas.append(Chara((10, 6), CharaList.CHA_NO_MOTHER))
                Game.charas.append(Chara((10, 4), CharaList.CHA_NO_DAUGHTER))
                Game.charas.append(Chara((12, 5), CharaList.CHA_NO_BOY))
                Game.charas.append(Chara((12, 6), CharaList.CHA_NO_GIRL))
                Game.charas.append(Chara((7, 5), CharaList.CHA_NO_MAN))
                Game.charas.append(Chara((7, 6), CharaList.CHA_NO_WOMAN))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 13), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 12), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((11, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Game.charas.append(Chara((12, 11), CharaList.CHA_NO_FIRE))
                Player.MAP2_flg =1
                Game.field.QUAKE = 4
                Field.MAP1[4][5] = 99
                Field.MAP1[4][4] = 99
                for i in range (14):
                    for j in range(15):
                        if Field.MAP1[i][j]== 76:
                            Field.MAP1[i][j]= 79
                print(Game.field.QUAKE)
                
    if Game.field.QUAKE == 4:  
        if Game.field.map_no ==1:
                Player.selif_flg =2
                for i in CharaList.CHARA_LIST:
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i== 5 or i== 6: 
                        i[2] = 1
                        i[5] = []
                        i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,34,35,36,37,38,39,40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                Game.charas = []
                Game.charas.append(Chara((6, 6), CharaList.CHA_NO_FATHER))
                Game.charas.append(Chara((6, 5), CharaList.CHA_NO_MOTHER))
                Game.charas.append(Chara((10, 5), CharaList.CHA_NO_DAUGHTER))
                Game.charas.append(Chara((10, 5), CharaList.CHA_NO_BOY))
                Game.charas.append(Chara((10, 5), CharaList.CHA_NO_GIRL))
                Game.charas.append(Chara((5, 5), CharaList.CHA_NO_MAN))
                Game.charas.append(Chara((5, 6), CharaList.CHA_NO_WOMAN))
                for i in range (14):
                    for j in range(15):
                        if Field.MAP2[i][j]== 74:
                            Field.MAP2[i][j]= 79
                        if Field.MAP2[i][j]== 105:
                            Field.MAP2[i][j]= 94   
                        if Field.MAP2[i][j]== 106:
                            Field.MAP2[i][j]= 33 
                        if Field.MAP2[i][j]== 107:
                            Field.MAP2[i][j]= 73 
                Game.field.QUAKE = 5
                
                print(Game.field.QUAKE)
    if Game.field.QUAKE == 5: 
        if Game.field.map_no ==2:
            Game.charas = []
            Game.field.QUAKE = 4
        if Game.field.map_no ==10:
                Player.selif_flg =2
                for i in CharaList.CHARA_LIST:
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i== 5 or i== 6: 
                        i[2] = 1
                        i[5] = []
                        i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,34,35,36,37,38,39,40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                Game.charas = []
                Game.charas.append(Chara((6, 6), CharaList.CHA_NO_FATHER))
                Game.charas.append(Chara((6, 5), CharaList.CHA_NO_MOTHER))
                Game.charas.append(Chara((5, 6), CharaList.CHA_NO_DAUGHTER))
                Game.charas.append(Chara((12, 7), CharaList.CHA_NO_BOY))
                Game.charas.append(Chara((12, 6), CharaList.CHA_NO_GIRL))
                Game.charas.append(Chara((5, 5), CharaList.CHA_NO_MAN))
                Game.charas.append(Chara((5, 6), CharaList.CHA_NO_WOMAN))
                Game.field.QUAKE = 6

    if Game.field.QUAKE == 6: 
        if Game.field.map_no ==1:
            Game.charas = []
        if Game.field.map_no ==11:
                Player.selif_flg =2
                for i in CharaList.CHARA_LIST:
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i== 5 or i== 6: 
                        i[2] = 1
                        i[5] = []
                        i[5] = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,34,35,36,37,38,39,40, 41, 42, 43, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                Game.charas = []
                Game.charas.append(Chara((6, 6), CharaList.CHA_NO_FATHER))
                Game.charas.append(Chara((6, 5), CharaList.CHA_NO_MOTHER))
                Game.charas.append(Chara((5, 6), CharaList.CHA_NO_DAUGHTER))
                Game.charas.append(Chara((12, 7), CharaList.CHA_NO_BOY))
                Game.charas.append(Chara((12, 6), CharaList.CHA_NO_GIRL))
                Game.charas.append(Chara((5, 5), CharaList.CHA_NO_MAN))
                Game.charas.append(Chara((5, 6), CharaList.CHA_NO_WOMAN))
                Game.field.QUAKE = 7
                
                print(Game.field.QUAKE)            
                
    for m_no,chara in enumerate(Game.charas):
       
        if Game.field.map_no ==  4:
            if m_no == 0 or m_no == 1 or m_no == 2 or m_no == 3 or m_no == 4:
                continue
            if Player.clear_flg == 1:
                continue
        if Game.field.map_no ==  5:
                if Player.QUAKE_flg == 1:
                    Player.clear_flg = 1
                elif m_no == 3  or m_no == 4 or m_no ==5 or m_no == 6:
                    continue    
        if Game.field.map_no ==  6:
            if m_no == 0 or m_no == 1 or m_no == 2 or m_no ==5 or m_no == 6:
                 continue
            if Player.QUAKE_flg == 1:
                continue
        if not Game.field.map_no ==  2:
            if m_no == 8 or m_no == 9  or m_no == 10 or m_no ==11 or m_no == 12 or m_no == 13 or m_no == 14  or m_no == 15 or m_no ==16 or m_no == 17:
                continue
        if not Game.field.map_no == 5:
            if Game.field.QUAKE == 2:
                continue      
        chara.draw()
    # Ｃ－４５最後）プレイヤーの描画
    Game.player.draw()
    # Ｄ－５１Playerから）レベルの描画（左空白埋めで５桁）
    level_str = str(Game.player.level).rjust(5)
    level_render = smallfont.render(f'Level:{level_str}',
                                    True, (255, 255, 255))
    Game.surface.blit(level_render, (1000, 30))
    # Ｄ－５２）HPの描画（左空白埋めで５桁）
    hp_str = str(Game.player.hp).rjust(5)
    hp_render = smallfont.render(f'   HP:{hp_str}',
                                    True, (255, 255, 255))
    Game.surface.blit(hp_render, (1000, 80))
    #アイテム表示
    if Player.item_flg3 == 1:
        item1 = item_font.render(f'☆にじいろの粉',
                                        True, (255, 255, 255))
        Game.surface.blit(item1, (1000, 130))
        Player.end_flg = 1
    if Player.item_flg2 == 1:
        item1 = item_font.render(f'☆ひみつの鍵',
                                        True, (255, 255, 255))
        Game.surface.blit(item1, (1000, 180))
        Player.kagi_flg = 1
    
    if Player.item_flg1 == 1:
        item1 = item_font.render(f'☆まほうの靴',
                                        True, (255, 255, 255))
        Game.surface.blit(item1, (1000, 230))
        Player.UNMOVABLE_CHIP_LIST = [2,7]

# メイン処理
def main():
    # ゲーム情報の初期化処理を実行
    init_game_info()
    # ゲームのメインループ
    while True:
        # ゲームのカウンタを１加算
        Game.count += 1
        # イベントチェック処理（終了、キー入力）を実行
        Game.check_event()
        # 画面を黒で塗りつぶす
        Game.surface.fill((0, 0, 0))
        # ===== ゲームフェーズによる処理段階分け =====
        # フィールド上の場合
        if Game.phase == Phase.IN_FIELD:
            # Ｄ－５３最後）プレイヤーの毎回処理
            Game.player.frame_process_img()
            
            
            # if  Player.MAP2_flg == 1:
            #     Game.field.map_no = 2
            #     Game.field.new_field = Field.MAP_LIST[2]
            #     Game.field.read_map_info()
            #     Game.field.draw()
            #     Player.MAP2_flg = 0
            #     pygame.display.update()
            #     Player.epi_flg += 1
                
            if  Player.MAP4_flg == 1:
                if Game.field.map_no == 4:
                    Game.field.map_no = 4
                    Game.field.new_field = Field.MAP_LIST[4]
                    Game.field.read_map_info()
                    Game.field.draw()

            # if Player.TOUBOKU_flg == 1:
            #     pygame.display.update()
            #     Player.TOUBOKU_flg = 0

            if  Player.MAP8_flg == 1:
                Game.field.map_no = 8
                Game.field.new_field = Field.MAP_LIST[8]
                Game.field.read_map_info()
                Game.field.draw()
                Player.MAP8_flg = 0
                pygame.display.update()
                Player.door_flg += 1  
                
            if  Player.MAP8_flg2 == 1:
                Game.field.map_no = 8
                Game.field.new_field = Field.MAP_LIST[8]
                Game.field.read_map_info()
                Game.field.draw()
                Player.MAP8_flg2 = 0
                pygame.display.update()     
                
            # Ｈ－１０５最後)モンスターの毎回処理
            for chara in Game.charas:
                chara.frame_process_img()
            
            # 基本描画処理
            basic_draw()

        # 戦闘中の場合
        elif Game.phase == Phase.IN_BATTLE:
            # Ｎ－１７７Battleから、最後）戦闘中の毎回処理
            Game.battle.frame_process_btl()
            # 基本描画処理
            basic_draw()
            # Ｋ－１４７最後）戦闘画面描画処理
            Game.battle.draw()
            
        # ゲームオーバーの場合
        elif Game.phase == Phase.GAME_OVER:
            # 基本描画処理
            basic_draw()
            # ゲームオーバーメッセージの描画
            go_str = largefont.render('GAME OVER...',
                                        True, (255, 0, 0))
            Game.surface.blit(go_str, (40, 300))
            
        elif Game.phase == Phase.GAME_CLEAR:
            # 基本描画処理
            basic_draw()
            # ゲームオーバーメッセージの描画
            go_str = largefont.render('GAME CLEAR',
                                        True, (0, 0, 0))
            Game.surface.blit(go_str, (40, 300))

        pygame.display.update()     # 描画更新処理
        clock.tick(25)              # 一定時間処理

try:
    pygame.mixer.init()
    pygame.mixer.music.load('BGM.mp3')   #BGMをロード
    pygame.mixer.music.play(-1)

except:
    print("ファイルが見当たらないか、オーディオ機器が接続されていません")
# メイン処理の呼び出し
if __name__ == '__main__':
    main()
