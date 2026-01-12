from PIL import Image
import os

ASCII_CHARS = " ⠂⠆⠖⠶⡶⣶⣷⣿"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def resize_image(img, width):
    w, h = img.size
    ratio = h / w
    new_height = int(width * ratio * 0.5)
    return img.resize((width, new_height))

def pixel_to_ascii(img):
    pixels = img.getdata()
    scale = len(ASCII_CHARS)
    return "".join(ASCII_CHARS[p * scale // 256] for p in pixels)

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

def image_to_banner(path, fixed_size, boxed):
    img = Image.open(path).convert("L")

    if fixed_size:
        img = resize_image(img, 115)
    else:
        img = resize_image(img, 75)

    ascii_str = pixel_to_ascii(img)
    width = img.width

    banner = "\n".join(
        ascii_str[i:i + width]
        for i in range(0, len(ascii_str), width)
    )

    if boxed:
        banner = put_in_box(banner)

    return banner

def main():
    clear()
    print("=== TOOL TẠO BANNER ASCII ===\n")
    print("tool by anhnguyencoder\n")

    img_path = input("NHẬP TÊN FILE ẢNH: ").strip()
    if not os.path.exists(img_path):
        print("❌ Không tìm thấy file ảnh!")
        return

    fixed = input("DÙNG KÍCH THƯỚC CỐ ĐỊNH (y/n): ").lower() == "y"
    boxed = input("ART CÓ ĐỂ TRONG KHÔNG (dùng nếu muốn trưng bày art) (y/n): ").lower() == "y"

    print("\n⏳ Đang tạo banner...\n")

    banner = image_to_banner(img_path, fixed, boxed)

    print(banner)

    with open("banner.txt", "w", encoding="utf-8") as f:
        f.write(banner)

    print("\n✅ Đã lưu banner vào banner.txt")

if __name__ == "__main__":
    main()
