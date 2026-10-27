# -*- coding: utf-8 -*-
import json
import os
import re

courses_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\courses.json"
search_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\search-index.json"

# 1. Update courses.json
with open(courses_path, 'r', encoding='utf-8') as f:
    courses_data = json.load(f)

# Update category counts
for cat in courses_data["categories"]:
    if cat["id"] == "safety":
        cat["count"] = 2
    elif cat["id"] == "all":
        cat["count"] = 8

c6_course = {
    "id": "pv-distribution-safety-regulations-20261027",
    "slug": "pv-distribution-safety-regulations",
    "title": "太陽光電設置乙級技術士回訓課程——配電線路現場工作安全注意事項說明",
    "subtitle": "麥肯錫顧問風格 10 分鐘精華導讀 ✕ 20 頁金字塔原理簡報 ✕ 台電配電現場工安法典",
    "instructor": "台電配電線路安全權威 ＆ 葉大衛",
    "date": "2026-10-27",
    "category": "safety",
    "status": "ready",
    "badge": "旗艦回訓核心課",
    "recordingDuration": "51 分鐘",
    "slidesCount": 20,
    "sourceHandoutPages": 20,
    "url": "courses/pv-distribution-safety-regulations.html",
    "coreThesis": "只要張開眼睛，風險就在身邊；嚴格落實 5151 單人閉環作業與公安三護『自護為核心』，恪守未檢電接地前一律視為活電，以制度、紀律與直覺本能築起零職災生命防線。",
    "highlights": [
        "台電 3 層 5 級風控與事故病灶：風險震央集中在基層現場單位（佔案件 95% 以上）；資淺領班與年資斷層引發誤判，職災傷亡主管連帶民刑訴訟長達十餘年。",
        "5151 原則與檢電接地鐵律：一定位、一指令、一複誦、一操作、一回報（單人單步閉環）；公安三護自護佔 70%（絕不把生命交給領班）；未完成檢電接地前一律視為活電。",
        "電氣血淚事故與工法軍規：電纜溝踩踏擠穿絕緣層引爆電弧（必鋪防火毯）；低壓 220V 右手進左手出流經心臟（隔週組織潰爛亡）；路燈架空改地下未拆線雙電源逆送；局限空間四合一測氣（硫化氫攪水暴釋奪命）。"
    ],
    "oneSentenceTakeaway": "自護為本親自檢電接地，嚴守 5151 單人閉環與 1.5m 支撐通道，讓安全成為直覺本能。",
    "modules": [
        {
            "moduleNo": 1,
            "name": "台電風控架構與高危成因",
            "slides": "01-04",
            "summary": "3層5級風控體系、現場案件佔95%震央、勞檢六大常見缺失、資淺領班斷層與主管連帶訴訟十年。"
        },
        {
            "moduleNo": 2,
            "name": "5151作業原則與公安三護",
            "slides": "05-08",
            "summary": "5151單人單步閉環操作、公安三護自護為本70%、隨身檢電筆與未接地前全視為活電、跨區處轉供彈開接地夾慘劇。"
        },
        {
            "moduleNo": 3,
            "name": "電氣感電與逆送血淚案例",
            "slides": "09-12",
            "summary": "電纜溝踩踏擠穿絕緣電弧灼傷、低壓220V流經心臟隔週組織潰爛亡、升空車隱蔽物脫落相間短路、路燈雙電源逆送電擊。"
        },
        {
            "moduleNo": 4,
            "name": "道路交維與高差防墜標準",
            "slides": "13-16",
            "summary": "站馬路反光背心進工地安全帽、電動旗手電池包膠、起重機一機三證0.25m過卷停機、高差1.5m通道2m防墜網、4m電桿墜落鋼絲剪撞腰椎。"
        },
        {
            "moduleNo": 5,
            "name": "局限空間深開挖與十條軍規",
            "slides": "17-20",
            "summary": "局限空間四合一氣體（硫化氫攪水暴釋案例）、深開挖超1.5m擋土支撐、電纜套管壓接次數與簽字追溯責任制、配電工安十條軍規。"
        }
    ]
}

# Replace or append Course 6
existing_idx = None
for i, c in enumerate(courses_data["courses"]):
    if c["slug"] == "pv-distribution-safety-regulations":
        existing_idx = i
        break

if existing_idx is not None:
    courses_data["courses"][existing_idx] = c6_course
else:
    # Insert after course 5 (grid policies)
    insert_pos = len(courses_data["courses"])
    for i, c in enumerate(courses_data["courses"]):
        if c["slug"] == "pv-grid-connection-policies":
            insert_pos = i + 1
            break
    courses_data["courses"].insert(insert_pos, c6_course)

with open(courses_path, 'w', encoding='utf-8') as f:
    json.dump(courses_data, f, ensure_ascii=False, indent=2)
print("Updated data/courses.json successfully!")

# 2. Update search-index.json
from generate_deck_c6 import slides_data as c6_slides

with open(search_path, 'r', encoding='utf-8') as f:
    search_data = json.load(f)

# Remove existing c6 slides if any
search_data = [item for item in search_data if item.get("courseSlug") != "pv-distribution-safety-regulations"]

# Append new c6 slides
for s in c6_slides:
    sn = s["slideNo"]
    text_content = f"{s['title']} {s['question']} {' '.join(s['highlights'])} {s['takeaway']} {s['visualTitle']} {s['noteTakeaway']} {s['noteDetail']} {s['noteTransition']}"
    # Clean HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', text_content)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    tags = ["配電線路", "工作安全", "台電工安", "5151原則", "檢電掛接地", "工安軍規"]
    if "3層5級" in clean_text or "風控" in clean_text: tags.extend(["3層5級風控", "風險震央"])
    if "領班" in clean_text or "訴訟" in clean_text: tags.extend(["資淺領班", "主管訴訟責任"])
    if "公安三護" in clean_text or "自護" in clean_text: tags.extend(["公安三護", "自護為核心"])
    if "跨區處" in clean_text or "轉供" in clean_text: tags.extend(["跨區處轉供", "低壓接地夾彈開", "CX40", "T121"])
    if "電纜溝" in clean_text or "防火毯" in clean_text: tags.extend(["電纜溝踩踏", "擠穿絕緣", "防火毯"])
    if "低壓感電" in clean_text or "心臟" in clean_text: tags.extend(["低壓感電", "流經心臟", "體內組織潰爛"])
    if "升空車" in clean_text or "隱蔽" in clean_text: tags.extend(["升空車短路", "隱蔽物脫落", "絕緣手套炸黑"])
    if "路燈" in clean_text or "逆送" in clean_text: tags.extend(["雙電源逆送", "路燈架空改地下未拆線"])
    if "交維" in clean_text or "反光背心" in clean_text: tags.extend(["道路交維", "站馬路反光背心", "進工地安全帽", "旗手電池包膠"])
    if "起重機" in clean_text or "一機三證" in clean_text or "過卷" in clean_text: tags.extend(["起重機一機三證", "0.25m過卷停機", "6年超音波探傷", "斜坡止滑墊"])
    if "高差" in clean_text or "防墜" in clean_text or "通道" in clean_text: tags.extend(["高差1.5m通道", "2m防墜護欄", "全身背負雙大鉤", "4m電桿墜落鋼絲剪"])
    if "局限空間" in clean_text or "硫化氫" in clean_text or "氣體" in clean_text: tags.extend(["局限空間四合一", "氧氣18%", "硫化氫攪水暴釋"])
    if "開挖" in clean_text or "擋土" in clean_text: tags.extend(["深開挖超1.5m", "擋土支撐", "露天開挖主管", "斜坡立桿2.1m"])
    if "壓接" in clean_text or "簽字" in clean_text or "操作棒" in clean_text: tags.extend(["壓接套管大線3次", "電纜頭簽字追溯", "絕緣操作棒切熔絲"])
    if "十條軍規" in clean_text: tags.append("工安十條軍規")
    
    search_data.append({
        "courseId": "pv-distribution-safety-regulations-20261027",
        "courseSlug": "pv-distribution-safety-regulations",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——配電線路現場工作安全注意事項說明",
        "slideNo": sn,
        "slideTitle": s["title"],
        "module": s["module"],
        "tags": list(set(tags)),
        "content": clean_text,
        "url": f"courses/pv-distribution-safety-regulations.html#s{sn}"
    })

with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)
print(f"Updated data/search-index.json successfully! Total slides indexed: {len(search_data)}")
