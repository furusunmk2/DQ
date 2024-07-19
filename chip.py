from game import Game
from square import Square

# フィールドチップクラス（画面１マスのクラス）
class Chip(Square):
    # チップ（フィールドの１マス）画像のリスト
    images = None
    
    # コンストラクタ
    def __init__(self):
        # Ａ－１３Squareから）親クラスのコンストラクタを呼び出す
        super().__init__()
        # Ａ－１４）チップ番号に初期値を設定
        self.chip_no = 0
        # Ａ－１５）画像リストが空の場合（初回のみ）
        if Chip.images == None:
            # Ａ－１６）チップ（フィールドの部品）画像を読み込み
            Chip.images = (
                Game.read_image_for_square('image/chip0.png'),
                Game.read_image_for_square('image/chip1.png'),
                Game.read_image_for_square('image/chip2.png'),
                Game.read_image_for_square('image/chip3.png'),
                Game.read_image_for_square('image/chip4.png'),
                Game.read_image_for_square('image/chip5.png'),
                Game.read_image_for_square('image/chip6.png'),
                Game.read_image_for_square('image/chip7.png'),
                Game.read_image_for_square('image/chip8.png'),
                Game.read_image_for_square('image/chip9.png'),
                Game.read_image_for_square('image/chip10.png'),
                Game.read_image_for_square('image/chip11.png'),
                Game.read_image_for_square('image/chip12.png'),
                Game.read_image_for_square('image/chip13.png'),
                Game.read_image_for_square('image/chip14.png'),
                Game.read_image_for_square('image/chip15.png'),
                Game.read_image_for_square('image/chip16.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip18.png'),
                Game.read_image_for_square('image/chip19.png'),
                Game.read_image_for_square('image/chip20.png'),
                Game.read_image_for_square('image/chip21.png'),
                Game.read_image_for_square('image/chip22.png'),
                Game.read_image_for_square('image/chip23.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip25.png'),
                Game.read_image_for_square('image/chip26.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip30.png'),
                Game.read_image_for_square('image/chip31.png'),
                Game.read_image_for_square('image/chip32.png'),
                Game.read_image_for_square('image/chip33.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip15.png'),
                Game.read_image_for_square('image/chip16.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip17.png'),
                Game.read_image_for_square('image/chip40.png'),
                Game.read_image_for_square('image/chip41.png'),
                Game.read_image_for_square('image/chip42.png'),
                Game.read_image_for_square('image/chip43.png'),
            )
    
    # チップ番号設定
    def set_chip_no(self, no):
        # Ａ－１７）引数の番号を設定
        self.chip_no = no
        # Ａ－１８Fieldへ）番号に対応する画像を設定
        self.set_image(self.images[no])
