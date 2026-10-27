# -*- coding: utf-8 -*-
import os

out_dir = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\courses"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "pv-grid-connection-policies.html")

slides_data = [
    {
        "slideNo": 1,
        "module": "MODULE 1 ｜ 併網程序與時效控管",
        "ref": "講義對照 P.01 ｜ 錄音 00:00~02:47",
        "title": "光電併網六大核心階段：從併審規劃到電費結算，掌握電網責任分界點與時限紅線",
        "question": "太陽光電從土地籌設到正式售電需跨越哪些法定關卡？台電與政府主管機關的審查分工與邊界在哪裡？",
        "highlights": [
            "<strong>併網六大標準階段：</strong>併聯審查 ➔ 同意備案 ➔ 簽訂購售電契約 ➔ 案場施工 ➔ 併聯試運轉送電 ➔ 取得設備登記正式售電。",
            "<strong>兩大審查維度解耦：</strong>前兩階段屬台電與地方政府之籌設規劃許可；後四階段為實體工程施工、電網驗電與正式運轉登記。",
            "<strong>電費計量起算基石：</strong>完成現場試運轉並裝表掛表後，台電核發「併聯完成函」，自設備登記生效日起按月定期結算電費。"
        ],
        "takeaway": "併網六大階段是光電資產變現的法定生命週期；嚴控台電與主管機關公文節點，是確保投資如期回收的前提。",
        "visualTitle": "太陽光電建置與台電併網六大核心階段全流程圖",
        "visualType": "grid_six_stages",
        "thumbImg": "../assets/images/slides/slide_01.jpg",
        "thumbCaption": "講義 P.01：太陽光電發電設備併網作業整體流程圖",
        "thumbLabel": "P.01 併網六大流程",
        "noteTakeaway": "台電配電處吳家進課長開講：光電案場從無到有，必須依序通過台電電網容量審查與地方政府同意備案，才能進場施工。",
        "noteDetail": "許多工程師誤以為施工完成就能立刻領電費；實際上必須通過併聯試運轉、取得台電『併聯完成函』，並向主管機關取得設備登記，電費才能正式起算。",
        "noteTransition": "在六大階段中，哪兩個時間節點最容易超期導致案場廢案？請看第二頁關鍵時效節點分析。"
    },
    {
        "slideNo": 2,
        "module": "MODULE 1 ｜ 關鍵時效節點紅線",
        "ref": "講義對照 P.02 ｜ 錄音 02:47~04:23",
        "title": "時效違規即廢案：取得同意備案 2 個月內啟動簽約、簽約完成 1 年內必須取得設備登記",
        "question": "為什麼常有業者因工程延誤面臨躉購資格撤銷？設備管理辦法明定的兩大「剛性時效紅線」是什麼？",
        "highlights": [
            "<strong>備案後 2 個月內啟動簽約：</strong>取得地方政府同意備案後，必須在 2 個月內向台電申請辦理簽約（指啟動簽約與細部協商，非完成簽約）。",
            "<strong>簽約後 1 年內取得設備登記：</strong>管理辦法明定自簽約日起算 1 年內必須完工、驗電並取得設備登記，逾期同意備案失效！",
            "<strong>超期補件之連鎖代價：</strong>超期未完工將喪失原核定之躉購費率，必須重新補辦備案並適用新年度較低費率，造成數百萬收益損失。"
        ],
        "takeaway": "「2 個月啟動簽約、1 年內取得登記」是不可逾越的法定紅線；工程進度必須倒排時程，嚴防超期廢案。",
        "visualTitle": "光電併網兩大關鍵時效倒數紅線與超期風險示意圖",
        "visualType": "timeline_deadlines",
        "thumbImg": "../assets/images/slides/slide_02.jpg",
        "thumbCaption": "講義 P.02：再生能源發電設備設置管理辦法時效規範",
        "thumbLabel": "P.02 關鍵時效管制",
        "noteTakeaway": "吳課長特別提醒：拿到同意備案後 2 個月內就要找台電營業課簽約；簽完約只有 1 年時間蓋好並拿到設備登記。",
        "noteDetail": "實務上很多案場因為包商施工拖延，超過 1 年期限才發現備案失效，被台電退件要求重跑程序，甚至原本高躉購費率直接跌到新年度費率，血本無歸。",
        "noteTransition": "向台電申請時，台電內部究竟依循哪六類程序進行把關？請看第三頁台電側六大細分審查。"
    },
    {
        "slideNo": 3,
        "module": "MODULE 1 ｜ 台電六大細分程序",
        "ref": "講義對照 P.03 ｜ 錄音 04:23~09:13",
        "title": "台電側六類審查全解析：配電級審查初協合併辦理，細部協商聚焦交流側保護協調",
        "question": "配電級與輸電級審查權責如何劃分？台電圖面審查為何「只查責任分界點交流側，不介入直流內部」？",
        "highlights": [
            "<strong>配電級與輸電級分工：</strong>配電級由各區營業處檢驗課/設計課承辦；輸電級（高壓/特高壓大案場）由輸變電工程處統籌辦理。",
            "<strong>併審與初協二合一：</strong>配電級將「容量審查（饋線容量與衝擊）」與「初步協商（決定責任分界點）」合併同步審查，大幅縮短公文時效。",
            "<strong>細部協商（圖審）界線：</strong>依能源署協調原則，台電僅嚴格核查責任分界點交流側保護裝置（50/51/27/59），案場內部設備由業者自負工藝責任。"
        ],
        "takeaway": "台電細部協商本質是防禦電網跳脫；掌握交流保護開關配置與分界點規範，即可確保一次圖審過關。",
        "visualTitle": "台電六大細分審查權責矩陣 ✕ 責任分界點防禦架構",
        "visualType": "taipower_six_steps",
        "thumbImg": "../assets/images/slides/slide_03.jpg",
        "thumbCaption": "講義 P.03：台電併聯審查、細部協商與保護協調圖說",
        "thumbLabel": "P.03 台電六類程序",
        "noteTakeaway": "配電級案場由區處辦理，審查容量跟決定接點會一起做；細部協商就是大家常說的圖面審查。",
        "noteDetail": "台電不會去管你內部變流器擺哪裡、直流接頭怎麼串，台電唯一在乎的是責任分界點的交流保護！保護電驛整定要做好，案場短路不能跳掉台電主開關連累周邊用戶。",
        "noteTransition": "圖審通過並施工完竣後，如何順利送電並掛表計量？請看第四頁併聯試運轉與電費結算機制。"
    },
    {
        "slideNo": 4,
        "module": "MODULE 1 ｜ 試運轉送電與裝表",
        "ref": "講義對照 P.04 ｜ 錄音 09:13~12:35",
        "title": "試運轉報竣、檢驗送電與裝表計量：取得「併聯完成函」即刻起算躉售電費",
        "question": "案場完工報竣後，台電檢驗人員到場核驗哪些項目？「前送電」與「正式轉售」之間電量如何結算？",
        "highlights": [
            "<strong>報竣與外線配合：</strong>業者案場施工完畢向台電報竣；若涉及台電擴線，需等待台電外線工程施作完成至責任分界點。",
            "<strong>檢驗送電與裝表：</strong>區處檢驗班長到場核驗保護開關、相序與絕緣阻抗，無誤後進行裝表掛表，俗稱「併聯試運轉/前送電」。",
            "<strong>電量回溯一併結算：</strong>自裝表送電日起電表即開始累計度數；待取得主管機關設備登記正式轉售時，前送電期間電費一併全額結清補發。"
        ],
        "takeaway": "裝表掛表是度數累計的實體起點；及早完工報竣裝表，即可鎖定前送電期間的實質發電營收。",
        "visualTitle": "案場完工報竣、台電試運轉掛表與電費結算流轉示意圖",
        "visualType": "commissioning_meter",
        "thumbImg": "../assets/images/slides/slide_04.jpg",
        "thumbCaption": "講義 P.04：併聯試運轉檢驗項目與裝表計量作業手冊",
        "thumbLabel": "P.04 試運轉與裝表",
        "noteTakeaway": "檢驗課班長到場做併聯試運轉檢驗，合格當天就裝表掛表；裝表後電表就開始轉，電量完全不會浪費。",
        "noteDetail": "裝表後台電會核發『併聯完成函』，業者拿這張函去地方政府換設備登記；拿到設備登記後，前送電這段時間累積的度數台電會在第一期電費一次結清發放。",
        "noteTransition": "既有運轉中的案場若面板老化，該如何更新？請看第二模組第三型光電全數汰舊換新擴容新政。"
    },
    {
        "slideNo": 5,
        "module": "MODULE 2 ｜ 汰舊換新傳統枷鎖",
        "ref": "講義對照 P.05 ｜ 錄音 12:35~13:58",
        "title": "第三型光電汰舊換新傳統痛點：裝置容量受原核准容量死鎖，手續繁複受制地方審查",
        "question": "運轉 5~10 年的光電案場因風災受損或效率衰退欲更換面板，舊法規設定了哪些難以逾越的枷鎖？",
        "highlights": [
            "<strong>管理辦法第 16 條法源：</strong>太陽光電因老化、颱風損壞更換與容量有關之設備（太陽能板），必須報經輸配電業核轉主管機關核准。",
            "<strong>容量天花板死鎖：</strong>舊制嚴格限制更換後總容量「不得超過原設備登記容量」，多裝一度都屬違規，限制了技術升級紅利。",
            "<strong>公文公轉耗時數月：</strong>業者需先發函台電 ➔ 台電查核無虞轉函地方政府 ➔ 地方政府同意備查 ➔ 始得動工採購更換，發電損失慘重。"
        ],
        "takeaway": "舊制「不得超過原容量」限制了發電效能升級；面對面板衰退，案場陷入發電量持續萎縮的被動局面。",
        "visualTitle": "第三型光電舊制汰舊換新容量死鎖與公文流程痛點圖",
        "visualType": "retro_lock_pain",
        "thumbImg": "../assets/images/slides/slide_05.jpg",
        "thumbCaption": "講義 P.05：再生能源發電設備設置管理辦法第16條修法前條文",
        "thumbLabel": "P.05 舊制汰舊換新",
        "noteTakeaway": "以前光電板被颱風吹破或老化想要換新的，法規卡死更換後容量絕對不能比原登記大，多裝 1W 都不行！",
        "noteDetail": "以前換板子要先發公文給台電，台電轉給地方經發局，地方政府批核同意才能換，中間公文來回兩三個月，壞掉的板子不能發電，損失全由業者承擔。",
        "noteTransition": "最新法規如何破局？採用高效能面板如何突破容量限制？請看第六頁高效能模組擴容新政。"
    },
    {
        "slideNo": 6,
        "module": "MODULE 2 ｜ 高效能模組擴容突破",
        "ref": "講義對照 P.06 ｜ 錄音 13:58~16:08",
        "title": "高效能模組 (VPC) 突破容量天花板：只要台電饋線有餘裕，允許原場址大幅擴容換新",
        "question": "新制管理辦法如何為老舊案場解套？業者全數換裝 VPC 高效能面板，容量如何突破原裝機上限？",
        "highlights": [
            "<strong>全數更換高效能解鎖上限：</strong>依第 16 條第 2 項新制，案場若全數更換為高效能太陽能模組，更換後總容量「可超過原登記裝機容量」！",
            "<strong>原場址擴容 50% 實例：</strong>原登記 20kW 案場，換裝現代 500W+ 高效面板後容量躍升至 30kW，多出的 10kW 只要台電饋線有容量即可合法核准。",
            "<strong>台電出具容量證明為關鍵：</strong>突破容量上限的前提，是台電營業區處核查該節點尚有饋線餘裕，並正式出具「容量證明文件」。"
        ],
        "takeaway": "高效能模組換新是老舊案場「原地滿血復活＋大幅增產」的黃金政策窗口，徹底釋放屋頂潛能。",
        "visualTitle": "高效能模組 (VPC) 原場址突破容量天花板擴容模型 (20kW➔30kW)",
        "visualType": "vpc_expansion_model",
        "thumbImg": "../assets/images/slides/slide_06.jpg",
        "thumbCaption": "講義 P.06：第16條第2項高效能模組擴容申請原則",
        "thumbLabel": "P.06 VPC 擴容新政",
        "noteTakeaway": "吳課長宣布重大政策紅利：現在只要全數換成高效能 VPC 面板，容量可以合法突破原本上限，原案場 20kW 可以直接拉到 30kW！",
        "noteDetail": "十年前的面板一片只有 250W，現在隨便一片都 550W 以上；在同一個屋頂架構下，換新面板容量直接暴增 50% 以上，只要台電饋線還有空間就准許擴容！",
        "noteTransition": "擴容申請需要重新繳交土地建物文件嗎？請看第七頁擴容簡化流程與電價計算規則。"
    },
    {
        "slideNo": 7,
        "module": "MODULE 2 ｜ 擴容簡化與計價機制",
        "ref": "講義對照 P.07 ｜ 錄音 16:08~18:35",
        "title": "擴容行政綠色通道：免重複檢附土地建物權狀，新增容量適用新年度躉購費率",
        "question": "擴容汰舊換新需不需要重新辦理土地建物鑑界與審查？超出原登記容量的發電量如何結算電費？",
        "highlights": [
            "<strong>免重附土地建物證明：</strong>既有案場已合法建置於既有建物或土地上，擴容換新無需重新檢附地籍圖、建物權狀（地面型需補農業機關同意函）。",
            "<strong>超額容量審查要求：</strong>超出原容量部分若逾 20kW 免審門檻，需補辦併聯審查；台電核發新容量之審查意見書供報地方政府同意換照。",
            "<strong>新舊容量雙軌費率結算：</strong>原登記容量（如 20kW）維持歷史高躉購費率；擴容新增容量（如新增 10kW）依更換完工當年度公告費率核算！"
        ],
        "takeaway": "免附產權文件大幅加速擴容審批；新舊容量雙軌費率精準計費，確保案場歷史收益不受稀釋。",
        "visualTitle": "汰舊換新擴容綠色通道審查路徑 ✕ 新舊雙軌費率核算機制",
        "visualType": "dual_tariff_expansion",
        "thumbImg": "../assets/images/slides/slide_07.jpg",
        "thumbCaption": "講義 P.07：擴容容量計價方式與簡化檢附文件對照表",
        "thumbLabel": "P.07 擴容計價與免附文件",
        "noteTakeaway": "擴容換新不用再重新申請土地建物證明，省掉大筆代書費與公文時間；新增容量按當年度新費率算，原本舊容量照樣領舊的高費率！",
        "noteDetail": "如果原本簽 6 塊錢，擴容出來的 10kW 依照現在 4 塊多來算，兩者分開計費，既保障業者原本合約權益，又鼓勵業者投資把發電量極大化。",
        "noteTransition": "容量增加後，現場電氣保護與計量表計需要做哪些配合改動？請看第八頁擴容電氣校核與儀表升級。"
    },
    {
        "slideNo": 8,
        "module": "MODULE 2 ｜ 擴容電氣校核與表計",
        "ref": "講義對照 P.08 ｜ 錄音 18:35~19:06",
        "title": "擴容電氣校核必備：重新辦理細部協商（圖審）、校核保護協調與更換大型 CT/PT 表計",
        "question": "容量擴大後責任分界點面臨哪些衝擊？為什麼原有的計量電表與比流器 (CT) 必須強制升級？",
        "highlights": [
            "<strong>責任分界點衝擊校核：</strong>容量自 20kW 提升至 30kW，注入電網之額定電流與短路電流上升，必須重新向檢驗課辦理細部協商圖面審查。",
            "<strong>保護電驛重新整定：</strong>配合放大之變流器規格，過比流 (50/51) 與過電壓 (59) 跳脫值需重新計算整定，避免過載熔毀開關跳脫台電總盤。",
            "<strong>CT/PT 計量儀表升級：</strong>原有比流器 (CT) 額定容量恐面臨飽和溢位，台電送電前會同步更換大規格 CT/PT 表計，確保計量精準度。"
        ],
        "takeaway": "容量放大絕非單純換板子，電氣安全防線必須同步升級；重整保護與更換 CT 表計是擴容驗電送電的及格底線。",
        "visualTitle": "擴容案場電氣保護協調整定重新校核 ✕ CT/PT 儀表升級示意圖",
        "visualType": "electrical_ct_upgrade",
        "thumbImg": "../assets/images/slides/slide_08.jpg",
        "thumbCaption": "講義 P.08：責任分界點保護協調校核標準與CT換裝規範",
        "thumbLabel": "P.08 電氣保護與表計",
        "noteTakeaway": "容量從 20K 變 30K，電流變大，原本的開關保護跟電表可能受不了，必須重新送圖審讓台電檢查保護協調。",
        "noteDetail": "台電檢驗班長現場勘驗時，會檢查比流器 CT 規格有沒有跟著換大；如果沒換大，電表會燒掉或量不準，這些電氣細節工程師必須在設計階段就納入。",
        "noteTransition": "除了既有案場擴容，政府對新建建築物祭出了什麼強制法規？請看第三模組新建建築物強制設置光電規範。"
    },
    {
        "slideNo": 9,
        "module": "MODULE 3 ｜ 新建建築強制設置法源",
        "ref": "講義對照 P.09 ｜ 錄音 19:06~20:11",
        "title": "內政部新建建築強制光電法典：國土署七次跨部會協商，每 20m² 強制設置 1kW",
        "question": "再生能源發展條例第 12 條之 1 賦予內政部何種強制力？建築物強制設置太陽光電發電設備標準的核心準則是什麼？",
        "highlights": [
            "<strong>法定授權法源依據：</strong>依再生能源發展條例第 12 條之 1，內政部國土署歷經 7~8 次跨部會產官研深度協商，正式公布實施標準。",
            "<strong>每 20m² 設 1kW 剛性指標：</strong>符合條件之建築物，屋頂設置標準按「每 20 平方公尺建築/屋頂面積強制設置 1kW 光電容量」。",
            "<strong>千坪屋頂基本配額：</strong>以 1,000 平方公尺標準工廠/商辦為例，依法必須配置至少 50kW 太陽光電發電設備，屋頂綠能成為標配。"
        ],
        "takeaway": "光電已從「自願投資」正式躍升為建築法規之「法定強制標配」；每 20m² 設 1kW 成為全台營建業的設計新規範。",
        "visualTitle": "新建建築物強制設置光電法源體系與每 20m² 設 1kW 計算模型",
        "visualType": "mandatory_law_metric",
        "thumbImg": "../assets/images/slides/slide_09.jpg",
        "thumbCaption": "講義 P.09：建築物設置太陽光電發電設備標準條文要點",
        "thumbLabel": "P.09 強制設置法源",
        "noteTakeaway": "吳課長說明：內政部國土署開了七八次跨部會會議，台電也全程參與；現在只要蓋新房子符合規模，每 20 平方公尺就強制作 1kW 光電！",
        "noteDetail": "這項政策是國家 2050 淨零排放的關鍵拼圖，以後建商請建照必須直接把太陽能設計圖畫進去，1000 平方公尺的屋頂依法就是要生出 50kW 光電。",
        "noteTransition": "到底多大規模的建築物會被強制納管？哪些工程型態必須照辦？請看第十頁適用門檻與三擇一條件。"
    },
    {
        "slideNo": 10,
        "module": "MODULE 3 ｜ 強制適用對象與門檻",
        "ref": "講義對照 P.10 ｜ 錄音 20:11~21:17",
        "title": "強制適用三大門檻（三擇一即納管）：新建 1000m²、增建 1000m²、改建屋頂 1000m²",
        "question": "哪些建築工程會觸發強制裝設太陽光電義務？新建、增建與改建的判定面積標準有何細微差異？",
        "highlights": [
            "<strong>新建工程納管門檻：</strong>新建建築物之「建築面積」達 1,000 平方公尺（約 302.5 坪）以上者，強制設置光電。",
            "<strong>增建工程納管門檻：</strong>既有建築物增建，其「增加建築面積」達 1,000 平方公尺以上者，增建部分強制設置。",
            "<strong>改建工程納管門檻：</strong>既有建築物改建，其「改建屋頂面積」達 1,000 平方公尺以上者，全面強制納管安裝。",
            "<strong>工廠商辦全面先行：</strong>製造業廠房、物流倉儲、大型賣場與商辦大樓全數達到門檻，首波首當其衝全面推行！"
        ],
        "takeaway": "只要建築面積或屋頂面積跨越 1,000m² 紅線，即無條件觸發強制光電設計；規劃階段必須同步預留結構與電氣管線。",
        "visualTitle": "強制設置太陽光電三大建築型態判定樹狀圖 (新建/增建/改建 1000m²)",
        "visualType": "building_threshold_tree",
        "thumbImg": "../assets/images/slides/slide_10.jpg",
        "thumbCaption": "講義 P.10：新建、增建、改建建築物面積認定準則",
        "thumbLabel": "P.10 三大適用門檻",
        "noteTakeaway": "新建看建築面積 1000m²，增建看增加的面積 1000m²，改建看屋頂面積 1000m²，三個條件只要符合一個就逃不掉。",
        "noteDetail": "現在工業區蓋廠房動輒幾千坪，物流中心也是上千坪，全部都在強制設置範圍內；建築師在畫建築圖的時候就必須把結構承重、出線管路全部規劃好。",
        "noteTransition": "如果屋頂條件真的無法安裝，或者台電饋線沒容量，法規有豁免機制嗎？請看第十一頁豁免與暫緩條款。"
    },
    {
        "slideNo": 11,
        "module": "MODULE 3 ｜ 豁免機制與暫緩實施",
        "ref": "講義對照 P.11 ｜ 錄音 21:17~23:39, 34:27~35:38",
        "title": "合法免除設置三大彈性：台電容量不足依剩餘核減、特殊構造主管認定、住宅類暫緩",
        "question": "當台電電網容量不足或建築物有特殊構造時如何合法減免？為何住宅類與小型店面目前暫緩實施？",
        "highlights": [
            "<strong>台電饋線容量不足彈性下修：</strong>依法需裝 50kW，但台電審查確認饋線僅剩 10kW 容量，得依台電核定之 10kW 辦理設置與減免，不強人所難！",
            "<strong>特殊構造用途主管機關認定免設：</strong>寺廟教堂特殊斜頂、氣象雷達設施、電信機房、設有直升機停機坪之大型醫院，經審定得免設光電。",
            "<strong>住商兩大類暫不實施（2026/8/6 前）：</strong>G3 類辦公服務小型店面、H 類住宿類（集合住宅），因產權分散與管委會營運複雜，暫緩推行。"
        ],
        "takeaway": "法規兼顧電網瓶頸與建物特殊性；以台電容量證明或建築機關公文為憑，可合法精準核減裝置規模。",
        "visualTitle": "強制光電三大合法豁免與核減機制 ✕ 暫緩實施類別對照表",
        "visualType": "exemption_matrix",
        "thumbImg": "../assets/images/slides/slide_11.jpg",
        "thumbCaption": "講義 P.11：免除設置認定原則與特殊構造建築名冊",
        "thumbLabel": "P.11 豁免與暫緩規定",
        "noteTakeaway": "吳課長說明：如果台電饋線真的沒容量，台電會發證明，需要裝 50K 但台電只剩 10K，那就只裝 10K，建照照樣能拿。",
        "noteDetail": "像醫院屋頂要給直升機降落、氣象局屋頂有雷達，這些都可以申請免設；另外集合住宅公寓大樓因為上百戶產權很難分配，目前也先暫緩實施，避免糾紛。",
        "noteTransition": "強制設置的光電板在抗風結構與人員安全上有哪些嚴格規定？請看第十二頁 CNS 61215 負載與防墜工安。"
    },
    {
        "slideNo": 12,
        "module": "MODULE 3 ｜ 結構耐風與防墜工安",
        "ref": "講義對照 P.12 ｜ 錄音 23:39~25:07, 27:29~28:51",
        "title": "CNS 61215 靜態負載 5400Pa 測試：屋頂光電強制配置維護爬梯、走道通道與防護欄杆",
        "question": "屋頂光電如何抵禦台灣強烈颱風威脅？職安署與國土署在條文中寫入了哪些強制性人員安全設施？",
        "highlights": [
            "<strong>CNS 61215 靜態機械負載報告：</strong>屋頂安裝之光電模組必須通過靜態機械負載測試，出具正負向荷重 5,400 Pa（耐強颱風壓）之合格實驗報告。",
            "<strong>全生命週期防墜設施：</strong>條文強制要求設置場所必須具備永久性「維護爬梯、走道通道板與安全防護欄杆」，杜絕臨時作業踩踏採光罩墜落。",
            "<strong>跨部會防墜工安共識：</strong>國土署與職安署嚴格把關，未依圖設置通道與欄杆之建築物，將無法通過竣工會勘驗收。"
        ],
        "takeaway": "5400Pa 抗風強度與永久防墜欄杆通道是建築光電硬指標；將運維工安融入初始土建設計，方為長治久安之道。",
        "visualTitle": "CNS 61215 機械負載 5400Pa 測試標準 ✕ 屋頂三防一通工安架構",
        "visualType": "cns_wind_safety",
        "thumbImg": "../assets/images/slides/slide_12.jpg",
        "thumbCaption": "講義 P.12：屋頂光電結構抗風計算與安全防護設施規範",
        "thumbLabel": "P.12 抗風與防墜工安",
        "noteTakeaway": "屋頂光電板必須有 5400Pa 機械負載報告，確保颱風天不會被吹飛砸傷路人；屋頂上一定要做爬梯、通道走道跟防護欄杆。",
        "noteDetail": "職安署在會議中非常堅持這點：以往很多工人巡檢踩破採光罩摔死，現在法規直接要求建商在蓋房子的時候就要把永久性維護通道跟欄杆做好，保護後續維運人員生命安全。",
        "noteTransition": "除了結構安全，電氣迴路上最關鍵的「市電中斷孤島獨立運轉」如何落實？請看第四模組孤島獨立運轉與兩次檢驗卡控。"
    },
    {
        "slideNo": 13,
        "module": "MODULE 4 ｜ 市電斷電獨立運轉",
        "ref": "講義對照 P.13 ｜ 錄音 25:07~27:29",
        "title": "市電中斷孤島供電：光電系統必須與台電電網實體隔離，具備獨立轉供建築物能力",
        "question": "能源署與國土署為何強制要求「停電時光電要能發電自用」？如何透過 ATS 自動轉供開關兼顧防逆送與不斷電？",
        "highlights": [
            "<strong>法規政策核心訴求：</strong>政府不希望屋頂光電純粹只是賣電機器；當台電大停電時，建築物上的太陽能必須能獨立供應建築內部緊急用電！",
            "<strong>實體隔離保護台電人員：</strong>市電中斷時，光電系統必須藉由 ATS（自動切換開關）或手動隔離裝置與台電電網切離，嚴禁向外逆送電危及台電搶修人員。",
            "<strong>建立電氣基準啟動發電：</strong>透過搭配儲能系統 (BESS) 或緊急柴油發電機建立參考電壓與頻率，使光電逆變器偵測到電網信號重新啟動發電。"
        ],
        "takeaway": "停電時與台電隔離並轉供內線，是屋頂光電從「單純售電」轉型為「電網韌性分散式微電網」的核心技術飛躍。",
        "visualTitle": "市電中斷實體隔離 (ATS) ✕ 建築內線孤島自發自用微電網拓撲",
        "visualType": "island_microgrid",
        "thumbImg": "../assets/images/slides/slide_13.jpg",
        "thumbCaption": "講義 P.13：市電斷電隔離運轉機制與自動轉供切換線路",
        "thumbLabel": "P.13 斷電孤島運轉",
        "noteTakeaway": "吳課長點出政府最在乎的重點：台電大停電的時候，屋頂太陽能板不能跟著廢掉，必須能繼續發電給建築物自己用！",
        "noteDetail": "但前提是必須先裝 ATS 開關跟台電電網徹底切開，不然電逆送到台電電線桿上，台電維修人員上去搶修會被活活電死！切開之後，靠儲能或小發電機建立基準電壓，光電就能恢復發電。",
        "noteTransition": "獨立發電後，這筆電到底該並到建築物的哪一個盤？請看第十四頁光電併內線優先順序。"
    },
    {
        "slideNo": 14,
        "module": "MODULE 4 ｜ 光電併內線路徑配置",
        "ref": "講義對照 P.14 ｜ 錄音 39:46~41:11",
        "title": "光電併入建築內線策略：優先配置公共緊急迴路盤，兼顧試車用電與自用韌性",
        "question": "光電所發電力在建築物內部如何配置？併接公設內線、緊急照明還是產線動力盤？",
        "highlights": [
            "<strong>並接公共設施緊急迴路盤：</strong>停電時電力優先供給大樓電梯、地下室抽水泵、消防排煙機與緊急照明等關鍵維生負載。",
            "<strong>自發自用不轉售選型：</strong>若台電外線容量不足以承載全額躉售，業者可選用「全自發自用」，加裝零逆送電控制裝置，免除台電併網排隊等待。",
            "<strong>建築未送電前之「試車用電」：</strong>光電盤需具備獨立分盤開關，以便在建築物整體用電尚未正式送電前，單獨進行發電系統之試車驗電。"
        ],
        "takeaway": "依負載重要性階梯化配置光電自用迴路；並入公共緊急盤，能在災害斷電時提供最高等級的防災韌性保險。",
        "visualTitle": "建築物內部用電配電盤分流 ✕ 光電併接緊急迴路階梯架構",
        "visualType": "internal_distribution",
        "thumbImg": "../assets/images/slides/slide_14.jpg",
        "thumbCaption": "講義 P.14：光電系統併接建築內線盤與緊急負載切換圖",
        "thumbLabel": "P.14 併內線路徑配置",
        "noteTakeaway": "建築物設計光電時，最好並到公共設施的緊急受電盤，停電時抽水機、緊急電梯跟照明都能繼續運作。",
        "noteDetail": "在新建工程階段，大樓通常還沒正式通電，光電盤必須做獨立分盤隔離，這樣台電檢驗人員才能先針對光電系統進行『試車送電』，加速後續使照審驗。",
        "noteTransition": "營建與光電進度如何連動？建照使照與發電許可如何互相卡控？請看第十五頁證照連鎖卡控機制。"
    },
    {
        "slideNo": 15,
        "module": "MODULE 4 ｜ 建照使照連鎖卡控",
        "ref": "講義對照 P.15 ｜ 錄音 28:51~32:27",
        "title": "建照與使照連鎖雙重卡控：申請建照附圖說、申請使照附發電許可，杜絕掛羊頭賣狗肉",
        "question": "政府如何確保建商不會在完工後拆除光電？建照與使用執照的核發被設定了哪些「前置綁定條件」？",
        "highlights": [
            "<strong>申請「建照」之卡控關卡：</strong>掛號申請建築執照時，必須同步檢附「光電設置圖說」或「台電容量不足/受光不足之合法減免公文」。",
            "<strong>申請「使照」之卡控關卡：</strong>建築物完工申請使用執照時，必須檢附主管機關核發之「發電設備工作許可函」或「三年內同意備案證明」。",
            "<strong>杜絕虛應故事法制化閉環：</strong>若屋頂光電未依核定圖說施工完竣，建築主管機關一律暫緩核發使用執照，使建商無法交屋交割！"
        ],
        "takeaway": "建照綁圖說、使照綁許可；法制化閉環將光電驗收直接與建商交屋核心利益綁定，徹底杜絕虛應故事。",
        "visualTitle": "建築執照與使用執照連鎖綁定光電審驗閉環流程圖",
        "visualType": "license_interlock_loop",
        "thumbImg": "../assets/images/slides/slide_15.jpg",
        "thumbCaption": "講義 P.15：建照使照核發要點與光電查驗聯動審核表",
        "thumbLabel": "P.15 建照使照卡控",
        "noteTakeaway": "以前建商常常騙說會裝太陽能，房子蓋好就把屋頂拿去賣空中花園；現在法規設下鐵籠，沒附光電工作許可，連使用執照都拿不到！",
        "noteDetail": "拿不到使照建商就無法過戶、銀行分期款進不來，建商比誰都急！這套機制把建築審查跟能源管理完全縫合在一起，確保光電工程如期如質落地。",
        "noteTransition": "在施工完工送電環節，台電檢驗人員到底怎麼現場查驗？請看第十六頁台電兩次到場檢驗 SOP。"
    },
    {
        "slideNo": 16,
        "module": "MODULE 4 ｜ 台電兩次到場檢驗",
        "ref": "講義對照 P.16 ｜ 錄音 32:40~34:11, 41:11~41:48",
        "title": "台電現場檢驗「跑兩趟」SOP：第 1 趟驗發電送電、第 2 趟驗建物用電，確保光電先到位",
        "question": "為什麼台電檢驗班長必須分兩次到場？為什麼不能發電與用電「一次會勘搞定」？",
        "highlights": [
            "<strong>第 1 趟檢驗（發電設備檢驗送電）：</strong>專門查驗屋頂光電模組、逆變器、保護開關與責任分界點，試運轉送電後取得設備登記證明。",
            "<strong>第 2 趟檢驗（建築物整體用電送電）：</strong>業者持「使用執照副本 ＋ 光電設備登記文件」，台電始派員進行建築物整體用電檢驗並掛用電表。",
            "<strong>台電先發後用鐵律：</strong>台電內部程序嚴格落實「屋頂光電發電先送電、建築物本體用電後送電」，未完成光電建置絕不提供大樓正式用電！"
        ],
        "takeaway": "「先發電、後用電，班長跑兩趟」是台電嚴格落實國家政策的行政鐵律；兩階段送電時程必須精準排程。",
        "visualTitle": "台電檢驗班長「兩次到場檢驗送電」標準作業程序 (SOP)",
        "visualType": "two_inspection_sop",
        "thumbImg": "../assets/images/slides/slide_16.jpg",
        "thumbCaption": "講義 P.16：台電兩階段檢驗送電作業標準作業書",
        "thumbLabel": "P.16 台電兩次檢驗SOP",
        "noteTakeaway": "吳課長親自說明：台電檢驗課班長必須去兩趟！第一趟專門驗屋頂太陽能發電，第二趟才驗整棟大樓的用電掛表。",
        "noteDetail": "開會時很多建商哀求能不能跑一趟就好，但台電堅持跑兩趟，目的就是卡控建商：如果你屋頂太陽能沒通電，台電就不會給大樓正式用電，杜絕先上車後補票的投機心理。",
        "noteTransition": "進入案場運維階段，當變流器壞掉時如何快速更換？請看第五模組第三型光電變流器簡化更換程序。"
    },
    {
        "slideNo": 17,
        "module": "MODULE 5 ｜ 變流器故障停機痛點",
        "ref": "講義對照 P.17 ｜ 錄音 41:48~43:33",
        "title": "變流器故障停機痛點：舊制圖審修約耗時數月，案場每日數千度發電損失由業者買單",
        "question": "變流器是案場心臟，故障率最高；舊法規下更換變流器面臨哪些令人窒息的繁文縟節？",
        "highlights": [
            "<strong>繁雜舊制流程：</strong>變流器燒毀故障 ➔ 向台電營業區處申請更換 ➔ 重新辦理細部協商（圖審）➔ 修改供電契約 ➔ 核准始准採購安裝。",
            "<strong>漫長審查行政真空：</strong>一趟公文流程動輒延宕 1~2 個月；在夏季艷陽日，一個 100kW 案場停機一天即損失 400~500 度電（約數千元），累積損失達數十萬！",
            "<strong>公會陳情與三方破局：</strong>進金生等公會代表積極向台電與能源署反映，促成台電、能源署與產業公會展開三方協商，催生改革便民新制。"
        ],
        "takeaway": "停機一天就是實質虧損一天；打破事前死板審查流程，是維運工程師與投資業主最迫切的實務訴求。",
        "visualTitle": "變流器故障舊制停機損失累積模型 ✕ 三方公會協商破局歷程",
        "visualType": "inverter_outage_loss",
        "thumbImg": "../assets/images/slides/slide_17.jpg",
        "thumbCaption": "講義 P.17：變流器更換舊制流程圖與每日發電損失統計",
        "thumbLabel": "P.17 變流器停機痛點",
        "noteTakeaway": "以前變流器被雷打壞或燒掉，不能自己買來換，必須先去台電報備、重新送圖審、重新簽合約，光是公文就跑一兩個月！",
        "noteDetail": "夏天太陽正烈的時候，電廠停機兩個月沒電賣，幾十萬電費全泡湯，還要繳銀行貸款；公會不斷向台電跟能源署反映，最後三方達成共識推出簡化流程。",
        "noteTransition": "新制如何落實「先斬後奏」？需要滿足哪些前提條件？請看第十八頁第三型變流器先換後報備新制。"
    },
    {
        "slideNo": 18,
        "module": "MODULE 5 ｜ 先換後報備便民新制",
        "ref": "講義對照 P.18 ｜ 錄音 43:33~45:20",
        "title": "第三型變流器「先換後報備」：1:1 規格容量完全相同先斬後奏，停機時數大幅壓縮 90%",
        "question": "什麼是「先斬後奏」的便民更換新制？業者更換變流器時如何做到合法先換、事後補報備？",
        "highlights": [
            "<strong>先更換即刻復電（先斬後奏）：</strong>台電原則同意業者於變流器故障當下「先行採購更換並恢復發電」，將停機發電損失壓縮至最低！",
            "<strong>三大硬性等額條件（1:1 更換）：</strong>更換前後之「容量（如 20kW 限換 20kW）」、「相序（三相限換三相）」、「內部保險規格」必須完全一致。",
            "<strong>更換完竣事後報備抽查：</strong>更換完成後，業者檢附設備型錄與銘牌照片向台電區處報備，台電派員現場抽核無誤即正式發函備查，免除行政違規風險。"
        ],
        "takeaway": "「1:1 規格相同先換後報備」是台電對光電維運的最大便民德政；即時復電止血，事後補件合規。",
        "visualTitle": "第三型變流器「先換後報備」簡化作業流程 (SOP 比較圖)",
        "visualType": "inverter_fast_track",
        "thumbImg": "../assets/images/slides/slide_18.jpg",
        "thumbCaption": "講義 P.18：第三型光電變流器簡化更換作業指引",
        "thumbLabel": "P.18 變流器簡化更換",
        "noteTakeaway": "吳課長說明：現在台電同意『先斬後奏』！只要你換的變流器容量一樣、三相換三相、保護規格一樣，你可以先換上去發電，換完再來跟台電報備！",
        "noteDetail": "換完之後台電會派員去看一下銘牌，只要真的跟你報的一樣，台電就發備查函結案。這樣案場停電時間從兩個月縮短到一兩天，替業者搶回巨額電費！",
        "noteTransition": "有哪些情況絕對不適用簡化程序？若偷改容量或相序會有什麼後果？請看第十九頁簡化程序邊界紅線。"
    },
    {
        "slideNo": 19,
        "module": "MODULE 5 ｜ 簡化更換之邊界紅線",
        "ref": "講義對照 P.19 ｜ 錄音 45:20~47:06",
        "title": "簡化程序邊界紅線：嚴禁單三相切換或私自擴容，涉及規格變更一律回歸常規圖審",
        "question": "更換變流器若想順便加大容量或改接單相，為什麼絕對不能先換後報？一旦違規將面臨哪些法律責任？",
        "highlights": [
            "<strong>嚴禁單三相相序變更：</strong>絕不可將原本三相變流器私自更換為單相設備，否則將引發台電配電線路嚴重的「三相電壓不平衡」慘遭斷開！",
            "<strong>容量變更大於原機者無效：</strong>若配合汰舊換新欲將 20kW 擴大至 30kW，因涉及責任分界點短路容量與保護變更，絕對不適用先換後報！",
            "<strong>保險與保固責任邊界：</strong>私自更換未備查之變流器，若日後案場引發火災事故，保險公司與法院調卷查核將判定為違規安裝並拒絕理賠！"
        ],
        "takeaway": "規格相同走快車道，變更規格走常規圖審；守住 1:1 等額紅線，方能兼顧發電時效與法律合規防禦。",
        "visualTitle": "變流器更換快車道 (先換後備) vs 常規道 (圖審修約) 判定決策樹",
        "visualType": "inverter_decision_tree",
        "thumbImg": "../assets/images/slides/slide_19.jpg",
        "thumbCaption": "講義 P.19：變流器更換適用條件檢核表與違規罰則",
        "thumbLabel": "P.19 更換邊界紅線",
        "noteTakeaway": "吳課長嚴肅提醒：千萬不要三相偷偷換單相，或者 20K 偷換成 30K！這絕對不適用簡化程序，一定要先送台電做細部協商圖審！",
        "noteDetail": "很多保險公司跟法院發生火災理賠糾紛時，都會跟台電調最初核准的圖說對照；如果你私自改裝沒報備，火災保險一毛錢都不會賠，責任要工程師自己扛！",
        "noteTransition": "融會貫通全日課程，維運團隊與案場經理必須恪守哪些核心準則？請看第二十頁台電併網審查與維運十條軍規。"
    },
    {
        "slideNo": 20,
        "module": "MODULE 5 ｜ 併網與維運十條軍規",
        "ref": "全課歸納 ｜ 錄音 00:00~47:06",
        "title": "台電併網審查與維運十條軍規：時效防禦、責任分界、擴容紅利與合規驗收指南",
        "question": "身處電網嚴格監管環境，維運工程師與專案主管必須將哪十條操作鐵律深植於日常作業中？",
        "highlights": [
            "<strong>時效紀律（軍規 1-3）：</strong>備案 2 個月內啟動簽約；簽約 1 年內完工登記；裝表日即刻核對「併聯完成函」起算度數。",
            "<strong>擴容與新建（軍規 4-7）：</strong>汰舊換新全換 VPC 突破原容量上限；千坪新建案每 20m² 設 1kW 預留爬梯；電網不足出具台電證明合法下修；市電中斷必設 ATS 孤島切離。",
            "<strong>運維與更換（軍規 8-10）：</strong>兩階段送電「先發後用」嚴控建照使照時程；變流器 1:1 等額先換後報；變更容量或相序必回歸細部協商圖審。"
        ],
        "takeaway": "併網合規是電廠商業運轉的生命線；恪守十條軍規，確保案場二十年發電無虞、資產價值最大化。",
        "visualTitle": "台電併網審查、工程擴容與維運實戰十條軍規檢核法典",
        "visualType": "ten_commandments_c5",
        "thumbImg": "../assets/images/slides/slide_20.jpg",
        "thumbCaption": "講義 P.20：台電併聯技術規範與維運十條軍規總結",
        "thumbLabel": "P.20 併網十條軍規",
        "noteTakeaway": "十條軍規匯集台電配電處官方第一手審查標準與工程實戰經驗，是進金生每位維運工程師的防身寶典。",
        "noteDetail": "嚴控 2 個月與 1 年時限、善用 VPC 汰舊換新擴容紅利、變流器故障先換後報備，每一條都能替公司避開法規風險，穩穩賺進綠能收益。",
        "noteTransition": "全課 20 頁精華講解完畢，歡迎按 G 鍵切換總覽網格，或按 P 鍵匯出 16:9 顧問 PDF 備忘錄。"
    }
]

def make_visual_body(vtype):
    # Generates custom SVG for each visual type
    if vtype == "grid_six_stages":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="c5_g1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1B365D"/>
              <stop offset="100%" stop-color="#0E8A78"/>
            </linearGradient>
          </defs>
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">太陽光電建置與台電併網六大核心階段全流程</text>
          
          <!-- 上半段：籌設規劃期 (1-2) -->
          <rect x="20" y="48" width="245" height="90" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="20" y="48" width="245" height="24" rx="6" fill="#1D4ED8"/>
          <text x="142" y="65" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段 I：籌設規劃許可 (台電 ✕ 政府)</text>

          <g transform="translate(30, 80)" font-size="9.5" fill="#1E293B">
            <rect x="0" y="0" width="105" height="48" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
            <text x="52" y="20" font-weight="bold" fill="#1E40AF" text-anchor="middle">1. 併聯審查</text>
            <text x="52" y="36" font-size="8.5" fill="#64748B" text-anchor="middle">饋線容量與衝擊</text>

            <path d="M 108 24 L 122 24" stroke="#3B82F6" stroke-width="2"/>

            <rect x="125" y="0" width="105" height="48" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
            <text x="177" y="20" font-weight="bold" fill="#1E40AF" text-anchor="middle">2. 同意備案</text>
            <text x="177" y="36" font-size="8.5" fill="#64748B" text-anchor="middle">地方主管機關核定</text>
          </g>

          <!-- 箭頭向下 -->
          <path d="M 270 93 L 290 93 L 290 148 L 275 148" stroke="#0E8A78" stroke-width="2" fill="none"/>

          <!-- 下半段：工程建置與運轉 (3-6) -->
          <rect x="20" y="148" width="500" height="110" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
          <rect x="20" y="148" width="500" height="24" rx="6" fill="#047857"/>
          <text x="270" y="165" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段 II：實體工程施作、驗電與電費結算</text>

          <g transform="translate(30, 180)" font-size="9.5" fill="#1E293B">
            <!-- 3. 簽訂契約 -->
            <rect x="0" y="0" width="110" height="68" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
            <text x="55" y="20" font-weight="bold" fill="#047857" text-anchor="middle">3. 簽訂契約</text>
            <text x="55" y="36" font-size="8.5" fill="#DC2626" font-weight="bold" text-anchor="middle">備案後 2 個月內</text>
            <text x="55" y="52" font-size="8" fill="#64748B" text-anchor="middle">台電購售電合約</text>

            <path d="M 112 34 L 123 34" stroke="#10B981" stroke-width="2"/>

            <!-- 4. 案場施工 -->
            <rect x="125" y="0" width="110" height="68" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
            <text x="180" y="20" font-weight="bold" fill="#047857" text-anchor="middle">4. 案場施工</text>
            <text x="180" y="36" font-size="8.5" fill="#DC2626" font-weight="bold" text-anchor="middle">簽約後 1 年內完工</text>
            <text x="180" y="52" font-size="8" fill="#64748B" text-anchor="middle">屋頂支架與配線</text>

            <path d="M 237 34 L 248 34" stroke="#10B981" stroke-width="2"/>

            <!-- 5. 試運轉掛表 -->
            <rect x="250" y="0" width="110" height="68" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
            <text x="305" y="20" font-weight="bold" fill="#047857" text-anchor="middle">5. 試運轉送電</text>
            <text x="305" y="36" font-size="8.5" fill="#0E8A78" font-weight="bold" text-anchor="middle">現場驗電裝表</text>
            <text x="305" y="52" font-size="8" fill="#64748B" text-anchor="middle">核發「併聯完成函」</text>

            <path d="M 362 34 L 373 34" stroke="#10B981" stroke-width="2"/>

            <!-- 6. 設備登記售電 -->
            <rect x="375" y="0" width="105" height="68" rx="4" fill="url(#c5_g1)" stroke="#0E8A78"/>
            <text x="427" y="20" font-weight="bold" fill="#FFFFFF" text-anchor="middle">6. 設備登記</text>
            <text x="427" y="36" font-size="8.5" fill="#FDE047" font-weight="bold" text-anchor="middle">取得設備身分證</text>
            <text x="427" y="52" font-size="8" fill="#E2E8F0" text-anchor="middle">正式按月結清電費</text>
          </g>
        </svg>
        '''
    elif vtype == "timeline_deadlines":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">光電併網關鍵時效紅線與違規連鎖代價</text>

          <!-- 時間軸主線 -->
          <line x1="40" y1="90" x2="500" y2="90" stroke="#CBD5E1" stroke-width="4"/>

          <!-- 節點 1: 同意備案取得 -->
          <circle cx="70" cy="90" r="10" fill="#1E40AF" stroke="#DBEAFE" stroke-width="3"/>
          <text x="70" y="70" font-size="10.5" font-weight="bold" fill="#1E40AF" text-anchor="middle">取得同意備案</text>
          <text x="70" y="115" font-size="8.5" fill="#64748B" text-anchor="middle">時效倒數起算點</text>

          <!-- 紅線 1: 2 個月 -->
          <line x1="70" y1="90" x2="220" y2="90" stroke="#DC2626" stroke-width="4"/>
          <circle cx="220" cy="90" r="10" fill="#DC2626" stroke="#FEE2E2" stroke-width="3"/>
          <text x="145" y="60" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">⚠️ 限期 2 個月內</text>
          <text x="145" y="75" font-size="9" fill="#991B1B" text-anchor="middle">向台電申請辦理簽約</text>
          
          <rect x="170" y="115" width="100" height="50" rx="4" fill="#FEF2F2" stroke="#FCA5A5"/>
          <text x="220" y="132" font-size="9" font-weight="bold" fill="#B91C1C" text-anchor="middle">簽訂購售契約</text>
          <text x="220" y="148" font-size="8" fill="#64748B" text-anchor="middle">(含細部協商圖審)</text>

          <!-- 紅線 2: 1 年內 -->
          <line x1="220" y1="90" x2="450" y2="90" stroke="#D97706" stroke-width="4"/>
          <circle cx="450" cy="90" r="10" fill="#059669" stroke="#D1FAE5" stroke-width="3"/>
          <text x="335" y="60" font-size="11" font-weight="bold" fill="#D97706" text-anchor="middle">⚠️ 簽約後 1 年內強制完工</text>
          <text x="335" y="75" font-size="9" fill="#92400E" text-anchor="middle">必須正式取得「設備登記」</text>

          <rect x="400" y="115" width="100" height="50" rx="4" fill="#F0FDF4" stroke="#86EFAC"/>
          <text x="450" y="132" font-size="9" font-weight="bold" fill="#15803D" text-anchor="middle">取得設備登記</text>
          <text x="450" y="148" font-size="8" fill="#64748B" text-anchor="middle">正式轉售起算電費</text>

          <!-- 下方違規嚴重後果警示框 -->
          <rect x="25" y="180" width="490" height="75" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
          <text x="35" y="200" font-size="10.5" font-weight="bold" fill="#B91C1C">🚫 逾期違規之慘重代價（法規明定罰則）：</text>
          <text x="35" y="220" font-size="9" fill="#334155">① 逾期未簽約或超期未完工：地方政府直接撤銷「同意備案」，案場喪失合法地位！</text>
          <text x="35" y="238" font-size="9" fill="#334155">② 躉購費率直接跌落：必須重新申請備案，無法適用當年較高收購價，直接適用新年度低費率，損失數百萬！</text>
        </svg>
        '''
    elif vtype == "taipower_six_steps":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電側六類細分審查權責 ✕ 交流責任分界點防禦架構</text>

          <!-- 六類審查卡片 -->
          <g transform="translate(20, 52)" font-size="9.5">
            <rect x="0" y="0" width="155" height="60" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="77" y="18" font-weight="bold" fill="#1E40AF" text-anchor="middle">1. 併聯審查 ✕ 初步協商</text>
            <text x="77" y="34" font-size="8.5" fill="#334155" text-anchor="middle">配電級區處合併辦理</text>
            <text x="77" y="48" font-size="8" fill="#64748B" text-anchor="middle">核定饋線容量與併網節點</text>

            <rect x="172" y="0" width="155" height="60" rx="4" fill="#F0FDF4" stroke="#10B981"/>
            <text x="250" y="18" font-weight="bold" fill="#047857" text-anchor="middle">2. 簽訂購售契約</text>
            <text x="250" y="34" font-size="8.5" fill="#334155" text-anchor="middle">區營業處營業課主辦</text>
            <text x="250" y="48" font-size="8" fill="#64748B" text-anchor="middle">保障 20 年收購權利義務</text>

            <rect x="345" y="0" width="155" height="60" rx="4" fill="#FEFCE8" stroke="#F59E0B"/>
            <text x="422" y="18" font-weight="bold" fill="#B45309" text-anchor="middle">3. 併聯細部協商 (圖審)</text>
            <text x="422" y="34" font-size="8.5" fill="#334155" text-anchor="middle">區營業處檢驗課主辦</text>
            <text x="422" y="48" font-size="8" fill="#64748B" text-anchor="middle">核定責任分界點交流保護</text>

            <rect x="0" y="70" width="155" height="60" rx="4" fill="#FAF5FF" stroke="#A855F7"/>
            <text x="77" y="88" font-weight="bold" fill="#7E22CE" text-anchor="middle">4. 外線施工與報竣</text>
            <text x="77" y="104" font-size="8.5" fill="#334155" text-anchor="middle">台電延伸線路至分界點</text>
            <text x="77" y="118" font-size="8" fill="#64748B" text-anchor="middle">業者案場完工報竣</text>

            <rect x="172" y="70" width="155" height="60" rx="4" fill="#ECFDF5" stroke="#059669"/>
            <text x="250" y="88" font-weight="bold" fill="#065F46" text-anchor="middle">5. 併聯試運轉 (前送電)</text>
            <text x="250" y="104" font-size="8.5" fill="#334155" text-anchor="middle">檢驗課現場驗電裝表</text>
            <text x="250" y="118" font-size="8" fill="#64748B" text-anchor="middle">相序校正與保護跳脫測試</text>

            <rect x="345" y="70" width="155" height="60" rx="4" fill="#F0FDFA" stroke="#0E8A78"/>
            <text x="422" y="88" font-weight="bold" fill="#0E8A78" text-anchor="middle">6. 核發併聯完成函</text>
            <text x="422" y="104" font-size="8.5" fill="#334155" text-anchor="middle">計量電表正式起算度數</text>
            <text x="422" y="118" font-size="8" fill="#64748B" text-anchor="middle">供業者申辦設備登記</text>
          </g>

          <!-- 下方細部協商審查原則剖析 -->
          <rect x="20" y="195" width="500" height="62" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="35" y="215" font-size="10" font-weight="bold" fill="#1B365D">吳課長親授細部協商 (圖審) 核心心法：</text>
          <text x="35" y="233" font-size="9" fill="#334155">✓ 台電審查邊界：僅審核責任分界點「交流側」開關配置與保護協調，不介入案場內部直流串列佈局。</text>
          <text x="35" y="247" font-size="8.5" fill="#64748B">✓ 核心底線：案場故障時，案場主開關必須比台電外線開關優先跳脫，嚴防電廠事故拖垮整條電網！</text>
        </svg>
        '''
    elif vtype == "commissioning_meter":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">完工報竣、試運轉裝表與前送電電費回溯結算流轉</text>

          <!-- 步驟流程三欄 -->
          <g transform="translate(25, 52)">
            <!-- 欄 1: 報竣試運轉 -->
            <rect x="0" y="0" width="150" height="115" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
            <text x="75" y="22" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Step 1：完工報竣驗電</text>
            <text x="75" y="42" font-size="9" fill="#334155" text-anchor="middle">・業者施工完畢報竣</text>
            <text x="75" y="58" font-size="9" fill="#334155" text-anchor="middle">・檢驗課班長現場驗電</text>
            <text x="75" y="74" font-size="9" fill="#334155" text-anchor="middle">・絕緣阻抗與接地測試</text>
            <text x="75" y="92" font-size="8.5" fill="#64748B" text-anchor="middle">確認責任分界點安全</text>

            <path d="M 155 57 L 165 57" stroke="#3B82F6" stroke-width="2"/>

            <!-- 欄 2: 掛表與完成函 -->
            <rect x="170" y="0" width="150" height="115" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
            <text x="245" y="22" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">Step 2：裝表前送電</text>
            <text x="245" y="42" font-size="9" fill="#334155" text-anchor="middle">・台電裝設專用計量表</text>
            <text x="245" y="58" font-size="9" font-weight="bold" fill="#0E8A78" text-anchor="middle">・核發「併聯完成函」</text>
            <text x="245" y="74" font-size="9" fill="#334155" text-anchor="middle">・電表即刻開始累計度數</text>
            <text x="245" y="92" font-size="8.5" fill="#15803D" font-weight="bold" text-anchor="middle">★ 度數從此時開始計算</text>

            <path d="M 325 57 L 335 57" stroke="#10B981" stroke-width="2"/>

            <!-- 欄 3: 登記與電費補發 -->
            <rect x="340" y="0" width="150" height="115" rx="6" fill="#FEFCE8" stroke="#F59E0B" stroke-width="1.5"/>
            <text x="415" y="22" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">Step 3：設備登記結算</text>
            <text x="415" y="42" font-size="9" fill="#334155" text-anchor="middle">・向主管機關申辦登記</text>
            <text x="415" y="58" font-size="9" fill="#334155" text-anchor="middle">・正式取得設備身分證</text>
            <text x="415" y="74" font-size="9" font-weight="bold" fill="#D97706" text-anchor="middle">・電費一併結算發放</text>
            <text x="415" y="92" font-size="8.5" fill="#64748B" text-anchor="middle">按月週期撥付躉售款</text>
          </g>

          <!-- 下方電費追溯機制說明 -->
          <rect x="25" y="180" width="490" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="35" y="200" font-size="10.5" font-weight="bold" fill="#1B365D">前送電期間電費結算機制核心釋疑：</text>
          <text x="35" y="218" font-size="9" fill="#334155">・掛表到正式登記通常有數週行政時間差；台電自「裝表送電日」起電表即啟動計量。</text>
          <text x="35" y="234" font-size="9" fill="#334155">・正式取得設備登記後，前送電這段期間所累積的所有發電度數，台電將在「第一期電費單」一次全額補發結清！</text>
        </svg>
        '''
    elif vtype == "retro_lock_pain":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">第三型光電舊制汰舊換新容量死鎖與公文流程痛點</text>

          <!-- 左側痛點 1: 原容量鎖死 -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="28" rx="6" fill="#DC2626"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">痛點一：原登記容量天花板死鎖</text>

          <g transform="translate(37, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#991B1B">【舊制第 16 條嚴苛限制】</text>
            <text y="18">・更換面板後總容量不得超過原登記容量</text>
            <text y="36">・多裝 1W 都屬違規！</text>
            <text y="56" font-weight="bold" fill="#B91C1C">現代技術升級巨大障礙：</text>
            <text y="72">・舊案場 250W 面板早已全面停產</text>
            <text y="88">・市場現貨皆為 500W~600W 高效模組</text>
            <text y="104">・換新面板被迫「空出大半屋頂不敢鋪滿」</text>
            <text y="122" font-size="9" font-weight="bold" fill="#DC2626">➔ 白白浪費寶貴屋頂空間與發電潛力！</text>
          </g>

          <!-- 右側痛點 2: 公文冗長 -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="28" rx="6" fill="#D97706"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">痛點二：多層公文核轉耗時數月</text>

          <g transform="translate(292, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#B45309">【公文層層轉呈行政真空】</text>
            <text y="18">1. 業者發函台電區處申請換板</text>
            <text y="36">2. 台電區處核轉地方政府主管機關</text>
            <text y="54">3. 地方政府審查備查發函同意</text>
            <text y="72">4. 業者始得採購面板進場施工更換</text>
            <text y="94" font-weight="bold" fill="#B45309">發電損失誰買單？</text>
            <text y="110">颱風受損板子停擺 2~3 個月無法發電，</text>
            <text y="126" font-size="9" font-weight="bold" fill="#D97706">每天數千度發電收益全數蒸發！</text>
          </g>
        </svg>
        '''
    elif vtype == "vpc_expansion_model":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">高效能模組 (VPC) 突破容量上限擴容模型 (20kW➔30kW)</text>

          <!-- 舊案場 20kW -->
          <rect x="35" y="70" width="160" height="160" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="35" y="70" width="160" height="26" rx="6" fill="#1D4ED8"/>
          <text x="115" y="88" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">十年前案場：20kW</text>
          
          <g transform="translate(45, 110)" font-size="9.5" fill="#334155">
            <text y="0">・早期常規模組：250W/片</text>
            <text y="20">・總安裝片數：80 片</text>
            <text y="40">・總裝機容量：20 kW</text>
            <text y="60">・發電效率衰退：年降 1%~2%</text>
            <text y="80" font-weight="bold" fill="#1E40AF">現況：效能低落、急需更換</text>
          </g>

          <!-- 轉換箭頭 -->
          <path d="M 210 150 L 255 150" stroke="#0E8A78" stroke-width="3" marker-end="url(#arrow)"/>
          <text x="232" y="140" font-size="9" font-weight="bold" fill="#0E8A78" text-anchor="middle">全換VPC</text>

          <!-- 新案場 30kW -->
          <rect x="275" y="55" width="230" height="185" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="2"/>
          <rect x="275" y="55" width="230" height="28" rx="6" fill="#047857"/>
          <text x="390" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">全換高效模組：擴容至 30kW (+50%)</text>

          <g transform="translate(285, 98)" font-size="9.5" fill="#334155">
            <text y="0">・現代高效 VPC 模組：500W+ / 片</text>
            <text y="18">・同等屋頂面積總容量：<strong style="color:#047857;">30 kW</strong></text>
            <text y="36" font-weight="bold" fill="#0E8A78">【新制第 16 條第 2 項紅利】</text>
            <text y="52">✓ 突破原 20kW 容量限制！</text>
            <text y="68">✓ 只要台電出具「饋線容量證明」</text>
            <text y="84">✓ 免重附土地建物所有權證明！</text>
            <text y="102" font-size="9" font-weight="bold" fill="#15803D">➔ 土地與屋頂資產發電收益瞬間放大 1.5 倍！</text>
          </g>
        </svg>
        '''
    elif vtype == "dual_tariff_expansion":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">擴容換新審查路徑 ✕ 新舊雙軌費率核算機制</text>

          <!-- 雙軌費率切片圖 -->
          <g transform="translate(30, 52)">
            <rect x="0" y="0" width="480" height="95" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
            <text x="240" y="22" font-size="11" font-weight="bold" fill="#1B365D" text-anchor="middle">30kW 擴容總容量之電費雙軌結算模型</text>

            <!-- 舊容量 20kW (原費率) -->
            <rect x="20" y="38" width="280" height="42" rx="4" fill="#DBEAFE" stroke="#3B82F6"/>
            <text x="160" y="58" font-size="10" font-weight="bold" fill="#1E40AF" text-anchor="middle">原核准容量：20 kW (佔 66.7%)</text>
            <text x="160" y="72" font-size="8.5" fill="#1D4ED8" text-anchor="middle">★ 維持歷史高額躉購費率 (如 6.0 元/度)</text>

            <!-- 新增容量 10kW (新費率) -->
            <rect x="305" y="38" width="155" height="42" rx="4" fill="#FEF3C7" stroke="#F59E0B"/>
            <text x="382" y="58" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">新增容量：10 kW</text>
            <text x="382" y="72" font-size="8.5" fill="#92400E" text-anchor="middle">依完工新費率 (如 4.5 元/度)</text>
          </g>

          <!-- 下方行政簡化綠色通道 -->
          <rect x="30" y="160" width="480" height="95" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <text x="45" y="180" font-size="10.5" font-weight="bold" fill="#15803D">擴容換新免附文件與簡化程序重點：</text>
          <text x="45" y="200" font-size="9" fill="#334155">✓ 免附土地建物證明：本就在合法既有建物上，免重鑑界、免重新調閱建物與地籍謄本。</text>
          <text x="45" y="216" font-size="9" fill="#334155">✓ 超出 20kW 免審門檻部分：需補走併聯審查，由台電出具容量證明意見書。</text>
          <text x="45" y="232" font-size="8.5" fill="#64748B">（地面型水面型案場仍需出具農業主管機關同意函，完工後向地方政府完成環境備查）</text>
        </svg>
        '''
    elif vtype == "electrical_ct_upgrade":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">擴容案場電氣保護重整校核 ✕ 計量表計升級示意圖</text>

          <!-- 左側：保護重新協調 -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="28" rx="6" fill="#1D4ED8"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">責任分界點交流保護重新圖審</text>

          <g transform="translate(37, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【容量放大 ➔ 短路電流上升】</text>
            <text y="18">・發電電流自 29A 激增至 44A (以380V計)</text>
            <text y="36">・主斷路器 (NFB/VCB) 額定容量升級</text>
            <text y="54" font-weight="bold" fill="#1E40AF">保護電驛跳脫整定值重新計算：</text>
            <text y="70">・50/51 過比流保護曲線匹配</text>
            <text y="86">・59 過電壓與 27 低電壓容許區間校核</text>
            <text y="106" font-size="9" font-weight="bold" fill="#1D4ED8">➔ 確保案場故障優先跳開，不拖累台電！</text>
          </g>

          <!-- 右側：表計升級 -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#FEFCE8" stroke="#FDE047" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="28" rx="6" fill="#B45309"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">台電 CT/PT 計量表計升級規範</text>

          <g transform="translate(292, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#92400E">【防止比流器磁飽和溢位】</text>
            <text y="18">・舊案場 20kW 之 CT 規格過小</text>
            <text y="36">・電流放大若未換 CT，將引發磁飽和失真</text>
            <text y="54" font-weight="bold" fill="#92400E">台電檢驗班長換裝大型 CT：</text>
            <text y="70">・更換相匹配之高精度比流器 (CT/PT)</text>
            <text y="86">・校驗雙向四象限智慧電表</text>
            <text y="106" font-size="9" font-weight="bold" fill="#B45309">➔ 計量精確到每一度，維護發電收益！</text>
          </g>
        </svg>
        '''
    elif vtype == "mandatory_law_metric":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">新建建築物強制設置光電法源體系與計算標準</text>

          <!-- 核心指標圖卡 -->
          <g transform="translate(35, 52)">
            <rect x="0" y="0" width="470" height="85" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
            <text x="235" y="26" font-size="12" font-weight="bold" fill="#1D4ED8" text-anchor="middle">法定強制設置黃金公式</text>
            <text x="235" y="56" font-size="18" font-weight="bold" fill="#DC2626" text-anchor="middle">每 20 平方公尺 ➔ 強制設置 1 kW</text>
            <text x="235" y="74" font-size="9" fill="#64748B" text-anchor="middle">(再生能源發展條例第 12 條之 1 ✕ 國土署建築物設置太陽光電標準)</text>
          </g>

          <!-- 案例計算圖解 -->
          <g transform="translate(35, 150)">
            <rect x="0" y="0" width="225" height="100" rx="6" fill="#F0FDF4" stroke="#86EFAC"/>
            <text x="112" y="24" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">案例試算 A：1,000m² 標準廠房</text>
            <text x="112" y="48" font-size="10" fill="#334155" text-anchor="middle">建築面積 = 1,000 m² (約 302 坪)</text>
            <text x="112" y="68" font-size="12" font-weight="bold" fill="#047857" text-anchor="middle">法定容量 = 1000 / 20 = 50 kW</text>
            <text x="112" y="86" font-size="8.5" fill="#64748B" text-anchor="middle">約需安裝 90~100 片 550W 模組</text>

            <rect x="245" y="0" width="225" height="100" rx="6" fill="#FEFCE8" stroke="#FDE68A"/>
            <text x="112+245" y="24" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">案例試算 B：3,000m² 大型物流倉儲</text>
            <text x="112+245" y="48" font-size="10" fill="#334155" text-anchor="middle">屋頂面積 = 3,000 m² (約 907 坪)</text>
            <text x="112+245" y="68" font-size="12" font-weight="bold" fill="#D97706" text-anchor="middle">法定容量 = 3000 / 20 = 150 kW</text>
            <text x="112+245" y="86" font-size="8.5" fill="#64748B" text-anchor="middle">成為企業綠能資產與減碳主要來源</text>
          </g>
        </svg>
        '''
    elif vtype == "building_threshold_tree":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">強制設置太陽光電三大建築型態判定樹狀圖 (三擇一納管)</text>

          <!-- 三個入口分支 -->
          <g transform="translate(20, 52)">
            <!-- 分支 1: 新建 -->
            <rect x="0" y="0" width="160" height="135" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
            <rect x="0" y="0" width="160" height="26" rx="6" fill="#1D4ED8"/>
            <text x="80" y="18" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">型態 1：新建建築物</text>
            <g transform="translate(10, 38)" font-size="9" fill="#334155">
              <text y="0" font-weight="bold" fill="#1E40AF">判定基準：建築面積</text>
              <text y="18">達 <strong style="color:#DC2626; font-size:11px;">1,000 m² 以上</strong></text>
              <text y="36">典型對象：</text>
              <text y="50">・製造業新建廠房</text>
              <text y="64">・物流倉儲轉運中心</text>
              <text y="78">・大型購物中心賣場</text>
            </g>

            <!-- 分支 2: 增建 -->
            <rect x="170" y="0" width="160" height="135" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
            <rect x="170" y="0" width="160" height="26" rx="6" fill="#047857"/>
            <text x="250" y="18" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">型態 2：增建建築物</text>
            <g transform="translate(180, 38)" font-size="9" fill="#334155">
              <text y="0" font-weight="bold" fill="#047857">判定基準：增加建築面積</text>
              <text y="18">達 <strong style="color:#DC2626; font-size:11px;">1,000 m² 以上</strong></text>
              <text y="36">典型對象：</text>
              <text y="50">・擴建第二期廠房</text>
              <text y="64">・增建連棟鋼構倉庫</text>
              <text y="78">・廠區垂直加蓋工程</text>
            </g>

            <!-- 分支 3: 改建 -->
            <rect x="340" y="0" width="160" height="135" rx="6" fill="#FEFCE8" stroke="#F59E0B" stroke-width="1.5"/>
            <rect x="340" y="0" width="160" height="26" rx="6" fill="#B45309"/>
            <text x="420" y="18" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">型態 3：改建建築物</text>
            <g transform="translate(350, 38)" font-size="9" fill="#334155">
              <text y="0" font-weight="bold" fill="#B45309">判定基準：改建屋頂面積</text>
              <text y="18">達 <strong style="color:#DC2626; font-size:11px;">1,000 m² 以上</strong></text>
              <text y="36">典型對象：</text>
              <text y="50">・既有大樓屋頂翻修</text>
              <text y="64">・耐震結構補強改建</text>
              <text y="78">・老舊廠房屋頂全面換新</text>
            </g>
          </g>

          <!-- 匯流至強制結論 -->
          <rect x="20" y="198" width="500" height="55" rx="4" fill="#FFFFFF" stroke="#DC2626" stroke-width="1.5"/>
          <text x="270" y="220" font-size="11" font-weight="bold" fill="#B91C1C" text-anchor="middle">三者符合任意一項 ➔ 無條件強制設置太陽光電發電設備！</text>
          <text x="270" y="240" font-size="9" fill="#64748B" text-anchor="middle">（未依圖說施工完竣者，建築主管機關一律暫緩核發使用執照）</text>
        </svg>
        '''
    elif vtype == "exemption_matrix":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">強制光電三大合法豁免/核減機制 ✕ 暫緩實施類別對照</text>

          <!-- 三大豁免機制 -->
          <g transform="translate(20, 52)">
            <rect x="0" y="0" width="155" height="120" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="77" y="20" font-size="10.5" font-weight="bold" fill="#1E40AF" text-anchor="middle">1. 台電容量不足核減</text>
            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0">・需設 50kW 但饋線剩 10kW</text>
              <text y="14">・台電出具「容量瓶頸公文」</text>
              <text y="30" font-weight="bold" fill="#1D4ED8">➔ 得依台電容量設置 (10kW)</text>
              <text y="46">  免受 20m²/kW 限制！</text>
              <text y="62" fill="#64748B">實事求是、不強人所難</text>
            </g>

            <rect x="172" y="0" width="155" height="120" rx="6" fill="#F0FDF4" stroke="#10B981"/>
            <text x="250" y="20" font-size="10.5" font-weight="bold" fill="#047857" text-anchor="middle">2. 特殊構造經審免設</text>
            <g transform="translate(180, 38)" font-size="8.5" fill="#334155">
              <text y="0">・寺廟/教堂等特殊斜頂</text>
              <text y="14">・氣象局雷達/電信通訊站</text>
              <text y="28">・直升機停機坪急救醫院</text>
              <text y="46" font-weight="bold" fill="#047857">➔ 經建築主管機關認定</text>
              <text y="62">  得「全額免除設置」！</text>
            </g>

            <rect x="345" y="0" width="155" height="120" rx="6" fill="#FEFCE8" stroke="#F59E0B"/>
            <text x="422" y="20" font-size="10.5" font-weight="bold" fill="#B45309" text-anchor="middle">3. 全自發自用不轉售</text>
            <g transform="translate(353, 38)" font-size="8.5" fill="#334155">
              <text y="0">・電網完全無容量併網時</text>
              <text y="14">・業者可選「自發自用」</text>
              <text y="28">・安裝逆送防止裝置 (雙CT)</text>
              <text y="46" font-weight="bold" fill="#B45309">➔ 不送電入網免排饋線</text>
              <text y="62">  直接供應廠內自耗電！</text>
            </g>
          </g>

          <!-- 下方暫緩實施對照 (2026/08/06 前) -->
          <rect x="20" y="180" width="500" height="75" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
          <text x="35" y="200" font-size="10.5" font-weight="bold" fill="#B91C1C">⚠️ 2026 年 8 月 6 日前「暫不實施」之兩大類別（暫緩推行）：</text>
          <text x="35" y="220" font-size="9" fill="#334155">① G3 類（辦公服務類小型店面、門市零售等小型商業建築物）</text>
          <text x="35" y="238" font-size="9" fill="#334155">② H 類住宿類（包括短期招待所與長期集合住宅公寓大樓，因多住戶管委會產權營運複雜，暫緩推行）</text>
        </svg>
        '''
    elif vtype == "cns_wind_safety":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">CNS 61215 機械負載 5400Pa 測試 ✕ 屋頂工安三防架構</text>

          <!-- 左側：抗風負載 -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="28" rx="6" fill="#1D4ED8"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">結構抗風：CNS 61215 測試</text>

          <g transform="translate(37, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【法定強制機械強度報告】</text>
            <text y="18">・靜態機械負載：正負向荷重</text>
            <text y="34" font-size="13" font-weight="bold" fill="#DC2626">  5,400 Pa 實驗報告</text>
            <text y="52">・等同可承受 17 級強烈颱風風壓</text>
            <text y="68">・防止模組表面玻璃與背板破裂</text>
            <text y="86">・防止強風掀翻掀落砸傷行人建物</text>
            <text y="106" font-size="9" font-weight="bold" fill="#1D4ED8">➔ 報告未滿 5 年 400 方者不得採用！</text>
          </g>

          <!-- 右側：屋頂工安防護 -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="28" rx="6" fill="#047857"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">維運工安：屋頂永久性設施</text>

          <g transform="translate(292, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#047857">【第 2 條第 4 款強制項目】</text>
            <text y="18">① 專用維護爬梯：附安全防墜背籠</text>
            <text y="36">② 永久走道板通道：嚴禁踩踏採光罩</text>
            <text y="54">③ 屋頂邊緣安全防護欄杆 (高>1.1m)</text>
            <text y="74" font-weight="bold" fill="#B45309">職安署聯手把關：</text>
            <text y="90">未設置通道欄杆之建築物竣工驗收時，</text>
            <text y="106" font-size="9" font-weight="bold" fill="#DC2626">一律列為嚴重缺失暫緩給照！</text>
          </g>
        </svg>
        '''
    elif vtype == "island_microgrid":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">市電斷電實體隔離 (ATS) ✕ 建築內線孤島微電網運轉拓撲</text>

          <!-- 左側：台電電網 (市電斷電) -->
          <rect x="25" y="60" width="115" height="100" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
          <text x="82" y="85" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">台電外部電網</text>
          <text x="82" y="105" font-size="10" font-weight="bold" fill="#B91C1C" text-anchor="middle">⚡ 0V 市電斷電</text>
          <text x="82" y="125" font-size="8.5" fill="#64748B" text-anchor="middle">線路搶修中</text>

          <!-- 中間：ATS 自動隔離切換開關 -->
          <rect x="175" y="60" width="115" height="100" rx="6" fill="#FEFCE8" stroke="#F59E0B" stroke-width="2"/>
          <text x="232" y="85" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">ATS 切換開關</text>
          <text x="232" y="105" font-size="9.5" font-weight="bold" fill="#DC2626" text-anchor="middle">【實體物理隔離】</text>
          <text x="232" y="125" font-size="8" fill="#B45309" text-anchor="middle">嚴禁逆送電至外網</text>
          <text x="232" y="140" font-size="8" fill="#15803D" font-weight="bold" text-anchor="middle">轉入內線孤島運轉</text>

          <line x1="140" y1="110" x2="175" y2="110" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
          <line x1="290" y1="110" x2="325" y2="110" stroke="#10B981" stroke-width="3"/>

          <!-- 右側：建築物屋頂光電與微電網 -->
          <rect x="325" y="50" width="190" height="120" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="2"/>
          <text x="420" y="72" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">建築物自立微電網</text>
          <g transform="translate(335, 90)" font-size="9" fill="#334155">
            <text y="0">・屋頂太陽能板持續發電</text>
            <text y="16">・儲能 (BESS) / 發電機建壓</text>
            <text y="32">・優先供電：緊急照明、電梯、</text>
            <text y="48">  抽水泵、消防設備與電腦機房</text>
            <text y="66" font-weight="bold" fill="#047857">➔ 大停電時建築維生系統不中斷！</text>
          </g>

          <!-- 下方安全鐵律 -->
          <rect x="25" y="185" width="490" height="70" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="35" y="205" font-size="10.5" font-weight="bold" fill="#1B365D">國土署與台電安全鐵律：</text>
          <text x="35" y="223" font-size="9" fill="#334155">① 實體切離保障人命：斷電時光電必須在毫秒級實體切離外網，避免逆送高壓電擊搶修線路之台電工班。</text>
          <text x="35" y="239" font-size="9" fill="#334155">② 孤島自立運轉：結合儲能或發電機建立頻率電壓參考點，使建築物在災時具備 24~48 小時維生自給能力。</text>
        </svg>
        '''
    elif vtype == "internal_distribution":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">光電併入建築內線配電盤分流與階梯架構</text>

          <!-- 建築主盤與分盤架構 -->
          <g transform="translate(30, 52)">
            <rect x="0" y="0" width="130" height="90" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="65" y="22" font-size="10" font-weight="bold" fill="#1E40AF" text-anchor="middle">屋頂光電發電盤</text>
            <text x="65" y="42" font-size="8.5" fill="#334155" text-anchor="middle">50kW 逆變器輸出</text>
            <text x="65" y="58" font-size="8.5" fill="#334155" text-anchor="middle">獨立隔離分盤</text>
            <text x="65" y="74" font-size="8" fill="#64748B" text-anchor="middle">(支援初期試車用電)</text>

            <path d="M 130 45 L 175 45" stroke="#3B82F6" stroke-width="2"/>

            <rect x="175" y="0" width="130" height="90" rx="4" fill="#FEFCE8" stroke="#F59E0B"/>
            <text x="240" y="22" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">公共設施主受電盤</text>
            <text x="240" y="42" font-size="8.5" fill="#334155" text-anchor="middle">具備 ATS 切換機制</text>
            <text x="240" y="58" font-size="8.5" fill="#334155" text-anchor="middle">常態與市電併聯</text>
            <text x="240" y="74" font-size="8" fill="#64748B" text-anchor="middle">異常時轉供內部</text>

            <path d="M 305 45 L 350 45" stroke="#F59E0B" stroke-width="2"/>

            <rect x="350" y="0" width="130" height="90" rx="4" fill="#F0FDF4" stroke="#10B981"/>
            <text x="415" y="22" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">緊急用電優先迴路</text>
            <text x="415" y="42" font-size="8.5" fill="#047857" text-anchor="middle">① 維生電梯 / 抽水泵</text>
            <text x="415" y="58" font-size="8.5" fill="#047857" text-anchor="middle">② 消防排煙 / 照明</text>
            <text x="415" y="74" font-size="8.5" fill="#047857" text-anchor="middle">③ 機房通訊不斷電</text>
          </g>

          <!-- 下方設計建議說明 -->
          <rect x="30" y="160" width="480" height="95" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="45" y="180" font-size="10.5" font-weight="bold" fill="#1B365D">吳課長工程規劃實戰提示：</text>
          <text x="45" y="200" font-size="9" fill="#334155">1. 獨立光電盤設計：在建築物本體尚未正式送電前，光電盤必須能配合「試車用電」獨立啟動送電測試。</text>
          <text x="45" y="216" font-size="9" fill="#334155">2. 優先並接公設緊急盤：停電時自發自用電力不應分散至一般插座，應集中給公共維生設備，創造最大抗災價值。</text>
          <text x="45" y="232" font-size="8.5" fill="#64748B">（若外線無容量，亦可申請全自發自用不轉售，直接將電力消耗於內部負載，免除饋線排隊）</text>
        </svg>
        '''
    elif vtype == "license_interlock_loop":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">建照與使照連鎖綁定光電審驗閉環流程圖</text>

          <!-- 關卡 1: 建照掛號 -->
          <rect x="25" y="55" width="225" height="185" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="25" y="55" width="225" height="28" rx="6" fill="#1D4ED8"/>
          <text x="137" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第一道卡控：申請建築執照 (建照)</text>

          <g transform="translate(37, 98)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【法定檢附文件二擇一】</text>
            <text y="18">① 依規範繪製之「光電設置圖說」</text>
            <text y="34">   (含每 20m² 設 1kW 結構抗風圖)</text>
            <text y="54">② 合法減免證明公文：</text>
            <text y="70">   ・台電出具「饋線容量不足證明」</text>
            <text y="86">   ・建築主管機關「特殊用途免設函」</text>
            <text y="110" font-size="9" font-weight="bold" fill="#DC2626">➔ 未檢附上述文件，建照一律不予核發！</text>
          </g>

          <!-- 箭頭 -->
          <path d="M 255 145 L 280 145" stroke="#CBD5E1" stroke-width="3"/>

          <!-- 關卡 2: 使照掛號 -->
          <rect x="285" y="55" width="225" height="185" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
          <rect x="285" y="55" width="225" height="28" rx="6" fill="#047857"/>
          <text x="397" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第二道卡控：申請使用執照 (使照)</text>

          <g transform="translate(297, 98)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#047857">【法定檢附完工證明文件】</text>
            <text y="18">① 發電業「工作許可證」</text>
            <text y="34">   (主管機關允許施工函)</text>
            <text y="54">② 3 年內有效之「同意備案證明」</text>
            <text y="74" font-weight="bold" fill="#B45309">建商交屋死穴：</text>
            <text y="90">光電未完工 ➔ 拿不到使用執照 ➔</text>
            <text y="106">無法辦理保存登記與產權過戶交屋！</text>
            <text y="122" font-size="9" font-weight="bold" fill="#15803D">➔ 倒逼建商如期如質完成光電！</text>
          </g>
        </svg>
        '''
    elif vtype == "two_inspection_sop":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電檢驗班長「兩次到場檢驗送電」標準作業程序</text>

          <!-- 第 1 趟：發電 -->
          <rect x="25" y="55" width="235" height="135" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="25" y="55" width="235" height="28" rx="6" fill="#1D4ED8"/>
          <text x="142" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第 1 趟：光電發電設備檢驗送電</text>
          <g transform="translate(37, 95)" font-size="9" fill="#334155">
            <text y="0">・對象：屋頂光電系統、逆變器與分界點開關</text>
            <text y="16">・重點：核校保護電驛整定、相序與絕緣阻抗</text>
            <text y="32">・動作：現場裝設發電專用雙向計量電表</text>
            <text y="48" font-weight="bold" fill="#0E8A78">・成果：台電正式核發「併聯完成函」</text>
            <text y="64" font-size="8.5" fill="#1E40AF">業者憑函向地方政府換取「發電設備登記」</text>
          </g>

          <!-- 第 2 趟：用電 -->
          <rect x="280" y="55" width="235" height="135" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
          <rect x="280" y="55" width="235" height="28" rx="6" fill="#047857"/>
          <text x="397" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第 2 趟：建築物整體用電檢驗送電</text>
          <g transform="translate(292, 95)" font-size="9" fill="#334155">
            <text y="0">・前置：業者需繳驗「使用執照 ＋ 設備登記」</text>
            <text y="16">・對象：建築物本體受電室、主配電盤與公共線路</text>
            <text y="32">・動作：現場裝設建築物本體一般用電電表</text>
            <text y="48" font-weight="bold" fill="#15803D">・成果：建築物正式通電投用！</text>
            <text y="64" font-size="8.5" fill="#047857">光電未先送電，大樓絕不給通電！</text>
          </g>

          <!-- 下方核心結論 -->
          <rect x="25" y="200" width="490" height="55" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="270" y="222" font-size="10.5" font-weight="bold" fill="#1B365D" text-anchor="middle">「先發電、後用電，班長跑兩趟」行政鐵律：</text>
          <text x="270" y="240" font-size="9" fill="#64748B" text-anchor="middle">從程序上徹底鎖死建商逃避責任的空間，確保建築物正式投用前，太陽光電已百分之百通電運轉！</text>
        </svg>
        '''
    elif vtype == "inverter_outage_loss":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">變流器故障舊制停機公文流程 ✕ 每日發電損失累積痛點</text>

          <!-- 舊制漫長流程圖 (左側) -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="28" rx="6" fill="#DC2626"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">舊制事前審查冗長路徑 (耗時2個月)</text>

          <g transform="translate(37, 95)" font-size="9" fill="#334155">
            <text y="0">1. 變流器燒毀故障停機</text>
            <text y="16">2. 發函台電區處申請更換</text>
            <text y="32">3. 重新辦理細部協商圖面審查</text>
            <text y="48">4. 辦理供電合約變更修約</text>
            <text y="64">5. 台電發文核准始准動工採購換裝</text>
            <text y="82" font-weight="bold" fill="#DC2626">停機時間：長達 45 ～ 60 天！</text>
            <text y="98" fill="#B91C1C">好天氣無法發電，業主只能乾著急！</text>
          </g>

          <!-- 損失測算圖 (右側) -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#FEFCE8" stroke="#FDE68A" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="28" rx="6" fill="#D97706"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">100kW 案場停機損失震撼測算</text>

          <g transform="translate(292, 95)" font-size="9.5" fill="#334155">
            <text y="0">・日照良好夏日 (每日4.2度/kW)：</text>
            <text y="16">  每日發電量 = 100kW × 4.2 = 420 度</text>
            <text y="34">・躉購費率 5.0 元/度：</text>
            <text y="50" font-weight="bold" fill="#B45309">  每日損失 = 420 × 5 = 2,100 元/天</text>
            <text y="70">・停機 60 天累積發電損失：</text>
            <text y="88" font-size="13" font-weight="bold" fill="#DC2626">  高達 126,000 元！</text>
            <text y="108" font-size="8.5" fill="#64748B">相當於白白吃掉案場全年維運利潤！</text>
          </g>
        </svg>
        '''
    elif vtype == "inverter_fast_track":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">第三型光電變流器簡化更換程序 (先換後備查 SOP)</text>

          <!-- 舊制 vs 新制流程對比 -->
          <g transform="translate(25, 52)">
            <!-- 舊制 -->
            <rect x="0" y="0" width="235" height="120" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
            <text x="117" y="22" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">✕ 舊制：事前審查 (停機 60 天)</text>
            <g transform="translate(15, 42)" font-size="8.5" fill="#334155">
              <text y="0">故障 ➔ 申請 ➔ 圖審 ➔ 修約 ➔ 核准 ➔ 採購 ➔ 更換</text>
              <text y="20" font-weight="bold" fill="#B91C1C">停機損失巨大，行政手續窒息僵化！</text>
              <text y="40" fill="#64748B">公文往返期間案場無法發出一度電</text>
            </g>

            <!-- 新制 -->
            <rect x="255" y="0" width="235" height="120" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
            <text x="372" y="22" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">✓ 新制：先換後備查 (停機 1~2 天)</text>
            <g transform="translate(270, 42)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#047857">故障 ➔ 立即 1:1 換裝 ➔ 恢復發電 ➔ 拍照備查</text>
              <text y="20" font-weight="bold" fill="#15803D">台電原則同意先斬後奏，快速止血！</text>
              <text y="40" fill="#64748B">事後台電現場抽檢銘牌規格無誤即備查結案</text>
            </g>
          </g>

          <!-- 下方新制適用三前提 -->
          <rect x="25" y="182" width="490" height="75" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <text x="35" y="202" font-size="10.5" font-weight="bold" fill="#1D4ED8">「先換後報備」快車道之三大剛性前提（缺一不可）：</text>
          <text x="35" y="220" font-size="9" fill="#334155">① 容量完全相同：原 20kW 變流器僅能更換為同等 20kW 設備，不可私自增減容量。</text>
          <text x="35" y="236" font-size="9" fill="#334155">② 相序完全相同：原三相變流器限換三相設備，嚴禁換成單相；內部保險規格亦需完全相符。</text>
        </svg>
        '''
    elif vtype == "inverter_decision_tree":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">變流器更換快車道 vs 常規道判定決策樹</text>

          <!-- 頂部問題點 -->
          <rect x="180" y="52" width="180" height="35" rx="4" fill="#1B365D"/>
          <text x="270" y="74" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">變流器損壞更換需求</text>

          <!-- 判定問題 -->
          <path d="M 270 87 L 270 105" stroke="#CBD5E1" stroke-width="2"/>
          <rect x="135" y="105" width="270" height="35" rx="4" fill="#FEFCE8" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="270" y="127" font-size="10" font-weight="bold" fill="#B45309" text-anchor="middle">容量、相序、保護規格是否 100% 相同？</text>

          <!-- 是 (走快車道) -->
          <path d="M 135 122 L 80 122 L 80 160" stroke="#10B981" stroke-width="2"/>
          <text x="95" y="142" font-size="9" font-weight="bold" fill="#15803D">是 (1:1等額)</text>
          <rect x="20" y="160" width="220" height="90" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="2"/>
          <text x="130" y="180" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">走快車道：先換後備查</text>
          <g transform="translate(30, 198)" font-size="8.5" fill="#334155">
            <text y="0">✓ 即刻更換復電發電</text>
            <text y="14">✓ 檢附型錄照片發函報備台電</text>
            <text y="28">✓ 現場抽核通過即核准備查</text>
            <text y="44" font-weight="bold" fill="#047857">➔ 停機時間 < 48 小時！</text>
          </g>

          <!-- 否 (走常規道) -->
          <path d="M 405 122 L 460 122 L 460 160" stroke="#DC2626" stroke-width="2"/>
          <text x="425" y="142" font-size="9" font-weight="bold" fill="#DC2626">否 (規格變更)</text>
          <rect x="300" y="160" width="220" height="90" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="410" y="180" font-size="11" font-weight="bold" fill="#B91C1C" text-anchor="middle">走常規道：事前圖審修約</text>
          <g transform="translate(310, 198)" font-size="8.5" fill="#334155">
            <text y="0">・涉及三相換單相或加大容量</text>
            <text y="14">・必須重新向檢驗課送細部協商</text>
            <text y="28">・核准並修約後始得動工更換</text>
            <text y="44" font-weight="bold" fill="#B91C1C">➔ 避免三相不平衡與保險拒賠！</text>
          </g>
        </svg>
        '''
    elif vtype == "ten_commandments_c5":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="30" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電併網審查、工程擴容與維運實戰十條軍規檢核表</text>

          <!-- 三大模塊排布 -->
          <!-- 模塊 1: 時效與審查 (3條) -->
          <g transform="translate(15, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#1D4ED8"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">時效防禦篇 (軍規 1-3)</text>
            
            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#1E40AF">軍規 1：備案 2 個月內簽約</text>
              <text y="14" fill="#64748B">逾期撤銷備案，時程嚴加倒排</text>
              <text y="36" font-weight="bold" fill="#1E40AF">軍規 2：簽約 1 年內完工登記</text>
              <text y="50" fill="#64748B">超期失效重審，費率直接腰斬</text>
              <text y="72" font-weight="bold" fill="#1E40AF">軍規 3：掛表即核完成函</text>
              <text y="86" fill="#64748B">前送電度數於首期電費補發結清</text>
              <text y="108" font-weight="bold" fill="#1E40AF">軍規 4：圖審專注交流側</text>
              <text y="122" fill="#64748B">責任分界保護嚴整，不拖累外網</text>
              <text y="146" font-size="8" fill="#1D4ED8">嚴守法定公文時效節點</text>
            </g>
          </g>

          <!-- 模塊 2: 擴容與新建 (3條) -->
          <g transform="translate(187, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#FEFCE8" stroke="#FBBF24" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#D97706"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">擴容與法規篇 (軍規 5-7)</text>

            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#B45309">軍規 5：全換 VPC 破上限</text>
              <text y="14" fill="#64748B">原場址擴容增產，免重附權狀</text>
              <text y="36" font-weight="bold" fill="#B45309">軍規 6：新建千坪每20m²設1k</text>
              <text y="50" fill="#64748B">建照使照連鎖綁定，預留結構</text>
              <text y="72" font-weight="bold" fill="#B45309">軍規 7：容量不足出具證明</text>
              <text y="86" fill="#64748B">憑台電公文合法下修免受罰</text>
              <text y="108" font-weight="bold" fill="#B45309">軍規 8：斷電實體切離 ATS</text>
              <text y="122" fill="#64748B">轉入內線孤島運轉，絕不逆送</text>
              <text y="146" font-size="8" fill="#B45309">搶佔政策紅利與合規防線</text>
            </g>
          </g>

          <!-- 模塊 3: 運維與更換 (4條) -->
          <g transform="translate(360, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#F0FDF4" stroke="#4ADE80" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#16A34A"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">運維更換篇 (軍規 9-10)</text>

            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#15803D">軍規 9：先發後用跑兩趟</text>
              <text y="14" fill="#64748B">台電先驗光電通電，再驗大樓用電</text>
              <text y="36" font-weight="bold" fill="#15803D">軍規 10：等額先換後報備</text>
              <text y="50" fill="#64748B">1:1容量相序相同先斬後奏止血</text>
              <text y="72" font-weight="bold" fill="#15803D">加碼：改容量回歸圖審</text>
              <text y="86" fill="#64748B">嚴禁單三相偷換，防保險拒賠</text>
              <text y="108" font-weight="bold" fill="#15803D">加碼：擴容同步升級 CT</text>
              <text y="122" fill="#64748B">防比流器磁飽和，度數顆顆入袋</text>
              <text y="146" font-size="8" fill="#16A34A">守護二十年資產穩定發電</text>
            </g>
          </g>
        </svg>
        '''
    else:
        return f'<div style="padding:20px; text-align:center; color:#64748B;">{vtype} visual placeholder</div>'

slides_html = []
for s in slides_data:
    sn = s["slideNo"]
    act_cls = "active" if sn == 1 else ""
    hl_items = "".join([f'<li class="highlight-item">{h}</li>' for h in s["highlights"]])
    visual_body = make_visual_body(s["visualType"])
    
    sh = f'''
      <!-- ==========================================
           SLIDE {sn}
           ========================================== -->
      <section class="slide-item {act_cls}" data-slide="{sn}"
        data-note-takeaway="{s["noteTakeaway"]}"
        data-note-detail="{s["noteDetail"]}"
        data-note-transition="{s["noteTransition"]}">
        <div class="slide-header">
          <div class="slide-tracker">
            <span class="module-badge">{s["module"]}</span>
            <span class="source-ref-badge">{s["ref"]}</span>
          </div>
          <h2 class="slide-action-title">{s["title"]}</h2>
        </div>
        <div class="slide-body slide-split-2col">
          <div class="insight-panel">
            <div class="core-question-block">
              <div class="block-title">📌 本章要解決的問題／核心論點</div>
              <div class="block-desc">{s["question"]}</div>
            </div>
            <ul class="highlights-list">
              {hl_items}
            </ul>
            <div class="takeaway-banner">
              {s["takeaway"]}
            </div>
          </div>
          <div class="visual-panel">
            <div class="diagram-header">
              <span>{s["visualTitle"]}</span>
              <span class="badge badge-gold">進金生能源 6692</span>
            </div>
            <div class="diagram-body" style="width:100%;">
              {visual_body}
            </div>
            <div class="source-handout-thumb">
              <div class="thumb-preview-wrap open-lightbox-trigger" data-img-src="{s["thumbImg"]}" data-caption="{s["thumbCaption"]}">
                <img src="{s["thumbImg"]}" alt="{s["thumbLabel"]}">
              </div>
              <div class="thumb-info">
                <div>原廠講義：<strong>{s["thumbLabel"]}</strong></div>
                <button type="button" class="open-lightbox-trigger" data-img-src="{s["thumbImg"]}">點擊放大原圖 ↗</button>
              </div>
            </div>
          </div>
        </div>
        <div class="slide-footer">
          <div class="footer-meta">
            <span class="footer-brand-tag">ACMEPOINT 6692 ✕ 台電併網與政策</span>
            <span>頁碼：{sn:02d} / 20</span>
          </div>
          <div class="footer-keys-tip">按 N 鍵呼出講稿 ｜ ← / → 換頁 ｜ F 全螢幕 ｜ G 總覽</div>
        </div>
      </section>
    '''
    slides_html.append(sh)

full_html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>太陽光電設置乙級技術士回訓課程——光電併網與相關政策趨勢｜麥肯錫風格專業簡報</title>
  <link rel="stylesheet" href="../assets/css/deck.css">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="deck-view">

  <!-- Top App Bar -->
  <header class="deck-topbar">
    <div class="topbar-left">
      <a href="../index.html" class="back-home-btn">
        <span>← 返回知識庫首頁</span>
      </a>
      <div class="deck-title-mini">
        <strong>進金生能源 6692</strong> ｜ 太陽光電設置乙級技術士回訓課程——光電併網與相關政策趨勢
      </div>
    </div>
    <div class="topbar-center">
      <div class="slide-counter" id="slide-counter-text">1 / 20</div>
    </div>
    <div class="topbar-right">
      <button class="tool-btn" id="notes-toggle-btn" title="開啟/關閉講者備忘錄 (按 N)">
        <span>📝 講稿備忘 (N)</span>
      </button>
      <button class="tool-btn" id="overview-toggle-btn" title="投影片總覽 (按 G)">
        <span>⊞ 總覽 (G)</span>
      </button>
      <button class="tool-btn" id="fullscreen-btn" title="全螢幕模式 (按 F)">
        <span>⛶ 全螢幕 (F)</span>
      </button>
      <button class="tool-btn" id="print-btn" title="列印/匯出 PDF (按 P)">
        <span>🖨 列印 PDF</span>
      </button>
    </div>
  </header>

  <!-- Workspace Canvas -->
  <main class="deck-workspace">
    <button class="deck-nav-btn nav-prev" id="deck-prev-btn" title="上一頁 (← / Backspace)">‹</button>
    <button class="deck-nav-btn nav-next" id="deck-next-btn" title="下一頁 (→ / Space)">›</button>

    <div class="slide-canvas" id="slide-canvas">
      <div class="deck-progress-bar" id="deck-progress-bar"></div>
      {"".join(slides_html)}
    </div>
  </main>

  <!-- Speaker Notes Drawer (Toggled by 'N') -->
  <aside class="speaker-notes-drawer" id="speaker-notes-drawer">
    <div class="notes-header">
      <div class="notes-title">
        <span>🎙 麥肯錫顧問風格 3 段式講者備忘錄 (Speaker Notes)</span>
        <span style="font-size:0.75rem; color:#94A3B8; font-weight:normal;">按 N 鍵或點擊右側 × 關閉</span>
      </div>
      <button class="notes-close-btn" id="notes-close-btn" title="關閉備忘錄">&times;</button>
    </div>
    <div class="notes-content-grid">
      <div class="notes-col">
        <div class="notes-col-label">① 本頁核心結論 (Takeaway)</div>
        <div class="notes-col-body" id="notes-col-takeaway">
          本頁重點：依規範嚴格落實。
        </div>
      </div>
      <div class="notes-col">
        <div class="notes-col-label">② 補充說明與數據佐證 (Field Note & Data)</div>
        <div class="notes-col-body" id="notes-col-detail">
          實務數據與補充說明：詳見相關技術手冊。
        </div>
      </div>
      <div class="notes-col">
        <div class="notes-col-label">③ 下一步 / 轉場提示 (Transition)</div>
        <div class="notes-col-body" id="notes-col-transition">
          下一頁重點：進入下一核心環節。
        </div>
      </div>
    </div>
  </aside>

  <!-- Overview Grid Modal (Toggled by 'G') -->
  <div class="overview-modal" id="overview-modal">
    <div class="overview-header">
      <h2>⊞ 全簡報 20 頁投影片總覽導航</h2>
      <button class="tool-btn" id="overview-close-btn">關閉總覽 (Esc)</button>
    </div>
    <div class="overview-grid" id="overview-grid"></div>
  </div>

  <!-- Lightbox Modal for Original Handout Images -->
  <div class="lightbox-modal" id="lightbox-modal">
    <button class="lightbox-close-btn" id="lightbox-close-btn">&times;</button>
    <div class="lightbox-content">
      <img id="lightbox-img" src="" alt="講義原圖放大">
      <div class="lightbox-caption" id="lightbox-caption">原版乙級回訓實體講義投影片對照</div>
    </div>
  </div>

  <script src="../assets/js/deck.js"></script>
</body>
</html>
'''

with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated {out_path} successfully with all 20 slides!")
