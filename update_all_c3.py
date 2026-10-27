# -*- coding: utf-8 -*-
import json
import os

courses_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\courses.json"
search_index_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\search-index.json"

# 1. Update courses.json
with open(courses_path, "r", encoding="utf-8") as f:
    courses_data = json.load(f)

course_3_meta = {
    "id": "bess-technologies-applications-20261027",
    "slug": "bess-technologies-applications",
    "title": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
    "subtitle": "麥肯錫顧問風格 10 分鐘精華導讀 ✕ 20 頁金字塔原理簡報 ✕ 能源管理與表後儲能",
    "instructor": "慧能 張經理 (特聘業界專家) ＆ 葉大衛",
    "date": "2026-10-27",
    "category": "advanced",
    "status": "ready",
    "badge": "旗艦回訓核心課",
    "recordingDuration": "44 分鐘",
    "slidesCount": 20,
    "sourceHandoutPages": 20,
    "url": "courses/bess-technologies-applications.html",
    "coreThesis": "儲能是前鋒，能管是中樞；以數據診斷用電浪費，以儲能放電免除限電，是工廠電費最佳化的終極解法。",
    "highlights": [
        "批次電價價差 9.29 元：製造業尖離峰套利空間雄厚，扣除 15% 損耗儲能櫃 5.22 年全本金收回。",
        "台電需量 2880 次規則：每月 2880 次 15 分鐘平均需量取單次最高值，儲能放電無感削峰免除超約重罰。",
        "四大實操管理案例：高低壓雙表揪出變壓器損耗 12.6%（年漏40萬）、空壓機共振改管關一台（省40萬降50kW）、自強號讓莒光號錯峰（省100萬基本費）、生鏽輸送帶狂吃 13 萬度電。"
    ],
    "oneSentenceTakeaway": "不用換設備、靠管理節能，結合表後儲能充放電套利與需量反應，創造每年百萬現金流純利。",
    "modules": [
        {
            "moduleNo": 1,
            "name": "管理型節能理念與台灣電力政策局勢",
            "slides": "01-04",
            "summary": "台塑14年節能心法、AIDC機房引爆備用容量缺口、批次電價價差9.29元與用電大戶儲能履約。"
        },
        {
            "moduleNo": 2,
            "name": "電費單科學診斷與台電需量規則",
            "slides": "05-08",
            "summary": "能源管理法800kW申報、電費單六大維度（離峰佔比36%異常）、台電2880次抓最高峰與夏月自我同比省11萬。"
        },
        {
            "moduleNo": 3,
            "name": "表後儲能七大效益與操作模式",
            "slides": "09-12",
            "summary": "表後儲能免拉閘限電、夏月單充單放/非夏月雙充雙放、需量反應每度補貼10元無罰則與關鍵冷凍機備援UPS。"
        },
        {
            "moduleNo": 4,
            "name": "能源可視化落地與電表配置架構",
            "slides": "13-16",
            "summary": "總盤/高壓分盤/低壓總盤三層電表（拒絕800顆）、季度數據覆盤追究到人、自強號讓莒光號避峰省百萬與ESCO 8:2商模。"
        },
        {
            "moduleNo": 5,
            "name": "一體機參數測算與四大實操案例",
            "slides": "17-20",
            "summary": "125kW/261kWh一體機占地如公廁5.22年回本、變壓器損耗12.6%、空壓機共振改管、生鏽輸送帶與創儲節四位一體。"
        }
    ]
}

# Update or insert into courses list
courses_list = courses_data.get("courses", [])
c3_exists = False
for idx, c in enumerate(courses_list):
    if "bess" in c.get("id", "") or "bess" in c.get("slug", "") or "储能" in c.get("title", "") or "儲能" in c.get("title", ""):
        courses_list[idx] = course_3_meta
        c3_exists = True
        break

if not c3_exists:
    courses_list.insert(2, course_3_meta)

courses_data["courses"] = courses_list

with open(courses_path, "w", encoding="utf-8") as f:
    json.dump(courses_data, f, ensure_ascii=False, indent=2)

print("Updated data/courses.json successfully with Course 3!")

# 2. Update search-index.json
with open(search_index_path, "r", encoding="utf-8") as f:
    search_index = json.load(f)

# Filter out old course 3 if any
search_index = [item for item in search_index if item.get("course") != "bess-technologies-applications"]

course_3_slides_index = [
    {
        "id": "pv-bess-s1",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 1,
        "title": "儲能系統技術與應用現況：能源管理 (EMS) ✕ 表後儲能 (BTM) 的價值最大化",
        "category": "模組總綱",
        "tags": ["表後儲能", "BTM", "能源管理", "EMS", "乙級技術士", "回訓課程", "慧能張經理", "台塑節能"],
        "content": "儲能是前鋒，能管是中樞；以數據診斷用電浪費，以儲能放電免除限電。台塑14年管理型節能哲學，結合表後儲能四大價值：電價套利、防超約需量平抑、重要設備備援、台電電力交易獲取補貼。",
        "anchor": "courses/bess-technologies-applications.html#s1"
    },
    {
        "id": "pv-bess-s2",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 2,
        "title": "AIDC 機房引爆用電缺口：台電推動「藏電於民」，民間分散式儲能成為電網解方",
        "category": "政策背景",
        "tags": ["藏電於民", "分散式儲能", "AIDC", "備用容量", "電力交易", "電網韌性", "免建電廠"],
        "content": "AIDC 高耗能機房引爆用電缺口，新建電廠耗資數千億且環評漫長；台電推動藏電於民，鼓勵企業自建表後儲能就地削峰填谷，平時充低放高自給自足，緊急時接受台電調度領取每度10元高額補貼。",
        "anchor": "courses/bess-technologies-applications.html#s2"
    },
    {
        "id": "pv-bess-s3",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 3,
        "title": "三段式價差 6.86 元、批次電價飆至 9.29 元：表後儲能充放電套利空間巨大",
        "category": "電價套利",
        "tags": ["批次電價", "9.29元", "三段式電價", "6.86元", "夏月套利", "尖離峰價差", "金融級資產"],
        "content": "台電電價持續調漲，三段式夏月尖離峰價差每度6.86元，工業區專用批次電價尖離峰價差飆達9.29元！離峰充電尖峰放電，使表後儲能成為穩定產生強勁現金流的金融級能源資產，回收期縮短至5年內。",
        "anchor": "courses/bess-technologies-applications.html#s3"
    },
    {
        "id": "pv-bess-s4",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 4,
        "title": "綠電憑證飆漲至 5.8 元且斷貨：表後儲能成用電大戶履行義務量的唯一可行解",
        "category": "用電大戶",
        "tags": ["用電大戶", "5000kW", "800kW", "綠電憑證5.8元", "自建光電無空間", "表後儲能履約", "地方條例"],
        "content": "綠電憑證單價飆至5.6~5.8元且斷貨，自建光電受限屋頂空間；台北維持4000kW，台中台南下殺至800kW；表後儲能占地僅1.3m²，是買不到綠電、建不了光電的企業履行法定義務兼賺套利的最優解。",
        "anchor": "courses/bess-technologies-applications.html#s4"
    },
    {
        "id": "pv-bess-s5",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 5,
        "title": "800kW 以上用戶限期申報五年計畫：能源可視化是通過合規稽核的硬性前提",
        "category": "法規合規",
        "tags": ["能源管理法", "800kW", "五年計畫", "能源可視化", "法定死線", "公文通知", "客觀數據"],
        "content": "能源管理法強制要求800kW以上重點用電戶於後年3月31日前提交5年節能計畫書，核心硬指標為能源可視化；將公文合規壓力轉化為工廠用電大體檢契機，藉由儀表裝設直擊長年未察覺的電費黑洞。",
        "anchor": "courses/bess-technologies-applications.html#s5"
    },
    {
        "id": "pv-bess-s6",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 6,
        "title": "電費單六大維度秒判工廠健康度：離峰佔比達 36% 即屬異常，基本電費超標透露管理失控",
        "category": "電費單診斷",
        "tags": ["電費單診斷", "六大維度", "離峰佔比36%", "基本電費15%", "契約容量", "負載率", "隱形浪費"],
        "content": "一年12張電費單診斷六大維度：契約容量、最高需量、尖離峰佔比、負載率、基本電費佔比、平均電價；非24小時工廠離峰佔比達36%即代表嚴重浪費；基本電費超過15%代表契約容量虛高或管理失控。",
        "anchor": "courses/bess-technologies-applications.html#s6"
    },
    {
        "id": "pv-bess-s7",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 7,
        "title": "台電最高需量規則解密：每月 2880 次取單次最高值，2879 次表現良好單次超標即重罰",
        "category": "台電需量規則",
        "tags": ["台電需量", "2880次", "15分鐘平均", "單次最高值", "超約附加費", "時間戳排查", "撞峰衝高"],
        "content": "台電一天採集96次15分鐘平均需量，全月共2880筆，只取單次最高的那1筆當計費需量！哪怕前2879次都控制在800kW，只要有一次因疏忽衝到1200kW，當月即判定超約200kW重罰；必須調取15分鐘數據精確鎖定時間戳排查。",
        "anchor": "courses/bess-technologies-applications.html#s7"
    },
    {
        "id": "pv-bess-s8",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 8,
        "title": "平均單價自我同比法：同夏月不同月份差 11 萬，數據反推設備開機時序與行為異常",
        "category": "單價同比",
        "tags": ["平均單價", "自我同比", "夏月6月vs9月", "差0.11元省11萬", "台電牌價相同", "開機時序", "待機耗電"],
        "content": "拒絕跨界攀比台積電1.9元/度，專注自家同夏月自我同比；牌價完全相同下，某廠6月3.35元與9月3.24元差0.11元即差出11萬流動電費；產能相近單價偏高代表尖峰集中或無人時段未關機浪費。",
        "anchor": "courses/bess-technologies-applications.html#s8"
    },
    {
        "id": "pv-bess-s9",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 9,
        "title": "表後儲能七大核心效益：徹底終結拉閘限電痛苦，免關設備放電頂峰平抑需量",
        "category": "儲能效益",
        "tags": ["表後儲能", "七大效益", "免拉閘限電", "放電平抑需量", "超約附加費歸零", "削峰填谷", "電力交易"],
        "content": "過去防超約用需量控制器強行關空調引發抱怨；儲能一放電設備全開需量自動下降！七大效益：尖離峰電價套利、契約容量優化下調、重要設備備援、台電電力交易、需量反應措施、用電大戶履約與減碳形象。",
        "anchor": "courses/bess-technologies-applications.html#s9"
    },
    {
        "id": "pv-bess-s10",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 10,
        "title": "夏月單充單放、非夏月雙充雙放：週末全天休眠調養，精細化排程極大化套利兼顧壽命",
        "category": "充放電排程",
        "tags": ["充放電排程", "夏月單充單放", "非夏月雙充雙放", "午間離峰13-14點", "週日休眠", "電芯壽命", "循環折舊"],
        "content": "夏月夜間0-6點充低、日間10-16點放高賺取6.86~9.29元差價；非夏月利用中午13-14點離峰二次充電、傍晚18-20點二次放電實現一日兩次套利！週日全天皆為離峰電價無價差，排定儲能休眠停機延長10年壽命。",
        "anchor": "courses/bess-technologies-applications.html#s10"
    },
    {
        "id": "pv-bess-s11",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 11,
        "title": "需量反應零風險獲利：日選型固定放電最穩健，彈性反應每度補貼 10 元無罰則",
        "category": "需量反應",
        "tags": ["需量反應", "日選型", "彈性反應型", "每度補貼10元", "無罰則", "高裝檢比喻", "備用發電機"],
        "content": "需量反應如部隊高裝檢，不問手段只看結果，可用儲能放電、發電機或關機，需量降下即可領錢！日選型5~10月每日18-20點固定放電最穩健；彈性反應配合緊急調度每度補貼高達10元，未配合完全不罰款。",
        "anchor": "courses/bess-technologies-applications.html#s11"
    },
    {
        "id": "pv-bess-s12",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 12,
        "title": "儲能絕非全廠不斷電：切換延遲 1 秒必須搭配 UPS，聚焦咽喉核心設備防止食材報廢",
        "category": "備援配置",
        "tags": ["備援電源", "全廠備援陷阱", "冷凍機保護", "VCS切換1秒", "在線式UPS", "4ms無縫", "食材報廢"],
        "content": "為整廠做不斷電備援成本高如電廠完全不可行；某食品廠專為急速冷凍機配置儲能備援防止百萬食材腐爛；儲能VCS切換有1秒內中斷，馬達水泵不受影響，但電腦PLC控制系統必須串接在線式UPS (4ms) 防死機。",
        "anchor": "courses/bess-technologies-applications.html#s12"
    },
    {
        "id": "pv-bess-s13",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 13,
        "title": "電表分層安裝黃金三原則：總盤、高壓分盤、低壓總盤三層即足，嚴禁全廠浮濫裝 800 顆",
        "category": "電表配置",
        "tags": ["電表分層", "三層架構", "總盤", "高壓分盤", "低壓總盤", "拒絕800顆", "重點大心臟設備"],
        "content": "某工廠盲目裝設800顆電表導致資訊過載淪為垃圾；極簡三層骨架：總盤（全廠總量）、高壓分盤（車間配電）、低壓總盤（變壓器損耗）；僅對空壓機、冰水主機等佔全廠70%用電之重點設備單獨裝表，20顆表即掌大局。",
        "anchor": "courses/bess-technologies-applications.html#s13"
    },
    {
        "id": "pv-bess-s14",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 14,
        "title": "季度電力數據覆盤機制：顧問拋異常曲線、現場講真實原因，管路與壓力缺陷全面現形",
        "category": "數據覆盤",
        "tags": ["季度覆盤", "顧問拋曲線", "現場講原因", "管路漏氣", "空壓機震盪", "責任歸屬", "閉環管理"],
        "content": "每季度召開電力覆盤會議，能管顧問從系統拋出異常波形，點名設備現場負責人覆盤；透過高頻震盪或無載耗電揪出管路漏氣、閥門堵塞或壓力設定過高等缺陷；客觀15分鐘曲線終結跨部門推諉，將數據變現。",
        "anchor": "courses/bess-technologies-applications.html#s14"
    },
    {
        "id": "pv-bess-s15",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 15,
        "title": "自強號讓莒光號避峰哲學：核心製程啟動時關停輔機，錯峰 20 分鐘契約容量直降 500kW",
        "category": "錯峰避峰",
        "tags": ["自強號讓莒光號", "火車避峰", "錯峰啟動", "2700kW降至2000kW", "降約500kW", "省100萬基本費", "開機時序"],
        "content": "自強號（製程核心設備）通過時，莒光號（抽水泵、空調輔機）在側線暫停！某廠3台高耗能設備早上8點同時啟動衝破2700kW，改為錯開20分鐘啟動峰值降至2000kW，契約容量下調500kW，每年光基本電費省100萬元純利！",
        "anchor": "courses/bess-technologies-applications.html#s15"
    },
    {
        "id": "pv-bess-s16",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 16,
        "title": "ESCO 8:2 利潤分成商模：零資本支出改造，以節省電費分期償付實現零風險共贏",
        "category": "ESCO商模",
        "tags": ["ESCO", "節能績效分享", "8:2分成", "零資本支出", "Zero CapEx", "三年約滿設備贈與", "Baseline基線"],
        "content": "台塑時期驗證之ESCO商模：節能服務商全額出資裝設電表與能管，工廠零前期資本支出；省下電費淨額由雙方按8:2拆分（服務商8成、業主2成，簽約3年），期滿設備無償歸業主；以節省電費支付改造成本零風險推動轉型。",
        "anchor": "courses/bess-technologies-applications.html#s16"
    },
    {
        "id": "pv-bess-s17",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 17,
        "title": "標準一體機 125kW / 261kWh 占地如公廁：扣除 15% 損耗年賺 140 萬，5.22 年全本收回",
        "category": "一體機參數與ROI",
        "tags": ["一體機儲能櫃", "125kW/261kWh", "占地1.3m²", "扣除15%損耗", "年賺140萬", "總價750萬", "5.22年回本"],
        "content": "單台一體機尺寸僅1.3m×1.3m×2.35m占地如小型公廁；雙櫃額定250kW/522kWh，扣除15%充放電損耗按440kWh保守測算；年綜合收益達140萬元（套利+降約+需量反應），總建置成本約750萬，5.22年靜態全本回收！",
        "anchor": "courses/bess-technologies-applications.html#s17"
    },
    {
        "id": "pv-bess-s18",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 18,
        "title": "高低壓雙表揪出變壓器損耗 12.6%：合理值僅 3%，每月多耗萬度電、年蒸發 40 萬電費",
        "category": "案例一：變壓器損耗",
        "tags": ["變壓器損耗", "高低壓雙表", "損耗率12.6%", "正常3%", "月損11262度", "年漏40萬", "換油保養"],
        "content": "高壓進線減低壓出線差額即為變壓器損耗；正常損耗率應在3%以下，某廠實測高達12.6%，每月多損耗11,262度電，年蒸發40萬電費！緊急安排停機換油保養或汰換老舊變壓器，投資數萬元1年全額回本。",
        "anchor": "courses/bess-technologies-applications.html#s18"
    },
    {
        "id": "pv-bess-s19",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 19,
        "title": "兩台空壓機管路共振互推：花數千元改管關閉一台，年省 40 萬電費並下調 50kW 契約",
        "category": "案例二：空壓機改管",
        "tags": ["空壓機改管", "氣流對沖互推", "高頻鋸齒震盪", "關閉一台", "年省40萬", "調降50kW契約", "管路優化"],
        "content": "兩台空壓機出氣主管對沖無緩衝罐，在高頻打氣與卸載間劇烈震盪互相推擠打內戰；花數千元改管消除干涉後，僅需開啟一台即可滿足全產線風壓！年省流動電費40萬，額外下調50kW契約容量，免去200萬添購新機費用。",
        "anchor": "courses/bess-technologies-applications.html#s19"
    },
    {
        "id": "pv-bess-s20",
        "course": "bess-technologies-applications",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——儲能系統技術與應用現況",
        "slideNo": 20,
        "title": "生鏽輸送帶多吃 13 萬度電：創能 (PV) ✕ 儲能 (BTM) ✕ 節能 (EMS) 構築企業綠能護城河",
        "category": "案例三與創儲節整合",
        "tags": ["輸送帶生鏽", "定速馬達超額20kW", "年耗13萬度", "預防保養", "創能光電", "表後儲能", "能管節能", "進金生能源"],
        "content": "定速輸送帶鐵鏈生鏽摩擦大增，馬達超額輸出20kW年多吃13萬度電，現場毫無察覺；能管曲線賦能預防保養防非預期停機；進金生整合屋頂太陽能創能、表後儲能削峰填谷、能管數據體檢與綠電採購，構築企業綠能護城河。",
        "anchor": "courses/bess-technologies-applications.html#s20"
    }
]

search_index.extend(course_3_slides_index)

with open(search_index_path, "w", encoding="utf-8") as f:
    json.dump(search_index, f, ensure_ascii=False, indent=2)

print(f"Updated data/search-index.json successfully! Total index count: {len(search_index)} slides across 3 courses.")
