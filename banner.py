from PIL import Image
import os

CHARS = "⣿⣶⣦⣤⣄⣀⠄⠂"

BACKGROUND_CHARS = {" ", "⠄", "⠂"}

MAX_AUTO_WIDTH = 58

def crop_ascii(lines):
    while lines and all(c in BACKGROUND_CHARS for c in lines[0]):
        lines.pop(0)

    while lines and all(c in BACKGROUND_CHARS for c in lines[-1]):
        lines.pop()

    if not lines:
        return lines

    left = min(
        i for line in lines
        for i, c in enumerate(line)
        if c not in BACKGROUND_CHARS
    )
    right = max(
        i for line in lines
        for i, c in enumerate(line)
        if c not in BACKGROUND_CHARS
    )

    return [line[left:right+1] for line in lines]

def image_to_gift_banner(image_path, fixed_size, art_box, save_txt=True):
    try:
        img = Image.open(image_path).convert("L")
    except:
        print("❌ Không mở được file ảnh")
        return

    w, h = img.size
    ratio = h / w

    if fixed_size:
        new_w = w
    else:
        new_w = min(MAX_AUTO_WIDTH, w)

    new_h = int(new_w * ratio * 0.5)
    img = img.resize((new_w, new_h))

    pixels = list(img.getdata())
    raw_lines = []

    for i in range(0, len(pixels), new_w):
        row = pixels[i:i + new_w]
        line = ""
        for p in row:
            idx = p * (len(CHARS) - 1) // 255
            line += CHARS[idx]
        raw_lines.append(line.rstrip())

    final_lines = crop_ascii(raw_lines)

    if art_box:
        width = max(len(line) for line in final_lines)
        top = "=" * (width + 6)
        bottom = "=" * (width + 6)

        framed = [top]
        for line in final_lines:
            framed.append(f"|| {line.ljust(width)} ||")
        framed.append(bottom)

        final_text = "\n".join(framed)
    else:
        final_text = "\n".join(final_lines)

    print(final_text)
    if save_txt:
        name = os.path.splitext(os.path.basename(image_path))[0]
        out = f"banner_{name}.txt"
        with open(out, "w", encoding="utf-8") as f:
            f.write(final_text)
        print(f"\n💾 Đã lưu: {out}")

img_file = input("NHẬP TÊN FILE ẢNH: ").strip()
fixed = input("DÙNG KÍCH THƯỚC CỐ ĐỊNH (y/n): ").lower() == "y"
art_box = input(
    "ART CÓ ĐỂ TRONG KHUNG KHÔNG (dùng nếu muốn trưng bày art) (y/n): "
).lower() == "y"

image_to_gift_banner(img_file, fixed, art_box)
