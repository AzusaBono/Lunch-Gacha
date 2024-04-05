import random
import tkinter as tk
from PIL import Image, ImageTk

class Lunch_Gacha:
    def __init__(self, window):
        self.window = window
        window.title("今日のランチは")
        #ウィンドウのサイズを設定
        window.geometry("350x350")
        # 背景色が黄色のフレームを作成して配置
        self.bg_frame = tk.Frame(window, bg="yellow")
        self.bg_frame.pack(fill=tk.BOTH, expand=True) #（フレームが水平方向と垂直方向の両方に親ウィンドウに合わせて拡張される）
        # ボタンを作成し、下部に配置
        self.gacha_button = tk.Button(self.bg_frame, text="Let's choice!", command=self.pull_gacha,
                                      bg="gray", fg="yellow", font=("Courier New", 14, "bold"), relief=tk.RAISED, bd=3)
        self.gacha_button.pack(side=tk.BOTTOM, pady=25)
        # 結果（画像）ラベルを作成し、中央に配置
        self.result_label = tk.Label(self.bg_frame, bg="yellow") 
        self.result_label.pack(pady=30)
        
        self.lunch_images = {
            "カレー": {"image": "curry.png", "probability": 4},
            "餃子": {"image": "gyoza.png", "probability": 4},
            "ハンバーグ": {"image": "hamberg.png", "probability": 4},
            "ナポリタン": {"image": "napolitan.png", "probability": 80},
            "お寿司": {"image": "sushi.png", "probability": 4},
            "タコ焼き": {"image": "takoyaki.png", "probability": 4},
            }

    def pull_gacha(self):
        # ランチリストからランダムに1つ選択
        result = random.choices(list(self.lunch_images.keys()),  # ガチャのアイテムリスト
                                weights=[lunch["probability"] for lunch in self.lunch_images.values()])[0]  # 各アイテムの選択確率
        # 画像位置パス = 辞書からランダムに出力された結果
        image_path = self.lunch_images[result]["image"]
        # 画像を開く
        image = Image.open(image_path)
        # 画像をリサイズ
        image = image.resize((300, 200), Image.BICUBIC)
        # 画像をTkinterで表示可能な形式に変換
        photo = ImageTk.PhotoImage(image)

        # ラベルに画像を設定して表示
        self.result_label.image_ref = photo
        self.result_label.config(image=photo)
        
                
def main():
    root = tk.Tk()
    app = Lunch_Gacha(root)
    root.mainloop()

if __name__ == "__main__":
    main()
