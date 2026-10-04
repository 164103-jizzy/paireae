import time
import sys

lyrics = [
    ("ถ้าหากรักนี้ ไม่บอกไม่พูดไม่กล่าว",0.195 ,0.05),
    ("แล้วเขาจะรู้ว่ารักหรือเปล่า",0.09 ,0.7),
    ("อาจจะไม่แน่ใจ",0.2, 0.63),
    ("อยากให้เขารู้ ฉันคงต้องแสดงออก",0.195 , 0.5),
    ("ไม่ใช่ให้ใครเขาบอก",0.14 , 0.4),
    ("หรือว่าให้เขาเดาเอง",0.14, 0.5),
    ("ว่ารัก 'เธอ'", 0.23, 1)
]

def lines(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def music():
    for text, delay, pause in lyrics:
        lines(text, delay)
        time.sleep(pause)

music()