from PIL import Image
import numpy as np

# 画像のパス
image_path = "./yaju.jpg"

# 画像を開く
img = Image.open(image_path)

# 画像をグレースケールに変換
img = img.convert("L")

# 画像のサイズを縮小（ASCIIアートに適したサイズにする）
width, height = img.size
aspect_ratio = height / width
new_width = 100  # 出力サイズの調整
new_height = int(aspect_ratio * new_width * 0.55)  # ASCIIの縦横比を調整
img = img.resize((new_width, new_height))

# ASCIIアート用の文字セット（濃淡に応じて）
ascii_chars = "@%#*+=-:. "

# ピクセル値をASCII文字に変換
pixels = np.array(img)
ascii_image = "\n".join(
    "".join(ascii_chars[pixel // 32] for pixel in row) for row in pixels
)

# 結果を出力
ascii_image
