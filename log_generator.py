import random
import time
import sys

LEVELS = ["INFO", "WARNING", "ERROR"]
MESSAGES = [
    "任務完成", "資料處理中", "連線成功", "發現小問題", "磁碟空間不足", "找不到檔案",
    "操作逾時", "未知例外發生"
]

while True:
    level = random.choice(LEVELS)
    msg = random.choice(MESSAGES)
    print(f"{level}: {msg}", flush=True)
    time.sleep(1)

