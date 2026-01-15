from PIL import Image
import os

ASCII_CHARS = "⣿⣾⣤⣶⣦⣀⡀ "

def resize_image(img, fixed_size):
    if fixed_size:
        return img

    TARGET_WIDTH = 75

    w, h = img.size
    ratio = h / w

    new_height = int(TARGET_WIDTH * ratio * 0.55)

    return img.resize((TARGET_WIDTH, new_height))

def image_to_ascii(img):
    img = img.convert("L")
    pixels = img.getdata()
    ascii_str = ""

    for pixel in pixels:
        index = pixel * (len(ASCII_CHARS) - 1) // 255
        ascii_str += ASCII_CHARS[index]

    width = img.width
    return [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]

def add_frame(ascii_lines):
    w = len(ascii_lines[0])
    top = "┌" + "─" * w + "┐"
    bottom = "└" + "─" * w + "┘"
    framed = [top]
    for line in ascii_lines:
        framed.append("│" + line + "│")
    framed.append(bottom)
    return framed

def main():
    img_path = input("NHẬP TÊN FILE ẢNH: ").strip()

    if not os.path.exists(img_path):
        print("❌ Không tìm thấy file ảnh")
        return

    fixed = input("DÙNG KÍCH THƯỚC CỐ ĐỊNH (y/n): ").lower() == "y"
    frame = input("ART CÓ ĐỂ TRONG KHUNG KHÔNG (y/n): ").lower() == "y"

    img = Image.open(img_path)
    img = resize_image(img, fixed)

    ascii_art = image_to_ascii(img)

    if frame:
        ascii_art = add_frame(ascii_art)

    banner = "\n".join(ascii_art)

    print("\n===== BANNER =====\n")
    print(banner)

    with open("banner.txt", "w", encoding="utf-8") as f:
        f.write(banner)

    print("\n✅ Đã lưu banner vào banner.txt")

if __name__ == "__main__":
    main()
