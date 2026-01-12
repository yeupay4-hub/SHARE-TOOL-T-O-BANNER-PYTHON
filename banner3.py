from PIL import Image
import os
from pystyle import Colors, Colorate, Center, Write, Anime
from pystyle import Col

banners = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣾⣿⣿⣿⣿⣿⣤⣿⣿⣿⣤⣾⣿⣿⣤⣾⣿⣤⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣤⣾⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣤⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣿⣿⣿⣤⣿⣾⣿⣤⣿⣿⣿⣿⣿⣿⣤⣿⠖⣾⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⠖⣤⣤⣤⣿⣿⣿⣿⣾⠖⣿⣾⣿⣿⣿⣿⣿⣿⣿⣤⣿⣾⣿⣿⣿⣿⣤⠆⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣤⣤⣤⣿⣿⣿⣤⣤⣤⣿⣤⣿⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣤⣿⣿⣤⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣤⠆⣿⣿⣿⣿⣤⠖⣤⣤⣿⣤⣿⣿⣾⣤⣤⣿⣿⣿⣾⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣾⣤⣾⣿⣤⣤⣿⣿⣿⣤⣿⣤⣿⣿⣿⣾⣤⣤⣿⣤⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣤⣿⣿⣤⣾⣤⣤⣿⣤⣿⣤⣤⣤⣾⣿⣤⣿⣿⣤⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⠖⣿⣿⣿⣾⠖⣤⣿⣾⣿⣤⣿⣿⣿⣤⣾⣾⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣤⣿⣤⣤⣿⣿⣤⣤⣤⠆⣿⣿⣿⣤⣿⣿⣿⣿⣿⠖⣿⣿⣤⠆⣤⣤⠖⣤⠆⣿⣾⠖⣾⠖⣤⣿⣿⣿⣿⠖⣾⣾⣾⣿⣾⣤⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣾⣿⣿⣿⣤⣿⣿⣤⣾⣤⣿⣿⣤⣿⣿⣿⣾⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣾⣿⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣤⣿⣿⣿⣿⣿⣤⣿⣿⣾⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠖⣤⠆⣿⠆⣿⣤⣿⣤⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣤⣤⣿⣾⣿⣤⣿⣿⣿⣿⣿⣾⣤⣿⣿⣿⣤⣤⣿⣿⣿⠖⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣤⣿⣿⣿⣤⣿⣿⣿⠖⣾⣤⣿⣿⣾⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣾⣾⣾⣾⣾⣾⣾⣤⣾⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣿⣤⣿⣿⣿⣾⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣾⣤⣤⣿⣤⣿⣿⣿⣿⣾⣿⣾⣾⣾⣾⣾⣾⣾⣾⣾
⣤⣤⣤⣤⣤⣤⣤⠖⣤⣤⣿⣤⣤⣿⣿⣿⠖⣿⣿⣿⣿⠖⠆⣿⣤⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣤⣿⣤⣿⣿⣿⣾⣾⣿⣤⣾⣾⣾⣾⣾⣾⣾⣾⣾
⣤⣤⣤⣤⣤⣤⣤⣤⣿⠖⣿⠖⣤⣿⣤⣿⣤⣿⣿⣤⣿⣤⣤⣿⣤⣤⣿⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣾⣿⠖⣿⣿⣤⣿⣾⣿⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾
⣤⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿⣤⣤⣿⠖⣤⠆⣿⣿⣿⣿⣿⠆⣾⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣤⣾⣿⣿⣿⣿⣿⣿⣾⣾⣤⣾⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣤⠖⣤⣤⣤⣿⣿⣿⣤⣿⣤⣾⣾⣾⣤⣿⣿⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣾⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣤⣾⣿⣤⣿⣿⠆⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣾⣾⣾⣿⣿⣿⣤⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⠖⣿⣤⣿⣿⣤⣿⣤⣾⣿⣤⣿⣿⣤⣿⣿⣾⣾⣾⣿⣿⣾⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣤⣤⠖⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣤⣿⣤⣿⣤⣤⣿⣤⣾⣿⣿⣤⠖⣿⣿⣤⣿⣾⣾⣿⣿⣤⣾⣾⣤⣿⣾⣾⣾⣾⠆⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣤⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣾⣿⣿⣤⣤⣾⣿⣿⣿⣤⣾⣿⣿⣿⣾⣾⣾⣾⣤⣤⣾⣤⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠆⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣾⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠖⣤⣿⣿⣤⣿⣾⣿⣿⣿⣿⣾⣾⣾⣾⣾⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣤⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣤⣤⣤⣿⣤⣾⣿⣿⣿⣿⣿⣤⣾⣾⣾⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣾⣤⣾⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿
                SOURCE CODE TOOL BY ANHNGUYENCODER
"""
DOT_ASCII = " .:·•oO"
DOT_BLOCK = " ⣀⣄⣆⣇⣧⣷⣿"

DEFAULT_WIDTH = 85

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def resize_image(img, width):
    w, h = img.size
    ratio = h / w
    new_height = int(width * ratio * 0.5)
    return img.resize((width, new_height))


def pixel_to_dot(img, charset):
    pixels = img.getdata()
    scale = len(charset)
    return "".join(charset[p * scale // 256] for p in pixels)

def put_in_box(text):
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)

    top = "┌" + "─" * (max_len + 2) + "┐"
    bottom = "└" + "─" * (max_len + 2) + "┘"

    box = [top]
    for line in lines:
        box.append("│ " + line.ljust(max_len) + " │")
    box.append(bottom)

    return "\n".join(box)


def image_to_banner(path, charset, boxed, fixed_size):
    img = Image.open(path).convert("L")

    if not fixed_size:
        img = resize_image(img, DEFAULT_WIDTH)

    dot_str = pixel_to_dot(img, charset)
    w = img.width

    banner = "\n".join(
        dot_str[i:i + w]
        for i in range(0, len(dot_str), w)
    )

    if boxed:
        banner = put_in_box(banner)

    return banner

def main():
    clear()
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.purple)), banners))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "===== TOOL TẠO BANNER =====\n"))

    img_path = input(Colorate.Horizontal(Colors.green_to_blue, "NHẬP TÊN FILE ẢNH: ")).strip()
    if not os.path.exists(img_path):
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.orange)), "❌ Không tìm thấy file ảnh!"))
        return

    print(Colorate.Horizontal(Colors.green_to_blue, "\nCHỌN KIỂU DOT:"))
    print(Colorate.Horizontal(Colors.red_to_blue, "1. DOT ASCII (nhẹ)"))
    print(Colorate.Horizontal(Colors.green_to_cyan, "2. DOT BLOCK (đậm)"))
    choice = input(Colorate.Horizontal(Colors.green_to_blue, "NHẬP LỰA CHỌN (1/2): ")).strip()

    if choice == "1":
        charset = DOT_ASCII
    elif choice == "2":
        charset = DOT_BLOCK
    else:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.orange)), "❌ Lựa chọn không hợp lệ!"))
        return

    fixed_size = input(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.cyan)), "DÙNG KÍCH THƯỚC Cố ĐỊNH (y/n): ")).lower() == "y"

    boxed = input(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.cyan)), "ART CÓ ĐỂ TRONG  KHÔNG (dùng nếu muốn trưng bày art) (y/n): ")).lower() == "y"

    print(Colorate.Horizontal(Colors.green_to_blue, "\nĐang Xử Lý...\n"))
    banner = image_to_banner(img_path, charset, boxed, fixed_size)

    print(banner)

    save = input(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.cyan)), "LƯU FILE BANNER (y/n): ")).lower() == "y"
    if save:
        with open("banner.txt", "w", encoding="utf-8") as f:
            f.write(banner)
        print(Colorate.Horizontal(Colors.green_to_blue, "✅ Đã lưu banner.txt"))

if __name__ == "__main__":
    main()
