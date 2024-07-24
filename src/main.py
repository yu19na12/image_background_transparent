from rembg import remove
from PIL import Image
import os

# プロジェクトのルートディレクトリへの相対パスを取得
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 入力画像と出力画像のパスを設定
input_path = os.path.join(project_root, "image", "input.JPG")
output_path = os.path.join(project_root, "image", "output.png")

input_image = Image.open(input_path)
output = remove(input_image)
output.save(output_path)

print(f"背景が削除された画像が {output_path} に保存されました。")