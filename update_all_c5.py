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
    if cat["id"] == "inverter":
        cat["count"] = 2
    elif cat["id"] == "all":
        cat["count"] = 7

c5_course = {
    "id": "pv-grid-connection-policies-20261027",
    "slug": "pv-grid-connection-policies",
    "title": "太陽光電設置乙級技術士回訓課程——光電併網與相關政策趨勢",
    "subtitle": "麥肯錫顧問風格 10 分鐘精華導讀 ✕ 20 頁金字塔原理簡報 ✕ 併網六大階段與最新法規",
    "instructor": "吳家進 課長 (台電配電處) ＆ 葉大衛",
    "date": "2026-10-27",
    "category": "inverter",
    "status": "ready",
    "badge": "旗艦回訓核心課",
    "recordingDuration": "47 分鐘",
    "slidesCount": 20,
    "sourceHandoutPages": 20,
    "url": "courses/pv-grid-connection-policies.html",
    "coreThesis": "併網合規是電廠商轉的命脈；嚴格卡控 2 個月簽約與 1 年完工時效紅線，把握全數換新 VPC 突破容量上限新政，杜絕孤島逆送與先發後用檢驗卡點，確保併網收益分秒不漏。",
    "highlights": [
        "併網六階段與嚴格時效紅線：取得地方備案後 2 個月內必辦台電簽約，簽約後 1 年內必須完工登記，逾期備案失效費率跌落；細部協商專注交流側責任分界點保護協調 (50/51/27/59)。",
        "第三型全數汰舊換新 VPC 擴容新政：更換為高效能模組 (VPC) 可突破原登記容量上限（饋線有容量為前提），免重附土地建物權狀，原容量保歷史高費率、新增容量享新費率雙軌結算。",
        "新建千坪建物強制設光電與台電跑兩趟：新建/增改建 ≥1,000m² 每 20m² 強制設 1kW，CNS 61215 靜態負載 5,400Pa 抗 17 級強颱；市電斷電 ATS 實體切離獨立運轉，台電檢驗班長跑兩趟『先發後用』卡控使照送電。"
    ],
    "oneSentenceTakeaway": "以時效守住歷史高費率，以 VPC 換新突破饋線容量，以 ATS 隔離與合格送電貫徹併網軍規。",
    "modules": [
        {
            "moduleNo": 1,
            "name": "太陽光電併網六大階段與時效紅線",
            "slides": "01-04",
            "summary": "併聯審查至售電結算六大階段、2個月簽約與1年完工時效、配電區處審查合併與保護協調邊界、前送電掛表度數第一期結清。"
        },
        {
            "moduleNo": 2,
            "name": "第三型光電全數汰舊換新擴容新政",
            "slides": "05-08",
            "summary": "管理辦法第16條突破容量上限、全數更換VPC高效模組、免重附土地建物證明、新舊雙軌費率結算與圖審CT/PT擴容配套。"
        },
        {
            "moduleNo": 3,
            "name": "新建建築物強制設置太陽光電",
            "slides": "09-12",
            "summary": "發展條例第12條之1國土署三擇一千坪門檻、每20m²強制設1kW、台電核減與豁免條件、CNS 61215 5400Pa與維護爬梯規範。"
        },
        {
            "moduleNo": 4,
            "name": "孤島獨立運轉與台電兩次檢驗卡控",
            "slides": "13-16",
            "summary": "市電中斷ATS自動/手動實體隔離防逆送、光電轉供公設維生盤、建照附圖說使照附發電許可、台電檢驗班長跑兩趟先發後用。"
        },
        {
            "moduleNo": 5,
            "name": "第三型變流器簡化更換與十條軍規",
            "slides": "17-20",
            "summary": "變流器1:1容量相同先換後報備抽核、三相禁改單相、年底法規變更預告與光電併網運維十條軍規。"
        }
    ]
}

# Replace or append Course 5
existing_idx = None
for i, c in enumerate(courses_data["courses"]):
    if c["slug"] == "pv-grid-connection-policies":
        existing_idx = i
        break

if existing_idx is not None:
    courses_data["courses"][existing_idx] = c5_course
else:
    # Insert after course 4 (green power trading)
    insert_pos = len(courses_data["courses"])
    for i, c in enumerate(courses_data["courses"]):
        if c["slug"] == "green-power-trading-trec":
            insert_pos = i + 1
            break
    courses_data["courses"].insert(insert_pos, c5_course)

with open(courses_path, 'w', encoding='utf-8') as f:
    json.dump(courses_data, f, ensure_ascii=False, indent=2)
print("Updated data/courses.json successfully!")

# 2. Update search-index.json
from generate_deck_c5 import slides_data as c5_slides

with open(search_path, 'r', encoding='utf-8') as f:
    search_data = json.load(f)

# Remove existing c5 slides if any
search_data = [item for item in search_data if item.get("courseSlug") != "pv-grid-connection-policies"]

# Append new c5 slides
for s in c5_slides:
    sn = s["slideNo"]
    text_content = f"{s['title']} {s['question']} {' '.join(s['highlights'])} {s['takeaway']} {s['visualTitle']} {s['noteTakeaway']} {s['noteDetail']} {s['noteTransition']}"
    # Clean HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', text_content)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    tags = ["台電併網", "併網政策", "台電配電處", "吳家進", "併聯規範", "太陽光電法規"]
    if "六階段" in clean_text or "時效" in clean_text: tags.extend(["併網六階段", "2個月簽約", "1年完工"])
    if "細部協商" in clean_text or "責任分界" in clean_text: tags.extend(["細部協商", "責任分界點", "保護協調"])
    if "汰舊換新" in clean_text or "VPC" in clean_text: tags.extend(["汰舊換新", "VPC高效模組", "突破容量上限", "雙軌費率"])
    if "新建" in clean_text or "國土署" in clean_text: tags.extend(["新建建築物", "國土署門檻", "每20m²設1k", "建築面積1000m²"])
    if "CNS" in clean_text or "5400" in clean_text: tags.extend(["CNS 61215", "5400Pa", "17級強颱", "維護爬梯"])
    if "孤島" in clean_text or "ATS" in clean_text: tags.extend(["孤島運轉", "ATS實體隔離", "防逆送電", "維生盤"])
    if "跑兩趟" in clean_text or "先發後用" in clean_text: tags.extend(["台電跑兩趟", "先發後用", "掛表送電", "使照卡控"])
    if "變流器更換" in clean_text or "先換後報" in clean_text: tags.extend(["變流器更換", "先換後報備", "三相不可換單相"])
    if "軍規" in clean_text: tags.append("併網十條軍規")
    
    search_data.append({
        "courseId": "pv-grid-connection-policies-20261027",
        "courseSlug": "pv-grid-connection-policies",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——光電併網與相關政策趨勢",
        "slideNo": sn,
        "slideTitle": s["title"],
        "module": s["module"],
        "tags": list(set(tags)),
        "content": clean_text,
        "url": f"courses/pv-grid-connection-policies.html#s{sn}"
    })

with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)
print(f"Updated data/search-index.json successfully! Total slides indexed: {len(search_data)}")
