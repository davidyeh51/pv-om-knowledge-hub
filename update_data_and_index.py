# -*- coding: utf-8 -*-
import json
import os

courses_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\courses.json"
search_index_path = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\data\search-index.json"

# 1. Update courses.json
with open(courses_path, "r", encoding="utf-8") as f:
    courses_data = json.load(f)

# Update Course 2 in courses_data
course_2_meta = {
    "id": "pv-thermal-ir-inspection-20261027",
    "slug": "pv-thermal-ir-inspection",
    "title": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
    "subtitle": "麥肯錫顧問風格 10 分鐘精華導讀 ✕ 20 頁金字塔原理簡報 ✕ 熱影像失效分析",
    "instructor": "葉大衛 (David Yeh)",
    "date": "2026-10-27",
    "category": "safety",
    "status": "ready",
    "badge": "旗艦回訓核心課",
    "recordingDuration": "44 分鐘",
    "slidesCount": 20,
    "sourceHandoutPages": 20,
    "url": "courses/pv-thermal-ir-inspection.html",
    "coreThesis": "熱影像檢查是以熱力學溫差倒推電氣內阻與壓差異常的電氣聽診器，是捍衛電廠資產最前線的防禦利刃。",
    "highlights": [
        "遮陰放熱乘數效應：遮陰 3/4 焦耳熱暴增 243 倍，全遮片退化為絕緣體引發峰值集中加熱。",
        "集中式並聯反向逆灌：單片開路壓差誘發 20~23A 反向電流，在低照度陰天引爆連接器大火。",
        "三大工程防禦紅線：打破絕對溫度迷思（相對溫差 ≥0.5°C 即異常）、鋁框嚴禁鐵自攻螺絲、設備接地嚴禁共地台電 N 相。"
    ],
    "oneSentenceTakeaway": "打破絕對溫度迷思，以 0.5°C 相對溫差早期介入，落實接地獨立與開關上選，杜絕電弧火災。",
    "modules": [
        {
            "moduleNo": 1,
            "name": "遮陰熱效應原理與半導體物理特性",
            "slides": "01-04",
            "summary": "I²R 焦耳熱放大乘數（遮3/4飆243倍）、全遮絕緣化峰值發熱、半切分流反常溫升與二極體極限。"
        },
        {
            "moduleNo": 2,
            "name": "開路故障、電壓特徵與系統級隱患",
            "slides": "05-08",
            "summary": "整片遮陰啟動門檻、IEC 62446-3開路溫升2~7°C、單片開路電壓跌落2~13V與PR監控盲區。"
        },
        {
            "moduleNo": 3,
            "name": "反向電流危害、熔絲真諦與典型案場",
            "slides": "09-12",
            "summary": "低照度陰天20~23A反向充電引發火災、25A熔絲設計真諦、水庫白鷺鸶鳥糞與避雷針獨立串列隔離。"
        },
        {
            "moduleNo": 4,
            "name": "接頭工藝、電位差腐蝕與熱異常判定",
            "slides": "13-16",
            "summary": "MC4異廠混接3分鐘160°C融毀、毛細滲透氯化銅腐蝕、鐵鋁自攻螺絲2.3V超標、相對溫差0.5°C黃金法則與嚴禁共地N相。"
        },
        {
            "moduleNo": 5,
            "name": "並聯拓撲、保護元件演進與表前開關",
            "slides": "17-20",
            "summary": "健達巧克力三色反向充電擊穿IGBT、阻隔二極體到DC熔絲座演進、空拍4°~5°開口率與表前開關養豬場1500A選型。"
        }
    ]
}

# Replace or insert Course 2
courses_list = courses_data.get("courses", [])
replaced = False
for idx, c in enumerate(courses_list):
    if "thermal" in c.get("id", "") or "thermal" in c.get("slug", ""):
        courses_list[idx] = course_2_meta
        replaced = True
        break

if not replaced:
    courses_list.insert(1, course_2_meta)

courses_data["courses"] = courses_list

with open(courses_path, "w", encoding="utf-8") as f:
    json.dump(courses_data, f, ensure_ascii=False, indent=2)

print("Updated data/courses.json successfully!")

# 2. Update search-index.json
with open(search_index_path, "r", encoding="utf-8") as f:
    search_index = json.load(f)

# Keep course 1 slides and filter out old course 2 if any
search_index = [item for item in search_index if item.get("course") != "pv-thermal-ir-inspection"]

course_2_slides_index = [
    {
        "id": "pv-thermal-s1",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 1,
        "title": "太陽光電系統熱影像檢查與失效分析：從微觀發熱物理到宏觀電廠安全防線",
        "category": "模組總綱",
        "tags": ["熱影像", "失效分析", "乙級技術士", "回訓課程", "葉大衛", "進金生能源", "電氣安全"],
        "content": "熱影像檢查是以熱力學溫差倒推電氣內阻異常的電氣聽診器。涵蓋遮陰熱效應放大、二極體極限、開路溫升 2~7°C、反向電流 20~23A、MC4 異廠混接 160°C 融毀、鐵鋁自攻螺絲 2.3V 電位差腐蝕、相對溫差 0.5°C 判定及設備接地嚴禁共地 N 相。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s1"
    },
    {
        "id": "pv-thermal-s2",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 2,
        "title": "I²R 焦耳熱倍率乘數效應：遮陰 3/4 放熱飆升 243 倍，全遮絕緣化達到峰值加熱",
        "category": "遮陰發熱",
        "tags": ["I2R", "焦耳熱", "遮陰熱效應", "243倍", "9R", "絕緣體", "熱斑", "等效電阻"],
        "content": "遮陰 1/4 產生 9R 熱耗；遮陰 3/4 放熱飆升 243 倍 (12-3)^2 * 3R = 243R；全遮蔽狀態下電池片從半導體退化為高阻絕緣體，表面細線承載全部串聯大電流，達到峰值加熱，極易燒穿背板。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s2"
    },
    {
        "id": "pv-thermal-s3",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 3,
        "title": "半切組件反直覺熱分佈：下半部受遮受阻，大電流被迫全數湧向上半部背板集中發熱",
        "category": "半切特徵",
        "tags": ["半切組件", "反常溫升", "分流拓撲", "短邊朝下", "隱裂排查", "背板過熱"],
        "content": "半切組件下半部被小面積遮陰時，發熱點不在下半部反而集中在上半部！因上下兩半並聯，下部受阻後 7~8A 大電流湧向上半部分流導通；建議短邊朝下安裝以降低背板熱老化，遮擋下半部可排查上半部隱裂破片。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s3"
    },
    {
        "id": "pv-thermal-s4",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 4,
        "title": "短時救急與長時過熱：狹小接線盒灌膠環境下的熱積聚與二極體熔斷起弧風險",
        "category": "二極體極限",
        "tags": ["旁路二極體", "接線盒", "灌膠密閉", "熱積聚", "熱穿孔", "直流電弧", "火災蔓延"],
        "content": "旁路二極體為耗能元件，密閉灌膠空間狹小 + 晴天戶外高溫 + 長期導通焦耳熱三疊加，極易熱穿孔燒毀。二極體搭電短路後引燃接線盒塑料，拉出持續直流電弧；長時受遮必壞無疑，絕不可作為常規運行機制。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s4"
    },
    {
        "id": "pv-thermal-s5",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 5,
        "title": "二極體啟動嚴格門檻：必須遮蔽整片完整電池片方觸發，局部小面積遮陰落入保護盲區",
        "category": "啟動門檻",
        "tags": ["導通門檻", "局部遮陰", "保護盲區", "偏壓", "微小鳥糞", "竣工驗收", "接線盒偏熱"],
        "content": "1顆二極體跨接保護20~24片電池，必須完整遮蔽單片產生足夠反向偏壓（約0.7V）方能觸發導通；局部遮蔽1/4片或點狀鳥糞時二極體截止不動作，電池片持續承受全部串聯電流烘烤；竣工驗收無遮陰下二極體偏熱代表短路損壞。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s5"
    },
    {
        "id": "pv-thermal-s6",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 6,
        "title": "IEC 62446-3 國際標準：無功耗散能量原位轉熱，開路故障區域溫升 2～7°C",
        "category": "開路熱影像",
        "tags": ["IEC 62446-3", "開路故障", "溫升2~7度", "無功耗散", "輻照能量", "日照窗口", "熱圖譜"],
        "content": "依據 IEC 62446-3 標準，開路區域吸收的太陽輻射能量無法向外輸出，100% 在組件內部轉化為熱能，使故障區溫度比正常發電區高出 2～7°C；需在日照強度 >700 W/m² 時量測排查。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s6"
    },
    {
        "id": "pv-thermal-s7",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 7,
        "title": "開路電壓斷崖式跌落：單片端電壓驟降至 2～13V，實務無需繁瑣溫度修正即可確診",
        "category": "開路電壓",
        "tags": ["開路電壓", "2~13V", "8~10V", "萬用電表", "負溫度係數", "電氣量測", "快速確診"],
        "content": "正常 600W 組件電壓約 39V，內部 1/3 子回路開路時端電壓驟降至 2～13V（典型實測 8~10V）；溫度升高微幅再降電壓；實務維運無需複雜溫度係數修正，只要電壓大跌且伴隨紅外溫升 2~7°C 即可確診。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s7"
    },
    {
        "id": "pv-thermal-s8",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 8,
        "title": "開路隱性系統風險：單片 200W 損耗淹沒於 PR 誤差，集中式逆變器並聯誘發反向電流燒毀",
        "category": "系統級風險",
        "tags": ["PR誤差", "監控盲區", "集中式逆變器", "反向電流", "MPPT燒毀", "端子融毀", "100MW暗場"],
        "content": "單片 600W 模組開路 1/3 僅損失 200W，在 10kW 串列僅少 0.2kW，完全淹沒在 PR 誤差範圍內；但集中式逆變器下多串並聯，故障串列電壓偏低誘發巨大反向電流逆灌，燒毀 MPPT 模組、端子與保險絲。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s8"
    },
    {
        "id": "pv-thermal-s9",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 9,
        "title": "反向電流致命機制：低照度陰天逆向灌流高發，20～23A 強大焦耳熱在接頭引爆大火",
        "category": "反向電流",
        "tags": ["反向電流", "低照度陰天", "20~23A", "焦耳熱起火", "電位差逆灌", "接頭火災"],
        "content": "並聯回路中高電壓串列向低電壓串列逆向充電；低照度陰天變流器做功能力下降，反向電流發生率最高；當反向電流達 20～23A 時，在接頭接觸電阻處依 I²R 瘋狂放熱，瞬時點燃外殼引爆暗場火災。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s9"
    },
    {
        "id": "pv-thermal-s10",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 10,
        "title": "25A 熔絲設計真諦：絕非防禦順向工作電流，而是反向電流超標時的生死熔斷閥",
        "category": "熔絲真諦",
        "tags": ["25A保險絲", "OCPD", "順向13A", "反向超標", "受限電流源", "熔斷隔離", "嚴禁加大"],
        "content": "光伏組件順向工作電流僅 10~13A，永遠不可能達到 25A；配置 25A 熔絲的唯一目的，是當外界多組並聯逆灌電流超過 25A 時毫秒級熔斷隔離；保險絲常燒斷是電壓失配求救訊號，嚴禁私自換大規格。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s10"
    },
    {
        "id": "pv-thermal-s11",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 11,
        "title": "白鷺鸶排泄物整片覆蓋連鎖災難：長期遮陰燒毀二極體，更換組件重在防火而非微小度數",
        "category": "鳥糞案例",
        "tags": ["白鷺鸶", "鳥糞覆蓋", "水庫案場", "二極體燒毀", "接線盒起弧", "防火決策", "度數vs安全"],
        "content": "水庫水面案場白鷺鸶盤踞糞便整片覆蓋，長期持續遮陰導致接線盒二極體批量熱融損毀，兩片模組全換；維運更換的核心不是挽回發電度數，而是避免接線盒燒穿拉出直流電弧引燃下方浮台與可燃物。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s11"
    },
    {
        "id": "pv-thermal-s12",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 12,
        "title": "避雷針陰影獨立串列隔離：專列專機精準處置，防範全場變流器發電效率腰斬慘劇",
        "category": "避雷針設計",
        "tags": ["避雷針遮陰", "獨立串列", "發電腰斬", "橫向跨列", "專機專用", "電氣隔離", "優化設計"],
        "content": "避雷針陰影每日掃射使某案場 3 年後變流器讀取電壓腰斬減半；嚴禁橫向跨列串聯；顧問級優化解法：將避雷針陰影覆蓋區域單獨劃分為 1~2 個獨立串列接入專用逆變器或 MPPT，隔離故障擴散。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s12"
    },
    {
        "id": "pv-thermal-s13",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 13,
        "title": "MC4 連接器異廠混接 3 分鐘飆至 160°C，隨手施工誘發水氣滲透與海邊氯化銅腐蝕",
        "category": "接頭失效",
        "tags": ["MC4連接器", "異廠混接", "160度融毀", "滲透現象", "扭力規範", "海邊鹽霧", "氯化銅"],
        "content": "同廠接頭通電 5 分鐘 135°C；異廠混接僅 3 分鐘飆至 160°C，2 分鐘後融化變形；手擰未達 IP65 扭力誘發毛細滲透現象，水氣被負壓吸入；海邊氯離子置換氧化銅生成氯化銅，接觸電阻暴增拉弧起火。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s13"
    },
    {
        "id": "pv-thermal-s14",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 14,
        "title": "電位差腐蝕致命傷：鋁框嚴禁鐵自攻螺絲，電位差達 2.3V 嚴重超標導致鋁材溶解大洞",
        "category": "電位差腐蝕",
        "tags": ["電位差腐蝕", "自攻螺絲", "鋁框穿孔", "活性金屬", "2.3V超標", "NaCl電解質", "接地規範"],
        "content": "鋁活性高釋放電子溶解（Al -> Al3+ + 3e-），鐵自攻螺絲當接地螺絲使鋁框被吃出大洞；標準要求金屬電位差在 2V 以內（建議 1V），鐵鋁電位差高達 2.3V 嚴重違規；海邊強電解質倍速加速腐蝕且原廠拒保。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s14"
    },
    {
        "id": "pv-thermal-s15",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 15,
        "title": "打破絕對溫度迷思：同工況下相對溫差高出 0.5°C 即屬異常，接觸電阻偏大必須立即處置",
        "category": "熱異常法則",
        "tags": ["熱異常判定", "相對溫差", "0.5度即異常", "電氣一致性", "打破絕對溫度", "早期介入", "草料火災"],
        "content": "破除高出 10°C 或 30°C 才換的盲點！電氣一致性原理：相同工況下內阻應一致，只要某接頭比周邊高出 0.5°C 即判定為接觸電阻異常；百元接頭早期更換，杜絕引燃牧草或乾草的全場巨額賠償。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s15"
    },
    {
        "id": "pv-thermal-s16",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 16,
        "title": "設備接地嚴禁與台電 N 相共地：防範電網故障電流反竄鋼梁，電倒全場畜禽血淚案例",
        "category": "接地規範",
        "tags": ["設備接地", "台電N相接地", "嚴禁共地", "5歐姆", "畜禽舍漏電", "種豬觸電", "鋼梁帶電"],
        "content": "設備接地防漏電、支撐變流器跳脫保護（<=5歐姆獨立打設）；N相接地保台電分擔電網故障電流；共地線導致電網故障電流順著鋁框與鋼梁反竄入建築，未鋪地網之畜禽舍整場帶電，母豬與種豬全被電倒。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s16"
    },
    {
        "id": "pv-thermal-s17",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 17,
        "title": "健達巧克力三色案場實錄：嚴禁混接不同串數與方位，IGBT 後端反向灌流頻繁擊穿逆變器",
        "category": "多串並聯拓撲",
        "tags": ["健達巧克力", "三色熱圖", "59度/54度/65度", "18片vs15片", "IGBT燒毀", "不同朝向", "直流母線"],
        "content": "未併網電廠空拍呈現 59°C、54°C、65°C 三種顏色，18片高壓串對15片（3片短路）低壓串劇烈逆灌；同一逆變器嚴禁混接不同串數或不同朝向；變流器內部在 IGBT 後端並聯，反向電流從後端灌入擊穿 IGBT 模組。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s17"
    },
    {
        "id": "pv-thermal-s18",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 18,
        "title": "保護元件演進史：從 IP65 密閉發熱的阻隔二極體，到免動火秒級抽換的 DC 熔絲座",
        "category": "保護元件演進",
        "tags": ["阻隔二極體", "DC熔絲座", "IP65密閉", "動火解焊", "秒級抽換", "匯流箱", "元件演進"],
        "content": "早期阻隔二極體為發熱耗能件，放入 IP65 密閉箱原理衝突且更換需動火解焊；現代全數轉向 DC 熔絲座，免動火秒級抽換；依規範 1~2 串小型逆變器可免設熔絲，多並聯集中型精準配置 25A 熔絲。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s18"
    },
    {
        "id": "pv-thermal-s19",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 19,
        "title": "空拍熱影像開口率 4°~5° 幾何控制，左右兩側零星點精準鎖定接線盒引線拉扯脫焊",
        "category": "空拍參數",
        "tags": ["無人機巡檢", "開口率4~5度", "單像素覆蓋", "接線盒拉扯", "兩側熱斑", "直流箱價值", "200MW案場"],
        "content": "空拍熱像儀開口率約 4°~5°，飛行高度需確保單模組 >=1 個像素；左右兩側零星熱點 100% 為施工拉扯引線焊點脫落；200MW 案場無直流箱人工檢測需 6 個月 2000 萬，空拍排查開路/短路/二極體是唯一經濟方案。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s19"
    },
    {
        "id": "pv-thermal-s20",
        "course": "pv-thermal-ir-inspection",
        "courseTitle": "太陽光電設置乙級技術士回訓課程——太陽光電系統熱影像檢查與失效分析",
        "slideNo": 20,
        "title": "表前開關耐電流必須嚴格上選：養豬場排糞溝直選 1500A 規格，抵禦氨氣腐蝕電弧爆燃",
        "category": "表前開關選型",
        "tags": ["表前開關", "耐電流上選", "嚴禁下修", "800A選1000A", "養豬場1500A", "氨氣腐蝕", "電弧放電"],
        "content": "表前開關為純開關無過載跳脫功能，耐電流容量只能上選不能下修（算800A上選1000A）；養豬場排糞溝正上方氨氣常年腐蝕銅排，直選 1500A 超大規格方能確保全生命週期不炭化拉弧燒穿鋼板。",
        "anchor": "courses/pv-thermal-ir-inspection.html#s20"
    }
]

search_index.extend(course_2_slides_index)

with open(search_index_path, "w", encoding="utf-8") as f:
    json.dump(search_index, f, ensure_ascii=False, indent=2)

print(f"Updated data/search-index.json successfully with total {len(search_index)} items!")
