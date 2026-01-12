from PIL import Image
import os

DOT_CHARS = "⣿⣾⣶⣤⣀⠂ "

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def resize_image(img, width):
    w, h = img.size
    ratio = h / w
    height = int(width * ratio * 0.55)
    return img.resize((width, height))

def pixel_to_dot(pixel):
    return DOT_CHARS[pixel * len(DOT_CHARS) // 256]

def image_to_dots(path, fixed_size=True):
    img = Image.open(path).convert("L")

    width = 120 if fixed_size else 80
    img = resize_image(img, width)

    pixels = img.getdata()
    dots = "".join(pixel_to_dot(p) for p in pixels)

    result = []
    for i in range(0, len(dots), img.width):
        result.append(dots[i:i + img.width])

    return "\n".join(result)

def make_box(text):
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)

    top = "┌" + "─" * (max_len + 2) + "┐"
    bottom = "└" + "─" * (max_len + 2) + "┘"

    box = [top]
    for line in lines:
        box.append("│ " + line.ljust(max_len) + " │")
    box.append(bottom)

    return "\n".join(box)

def main():
    clear()
    print("=== TOOL TẠO BANNER BLOCK ASCII ===\n")
    print("tool by anhnguyencoder\n")

    img_path = input("NHẬP TÊN FILE ẢNH: ").strip()
    if not os.path.isfile(img_path):
        print("❌ Không tìm thấy file ảnh!")
        return

    fixed = input("DÙNG KÍCH THƯỚC CỐ ĐỊNH (y/n): ").lower() == "y"
    boxed = input("ART CÓ ĐỂ TRONG  KHÔNG (dùng nếu muốn trưng bày art) (y/n): ").lower() == "y"

    print("\n⏳ Đang tạo banner...\n")

    art = image_to_dots(img_path, fixed)

    if boxed:
        art = make_box(art)

    print(art)

    with open("banner.txt", "w", encoding="utf-8") as f:
        f.write(art)

    print("\n✅ Đã lưu banner vào banner.txt")


if __name__ == "__main__":
    main()
