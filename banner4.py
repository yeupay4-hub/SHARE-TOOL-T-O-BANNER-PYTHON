import cv2
import numpy as np
import sys
import subprocess

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

try:
    import cv2
except ImportError:
    print("⚙️ Đang cài opencv-python...")
    install("opencv-python")
    import cv2

try:
    import numpy as np
except ImportError:
    print("⚙️ Đang cài numpy...")
    install("numpy")
    import numpy as np

BRAILLE_BASE = 0x2800
BRAILLE_MAP = [
    (0,0,0x01),(1,0,0x02),(2,0,0x04),(3,0,0x40),
    (0,1,0x08),(1,1,0x10),(2,1,0x20),(3,1,0x80)
]

def img_to_braille(img, frame):
    h, w = img.shape
    lines = []

    for y in range(0, h - 3, 4):
        line = ""
        for x in range(0, w - 1, 2):
            bits = 0
            for dy, dx, bit in BRAILLE_MAP:
                if img[y+dy, x+dx] > 0:
                    bits |= bit
            line += chr(BRAILLE_BASE + bits)
        lines.append(line)

    if frame:
        max_len = max(len(l) for l in lines)

        top    = "┌" + "─" * max_len + "┐"
        bottom = "└" + "─" * max_len + "┘"

        framed = [top]
        for l in lines:
            framed.append("│" + l.ljust(max_len) + "│")
        framed.append(bottom)

        return "\n".join(framed)

    return "\n".join(lines)

def main():
    print("=== TOOL TẠO NÉT BANNER ===")

    fname = input("NHẬP TÊN FILE ẢNH: ").strip()
    fixed = input("DÙNG KÍCH THƯỚC CỐ ĐỊNH (y/n): ").lower() == "y"
    frame = input("CÓ DÙNG KHUNG XUNG QUANH BANNER KHÔNG (y/n): ").lower() == "y"

    img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("❌ Không mở được ảnh")
        return

    h, w = img.shape

    if fixed:
        max_w = 360
        if w > max_w:
            scale = max_w / w
            img = cv2.resize(img, (int(w * scale), int(h * scale)))
    else:
        target_w = 100
        scale = target_w / w
        img = cv2.resize(img, (target_w, int(h * scale)))

    edges = cv2.Canny(img, 60, 130)
    edges = cv2.dilate(edges, np.ones((2,2), np.uint8), 1)

    banner = img_to_braille(edges, frame)

    with open("banner.txt", "w", encoding="utf-8") as f:
        f.write(banner)

    print("\n✅ ĐÃ TẠO BANNER")
    print("📄 File: banner.txt\n")
    print(banner)

if __name__ == "__main__":
    main()
