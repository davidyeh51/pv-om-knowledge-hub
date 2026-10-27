# -*- coding: utf-8 -*-
import json
import os

courses_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\courses.json"
search_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\search-index.json"

# 1. Update courses.json
with open(courses_path, 'r', encoding='utf-8') as f:
    courses_data = json.load(f)

# Update category counts
has_trading_cat = False
for cat in courses_data["categories"]:
    if cat["id"] == "trading":
        has_trading_cat = True
        cat["count"] = 1
    elif cat["id"] == "all":
        cat["count"] = 5

if not has_trading_cat:
    courses_data["categories"].append({
        "id": "trading",
        "name": "綠電交易與憑證",
        "count": 1
    })

c4_course = {
    "id": "green-power-trading-trec-20261027",
    "slug": "green-power-trading-trec",
    "title": "太陽光電設置乙級技術士回訓課程——綠電交易機制與再生能源憑證制度",
    "subtitle": "麥肯錫顧問風格 10 分鐘精華導讀 ✕ 20 頁金字塔原理簡報 ✕ 綠電憑證與自由化市場",
    "instructor": "張彥堂 科長 (經濟部標檢局憑證中心) ＆ 葉大衛",
    "date": "2026-10-27",
    "category": "trading",
    "status": "ready",
    "badge": "旗艦回訓核心課",
    "recordingDuration": "55 分鐘",
    "slidesCount": 20,
    "sourceHandoutPages": 20,
    "url": "courses/green-power-trading-trec.html",
    "coreThesis": "T-REC 憑證是唯一官方法定綠電身分證；善用二三型設備售電鬆綁、沙盒 3.0 事後彈性分配與零股化新制，打破發用電時空錯配，實現綠電採購效益最大化。",
    "highlights": [
        "二三型免轉一型發電業鬆綁：屋頂自用光電免去委員現勘與技術員高成本，直接透過售電業賣電，引爆百萬瓩「螞蟻雄兵」自由市場供給。",
        "台電沙盒 3.0 事後彈性劃撥：打破事前合約固定比例限制，事後依需求劃撥重點電號，資料提供費更斷崖暴降 98% (大戶由 120 萬降至 2.4 萬)。",
        "三大新制賦能企業：零股化按月結清對齊跨國多元財年、解約轉綠電次日拍照追溯起算點、單一電號多主體依出資比例拆分憑證。"
    ],
    "oneSentenceTakeaway": "以法規為基石、以沙盒 3.0 為操盤武器，徹底告別躉購依賴，釋放民間綠電最大商業價值。",
    "modules": [
        {
            "moduleNo": 1,
            "name": "綠電憑證本質與國際範疇界定",
            "slides": "01-04",
            "summary": "T-REC唯一官方綠電身分證、轉讓一次為限、RE100五大綠能正名、廢棄物抽蓄排除、申請前置公文與CBAM認PPA實務。"
        },
        {
            "moduleNo": 2,
            "name": "綠電交易市場演進與路徑全貌",
            "slides": "05-08",
            "summary": "98年FIT拓荒到106年電業自由化、4A自用/4B電證分離/PPA直轉供三大體系、二三型售電大鬆綁與存憑證現貨真相。"
        },
        {
            "moduleNo": 3,
            "name": "自由市場定價與便民推廣政策",
            "slides": "09-12",
            "summary": "台電FIT費率下限錨定疊加加成、台資電統購分銷突破聯貸信評枷鎖、台電小額綠電練兵場與中小企業4.3元平價競標市集。"
        },
        {
            "moduleNo": 4,
            "name": "無電號租戶解方與沙盒3.0彈性分配",
            "slides": "13-16",
            "summary": "台北101綠色大樓團購破2億度、供需季節作息雙重錯配、台電15分鐘四水桶同區間二次彌合與沙盒3.0規費狂降98%事後劃撥。"
        },
        {
            "moduleNo": 5,
            "name": "2026最新變革與維運十條軍規",
            "slides": "17-20",
            "summary": "零股化按月結算對齊全球財年、查核打破分區與1MW自撰報告快速發證、年底三大新法規預告與綠電採購維運十條軍規。"
        }
    ]
}

# Replace or append Course 4
existing_idx = None
for i, c in enumerate(courses_data["courses"]):
    if c["slug"] == "green-power-trading-trec":
        existing_idx = i
        break

if existing_idx is not None:
    courses_data["courses"][existing_idx] = c4_course
else:
    # Insert after course 3 (bess)
    insert_pos = len(courses_data["courses"])
    for i, c in enumerate(courses_data["courses"]):
        if c["slug"] == "bess-technologies-applications":
            insert_pos = i + 1
            break
    courses_data["courses"].insert(insert_pos, c4_course)

with open(courses_path, 'w', encoding='utf-8') as f:
    json.dump(courses_data, f, ensure_ascii=False, indent=2)
print("Updated data/courses.json successfully!")

# 2. Update search-index.json
from generate_deck_c4 import slides_data as c4_slides

with open(search_path, 'r', encoding='utf-8') as f:
    search_data = json.load(f)

# Remove existing c4 slides if any
search_data = [item for item in search_data if item.get("courseSlug") != "green-power-trading-trec"]

# Append new c4 slides
for s in c4_slides:
    sn = s["slideNo"]
    text_content = f"{s['title']} {s['question']} {' '.join(s['highlights'])} {s['takeaway']} {s['visualTitle']} {s['noteTakeaway']} {s['noteDetail']} {s['noteTransition']}"
    # Clean HTML tags
    import re
    clean_text = re.sub(r'<[^>]+>', ' ', text_content)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    tags = ["綠電憑證", "T-REC", "綠電交易", "經濟部標檢局", "RE100", "台電轉供"]
    if "二三型" in clean_text: tags.append("二三型鬆綁")
    if "沙盒" in clean_text: tags.append("沙盒3.0")
    if "零股" in clean_text: tags.append("零股化")
    if "101" in clean_text or "租戶" in clean_text: tags.append("無電號租戶")
    if "FIT" in clean_text or "躉購" in clean_text: tags.append("FIT躉購")
    if "CBAM" in clean_text or "碳排" in clean_text: tags.append("CBAM碳盤查")
    if "台資電" in clean_text or "統購" in clean_text: tags.append("台資電統購分銷")
    if "小額綠電" in clean_text: tags.append("台電小額綠電")
    if "軍規" in clean_text: tags.append("綠電十條軍規")
    
    search_data.append({
        "courseId": "green-power-trading-trec-20261027",
        "courseSlug": "green-power-trading-trec",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——綠電交易機制與再生能源憑證制度",
        "slideNo": sn,
        "slideTitle": s["title"],
        "module": s["module"],
        "tags": list(set(tags)),
        "content": clean_text,
        "url": f"courses/green-power-trading-trec.html#s{sn}"
    })

with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)
print(f"Updated data/search-index.json successfully! Total slides indexed: {len(search_data)}")
