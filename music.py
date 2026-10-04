import sys    # ใช้ sys.stdout.flush() ให้ตัวอักษรขึ้นทันที
import time   # ใช้ time.sleep() หน่วงเวลา

# แต่ละบรรทัดคือ (ข้อความ, เวลาต่อตัวอักษร, เวลาพักหลังพิมพ์จบ)
# - เวลาต่อตัวอักษร: ยิ่งน้อยยิ่งพิมพ์เร็ว (วินาที)
# - เวลาพัก: หยุดนานแค่ไหนก่อนขึ้นบรรทัดถัดไป (วินาที)
# ใส่ข้อความของตัวเองได้เลย
lines = [
    ("billy jean not my lover.", 0.1, 5.0),
    ("she just the girl.", 0.08, 1.0),
    ("claim i'm the one.", 0.15, 1.0),
]


def type_line(text, char_delay):
    for char in text:
        sys.stdout.write(char)   # เขียนตัวอักษรออกจอ (ยังไม่ขึ้นบรรทัดใหม่)
        sys.stdout.flush()       # บังคับให้แสดงทันที ไม่งั้นจะออกมาเป็นก้อนเดียว
        time.sleep(char_delay)   # รอก่อนพิมพ์ตัวถัดไป
    sys.stdout.write("\n")       # พิมพ์จบแล้วขึ้นบรรทัดใหม่


def main():
    for text, char_delay, pause in lines:
        type_line(text, char_delay)
        time.sleep(pause)        # พักก่อนขึ้นประโยคถัดไป


main()