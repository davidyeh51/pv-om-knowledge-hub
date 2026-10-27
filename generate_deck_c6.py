# -*- coding: utf-8 -*-
import os
import sys

out_dir = r"G:\我的雲端硬碟\0_AI Agent\Obsidian\DavidCloud\大衛工作\3.0 組織層級\3.3 人資管理\3.3.5 育才\pv-om-knowledge-hub\courses"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "pv-distribution-safety-regulations.html")

slides_data = [
    {
        "slideNo": 1,
        "module": "MODULE 1 ｜ 台電風控架構與高危成因",
        "ref": "講義對照 P.01 ｜ 錄音 00:00~01:00",
        "title": "配電線路現場工作安全法典：建構台電 3 層 5 級風控防線，從基層現場遏制工安死角",
        "question": "面對每年外線作業的多發工傷，台電如何劃分公安風控層級？為什麼最基層現場反而是風險最高發的震央？",
        "highlights": [
            "<strong>台電 3 層 5 級風控架構：</strong>由現場工作單位、各區營業處主管處、乃至總管理處風控中心，建構縱深管理防禦網絡。",
            "<strong>風險重心地面化倒置：</strong>體系頂端管理制度最嚴，但工傷案件 95% 以上集中在最基層現場單位（作業案件母數龐大、第一線變數最多）。",
            "<strong>維運專業工程師使命：</strong>光伏案場施工與維運常需租用或穿越台電配電管路、電桿與開關箱，必須以台電軍規級標準捍衛同仁生命安全。"
        ],
        "takeaway": "工安風險不在公文體系頂端，而在第一線施工現場；以 3 層 5 級嚴格標準杜絕僥倖心態。",
        "visualTitle": "台電 3 層 5 級公安風控金字塔與現場案件震央圖",
        "visualType": "safety_three_five_pyramid",
        "thumbImg": "../assets/images/slides/slide_01.jpg",
        "thumbCaption": "講義 P.01：台電公安風控層級與現場管理責任",
        "thumbLabel": "P.01 3層5級風控",
        "noteTakeaway": "台電配電線路現場工安權威開講：配電線路外線施工是高危險行業，風險重心永遠在最前線現場單位。",
        "noteDetail": "許多外包廠商抱怨台電比中華電信、自來水管路管得嚴格得多；但即便管這麼嚴，每年仍有工傷事故，說明現場人員危機意識與習慣養成才是生與死的界線。",
        "noteTransition": "現場最常被勞動檢查處與主管稽查抓到的違規缺失有哪些？請看第二頁常見安全缺失盤點。"
    },
    {
        "slideNo": 2,
        "module": "MODULE 1 ｜ 課程骨架與知識地圖",
        "ref": "講義對照 P.02 ｜ 錄音 01:00~04:04",
        "title": "全課程知識地圖：五大配電工安模組與 20 頁金字塔防禦骨架",
        "question": "本次回訓如何從真實血淚案例提煉為系統化防護 SOP？工程師該如何掌握 20 項安全防禦關鍵？",
        "highlights": [
            "<strong>模組一 風控體系與事故誘因：</strong>3 層 5 級風控、資淺領班斷層、承攬商高流動率與主管連帶法律責任。",
            "<strong>模組二 5151 原則與驗電接地：</strong>一定位一指令一複誦一操作一回報、公安三護（自護為本）與跨區處協調防護。",
            "<strong>模組三 感電電弧與逆送電血淚：</strong>電纜溝踩踏擠穿、低壓接頭流經心臟、升空車隱蔽物脫落與路燈雙電源逆送。",
            "<strong>模組四 道路交維與高差防墜：</strong>站馬路反光背心、工程車 6 年超音波、起重機 0.25m 過卷停機、電桿防墜與 1.5m 通道。",
            "<strong>模組五 局限空間與深開挖軍規：</strong>四合一氣體檢測（硫化氫攪水釋放案例）、1.5m 擋土支撐、電纜頭簽字制與工安十條軍規。"
        ],
        "takeaway": "五大工安模組環環相扣，構築配電線路與光伏維運不可跨越的零職災生命防禦牆。",
        "visualTitle": "配電線路現場安全五大模組邏輯架構與全景矩陣",
        "visualType": "safety_module_map",
        "thumbImg": "../assets/images/slides/slide_02.jpg",
        "thumbCaption": "講義 P.02：全課程安全防禦架構與五大模組綱要",
        "thumbLabel": "P.02 工安架構地圖",
        "noteTakeaway": "本課程以麥肯錫金字塔原理，將 50 分鐘台電現場演講精華提煉為五大模組 20 頁行動決策簡報。",
        "noteDetail": "包含數十起真實感電、電弧灼傷、高空墜落與逆送電死亡案例復盤，每一個數據背後都是一條寶貴人命與家庭破碎。",
        "noteTransition": "深入探討台電現場作業六大常見違規缺失，請看第三頁缺失盤點。"
    },
    {
        "slideNo": 3,
        "module": "MODULE 1 ｜ 現場違規缺失盤點",
        "ref": "講義對照 P.03 ｜ 錄音 01:00~04:04",
        "title": "勞檢稽查六大現場致命缺失：未穿背負式安全帶、未檢電掛接地與斜坡未置輪止滑墊",
        "question": "勞動檢查組與台電工安巡查現場時，最常開罰停工的六大違規盲點是什麼？",
        "highlights": [
            "<strong>高空作業防護缺失：</strong>未配備全身背負式安全帶與輔助繩（傳統腰帶式已全面淘汰），赤手空拳攀爬電桿或屋頂。",
            "<strong>電氣作業致命缺失：</strong>碰觸裸露帶電導體前未落實驗電、未掛接地，僅憑他人隨口告知「已斷電」即盲目上手。",
            "<strong>工程車輛作業缺失：</strong>工程車停於鬆軟地面未鋪墊木；停於斜坡未放置輪胎止滑墊（台電工程車強制出勤必放止滑墊）。",
            "<strong>吊掛、孔洞與開挖盲點：</strong>吊掛物下方有人通行；進入地下孔洞未測氣未通風；開挖深度超過 1.5m 未設擋土支撐。"
        ],
        "takeaway": "勞檢必查六大缺失即是致命陷阱；全面配備背負式安全帶、檢電接地與輪止滑墊是出勤底線。",
        "visualTitle": "現場作業六大常見違規缺失 ✕ 勞檢必查防護清單",
        "visualType": "safety_six_defects",
        "thumbImg": "../assets/images/slides/slide_03.jpg",
        "thumbCaption": "講義 P.03：現場常見工作安全缺失與法規標準清單",
        "thumbLabel": "P.03 六大常見缺失",
        "noteTakeaway": "勞檢最近查得最凶的就是『全身背負式安全帶』與『工程車輪胎止滑墊』。",
        "noteDetail": "很多司機辯解不知道什麼叫斜坡，台電統一規定：無論看似多平，只要車子停下來就必須放輪止滑墊，養成直覺習慣！",
        "noteTransition": "為什麼管這麼嚴格，台電每年仍然有工傷事故？請看第四頁深層事故誘因剖析。"
    },
    {
        "slideNo": 4,
        "module": "MODULE 1 ｜ 事故成因與法律責任",
        "ref": "講義對照 P.04 ｜ 錄音 04:04~07:01",
        "title": "工安事故四大管理病灶：年資斷層缺乏危機感、外勞違規攀爬與主管連帶民刑訴訟十餘年",
        "question": "台電與承攬商在制度齊備下為何仍頻繁出事？現場主管如果發生職災將面臨何種法律風暴？",
        "highlights": [
            "<strong>一線人員年資嚴重斷層：</strong>台電出現退休大斷層，年輕領班經驗不足過早推上一線；老班員倚老賣老不服管教，缺乏危機意識。",
            "<strong>承攬商流動率高與外勞隱患：</strong>包商工人訓練完即跳槽，引進大量外勞甚至徒手攀爬電桿，嚴重違反高空作業紀律。",
            "<strong>標準作業流程 (SOP) 未落地：</strong>部分現場無標準工序，工作紀律鬆弛，習慣憑經驗主義「猜測斷電」。",
            "<strong>主管連帶刑事與民事責任：</strong>現場工人傷亡，家屬通常連同現場主管一併提告過失致死，纏訟期長達十餘年，身心重創。"
        ],
        "takeaway": "現場出事主管連帶吃官司；強化領班權威、落實 SOP 紀律與杜絕外勞盲爬，是自保防禦關鍵。",
        "visualTitle": "事故誘因漏斗模型 ✕ 現場主管法律連帶責任鏈",
        "visualType": "accident_causes_liability",
        "thumbImg": "../assets/images/slides/slide_04.jpg",
        "thumbCaption": "講義 P.04：工安事故深層誘因與現場主管法律責任",
        "thumbLabel": "P.04 事故誘因與責任",
        "noteTakeaway": "講師沉痛呼籲主管：不要以為死掉的是工人和承包商自己沒事，家屬提告是連主管一起告！",
        "noteDetail": "很多主管即便最後無罪，十幾年間天天跑法院開庭，生活與家庭全被毀掉。因此在現場必須建立絕對權威與嚴明紀律。",
        "noteTransition": "如何從制度上根絕個人隨意操作？請看第二模組 5151 作業原則與公安三護。"
    },
    {
        "slideNo": 5,
        "module": "MODULE 2 ｜ 5151 作業原則",
        "ref": "講義對照 P.05 ｜ 錄音 07:01~09:06",
        "title": "5151 作業原則硬性落地：一定位、一指令、一複誦、一操作、一回報，嚴禁多點混亂操作",
        "question": "什麼是台電杜絕誤操作的「5151 原則」？為什麼強調每一步驟必須由「單人單指令」完成？",
        "highlights": [
            "<strong>五大閉環步驟：</strong>一定位（精準到點）➔ 一指令（領班清晰下達）➔ 一複誦（作業員大聲複誦）➔ 一操作（專注單項動作）➔ 一回報（完成登錄）。",
            "<strong>「1」的核心哲學：</strong>所有動作同一時間只能由「一個人、一個指令、一個位置」執行，嚴禁多位置並行、多指令齊下引發混亂。",
            "<strong>領班絕對監護制：</strong>領班不得親自參與動手作業，必須專職站立地面全景監護、排查危害並把控作業指令。"
        ],
        "takeaway": "5151 是電氣操作的航太級防錯機制；定位複誦單人閉環，徹底阻斷誤投誤切誘發爆炸。",
        "visualTitle": "5151 作業原則五步單向閉環流轉架構圖",
        "visualType": "safety_5151_loop",
        "thumbImg": "../assets/images/slides/slide_05.jpg",
        "thumbCaption": "講義 P.05：5151 作業原則與防誤操作操作規程",
        "thumbLabel": "P.05 5151作業原則",
        "noteTakeaway": "5151 原則是台電從無數誤操作事故中總結出的黃金法則。",
        "noteDetail": "很多事故都是因為領班喊一聲，現場三四個人同時動手，A以為B斷了電，結果切到活電炸機。單人、單指令、複誦、回報是唯一解。",
        "noteTransition": "除領班監護外，個人在現場如何保護自己？請看第六頁公安三護理念。"
    },
    {
        "slideNo": 6,
        "module": "MODULE 2 ｜ 公安三護安全理念",
        "ref": "講義對照 P.06 ｜ 錄音 09:06~10:34 / 32:03~33:33",
        "title": "公安三護責任金字塔：自護為核心、互護為照應、監護在側，絕不把生命托付他人",
        "question": "台電安全口號「自護、互護、監護」的三層責任邏輯是什麼？為何作業人員常犯「過度信賴他人」的致命錯誤？",
        "highlights": [
            "<strong>自護（核心，佔比 70%）：</strong>作業人員自身必須佩戴全套絕緣與防墜防護具，親自驗電、確認掛接地，對自己生命負首要責任。",
            "<strong>互護（照應，佔比 20%）：</strong>工作夥伴彼此提醒、交叉比對周遭活電死角，互查安全帶與絕緣手套是否完好。",
            "<strong>監護（把關，佔比 10%）：</strong>領班站在全局視野掌控風險，提醒外部危險（吊車逼近、道路車輛、掩蔽物脫落）。",
            "<strong>顛覆性警示：</strong>「絕不要把你的生命交到領班手上！」即便領班告知已停電，自己沒親自驗電絕不可碰觸導體。"
        ],
        "takeaway": "自護是生命最後一道防線；夥伴互查、領班在側，但親自檢電掛接地的自主防禦絕不可省。",
        "visualTitle": "公安三護（自護-互護-監護）同心圓與責任權重圖",
        "visualType": "safety_three_guards",
        "thumbImg": "../assets/images/slides/slide_06.jpg",
        "thumbCaption": "講義 P.06：公安三護理念與個人防護具著裝手冊",
        "thumbLabel": "P.06 公安三護理念",
        "noteTakeaway": "講師反覆強調：『不要把生命交在別人手上！』領班也會疏忽、值班主任也會搞錯。",
        "noteDetail": "許多殉職工人的遺言都是『領班跟我說停電了』，結果上去一摸直接電死。自我防護、親自掏出檢電筆才是唯一活命保證。",
        "noteTransition": "現場驗電與掛接地該如何執行才算合規？請看第七頁檢電掛接地絕對鐵律。"
    },
    {
        "slideNo": 7,
        "module": "MODULE 2 ｜ 檢電掛接地鐵律",
        "ref": "講義對照 P.07 ｜ 錄音 10:34~12:30 / 25:16~27:59",
        "title": "檢電掛接地操作紅線：未完成全流程前一律視為活電，口袋隨身攜帶檢電筆",
        "question": "為什麼僅完成單側接地或僅口頭確認停電極端危險？「未完成全流程一律視為活電」的實質內涵為何？",
        "highlights": [
            "<strong>口袋隨身檢電筆習慣：</strong>工程師上桿或開箱前，檢電筆必隨身掏出碰觸導體確認無電；無檢電筆者嚴禁作業。",
            "<strong>未完成全流程前皆為活電：</strong>只要未全數完成「檢電 ➔ 掛接地線」，即便開關已拉開，全部導線一律視為 100% 活電！",
            "<strong>半途脫防護具慘案：</strong>台電作業人員在常開點（雙向供電交界），完成 A 側接地後誤以為全線無電，提前脫下絕緣手套，換至 B 側掛接地時瞬間短路，全身嚴重電弧灼傷。",
            "<strong>剝線露出新導體：</strong>掛接地線嚴禁直接夾在生鏽氧化之接線管上，必須剝除外皮露出新銅導體，確保接地迴路阻抗為零。"
        ],
        "takeaway": "檢電筆碰一下保一生平安；全流程完成前絕不脫絕緣手套，接地必須露出純銅導體。",
        "visualTitle": "檢電掛接地四步標準程序 (SOP) ✕ 致命錯誤對照圖",
        "visualType": "safety_grounding_sop",
        "thumbImg": "../assets/images/slides/slide_07.jpg",
        "thumbCaption": "講義 P.07：檢電筆使用規範與接地線掛接標準圖說",
        "thumbLabel": "P.07 檢電接地鐵律",
        "noteTakeaway": "講師到現場抽檢第一件事：『檢電筆拿出來！』拿不出來的就是違規。",
        "noteDetail": "停電作業常遇到雙向電源或常開點，一邊斷了一邊還帶電；作業員以為做完一邊就安全了，把手套脫掉去摸另一邊，一碰就是幾千安培接地短路電弧！",
        "noteTransition": "如果電網涉及兩個不同供電區處的交界點，會發生什麼意想不到的致命事故？請看第八頁跨區處轉供失誤血淚案例。"
    },
    {
        "slideNo": 8,
        "module": "MODULE 2 ｜ 跨區處協調失誤案例",
        "ref": "講義對照 P.08 ｜ 錄音 14:10~18:04",
        "title": "跨區處界線電纜致命轉供：低壓接地夾無法承載高壓電流彈開，C 相高壓電直灌作業員",
        "question": "為什麼在兩個台電區處管轄交界點作業最容易發生致命事故？低壓接地線為何絕不能替代高壓專用接地線？",
        "highlights": [
            "<strong>事故背景（CX40 與 T121 銜接點）：</strong>北北區處更換電纜停電，現場人員使用「低壓接地線」掛接地；基隆區處不知情，為縮小停電範圍執行「轉供」投入開關復電。",
            "<strong>致命硬體錯誤：</strong>低壓接地線採彈簧夾爪式（非高壓螺旋旋緊式），高壓電流瞬間湧入產生強烈電磁斥力，接地夾被直接彈開！",
            "<strong>高壓電灌入現場：</strong>A、B 相電流入地，C 相接地夾脫落，高壓電流直接沿導線灌入作業人員體內，釀成重大感電傷亡。",
            "<strong>兩大防禦教訓：</strong>跨轄區交界處作業必須由雙方調度台書面確認連鎖；嚴禁用低壓接地線替代高壓專用耐電磁力接地線。"
        ],
        "takeaway": "轄區交界點作業必作雙方書面閉鎖；嚴禁用低壓接地夾應付高壓線路，防範電磁斥力脫落。",
        "visualTitle": "跨區處供電拓撲（北北 vs 基隆）✕ 低壓接地夾彈開失效圖",
        "visualType": "safety_boundary_cross",
        "thumbImg": "../assets/images/slides/slide_08.jpg",
        "thumbCaption": "講義 P.08：跨區處轉供事故線路單線圖與接地失效分析",
        "thumbLabel": "P.08 跨區處轉供案例",
        "noteTakeaway": "這是台電最經典也最慘痛的真實案例之一。",
        "noteDetail": "兩邊區處缺乏溝通，基隆端為了績效縮減停電用戶，轉供把電送出去，正好打在北北區處施工點。更要命的是現場圖省事拿低壓夾子掛接地，高壓電一來啪一聲夾子彈飛，工人直接被 C 相高壓電死！",
        "noteTransition": "進入第三模組，探討更多現場感電、電弧灼傷與逆送電的真實事故復盤。"
    },
    {
        "slideNo": 9,
        "module": "MODULE 3 ｜ 電纜溝作業事故復盤",
        "ref": "講義對照 P.09 ｜ 錄音 11:01~12:30",
        "title": "電纜溝內踩踏運轉電纜引發絕緣被穿：電弧瞬間爆炸灼傷，作業前強制鋪設防火毯",
        "question": "人孔與地下電纜溝內部空間狹窄，為何「踩踏帶電電纜」會引發絕緣擊穿與電弧爆炸？",
        "highlights": [
            "<strong>事故現場重現：</strong>作業人員進入台電配電人孔拖拉新電纜，因空間擁擠直接踩踏在運轉中的高壓電纜群上方。",
            "<strong>絕緣厚度壓縮效應：</strong>人體重量集中施壓於電纜表皮，絕緣層被物理壓縮變薄，耐壓絕緣強度驟降低於電網工作電壓，電流瞬間擊穿絕緣層！",
            "<strong>猛烈電弧灼傷：</strong>擊穿瞬間誘發千安級相間或相對地電弧，高達數千度電弧火焰將站在上方的作業人員全身嚴重灼傷。",
            "<strong>整改軍規：</strong>嚴禁直接踩踏任何帶電電纜；若必須在電纜上方作業，必須預先鋪設多層耐磨防火毯實體隔離。"
        ],
        "takeaway": "帶電電纜絕緣層受壓必崩潰；嚴禁腳踩運轉電纜，下溝進孔前強制鋪設防火毯。",
        "visualTitle": "電纜絕緣層受體重擠壓崩潰擊穿原理 ✕ 防火毯鋪設工法圖",
        "visualType": "safety_cable_tread",
        "thumbImg": "../assets/images/slides/slide_09.jpg",
        "thumbCaption": "講義 P.09：人孔電纜溝施工規範與防火毯鋪設標準",
        "thumbLabel": "P.09 電纜溝踩踏事故",
        "noteTakeaway": "光伏升壓站或配電箱常常有電纜溝，很多人習慣把粗電纜當階梯踩，這是拿命在賭。",
        "noteDetail": "高壓電纜的絕緣厚度是精密計算過的，人在上面踩跳，絕緣層被壓扁，電場強度瞬間超過絕緣介質耐受極限，直接擊穿炸出大火球，整個人當場燒焦。",
        "noteTransition": "低壓電（110V/220V）真的電不死人嗎？請看第十頁低壓接頭觸碰引發心臟纖維顫動致死案例。"
    },
    {
        "slideNo": 10,
        "module": "MODULE 3 ｜ 低壓感電致死案例",
        "ref": "講義對照 P.10 ｜ 錄音 12:30~14:10 / 18:04~19:07",
        "title": "低壓 220V 致命電流路徑：右手觸裸接頭、左手抱接地電桿經心臟，體內組織潰爛亡",
        "question": "為什麼現場工程師最容易輕忽低壓電？電流路徑如何決定生死？為何現場沒死隔週仍會身亡？",
        "highlights": [
            "<strong>事故經過（陳老三案例）：</strong>作業人員登上電桿維護，未穿絕緣衣，轉身時右手不慎觸碰未包覆絕緣的低壓接頭，左手正緊抱接地的水泥電桿。",
            "<strong>致命心臟電流迴路：</strong>電流由右手進入、橫貫胸腔流經心臟、自左手導入接地電桿入地，瞬間引發心室纖維性顫動當場休克。",
            "<strong>體內組織微血管潰爛延遲死亡：</strong>許多低壓感電者現場搶救甦醒，但微小電流已沿血管神經將體內深層肌肉與內臟微組織電熟，1~2 週後體內全面潰爛衰竭身亡。",
            "<strong>防護鐵律：</strong>低壓裸線接頭必須 100% 絕緣隱蔽；雨天作業哪怕低壓也必須穿戴絕緣手套與絕緣鞋。"
        ],
        "takeaway": "電流流經心臟毫安級即致命；低壓接頭嚴格隱蔽，嚴禁雙手同時碰觸導體與接地桿。",
        "visualTitle": "電流自右手經心臟至左手接地迴路 ✕ 體內延遲潰爛致死機制剖析圖",
        "visualType": "safety_low_voltage_death",
        "thumbImg": "../assets/images/slides/slide_10.jpg",
        "thumbCaption": "講義 P.10：低壓感電事故人體通路模型與防護要點",
        "thumbLabel": "P.10 低壓感電致死",
        "noteTakeaway": "很多人以為只有 11.4kV/22.8kV 高壓會死人，低壓 220V 被電一下只是麻麻的？大錯特錯！",
        "noteDetail": "只要形成『右手進、左手出』橫貫心臟的迴路，幾十毫安培就足以讓心跳停止。更可怕的是電流會把體內微血管電壞，現場沒事送醫，一週後五臟六腑潰爛死在病房。",
        "noteTransition": "在升空車上作業時，防護套管如果掉落會引發什麼爆炸？請看第十一頁升空車隱蔽物脫落事故。"
    },
    {
        "slideNo": 11,
        "module": "MODULE 3 ｜ 升空車作業事故復盤",
        "ref": "講義對照 P.11 ｜ 錄音 19:07~21:50",
        "title": "升空車相間短路大爆炸：隱蔽物脫落觸碰接線環，絕緣手套炸黑與地面領班監護失靈",
        "question": "在高空作業車上已做高壓隱蔽防護，為何仍發生電弧爆炸？地面領班失誤在哪裡？",
        "highlights": [
            "<strong>事故經過：</strong>作業人員在升空車桶內剪切 B 相接線管，已對 C 相高壓導線加裝橘色絕緣隱蔽管，但固定夾未夾緊。",
            "<strong>隱蔽管脫落引爆短路：</strong>C 相隱蔽管滑脫露出帶電導體，作業人員剪斷 B 相導線時操作工具甩動觸碰 C 相接線環，瞬間爆發 B-C 相間短路電弧！",
            "<strong>手套面罩炸黑救回一命：</strong>高達數千度短路電弧將其絕緣手套炸黑融化，面部灼傷；所幸戴齊防護具保住性命，未穿防護具必當場碳化。",
            "<strong>領班重大監護失職：</strong>地面領班站在下方未能及時抬頭發現隱蔽物鬆脫並喝止作業，未履行全程現場監護之法定責任。"
        ],
        "takeaway": "隱蔽防護夾具必須雙重鎖定；領班抬頭全程凝視高空作業，消滅隱蔽脫落盲區。",
        "visualTitle": "升空車 B-C 相間短路爆炸 ✕ 隱蔽夾鬆脫與領班視線盲區剖析圖",
        "visualType": "safety_bucket_truck_arc",
        "thumbImg": "../assets/images/slides/slide_11.jpg",
        "thumbCaption": "講義 P.11：高空作業車絕緣隱蔽器具安裝與固定規範",
        "thumbLabel": "P.11 升空車隱蔽脫落",
        "noteTakeaway": "升空車絕緣桶雖然有耐壓測試，但如果桶內兩相導體碰在一起短路，絕緣桶救不了你。",
        "noteDetail": "作業員剪線時注意力全在剪刀上，根本看不到身後 C 相套管滑落。此時全靠地面領班在下面看，領班只要低頭滑手機或發呆，就是一場毀容爆炸。",
        "noteTransition": "還有哪種電氣事故比直接碰電更防不勝防？請看第十二頁路燈與號誌線路雙電源逆送電案例。"
    },
    {
        "slideNo": 12,
        "module": "MODULE 3 ｜ 雙電源逆送電案例",
        "ref": "講義對照 P.12 ｜ 錄音 22:44~24:33 / 28:19~30:55",
        "title": "配合地下化老舊架空未拆除：拉開閘刀誤認已斷電，慘遭另一路地下雙電源逆送擊倒",
        "question": "為何路燈與交通號誌線路是台電人員最常遭遇「逆送電感電」的頭號殺手（同類事故至少 3~4 起）？",
        "highlights": [
            "<strong>雙電源共存致死陷阱：</strong>早年架空 220V 供電路燈配合道路地下化，改由地下電纜供電；施工單位偷懶未拆除舊架空引線，台電端亦未切斷，造成「架空+地下雙向並存」。",
            "<strong>拉開閘刀誤判停電：</strong>維修人員拉開現場老式切換閘刀，以為前方電源已全數切除，未持檢電筆驗電即徒手剪拆變壓器引線。",
            "<strong>隱蔽地下電源逆灌：</strong>地下端電源沿未拆除迴路直接逆向倒灌至開關背後，維修人員慘遭強烈逆送電擊倒！",
            "<strong>維運絕對鐵律：</strong>切開開關絕不等於斷電；任何涉及二次側、公共照明或光伏併網的迴路，施工前必須雙向檢電。"
        ],
        "takeaway": "雙電源與舊線未拆是逆送電元兇；拉開閘刀絕不等於停電，兩側全部驗電方可動工。",
        "visualTitle": "路燈架空改地下未拆除雙電源迴路逆灌拓撲圖",
        "visualType": "safety_backfeed_circuit",
        "thumbImg": "../assets/images/slides/slide_12.jpg",
        "thumbCaption": "講義 P.12：公共照明雙電源逆送事故線路圖與排查 SOP",
        "thumbLabel": "P.12 雙電源逆送事故",
        "noteTakeaway": "講師講了至少三四次：路燈、交通號誌、綠能案場最常發生逆送電感電！",
        "noteDetail": "許多地方政府或外包商改地下化時，線拉下去了，舊架空線懶得剪就丟在上面，台電變壓器也沒拆。維修工人把開關拉開以為沒電，結果電從另一條隱藏線路倒灌上來，當場電死。",
        "noteTransition": "現場除了電氣危險，道路施工與車輛吊掛有哪些勞檢硬性規定？請看第四模組道路交維與高差防墜。"
    },
    {
        "slideNo": 13,
        "module": "MODULE 4 ｜ 道路交維安全規範",
        "ref": "講義對照 P.13 ｜ 錄音 33:48~36:35",
        "title": "道路施工交維法定紅線：進工地必戴安全帽、站馬路必著反光背心、電動旗手電池包膠",
        "question": "道路施工交維缺失頻頻被民眾拍照檢舉與勞檢重罰，現場人員配備與交維設施有哪些剛性界線？",
        "highlights": [
            "<strong>人員兩大黃金原則：</strong>「進工地必戴安全帽」（踏入交通錐工區範圍一律配戴）；「站馬路必穿反光背心」（變電所或封閉案場內則不強制）。",
            "<strong>交維連桿全封閉：</strong>交通錐之間必須使用專用連桿實體串接圈閉，嚴禁單擺散錐留下開口讓車輛行人誤闖。",
            "<strong>電動旗手規範與電池絕緣：</strong>必須具備合規面部人形（嚴禁卡通貼圖）；旗手底座蓄電池帶電極柱與鱷魚夾，必須以厚橡膠完全包覆密封，防止雨水導電引爆或觸電。"
        ],
        "takeaway": "道路交維連桿密閉不留開口；站馬路穿反光背心、進工地戴安全帽、旗手電池嚴密包膠。",
        "visualTitle": "道路交維標準佈設圖（交通錐連桿、告示牌、反光背心、電池包膠檢查點）",
        "visualType": "safety_traffic_control",
        "thumbImg": "../assets/images/slides/slide_13.jpg",
        "thumbCaption": "講義 P.13：道路交通安全設施設置規範與電動旗手標準",
        "thumbLabel": "P.13 道路交維標準",
        "noteTakeaway": "很多人以為在馬路旁邊指揮交通不用管，民眾路過隨手一拍就是幾萬塊罰單。",
        "noteDetail": "勞檢最常抓的細節是電動旗手底下的電瓶！鱷魚夾裸露在外面，一下雨就漏電短路，必須用橡膠絕緣皮全包起來。",
        "noteTransition": "工程車輛與吊掛作業有哪些法定年限與資質要求？請看第十四頁車輛器具一機三證。"
    },
    {
        "slideNo": 14,
        "module": "MODULE 4 ｜ 車輛器具與起重法規",
        "ref": "講義對照 P.14 ｜ 錄音 36:35~40:00",
        "title": "車輛設備勞檢必查項目：起重機一機三證、滿 6 年超音波探傷、0.25m 過卷警報自動停機",
        "question": "起重機與升空高空作業車在勞動檢查中為何退件率最高？哪些安全裝置故障會引發致命崩塌？",
        "highlights": [
            "<strong>移動式起重機「一機三證」：</strong>起重機檢查合格證、操作人員合格證、吊掛作業人員合格證缺一不可。",
            "<strong>過卷預防裝置（0.25 公尺強制停機）：</strong>吊鉤上升至距臂端頂部 0.25 公尺時，過卷警報器必須自動響起並強制切斷動力停機，防止拉碎滑輪吊鉤彈射砸死地面人員。",
            "<strong>高空作業車 6 年超音波探傷：</strong>作業車出廠滿 6 年起，每 2 年必須實施一次吊臂結構超音波非破壞檢測，排查金屬疲勞裂紋。",
            "<strong>斜坡止滑墊與中文標識：</strong>車停斜坡必墊輪止滑墊；起重臂必須張貼中文額定荷重表及性能曲線圖，按鈕必須防水中文標識。"
        ],
        "takeaway": "起重吊掛恪守一機三證；0.25m 過卷強制斷電，6 年作業車超音波探傷防吊臂斷裂。",
        "visualTitle": "起重機一機三證清單 ✕ 0.25m 過卷防護與 6 年超音波檢測週期圖",
        "visualType": "safety_crane_regulations",
        "thumbImg": "../assets/images/slides/slide_14.jpg",
        "thumbCaption": "講義 P.14：起重機勞檢必查項目與高空車檢測手冊",
        "thumbLabel": "P.14 車輛器具一機三證",
        "noteTakeaway": "起重機過卷裝置沒調好，吊車油壓馬達力道幾十噸，直接把頂部鋼輪擠碎，鋼勾彈出來砸到地上像砲彈一樣。",
        "noteDetail": "勞檢一來第一件事看一機三證，第二看中文荷重表有沒有貼。很多吊車買日本外匯車沒改中文標籤，被開單改善隨便貼張紙，一下雨字全糊了，直接停工處分！",
        "noteTransition": "高處作業最容易發生的墜落如何防護？請看第十五頁高差防墜三道防線。"
    },
    {
        "slideNo": 15,
        "module": "MODULE 4 ｜ 高空防墜與通道標準",
        "ref": "講義對照 P.15 ｜ 錄音 40:00~41:56",
        "title": "高差作業防墜法定門檻：垂直高差超 1.5m 設專用通道、2m 以上設置防墜護欄與背負安全帶",
        "question": "建築屋頂光電施工與電桿維運中，墜落致死率長年居高不下，勞工安全法規設定了哪些剛性高差界線？",
        "highlights": [
            "<strong>垂直高差 1.5 公尺門檻：</strong>作業面與基層高差超過 1.5 公尺時，必須設置專用安全上下設備（爬梯、踏步通道），嚴禁抓取管線徒手攀爬跳躍。",
            "<strong>墜落防護 2.0 公尺門檻：</strong>作業高度達 2.0 公尺以上或樓板邊緣開口，必須設置固定式或臨時合格防護護欄，或鋪設安全防護網。",
            "<strong>全身背負式安全帶強制落實：</strong>嚴格淘汰傳統單腰帶安全帶，高空作業必須佩戴「全身背負式雙大鉤安全帶」，採雙掛繩交替掛接於母索或錨定點。",
            "<strong>屋頂光伏嚴禁赤手空拳：</strong>嚴禁未著防墜具徒手攀爬浪板屋頂；採光罩與脆弱屋頂必須預先鋪設走道板與防墜網。"
        ],
        "takeaway": "1.5m 設上下通道、2m 設防墜護欄；全身背負式雙掛繩交替扣鎖，杜絕屋頂盲攀墜落。",
        "visualTitle": "高差作業 1.5m/2.0m 法定門檻示意圖 ✕ 全身背負式安全帶雙鉤掛接標準工法",
        "visualType": "safety_fall_protection",
        "thumbImg": "../assets/images/slides/slide_15.jpg",
        "thumbCaption": "講義 P.15：高空防墜設施規範與全身背負式安全帶使用手冊",
        "thumbLabel": "P.15 高差防墜標準",
        "noteTakeaway": "屋頂光電施工最常見的工安就是踩破採光罩或在浪板上滑倒掉下來。",
        "noteDetail": "很多工人自恃身手矯健，兩層樓高度直接跳上跳下；法規明定 1.5m 就要有合格樓梯或爬梯，2m 就要有護欄和背負式安全帶，不能赤手空拳爬屋頂。",
        "noteTransition": "老員工因為經驗豐富就不會墜落嗎？請看第十六頁 4 米電桿墜落鋼絲剪撞腰椎重傷案例。"
    },
    {
        "slideNo": 16,
        "module": "MODULE 4 ｜ 高空墜落與工具防護案例",
        "ref": "講義對照 P.16 ｜ 錄音 21:50~22:44 / 44:49~45:16",
        "title": "4 米電桿踏釘滑脫墜落：背負鋼絲剪直撞腰椎致殘，嚴禁由桿頂向下拋擲工具物料",
        "question": "為什麼資深老員工也會摔下電桿？工具擺放位置與高空傳遞方式如何決定二次傷害程度？",
        "highlights": [
            "<strong>資深老手腳滑墜落慘案：</strong>台電資深員工自恃經驗豐富攀爬電桿未繫安全帶，腳踩腳踏釘滑脫，從 4 公尺高處（約一樓半高度）直接墜地。",
            "<strong>腰部工具引發二次重創：</strong>墜地時背後口袋插放的「鋼絲剪」隨體重重擊脊椎，直接造成腰椎粉碎性骨折嚴重癱瘓殘疾！",
            "<strong>高空物料拋擲死刑：</strong>電桿上作業時，拆卸之螺栓、導線、手工具絕對嚴禁由上往下拋擲，過往多次發生拋擲工具砸穿地面人員安全帽當場死亡之慘劇。",
            "<strong>工具安全袋與繩索吊運：</strong>高空物料與重型手工具必須放置於專用防掉落工具袋，長度較大者一律使用牽引繩滑輪組上下吊運。"
        ],
        "takeaway": "4 米墜落加尖銳工具足以致命癱瘓；腰間工具收納合規，物料一律繩索吊運嚴禁拋擲。",
        "visualTitle": "電桿 4m 踏釘滑落腰椎受創力學剖析 ✕ 滑輪吊袋安全傳遞標準圖",
        "visualType": "safety_pole_fall_tool",
        "thumbImg": "../assets/images/slides/slide_16.jpg",
        "thumbCaption": "講義 P.16：電桿作業工具收納與防墜吊運作業要點",
        "thumbLabel": "P.16 電桿墜落與工具傷",
        "noteTakeaway": "這是老員工血的教訓：跌落高度只有 4 米不算特別高，但背後插了把大剪刀，撞下去直接傷到中樞神經。",
        "noteDetail": "另外桿上千萬不要偷懶往下面丟東西，上面掉顆螺絲下來速度重力加速度就像子彈，地面人員就算戴安全帽脖子也可能被砸斷！",
        "noteTransition": "進入第五模組，深入探討密閉地下孔洞、深開挖與工程維運十條軍規。"
    },
    {
        "slideNo": 17,
        "module": "MODULE 5 ｜ 局限空間氣體檢測",
        "ref": "講義對照 P.17 ｜ 錄音 02:41~03:40 / 48:12~49:51",
        "title": "局限空間四合一氣體檢測鐵律：氧氣 ≥18%、硫化氫溶於水攪動暴釋奪命",
        "question": "人孔與蓄水池看似無毒，為何作業員進去會瞬間昏厥身亡？硫化氫為何常被初篩檢測漏掉？",
        "highlights": [
            "<strong>法定四合一氣體檢測標準：</strong>氧氣濃度 ($O_2$) 必須維持在 18% 以上（低於 18% 缺氧危險）；一氧化碳 ($CO$)、氫氣 ($H_2$) 與硫化氫 ($H_2S$) 必須在安全閾值內。",
            "<strong>洗水塔工人慘死案例：</strong>硫化氫極易溶於積水；初篩檢測水面上方數值完全正常，工人進入後搓洗攪動水底淤泥，大量硫化氫如香檳開蓋瞬間暴釋，工人吸入一口當場神經麻痺昏厥溺死！",
            "<strong>SOP 鐵律：</strong>開蓋後通風至少 15 分鐘，檢測時必須長桿探入攪動水體後再次檢測，且作業全程強制機械強迫換氣。"
        ],
        "takeaway": "四合一氣體合格方可入孔；硫化氫溶於水攪動即暴釋，全程強制抽排風捍衛呼吸。",
        "visualTitle": "局限空間四合一氣體安全區間 ✕ 硫化氫溶水攪動釋放致死機制圖",
        "visualType": "safety_confined_space_gas",
        "thumbImg": "../assets/images/slides/slide_17.jpg",
        "thumbCaption": "講義 P.17：局限空間作業危害預防與四合一氣體偵測手冊",
        "thumbLabel": "P.17 局限空間氣體檢測",
        "noteTakeaway": "人孔和密閉水槽是無形殺手，特別是南部養豬場或工廠案場，沼氣濃度極高。",
        "noteDetail": "很多工人拿著偵測器在洞口晃一下說沒事就跳下去，水一攪動，深層高濃度硫化氫衝出來，兩秒鐘之內嗅覺神經癱瘓倒地，下去救的人也跟著吸入死在裡面，一死死好幾個。",
        "noteTransition": "地下開挖深度超過多少必須設置擋土支撐？請看第十八頁深開挖與管線協調。"
    },
    {
        "slideNo": 18,
        "module": "MODULE 5 ｜ 深開挖與管線防護",
        "ref": "講義對照 P.18 ｜ 錄音 03:40~04:04 / 49:51~50:23",
        "title": "開挖超 1.5 米強制擋土支撐：設專任開挖主管，會同地下管線主管機關協調防挖爆",
        "question": "配電管路或大型光電基樁開挖，為何頻傳崩塌活埋與挖斷瓦斯管？法規紅線在哪裡？",
        "highlights": [
            "<strong>1.5 米擋土支撐剛性界限：</strong>露天開挖深度超過 1.5 公尺時，必須依法設置專用鋼軌樁、擋土板或斜坡支撐，防止土壁瞬間坍塌活埋工人。",
            "<strong>專任露天開挖作業主管在場：</strong>開挖現場必須派駐經勞動部結業合格之「露天開挖作業主管」，全程監控地質含水量與土壓變化。",
            "<strong>跨管線圖資協調大會：</strong>動工前必須召集自來水、中華電信、天然氣瓦斯、軍用光纖與台電等相關管線單位召開實體圖資會勘協調會。",
            "<strong>斜坡立桿覆土支撐力測算：</strong>在斜坡地帶開挖立電桿（入土深度需達 2.1 公尺），必須精確校核下坡側覆土剪力支撐，防止電桿向空側失穩倒塌。"
        ],
        "takeaway": "開挖超 1.5m 強制擋土支撐；專任主管在場監造，會同管線圖資會勘杜絕挖爆活埋。",
        "visualTitle": "開挖擋土支撐工程斷面圖 ✕ 斜坡立桿 2.1m 覆土失穩倒塌受力分析圖",
        "visualType": "safety_excavation_shoring",
        "thumbImg": "../assets/images/slides/slide_18.jpg",
        "thumbCaption": "講義 P.18：露天開挖安全規範與斜坡電桿基礎工程手冊",
        "thumbLabel": "P.18 深開挖與管線防護",
        "noteTakeaway": "土石的重量超乎想像，一立方米的泥土重達 1.8 噸，一旦坍塌壓在胸口幾分鐘就窒息。",
        "noteDetail": "超過 1.5 米就必須打擋土樁。同時挖馬路前千萬不要憑感覺挖，沒開協調會一挖土機下去挖斷瓦斯管引發大火，或是挖斷專用光纖，賠償金額高達數千萬。",
        "noteTransition": "現場細節工藝如何影響系統安全與人員壽命？請看第十九頁施工品質與責任追溯。"
    },
    {
        "slideNo": 19,
        "module": "MODULE 5 ｜ 施工品質與細節管控",
        "ref": "講義對照 P.19 ｜ 錄音 42:20~44:00 / 45:16~47:51",
        "title": "嚴苛施工品質細節守衛生命：套管壓縮兩次以上、電纜頭簽字終身追溯、操作棒遠距切熔絲",
        "question": "為什麼台電統計事故大量爆發在「電纜接頭」？如何以細部工藝規範杜絕爆炸與火災？",
        "highlights": [
            "<strong>壓接套管壓縮次數規範：</strong>施作電纜直線接頭時，No. 1 規格套管兩側各壓接 2 次；500 MCM 大截面電纜兩側各壓接 3 次，確保接觸電阻最小化。",
            "<strong>電纜頭施作人員簽字追溯制：</strong>完工之高壓電纜接頭外層強制施作人員簽署全名與日期；若後續發生電纜頭擊穿事故，直接追溯施作者紀錄，劣質包商通報停權。",
            "<strong>絕緣操作棒遠距操作變壓器：</strong>切換變壓器過載保護熔絲桶（Cutout Fuse）時，必須站在遠處使用加長型絕緣操作棒操作；若變壓器內部短路，投入瞬間高溫油氣爆噴，操作棒保證人員立於爆炸半徑之外。",
            "<strong>接地線嚴禁直接夾鏽蝕套管：</strong>接地端子必須刮除表面銅綠氧化層露出純金屬導體，嚴禁偷懶隨手夾在生鏽套管上。"
        ],
        "takeaway": "電纜頭簽字追溯工程責任；大線壓接 3 次防發熱，操作棒遠距切投防變壓器油爆。",
        "visualTitle": "壓接套管壓縮點位示意圖 ✕ 電纜頭簽名追溯牌 ✕ 變壓器熔絲操作棒安全距離圖",
        "visualType": "safety_quality_traceability",
        "thumbImg": "../assets/images/slides/slide_19.jpg",
        "thumbCaption": "講義 P.19：高壓電纜頭製作規範與變壓器熔絲操作手冊",
        "thumbLabel": "P.19 施工品質追溯",
        "noteTakeaway": "接頭施工不良是火災與跳脫的第一大元兇。",
        "noteDetail": "台電推行電纜頭簽名制後，事故率大幅下降，因為做頭的人知道名字留在上面跑不掉。另外操作熔絲筒一定要用操作棒，變壓器內部短路時一送電直接炸開，絕緣油像烈火一樣噴出來，站在前面沒操作棒必死無疑。",
        "noteTransition": "總結全課二十頁精華，請看第二十頁配電線路工安維運十條軍規。"
    },
    {
        "slideNo": 20,
        "module": "MODULE 5 ｜ 配電線路工安十條軍規",
        "ref": "講義對照 P.20 ｜ 錄音 50:23~50:42",
        "title": "配電線路現場工作安全十條軍規：制度、紀律、自護本能與零職災實戰考核",
        "question": "光伏維運與電氣工程師如何將台電血淚案例化為每日出勤的直覺反射與考核軍規？",
        "highlights": [
            "<strong>守規線（軍規 1–3）：</strong>未驗電掛接地一律視為活電；自護為本絕不把性命交給領班；嚴格落實 5151 單人閉環作業。",
            "<strong>防護線（軍規 4–6）：</strong>高空 2m 必戴全身背負雙鉤安全帶；工程車停斜坡必放輪止滑墊；起重機落實一機三證與 0.25m 過卷停機。",
            "<strong>作業線（軍規 7–10）：</strong>局限空間四合一測氣（嚴防攪水釋硫化氫）；深開挖超 1.5m 設擋土支撐；電纜溝鋪防火毯禁踩電纜；電纜接頭簽字終身追溯責任制。"
        ],
        "takeaway": "工安十條軍規是保命符，融入血液形成直覺本能，守護每一位電氣工程師平安回家。",
        "visualTitle": "配電現場工作安全十條軍規矩陣表（守規線、防護線、作業線、文化線）",
        "visualType": "safety_ten_commandments",
        "thumbImg": "../assets/images/slides/slide_20.jpg",
        "thumbCaption": "講義 P.20：配電線路現場安全注意事項總則與考核標準",
        "thumbLabel": "P.20 工安十條軍規",
        "noteTakeaway": "講師最後結語：公安不僅是制度與紀律，更要塑造成一種工作態度與文化！",
        "noteDetail": "遇到危險動作，不是因為主管要來查才戴安全帽，而是自然而然覺得沒戴安全帽走在馬路上渾身不自在。當安全成為習慣，才能真正達成零職災。",
        "noteTransition": "全課 20 頁講解完畢，歡迎按 G 開啟總覽，或按 P 列印 16:9 顧問 PDF 備忘錄。"
    }
]

def render_svg(visual_type):
    if visual_type == "safety_three_five_pyramid":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="gradTop" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#002060"/>
              <stop offset="100%" stop-color="#0F172A"/>
            </linearGradient>
            <linearGradient id="gradMid" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284C7"/>
              <stop offset="100%" stop-color="#0369A1"/>
            </linearGradient>
            <linearGradient id="gradBot" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#EF4444"/>
              <stop offset="100%" stop-color="#B91C1C"/>
            </linearGradient>
          </defs>
          <polygon points="280,30 380,105 180,105" fill="url(#gradTop)" stroke="#D4AF37" stroke-width="2"/>
          <text x="280" y="70" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">第 3 層：總處風控中心</text>
          <text x="280" y="90" fill="#94A3B8" font-size="10" text-anchor="middle">政策制定 ✕ 宏觀監督</text>

          <polygon points="175,115 385,115 440,195 120,195" fill="url(#gradMid)" stroke="#38BDF8" stroke-width="2"/>
          <text x="280" y="145" fill="#FFFFFF" font-size="13" font-weight="bold" text-anchor="middle">第 2 層：各區營業處主管處 (5級架構)</text>
          <text x="280" y="168" fill="#E0F2FE" font-size="10" text-anchor="middle">巡檢稽核 ✕ 督導考核 ✕ 跨單位協調</text>

          <polygon points="115,205 445,205 510,295 50,295" fill="url(#gradBot)" stroke="#FCA5A5" stroke-width="2.5"/>
          <text x="280" y="240" fill="#FFFFFF" font-size="15" font-weight="bold" text-anchor="middle">第 1 層：基層現場工作單位（事故高發震央！）</text>
          <text x="280" y="265" fill="#FEE2E2" font-size="11" text-anchor="middle">案件母數佔 95% 以上 ✕ 變數最多 ✕ 生死第一線</text>

          <rect x="390" y="45" width="150" height="50" rx="6" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="465" y="65" fill="#B45309" font-size="10" font-weight="bold" text-anchor="middle">⚠️ 管理認知錯位</text>
          <text x="465" y="82" fill="#78350F" font-size="9" text-anchor="middle">頂端最嚴，底層最危！</text>
        </svg>
        '''
    elif visual_type == "safety_module_map":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(15, 20)">
            <rect x="0" y="0" width="95" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <rect x="0" y="0" width="95" height="35" rx="8" fill="#002060"/>
            <text x="47" y="22" fill="#D4AF37" font-size="11" font-weight="bold" text-anchor="middle">模組一</text>
            <text x="47" y="55" fill="#0F172A" font-size="11" font-weight="bold" text-anchor="middle">風控體系</text>
            <text x="47" y="75" fill="#64748B" font-size="9" text-anchor="middle">• 3層5級架構</text>
            <text x="47" y="95" fill="#64748B" font-size="9" text-anchor="middle">• 六大常見缺失</text>
            <text x="47" y="115" fill="#64748B" font-size="9" text-anchor="middle">• 資淺領班斷層</text>
            <text x="47" y="135" fill="#64748B" font-size="9" text-anchor="middle">• 主管訴訟十年</text>
          </g>
          <g transform="translate(125, 20)">
            <rect x="0" y="0" width="95" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <rect x="0" y="0" width="95" height="35" rx="8" fill="#002060"/>
            <text x="47" y="22" fill="#D4AF37" font-size="11" font-weight="bold" text-anchor="middle">模組二</text>
            <text x="47" y="55" fill="#0F172A" font-size="11" font-weight="bold" text-anchor="middle">5151原則</text>
            <text x="47" y="75" fill="#64748B" font-size="9" text-anchor="middle">• 單人閉環流程</text>
            <text x="47" y="95" fill="#64748B" font-size="9" text-anchor="middle">• 公安三護自護</text>
            <text x="47" y="115" fill="#64748B" font-size="9" text-anchor="middle">• 檢電掛接地</text>
            <text x="47" y="135" fill="#64748B" font-size="9" text-anchor="middle">• 跨區處轉供彈開</text>
          </g>
          <g transform="translate(235, 20)">
            <rect x="0" y="0" width="95" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <rect x="0" y="0" width="95" height="35" rx="8" fill="#002060"/>
            <text x="47" y="22" fill="#D4AF37" font-size="11" font-weight="bold" text-anchor="middle">模組三</text>
            <text x="47" y="55" fill="#0F172A" font-size="11" font-weight="bold" text-anchor="middle">感電血淚</text>
            <text x="47" y="75" fill="#64748B" font-size="9" text-anchor="middle">• 電纜溝擠穿電弧</text>
            <text x="47" y="95" fill="#64748B" font-size="9" text-anchor="middle">• 低壓經心臟亡</text>
            <text x="47" y="115" fill="#64748B" font-size="9" text-anchor="middle">• 升空車短路炸黑</text>
            <text x="47" y="135" fill="#64748B" font-size="9" text-anchor="middle">• 路燈雙電源逆送</text>
          </g>
          <g transform="translate(345, 20)">
            <rect x="0" y="0" width="95" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <rect x="0" y="0" width="95" height="35" rx="8" fill="#002060"/>
            <text x="47" y="22" fill="#D4AF37" font-size="11" font-weight="bold" text-anchor="middle">模組四</text>
            <text x="47" y="55" fill="#0F172A" font-size="11" font-weight="bold" text-anchor="middle">交維與防墜</text>
            <text x="47" y="75" fill="#64748B" font-size="9" text-anchor="middle">• 站馬路反光背心</text>
            <text x="47" y="95" fill="#64748B" font-size="9" text-anchor="middle">• 起重機一機三證</text>
            <text x="47" y="115" fill="#64748B" font-size="9" text-anchor="middle">• 6年超音波探傷</text>
            <text x="47" y="135" fill="#64748B" font-size="9" text-anchor="middle">• 1.5m/2m防墜網</text>
          </g>
          <g transform="translate(455, 20)">
            <rect x="0" y="0" width="95" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <rect x="0" y="0" width="95" height="35" rx="8" fill="#002060"/>
            <text x="47" y="22" fill="#D4AF37" font-size="11" font-weight="bold" text-anchor="middle">模組五</text>
            <text x="47" y="55" fill="#0F172A" font-size="11" font-weight="bold" text-anchor="middle">局限與軍規</text>
            <text x="47" y="75" fill="#64748B" font-size="9" text-anchor="middle">• 四合一氣體檢測</text>
            <text x="47" y="95" fill="#64748B" font-size="9" text-anchor="middle">• 硫化氫攪水奪命</text>
            <text x="47" y="115" fill="#64748B" font-size="9" text-anchor="middle">• 1.5m擋土支撐</text>
            <text x="47" y="135" fill="#64748B" font-size="9" text-anchor="middle">• 工安十條軍規</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_six_defects":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(20, 20)">
            <rect x="0" y="0" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="15" y="25" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 1：高空作業未戴安全帶</text>
            <text x="15" y="45" fill="#475569" font-size="10">未戴全身背負式安全帶與輔助繩，腰帶式</text>
            <text x="15" y="60" fill="#475569" font-size="10">防護力不足已全面禁用。</text>

            <rect x="275" y="0" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="290" y="25" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 2：未檢電即碰裸露導體</text>
            <text x="290" y="45" fill="#475569" font-size="10">聽信他人隨口『已停電』未親自驗電，</text>
            <text x="290" y="60" fill="#475569" font-size="10">未掛接地線即徒手碰觸。</text>

            <rect x="0" y="95" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="15" y="120" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 3：工程車斜坡未置止滑墊</text>
            <text x="15" y="140" fill="#475569" font-size="10">停靠微斜坡或路邊未放置三角止滑墊，</text>
            <text x="15" y="155" fill="#475569" font-size="10">鬆軟地面未鋪外伸撐座墊木。</text>

            <rect x="275" y="95" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="290" y="120" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 4：吊掛物下方有人通行</text>
            <text x="290" y="140" fill="#475569" font-size="10">起重吊掛半徑未淨空，無牽引繩拉扯，</text>
            <text x="290" y="155" fill="#475569" font-size="10">吊鉤防滑舌片失效或缺損。</text>

            <rect x="0" y="190" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="15" y="215" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 5：地下孔洞未測氣未通風</text>
            <text x="15" y="235" fill="#475569" font-size="10">進孔未用四合一偵測器，未抽風15分鐘，</text>
            <text x="15" y="250" fill="#475569" font-size="10">養豬場或蓄水池沼氣瞬間窒息。</text>

            <rect x="275" y="190" width="245" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
            <text x="290" y="215" fill="#991B1B" font-size="12" font-weight="bold">❌ 缺失 6：深開挖超 1.5m 無支撐</text>
            <text x="290" y="235" fill="#475569" font-size="10">垂直開挖超過 1.5 公尺未做擋土支撐，</text>
            <text x="290" y="250" fill="#475569" font-size="10">土石塌方無逃生空間活埋窒息。</text>
          </g>
        </svg>
        '''
    elif visual_type == "accident_causes_liability":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="20" y="20" width="240" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
          <text x="140" y="50" fill="#002060" font-size="14" font-weight="bold" text-anchor="middle">現場四大管理病灶</text>

          <g transform="translate(35, 75)">
            <rect x="0" y="0" width="210" height="42" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="10" y="20" fill="#1E40AF" font-size="11" font-weight="bold">1. 資淺領班 ✕ 經驗斷層</text>
            <text x="10" y="34" fill="#64748B" font-size="9">老員工不聽管教，新手缺乏危機感</text>
          </g>
          <g transform="translate(35, 125)">
            <rect x="0" y="0" width="210" height="42" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="10" y="20" fill="#1E40AF" font-size="11" font-weight="bold">2. 外包流動高 ✕ 外勞徒手爬</text>
            <text x="10" y="34" fill="#64748B" font-size="9">外勞不懼生死盲爬電桿，違規猖獗</text>
          </g>
          <g transform="translate(35, 175)">
            <rect x="0" y="0" width="210" height="42" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="10" y="20" fill="#1E40AF" font-size="11" font-weight="bold">3. 標準作業程序 (SOP) 缺失</text>
            <text x="10" y="34" fill="#64748B" font-size="9">憑經驗主義猜測停電，無覆誦回報</text>
          </g>
          <g transform="translate(35, 225)">
            <rect x="0" y="0" width="210" height="42" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="10" y="20" fill="#1E40AF" font-size="11" font-weight="bold">4. 外線人力缺口與技能斷層</text>
            <text x="10" y="34" fill="#64748B" font-size="9">招工極度困難，未成熟即推上一線</text>
          </g>

          <rect x="290" y="20" width="250" height="270" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="415" y="50" fill="#991B1B" font-size="14" font-weight="bold" text-anchor="middle">現場主管連帶法律責任鏈</text>

          <circle cx="415" cy="100" r="30" fill="#DC2626"/>
          <text x="415" y="105" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">傷亡事故</text>

          <path d="M 415 135 L 415 160" stroke="#DC2626" stroke-width="2" marker-end="url(#arrowRed)"/>
          <rect x="315" y="165" width="200" height="45" rx="4" fill="#FFFFFF" stroke="#DC2626"/>
          <text x="415" y="185" fill="#991B1B" font-size="11" font-weight="bold" text-anchor="middle">家屬提告：過失致死 / 業務過失</text>
          <text x="415" y="200" fill="#475569" font-size="9" text-anchor="middle">現場作業員 + 現場主管連帶提告！</text>

          <rect x="315" y="225" width="200" height="50" rx="4" fill="#FFFBEB" stroke="#F59E0B"/>
          <text x="415" y="245" fill="#B45309" font-size="11" font-weight="bold" text-anchor="middle">纏訟 10~15 年漫長煎熬</text>
          <text x="415" y="262" fill="#78350F" font-size="9" text-anchor="middle">跑法院、巨額賠償、家庭職涯盡毀</text>
        </svg>
        '''
    elif visual_type == "safety_5151_loop":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arrowGold" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <path d="M0,0 L0,6 L6,3 z" fill="#D4AF37"/>
            </marker>
          </defs>
          <rect x="15" y="20" width="530" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
          <text x="280" y="48" fill="#002060" font-size="15" font-weight="bold" text-anchor="middle">5151 作業原則：單人單點五步閉環防錯架構</text>

          <g transform="translate(40, 75)">
            <rect x="0" y="0" width="85" height="120" rx="6" fill="#002060"/>
            <text x="42" y="28" fill="#D4AF37" font-size="12" font-weight="bold" text-anchor="middle">1. 一定位</text>
            <text x="42" y="55" fill="#FFFFFF" font-size="10" text-anchor="middle">精確抵達</text>
            <text x="42" y="75" fill="#94A3B8" font-size="9" text-anchor="middle">指定設備</text>
            <text x="42" y="95" fill="#94A3B8" font-size="9" text-anchor="middle">開關箱位置</text>
          </g>
          <path d="M 130 135 L 145 135" stroke="#D4AF37" stroke-width="2" marker-end="url(#arrowGold)"/>

          <g transform="translate(150, 75)">
            <rect x="0" y="0" width="85" height="120" rx="6" fill="#0F766E"/>
            <text x="42" y="28" fill="#5EEAD4" font-size="12" font-weight="bold" text-anchor="middle">2. 一指令</text>
            <text x="42" y="55" fill="#FFFFFF" font-size="10" text-anchor="middle">領班下達</text>
            <text x="42" y="75" fill="#CCFBF1" font-size="9" text-anchor="middle">單一明確</text>
            <text x="42" y="95" fill="#CCFBF1" font-size="9" text-anchor="middle">切斷/投入指令</text>
          </g>
          <path d="M 240 135 L 255 135" stroke="#D4AF37" stroke-width="2" marker-end="url(#arrowGold)"/>

          <g transform="translate(260, 75)">
            <rect x="0" y="0" width="85" height="120" rx="6" fill="#B45309"/>
            <text x="42" y="28" fill="#FDE68A" font-size="12" font-weight="bold" text-anchor="middle">3. 一複誦</text>
            <text x="42" y="55" fill="#FFFFFF" font-size="10" text-anchor="middle">大聲複誦</text>
            <text x="42" y="75" fill="#FEF3C7" font-size="9" text-anchor="middle">雙方確認</text>
            <text x="42" y="95" fill="#FEF3C7" font-size="9" text-anchor="middle">無任何誤解</text>
          </g>
          <path d="M 350 135 L 365 135" stroke="#D4AF37" stroke-width="2" marker-end="url(#arrowGold)"/>

          <g transform="translate(370, 75)">
            <rect x="0" y="0" width="85" height="120" rx="6" fill="#1D4ED8"/>
            <text x="42" y="28" fill="#93C5FD" font-size="12" font-weight="bold" text-anchor="middle">4. 一操作</text>
            <text x="42" y="55" fill="#FFFFFF" font-size="10" text-anchor="middle">單人專注</text>
            <text x="42" y="75" fill="#DBEAFE" font-size="9" text-anchor="middle">執行操作</text>
            <text x="42" y="95" fill="#DBEAFE" font-size="9" text-anchor="middle">防電弧噴濺</text>
          </g>
          <path d="M 460 135 L 475 135" stroke="#D4AF37" stroke-width="2" marker-end="url(#arrowGold)"/>

          <g transform="translate(480, 75)">
            <rect x="0" y="0" width="60" height="120" rx="6" fill="#15803D"/>
            <text x="30" y="28" fill="#86EFAC" font-size="11" font-weight="bold" text-anchor="middle">5. 回報</text>
            <text x="30" y="55" fill="#FFFFFF" font-size="9" text-anchor="middle">操作完畢</text>
            <text x="30" y="75" fill="#DCFCE7" font-size="9" text-anchor="middle">回報領班</text>
            <text x="30" y="95" fill="#DCFCE7" font-size="8" text-anchor="middle">登錄確認</text>
          </g>

          <rect x="50" y="220" width="460" height="50" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="280" y="242" fill="#92400E" font-size="11" font-weight="bold" text-anchor="middle">⭐ 核心禁令：嚴禁同一時間多指令、多位置、多人並行操作！</text>
          <text x="280" y="258" fill="#78350F" font-size="10" text-anchor="middle">領班絕不可親自上手動手施工，必須專職站立地面全景監護！</text>
        </svg>
        '''
    elif visual_type == "safety_three_guards":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <circle cx="280" cy="160" r="140" fill="#F1F5F9" stroke="#94A3B8" stroke-width="2"/>
          <text x="280" y="45" fill="#475569" font-size="12" font-weight="bold" text-anchor="middle">監護 (領班在側 10%)：全景防禦、外部威脅把關</text>

          <circle cx="280" cy="160" r="95" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
          <text x="280" y="95" fill="#0369A1" font-size="12" font-weight="bold" text-anchor="middle">互護 (夥伴照應 20%)：相互排查死角</text>

          <circle cx="280" cy="160" r="55" fill="#002060" stroke="#D4AF37" stroke-width="2.5"/>
          <text x="280" y="152" fill="#FFFFFF" font-size="13" font-weight="bold" text-anchor="middle">自護 (核心 70%)</text>
          <text x="280" y="172" fill="#D4AF37" font-size="10" font-weight="bold" text-anchor="middle">個人生命自己防禦</text>

          <rect x="20" y="235" width="220" height="65" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
          <text x="130" y="255" fill="#991B1B" font-size="11" font-weight="bold" text-anchor="middle">⚠️ 絕對不要做的事</text>
          <text x="130" y="275" fill="#475569" font-size="10" text-anchor="middle">『把生命完全交給領班！』</text>
          <text x="130" y="290" fill="#475569" font-size="9" text-anchor="middle">領班說停電就去摸 = 自尋死路</text>

          <rect x="320" y="235" width="220" height="65" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5"/>
          <text x="430" y="255" fill="#166534" font-size="11" font-weight="bold" text-anchor="middle">✅ 自護黃金原則</text>
          <text x="430" y="275" fill="#15803D" font-size="10" text-anchor="middle">『口袋掏出檢電筆親自碰』</text>
          <text x="430" y="290" fill="#475569" font-size="9" text-anchor="middle">全套防護穿戴齊全才上工</text>
        </svg>
        '''
    elif visual_type == "safety_grounding_sop":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 25)">
            <rect x="0" y="0" width="230" height="120" rx="8" fill="#F8FAFC" stroke="#16A34A" stroke-width="2"/>
            <text x="115" y="30" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">步驟一：口袋掏出檢電筆驗電</text>
            <text x="20" y="60" fill="#334155" font-size="10">• 即使開關已拉開，仍必須驗電</text>
            <text x="20" y="80" fill="#334155" font-size="10">• 檢電筆隨身攜帶，碰觸三相導體</text>
            <text x="20" y="100" fill="#334155" font-size="10">• 確認聲光無任何電氣反應</text>
          </g>

          <g transform="translate(300, 25)">
            <rect x="0" y="0" width="230" height="120" rx="8" fill="#F8FAFC" stroke="#16A34A" stroke-width="2"/>
            <text x="115" y="30" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">步驟二：剝除氧化皮露出純銅</text>
            <text x="20" y="60" fill="#334155" font-size="10">• 嚴禁直接夾在生鏽氧化接線管</text>
            <text x="20" y="80" fill="#334155" font-size="10">• 刮除導線表面灰塵雜質與銅綠</text>
            <text x="20" y="100" fill="#334155" font-size="10">• 露出新鮮金屬導體確保零阻抗</text>
          </g>

          <g transform="translate(30, 165)">
            <rect x="0" y="0" width="230" height="125" rx="8" fill="#F8FAFC" stroke="#16A34A" stroke-width="2"/>
            <text x="115" y="30" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">步驟三：掛接接地線實體短路</text>
            <text x="20" y="60" fill="#334155" font-size="10">• 先接接地端，後接導線端</text>
            <text x="20" y="80" fill="#334155" font-size="10">• 高壓線路必須用高壓螺旋夾</text>
            <text x="20" y="100" fill="#334155" font-size="10">• 形成實體等電位短路洩放通路</text>
          </g>

          <g transform="translate(300, 165)">
            <rect x="0" y="0" width="230" height="125" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
            <text x="115" y="30" fill="#991B1B" font-size="13" font-weight="bold" text-anchor="middle">⚠️ 未完成前全部視為活電！</text>
            <text x="20" y="60" fill="#7F1D1D" font-size="10">• 在接地全流程完成前，嚴禁脫手套</text>
            <text x="20" y="80" fill="#7F1D1D" font-size="10">• 常開點兩側未全掛前，絕非安全</text>
            <text x="20" y="100" fill="#7F1D1D" font-size="10">• 違者依接地短路電弧當場重傷！</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_boundary_cross":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="20" y="30" width="230" height="160" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
          <text x="135" y="60" fill="#1E40AF" font-size="13" font-weight="bold" text-anchor="middle">北北區處轄區 (T121 線路)</text>
          <text x="135" y="85" fill="#475569" font-size="10" text-anchor="middle">申請停電更換電纜</text>
          <text x="135" y="110" fill="#DC2626" font-size="11" font-weight="bold" text-anchor="middle">❌ 錯誤使用：低壓接地彈簧夾</text>
          <text x="135" y="130" fill="#64748B" font-size="9" text-anchor="middle">無法承受高壓短路大電流！</text>
          <rect x="60" y="145" width="150" height="30" rx="4" fill="#FEE2E2" stroke="#EF4444"/>
          <text x="135" y="165" fill="#991B1B" font-size="10" font-weight="bold" text-anchor="middle">工人進行換線作業中</text>

          <rect x="310" y="30" width="230" height="160" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
          <text x="425" y="60" fill="#92400E" font-size="13" font-weight="bold" text-anchor="middle">基隆區處轄區 (CX40 線路)</text>
          <text x="425" y="85" fill="#475569" font-size="10" text-anchor="middle">為縮小停電範圍欲做「轉供」</text>
          <text x="425" y="110" fill="#DC2626" font-size="11" font-weight="bold" text-anchor="middle">❌ 缺乏溝通：不知交界有人施工</text>
          <text x="425" y="130" fill="#64748B" font-size="9" text-anchor="middle">投入常開點送出高壓大電！</text>
          <rect x="350" y="145" width="150" height="30" rx="4" fill="#FDE68A" stroke="#D97706"/>
          <text x="425" y="165" fill="#78350F" font-size="10" font-weight="bold" text-anchor="middle">高壓電直接往交界灌入 ⚡</text>

          <path d="M 310 110 L 250 110" stroke="#DC2626" stroke-width="3" stroke-dasharray="5,5"/>
          <text x="280" y="100" fill="#DC2626" font-size="10" font-weight="bold" text-anchor="middle">轉供逆送</text>

          <rect x="30" y="210" width="500" height="85" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="280" y="235" fill="#991B1B" font-size="12" font-weight="bold" text-anchor="middle">💥 事故爆發機制：高壓電磁斥力將低壓彈簧夾直接彈飛！</text>
          <text x="280" y="255" fill="#475569" font-size="10" text-anchor="middle">A、B 相電流尚能導入大地，C 相夾子被電磁斥力崩飛脫落！</text>
          <text x="280" y="275" fill="#B91C1C" font-size="11" font-weight="bold" text-anchor="middle">C 相高壓電直接灌穿北北區處作業人員體內，釀成當場電擊殉職慘劇！</text>
        </svg>
        '''
    elif visual_type == "safety_cable_tread":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="30" y="20" width="500" height="130" rx="8" fill="#F8FAFC" stroke="#DC2626" stroke-width="2"/>
          <text x="280" y="45" fill="#991B1B" font-size="14" font-weight="bold" text-anchor="middle">電纜受重壓絕緣被穿原理 (Insulation Breakdown)</text>

          <g transform="translate(60, 65)">
            <rect x="0" y="20" width="200" height="35" rx="6" fill="#1E293B"/>
            <text x="100" y="42" fill="#FFFFFF" font-size="10" text-anchor="middle">正常電纜絕緣層 (完整厚度 d)</text>
            <text x="100" y="70" fill="#16A34A" font-size="9" text-anchor="middle">耐壓強度 E = V/d ＞ 工作電壓 (安全)</text>
          </g>

          <path d="M 270 95 L 300 95" stroke="#DC2626" stroke-width="2"/>

          <g transform="translate(310, 65)">
            <rect x="0" y="28" width="200" height="15" rx="3" fill="#EF4444"/>
            <text x="100" y="40" fill="#FFFFFF" font-size="9" font-weight="bold" text-anchor="middle">體重踩壓絕緣層變薄 (厚度 d' ↓↓)</text>
            <text x="100" y="70" fill="#DC2626" font-size="9" font-weight="bold" text-anchor="middle">電場強度 E' 暴增 ➔ 瞬間被穿爆炸 ⚡</text>
          </g>

          <rect x="30" y="170" width="500" height="120" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>
          <text x="280" y="195" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">✅ 電纜溝人孔作業鐵律：強制鋪設多層耐磨防火毯</text>
          <text x="60" y="225" fill="#334155" font-size="10">• 嚴禁將運轉中電纜當踏階踩踏行走，人體重力集中於鞋底足部產生數十 kg/cm² 壓強。</text>
          <text x="60" y="248" fill="#334155" font-size="10">• 進入人孔若無落腳處，必須使用專用絕緣架台，或滿鋪耐火絕緣毯分散承重。</text>
          <text x="60" y="270" fill="#15803D" font-size="10" font-weight="bold">• 杜絕電弧灼傷：絕緣厚度即是生命線，踩踏電纜等於踩在定時炸彈上！</text>
        </svg>
        '''
    elif visual_type == "safety_low_voltage_death":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="25" y="20" width="245" height="270" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="147" y="45" fill="#991B1B" font-size="13" font-weight="bold" text-anchor="middle">致命心臟迴路（陳老三慘案）</text>

          <g transform="translate(45, 65)">
            <circle cx="100" cy="40" r="18" fill="#F87171"/>
            <text x="100" y="44" fill="#FFFFFF" font-size="10" text-anchor="middle">頭部</text>
            <line x1="100" y1="58" x2="100" y2="120" stroke="#1E293B" stroke-width="4"/>
            <line x1="100" y1="75" x2="30" y2="90" stroke="#DC2626" stroke-width="4"/>
            <text x="15" y="110" fill="#DC2626" font-size="9" font-weight="bold">右手觸裸接頭 ⚡</text>

            <line x1="100" y1="75" x2="170" y2="90" stroke="#1E293B" stroke-width="4"/>
            <text x="150" y="110" fill="#1E293B" font-size="9" font-weight="bold">左手抱電桿</text>

            <circle cx="100" cy="85" r="10" fill="#EF4444"/>
            <text x="100" y="89" fill="#FFFFFF" font-size="8" text-anchor="middle">心臟</text>
            <path d="M 40 85 Q 100 80 160 85" stroke="#EF4444" stroke-width="2" stroke-dasharray="3,3"/>
          </g>

          <text x="147" y="215" fill="#7F1D1D" font-size="10" text-anchor="middle">橫貫胸腔流經心臟！</text>
          <text x="147" y="235" fill="#991B1B" font-size="10" font-weight="bold" text-anchor="middle">心室纖維性顫動當場休克</text>
          <text x="147" y="255" fill="#475569" font-size="9" text-anchor="middle">水泥電桿內含接地鋼筋通大地</text>

          <rect x="290" y="20" width="245" height="270" rx="8" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
          <text x="412" y="45" fill="#B45309" font-size="13" font-weight="bold" text-anchor="middle">微電流體內潰爛延遲死亡</text>

          <g transform="translate(310, 70)">
            <rect x="0" y="0" width="205" height="50" rx="4" fill="#FFFFFF" stroke="#F59E0B"/>
            <text x="10" y="22" fill="#B45309" font-size="10" font-weight="bold">1. 現場獲救甦醒：</text>
            <text x="10" y="38" fill="#64748B" font-size="9">表面僅輕微水泡，看似神智清醒無恙</text>

            <rect x="0" y="65" width="205" height="50" rx="4" fill="#FFFFFF" stroke="#F59E0B"/>
            <text x="10" y="87" fill="#B45309" font-size="10" font-weight="bold">2. 深層微血管受損：</text>
            <text x="10" y="103" fill="#64748B" font-size="9">電流沿阻抗最低之血管與神經灼熟</text>

            <rect x="0" y="130" width="205" height="55" rx="4" fill="#FEF2F2" stroke="#EF4444"/>
            <text x="10" y="152" fill="#991B1B" font-size="10" font-weight="bold">3. 隔 1~2 週組織全面潰爛：</text>
            <text x="10" y="168" fill="#7F1D1D" font-size="9">肌肉壞死引發敗血症，器官衰竭身亡！</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_bucket_truck_arc":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="25" y="20" width="510" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
          <text x="280" y="48" fill="#002060" font-size="14" font-weight="bold" text-anchor="middle">升空車絕緣隱蔽物脫落 ✕ 相間短路電弧爆炸機制</text>

          <g transform="translate(50, 75)">
            <rect x="0" y="0" width="200" height="120" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="100" y="25" fill="#1E40AF" font-size="11" font-weight="bold" text-anchor="middle">高空剪管作業點</text>
            <text x="20" y="55" fill="#334155" font-size="10">• 作業員剪斷 B 相接線管</text>
            <text x="20" y="75" fill="#DC2626" font-size="10" font-weight="bold">• C 相橘色隱蔽套管夾具鬆脫！</text>
            <text x="20" y="95" fill="#334155" font-size="10">• 操作桿不慎觸碰 C 相接線環</text>
          </g>

          <path d="M 260 135 L 295 135" stroke="#DC2626" stroke-width="3"/>
          <circle cx="280" cy="135" r="18" fill="#EF4444"/>
          <text x="280" y="140" fill="#FFFFFF" font-size="9" font-weight="bold" text-anchor="middle">相間短路</text>

          <g transform="translate(310, 75)">
            <rect x="0" y="0" width="200" height="120" rx="6" fill="#FEF2F2" stroke="#EF4444"/>
            <text x="100" y="25" fill="#991B1B" font-size="11" font-weight="bold" text-anchor="middle">數千度電弧大爆炸 💥</text>
            <text x="20" y="55" fill="#7F1D1D" font-size="10">• 電流瞬間由 C 相灌入 B 相</text>
            <text x="20" y="75" fill="#7F1D1D" font-size="10">• 絕緣手套炸黑炸穿、面部灼傷</text>
            <text x="20" y="95" fill="#15803D" font-size="10" font-weight="bold">• 佩戴防護面罩保住一命！</text>
          </g>

          <rect x="50" y="215" width="460" height="55" rx="6" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5"/>
          <text x="280" y="238" fill="#B45309" font-size="11" font-weight="bold" text-anchor="middle">⚠️ 地面領班失職死角：抬頭全程監護是唯一解法！</text>
          <text x="280" y="255" fill="#78350F" font-size="9" text-anchor="middle">桶內作業員視線被遮擋，地面領班若發呆滑手機，隱蔽物滑脫無人預警必釀爆炸！</text>
        </svg>
        '''
    elif visual_type == "safety_backfeed_circuit":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="20" y="20" width="520" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
          <text x="280" y="45" fill="#002060" font-size="14" font-weight="bold" text-anchor="middle">路燈與號誌「架空改地下未拆線」雙電源逆送拓撲圖</text>

          <g transform="translate(40, 70)">
            <rect x="0" y="0" width="130" height="70" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="65" y="25" fill="#1E40AF" font-size="10" font-weight="bold" text-anchor="middle">電源 A：原架空 220V</text>
            <text x="65" y="45" fill="#64748B" font-size="9" text-anchor="middle">台電未斷電、舊線未拆</text>
            <text x="65" y="60" fill="#DC2626" font-size="8" font-weight="bold" text-anchor="middle">暗藏活電！</text>
          </g>

          <g transform="translate(40, 160)">
            <rect x="0" y="0" width="130" height="70" rx="4" fill="#F0FDF4" stroke="#16A34A"/>
            <text x="65" y="25" fill="#166534" font-size="10" font-weight="bold" text-anchor="middle">電源 B：新地下電纜</text>
            <text x="65" y="45" fill="#64748B" font-size="9" text-anchor="middle">道路地下化新電源</text>
            <text x="65" y="60" fill="#15803D" font-size="8" font-weight="bold" text-anchor="middle">正常供電中</text>
          </g>

          <path d="M 175 105 L 240 135" stroke="#DC2626" stroke-width="2"/>
          <path d="M 175 195 L 240 165" stroke="#16A34A" stroke-width="2"/>

          <g transform="translate(240, 110)">
            <rect x="0" y="0" width="110" height="80" rx="4" fill="#FEF3C7" stroke="#D97706"/>
            <text x="55" y="25" fill="#92400E" font-size="10" font-weight="bold" text-anchor="middle">現場切換開關</text>
            <text x="55" y="48" fill="#B45309" font-size="9" text-anchor="middle">維修員拉開閘刀</text>
            <text x="55" y="68" fill="#DC2626" font-size="9" font-weight="bold" text-anchor="middle">誤判已完全斷電</text>
          </g>

          <path d="M 355 150 L 410 150" stroke="#DC2626" stroke-width="3" stroke-dasharray="4,4"/>
          <text x="382" y="140" fill="#DC2626" font-size="9" font-weight="bold" text-anchor="middle">逆送電灌入</text>

          <g transform="translate(410, 110)">
            <rect x="0" y="0" width="115" height="80" rx="4" fill="#FEF2F2" stroke="#DC2626"/>
            <text x="57" y="25" fill="#991B1B" font-size="10" font-weight="bold" text-anchor="middle">現場作業人員 ⚡</text>
            <text x="57" y="48" fill="#7F1D1D" font-size="9" text-anchor="middle">未驗電剪開引線</text>
            <text x="57" y="68" fill="#B91C1C" font-size="9" font-weight="bold" text-anchor="middle">遭逆送電當場擊倒</text>
          </g>

          <rect x="40" y="245" width="480" height="35" rx="4" fill="#FEE2E2" stroke="#EF4444"/>
          <text x="280" y="267" fill="#991B1B" font-size="10" font-weight="bold" text-anchor="middle">🛡️ 救命鐵律：拉開開關絕不等於斷電！施工前必對開關兩側進行雙向驗電！</text>
        </svg>
        '''
    elif visual_type == "safety_traffic_control":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="20" y="20" width="520" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
          <text x="280" y="48" fill="#002060" font-size="14" font-weight="bold" text-anchor="middle">道路施工標準交維防護 ✕ 電動旗手絕緣要點</text>

          <g transform="translate(40, 70)">
            <rect x="0" y="0" width="140" height="120" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="70" y="25" fill="#1E40AF" font-size="11" font-weight="bold" text-anchor="middle">交通錐連桿封閉</text>
            <text x="15" y="55" fill="#334155" font-size="9">• 交通錐間必掛連桿</text>
            <text x="15" y="75" fill="#334155" font-size="9">• 嚴禁散擺留開口</text>
            <text x="15" y="95" fill="#15803D" font-size="9" font-weight="bold">• 施工告示牌醒目</text>
          </g>

          <g transform="translate(200, 70)">
            <rect x="0" y="0" width="150" height="120" rx="6" fill="#F0FDF4" stroke="#16A34A"/>
            <text x="75" y="25" fill="#166534" font-size="11" font-weight="bold" text-anchor="middle">人員防護黃金準則</text>
            <text x="15" y="55" fill="#15803D" font-size="10" font-weight="bold">進工地 ➔ 必戴安全帽</text>
            <text x="15" y="80" fill="#0369A1" font-size="10" font-weight="bold">站馬路 ➔ 必著反光背心</text>
            <text x="15" y="105" fill="#64748B" font-size="8">變電所/封閉案場不強制背心</text>
          </g>

          <g transform="translate(370, 70)">
            <rect x="0" y="0" width="150" height="120" rx="6" fill="#FEF3C7" stroke="#D97706"/>
            <text x="75" y="25" fill="#92400E" font-size="11" font-weight="bold" text-anchor="middle">電動旗手電池包膠</text>
            <text x="15" y="50" fill="#78350F" font-size="9">• 必須標準人形臉孔</text>
            <text x="15" y="70" fill="#DC2626" font-size="9" font-weight="bold">• 電池極柱鱷魚夾</text>
            <text x="15" y="90" fill="#DC2626" font-size="9" font-weight="bold">  必須厚橡膠完全包覆</text>
            <text x="15" y="108" fill="#475569" font-size="8">防止下雨漏電或短路引爆</text>
          </g>

          <rect x="40" y="210" width="480" height="60" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
          <text x="280" y="235" fill="#991B1B" font-size="11" font-weight="bold" text-anchor="middle">⚠️ 勞檢與民眾拍照檢舉熱點：交維不全即刻開罰！</text>
          <text x="280" y="255" fill="#475569" font-size="10" text-anchor="middle">哪怕只是站在馬路邊指揮交通，只要沒穿反光背心或電池裸露，立刻拍照停工處分！</text>
        </svg>
        '''
    elif visual_type == "safety_crane_regulations":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 20)">
            <rect x="0" y="0" width="245" height="125" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="122" y="28" fill="#002060" font-size="12" font-weight="bold" text-anchor="middle">起重機「一機三證」勞檢必查</text>
            <text x="15" y="55" fill="#334155" font-size="10">1. 起重機檢查合格證（合格有效期限）</text>
            <text x="15" y="78" fill="#334155" font-size="10">2. 操作人員合格證（重機械操作執照）</text>
            <text x="15" y="101" fill="#334155" font-size="10">3. 吊掛作業人員合格證（吊掛證照受訓）</text>
          </g>

          <g transform="translate(290, 20)">
            <rect x="0" y="0" width="245" height="125" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
            <text x="122" y="28" fill="#991B1B" font-size="12" font-weight="bold" text-anchor="middle">0.25 公尺過卷防護斷電</text>
            <text x="15" y="55" fill="#7F1D1D" font-size="10">• 吊鉤距臂頂 0.25m 必須警報並停機</text>
            <text x="15" y="78" fill="#7F1D1D" font-size="10">• 防止油壓過卷擠碎滑輪鋼架</text>
            <text x="15" y="101" fill="#DC2626" font-size="10" font-weight="bold">• 杜絕鋼鉤彈脫砲彈式砸死地面人！</text>
          </g>

          <g transform="translate(25, 160)">
            <rect x="0" y="0" width="245" height="125" rx="8" fill="#EFF6FF" stroke="#0284C7" stroke-width="2"/>
            <text x="122" y="28" fill="#0369A1" font-size="12" font-weight="bold" text-anchor="middle">高空作業車滿 6 年超音波檢測</text>
            <text x="15" y="55" fill="#334155" font-size="10">• 出廠滿 6 年起，每 2 年檢測一次</text>
            <text x="15" y="78" fill="#334155" font-size="10">• 吊臂結構超音波非破壞探傷 (NDT)</text>
            <text x="15" y="101" fill="#0369A1" font-size="10" font-weight="bold">• 預防金屬疲勞內裂引發無預警折斷</text>
          </g>

          <g transform="translate(290, 160)">
            <rect x="0" y="0" width="245" height="125" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
            <text x="122" y="28" fill="#B45309" font-size="12" font-weight="bold" text-anchor="middle">斜坡止滑墊 ✕ 中文荷重標識</text>
            <text x="15" y="55" fill="#78350F" font-size="10">• 工程車出勤停靠，強制放輪止滑墊</text>
            <text x="15" y="78" fill="#78350F" font-size="10">• 吊車必貼中文額定荷重與性能曲線</text>
            <text x="15" y="101" fill="#B45309" font-size="10" font-weight="bold">• 操作鈕中文防水標籤，嚴禁隨意手寫</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_fall_protection":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 25)">
            <rect x="0" y="0" width="230" height="130" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
            <text x="115" y="30" fill="#1E40AF" font-size="13" font-weight="bold" text-anchor="middle">高差 1.5 公尺法定門檻</text>
            <text x="20" y="60" fill="#334155" font-size="10">• 高差 ＞ 1.5m 必設專用上下設備</text>
            <text x="20" y="80" fill="#334155" font-size="10">• 合格安全梯、踏步梯或搭接走道</text>
            <text x="20" y="105" fill="#DC2626" font-size="10" font-weight="bold">• 嚴禁抓電纜或結構跳躍攀爬！</text>
          </g>

          <g transform="translate(295, 25)">
            <rect x="0" y="0" width="235" height="130" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
            <text x="117" y="30" fill="#991B1B" font-size="13" font-weight="bold" text-anchor="middle">高差 2.0 公尺防墜護欄</text>
            <text x="20" y="60" fill="#7F1D1D" font-size="10">• 高度 ＞ 2.0m 必設 90cm 以上護欄</text>
            <text x="20" y="80" fill="#7F1D1D" font-size="10">• 開口處鋪設防護網或踢腳板</text>
            <text x="20" y="105" fill="#991B1B" font-size="10" font-weight="bold">• 無護欄處強制掛雙大鉤安全帶！</text>
          </g>

          <g transform="translate(30, 175)">
            <rect x="0" y="0" width="500" height="115" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>
            <text x="250" y="28" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">全身背負式安全帶 (Full Body Harness) 強制標準</text>
            <text x="25" y="55" fill="#334155" font-size="10">• 全面淘汰單腰帶式：墜落時腰帶勒擠內臟造成內出血或脊椎折斷，法規已全面禁止。</text>
            <text x="25" y="78" fill="#334155" font-size="10">• 雙大鉤交替掛接：在電桿或屋頂走動時，兩根大鉤始終有一根扣在安全母索上（100% 扣鎖）。</text>
            <text x="25" y="100" fill="#15803D" font-size="10" font-weight="bold">• 屋頂光伏嚴禁赤手空拳：採光罩與脆弱石綿瓦必須鋪設跳板與安全網，防止踏穿墜落！</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_pole_fall_tool":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="25" y="20" width="245" height="270" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
          <text x="147" y="45" fill="#991B1B" font-size="13" font-weight="bold" text-anchor="middle">4m 電桿墜落鋼絲剪重創腰椎</text>

          <g transform="translate(45, 65)">
            <line x1="40" y1="20" x2="40" y2="180" stroke="#64748B" stroke-width="6"/>
            <text x="50" y="40" fill="#64748B" font-size="9">水泥電桿</text>

            <circle cx="90" cy="50" r="12" fill="#F87171"/>
            <text x="90" y="80" fill="#DC2626" font-size="9" font-weight="bold">踏釘滑脫</text>
            <path d="M 90 90 L 90 140" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>

            <rect x="75" y="145" width="60" height="25" rx="3" fill="#1E293B"/>
            <text x="105" y="162" fill="#FFFFFF" font-size="8" text-anchor="middle">鋼絲剪</text>
            <text x="105" y="195" fill="#DC2626" font-size="10" font-weight="bold" text-anchor="middle">重擊腰椎致殘！</text>
          </g>

          <text x="147" y="240" fill="#7F1D1D" font-size="9" text-anchor="middle">高度僅 4 米（一樓半），但背部尖銳</text>
          <text x="147" y="255" fill="#7F1D1D" font-size="9" text-anchor="middle">工具撞擊直接引發脊椎粉碎骨折癱瘓</text>

          <rect x="290" y="20" width="245" height="270" rx="8" fill="#EFF6FF" stroke="#0284C7" stroke-width="2"/>
          <text x="412" y="45" fill="#0369A1" font-size="13" font-weight="bold" text-anchor="middle">高空物料傳遞與工具防護</text>

          <g transform="translate(310, 70)">
            <rect x="0" y="0" width="205" height="55" rx="4" fill="#FFFFFF" stroke="#EF4444"/>
            <text x="10" y="22" fill="#DC2626" font-size="10" font-weight="bold">❌ 嚴禁向下拋擲工具物料：</text>
            <text x="10" y="38" fill="#475569" font-size="9">小螺絲掉落加速度如砲彈，</text>
            <text x="10" y="49" fill="#475569" font-size="8">多次砸穿安全帽致地面人員身亡！</text>

            <rect x="0" y="70" width="205" height="55" rx="4" fill="#FFFFFF" stroke="#0284C7"/>
            <text x="10" y="92" fill="#0369A1" font-size="10" font-weight="bold">✅ 工具安全袋收納：</text>
            <text x="10" y="108" fill="#475569" font-size="9">手工具均須配備防墜繩，</text>
            <text x="10" y="119" fill="#475569" font-size="8">插放於大腿側袋，嚴禁置於背部腰椎。</text>

            <rect x="0" y="140" width="205" height="55" rx="4" fill="#F0FDF4" stroke="#16A34A"/>
            <text x="10" y="162" fill="#166534" font-size="10" font-weight="bold">✅ 滑輪繩索吊運物料：</text>
            <text x="10" y="178" fill="#475569" font-size="9">重型物料一律採用牽引繩吊袋，</text>
            <text x="10" y="189" fill="#15803D" font-size="8">地面下方半徑 3 米淨空！</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_confined_space_gas":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 20)">
            <rect x="0" y="0" width="245" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="122" y="30" fill="#002060" font-size="12" font-weight="bold" text-anchor="middle">局限空間四合一氣體標準</text>

            <rect x="15" y="45" width="215" height="45" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="25" y="65" fill="#1E40AF" font-size="10" font-weight="bold">1. 氧氣濃度 (O2) ＞ 18%</text>
            <text x="25" y="80" fill="#64748B" font-size="8">低於 18% 缺氧窒息；＞23% 劇烈助燃</text>

            <rect x="15" y="100" width="215" height="45" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="25" y="120" fill="#1E40AF" font-size="10" font-weight="bold">2. 一氧化碳 (CO) ＜ 35 ppm</text>
            <text x="25" y="135" fill="#64748B" font-size="8">無色無味，與血紅素結合致死</text>

            <rect x="15" y="155" width="215" height="45" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="25" y="175" fill="#1E40AF" font-size="10" font-weight="bold">3. 氫氣 (H2) 爆炸下限 ＜ 10%</text>
            <text x="25" y="190" fill="#64748B" font-size="8">密閉蓄電池室易積聚，微火花即爆</text>

            <rect x="15" y="210" width="215" height="45" rx="4" fill="#FEF2F2" stroke="#EF4444"/>
            <text x="25" y="230" fill="#DC2626" font-size="10" font-weight="bold">4. 硫化氫 (H2S) ＜ 10 ppm</text>
            <text x="25" y="245" fill="#991B1B" font-size="8">劇毒沼氣，麻痺嗅覺神經奪命</text>
          </g>

          <g transform="translate(290, 20)">
            <rect x="0" y="0" width="245" height="270" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
            <text x="122" y="30" fill="#991B1B" font-size="12" font-weight="bold" text-anchor="middle">硫化氫溶水「攪動暴釋」致死慘劇</text>

            <g transform="translate(20, 50)">
              <rect x="0" y="0" width="205" height="60" rx="4" fill="#FFFFFF" stroke="#F59E0B"/>
              <text x="10" y="20" fill="#B45309" font-size="10" font-weight="bold">初始靜止水體（測氣正常）：</text>
              <text x="10" y="38" fill="#64748B" font-size="9">硫化氫高濃度溶解於水底淤泥中，</text>
              <text x="10" y="50" fill="#64748B" font-size="8">水面上方氣體濃度初篩完全合格！</text>

              <path d="M 102 65 L 102 85" stroke="#DC2626" stroke-width="2"/>

              <rect x="0" y="85" width="205" height="65" rx="4" fill="#FFFFFF" stroke="#DC2626"/>
              <text x="10" y="105" fill="#DC2626" font-size="10" font-weight="bold">工人下水搓洗攪動（瞬間釋放）：</text>
              <text x="10" y="123" fill="#7F1D1D" font-size="9">如香檳開蓋！硫化氫大量噴發，</text>
              <text x="10" y="138" fill="#991B1B" font-size="8" font-weight="bold">吸入一口嗅覺神經秒癱瘓，昏倒溺死！</text>

              <path d="M 102 155 L 102 170" stroke="#16A34A" stroke-width="2"/>

              <rect x="0" y="170" width="205" height="40" rx="4" fill="#F0FDF4" stroke="#16A34A"/>
              <text x="10" y="188" fill="#166534" font-size="9" font-weight="bold">SOP：長桿攪水後二次測氣！</text>
              <text x="10" y="202" fill="#15803D" font-size="8">開蓋通風 15 分鐘，作業全程強迫抽排風</text>
            </g>
          </g>
        </svg>
        '''
    elif visual_type == "safety_excavation_shoring":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 20)">
            <rect x="0" y="0" width="245" height="270" rx="8" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="122" y="30" fill="#002060" font-size="12" font-weight="bold" text-anchor="middle">深開挖 1.5 米強制擋土支撐</text>

            <rect x="15" y="50" width="215" height="60" rx="4" fill="#FEF2F2" stroke="#EF4444"/>
            <text x="25" y="72" fill="#991B1B" font-size="10" font-weight="bold">開挖深度 ＞ 1.5 公尺法規紅線：</text>
            <text x="25" y="90" fill="#475569" font-size="9">土石 1m³ 重達 1.8 噸，塌方瞬間活埋！</text>
            <text x="25" y="102" fill="#DC2626" font-size="8" font-weight="bold">必須裝設鋼軌樁、擋土板或斜坡支撐</text>

            <rect x="15" y="125" width="215" height="55" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="25" y="145" fill="#1E40AF" font-size="10" font-weight="bold">露天開挖專任主管在場：</text>
            <text x="25" y="163" fill="#475569" font-size="9">取得勞動部證照主管全程在場，</text>
            <text x="25" y="174" fill="#64748B" font-size="8">監控地下水滲流與土壁裂紋變化</text>

            <rect x="15" y="195" width="215" height="55" rx="4" fill="#F0FDF4" stroke="#16A34A"/>
            <text x="25" y="215" fill="#166534" font-size="10" font-weight="bold">跨管線圖資協調會勘：</text>
            <text x="25" y="233" fill="#475569" font-size="9">動土前召集自來水、瓦斯、電信會勘，</text>
            <text x="25" y="244" fill="#15803D" font-size="8" font-weight="bold">杜絕挖斷天然氣引爆或挖斷光纖巨賠！</text>
          </g>

          <g transform="translate(290, 20)">
            <rect x="0" y="0" width="245" height="270" rx="8" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
            <text x="122" y="30" fill="#B45309" font-size="12" font-weight="bold" text-anchor="middle">斜坡立桿 2.1m 覆土失穩倒塌</text>

            <g transform="translate(20, 50)">
              <line x1="20" y1="20" x2="185" y2="120" stroke="#78350F" stroke-width="3"/>
              <text x="110" y="60" fill="#78350F" font-size="9">斜坡地面 (傾角 30°)</text>

              <rect x="80" y="40" width="20" height="90" fill="#64748B"/>
              <text x="90" y="30" fill="#1E293B" font-size="9" font-weight="bold" text-anchor="middle">電桿</text>

              <path d="M 105 75 Q 140 85 160 120" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
              <text x="155" y="105" fill="#DC2626" font-size="9" font-weight="bold">向空側倒塌 ➔</text>
            </g>

            <rect x="15" y="180" width="215" height="70" rx="4" fill="#FFFFFF" stroke="#D97706"/>
            <text x="25" y="200" fill="#92400E" font-size="10" font-weight="bold">斜坡立桿工程受力陷阱：</text>
            <text x="25" y="218" fill="#64748B" font-size="8">• 立桿入土深度標準 2.1 公尺</text>
            <text x="25" y="232" fill="#64748B" font-size="8">• 斜坡下坡側覆土缺乏橫向支撐力</text>
            <text x="25" y="244" fill="#DC2626" font-size="8" font-weight="bold">• 必須加裝斜向拉線或擴大基座澆灌</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_quality_traceability":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 20)">
            <rect x="0" y="0" width="165" height="270" rx="6" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="82" y="28" fill="#002060" font-size="11" font-weight="bold" text-anchor="middle">壓接套管壓縮次數</text>

            <rect x="10" y="45" width="145" height="95" rx="4" fill="#EFF6FF" stroke="#3B82F6"/>
            <text x="20" y="65" fill="#1E40AF" font-size="10" font-weight="bold">No. 1 規格電纜：</text>
            <text x="20" y="85" fill="#334155" font-size="9">套管兩側各壓 2 次</text>
            <text x="20" y="105" fill="#334155" font-size="9">共 4 次均勻壓實</text>
            <text x="20" y="125" fill="#15803D" font-size="8" font-weight="bold">確保低阻抗發熱</text>

            <rect x="10" y="155" width="145" height="95" rx="4" fill="#FEF3C7" stroke="#D97706"/>
            <text x="20" y="175" fill="#B45309" font-size="10" font-weight="bold">500 MCM 大線：</text>
            <text x="20" y="195" fill="#78350F" font-size="9">套管兩側各壓 3 次</text>
            <text x="20" y="215" fill="#78350F" font-size="9">共 6 次大噸位壓接</text>
            <text x="20" y="235" fill="#DC2626" font-size="8" font-weight="bold">少壓一次必融接頭！</text>
          </g>

          <g transform="translate(200, 20)">
            <rect x="0" y="0" width="165" height="270" rx="6" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="82" y="28" fill="#002060" font-size="11" font-weight="bold" text-anchor="middle">電纜頭簽字終身追溯</text>

            <rect x="10" y="45" width="145" height="205" rx="4" fill="#F0FDF4" stroke="#16A34A"/>
            <text x="20" y="70" fill="#166534" font-size="10" font-weight="bold">施作者簽名標籤：</text>
            <rect x="20" y="85" width="125" height="55" rx="3" fill="#FFFFFF" stroke="#86EFAC"/>
            <text x="82" y="105" fill="#15803D" font-size="9" font-weight="bold" text-anchor="middle">施作者：陳○○</text>
            <text x="82" y="125" fill="#64748B" font-size="8" text-anchor="middle">日期：2026/10/27</text>

            <text x="20" y="160" fill="#334155" font-size="9">• 完工接頭標籤簽名</text>
            <text x="20" y="180" fill="#334155" font-size="9">• 擊穿事故直接追溯</text>
            <text x="20" y="200" fill="#334155" font-size="9">• 劣質包商記錄停權</text>
            <text x="20" y="225" fill="#15803D" font-size="9" font-weight="bold">• 責任到人事故驟降</text>
          </g>

          <g transform="translate(375, 20)">
            <rect x="0" y="0" width="160" height="270" rx="6" fill="#F8FAFC" stroke="#002060" stroke-width="2"/>
            <text x="80" y="28" fill="#002060" font-size="11" font-weight="bold" text-anchor="middle">操作棒遠距切熔絲桶</text>

            <rect x="10" y="45" width="140" height="205" rx="4" fill="#FEF2F2" stroke="#EF4444"/>
            <text x="20" y="70" fill="#991B1B" font-size="10" font-weight="bold">絕緣操作棒鐵律：</text>
            <text x="20" y="95" fill="#7F1D1D" font-size="9">• 變壓器過載熔絲桶</text>
            <text x="20" y="115" fill="#7F1D1D" font-size="9">• 內部短路投入瞬間</text>
            <text x="20" y="135" fill="#DC2626" font-size="9" font-weight="bold">• 絕緣油瞬間汽化！</text>
            <text x="20" y="155" fill="#DC2626" font-size="9" font-weight="bold">• 數百升火油爆噴！</text>
            <text x="20" y="185" fill="#15803D" font-size="9" font-weight="bold">• 操作棒長度保障：</text>
            <text x="20" y="205" fill="#334155" font-size="8">立於爆噴半徑之外</text>
            <text x="20" y="225" fill="#334155" font-size="8">保證人員毫髮無傷</text>
          </g>
        </svg>
        '''
    elif visual_type == "safety_ten_commandments":
        return '''
        <svg viewBox="0 0 560 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
          <rect x="15" y="15" width="530" height="290" rx="8" fill="#002060" stroke="#D4AF37" stroke-width="2"/>
          <text x="280" y="42" fill="#D4AF37" font-size="15" font-weight="bold" text-anchor="middle">配電線路現場工作安全十條軍規（進金生維運工程師保命手冊）</text>

          <g transform="translate(30, 60)">
            <rect x="0" y="0" width="240" height="110" rx="6" fill="#0F172A" stroke="#38BDF8"/>
            <text x="120" y="22" fill="#38BDF8" font-size="11" font-weight="bold" text-anchor="middle">🛡️ 守規線（電氣本質防禦）</text>
            <text x="15" y="45" fill="#FFFFFF" font-size="9">1. 未完成檢電接地全流程，一律視為活電</text>
            <text x="15" y="65" fill="#FFFFFF" font-size="9">2. 自護為核心，絕不把生命托付他人</text>
            <text x="15" y="85" fill="#FFFFFF" font-size="9">3. 嚴格執行 5151 原則，單人單步閉環操作</text>
          </g>

          <g transform="translate(290, 60)">
            <rect x="0" y="0" width="240" height="110" rx="6" fill="#0F172A" stroke="#FBBF24"/>
            <text x="120" y="22" fill="#FBBF24" font-size="11" font-weight="bold" text-anchor="middle">🧗 防護線（高空車輛防墜）</text>
            <text x="15" y="45" fill="#FFFFFF" font-size="9">4. 高差 2m 必戴全身背負雙大鉤安全帶</text>
            <text x="15" y="65" fill="#FFFFFF" font-size="9">5. 工程車斜坡必放止滑墊，6年超音波探傷</text>
            <text x="15" y="85" fill="#FFFFFF" font-size="9">6. 起重機落實一機三證，0.25m 過卷自動停機</text>
          </g>

          <g transform="translate(30, 180)">
            <rect x="0" y="0" width="500" height="110" rx="6" fill="#0F172A" stroke="#34D399"/>
            <text x="250" y="22" fill="#34D399" font-size="11" font-weight="bold" text-anchor="middle">⚡ 作業與文化線（現場細節與直覺本能）</text>
            <text x="20" y="45" fill="#FFFFFF" font-size="9">7. 局限空間四合一測氣（長桿探入攪水二次驗，嚴防硫化氫暴釋）</text>
            <text x="20" y="65" fill="#FFFFFF" font-size="9">8. 深開挖超 1.5m 強制擋土支撐，動土前會同所有管線單位協調</text>
            <text x="20" y="85" fill="#FFFFFF" font-size="9">9. 電纜溝鋪設防火毯嚴禁踩踏；電纜頭施作人員簽字終身追溯責任制</text>
            <text x="20" y="102" fill="#FDE68A" font-size="9" font-weight="bold">10. 安全是直覺本能：只要張開眼睛，風險就在身邊，守護同仁平安回家！</text>
          </g>
        </svg>
        '''
    return "<div style='display:flex;align-items:center;justify-content:center;height:100%;color:#94A3B8;'>圖表載入中</div>"

# Generate slides HTML
slides_html = []
for s in slides_data:
    sn = s["slideNo"]
    active_cls = " active" if sn == 1 else ""
    svg_code = render_svg(s["visualType"])
    
    hl_items = "".join([f"<li>{h}</li>" for h in s["highlights"]])
    
    slide_block = f'''
      <!-- Slide {sn:02d} -->
      <section class="slide-item{active_cls}" id="s{sn}" 
               data-slide-index="{sn}"
               data-note-takeaway="{s['noteTakeaway']}"
               data-note-detail="{s['noteDetail']}"
               data-note-transition="{s['noteTransition']}">
        
        <!-- Header -->
        <div class="slide-header">
          <div class="slide-module-badge">{s["module"]}</div>
          <div class="slide-action-title">{s["title"]}</div>
          <div class="slide-source-ref">{s["ref"]}</div>
        </div>

        <!-- Body 2-Column Grid -->
        <div class="slide-body-grid">
          
          <!-- Left Column: Problem, Highlights, Takeaway -->
          <div class="slide-left-col">
            <div class="col-section core-question-box">
              <div class="sec-label">📌 本章要解決的問題／核心論點</div>
              <div class="sec-body question-text">{s["question"]}</div>
            </div>

            <div class="col-section highlights-box">
              <div class="sec-label">💡 1–3 個最值得記住的亮點（關鍵數據／案例）</div>
              <ul class="highlights-list">
                {hl_items}
              </ul>
            </div>

            <div class="col-section takeaway-box">
              <div class="sec-label">🎯 一句話總結</div>
              <div class="takeaway-text">{s["takeaway"]}</div>
            </div>
          </div>

          <!-- Right Column: Vector Diagram & Original Handout Thumbnail -->
          <div class="slide-right-col">
            <div class="diagram-wrapper">
              <div class="diagram-header">
                <span class="diagram-title">{s["visualTitle"]}</span>
                <span class="diagram-badge">向量圖表</span>
              </div>
              <div class="diagram-body">
                {svg_code}
              </div>
            </div>

            <div class="thumb-wrapper">
              <div class="thumb-header">
                <span>實體講義圖冊對照</span>
                <span class="thumb-expand-hint">點擊圖片放大 🔍</span>
              </div>
              <div class="thumb-img-container" data-img-src="{s['thumbImg']}" data-caption="{s['thumbCaption']}">
                <img src="{s['thumbImg']}" alt="{s['thumbCaption']}" class="thumb-img" onerror="this.src='../assets/images/slides/slide_01.jpg'">
                <div class="thumb-overlay">
                  <span>放大檢視高清講義 🔍</span>
                </div>
              </div>
              <div class="thumb-caption-text">{s["thumbCaption"]}</div>
            </div>
          </div>

        </div>
      </section>
    '''
    slides_html.append(slide_block)

full_html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>太陽光電設置乙級技術士回訓課程——配電線路現場工作安全注意事項說明｜麥肯錫風格專業簡報</title>
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
        <strong>進金生能源 6692</strong> ｜ 太陽光電設置乙級技術士回訓課程——配電線路現場工作安全注意事項說明
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
