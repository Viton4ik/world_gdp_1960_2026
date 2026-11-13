import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_video_race"
TEMP_DIR = ".temp_video_assets"
MODE = "DEBT"

def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Создание изолированной виртуальной среды (.venv_video_race)...")
        venv.create(VENV_DIR, with_pip=True)

def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")

def run_bootstrap():
    print("==================================================================")
    if MODE == "GDP":
        print("  ГЕНЕРАТОР ВИДЕО: WORLD'S LARGEST ECONOMIES GDP (1960 - 2026)    ")
    else:
        print("  ГЕНЕРАТОР ВИДЕО: GLOBAL GOVERNMENT DEBT RACE (1926 - 2026)      ")
    print("==================================================================")
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()
    
    print("[2/5] Установка библиотек и портативного кодека FFmpeg в виртуальную среду...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install", 
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])
    
    try:
        print("[3/5] Запуск генерации графики, флагов, музыки и рендеринга MP4...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Самоочистка: удаление виртуальной среды и временных файлов...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Очистка завершена! Проверьте готовый MP4-файл в папке проекта.")

def create_crisp_flag(code, width=78, height=50):
    from PIL import Image, ImageDraw
    import numpy as np

    canvas = Image.new("RGBA", (width + 6, height + 6), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (width, height), (15, 20, 28, 160))
    canvas.paste(shadow, (4, 4))

    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (245, 247, 250)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(40, 53, 107))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx-1, cy-1, cx+1, cy+1], fill=(255, 255, 255))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(222, 41, 16))
        draw.ellipse([int(w*0.1), int(h*0.15), int(w*0.28), int(h*0.42)], fill=(255, 222, 0))
    elif code == "jp":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.3)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(188, 0, 45))
    elif code == "de":
        draw.rectangle([0, 0, w, h//3], fill=(20, 20, 20))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(210, 16, 26))
        draw.rectangle([0, 2*h//3, w, h], fill=(255, 206, 0))
    elif code == "fr":
        draw.rectangle([0, 0, w//3, h], fill=(0, 38, 84))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(248, 250, 252))
        draw.rectangle([2*w//3, 0, w, h], fill=(237, 41, 57))
    elif code == "it":
        draw.rectangle([0, 0, w//3, h], fill=(0, 140, 69))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(248, 250, 252))
        draw.rectangle([2*w//3, 0, w, h], fill=(205, 33, 42))
    elif code == "ru":
        draw.rectangle([0, 0, w, h//3], fill=(248, 250, 252))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(0, 57, 166))
        draw.rectangle([0, 2*h//3, w, h], fill=(213, 43, 30))
    elif code == "nl":
        draw.rectangle([0, 0, w, h//3], fill=(174, 28, 40))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(33, 70, 139))
    elif code == "es":
        draw.rectangle([0, 0, w, h//4], fill=(170, 21, 27))
        draw.rectangle([0, h//4, w, 3*h//4], fill=(241, 191, 0))
        draw.rectangle([0, 3*h//4, w, h], fill=(170, 21, 27))
    elif code == "in":
        draw.rectangle([0, 0, w, h//3], fill=(255, 153, 51))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(19, 136, 8))
        r = int(h * 0.12)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], outline=(0, 0, 128), width=2)
    elif code == "ca":
        draw.rectangle([0, 0, w//4, h], fill=(216, 6, 33))
        draw.rectangle([w//4, 0, 3*w//4, h], fill=(248, 250, 252))
        draw.rectangle([3*w//4, 0, w, h], fill=(216, 6, 33))
        r = int(h * 0.18)
        draw.polygon([(w//2, h//2 - r), (w//2 - r, h//2 + r//2), (w//2 + r, h//2 + r//2)], fill=(216, 6, 33))
    elif code == "br":
        draw.rectangle([0, 0, w, h], fill=(0, 156, 59))
        draw.polygon([(w//2, int(h*0.12)), (int(w*0.88), h//2), (w//2, int(h*0.88)), (int(w*0.12), h//2)], fill=(255, 223, 0))
        r = int(h * 0.18)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(0, 39, 118))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w//2 - 6, 0, w//2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h//2 - 6, w, h//2 + 6], fill=(255, 255, 255))
        draw.rectangle([w//2 - 3, 0, w//2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h//2 - 3, w, h//2 + 3], fill=(200, 16, 46))
    elif code == "mx":
        draw.rectangle([0, 0, w//3, h], fill=(0, 104, 71))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(248, 250, 252))
        draw.rectangle([2*w//3, 0, w, h], fill=(206, 17, 38))
        draw.ellipse([w//2 - 4, h//2 - 4, w//2 + 4, h//2 + 4], fill=(139, 69, 19))
    elif code == "au":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w//2, h//2)], fill=(255, 255, 255), width=3)
        draw.line([(0, h//2), (w//2, 0)], fill=(255, 255, 255), width=3)
        draw.rectangle([w//4 - 2, 0, w//4 + 2, h//2], fill=(200, 16, 46))
        draw.rectangle([0, h//4 - 2, w//2, h//4 + 2], fill=(200, 16, 46))
    elif code == "kr":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.22)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(205, 46, 58))
        draw.chord([w//2 - r, h//2 - r, w//2 + r, h//2 + r], start=0, end=180, fill=(0, 71, 160))
    elif code == "ch":
        draw.rectangle([0, 0, w, h], fill=(218, 41, 28))
        draw.rectangle([w//2 - 4, int(h*0.2), w//2 + 4, int(h*0.8)], fill=(255, 255, 255))
        draw.rectangle([int(w*0.3), h//2 - 4, int(w*0.7), h//2 + 4], fill=(255, 255, 255))
    elif code == "se":
        draw.rectangle([0, 0, w, h], fill=(0, 106, 167))
        draw.rectangle([int(w*0.32), 0, int(w*0.44), h], fill=(254, 204, 2))
        draw.rectangle([0, h//2 - 4, w, h//2 + 4], fill=(254, 204, 2))
    elif code == "tr":
        draw.rectangle([0, 0, w, h], fill=(227, 10, 23))
        r = int(h * 0.22)
        draw.ellipse([w//2 - r - 4, h//2 - r, w//2 + r - 4, h//2 + r], fill=(255, 255, 255))
        r2 = int(h * 0.17)
        draw.ellipse([w//2 - r2, h//2 - r2, w//2 + r2, h//2 + r2], fill=(227, 10, 23))
    elif code == "sa":
        draw.rectangle([0, 0, w, h], fill=(0, 108, 53))
        draw.rectangle([int(w*0.25), int(h*0.62), int(w*0.75), int(h*0.68)], fill=(255, 255, 255))
    elif code == "id":
        draw.rectangle([0, 0, w, h//2], fill=(255, 0, 0))
        draw.rectangle([0, h//2, w, h], fill=(248, 250, 252))
    elif code == "ar":
        draw.rectangle([0, 0, w, h//3], fill=(116, 172, 223))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(116, 172, 223))
        draw.ellipse([w//2 - 4, h//2 - 4, w//2 + 4, h//2 + 4], fill=(246, 180, 14))

    canvas.paste(img, (0, 0))
    return np.array(canvas)

def run_worker():
    import math
    import wave
    import requests
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import matplotlib.animation as animation
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    from PIL import Image
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO = {
        "United States": "us", "China": "cn", "Germany": "de", "Japan": "jp",
        "India": "in", "United Kingdom": "gb", "France": "fr", "Italy": "it",
        "Brazil": "br", "Canada": "ca", "Russia": "ru", "Mexico": "mx",
        "Australia": "au", "South Korea": "kr", "Spain": "es", "Netherlands": "nl",
        "Switzerland": "ch", "Turkey": "tr", "Saudi Arabia": "sa", "Indonesia": "id",
        "Sweden": "se", "Argentina": "ar"
    }

    if MODE == "GDP":
        START_YEAR = 1960.0
        END_YEAR = 2026.83
        TITLE_MAIN = "WORLD'S LARGEST ECONOMIES (GDP)"
        TITLE_SUB = "Nominal GDP in USD (1960 – Oct 2026)  •  Official World Bank & IMF Data"
        FINAL_OUTPUT = "world_gdp_1960_2026_shorts.mp4"
        ANCHORS = {
            "United States":  {1960: 543.3, 1970: 1073.3, 1980: 2857.3, 1990: 5963.1, 2000: 10250.9, 2010: 15049.0, 2020: 21323.0, 2026: 30300.0},
            "China":          {1960: 59.7,  1970: 92.6,   1980: 191.1,  1990: 360.9,  2000: 1211.3,  2010: 6087.2,  2020: 14687.7, 2026: 19500.0},
            "Germany":        {1960: 84.3,  1970: 215.8,  1980: 950.3,  1990: 1771.6, 2000: 1948.0,  2010: 3399.6,  2020: 3889.7,  2026: 4750.0},
            "Japan":          {1960: 44.3,  1970: 212.6,  1980: 1105.4, 1990: 3132.8, 2000: 4968.4,  2010: 5759.1,  2020: 5055.6,  2026: 4400.0},
            "India":          {1960: 37.0,  1970: 62.4,   1980: 186.3,  1990: 321.0,  2000: 468.4,   2010: 1675.6,  2020: 2671.6,  2026: 4350.0},
            "United Kingdom": {1960: 73.2,  1970: 130.7,  1980: 564.9,  1990: 1093.2, 2000: 1665.5,  2010: 2491.4,  2020: 2697.8,  2026: 3750.0},
            "France":         {1960: 62.2,  1970: 148.5,  1980: 701.3,  1990: 1269.1, 2000: 1365.6,  2010: 2645.2,  2020: 2647.4,  2026: 3280.0},
            "Italy":          {1960: 40.4,  1970: 113.4,  1980: 477.3,  1990: 1181.2, 2000: 1146.7,  2010: 2136.1,  2020: 1897.5,  2026: 2420.0},
            "Brazil":         {1960: 17.0,  1970: 42.3,   1980: 237.4,  1990: 462.0,  2000: 655.4,   2010: 2208.9,  2020: 1476.1,  2026: 2350.0},
            "Canada":         {1960: 40.5,  1970: 87.9,   1980: 276.0,  1990: 596.1,  2000: 744.8,   2010: 1617.3,  2020: 1655.7,  2026: 2280.0},
            "Russia":         {1960: 142.0, 1970: 289.0,  1980: 585.0,  1990: 516.8,  2000: 259.7,   2010: 1524.9,  2020: 1493.1,  2026: 2180.0},
            "Mexico":         {1960: 13.0,  1970: 35.5,   1980: 205.1,  1990: 261.3,  2000: 707.9,   2010: 1057.8,  2020: 1120.8,  2026: 2020.0},
            "South Korea":    {1960: 3.9,   1970: 9.0,    1980: 65.4,   1990: 283.4,  2000: 576.2,   2010: 1144.0,  2020: 1644.3,  2026: 1920.0},
            "Australia":      {1960: 18.6,  1970: 41.3,   1980: 149.9,  1990: 311.4,  2000: 415.8,   2010: 1148.6,  2020: 1328.4,  2026: 1850.0},
            "Spain":          {1960: 12.1,  1970: 40.9,   1980: 230.8,  1990: 536.6,  2000: 598.4,   2010: 1422.1,  2020: 1278.1,  2026: 1760.0},
            "Indonesia":      {1960: 8.7,   1970: 9.8,    1980: 78.0,   1990: 114.4,  2000: 165.0,   2010: 755.1,   2020: 1059.1,  2026: 1480.0},
            "Turkey":         {1960: 14.0,  1970: 17.1,   1980: 68.8,   1990: 150.7,  2000: 274.3,   2010: 777.0,   2020: 720.3,   2026: 1340.0},
            "Netherlands":    {1960: 13.5,  1970: 38.2,   1980: 193.8,  1990: 321.4,  2000: 417.6,   2010: 847.4,   2020: 909.8,   2026: 1220.0},
            "Saudi Arabia":   {1960: 4.2,   1970: 5.4,    1980: 164.5,  1990: 117.6,  2000: 189.5,   2010: 528.2,   2020: 734.3,   2026: 1110.0},
            "Switzerland":    {1960: 10.5,  1970: 24.2,   1980: 119.0,  1990: 258.0,  2000: 279.2,   2010: 583.8,   2020: 741.9,   2026: 940.0},
            "Sweden":         {1960: 15.8,  1970: 38.1,   1980: 140.1,  1990: 259.9,  2000: 262.8,   2010: 495.8,   2020: 547.1,   2026: 655.0},
            "Argentina":      {1960: 24.5,  1970: 31.5,   1980: 77.0,   1990: 141.4,  2000: 284.2,   2010: 423.6,   2020: 385.5,   2026: 640.0}
        }
    else:
        START_YEAR = 1926.0
        END_YEAR = 2026.83
        TITLE_MAIN = "GLOBAL GOVERNMENT DEBT"
        TITLE_SUB = "Gross Public Debt in USD (1926 – Oct 2026)  •  Official IMF & World Bank Data"
        FINAL_OUTPUT = "global_government_debt_1926_2026_shorts.mp4"
        ANCHORS = {
            "United States":  {1926: 19.6, 1940: 50.7, 1945: 258.7, 1960: 290.5, 1970: 380.9, 1980: 909.0, 1990: 3206.3, 2000: 5628.7, 2010: 13528.8, 2020: 27747.8, 2026: 35800.0},
            "China":          {1926: 0.8,  1940: 1.5,  1945: 2.2,   1960: 4.5,   1970: 7.0,   1980: 15.0,  1990: 45.0,   2000: 265.0,  2010: 2030.0,  2020: 10200.0, 2026: 16800.0},
            "Japan":          {1926: 2.5,  1940: 9.8,  1945: 35.0,  1960: 4.2,   1970: 24.5,  1980: 550.0, 1990: 2100.0, 2000: 6900.0, 2010: 11800.0, 2020: 13100.0, 2026: 11200.0},
            "United Kingdom": {1926: 36.5, 1940: 42.0, 1945: 95.0,  1960: 78.0,  1970: 82.0,  1980: 240.0, 1990: 350.0,  2000: 610.0,  2010: 1850.0,  2020: 2900.0,  2026: 3650.0},
            "France":         {1926: 14.0, 1940: 18.0, 1945: 28.0,  1960: 18.5,  1970: 30.0,  1980: 145.0, 1990: 450.0,  2000: 810.0,  2010: 2250.0,  2020: 3100.0,  2026: 3550.0},
            "India":          {1926: 1.8,  1940: 2.5,  1945: 4.5,   1960: 12.0,  1970: 25.0,  1980: 75.0,  1990: 230.0,  2000: 340.0,  2010: 1120.0,  2020: 2400.0,  2026: 3350.0},
            "Italy":          {1926: 4.5,  1940: 8.5,  1945: 12.0,  1960: 13.0,  1970: 32.0,  1980: 260.0, 1990: 1100.0, 2000: 1250.0, 2010: 2550.0,  2020: 2950.0,  2026: 3250.0},
            "Germany":        {1926: 3.2,  1940: 25.0, 1945: 45.0,  1960: 14.0,  1970: 38.0,  1980: 290.0, 1990: 710.0,  2000: 1180.0, 2010: 2750.0,  2020: 2700.0,  2026: 2950.0},
            "Canada":         {1926: 2.4,  1940: 4.0,  1945: 16.5,  1960: 22.0,  1970: 42.0,  1980: 135.0, 1990: 440.0,  2000: 610.0,  2010: 1350.0,  2020: 1950.0,  2026: 2350.0},
            "Brazil":         {1926: 0.9,  1940: 1.2,  1945: 2.0,   1960: 4.0,   1970: 14.0,  1980: 85.0,  1990: 180.0,  2000: 410.0,  2010: 1380.0,  2020: 1420.0,  2026: 1950.0},
            "Spain":          {1926: 3.1,  1940: 4.2,  1945: 5.5,   1960: 4.8,   1970: 7.5,   1980: 42.0,  1990: 230.0,  2000: 360.0,  2010: 880.0,   2020: 1550.0,  2026: 1780.0},
            "South Korea":    {1926: 0.1,  1940: 0.2,  1945: 0.3,   1960: 0.6,   1970: 2.1,   1980: 14.0,  1990: 36.0,   2000: 105.0,  2010: 340.0,   2020: 790.0,   2026: 1050.0},
            "Australia":      {1926: 2.2,  1940: 3.1,  1945: 7.8,   1960: 8.5,   1970: 14.0,  1980: 38.0,  1990: 55.0,   2000: 78.0,   2010: 260.0,   2020: 780.0,   2026: 950.0},
            "Mexico":         {1926: 0.6,  1940: 0.8,  1945: 1.4,   1960: 3.2,   1970: 11.0,  1980: 68.0,  1990: 125.0,  2000: 240.0,  2010: 450.0,   2020: 650.0,   2026: 920.0},
            "Netherlands":    {1926: 1.1,  1940: 1.8,  1945: 4.2,   1960: 5.5,   1970: 12.0,  1980: 82.0,  1990: 220.0,  2000: 235.0,  2010: 510.0,   2020: 520.0,   2026: 580.0},
            "Indonesia":      {1926: 0.3,  1940: 0.5,  1945: 0.9,   1960: 2.1,   1970: 4.8,   1980: 24.0,  1990: 52.0,   2000: 148.0,  2010: 195.0,   2020: 415.0,   2026: 560.0},
            "Russia":         {1926: 1.2,  1940: 4.5,  1945: 14.0,  1960: 18.0,  1970: 28.0,  1980: 65.0,  1990: 120.0,  2000: 160.0,  2010: 170.0,   2020: 290.0,   2026: 420.0},
            "Turkey":         {1926: 0.4,  1940: 0.7,  1945: 1.1,   1960: 2.8,   1970: 5.5,   1980: 21.0,  1990: 48.0,   2000: 105.0,  2010: 310.0,   2020: 285.0,   2026: 410.0},
            "Saudi Arabia":   {1926: 0.1,  1940: 0.2,  1945: 0.3,   1960: 0.5,   1970: 0.8,   1980: -5.0,  1990: 65.0,   2000: 160.0,  2010: 45.0,    2020: 238.0,   2026: 340.0},
            "Switzerland":    {1926: 0.9,  1940: 1.6,  1945: 3.8,   1960: 4.2,   1970: 7.5,   1980: 36.0,  1990: 82.0,   2000: 130.0,  2010: 215.0,   2020: 310.0,   2026: 330.0},
            "Argentina":      {1926: 1.3,  1940: 1.9,  1945: 2.8,   1960: 5.5,   1970: 9.8,   1980: 28.0,  1990: 62.0,   2000: 145.0,  2010: 185.0,   2020: 320.0,   2026: 310.0},
            "Sweden":         {1926: 0.7,  1940: 1.4,  1945: 3.2,   1960: 5.0,   1970: 11.5,  1980: 58.0,  1990: 115.0,  2000: 140.0,  2010: 190.0,   2020: 215.0,   2026: 225.0}
        }

    print(" -> Подготовка прямоугольных флагов стран (с мягкой тенью, без рамок)...")
    flags = {country: create_crisp_flag(code, 78, 50) for country, code in COUNTRIES_ISO.items()}

    print(" -> Подготовка фоновой музыки (Royalty-Free / CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "bg_music.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: Deep Financial Pulse (Ambient Synthwave Procedural Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    freqs_base = np.select(
        [(t % 8) < 2, (t % 8) < 4, (t % 8) < 6, (t % 8) >= 6],
        [110.0, 87.31, 130.81, 98.0]
    )
    pulse = 0.5 + 0.5 * np.sin(2 * math.pi * 2.0 * t)
    bass = 0.25 * np.sin(2 * math.pi * freqs_base * t) * pulse
    pad1 = 0.15 * np.sin(2 * math.pi * (freqs_base * 1.5) * t)
    pad2 = 0.10 * np.sin(2 * math.pi * (freqs_base * 2.0) * t + 0.5)
    arp = 0.08 * np.sin(2 * math.pi * (freqs_base * 3.0) * t) * (0.5 + 0.5 * np.sin(2 * math.pi * 4.0 * t))

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((bass + pad1 + arp) * envelope, -0.95, 0.95)
    stereo_right = np.clip((bass + pad2 + arp) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Построение матрицы данных с плавной пересортировкой (Hann Window Smoothing)...")
    fine_years = np.linspace(START_YEAR, END_YEAR, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    # Если статистика ушла в минус или 0, страна исключается из рейтинга и уходит из кадра
    df_values = df_values.where(df_values > 0, np.nan)
    df_ranks = df_values.rank(axis=1, method='first', ascending=True).fillna(0.0)

    win_size = 35
    hann_win = np.hanning(win_size)
    hann_win /= hann_win.sum()
    df_ranks_smooth = df_ranks.apply(
        lambda col: np.convolve(np.pad(col.values, (win_size//2, win_size//2), mode='edge'), hann_win, mode='valid')[:len(col)]
    )

    def format_usd(val_billion):
        if val_billion >= 1000.0:
            return f"${val_billion / 1000.0:,.2f}T"
        return f"${val_billion:,.0f}B"

    def axis_fmt(x, pos):
        if x == 0:
            return "$0"
        elif x >= 1000:
            return f"${x/1000:.0f}T"
        return f"${x:.0f}B"

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Рендеринг 40-секундного видео HD 9:16 ({TOTAL_FRAMES} кадров, 30 FPS)...")
    BG_GRAY = '#474e59'
    PLOT_BG_GRAY = '#3f4650'

    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor(BG_GRAY)

    # Левые 34% ширины экрана выделены под колонку Названий и Флагов в фиксированных координатах осей
    ax = fig.add_axes([0.34, 0.06, 0.62, 0.79])

    # Статическая шапка в верхней зоне фигуры (никогда не пересекается с верхним бегунком)
    fig.text(
        0.5, 0.935, TITLE_MAIN,
        color='#ffffff', fontsize=22, fontweight='bold', ha='center', va='center'
    )
    fig.text(
        0.5, 0.902, TITLE_SUB,
        color='#bae6fd', fontsize=11.0, fontweight='bold', ha='center', va='center'
    )
    line_ax = fig.add_axes([0.05, 0.878, 0.90, 0.002])
    line_ax.set_facecolor('#7dd3fc')
    line_ax.set_xticks([])
    line_ax.set_yticks([])
    for sp in line_ax.spines.values():
        sp.set_visible(False)

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor(PLOT_BG_GRAY)

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.7].dropna()
        max_val = max(vals_row.max(), 10.0)

        ax.set_xlim(0, max_val * 1.25)
        ax.set_ylim(min_visible_rank - 0.65, max_rank + 0.65)
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(axis_fmt))

        ax.xaxis.grid(True, color='#64748b', linestyle='--', linewidth=0.9, alpha=0.5, zorder=0)
        ax.set_axisbelow(True)

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.7)) / 0.7))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            r_c = 0.12 + 0.05 * norm_rank
            g_c = 0.16 + 0.08 * norm_rank
            b_c = 0.21 + 0.13 * norm_rank
            bar_color = (r_c, g_c, b_c, alpha)

            # 1. Мягкая 3D-тень под полоской
            ax.barh(
                smooth_y - 0.055, val + max_val * 0.004, height=0.54,
                color='#141920', alpha=0.65 * alpha, zorder=2, edgecolor='none'
            )

            # 2. Основная полоска (темно-серая с синеватым отливом, БЕЗ рамок-квадратов edgecolor='none')
            ax.barh(
                smooth_y, val, height=0.54,
                color=bar_color, edgecolor='none', zorder=3
            )

            # 3. 3D-фаска вдоль верхнего края полоски
            bevel_h = 0.09
            ax.barh(
                smooth_y + (0.54 / 2.0) - (bevel_h / 2.0), val, height=bevel_h,
                color='#7dd3fc', alpha=0.22 * alpha, zorder=4, edgecolor='none'
            )

            # 4. Акцентный синеватый торец на правом конце полоски
            cap_w = max_val * 0.007
            ax.barh(
                smooth_y, cap_w, left=max(0, val - cap_w), height=0.54,
                color='#60a5fa', alpha=0.85 * alpha, zorder=4, edgecolor='none'
            )

            # 5. ПРЯМОУГОЛЬНЫЙ ФЛАГ — строго в фиксированной колонке X = -0.075 (axes fraction)
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.46, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (-0.075, smooth_y),
                    xycoords=('axes fraction', 'data'),
                    frameon=False,
                    box_alignment=(0.5, 0.5),
                    zorder=5,
                    annotation_clip=False
                )
                ax.add_artist(ab)

            # 6. НАЗВАНИЕ СТРАНЫ — строго в фиксированной колонке X = -0.155 (axes fraction)
            ax.text(
                -0.155, smooth_y, country,
                transform=ax.get_yaxis_transform(),
                color='#ffffff', fontsize=13.0, fontweight='bold',
                va='center', ha='right', alpha=alpha, zorder=6, clip_on=False
            )

            # 7. СУММА В ДОЛЛАРАХ — справа от конца полоски
            ax.text(
                val + max_val * 0.020, smooth_y, format_usd(val),
                color='#e0f2fe', fontsize=13.0, fontweight='bold',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#94a3b8')
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_color('#64748b')
        ax.tick_params(axis='x', colors='#cbd5e1', labelsize=10.5)

        ax.text(
            0.96, 0.11, f"{year_int}", transform=ax.transAxes,
            color='#313740', fontsize=74, fontweight='bold', ha='right', va='center', zorder=1
        )
        ax.text(
            0.95, 0.045, f"{date_str}", transform=ax.transAxes,
            color='#bae6fd', fontsize=22, fontweight='bold', ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Прогресс рендеринга: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} кадров)")

    temp_video = os.path.join(TEMP_DIR, "silent_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5000, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    print(" -> Наложение фоновой музыки и сборка финального MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_OUTPUT
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> УСПЕХ! Готовый видеофайл сохранен: {FINAL_OUTPUT}")

if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
