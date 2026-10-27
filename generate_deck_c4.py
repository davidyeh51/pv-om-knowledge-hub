# -*- coding: utf-8 -*-
import os

out_dir = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\courses"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "green-power-trading-trec.html")

slides_data = [
    {
        "slideNo": 1,
        "module": "MODULE 1 ｜ 綠電憑證本質與國際範疇",
        "ref": "講義對照 P.01 ｜ 錄音 00:00~05:07",
        "title": "綠電憑證 (T-REC) 核心本質：唯一官方綠電身分證，轉讓一次為限且採全生命週期電子溯源",
        "question": "電子注入電網無法區分顏色，綠電如何被證明？T-REC 為何被賦予「唯一官方、轉讓一次、電子化」三大特質？",
        "highlights": [
            "<strong>電網同質化困境：</strong>電網傳輸的電子物理上無法分辨綠、灰或白，唯有經濟部標檢局再生能源憑證中心（T-REC）核發之憑證能作為法定身分證。",
            "<strong>轉讓一次為限（非股票）：</strong>T-REC 嚴禁重複轉手炒作或囤積，僅能在憑證中心專屬帳號間由賣方移轉給買方一次，隨後鎖定宣告註銷。",
            "<strong>產銷履歷式溯源機制：</strong>採全電子化發行，記載電廠、發電時段與防偽編號，實現自發電端至用電端之全生命週期嚴格溯源與零重複計算。"
        ],
        "takeaway": "T-REC 是兼具唯一官方背書與單次轉讓防偽的綠電身分證，是企業跨越國際綠色供應鏈門檻的法定通行證。",
        "visualTitle": "T-REC 電子身分證與單次移轉生命週期拓撲圖",
        "visualType": "trec_lifecycle",
        "thumbImg": "../assets/images/slides/slide_01.jpg",
        "thumbCaption": "講義 P.01：再生能源憑證制度法源與核心精神",
        "thumbLabel": "P.01 憑證法源精神",
        "noteTakeaway": "本堂課由標檢局張彥堂科長主講，開宗明義定調憑證就是綠電的電子身分證，只能轉讓一次。",
        "noteDetail": "憑證不是股票，不可重複買賣交易；買賣雙方都在憑證中心有專屬帳號，由發電端移轉至用電端後即行鎖定，供企業作 ESG 或減碳宣告。",
        "noteTransition": "搞懂了憑證的身分證本質後，國際 RE100 倡議到底承認哪些能源？請看第二頁 RE100 邊界判定。"
    },
    {
        "slideNo": 2,
        "module": "MODULE 1 ｜ 國際 RE100 範疇邊界",
        "ref": "講義對照 P.02 ｜ 錄音 05:07~06:56",
        "title": "國際 RE100 準則正面表列「風光水地生」：廢棄物不認可、抽蓄水力屬儲能、氫能僅為載體",
        "question": "國際倡議與台灣法規在再生能源定義上有何關鍵落差？廢棄物發電、抽蓄水力與氫能為何被排除於綠電之外？",
        "highlights": [
            "<strong>RE100 正面表列五大綠能：</strong>風力、太陽光電、水力（非抽蓄）、地熱、生質能；國內法規正面表列與國際倡議高度接軌。",
            "<strong>廢棄物發電的國際排斥：</strong>台灣再生能源發展條例雖列入廢棄物發電，但國際 RE100 嚴格不認可，且其碳排係數非為 0！",
            "<strong>抽蓄與氫能之工程正名：</strong>抽蓄水力係用位能調峰，本質屬「儲能」；氫能目前僅為「二次能源載體」，非原生再生能源。"
        ],
        "takeaway": "企業採購綠電切忌盲信「只要法規列入就通用」，必須以 RE100 五大正面表列為採購唯一判準，避免海外供應鏈審計觸礁。",
        "visualTitle": "國際 RE100 認可五大綠能 vs 排除/爭議能源範疇矩陣",
        "visualType": "re100_matrix",
        "thumbImg": "../assets/images/slides/slide_02.jpg",
        "thumbCaption": "講義 P.02：國際再生能源範疇認定與 RE100 規則",
        "thumbLabel": "P.02 RE100 範疇",
        "noteTakeaway": "張科長特別提醒：風光水地生是國際通用綠能，但廢棄物、抽蓄水力與氫能千萬不要混為一談。",
        "noteDetail": "抽蓄水力是先把水抽上去、要用時放下來，那是儲能；氫能只是能量載體；廢棄物發電雖然台灣條例認，但 RE100 嚴格不認，買了無法通過跨國大廠稽核。",
        "noteTransition": "明確了綠能範疇後，如何申請 T-REC 憑證？有哪些絕對紅線？請看第三頁申辦要件與排除對象。"
    },
    {
        "slideNo": 3,
        "module": "MODULE 1 ｜ 憑證申請與排除對象",
        "ref": "講義對照 P.03 ｜ 錄音 06:56~09:18",
        "title": "申請 T-REC 必備「設備登記與併網契約」：台電 FIT 躉購與環境部碳抵換專案絕對排除",
        "question": "電廠如何向憑證中心立案申請發證？哪兩大類發電主體受法律明定「絕對排除」於憑證申請資格之外？",
        "highlights": [
            "<strong>兩大前置法定要件：</strong>電廠必須先取得能源署或地方政府核發之「設備登記證明文件」＋完成與台電之「併聯供電契約」。",
            "<strong>第三方查驗與帳號開立：</strong>送交官方認可查驗機構完成現場查核，通過後憑證中心即行開立專屬帳號並按月發證。",
            "<strong>兩大絕對排除主體：</strong>凡已參加台電保證收購（FIT 躉購）機制、或已參加環境部溫室氣體減量抵換專案者，法律明定禁發憑證！"
        ],
        "takeaway": "申辦 T-REC 必須嚴格備齊登記函與併網約，且嚴守「不得重複享有 FIT 補貼或碳抵換」的合規單一性原則。",
        "visualTitle": "T-REC 申請四步標準作業流程與兩大法律排除紅線",
        "visualType": "apply_process",
        "thumbImg": "../assets/images/slides/slide_03.jpg",
        "thumbCaption": "講義 P.03：憑證申請流程圖與資格審查重點",
        "thumbLabel": "P.03 申請流程要件",
        "noteTakeaway": "發電業申請憑證必須具備登記函與併網約；凡是拿台電躉購補貼或去環境部換碳權的，一律排除發證。",
        "noteDetail": "雙重獲益是國際法規大忌。拿了台電 20 年固定躉購電價，就不能再拿綠電身分證去市場賣錢；參加環境部碳抵換專案亦同。",
        "noteTransition": "憑證取得後如何用於企業減碳宣告？歐盟 CBAM 又如何看待？請看第四頁碳排盤查與 CBAM 解密。"
    },
    {
        "slideNo": 4,
        "module": "MODULE 1 ｜ 碳排盤查與歐盟 CBAM",
        "ref": "講義對照 P.04 ｜ 錄音 15:25~19:54",
        "title": "範疇二碳排算式：光電憑證碳排係數為 0，歐盟 CBAM 認 PPA 合約而非純憑證",
        "question": "企業持有 T-REC 在範疇二碳排盤查中如何精確抵扣？面對歐盟 CBAM 碳關稅，純綠電憑證為何常被拒收？",
        "highlights": [
            "<strong>範疇二精確扣抵公式：</strong>風光水地熱 T-REC 碳排係數按 0 計算（企業用電 2000 度若持 1000 度光電憑證，碳排直接砍半）。",
            "<strong>生質能碳排係數非為 0：</strong>生質能發電仍具微量碳排，盤查時需向發電端另外索取實測數據計算，不可直接填 0。",
            "<strong>歐盟 CBAM 審查偏好實體 PPA：</strong>歐盟連自己的 GO 憑證都不完全買單，CBAM 更傾向要求買賣雙方的實體 PPA 合約與直接供電佐證。"
        ],
        "takeaway": "外銷歐盟企業切勿僅採購虛擬憑證應付，必須以「電證合一 PPA 實體轉供合約」作為抵禦 CBAM 碳關稅的實質防線。",
        "visualTitle": "範疇二碳排抵扣計算模型 ✕ 歐盟 CBAM 審查偏好漏斗",
        "visualType": "cbam_calc",
        "thumbImg": "../assets/images/slides/slide_04.jpg",
        "thumbCaption": "講義 P.04：溫室氣體盤查範疇二計算規則與國際認可",
        "thumbLabel": "P.04 範疇二扣抵模型",
        "noteTakeaway": "光電風電憑證碳排係數算 0，生質能則不是 0；而歐盟 CBAM 最在乎的是實體 PPA 長期購售電合約。",
        "noteDetail": "學員現場提問 CBAM 是否認台灣憑證，張科長坦言：歐盟為了保護本土產業，甚至不認自己的 GO 憑證，更看重工廠實體電力的 PPA 合約。",
        "noteTransition": "了解了憑證國際效力後，台灣綠電市場究竟是如何一步步演進至今日自由化格局的？請看第五頁市場發展全貌。"
    },
    {
        "slideNo": 5,
        "module": "MODULE 2 ｜ 台灣綠電市場演進",
        "ref": "講義對照 P.05 ｜ 錄音 09:18~11:49",
        "title": "綠電市場 17 年演進：從早期一度 10 元全民躉購，邁向 106 年電業法修正「綠電先行」自由化",
        "question": "台灣綠電從 98 年起經歷了哪些關鍵轉型？電業法「綠電先行」如何解綁台電全額收購的單一格局？",
        "highlights": [
            "<strong>民國 98 年躉購拓荒期：</strong>再生能源發展條例上路，早期太陽光電一度收購價逾 10 元，台電保障收購 20 年，實質由全民納稅買單。",
            "<strong>民國 106 年電業自由化：</strong>電業法重大修正啟動「綠電先行」，打破台電統購統銷，開放發電業與售電業直接對接民間用電大戶。",
            "<strong>轉供過渡到全面成熟：</strong>106~109 年受限台電轉供規章未臻成熟，僅靠自用發電憑證流轉；109 年起 PPA 正式商轉邁向規模化。"
        ],
        "takeaway": "台灣綠電已徹底告別「依賴台電躉購補貼」的嬰兒期，全面進入以市場供需為導向的「商業綠電自由化」時代。",
        "visualTitle": "台灣綠電自由化 17 年演進時間軸 (民國 98～115 年)",
        "visualType": "market_timeline",
        "thumbImg": "../assets/images/slides/slide_05.jpg",
        "thumbCaption": "講義 P.05：台灣綠電市場發展階段與電業法修法進程",
        "thumbLabel": "P.05 綠電演進時程",
        "noteTakeaway": "98 年一度光電收 10 塊錢由全民買單；106 年電業法修正開放綠電先行，開啟民間買賣直轉供新紀元。",
        "noteDetail": "早期台電代購是為扶植產業，銀行也只願意借錢給有台電保證收購的案場；修法後綠電自由化，讓買家可以直接跟電廠買綠電。",
        "noteTransition": "自由化之後，電與證到底有哪幾種轉供流動路徑？請看第六頁綠電四大流通路徑全圖。"
    },
    {
        "slideNo": 6,
        "module": "MODULE 2 ｜ 綠電四大流通路徑",
        "ref": "講義對照 P.06 ｜ 錄音 11:49~13:37",
        "title": "綠電轉供三大體系與四大路徑：4A 自發自用留存、4B 電證分離、直轉供 PPA 代輸",
        "question": "自發自用、電證分離與直轉供有何不同？電網代輸在技術與產權上如何實現「電與證」的精準流轉？",
        "highlights": [
            "<strong>4A 路徑（電證合一自發自用）：</strong>工廠自建光電屋頂，所發電力全部內部自用，憑證留在企業內部宣告 ESG 與抵扣範疇二。",
            "<strong>4B 路徑（電證分離市場交易）：</strong>自用發電電量廠內自行消耗，發放之綠電憑證則上架平台單獨轉售外部買家變現。",
            "<strong>1/2/3 途徑（電證合一 PPA 轉供）：</strong>大型綠電電廠透過台電高壓輸配電網，按月計量代輸至用電端，電與證同步交割。"
        ],
        "takeaway": "釐清 4A、4B 與直轉供路徑，企業才能依據自身「有無屋頂、有無電號、有無 ESG 急迫性」量身定做綠電組合。",
        "visualTitle": "台灣綠電市場三大體系與四大流通拓撲圖",
        "visualType": "trading_routes",
        "thumbImg": "../assets/images/slides/slide_06.jpg",
        "thumbCaption": "講義 P.06：綠電交易四大路徑與台電轉供關係圖",
        "thumbLabel": "P.06 四大交易路徑",
        "noteTakeaway": "4A 是自己發自己用證留著；4B 是電自己用但把證賣掉；1/2/3 是電與證綁在一起透過台電電網轉供。",
        "noteDetail": "2017 到 2020 年間因為台電轉供規則還在研擬，市面上只有 4A 跟 4B 兩種模式；2020 年直轉供上路後，PPA 規模才真正噴發。",
        "noteTransition": "在四大路徑中，是什麼政策讓自用型發電設備全面爆發？請看第七頁二三型設備鬆綁新政。"
    },
    {
        "slideNo": 7,
        "module": "MODULE 2 ｜ 二三型設備鬆綁紅利",
        "ref": "講義對照 P.07 ｜ 錄音 13:37~15:25",
        "title": "二三型設備鬆綁新政：免除轉型一型發電業繁瑣審查，小型屋頂電廠透過售電業直接賣電",
        "question": "舊制下小型二三型自用發電設備為何「有電賣不得」？能源署鬆綁函令如何釋放百萬瓩「螞蟻雄兵」？",
        "highlights": [
            "<strong>舊制嚴苛轉型壁壘：</strong>自用發電設備若要售電需轉「一型發電業」，面臨委員會現勘、專任技術員、繁雜月報，成本高昂。",
            "<strong>能源署鬆綁函令破局：</strong>二三型無須變更電業執照，只要與合格售電業簽約，即可合法將綠電轉供至自由市場！",
            "<strong>釋放「螞蟻雄兵」供給：</strong>小型工廠屋頂電廠大舉入市，帶動 2024–2026 年自由市場綠電交易規模呈現爆發式倍增。"
        ],
        "takeaway": "二三型自用發電設備鬆綁是近三年綠電市場供給端最大活水，徹底打破大型電廠獨占賣電的市場壟斷。",
        "visualTitle": "舊制繁瑣審查關卡 vs 新制售電業直轉「螞蟻雄兵」效益",
        "visualType": "deregulation_ants",
        "thumbImg": "../assets/images/slides/slide_07.jpg",
        "thumbCaption": "講義 P.07：自用發電設備二三型售電鬆綁政策前後對比",
        "thumbLabel": "P.07 二三型售電鬆綁",
        "noteTakeaway": "二三型自用光電以前要賣電得轉成一型發電業，被大批審查委員刁難還要聘專責人員；現在免轉型、透過售電業就能直接賣！",
        "noteDetail": "張科長強調：這條函令一出，全台灣數以萬計的中小型屋頂光電『螞蟻雄兵』全部活化，直接促成去年與今年綠電交易量爆發成長。",
        "noteTransition": "有了充沛供給後，大家在交易平台都怎麼買賣？請看第八頁憑證平台存憑證與店家證真相。"
    },
    {
        "slideNo": 8,
        "module": "MODULE 2 ｜ 交易平台實務真相",
        "ref": "講義對照 P.08 ｜ 錄音 20:02~22:15",
        "title": "憑證交易專區真相：「存憑證」現貨交易熱絡，「店家證」因 PPA 複雜條款全走線下私約",
        "question": "為什麼憑證中心官網的「店家證」專區成交量長年掛零？PPA 長約合約具備哪些無法線上點擊下單的特性？",
        "highlights": [
            "<strong>存憑證專區（現貨熱絡）：</strong>已發放完成之 4B 自發自用憑證，上架明碼標價，買方線上下單即完成移轉，流動性極佳。",
            "<strong>店家證專區（掛零真相）：</strong>電證合一長期 PPA 涉及發電預測、余電處置、違約保證金等複雜法律條款，無法透過網頁按鈕成交。",
            "<strong>線下深度客製談判：</strong>買賣雙方透過平台媒合後，均轉入線下由專業售電業協助量身簽約，平台僅負責最終憑證登錄與過戶。"
        ],
        "takeaway": "平台是媒合與過戶中樞而非電商購物車；搞懂「存憑證走線上、PPA 走線下私約」才能正確開展綠電採購。",
        "visualTitle": "憑證交易專區雙軌運作機制對比 (存憑證現貨 vs 店家證 PPA)",
        "visualType": "platform_realities",
        "thumbImg": "../assets/images/slides/slide_08.jpg",
        "thumbCaption": "講義 P.08：國家再生能源憑證交易專區操作介面說明",
        "thumbLabel": "P.08 交易專區實務",
        "noteTakeaway": "很多人誤以為買綠電像在蝦皮買東西按一下就結帳；存憑證可以線上買現貨，但 PPA 長約因為牽涉發電用電匹配，全是線下談完再到平台過戶。",
        "noteDetail": "店家證線上掛零不是沒人買，而是大家談好合約後直接線下預約媒合。平台絕非詐騙，而是國家公正的登錄移轉中樞。",
        "noteTransition": "既然 PPA 都在線下談判，那價格到底如何訂定？請看第九頁綠電自由市場定價基石。"
    },
    {
        "slideNo": 9,
        "module": "MODULE 3 ｜ 綠電自由市場定價",
        "ref": "講義對照 P.09 ｜ 錄音 22:15~24:51",
        "title": "自由市場定價基石：台電 FIT 躉購費率為絕對下限，疊加 VPC、風雨球場與北部加成",
        "question": "自由市場綠電價格如何形成？發電業者賣給民間的定價底線在哪裡？加成機制如何推高市場售價？",
        "highlights": [
            "<strong>台電 FIT 是價格錨定地板：</strong>自由市場交易價必然高於台電收購價，否則電廠直接賣給台電保證收購 20 年即可，何必承擔民間違約風險？",
            "<strong>太陽光電基礎費率區間：</strong>太陽光電 FIT 約 3.5～5.6 元/度；陸域風電約 2.1 元/度；離岸風電採競價無固定費率。",
            "<strong>法定加成推高成本邊界：</strong>高效能 VPC 模組 (+6%)、風雨球場加成、北部區域加成 (+15%) 累積後，自由市場售價多落在 4.8～6.5 元區間。"
        ],
        "takeaway": "台電 FIT 加成費率是綠電自由市場的剛性成本底線；採購評估應理性錨定「FIT 地板價 ＋ 轉供服務費 ＋ 市場合理溢價」。",
        "visualTitle": "綠電自由市場價格形成堆疊模型 (FIT 基準 ＋ 法定加成 ＋ 市場溢價)",
        "visualType": "pricing_ladder",
        "thumbImg": "../assets/images/slides/slide_09.jpg",
        "thumbCaption": "講義 P.09：再生能源躉購費率 (FIT) 基準表與加成機制",
        "thumbLabel": "P.09 FIT 價格定價階梯",
        "noteTakeaway": "張科長講白話：想在自由市場買到比台電便宜的綠電是不可能的！發電業者賣台電穩賺 20 年，賣你一定要出更高價格。",
        "noteDetail": "光電基本費率 3.5~5.6 元，如果案場有 VPC、在北部、又是風雨球場，加成上去躉購價就破 6 塊，自由市場賣價自然水漲船高。",
        "noteTransition": "高價之外，大型電廠還有嚴苛的信評門檻；中小企業如何破局？請看第十頁台資電統購分銷模式。"
    },
    {
        "slideNo": 10,
        "module": "MODULE 3 ｜ 台資電統購分銷突破",
        "ref": "講義對照 P.10 ｜ 錄音 24:51~26:31, 42:21~43:58",
        "title": "台資電統購分銷平台：充當信用護城河，化解聯貸銀行對中小企業信用評等之門檻限制",
        "question": "大型地面與離岸風場動輒數百億融資，中小企業為何遭銀行聯貸阻絕於外？台資電如何充當「信用破局者」？",
        "highlights": [
            "<strong>大型電廠融資信用枷鎖：</strong>大型電廠背後有龐大銀行團聯貸，要求 PPA 買方必須具備國際或本國頂級信用評等（如台積電等級）。",
            "<strong>中小企業信用邊緣化困境：</strong>全台具備 AAA 級信用企業屈指可數，廣大中小企業即便出價更高，亦因無信評報告而無法簽訂 PPA。",
            "<strong>台資電出面統購分銷：</strong>由具官股背景之台灣智慧電網公司出面統購大額綠電，再切分為小額短天期合約批發給中小企業。"
        ],
        "takeaway": "台資電統購分銷本質是「國營級信用擔保中介」，有效打通大型電廠與信評不足中小企業間的交易天塹。",
        "visualTitle": "大型電廠聯貸信評壁壘 vs 台資電統購分銷破局拓撲",
        "visualType": "taipower_credit",
        "thumbImg": "../assets/images/slides/slide_10.jpg",
        "thumbCaption": "講義 P.10：台灣智慧電網公司統購分銷機制架構",
        "thumbLabel": "P.10 台資電統購分銷",
        "noteTakeaway": "大電廠要跟銀行借幾百億，銀行只准賣給台積電這種高信評大戶；中小企業連談的資格都沒有，台資電就是來充當信評擔保人。",
        "noteDetail": "台資電出面把大電廠的綠電包下來，承擔信用風險，再拆成小額產品分銷給一般企業，徹底解決中小企業被市場邊緣化的痛點。",
        "noteTransition": "除了台資電之外，台電也推出了自己的綠電產品，請看第十一頁台電小額綠電專案。"
    },
    {
        "slideNo": 11,
        "module": "MODULE 3 ｜ 台電小額綠電專案",
        "ref": "講義對照 P.11 ｜ 錄音 27:10~29:47",
        "title": "台電小額綠電戰略深意：小額短約低風險，扮演中小用戶熟悉綠電契約細節之「實戰練兵場」",
        "question": "台電為何推出「1 萬度 / 20 萬度」小額綠電產品？這項政策對於初次嘗試買綠電的企業有何關鍵戰略價值？",
        "highlights": [
            "<strong>輕量級合約規格設計：</strong>提供 1 萬度、20 萬度小額產品，搭配 1 年期、5 年期合約，價格落在 5～6 元/度，大幅降低試水溫門檻。",
            "<strong>消弭與民爭利質疑：</strong>台電嚴格限額限量，不與民間售電業爭奪大額市場，定位於培育整體市場成熟度。",
            "<strong>契約實務「實戰練兵場」：</strong>透過與台電簽署標準化契約，中小企業得以親自搞懂轉供計量、時段劃分與責任條款，為日後洽商民間 PPA 奠定合約防禦力。"
        ],
        "takeaway": "台電小額綠電不是為獲利，而是為中小企業打造的「零風險綠電合約駕訓班」，是初入市場企業的最佳起手式。",
        "visualTitle": "台電小額綠電產品規格矩陣 (1萬/20萬度 ✕ 1年/5年期 ✕ 練兵效益)",
        "visualType": "small_green_matrix",
        "thumbImg": "../assets/images/slides/slide_11.jpg",
        "thumbCaption": "講義 P.11：台電小額綠電試辦方案內容與申請指引",
        "thumbLabel": "P.11 台電小額綠電",
        "noteTakeaway": "張科長替台電說公道話：台電推 1 萬度小額綠電不是要賺錢，而是讓中小企業先跟台電簽約練兵，看懂合約條款裡的諸多細節。",
        "noteDetail": "學會了跟台電簽定型化契約，後續再面對民間售電業或發電廠時，才知道合約裡哪些責任條款該改、如何爭取自己公司的權益。",
        "noteTransition": "如果預算更吃緊，還有什麼平價管道？請看第十二頁平價綠電競標與小農式綠電市集。"
    },
    {
        "slideNo": 12,
        "module": "MODULE 3 ｜ 平價競標與綠電市集",
        "ref": "講義對照 P.12 ｜ 錄音 29:47~32:11",
        "title": "平價綠電競標與小農式市集：鎖定員工未滿 200 人中小企業，底價 4.3 元打通對接通道",
        "question": "中小外銷企業如何取得低於市場行情的平價綠電？官方如何透過「小農市集」模式打破資訊不對稱？",
        "highlights": [
            "<strong>平價綠電競標限額保障：</strong>限定資本額 ≤ 1 億元、員工 < 200 人之中小企業，得標量上限為前一年總用電量 30%，確保雨露均霑。",
            "<strong>底價 4.3 元平抑通膨：</strong>2026 年度專案底價定在 4.3 元/度，大幅舒緩面臨海外碳關稅中小製造業的合規成本壓力。",
            "<strong>實體「綠電市集」巡迴擺攤：</strong>仿效農夫市集模式，於台中、高雄、台北、桃園巡迴展出，免事先報名即可與合格售電業面對面洽談。"
        ],
        "takeaway": "政策多管齊下提供「平價競標（4.3元）」與「實體市集（免門檻對接）」，中小企業應主動出擊鎖定年度配額。",
        "visualTitle": "中小企業平價綠電競標參數卡 ✕ 綠電市集全台巡迴地圖",
        "visualType": "bidding_market",
        "thumbImg": "../assets/images/slides/slide_12.jpg",
        "thumbCaption": "講義 P.12：平價綠電競標辦法與綠電市集活動規劃",
        "thumbLabel": "P.12 平價競標與市集",
        "noteTakeaway": "中小企業平價競標底價才 4.3 元，限定資本額 1 億以下、員工 200 人以下才能搶，每年 7~8 月推出，企業務必提早準備。",
        "noteDetail": "綠電市集就像小農擺攤，北中南巡迴免報名直接進場，讓買家可以直接跟售電業面對面問到飽，現場還宣講最新法規。",
        "noteTransition": "若公司身在台北 101 等商辦大樓、根本沒有獨立電表，該如何買綠電？請看第十三頁無電號租戶模式。"
    },
    {
        "slideNo": 13,
        "module": "MODULE 4 ｜ 無電號租戶解方演進",
        "ref": "講義對照 P.13 ｜ 錄音 32:11~34:07",
        "title": "無電號租戶綠電突圍：從台北 101 大樓 1.0 單租戶模式，跨越至 2.0 綠色大樓團購破 2 億度",
        "question": "租在大型商辦（如 101 大樓）的企業沒有獨立台電電號，如何轉供綠電？1.0 與 2.0 商業模式如何演進？",
        "highlights": [
            "<strong>商辦租戶無獨立電號之痛：</strong>商辦大樓全棟共用一組總電表，個別租戶無獨立電號，早期制度下無法向台電申請電網轉供。",
            "<strong>1.0 單租戶突破模式（800萬度）：</strong>經大樓房東出具同意書，租戶委託中間售電業簽約轉供，由大樓拆分內部計量，累計取得破 800 萬度。",
            "<strong>2.0 綠色大樓團購模式（破 2 億度）：</strong>大樓業主（如 101）統一出面採購大型綠電，全棟租戶共享綠電賦能，累計轉供量突破 2 億度！"
        ],
        "takeaway": "「綠色大樓 2.0 團購模式」將無電號劣勢轉化為大宗採購議價優勢，是金融與科技服務業落實 RE100 的最高效路徑。",
        "visualTitle": "無電號租戶綠電突圍架構 (1.0 單租戶模式 vs 2.0 綠色大樓團購)",
        "visualType": "tenant_101",
        "thumbImg": "../assets/images/slides/slide_13.jpg",
        "thumbCaption": "講義 P.13：無電號租戶綠電取得架構與 101 大樓實例",
        "thumbLabel": "P.13 101大樓租戶模式",
        "noteTakeaway": "在 101 租辦公室沒有電表也能買綠電！1.0 靠房東同意個別簽，2.0 更是由房東統籌全棟團購，累計已經轉供超過 2 億度。",
        "noteDetail": "2.0 團購模式讓整棟大樓都變成『綠色大樓』，房東用綠電拉高租金與企業形象，租戶免去單獨簽約的麻煩，創造雙贏成效斐然。",
        "noteTransition": "買到了綠電，為什麼常常發生發了電卻用不完的窘境？請看第十四頁發用電曲線天然錯配分析。"
    },
    {
        "slideNo": 14,
        "module": "MODULE 4 ｜ 供需曲線天然錯配",
        "ref": "講義對照 P.14 ｜ 錄音 34:07~35:32",
        "title": "供需曲線天然錯配：太陽光電夏日噴發、風電冬日滿載，與商辦週末無人形成「余電」難題",
        "question": "不同再生能源之發電時段與各類用戶之用電負載存在哪些天然錯配？為什麼 PPA 絕對需要售電業專業配比？",
        "highlights": [
            "<strong>季節性格差：</strong>太陽光電峰值在 5～8 月夏日白天，風電峰值在 10～2 月東北季風，水力四季均勻；單一綠能無法全年滿載。",
            "<strong>週間作息格差：</strong>商辦與大部分製造廠週一至週五負載拉滿，週六週日產線停工、用電量歸零，光電在週末形成大量浪費性「余電」。",
            "<strong>售電業中介配置價值：</strong>售電業以風光互補演算法整合多元案場，依據客戶用電曲線調配出最佳綠電套餐，避免大量余電被低價賤賣。"
        ],
        "takeaway": "綠電採購不是算算術總量，而是玩「每 15 分鐘曲線即時對齊的拼圖遊戲」；多元能源配比是消除余電損失的核心法門。",
        "visualTitle": "再生能源發電曲線 vs 用戶負載作息時空錯配示意圖",
        "visualType": "mismatch_curves",
        "thumbImg": "../assets/images/slides/slide_14.jpg",
        "thumbCaption": "講義 P.14：風光發電時段與產業用電負載曲線對照圖",
        "thumbLabel": "P.14 供需曲線錯配",
        "noteTakeaway": "光電夏天發最多、風電冬天發最多，而商辦大樓週六日根本沒人上班，電發出來沒人用就變成余電浪費掉。",
        "noteDetail": "這就是為什麼買綠電不能只看一年總度數；如果只買光電，週末的大量余電會讓你虧損嚴重，售電業的核心價值就是做風光配比。",
        "noteTransition": "台電是怎麼計算轉供與余電的？請看第十五頁台電 15 分鐘轉供結算與四大時段規則。"
    },
    {
        "slideNo": 15,
        "module": "MODULE 4 ｜ 台電轉供結算機制",
        "ref": "講義對照 P.15 ｜ 錄音 35:32~36:48",
        "title": "台電 15 分鐘轉供結算：週間尖峰/半尖峰、週六半尖峰、離峰四大時段與「月內二次彌合」",
        "question": "台電電網代輸轉供究竟如何按月結算？四大獨立時段劃分與「月內二次彌合」如何計算余電與灰電？",
        "highlights": [
            "<strong>15 分鐘粒度即時比對：</strong>台電每 15 分鐘比對發電端注入電量與用電端消耗電量，不足時自動補入台電灰電，多出則判定為余電。",
            "<strong>四大獨立時段互不相抵：</strong>劃分「週間尖峰、週間半尖峰、週六半尖峰、離峰」，四個時段猶如四個密封水桶，電量嚴禁跨時段挪用。",
            "<strong>月度同區間二次彌合：</strong>當月未匹配完之多餘綠電，允許在當月同一個時段代碼內進行二次彌合，將月度余電量壓制至最低。"
        ],
        "takeaway": "搞懂台電「四大時段密封水桶」規則，才能理解週六日的光電為何無法填補週三的尖峰，進而精準規劃儲能或風電互補。",
        "visualTitle": "台電 15 分鐘轉供比對與四大獨立時段「月內二次彌合」架構",
        "visualType": "wheeling_four_buckets",
        "thumbImg": "../assets/images/slides/slide_15.jpg",
        "thumbCaption": "講義 P.15：台電轉供四大時段劃分與 15 分鐘結算規則",
        "thumbLabel": "P.15 四大時段結算",
        "noteTakeaway": "台電每 15 分鐘結算一次，分為週間尖峰、週間半尖峰、週六半尖峰與離峰四大時段，各時段的電不能跨時段流動。",
        "noteDetail": "當月沒用完的電可以在當月『同一個時段』做第二次彌合；但週六半尖峰的余電絕對不能拿去補週間尖峰，這就是水桶理論。",
        "noteTransition": "如何打破這種死板的轉供限制？請看第十六頁台電 2026 年 10 月最新上線的沙盒 3.0。"
    },
    {
        "slideNo": 16,
        "module": "MODULE 4 ｜ 台電沙盒 3.0 彈性分配",
        "ref": "講義對照 P.16 ｜ 錄音 36:48~42:21",
        "title": "台電沙盒 3.0 彈性分配革命：打破事前固定比例僵局，事後自由劃撥且資料費暴降 98%",
        "question": "2026 年 10 月最新上線的「沙盒 3.0」如何解決傳統轉供死板僵化的痛點？企業如何利用事後分配消滅余電？",
        "highlights": [
            "<strong>舊制事前契約固定比例之弊：</strong>傳統月結需事前在合約明訂各電號固定分配比例，各廠產能變動時無法互助，產生大量無效余電。",
            "<strong>沙盒 3.0 事後自由挪移：</strong>月度結束後，企業可依實際用電結果，自由將已購綠電優先撥補給外銷高稽核電號，剩餘再勻分其他廠區。",
            "<strong>門檻收費斷崖式大降 98%：</strong>小用戶資料提供費自數十萬降至 2 萬元；1000 電號以上大戶更自 120 萬元暴降至 2.4 萬元！"
        ],
        "takeaway": "沙盒 3.0 是綠電分配機制的重大解放；「事後彈性劃撥 ＋ 規費狂降 98%」使跨廠區企業能以最低成本實現余電歸零。",
        "visualTitle": "傳統事前契約死板分配 vs 沙盒 3.0 事後彈性挪移對比模型",
        "visualType": "sandbox_3",
        "thumbImg": "../assets/images/slides/slide_16.jpg",
        "thumbCaption": "講義 P.16：台電沙盒 3.0 彈性分配方案與費用調整表",
        "thumbLabel": "P.16 沙盒 3.0 彈性分配",
        "noteTakeaway": "剛在 10 月份上線的沙盒 3.0 是超重磅利多！以前要在合約寫死分配比例，現在每個月底看誰缺電再事後分配，而且資料費直接打 2 折不到！",
        "noteDetail": "大戶資料提供費從 120 萬暴降到 2.4 萬，企業可以把綠電精準灌給需要 RE100 的外銷廠區，解決了產能調整時余電被浪費的千古難題。",
        "noteTransition": "除了分配機制大改，憑證結算今年也有重大突破，請看第十七頁 2026 綠電零股化新制。"
    },
    {
        "slideNo": 17,
        "module": "MODULE 5 ｜ 綠電零股化新制",
        "ref": "講義對照 P.17 ｜ 錄音 44:04~46:46",
        "title": "2026 綠電零股化新制：按月獨立結算告別零頭跨月滾存，完美適配全球客戶多元會計年度",
        "question": "舊制以「1000 度整數發證」帶來什麼跨年度弊端？零股化新制如何按月結清並完美對齊跨國客戶財年？",
        "highlights": [
            "<strong>舊制跨年滾存之痛：</strong>舊制不足 1000 度的零頭滾入次月，12 月份發電的零頭滾到隔年 1 月，造成碳排歸屬年份的重大核算爭議。",
            "<strong>跨國供應鏈多元財年衝擊：</strong>美商客戶以 6/7 月為財年、日商以 3/4 月結算，舊制跨月滾存讓跨國供應鏈廠商的碳盤查極為被動。",
            "<strong>按月獨立結算「零股全發」：</strong>2026 新制當月有多少度就發多少度零股憑證，不再跨月滾存，企業可自由挑選任意連續 12 個月精準對齊客戶財年。"
        ],
        "takeaway": "零股化徹底消滅了「跨年零頭漂泊」的會計頑疾，賦予企業高度靈活的盤查週期拼接彈性。",
        "visualTitle": "舊制 1000 度整數滾存跨年問題 vs 零股化按月結清對齊國際財年",
        "visualType": "fractional_trec",
        "thumbImg": "../assets/images/slides/slide_17.jpg",
        "thumbCaption": "講義 P.17：再生能源憑證零股化作業規範與核發實例",
        "thumbLabel": "P.17 憑證零股化",
        "noteTakeaway": "以前發電零頭要湊滿 1000 度才給一張，跨年的時候 12 月的零頭跑到 1 月，客戶氣得跳腳；今年零股化上路，按月全發乾乾淨淨！",
        "noteDetail": "美商看 6 月財年、日商看 3 月財年，現在每個月各算各的，企業要拼哪 12 個月隨你挑，國際供應鏈查帳再也不會產生歸屬爭議。",
        "noteTransition": "行政審查方面今年又做了哪些鬆綁？請看第十八頁查核機制取消分區與小型案場自撰報告。"
    },
    {
        "slideNo": 18,
        "module": "MODULE 5 ｜ 憑證查核大鬆綁",
        "ref": "講義對照 P.18 ｜ 錄音 46:46~48:19",
        "title": "憑證查核機制大鬆綁：取消北中南區域劃分自由選，1MW 以下案場自撰報告先行發證",
        "question": "2026 年 7 月上路的查驗制度改革解除了哪些行政枷鎖？1MW 以下小型案場如何大幅縮短發證等待期？",
        "highlights": [
            "<strong>廢除北中南分區限制：</strong>官方認可之 3 家查驗機構全面解除區域限制，業者可依服務品質與報價全台自由跨區挑選合作。",
            "<strong>1MW 以下案場自撰報告快速通關：</strong>裝置容量 1MW 以下之中小型案場，允許業者自行撰寫查核報告送審，書審通過即刻開立發證！",
            "<strong>事後差額現場抽查保障品質：</strong>先核發憑證讓綠電快速進入市場流通，後續再由查驗機構補做現場差額查驗，兼顧效率與防偽。"
        ],
        "takeaway": "查驗制度「打破分區限制 ＋ 1MW 自撰報告加速」大幅縮短了發證週期，為中小型綠電案場提供了極為友善的行政綠色通道。",
        "visualTitle": "憑證查驗制度改革：取消跨區限制 ✕ 1MW 自撰報告審驗加速拓撲",
        "visualType": "audit_reform",
        "thumbImg": "../assets/images/slides/slide_18.jpg",
        "thumbCaption": "講義 P.18：再生能源憑證查核作業鬆綁與簡化規範",
        "thumbLabel": "P.18 查核制度大鬆綁",
        "noteTakeaway": "今年 7 月起 3 家查驗機構全台灣自由選，不再限制北區只能找某家；而且 1MW 以下電廠可以自己寫報告，審過先發證，後面再補查現場！",
        "noteDetail": "這對中小型光電業者是一大德政，以往排隊等查驗機構現場查核動輒拖上好幾個月，現在自己送書審過關就先發證賺錢，效率成倍提升。",
        "noteTransition": "最後，主管機關預告在年底前還有哪些法規利多即將生效？請看第十九頁即將落地三大新法規。"
    },
    {
        "slideNo": 19,
        "module": "MODULE 5 ｜ 即將落地三大法規新制",
        "ref": "講義對照 P.19 ｜ 錄音 48:47~55:17",
        "title": "即將落地三大法規新政：未售台電余電可發證、電表拍照追溯起算點、單一電號多主體拆分",
        "question": "標檢局預計於 2026 年底前正式公告實施的「三項重磅法規革新」是什麼？將為業者釋放哪些實質紅利？",
        "highlights": [
            "<strong>未售台電之余電可發憑證（年底公告）：</strong>只要業者放棄台電躉購余電合約，即便電量未完全被用戶消耗，剩餘余電亦可全額核發綠電憑證！",
            "<strong>解約次日電表拍照追溯起算點：</strong>電廠與台電解約 FIT 改賣綠電時，次日拍照舉證電表讀數，憑證起算點即可直接追溯至解約日，消滅 1 個月審查空窗浪費。",
            "<strong>單一電號多主體出資憑證拆分：</strong>解決南軟園區等「多企業合資在單一電號屋頂建光電」的場域，管理中心申請後憑證可依出資比例直接拆分發給各家股東！"
        ],
        "takeaway": "三大新法規直擊「余電浪費、起算真空期、合資電廠分配」三大長期死結，是政策走向高度市場化與精準化的重大利多。",
        "visualTitle": "即將落地三大法規改革紅利 (余電發證 ✕ 拍照追溯 ✕ 單一電號拆分)",
        "visualType": "three_upcoming_laws",
        "thumbImg": "../assets/images/slides/slide_19.jpg",
        "thumbCaption": "講義 P.19：再生能源憑證實施辦法修正預告草案重點",
        "thumbLabel": "P.19 三大法規新政預告",
        "noteTakeaway": "三大預告新政年底前上路：沒賣台電的余電可以發憑證；電表拍照當天就能追溯發電；像南軟多家合資的案場憑證能直接按出資拆分！",
        "noteDetail": "特別是拍照追溯：以前跟台電解約要等一個月行政審查通過才開始算度數，白白損失一個月綠電；新規定解約隔天拍下電表照片，日後直接追溯補發！",
        "noteTransition": "貫穿全課知識，企業能源管理者與工程師應遵守哪些核心守則？請看第二十頁綠電交易與運維十條軍規。"
    },
    {
        "slideNo": 20,
        "module": "MODULE 5 ｜ 綠電交易與憑證運維十條軍規",
        "ref": "全課歸納 ｜ 錄音 00:00~55:41",
        "title": "綠電交易與憑證運維十條軍規：企業合約防禦、台電轉供調度與資產價值最大化",
        "question": "身處綠電自由化浪潮中的維運團隊與能源主管，必須嚴格恪守哪些實戰軍規與合約紅線？",
        "highlights": [
            "<strong>合規底線（軍規 1-3）：</strong>嚴禁與 FIT 躉購及碳抵換專案重疊；認明 RE100 五大正名綠能；廢棄物發電碳係數嚴禁逕自填 0。",
            "<strong>合約防禦（軍規 4-6）：</strong>善用台電小額綠電練兵摸清 PPA 眉角；審慎簽署 Take-or-Pay 必購條款；透過台資電破除大案場信用壁壘。",
            "<strong>調度增益（軍規 7-10）：</strong>全速切換台電沙盒 3.0 事後彈性分配；解約轉綠電當日拍照追溯起算；善用二三型設備鬆綁與零股化對齊海外財年。"
        ],
        "takeaway": "綠電採購不是單純比價，而是兼顧合規底線、合約防禦與精準調度的系統工程；恪守十條軍規，方能在零碳轉型中穩操勝券。",
        "visualTitle": "綠電交易與再生能源憑證運維實戰十條軍規檢核表",
        "visualType": "ten_commandments_c4",
        "thumbImg": "../assets/images/slides/slide_20.jpg",
        "thumbCaption": "講義 P.20：綠電採購與維運實務守則總結",
        "thumbLabel": "P.20 綠電十條軍規",
        "noteTakeaway": "十條軍規是進金生維運工程師與客戶能管主管的實戰聖經，涵蓋合規紅線、合約防禦與調度增益全流程。",
        "noteDetail": "不踩 FIT 雙重計算紅線、善用沙盒 3.0 事後分配、抓住解約拍照追溯與零股化紅利，就能替公司在合規與電費上創造數百萬的實質價值。",
        "noteTransition": "全課 20 頁精華講解完畢，歡迎按 G 鍵切換總覽網格，或按 P 鍵匯出 16:9 顧問 PDF 備忘錄。"
    }
]

def make_visual_body(vtype):
    # Generates custom SVG for each visual type
    if vtype == "trec_lifecycle":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="c4_g1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1B365D"/>
              <stop offset="100%" stop-color="#0E8A78"/>
            </linearGradient>
            <linearGradient id="c4_gold" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#D99B26"/>
              <stop offset="100%" stop-color="#C58518"/>
            </linearGradient>
          </defs>
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">T-REC 國家再生能源憑證生命週期 (轉讓一次為限)</text>
          
          <!-- Node 1: 發電端 -->
          <rect x="20" y="55" width="85" height="70" rx="6" fill="#FFFFFF" stroke="#0E8A78" stroke-width="2"/>
          <text x="62" y="78" font-size="11" font-weight="bold" fill="#0E8A78" text-anchor="middle">1. 發電端</text>
          <text x="62" y="96" font-size="9" fill="#64748B" text-anchor="middle">風光水地生</text>
          <text x="62" y="110" font-size="8" fill="#94A3B8" text-anchor="middle">併網計量讀數</text>
          
          <path d="M 105 90 L 125 90" stroke="#0E8A78" stroke-width="2" marker-end="url(#arrow)"/>
          
          <!-- Node 2: 第三方查驗 -->
          <rect x="125" y="55" width="85" height="70" rx="6" fill="#FFFFFF" stroke="#1B365D" stroke-width="2"/>
          <text x="167" y="78" font-size="11" font-weight="bold" fill="#1B365D" text-anchor="middle">2. 第三方查驗</text>
          <text x="167" y="96" font-size="9" fill="#64748B" text-anchor="middle">官方認可3家</text>
          <text x="167" y="110" font-size="8" fill="#94A3B8" text-anchor="middle">設備現場稽核</text>

          <path d="M 210 90 L 230 90" stroke="#1B365D" stroke-width="2"/>

          <!-- Node 3: 標檢局憑證中心 -->
          <rect x="230" y="50" width="100" height="80" rx="6" fill="url(#c4_g1)" stroke="#0E8A78" stroke-width="2"/>
          <text x="280" y="75" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. 憑證中心</text>
          <text x="280" y="93" font-size="10" fill="#E2E8F0" text-anchor="middle">核發電子身分證</text>
          <text x="280" y="110" font-size="9" font-weight="bold" fill="#FDE047" text-anchor="middle">1000度/張 (零股)</text>

          <path d="M 330 90 L 350 90" stroke="#D99B26" stroke-width="2"/>

          <!-- Node 4: 單次移轉 -->
          <rect x="350" y="55" width="80" height="70" rx="6" fill="#FFFFFF" stroke="#D99B26" stroke-width="2"/>
          <text x="390" y="78" font-size="11" font-weight="bold" fill="#D99B26" text-anchor="middle">4. 單次移轉</text>
          <text x="390" y="96" font-size="9" fill="#DC2626" font-weight="bold" text-anchor="middle">嚴禁二次交易</text>
          <text x="390" y="110" font-size="8" fill="#64748B" text-anchor="middle">帳號間電文轉移</text>

          <path d="M 430 90 L 450 90" stroke="#0E8A78" stroke-width="2"/>

          <!-- Node 5: 用電端註銷 -->
          <rect x="450" y="55" width="75" height="70" rx="6" fill="#FFFFFF" stroke="#0E8A78" stroke-width="2"/>
          <text x="487" y="78" font-size="11" font-weight="bold" fill="#0E8A78" text-anchor="middle">5. 宣告註銷</text>
          <text x="487" y="96" font-size="9" fill="#1B365D" text-anchor="middle">Scope 2 抵扣</text>
          <text x="487" y="110" font-size="8" fill="#10B981" font-weight="bold" text-anchor="middle">永久消滅鎖定</text>

          <!-- 下方特徵對照 -->
          <rect x="20" y="145" width="245" height="105" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
          <text x="30" y="166" font-size="11" font-weight="bold" fill="#1E40AF">官方法定防偽三大鐵律：</text>
          <text x="30" y="186" font-size="10" fill="#334155">① 唯一法定權責機構：經濟部標準檢驗局</text>
          <text x="30" y="204" font-size="10" fill="#334155">② 轉讓一次為限：杜絕金融炒作與黑市倒賣</text>
          <text x="30" y="222" font-size="10" fill="#334155">③ 全電子帳號管理：產銷履歷溯源、防重複計算</text>

          <rect x="275" y="145" width="245" height="105" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
          <text x="285" y="166" font-size="11" font-weight="bold" fill="#166534">企業持有之合規用途：</text>
          <text x="285" y="186" font-size="10" fill="#334155">✓ 溫室氣體盤查範疇二 (Scope 2) 電力碳排扣抵</text>
          <text x="285" y="204" font-size="10" fill="#334155">✓ 國際 RE100 / ESG 報告書合規宣告</text>
          <text x="285" y="222" font-size="10" fill="#334155">✓ 用電大戶條款法定義務量沖銷 (需電證合一)</text>
        </svg>
        '''
    elif vtype == "re100_matrix":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">RE100 正面表列認可 vs 爭議/排除能源範疇比較表</text>

          <!-- 認可清單 (左側) -->
          <rect x="20" y="48" width="245" height="205" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="20" y="48" width="245" height="30" rx="6" fill="#15803D"/>
          <text x="142" y="68" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓ RE100 正面表列認可綠能</text>
          
          <g transform="translate(32, 92)" font-size="10" fill="#1E293B">
            <text y="0" font-weight="bold" fill="#166534">1. 太陽光電 (Solar PV)：</text>
            <text y="14" fill="#64748B" font-size="9">屋頂型、地面型、漁電共生、水面浮動型</text>
            <text y="32" font-weight="bold" fill="#166534">2. 風力發電 (Wind)：</text>
            <text y="46" fill="#64748B" font-size="9">陸域風電、離岸固定式與浮動式風場</text>
            <text y="64" font-weight="bold" fill="#166534">3. 水力發電 (Hydro)：</text>
            <text y="78" fill="#64748B" font-size="9">川流式、水庫式常規水力發電 (排除抽蓄)</text>
            <text y="96" font-weight="bold" fill="#166534">4. 地熱發電 (Geothermal)：</text>
            <text y="110" fill="#64748B" font-size="9">深層與淺層熱液蒸氣發電</text>
            <text y="128" font-weight="bold" fill="#166534">5. 生質能 (Biomass)：</text>
            <text y="142" fill="#64748B" font-size="9">符合永續認證農林剩餘物 (碳係數非0)</text>
          </g>

          <!-- 排除清單 (右側) -->
          <rect x="275" y="48" width="245" height="205" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <rect x="275" y="48" width="245" height="30" rx="6" fill="#B91C1C"/>
          <text x="397" y="68" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✕ 排除或國際爭議之能源</text>

          <g transform="translate(287, 92)" font-size="10" fill="#1E293B">
            <text y="0" font-weight="bold" fill="#991B1B">✕ 廢棄物發電 (Waste-to-Energy)：</text>
            <text y="14" fill="#64748B" font-size="9">國內法規列入，但國際 RE100 堅決不承認！</text>
            <text y="28" fill="#DC2626" font-size="8.5">（焚化過程含化石衍生塑料，碳係數非0）</text>

            <text y="48" font-weight="bold" fill="#991B1B">✕ 抽蓄水力 (Pumped Hydro)：</text>
            <text y="62" fill="#64748B" font-size="9">利用位能調峰，本質是「儲能」非綠能發電</text>

            <text y="82" font-weight="bold" fill="#991B1B">✕ 氫能發電 (Hydrogen Power)：</text>
            <text y="96" fill="#64748B" font-size="9">現階段定位為「二次能源載體」，非原生綠能</text>

            <text y="116" font-weight="bold" fill="#991B1B">✕ 核能 (Nuclear) 與化石能源：</text>
            <text y="130" fill="#64748B" font-size="9">非再生能源，不得申請 T-REC 綠電憑證</text>
          </g>
        </svg>
        '''
    elif vtype == "apply_process":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">T-REC 申請標準流程 ✕ 兩大排除紅線</text>

          <!-- 四步流程 -->
          <g transform="translate(20, 52)">
            <rect x="0" y="0" width="115" height="85" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
            <text x="57" y="24" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">第一步：備齊證明</text>
            <text x="57" y="44" font-size="9" fill="#334155" text-anchor="middle">① 設備登記證明</text>
            <text x="57" y="58" font-size="8.5" fill="#64748B" text-anchor="middle">(能源署/地方政府)</text>
            <text x="57" y="74" font-size="9" fill="#334155" text-anchor="middle">② 台電併網合約</text>

            <rect x="130" y="0" width="115" height="85" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
            <text x="187" y="24" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">第二步：查驗審查</text>
            <text x="187" y="44" font-size="9" fill="#334155" text-anchor="middle">送交官方指定</text>
            <text x="187" y="58" font-size="9" font-weight="bold" fill="#0E8A78" text-anchor="middle">3家查驗機構</text>
            <text x="187" y="74" font-size="8.5" fill="#64748B" text-anchor="middle">完成現場/書面查核</text>

            <rect x="260" y="0" width="115" height="85" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
            <text x="317" y="24" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">第三步：設立帳號</text>
            <text x="317" y="44" font-size="9" fill="#334155" text-anchor="middle">查核報告完備送件</text>
            <text x="317" y="58" font-size="9" fill="#334155" text-anchor="middle">憑證中心核驗</text>
            <text x="317" y="74" font-size="8.5" fill="#B45309" font-weight="bold" text-anchor="middle">開立正式平台帳號</text>

            <rect x="390" y="0" width="110" height="85" rx="6" fill="#FDF4FF" stroke="#A855F7" stroke-width="1.5"/>
            <text x="445" y="24" font-size="11" font-weight="bold" fill="#7E22CE" text-anchor="middle">第四步：按月核發</text>
            <text x="445" y="44" font-size="9" fill="#334155" text-anchor="middle">台電抄表計量電數</text>
            <text x="445" y="58" font-size="9" fill="#7E22CE" font-weight="bold" text-anchor="middle">按月結清發證</text>
            <text x="445" y="74" font-size="8.5" fill="#64748B" text-anchor="middle">支援零股整額入帳</text>
          </g>

          <!-- 兩大絕對排除紅線警示框 -->
          <rect x="20" y="155" width="500" height="98" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="35" y="177" font-size="12" font-weight="bold" fill="#B91C1C">🚫 法律明定「絕對排除」申請憑證之兩大主體 (嚴禁雙重受惠)：</text>
          
          <g transform="translate(35, 195)" font-size="10" fill="#334155">
            <text y="0" font-weight="bold" fill="#991B1B">① 參加台電躉購 (FIT) 機制之電廠：</text>
            <text y="14" fill="#64748B">已享受台電 20 年保證收購費率補貼者，綠電所有權已歸台電代行，不得重複申請 T-REC 憑證對外銷售。</text>
            <text y="32" font-weight="bold" fill="#991B1B">② 參加環境部溫室氣體減量抵換專案之主體：</text>
            <text y="46" fill="#64748B">已向環境部申請抵換減量額度（碳權）者，不得再申請 T-REC 綠電憑證，徹底杜絕碳效益重複計算。</text>
          </g>
        </svg>
        '''
    elif vtype == "cbam_calc":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">範疇二電力碳排扣抵算式 ✕ 歐盟 CBAM 認可漏斗</text>

          <!-- 左側算式 -->
          <rect x="20" y="48" width="250" height="205" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
          <text x="145" y="70" font-size="12" font-weight="bold" fill="#1E40AF" text-anchor="middle">範疇二 (Scope 2) 盤查計算模型</text>

          <g transform="translate(30, 95)" font-size="10" fill="#1E293B">
            <rect x="0" y="0" width="230" height="42" rx="4" fill="#DBEAFE" stroke="#3B82F6" stroke-width="1"/>
            <text x="115" y="16" font-size="9" fill="#1E40AF" text-anchor="middle">總碳排 = 灰電量 × 台電係數 ＋ 綠電量 × 0</text>
            <text x="115" y="32" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">(風光水地熱 T-REC 碳排係數 = 0)</text>

            <text y="62" font-size="10" font-weight="bold" fill="#1E40AF">現場實例試算 (年用電 2000 度)：</text>
            <text y="78" font-size="9" fill="#475569">・購買 1000 度光電憑證 ＋ 1000 度台電灰電</text>
            <text y="94" font-size="9" fill="#475569">・總碳排 = 1000 × 0.495 ＋ 1000 × 0 = 495 kg</text>
            <text y="110" font-size="9" font-weight="bold" fill="#166534">➔ 憑證直接扣抵 50% 範疇二碳排放！</text>

            <text y="130" font-size="9" font-weight="bold" fill="#DC2626">⚠️ 生質能發電特別警示：</text>
            <text y="144" font-size="8.5" fill="#64748B">生質能碳排係數非為0，需發電端實測佐證！</text>
          </g>

          <!-- 右側 CBAM 漏斗 -->
          <rect x="280" y="48" width="240" height="205" rx="6" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
          <text x="400" y="70" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">歐盟 CBAM 認可階梯漏斗</text>

          <g transform="translate(290, 88)">
            <!-- Tier 1: PPA -->
            <polygon points="10,0 210,0 190,32 30,32" fill="#059669"/>
            <text x="110" y="20" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">★ 最具說服力：實體 PPA 長約</text>

            <!-- Tier 2: 電證合一轉供 -->
            <polygon points="30,36 190,36 170,68 50,68" fill="#0D9488"/>
            <text x="110" y="56" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">次佳：電證合一電網轉供</text>

            <!-- Tier 3: 純 T-REC 憑證 -->
            <polygon points="50,72 170,72 150,104 70,104" fill="#D97706"/>
            <text x="110" y="92" font-size="9.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">審查嚴格：純 T-REC 憑證</text>

            <!-- 關鍵解讀 -->
            <rect x="5" y="115" width="210" height="42" rx="4" fill="#FFFFFF" stroke="#D97706" stroke-width="1"/>
            <text x="110" y="130" font-size="8.5" font-weight="bold" fill="#B45309" text-anchor="middle">CBAM 連歐盟 GO 憑證都不完全買單</text>
            <text x="110" y="146" font-size="8" fill="#64748B" text-anchor="middle">高度要求製造端電力直接連結性</text>
          </g>
        </svg>
        '''
    elif vtype == "market_timeline":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台灣綠電自由化演進五大里程碑 (民國 98～115 年)</text>

          <!-- 時間軸主線 -->
          <line x1="40" y1="90" x2="500" y2="90" stroke="#CBD5E1" stroke-width="4"/>

          <!-- 節點 1: 98 年 -->
          <circle cx="60" cy="90" r="10" fill="#1E40AF" stroke="#DBEAFE" stroke-width="3"/>
          <text x="60" y="70" font-size="11" font-weight="bold" fill="#1E40AF" text-anchor="middle">民國98年</text>
          <rect x="20" y="110" width="80" height="70" rx="4" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
          <text x="60" y="128" font-size="9.5" font-weight="bold" fill="#1E40AF" text-anchor="middle">FIT 躉購拓荒</text>
          <text x="60" y="144" font-size="8.5" fill="#475569" text-anchor="middle">一度光電>10元</text>
          <text x="60" y="158" font-size="8" fill="#64748B" text-anchor="middle">台電保證收20年</text>
          <text x="60" y="170" font-size="8" fill="#64748B" text-anchor="middle">全民稅金買單</text>

          <!-- 節點 2: 106 年 -->
          <circle cx="170" cy="90" r="10" fill="#0E8A78" stroke="#CCFBF1" stroke-width="3"/>
          <text x="170" y="70" font-size="11" font-weight="bold" fill="#0E8A78" text-anchor="middle">民國106年</text>
          <rect x="130" y="110" width="80" height="70" rx="4" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
          <text x="170" y="128" font-size="9.5" font-weight="bold" fill="#0E8A78" text-anchor="middle">電業法修法</text>
          <text x="170" y="144" font-size="8.5" fill="#475569" text-anchor="middle">「綠電先行」</text>
          <text x="170" y="158" font-size="8" fill="#64748B" text-anchor="middle">開放自由交易</text>
          <text x="170" y="170" font-size="8" fill="#64748B" text-anchor="middle">T-REC憑證成立</text>

          <!-- 節點 3: 109 年 -->
          <circle cx="280" cy="90" r="10" fill="#D97706" stroke="#FEF3C7" stroke-width="3"/>
          <text x="280" y="70" font-size="11" font-weight="bold" fill="#D97706" text-anchor="middle">民國109年</text>
          <rect x="240" y="110" width="80" height="70" rx="4" fill="#FEFCE8" stroke="#FDE68A" stroke-width="1"/>
          <text x="280" y="128" font-size="9.5" font-weight="bold" fill="#D97706" text-anchor="middle">PPA 直轉工商轉</text>
          <text x="280" y="144" font-size="8.5" fill="#475569" text-anchor="middle">台電電網代輸</text>
          <text x="280" y="158" font-size="8" fill="#64748B" text-anchor="middle">大企業長約入市</text>
          <text x="280" y="170" font-size="8" fill="#64748B" text-anchor="middle">交易量突破性成長</text>

          <!-- 節點 4: 113 年 -->
          <circle cx="390" cy="90" r="10" fill="#7C3AED" stroke="#EDE9FE" stroke-width="3"/>
          <text x="390" y="70" font-size="11" font-weight="bold" fill="#7C3AED" text-anchor="middle">民國113年</text>
          <rect x="350" y="110" width="80" height="70" rx="4" fill="#FAF5FF" stroke="#DDD6FE" stroke-width="1"/>
          <text x="390" y="128" font-size="9.5" font-weight="bold" fill="#7C3AED" text-anchor="middle">二三型售電鬆綁</text>
          <text x="390" y="144" font-size="8.5" fill="#475569" text-anchor="middle">免轉一型發電業</text>
          <text x="390" y="158" font-size="8" fill="#64748B" text-anchor="middle">釋放「螞蟻雄兵」</text>
          <text x="390" y="170" font-size="8" fill="#64748B" text-anchor="middle">屋頂光電湧入市場</text>

          <!-- 節點 5: 115 年 -->
          <circle cx="480" cy="90" r="10" fill="#059669" stroke="#D1FAE5" stroke-width="3"/>
          <text x="480" y="70" font-size="11" font-weight="bold" fill="#059669" text-anchor="middle">民國115年</text>
          <rect x="440" y="110" width="80" height="70" rx="4" fill="#F0FDF4" stroke="#A7F3D0" stroke-width="1"/>
          <text x="480" y="128" font-size="9.5" font-weight="bold" fill="#059669" text-anchor="middle">零股化✕沙盒3.0</text>
          <text x="480" y="144" font-size="8.5" fill="#475569" text-anchor="middle">按月結清無滾存</text>
          <text x="480" y="158" font-size="8" fill="#64748B" text-anchor="middle">事後彈性劃撥</text>
          <text x="480" y="170" font-size="8" fill="#64748B" text-anchor="middle">資料費狂降98%</text>

          <!-- 結論註解 -->
          <rect x="20" y="195" width="500" height="55" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
          <text x="30" y="215" font-size="10" font-weight="bold" fill="#1B365D">演進核心主軸：</text>
          <text x="30" y="235" font-size="9" fill="#475569">從「單一政府躉購定價」完全轉型為「多主體市場化撮合」；門檻步步下放，讓全民與中小企業均能享受綠電自由。</text>
        </svg>
        '''
    elif vtype == "trading_routes":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台灣綠電市場三大體系與四大流通拓撲圖</text>

          <!-- 4A: 自發自用 -->
          <rect x="20" y="52" width="115" height="195" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="20" y="52" width="115" height="26" rx="6" fill="#1D4ED8"/>
          <text x="77" y="70" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4A 自發自用</text>
          <g transform="translate(28, 90)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【電證合一內耗】</text>
            <text y="18">・電廠：工廠屋頂</text>
            <text y="34">・電量：廠內全自用</text>
            <text y="50">・憑證：留廠自用</text>
            <text y="68" font-weight="bold" fill="#166534">效益：</text>
            <text y="84">✓ 抵扣範疇二</text>
            <text y="100">✓ 省下電網代輸費</text>
            <text y="116">✓ 免除轉供損耗</text>
            <text y="132" font-size="8" fill="#64748B">最單純自給自足模式</text>
          </g>

          <!-- 4B: 電證分離 -->
          <rect x="145" y="52" width="115" height="195" rx="6" fill="#F0FDFA" stroke="#0E8A78" stroke-width="1.5"/>
          <rect x="145" y="52" width="115" height="26" rx="6" fill="#0F766E"/>
          <text x="202" y="70" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4B 電證分離</text>
          <g transform="translate(153, 90)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#0F766E">【電自己用・證賣掉】</text>
            <text y="18">・電量：廠內自行消耗</text>
            <text y="34">・憑證：上架中心交易</text>
            <text y="50">・買方：純買憑證者</text>
            <text y="68" font-weight="bold" fill="#D97706">特性：</text>
            <text y="84">✓ 現貨平台直接下單</text>
            <text y="100">✓ 憑證變現補貼電費</text>
            <text y="116" font-size="8" fill="#DC2626">⚠️ CBAM 接受度較低</text>
            <text y="132" font-size="8" fill="#64748B">國內早期最活躍交易</text>
          </g>

          <!-- 直轉供 PPA -->
          <rect x="270" y="52" width="125" height="195" rx="6" fill="#FEFCE8" stroke="#CA8A04" stroke-width="1.5"/>
          <rect x="270" y="52" width="125" height="26" rx="6" fill="#A16207"/>
          <text x="332" y="70" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1/2/3 直轉供 PPA</text>
          <g transform="translate(278, 90)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#A16207">【電證合一電網代輸】</text>
            <text y="18">・電廠：大型地面/風場</text>
            <text y="34">・代輸：台電輸配電網</text>
            <text y="50">・交割：電證同步移轉</text>
            <text y="68" font-weight="bold" fill="#15803D">優勢：</text>
            <text y="84">✓ 規模化大宗供電</text>
            <text y="100">✓ 國際 RE100 滿分認可</text>
            <text y="116">✓ CBAM 最高抵禦力</text>
            <text y="132" font-size="8" fill="#64748B">大企業合規主流方案</text>
          </g>

          <!-- 售電業中介 -->
          <rect x="405" y="52" width="115" height="195" rx="6" fill="#FAF5FF" stroke="#9333EA" stroke-width="1.5"/>
          <rect x="405" y="52" width="115" height="26" rx="6" fill="#7E22CE"/>
          <text x="462" y="70" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">售電業中介代銷</text>
          <g transform="translate(413, 90)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#7E22CE">【螞蟻雄兵聚合器】</text>
            <text y="18">・上游：二三型小型光電</text>
            <text y="34">・下游：信評不足中小企</text>
            <text y="50">・加值：供需曲線配比</text>
            <text y="68" font-weight="bold" fill="#7E22CE">核心價值：</text>
            <text y="84">✓ 消滅週末余電</text>
            <text y="100">✓ 承擔信用風險</text>
            <text y="116">✓ 提供彈性合約</text>
            <text y="132" font-size="8" fill="#64748B">綠電普及化關鍵中樞</text>
          </g>
        </svg>
        '''
    elif vtype == "deregulation_ants":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">二三型自用發電設備售電鬆綁政策前後對比</text>

          <!-- 舊制 (左側) -->
          <rect x="20" y="50" width="245" height="200" rx="6" fill="#FEF2F2" stroke="#F87171" stroke-width="1.5"/>
          <rect x="20" y="50" width="245" height="30" rx="6" fill="#DC2626"/>
          <text x="142" y="70" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✕ 舊制：二三型轉一型發電業</text>

          <g transform="translate(32, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#B91C1C">【層層關卡・成本極高】</text>
            <text y="20">1. 重新向能源署申請變更執照</text>
            <text y="38">2. 跨部會專家學者大批委員現場現勘審查</text>
            <text y="56">3. 強制改裝大型消防設施與增設安全防護</text>
            <text y="74">4. 必須設置「專任主任技術員」常駐</text>
            <text y="92">5. 每月提報繁瑣營運月報與物料報表</text>
            <text y="116" font-size="10" font-weight="bold" fill="#DC2626">➔ 小型屋頂電廠不堪負荷，無人願轉！</text>
          </g>

          <!-- 新制 (右側) -->
          <rect x="275" y="50" width="245" height="200" rx="6" fill="#F0FDF4" stroke="#4ADE80" stroke-width="1.5"/>
          <rect x="275" y="50" width="245" height="30" rx="6" fill="#16A34A"/>
          <text x="397" y="70" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓ 新制：能源署函令直接鬆綁</text>

          <g transform="translate(287, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#15803D">【免變更執照・直通自由市場】</text>
            <text y="20">1. 免變更執照：維持二三型自用設備身分</text>
            <text y="38">2. 免專家委員會現場嚴苛會審</text>
            <text y="56">3. 免聘請高薪主任技術員、免繁複月報</text>
            <text y="74">4. 唯一動作：與合格「售電業」簽署代銷合約</text>
            <text y="92">5. 售電業統整後直接將綠電轉供至用戶端</text>
            <text y="116" font-size="10" font-weight="bold" fill="#15803D">➔ 釋放百萬瓩「螞蟻雄兵」，交易量倍增！</text>
          </g>
        </svg>
        '''
    elif vtype == "platform_realities":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">憑證交易專區雙板塊運作實務：「存憑證」現貨 vs「店家證」線下私約</text>

          <!-- 板塊 1: 存憑證 -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="30" rx="6" fill="#047857"/>
          <text x="142" y="72" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">專區一：存憑證 (現貨市場・熱絡)</text>

          <g transform="translate(37, 98)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#065F46">【交易標的：已核發完成之現成憑證】</text>
            <text y="18">・主要來源：4B 自發自用已發出之憑證</text>
            <text y="36">・交易特性：標準化、明碼標價、現貨成交</text>
            <text y="54">・操作方式：買賣雙方註冊會員，線上即時點選</text>
            <text y="72">・交割流程：平台帳號直接扣款劃撥過戶</text>
            <text y="94" font-size="10" font-weight="bold" fill="#047857">市場狀態：成交熱絡，中小企業搶購熱烈！</text>
            <text y="110" font-size="8.5" fill="#64748B">適合短期急需 ESG 報告或抵扣年度碳排者</text>
          </g>

          <!-- 板塊 2: 店家證 -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#FEFCE8" stroke="#FDE047" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="30" rx="6" fill="#B45309"/>
          <text x="397" y="72" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">專區二：店家證 (PPA 媒合・私下約定)</text>

          <g transform="translate(292, 98)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#92400E">【交易標的：未來電證綁定長期合約】</text>
            <text y="18">・主要來源：新建電廠 5~20 年長期購售電</text>
            <text y="36">・為何線上掛零？PPA 條款極其複雜：</text>
            <text y="52" fill="#B45309">  - 發用電時序匹配、余電由誰吸收</text>
            <text y="68" fill="#B45309">  - 違約保證金、台電代輸費分攤計算</text>
            <text y="86">・實務運作：線上僅供展示，全部轉入線下深度洽談</text>
            <text y="104" font-size="10" font-weight="bold" fill="#B45309">市場狀態：線上0筆，但線下私約巨量成交！</text>
            <text y="120" font-size="8.5" fill="#64748B">平台僅扮演最終合約備查與憑證撥付中樞</text>
          </g>
        </svg>
        '''
    elif vtype == "pricing_ladder":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">綠電自由市場價格形成堆疊模型 (階梯定價原理)</text>

          <!-- 階梯 1: FIT 基底 -->
          <rect x="30" y="170" width="140" height="75" rx="4" fill="#DBEAFE" stroke="#3B82F6" stroke-width="1.5"/>
          <text x="100" y="195" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">第 1 層：FIT 基準</text>
          <text x="100" y="215" font-size="10" font-weight="bold" fill="#1E40AF" text-anchor="middle">3.5 ～ 5.6 元/度</text>
          <text x="100" y="232" font-size="8" fill="#64748B" text-anchor="middle">(台電保證收購20年地板價)</text>

          <!-- 箭頭 1 -->
          <path d="M 175 190 L 195 160" stroke="#CBD5E1" stroke-width="2" marker-end="url(#arrow)"/>

          <!-- 階梯 2: 法定加成 -->
          <rect x="200" y="115" width="140" height="75" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="270" y="138" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">第 2 層：法定加成</text>
          <text x="270" y="156" font-size="10" font-weight="bold" fill="#92400E" text-anchor="middle">+6% ～ +27%</text>
          <text x="270" y="172" font-size="8" fill="#64748B" text-anchor="middle">VPC模組/北部/風雨球場</text>

          <!-- 箭頭 2 -->
          <path d="M 345 140 L 365 110" stroke="#CBD5E1" stroke-width="2"/>

          <!-- 階梯 3: 自由市場終端 -->
          <rect x="370" y="60" width="145" height="85" rx="4" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
          <text x="442" y="85" font-size="12" font-weight="bold" fill="#15803D" text-anchor="middle">終端自由市場售價</text>
          <text x="442" y="108" font-size="13" font-weight="bold" fill="#166534" text-anchor="middle">4.8 ～ 6.5 元/度</text>
          <text x="442" y="125" font-size="8.5" fill="#475569" text-anchor="middle">含售電服務費 ＋ 風險溢價</text>

          <!-- 下方文字解釋 -->
          <rect x="30" y="195" width="485" height="1" fill="#E2E8F0"/>
          <text x="30" y="258" font-size="9" fill="#64748B">
            * 價格邏輯：售電業賣給民間必須高於電廠賣給台電的「FIT ＋ 加成總和」，否則發電業毫無動機解約投入自由市場。
          </text>
        </svg>
        '''
    elif vtype == "taipower_credit":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台資電 (台灣智慧電網公司) 統購分銷破局示意圖</text>

          <!-- 左側痛點：聯貸銀行高門檻 -->
          <rect x="20" y="52" width="225" height="195" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <rect x="20" y="52" width="225" height="28" rx="6" fill="#DC2626"/>
          <text x="132" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">傳統大型電廠 PPA 困境</text>
          
          <g transform="translate(30, 95)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#991B1B">大型電廠 (數百億聯貸案)：</text>
            <text y="16">・銀行團嚴苛限制：PPA 買方必須</text>
            <text y="30" font-weight="bold" fill="#DC2626">  具備頂級信用評等 (AAA級)</text>
            <text y="48">・中小企業信用不足：即便出高價，</text>
            <text y="62" fill="#B91C1C">  亦因信評門檻遭銀行團一票否決！</text>
            <text y="82" font-weight="bold" fill="#991B1B">結果：</text>
            <text y="98">綠電全數被少數半導體龍頭包攬，</text>
            <text y="114">廣大中小企業面臨「有錢買不到」斷糧危機。</text>
          </g>

          <!-- 右側解方：台資電統購分銷 -->
          <rect x="260" y="52" width="260" height="195" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="260" y="52" width="260" height="28" rx="6" fill="#16A34A"/>
          <text x="390" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">台資電統購分銷破局解法</text>

          <g transform="translate(272, 95)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#15803D">台資電 (台灣智慧電網公司) 角色：</text>
            <text y="16">① 國營信用擔保：以公法人信評出面統購</text>
            <text y="30">   向大型離岸/光電案場承接大額綠電。</text>
            <text y="48">② 商品化切片拆分：將大額長約切分為</text>
            <text y="62" font-weight="bold" fill="#047857">   小額度 (1萬度起)、短期限標準商品。</text>
            <text y="80">③ 開放中小企業零售：無信評門檻負擔，</text>
            <text y="96">   一般製造業皆可依自身電耗公平採購！</text>
            <text y="116" font-size="9.5" font-weight="bold" fill="#166534">➔ 充當國家級信用蓄水池，普及綠電！</text>
          </g>
        </svg>
        '''
    elif vtype == "small_green_matrix":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電小額綠電產品規格矩陣 ✕ 實戰練兵價值</text>

          <!-- 矩陣卡片 1: 產品規格 -->
          <rect x="25" y="52" width="235" height="195" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
          <rect x="25" y="52" width="235" height="28" rx="6" fill="#1D4ED8"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">台電小額綠電產品規格</text>
          
          <g transform="translate(37, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">・銷售額度：</text>
            <text y="16">  1 萬度 / 20 萬度 (專為中小用戶設計)</text>
            <text y="36" font-weight="bold" fill="#1E40AF">・合約期限：</text>
            <text y="52">  1 年期 / 5 年期 (彈性短約、無長期套牢風險)</text>
            <text y="72" font-weight="bold" fill="#1E40AF">・價格區間：</text>
            <text y="88">  每度約 5 ～ 6 元 (區分全日型/昨日先行)</text>
            <text y="108" font-weight="bold" fill="#1E40AF">・銷售渠道：</text>
            <text y="124">  2025 年起改由台電官網直接對外受理</text>
          </g>

          <!-- 矩陣卡片 2: 核心戰略意義 -->
          <rect x="280" y="52" width="235" height="195" rx="6" fill="#FEF3C7" stroke="#FCD34D" stroke-width="1.5"/>
          <rect x="280" y="52" width="235" height="28" rx="6" fill="#D97706"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">張科長解密：中小企業實戰練兵場</text>

          <g transform="translate(292, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#B45309">① 摸清定型化契約眉角：</text>
            <text y="16">   藉由台電嚴謹合約，學習轉供計量、責任劃分</text>
            <text y="30">   與罰則條款，累積法務與採購實務經驗。</text>
            <text y="50" font-weight="bold" fill="#B45309">② 零信用違約風險：</text>
            <text y="66">   交易對手為國營台電，供電穩定且無倒閉風險。</text>
            <text y="86" font-weight="bold" fill="#B45309">③ 為民間大約奠定談判基礎：</text>
            <text y="102">   練兵結束後，日後洽談民間售電業 PPA 時，</text>
            <text y="116" font-weight="bold" fill="#B45309">   方能精準提出自我權益保護條款！</text>
          </g>
        </svg>
        '''
    elif vtype == "bidding_market":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">中小企業平價綠電競標 ✕ 綠電市集全台地圖</text>

          <!-- 左側：平價競標參數 -->
          <rect x="20" y="52" width="245" height="195" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="20" y="52" width="245" height="28" rx="6" fill="#16A34A"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">平價綠電競標核心參數</text>

          <g transform="translate(32, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#15803D">・超優惠底價：每度 4.3 元</text>
            <text y="16" fill="#64748B">(遠低於一般自由市場 5.5~6 元行情)</text>
            <text y="36" font-weight="bold" fill="#15803D">・投標資格硬門檻：</text>
            <text y="52">  資本額 ≤ 1 億元新台幣</text>
            <text y="68">  且員工總人數未滿 200 人中小企業</text>
            <text y="88" font-weight="bold" fill="#15803D">・投標額度上限：</text>
            <text y="104">  單一企業前一年度總用電量的 30%</text>
            <text y="124" font-size="9" fill="#15803D" font-weight="bold">➔ 每年 7~8 月開標，外銷小巨人務必把握！</text>
          </g>

          <!-- 右側：綠電市集地圖 -->
          <rect x="275" y="52" width="245" height="195" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
          <rect x="275" y="52" width="245" height="28" rx="6" fill="#2563EB"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">小農式「綠電市集」巡迴特點</text>

          <g transform="translate(287, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1D4ED8">・全台四大核心都會巡迴：</text>
            <text y="16">  已完成：台中場、高雄場</text>
            <text y="32">  巡迴中：台北場、桃園場</text>
            <text y="52" font-weight="bold" fill="#1D4ED8">・免預約・現場直接對接：</text>
            <text y="68">  如農夫市集擺攤，多家合格售電業駐點</text>
            <text y="88" font-weight="bold" fill="#1D4ED8">・現場官方最新政策宣講：</text>
            <text y="104">  標檢局專家駐場解惑，消除資訊不對稱</text>
            <text y="124" font-size="9" fill="#1D4ED8" font-weight="bold">➔ 免門檻現場媒合，加速簽約成案！</text>
          </g>
        </svg>
        '''
    elif vtype == "tenant_101":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">無電號租戶綠電突圍模式 (台北 101 大樓實例)</text>

          <!-- 模式 1.0 -->
          <rect x="20" y="50" width="245" height="200" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
          <rect x="20" y="50" width="245" height="30" rx="6" fill="#1E40AF"/>
          <text x="142" y="70" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1.0 單租戶突破模式 (110年上路)</text>

          <g transform="translate(32, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【痛點：無獨立電號無法轉供】</text>
            <text y="18">・突破機制：</text>
            <text y="34">  ① 租戶取得大樓房東書面同意書</text>
            <text y="50">  ② 委託中間售電業對接綠電</text>
            <text y="66">  ③ 大樓管委會協助依私表拆分度數</text>
            <text y="86" font-weight="bold" fill="#1E40AF">・實績成果：</text>
            <text y="102">  截至去年累計轉供量突破</text>
            <text y="118" font-size="11" font-weight="bold" fill="#1D4ED8">  800 萬度綠電！</text>
          </g>

          <!-- 模式 2.0 -->
          <rect x="275" y="50" width="245" height="200" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="275" y="50" width="245" height="30" rx="6" fill="#15803D"/>
          <text x="397" y="70" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2.0 綠色大樓團購模式 (商機爆發)</text>

          <g transform="translate(287, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#166534">【升級：房東統籌團購賦能全棟】</text>
            <text y="18">・升級機制：</text>
            <text y="34">  ① 房東統一出面與發電廠簽大約 PPA</text>
            <text y="50">  ② 打造「綠色大樓」品牌，提高租金溢價</text>
            <text y="66">  ③ 進駐租戶全員共享綠電與 ESG 榮耀</text>
            <text y="86" font-weight="bold" fill="#166534">・實績成果：</text>
            <text y="102">  截至去年累計轉供量驚人突破</text>
            <text y="118" font-size="12" font-weight="bold" fill="#15803D">  2 億度綠電！(成效翻 25 倍)</text>
          </g>
        </svg>
        '''
    elif vtype == "mismatch_curves":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">綠電供給與用戶消費時空雙重錯配示意圖</text>

          <!-- 季節曲線錯配 -->
          <g transform="translate(25, 52)">
            <rect x="0" y="0" width="235" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
            <text x="117" y="18" font-size="10" font-weight="bold" fill="#1B365D" text-anchor="middle">季節特性錯配 (光電 vs 風電)</text>
            <path d="M 20 80 Q 70 25 120 25 T 215 80" fill="none" stroke="#F59E0B" stroke-width="2.5"/>
            <text x="120" y="42" font-size="8.5" font-weight="bold" fill="#D97706" text-anchor="middle">光電：5~8月夏季盛暑</text>
            <path d="M 20 40 Q 60 75 110 75 T 215 35" fill="none" stroke="#3B82F6" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="175" y="28" font-size="8" font-weight="bold" fill="#2563EB">風電：冬季季風</text>
            <text x="117" y="98" font-size="8" fill="#64748B" text-anchor="middle">水力發電則全年度相對均勻</text>
          </g>

          <!-- 週間作息錯配 -->
          <g transform="translate(280, 52)">
            <rect x="0" y="0" width="235" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
            <text x="117" y="18" font-size="10" font-weight="bold" fill="#1B365D" text-anchor="middle">週間作息錯配 (平日 vs 週末)</text>
            <!-- 平日柱狀高，週末落底 -->
            <rect x="30" y="40" width="20" height="50" fill="#10B981"/>
            <rect x="60" y="40" width="20" height="50" fill="#10B981"/>
            <rect x="90" y="40" width="20" height="50" fill="#10B981"/>
            <rect x="120" y="40" width="20" height="50" fill="#10B981"/>
            <rect x="150" y="40" width="20" height="50" fill="#10B981"/>
            <rect x="180" y="80" width="18" height="10" fill="#EF4444"/>
            <rect x="202" y="80" width="18" height="10" fill="#EF4444"/>
            <text x="90" y="34" font-size="8" fill="#15803D" text-anchor="middle">週一~週五負載滿載</text>
            <text x="195" y="74" font-size="8" font-weight="bold" fill="#DC2626" text-anchor="middle">週末余電</text>
          </g>

          <!-- 核心痛點與售電業價值 -->
          <rect x="25" y="172" width="490" height="85" rx="6" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1"/>
          <text x="35" y="192" font-size="10.5" font-weight="bold" fill="#92400E">余電痛點與售電業不可或缺價值：</text>
          <text x="35" y="210" font-size="9" fill="#334155">① 余電陷阱：工廠週六日放假、太陽依舊發電，若未搭配儲能或風電，大量綠電淪為無效余電。</text>
          <text x="35" y="226" font-size="9" fill="#334155">② 售電業價值：運用風光互補演算法，為商辦/製造業客製多元綠電套餐，徹底平抑時空錯配！</text>
          <text x="35" y="242" font-size="8.5" font-weight="bold" fill="#B45309">➔ 綠電無法「一鍵線上刷卡採購」，中介最佳化配置才是核心技術！</text>
        </svg>
        '''
    elif vtype == "wheeling_four_buckets":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電轉供 15 分鐘計量與四大時段「密封水桶」規則</text>

          <!-- 四個水桶 -->
          <g transform="translate(20, 52)">
            <!-- 水桶 1 -->
            <rect x="0" y="0" width="115" height="110" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="57" y="22" font-size="11" font-weight="bold" fill="#B91C1C" text-anchor="middle">週間尖峰</text>
            <text x="57" y="40" font-size="8.5" fill="#64748B" text-anchor="middle">週一至週五 16~22h</text>
            <rect x="15" y="52" width="85" height="45" rx="4" fill="#FEE2E2"/>
            <text x="57" y="70" font-size="9" font-weight="bold" fill="#991B1B" text-anchor="middle">獨立水桶 A</text>
            <text x="57" y="85" font-size="8" fill="#DC2626" text-anchor="middle">嚴禁跨時段挪用</text>

            <!-- 水桶 2 -->
            <rect x="130" y="0" width="115" height="110" rx="6" fill="#FEFCE8" stroke="#F59E0B" stroke-width="1.5"/>
            <text x="187" y="22" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">週間半尖峰</text>
            <text x="187" y="40" font-size="8.5" fill="#64748B" text-anchor="middle">週一至週五 日間時段</text>
            <rect x="145" y="52" width="85" height="45" rx="4" fill="#FEF3C7"/>
            <text x="187" y="70" font-size="9" font-weight="bold" fill="#92400E" text-anchor="middle">獨立水桶 B</text>
            <text x="187" y="85" font-size="8" fill="#D97706" text-anchor="middle">光電主力產出區</text>

            <!-- 水桶 3 -->
            <rect x="260" y="0" width="115" height="110" rx="6" fill="#F0FDFA" stroke="#0E8A78" stroke-width="1.5"/>
            <text x="317" y="22" font-size="11" font-weight="bold" fill="#0F766E" text-anchor="middle">週六半尖峰</text>
            <text x="317" y="40" font-size="8.5" fill="#64748B" text-anchor="middle">週六專屬時段</text>
            <rect x="275" y="52" width="85" height="45" rx="4" fill="#CCFBF1"/>
            <text x="317" y="70" font-size="9" font-weight="bold" fill="#0E8A78" text-anchor="middle">獨立水桶 C</text>
            <text x="317" y="85" font-size="8" fill="#0D9488" text-anchor="middle">商辦最易余電</text>

            <!-- 水桶 4 -->
            <rect x="390" y="0" width="115" height="110" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
            <text x="447" y="22" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">離峰時段</text>
            <text x="447" y="40" font-size="8.5" fill="#64748B" text-anchor="middle">深夜與週日全天</text>
            <rect x="405" y="52" width="85" height="45" rx="4" fill="#DBEAFE"/>
            <text x="447" y="70" font-size="9" font-weight="bold" fill="#1E40AF" text-anchor="middle">獨立水桶 D</text>
            <text x="447" y="85" font-size="8" fill="#2563EB" text-anchor="middle">風電充裕時段</text>
          </g>

          <!-- 結算機制說明 -->
          <rect x="20" y="172" width="500" height="85" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="35" y="192" font-size="10" font-weight="bold" fill="#1B365D">台電轉供結算兩大鐵律：</text>
          <text x="35" y="210" font-size="9" fill="#334155">1. 15 分鐘即時比對：發電大於用電視為余電；發電不足用電自動補入台電灰電。</text>
          <text x="35" y="226" font-size="9" fill="#334155">2. 當月同區間「二次彌合」：未用完余電僅能在「當月同一個時段水桶」內互相填補，絕不可跨桶互抵！</text>
          <text x="35" y="242" font-size="8.5" fill="#64748B">（例如週六半尖峰的太陽光電余電，只能填補其他週六的半尖峰缺口，無法支援週三夜尖峰）</text>
        </svg>
        '''
    elif vtype == "sandbox_3":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">台電沙盒 3.0 彈性分配革命 (2026年10月新制)</text>

          <!-- 舊制 (左側) -->
          <rect x="20" y="50" width="245" height="140" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <text x="142" y="70" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">✕ 舊制：事前合約固定比例</text>
          <g transform="translate(30, 88)" font-size="9" fill="#334155">
            <text y="0">・事前在合約綁死各電號分配比例 (如50%/50%)</text>
            <text y="16">・產線歲修或訂單波動時，電號間無法互相調配</text>
            <text y="32">・每次調配必須重新修約，耗時數月</text>
            <text y="48" font-weight="bold" fill="#DC2626">➔ 結果：大量余電被浪費，合約極度僵化！</text>
          </g>

          <!-- 新制沙盒 3.0 (右側) -->
          <rect x="275" y="50" width="245" height="140" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <text x="397" y="70" font-size="11" font-weight="bold" fill="#15803D" text-anchor="middle">✓ 沙盒 3.0：事後自主彈性分配</text>
          <g transform="translate(285, 88)" font-size="9" fill="#334155">
            <text y="0">・月結後「事後自由分配」：掌握主導權</text>
            <text y="16">・綠電優先灌頂給外銷稽核電號 (如蘋果 RE100 廠)</text>
            <text y="32">・剩餘電量自動分攤給一般廠區，余電趨近於零</text>
            <text y="48" font-weight="bold" fill="#15803D">➔ 結果：企業自主操盤，余電大幅消滅！</text>
          </g>

          <!-- 下方費用暴降對照表 -->
          <rect x="20" y="198" width="500" height="60" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <text x="35" y="216" font-size="10.5" font-weight="bold" fill="#1D4ED8">規費斷崖式大降 98% 實況對照：</text>
          <text x="35" y="234" font-size="9.5" fill="#334155">・小規模電號用戶資料提供費：自原本數十萬元 ➔ 暴降為 <strong style="color:#1D4ED8;">2 萬元</strong>！</text>
          <text x="35" y="250" font-size="9.5" fill="#334155">・1,000 電號以上集團大戶資料提供費：自原本 120 萬元 ➔ 暴降為 <strong style="color:#059669;">2.4 萬元</strong> (降幅98%)！</text>
        </svg>
        '''
    elif vtype == "fractional_trec":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">2026 綠電零股化新制：按月結清告別跨年滾存</text>

          <!-- 舊制滾存問題 (左側) -->
          <rect x="20" y="52" width="245" height="195" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <rect x="20" y="52" width="245" height="28" rx="6" fill="#DC2626"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✕ 舊制：1,000 度整數發證</text>

          <g transform="translate(30, 95)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#991B1B">【零頭跨月滾存之痛】</text>
            <text y="16">・舊制以 1,000 度為一張發證單位</text>
            <text y="32">・未滿 1,000 度之零頭滾入次月累計</text>
            <text y="48" font-weight="bold" fill="#DC2626">致命痛點：跨年度年份歸屬大混亂！</text>
            <text y="64">・12 月發電產生之 1 度零頭，被迫滾入隔年 1 月</text>
            <text y="80">・與 1 月之 999 度混成一張新憑證</text>
            <text y="96">・企業申報碳排時，12 月的電被算在隔年</text>
            <text y="112" font-weight="bold" fill="#B91C1C">➔ 跨國客戶會計稽核判定不合格！</text>
          </g>

          <!-- 新制零股化 (右側) -->
          <rect x="275" y="52" width="245" height="195" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="275" y="52" width="245" height="28" rx="6" fill="#16A34A"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓ 2026 新制：按月獨立零股結清</text>

          <g transform="translate(285, 95)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#15803D">【當月結清・零頭全發】</text>
            <text y="16">・當月無論發幾度，全部獨立核發對應憑證！</text>
            <text y="32">・一張 1,000 度，零頭 15 度亦單獨核發零股證</text>
            <text y="48" font-weight="bold" fill="#166534">完美對齊全球客戶多元會計年度：</text>
            <text y="64">・美商財年 (結算於 6/7 月) ➔ 自由選取</text>
            <text y="80">・日商財年 (結算於 3/4 月) ➔ 自由選取</text>
            <text y="96">・任意連續 12 個月自由拼接申報</text>
            <text y="112" font-weight="bold" fill="#059669">➔ 徹底終結跨年爭議，市場反響極度正向！</text>
          </g>
        </svg>
        '''
    elif vtype == "audit_reform":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">2026 年 7 月憑證查核機制雙重改革拓撲圖</text>

          <!-- 改革一：取消分區 -->
          <rect x="20" y="52" width="245" height="195" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
          <rect x="20" y="52" width="245" height="28" rx="6" fill="#1D4ED8"/>
          <text x="142" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">革新一：全面打破北中南區域壁壘</text>

          <g transform="translate(32, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#1E40AF">【舊制痛點：強行依地緣分區】</text>
            <text y="18">・原本 3 家官方認可查驗機構劃分北中南</text>
            <text y="34">・業者無從跨區選擇熟悉或配合良好的機構</text>
            <text y="54" font-weight="bold" fill="#166534">【新制鬆綁：全台 3 家自由挑選】</text>
            <text y="72">・2026 年 7 月起廢止分區限制！</text>
            <text y="88">・業者可依服務排程、收費與配合度</text>
            <text y="104">  跨區自由委託任何一家查驗機構</text>
            <text y="124" font-size="9" font-weight="bold" fill="#1D4ED8">➔ 引進良性市場競爭，查核效率大躍進！</text>
          </g>

          <!-- 改革二：1MW 自撰報告 -->
          <rect x="275" y="52" width="245" height="195" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
          <rect x="275" y="52" width="245" height="28" rx="6" fill="#16A34A"/>
          <text x="397" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">革新二：1MW 以下案場自撰報告加速</text>

          <g transform="translate(287, 95)" font-size="9.5" fill="#334155">
            <text y="0" font-weight="bold" fill="#15803D">【舊制痛點：排隊等待現場查核耗時】</text>
            <text y="18">・小型案場往往因查驗排程拖延數月發證</text>
            <text y="38" font-weight="bold" fill="#15803D">【新制鬆綁：書審先行・後補抽驗】</text>
            <text y="56">・裝機容量 1MW 以下案場，業者可自行撰寫</text>
            <text y="72">  合格查核報告送件至憑證中心</text>
            <text y="88">・書審完畢即行開立發證，快速入市流通！</text>
            <text y="104">・事後補做現場差額抽檢查核以保真實性</text>
            <text y="124" font-size="9" font-weight="bold" fill="#166534">➔ 發證等待期由數月壓縮至數週！</text>
          </g>
        </svg>
        '''
    elif vtype == "three_upcoming_laws":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="32" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">即將落地三大法規新政 (預計 2026 年底前正式公告實施)</text>

          <!-- 卡片 1 -->
          <rect x="20" y="52" width="160" height="195" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
          <rect x="20" y="52" width="160" height="28" rx="6" fill="#1E40AF"/>
          <text x="100" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">新政一：余電核發憑證</text>
          <g transform="translate(28, 92)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#1D4ED8">【消滅余電無效浪費】</text>
            <text y="18">・現行痛點：</text>
            <text y="32">  未被用戶用完之余電，</text>
            <text y="46">  若未賣給台電無法發證。</text>
            <text y="66" font-weight="bold" fill="#166534">・年底修法突破：</text>
            <text y="80">  只要業者放棄台電躉購，</text>
            <text y="96">  超額余電亦可全數核發</text>
            <text y="112" font-weight="bold" fill="#047857">  T-REC 綠電憑證！</text>
            <text y="132" font-size="8" fill="#64748B">法規已於4/9預告</text>
          </g>

          <!-- 卡片 2 -->
          <rect x="190" y="52" width="160" height="195" rx="6" fill="#FEFCE8" stroke="#F59E0B" stroke-width="1.5"/>
          <rect x="190" y="52" width="160" height="28" rx="6" fill="#D97706"/>
          <text x="270" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">新政二：電表拍照追溯</text>
          <g transform="translate(198, 92)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#B45309">【消滅審查真空期】</text>
            <text y="18">・現行痛點：</text>
            <text y="32">  電廠解約 FIT 改賣綠電，</text>
            <text y="46">  等候審查 1 個月電量浪費。</text>
            <text y="66" font-weight="bold" fill="#B45309">・即將上路規定：</text>
            <text y="80">  解約次日拍照存證電表，</text>
            <text y="96">  日後憑證起算點直接追溯</text>
            <text y="112" font-weight="bold" fill="#B45309">  至解約當日！</text>
            <text y="132" font-size="8" fill="#64748B">1度綠電都不浪費</text>
          </g>

          <!-- 卡片 3 -->
          <rect x="360" y="52" width="160" height="195" rx="6" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5"/>
          <rect x="360" y="52" width="160" height="28" rx="6" fill="#059669"/>
          <text x="440" y="71" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">新政三：多主體拆分</text>
          <g transform="translate(368, 92)" font-size="9" fill="#334155">
            <text y="0" font-weight="bold" fill="#047857">【破解合資案場分配】</text>
            <text y="18">・現行痛點：</text>
            <text y="32">  如南軟多家合資建光電，</text>
            <text y="46">  單一電號憑證全歸管委會。</text>
            <text y="66" font-weight="bold" fill="#047857">・即將上路規定：</text>
            <text y="80">  管委會申報出資清冊，</text>
            <text y="96">  憑證直接依出資比例</text>
            <text y="112" font-weight="bold" fill="#059669">  分拆給各家股東！</text>
            <text y="132" font-size="8" fill="#64748B">合資電廠重大利多</text>
          </g>
        </svg>
        '''
    elif vtype == "ten_commandments_c4":
        return '''
        <svg viewBox="0 0 540 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
          <rect x="5" y="10" width="530" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
          <text x="270" y="30" font-size="13" font-weight="bold" fill="#1B365D" text-anchor="middle">綠電交易與再生能源憑證運維十條軍規檢核表</text>

          <!-- 三大模塊排布 -->
          <!-- 模塊 1: 合規紅線 (3條) -->
          <g transform="translate(15, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#FEF2F2" stroke="#F87171" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#DC2626"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">合規紅線篇 (軍規 1-3)</text>
            
            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#B91C1C">軍規 1：嚴禁雙重受惠</text>
              <text y="14" fill="#64748B">FIT 躉購與碳抵換絕不可申證</text>
              <text y="36" font-weight="bold" fill="#B91C1C">軍規 2：認明 RE100 邊界</text>
              <text y="50" fill="#64748B">唯風光水地生，排除廢棄物抽蓄</text>
              <text y="72" font-weight="bold" fill="#B91C1C">軍規 3：生質能係數非零</text>
              <text y="86" fill="#64748B">盤查碳排務必向發電端索取實測</text>
              <text y="108" font-weight="bold" fill="#B91C1C">軍規 4：轉讓一次為限</text>
              <text y="122" fill="#64748B">憑證非股票，移轉後即宣告註銷</text>
              <text y="146" font-size="8" fill="#DC2626">不踩法律與碳盤查審計紅線</text>
            </g>
          </g>

          <!-- 模塊 2: 合約防禦 (3條) -->
          <g transform="translate(187, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#FEFCE8" stroke="#FBBF24" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#D97706"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">合約防禦篇 (軍規 5-7)</text>

            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#B45309">軍規 5：小額綠電先練兵</text>
              <text y="14" fill="#64748B">先簽台電小額短約搞懂 PPA 眉角</text>
              <text y="36" font-weight="bold" fill="#B45309">軍規 6：防禦必購 (Take/Pay)</text>
              <text y="50" fill="#64748B">余電吸收歸屬需在合約嚴密約定</text>
              <text y="72" font-weight="bold" fill="#B45309">軍規 7：善用台資電統購</text>
              <text y="86" fill="#64748B">中小企借國營信評破除聯貸門檻</text>
              <text y="108" font-weight="bold" fill="#B45309">軍規 8：平價競標鎖定4.3</text>
              <text y="122" fill="#64748B">掌握每年7~8月平價專案額度</text>
              <text y="146" font-size="8" fill="#B45309">以契約條款鎖住企業利潤</text>
            </g>
          </g>

          <!-- 模塊 3: 調度增益 (4條) -->
          <g transform="translate(360, 45)">
            <rect x="0" y="0" width="165" height="215" rx="6" fill="#F0FDF4" stroke="#4ADE80" stroke-width="1.5"/>
            <rect x="0" y="0" width="165" height="24" rx="6" fill="#16A34A"/>
            <text x="82" y="16" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">調度增益篇 (軍規 9-10)</text>

            <g transform="translate(8, 38)" font-size="8.5" fill="#334155">
              <text y="0" font-weight="bold" fill="#15803D">軍規 9：切換沙盒 3.0</text>
              <text y="14" fill="#64748B">事後自主分配綠電，規費省98%</text>
              <text y="36" font-weight="bold" fill="#15803D">軍規 10：零股化對齊財年</text>
              <text y="50" fill="#64748B">按月結清自由拼接跨國會計年度</text>
              <text y="72" font-weight="bold" fill="#15803D">加碼：解約當日拍照追溯</text>
              <text y="86" fill="#64748B">轉綠電次日拍照電表杜絕真空期</text>
              <text y="108" font-weight="bold" fill="#15803D">加碼：二三型鬆綁直轉</text>
              <text y="122" fill="#64748B">屋頂光電免轉一型直售售電業</text>
              <text y="146" font-size="8" fill="#16A34A">將每一度綠電價值發揮極致</text>
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
            <span class="footer-brand-tag">ACMEPOINT 6692 ✕ 綠電交易與憑證</span>
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
  <title>太陽光電設置乙級技術士回訓課程——綠電交易機制與再生能源憑證制度｜麥肯錫風格專業簡報</title>
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
        <strong>進金生能源 6692</strong> ｜ 太陽光電設置乙級技術士回訓課程——綠電交易機制與再生能源憑證制度
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
