# 光伏維運知識庫擴充標準作業程序 (Expansion SOP)

本知識庫採用無伺服器靜態架構，具備零維護成本、高加載效能與高度可擴展性。當維運團隊有新課程（例如：新進工程師訓練、儲能微電網維護、無人機紅外檢測等）需要納入時，請依照下列步驟進行標準化擴充。

---

## 一、新增課程簡報檔案

1. 在 `courses/` 目錄建立新的 HTML 檔案，命名規則為 `course-[主題識別碼].html`（例如 `course-bess-operation.html`）。
2. 版型結構可複製 `courses/pv-om-fundamentals.html` 作為標準模板。
3. 遵循**麥肯錫金字塔結構**：
   - 每頁以**行動結論（Action Title）**作為標題。
   - 左側包含三大標準區塊：
     - `📌 本章要解決的問題／核心論點`
     - `💡 1–3 個最值得記住的亮點`
     - `🎯 一句話總結`
   - 右側放置重置圖表（SVG / HTML Table）與原廠講義縮圖。
   - 在每頁 `<section class="slide-item">` 填寫講者備忘錄屬性：
     - `data-note-takeaway`: 本頁核心結論
     - `data-note-detail`: 實務數據與補充說明
     - `data-note-transition`: 下一步 / 轉場提示

---

## 二、登記至中央目錄 (`data/courses.json`)

在 `data/courses.json` 的 `courses` 陣列中新增一筆物件：

```json
{
  "id": "pv-bess-scada-alarms",
  "slug": "pv-bess-scada-alarms",
  "title": "PV-BESS 光儲案場 SCADA 異常告警與 ISA-18.2 降噪實戰",
  "subtitle": "符合 ISA-18.2 / IEC 62682 標準之告警洪水抑制",
  "instructor": "專業技術委員會",
  "date": "2026-11-15",
  "category": "advanced",
  "status": "ready",
  "badge": "光儲進階專題",
  "recordingDuration": "45 分鐘",
  "slidesCount": 16,
  "sourceHandoutPages": 24,
  "url": "courses/course-bess-operation.html",
  "coreThesis": "透過多 AI Agent 協同消除 70% 抖動假告警，將警報轉為閉環派工單。",
  "highlights": [
    "告警合理化矩陣：抖動告警死區時間與延遲抑制演算法。",
    "物理特徵關聯：雲層經過動態遮蔽與線間短路快速解耦。",
    "8D 閉環聯動：一級關鍵告警 15 分鐘內自動生成 D0 通知。"
  ],
  "oneSentenceTakeaway": "告警合理化是運維工程師擺脫警報疲勞、聚焦核心電氣缺陷的數位防線。"
}
```

---

## 三、更新全文檢索索引 (`data/search-index.json`)

在 `data/search-index.json` 中為該課程的每張投影片新增檢索條目：

```json
{
  "id": "bess-s1",
  "course": "pv-bess-scada-alarms",
  "courseTitle": "PV-BESS 光儲案場 SCADA 異常告警與 ISA-18.2 降噪實戰",
  "slideNo": 1,
  "title": "符合 ISA-18.2 工業標準之告警合理化體系",
  "category": "前瞻光儲微網",
  "tags": ["ISA-18.2", "告警洪水", "SCADA", "光儲微電網"],
  "content": "檢討案場告警洪水與抖動警報，透過延遲計時器與死區閾值抑制 70% 無效通知...",
  "anchor": "courses/course-bess-operation.html#s1"
}
```

---

## 四、發布至 GitHub Pages

在本地終端機執行：

```bash
git add .
git commit -m "feat(courses): add PV-BESS SCADA alarms training module"
git push origin main
```

推送後，GitHub Pages 會在 1~2 分鐘內自動完成靜態構建，新課程與檢索關鍵字即刻在線上知識庫生效！
