from dataclasses import field
import pygame
from game import Game, Phase
from field import Field
from player import Player
from monster import Monster
from monsterlist import MonsterList
# from battle import Battle

# Pythonの基本処理
pygame.init()
Game.surface = pygame.display.set_mode([1280, 960])
clock = pygame.time.Clock()
pygame.display.set_caption('*** Sample RPG ***')

    

# 描画用フォント（等幅フォントを使用しているので、使えなかったら変えてください）
smallfont = pygame.font.SysFont('Courier', 36)   # 小さい文字用のフォント
largefont = pygame.font.SysFont(None, 120)   # 大きい文字用のフォント
item_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 24)

# ゲーム情報初期化処理
def init_game_info():
    # フィールド表示をスタート状態とする
    Game.phase = Phase.IN_FIELD
    # Ａ－２６Fieldから）フィールド・インスタンスを作成して、ゲームクラスの変数に設定
    Game.field = Field()
    # Ｃ－４４Playerから）プレイヤー・インスタンスを作成して、ゲームクラスの変数に設定
    Game.player = Player()
    # Ｈ－１０３Monsterから)モンスター・インスタンスのリストを作成して、ゲームクラスの変数に設定
    Game.monsters = []
    Game.monsters.append(Monster((8, 1), MonsterList.MON_NO_LADYBUG))
    Game.monsters.append(Monster((2, 8), MonsterList.MON_NO_BIRD))
    Game.monsters.append(Monster((1, 1), MonsterList.MON_NO_DOKINCHAN))
    Game.monsters.append(Monster((1, 8), MonsterList.MON_NO_NIZI_NEZUMI))
    
    
    # # Ｋ－１４６Battleから）戦闘画面
    # Game.battle = Battle()

# 基本描画処理
def basic_draw():
    # Ａ－２７最後）フィールドの描画
    Game.field.draw()
    # Ｈ－１０４)モンスター達の描画
    for i,monster in enumerate(Game.monsters):
        if i == 3:
                continue 
  
        monster.draw()
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
            
            
            if  Player.MAP2_flg == 1:
                Game.field.map_no = 2
                Game.field.new_field = Field.MAP_LIST[2]
                Game.field.read_map_info()
                Game.field.draw()
                Player.MAP2_flg = 0
                pygame.display.update()
                Player.takarabako_flg += 1
                
            if  Player.MAP5_flg == 1:
                Game.field.map_no = 5
                Game.field.new_field = Field.MAP_LIST[5]
                Game.field.read_map_info()
                Game.field.draw()
                Player.MAP5_flg = 0
                pygame.display.update()
                Player.otoshimono_flg += 1   
                 
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
            for monster in Game.monsters:
                monster.frame_process_img()
            
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
    pygame.mixer.music.load('bgm.mp3')   #BGMをロード

    pygame.mixer.music.play(-1)
except:
    print("ファイルが見当たらないか、オーディオ機器が接続されていません")
# メイン処理の呼び出し
if __name__ == '__main__':
    main()
