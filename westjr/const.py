# 広域エリア
areas = [
    "hokuriku",
    "kinki",
    "okayama",
    "hiroshima",
    "sanin"
]

# 駅名ID: 駅名
st = {
    # hokuriku
    "hokuriku": {'0482': '金沢', '0481': '西金沢', '0480': '野々市', '0479': '松任', '0478': '加賀笠間', '0477': '美川', '0476': '小舞子', '0475': '能美根上', '0474': '明峰', '0473': '小松', '0472': '粟津', '0471': '動橋', '0470': '加賀温泉', '0469': '大聖寺', '0468': '牛ノ谷', '0467': '細呂木', '0466': '芦原温泉', '0465': '丸岡', '0464': '春江', '0463': '森田', '0462': '福井', '0460': '越前花堂', '0459': '大土呂', '0458': '北鯖江', '0457': '鯖江', '0456': '武生', '0455': '王子保', '0454': '南条', '0453': '湯尾', '0452': '今庄', '0451': '南今庄', '0450': '敦賀', '0449': '新疋田', '0448': '近江塩津'},

    # kinki
    "ako": {'0455': '竜野', '0456': '相生', '2301': '西相生', '2302': '坂越', '2303': '播州赤穂', '2305': '天和'},
    "bantan": {'0425': '姫路', '0426': '京口', '0427': '野里', '0428': '砥堀', '0429': '仁豊野', '0430': '香呂', '0431': '溝口', '0432': '福崎', '0433': '甘地', '0434': '鶴居', '0435': '新野', '0436': '寺前', '0437': '長谷', '0438': '生野', '0439': '新井', '0440': '青倉', '0441': '竹田', '0391': '和田山'},
    "fukuchiyama": {'0409': '新三田', '0410': '広野', '0411': '相野', '0412': '藍本', '0413': '草野', '0414': '古市', '0415': '南矢代', '0416': '篠山口', '0417': '丹波大山', '0418': '下滝', '0419': '谷川', '0420': '柏原', '0421': '石生', '0422': '黒井', '0423': '市島', '0424': '丹波竹田', '0386': '福知山'},
    "gakkentoshi": {'3022': '平城山', '3023': '木津', '1322': '西木津', '1321': '祝園', '1320': '下狛', '1319': 'ＪＲ三山木', '1318': '同志社前', '1317': '京田辺', '1316': '大住', '1315': '松井山手', '1314': '長尾', '1313': '藤阪', '1312': '津田', '1311': '河内磐船', '1310': '星田', '1309': '寝屋川公園', '1308': '忍ケ丘', '1307': '四条畷', '1306': '野崎', '1305': '住道', '1304': '鴻池新田', '1303': '徳庵', '1302': '放出', '1301': '鴫野', '2517': '京橋', '1501': '大阪城北詰'},
    "hanwahagoromo": {'2509': '新今宮', '2510': '天王寺', '2601': '美章園', '2602': '南田辺', '2603': '鶴ケ丘', '2604': '長居', '2605': '我孫子町', '2606': '杉本町', '2607': '浅香', '2608': '堺市', '2609': '三国ケ丘', '2610': '百舌鳥', '2611': '上野芝', '6061': '津久野', '2613': '鳳', '2651': '東羽衣', '2614': '富木', '2615': '北信太', '2616': '信太山', '2617': '和泉府中', '2618': '久米田', '2619': '下松', '2620': '東岸和田', '2621': '東貝塚', '2622': '和泉橋本', '2623': '東佐野', '2624': '熊取', '2625': '日根野', '3701': '長滝', '3702': '新家', '3703': '和泉砂川', '3704': '和泉鳥取', '3705': '山中渓', '3706': '紀伊', '3707': '六十谷', '3708': '紀伊中ノ島', '3709': '和歌山'},
    "hokurikubiwako": {'0510': '新疋田', '0509': '近江塩津', '0508': '余呉', '0507': '木ノ本', '0506': '高月', '0505': '河毛', '0504': '虎姫', '0503': '長浜', '0502': '田村', '0501': '坂田', '0382': '米原', '0384': '彦根', '0385': '南彦根', '0386': '河瀬', '0387': '稲枝', '0388': '能登川', '0389': '安土', '0390': '近江八幡', '0391': '篠原', '0392': '野洲', '0393': '守山', '0394': '栗東', '0395': '草津', '0396': '南草津', '0397': '瀬田', '0398': '石山', '0399': '膳所', '0400': '大津', '0401': '山科', '0402': '京都', '0404': '西大路'},
    "kansai": {'0577': '加茂', '0576': '笠置', '0575': '大河原', '0574': '月ケ瀬口', '0573': '島ケ原', '0572': '伊賀上野', '0571': '佐那具', '0570': '新堂', '0569': '柘植', '0568': '加太', '0567': '関', '0566': '亀山'},
    "kansaiairport": {'2624': '熊取', '2625': '日根野', '2701': 'りんくうタウン', '2702': '関西空港'},
    "kinokuni": {'0542': '和歌山', '0541': '宮前', '0540': '紀三井寺', '0539': '黒江', '0538': '海南', '0537': '冷水浦', '0536': '加茂郷', '0535': '下津', '0534': '初島', '0533': '箕島', '0532': '紀伊宮原', '0531': '藤並', '0530': '湯浅', '0529': '広川ビーチ', '0528': '紀伊由良', '0527': '紀伊内原', '0526': '御坊', '0525': '道成寺', '0524': '和佐', '0523': '稲原', '0522': '印南', '0521': '切目', '0520': '岩代', '0519': '南部', '0518': '芳養', '0517': '紀伊田辺', '0516': '紀伊新庄', '0515': '朝来', '0514': '白浜', '0513': '紀伊富田', '0512': '椿', '0511': '紀伊日置', '0510': '周参見', '0508': '見老津', '0507': '江住', '0506': '和深', '0505': '田子', '0504': '田並', '0503': '紀伊有田', '0502': '串本', '0501': '紀伊姫', '0500': '古座', '0499': '紀伊田原', '0498': '紀伊浦神', '0497': '下里', '0496': '太地', '0495': '湯川', '0494': '紀伊勝浦', '0493': '紀伊天満', '0492': '那智', '0491': '宇久井', '0490': '紀伊佐野', '0489': '三輪崎', '0488': '新宮'},
    "kobesanyo": {'0415': '新大阪', '0416': '大阪', '0417': '塚本', '0419': '尼崎', '0420': '立花', '0421': '甲子園口', '0422': '西宮', '0460': 'さくら夙川', '0423': '芦屋', '0424': '甲南山手', '0425': '摂津本山', '0426': '住吉', '0427': '六甲道', '0428': '摩耶', '0429': '灘', '0430': '三ノ宮', '0431': '元町', '0432': '神戸', '0433': '兵庫', '0434': '新長田', '0435': '鷹取', '0462': '須磨海浜公園', '0436': '須磨', '0437': '塩屋', '0438': '垂水', '0439': '舞子', '0440': '朝霧', '0441': '明石', '0442': '西明石', '0443': '大久保', '0444': '魚住', '0445': '土山', '0446': '東加古川', '0447': '加古川', '0448': '宝殿', '0449': '曽根', '0450': 'ひめじ別所', '0451': '御着', '0465': '東姫路', '0452': '姫路', '0453': '英賀保', '0463': 'はりま勝原', '0454': '網干', '0455': '竜野', '0456': '相生', '0457': '有年', '0458': '上郡', '0459': '三石'},
    "kosei": {'0510': '新疋田', '0509': '近江塩津', '0919': '永原', '0618': 'マキノ', '0617': '近江中庄', '0616': '近江今津', '0615': '新旭', '0614': '安曇川', '0613': '近江高島', '0612': '北小松', '0611': '近江舞子', '0610': '比良', '0609': '志賀', '0608': '蓬莱', '0607': '和邇', '0606': '小野', '0605': '堅田', '0604': 'おごと温泉', '0603': '比叡山坂本', '0602': '唐崎', '0601': '大津京', '0401': '山科', '0402': '京都', '0404': '西大路'},
    "kusatsu": {'0587': '草津', '0586': '手原', '0585': '石部', '0584': '甲西', '0583': '三雲', '0582': '貴生川', '0581': '甲南', '0580': '寺庄', '0579': '甲賀', '0578': '油日', '0569': '柘植'},
    "kyoto": {'0401': '山科', '0402': '京都', '0404': '西大路', '0464': '桂川', '0405': '向日町', '0406': '長岡京', '0407': '山崎', '0461': '島本', '0408': '高槻', '0409': '摂津富田', '0466': 'ＪＲ総持寺', '0410': '茨木', '0411': '千里丘', '0412': '岸辺', '0413': '吹田', '0414': '東淀川', '0415': '新大阪', '0416': '大阪', '0417': '塚本'},
    "maizuru": {'0383': '綾部', '0442': '淵垣', '0443': '梅迫', '0444': '真倉', '0445': '西舞鶴', '0446': '東舞鶴'},
    "manyomahoroba": {'0588': '奈良', '0589': '京終', '0590': '帯解', '0591': '櫟本', '0592': '天理', '0593': '長柄', '0594': '柳本', '0595': '巻向', '0596': '三輪', '0597': '桜井', '0598': '香久山', '0599': '畝傍', '0600': '金橋', '0601': '高田'},
    "nara": {'0227': '京都', '0226': '東福寺', '0225': '稲荷', '0224': 'JR藤森', '0223': '桃山', '0222': '六地蔵', '0221': '木幡', '0220': '黄檗', '0219': '宇治', '0218': 'JR小倉', '0217': '新田', '0216': '城陽', '0215': '長池', '0214': '山城青谷', '0213': '山城多賀', '0212': '玉水', '0211': '棚倉', '0210': '上狛', '0228': '木津'},
    "osakahigashi": {'0415': '新大阪', '1204': '南吹田', '1206': 'ＪＲ淡路', '1207': '城北公園通', '1208': 'ＪＲ野江', '1301': '鴫野', '1302': '放出', '8006': '高井田中央', '8005': 'ＪＲ河内永和', '8004': 'ＪＲ俊徳道', '8003': 'ＪＲ長瀬', '8007': '衣摺加美北', '8001': '新加美', '3009': '久宝寺', '3010': '八尾'},
    "osakaloop": {'0416': '大阪', '2501': '福島', '2502': '野田', '2503': '西九条', '2504': '弁天町', '2506': '大正', '2507': '芦原橋', '2508': '今宮', '2509': '新今宮', '2510': '天王寺', '2511': '寺田町', '2512': '桃谷', '2513': '鶴橋', '2514': '玉造', '2515': '森ノ宮', '2516': '大阪城公園', '2517': '京橋', '2518': '桜ノ宮', '2519': '天満'},
    "sagano": {'0227': '京都', '0229': '梅小路京都西', '0230': '丹波口', '0231': '二条', '0232': '円町', '0233': '花園', '0234': '太秦', '0235': '嵯峨嵐山', '0236': '保津峡', '0237': '馬堀', '0238': '亀岡', '0239': '並河', '0240': '千代川', '0241': '八木', '0242': '吉富', '0243': '園部'},
    "sanin1": {'0243': '園部', '0244': '船岡', '0375': '日吉', '0376': '鍼灸大学前', '0377': '胡麻', '0378': '下山', '0379': '和知', '0380': '安栖里', '0381': '立木', '0382': '山家', '0383': '綾部', '0384': '高津', '0385': '石原', '0386': '福知山'},
    "sanin2": {'0386': '福知山', '0387': '上川口', '0388': '下夜久野', '0389': '上夜久野', '0390': '梁瀬', '0391': '和田山', '0392': '養父', '0393': '八鹿', '0395': '江原', '0396': '国府', '0397': '豊岡', '0398': '玄武洞', '0399': '城崎温泉', '0400': '竹野', '0401': '佐津', '0402': '柴山', '0403': '香住', '0404': '鎧', '0405': '餘部', '0406': '久谷', '0407': '浜坂', '0408': '諸寄', '0000': '居組'},
    "takarazuka": {'0415': '新大阪', '0416': '大阪', '0417': '塚本', '0419': '尼崎', '1601': '塚口', '1602': '猪名寺', '1603': '伊丹', '1604': '北伊丹', '1605': '川西池田', '1606': '中山寺', '1607': '宝塚', '1608': '生瀬', '1609': '西宮名塩', '1610': '武田尾', '1611': '道場', '1612': '三田', '1613': '新三田', '1614': '広野'},
    "tozai": {'1301': '鴫野', '2517': '京橋', '1501': '大阪城北詰', '1502': '大阪天満宮', '1503': '北新地', '1504': '新福島', '1505': '海老江', '1506': '御幣島', '1508': '加島', '0419': '尼崎', '1601': '塚口', '0420': '立花'},
    "wakayama1": {'0543': '五条', '0544': '大和二見', '0545': '隅田', '0546': '下兵庫', '0547': '橋本', '0548': '紀伊山田', '0549': '高野口', '0550': '中飯降', '0551': '妙寺', '0552': '大谷', '0553': '笠田', '0554': '西笠田', '0555': '名手', '0556': '粉河', '0557': '紀伊長田', '0558': '打田', '0559': '下井阪', '0560': '岩出', '0561': '船戸', '0562': '紀伊小倉', '0563': '布施屋', '0564': '千旦', '0565': '田井ノ瀬', '0542': '和歌山'},
    "wakayama2": {'0602': '王寺', '0603': '畠田', '0604': '志都美', '0605': '香芝', '0606': 'JR五位堂', '0601': '高田', '0607': '大和新庄', '0608': '御所', '0609': '玉手', '0610': '掖上', '0611': '吉野口', '0612': '北宇智', '0543': '五条'},
    "yamatoji": {'3002': 'ＪＲ難波', '2508': '今宮', '2509': '新今宮', '2510': '天王寺', '3003': '東部市場前', '3005': '平野', '3008': '加美', '3009': '久宝寺', '3010': '八尾', '3011': '志紀', '3012': '柏原', '3013': '高井田', '3014': '河内堅上', '3015': '三郷', '3016': '王寺', '3017': '法隆寺', '3018': '大和小泉', '3019': '郡山', '3020': '奈良', '3022': '平城山', '3023': '木津', '3024': '加茂', '3025': '笠置'},
    "yumesaki": {'2502': '野田', '2503': '西九条', '2551': '安治川口', '2552': 'ユニバーサルシティ', '2553': '桜島'},

    # okayama
    "hakubi1": {'0075': '倉敷', '0076': '清音', '0077': '総社', '0078': '豪渓', '0079': '日羽', '0080': '美袋', '0081': '備中広瀬', '0082': '備中高梁', '0083': '木野山', '0084': '備中川面', '0085': '方谷', '0087': '井倉', '0088': '石蟹', '0089': '新見', '0090': '布原', '0091': '備中神代', '0092': '足立', '0093': '新郷'},
    "sanyo1": {'0265': '上郡', '0266': '三石', '0267': '吉永', '0268': '和気', '0269': '熊山', '0270': '万富', '0271': '瀬戸', '0272': '上道', '0273': '東岡山', '0274': '高島', '0275': '西川原', '0245': '岡山', '0277': '北長瀬', '0278': '庭瀬', '0279': '中庄', '0075': '倉敷', '0280': '西阿知', '0281': '新倉敷', '0282': '金光', '0283': '鴨方', '0284': '里庄', '0285': '笠岡', '0286': '大門', '0287': '東福山', '0288': '福山', '0289': '備後赤坂', '0290': '松永', '0291': '東尾道', '0292': '尾道', '0106': '糸崎', '0107': '三原'},
    "setoohashi": {'0245': '岡山', '0246': '大元', '0247': '備前西市', '0248': '妹尾', '0249': '備中箕島', '0250': '早島', '0251': '久々原', '0252': '茶屋町', '0253': '植松', '0254': '木見', '0255': '上の町', '0256': '児島'},
    "unominato": {'0252': '茶屋町', '0258': '彦崎', '0259': '備前片岡', '0260': '迫川', '0261': '常山', '0262': '八浜', '0263': '備前田井', '0264': '宇野'},

    # hiroshima
    "kabe": {'0122': '広島', '0123': '新白島', '0124': '横川', '0199': '三滝', '0200': '安芸長束', '0201': '下祇園', '0202': '古市橋', '0203': '大町', '0204': '緑井', '0205': '七軒茶屋', '0206': '梅林', '0207': '上八木', '0208': '中島', '0209': '可部', '0312': '河戸帆待川', '0313': 'あき亀山'},
    "kure": {'0107': '三原', '0173': '須波', '0174': '安芸幸崎', '0175': '忠海', '0176': '安芸長浜', '0177': '大乗', '0178': '竹原', '0179': '吉名', '0180': '安芸津', '0181': '風早', '0182': '安浦', '0183': '安登', '0184': '安芸川尻', '0185': '仁方', '0186': '広', '0187': '新広', '0188': '安芸阿賀', '0189': '呉', '0190': '川原石', '0191': '吉浦', '0192': 'かるが浜', '0193': '天応', '0194': '呉ポートピア', '0195': '小屋浦', '0196': '水尻', '0197': '坂', '0198': '矢野', '0118': '海田市', '0119': '向洋', '0120': '天神川', '0122': '広島'},
    "sanyo2": {'0106': '糸崎', '0107': '三原', '0108': '本郷', '0109': '河内', '0110': '入野', '0111': '白市', '0112': '西高屋', '0113': '西条', '0447': '寺家', '0114': '八本松', '0115': '瀬野', '0116': '中野東', '0117': '安芸中野', '0118': '海田市', '0119': '向洋', '0120': '天神川', '0122': '広島', '0123': '新白島', '0124': '横川', '0125': '西広島', '0126': '新井口', '0127': '五日市', '0128': '廿日市', '0129': '宮内串戸', '0130': '阿品', '0131': '宮島口', '0132': '前空', '0133': '大野浦', '0134': '玖波', '0135': '大竹', '0136': '和木', '0137': '岩国', '0138': '南岩国'},
    "sanyo3": {'0137': '岩国', '0138': '南岩国', '0139': '藤生', '0140': '通津', '0141': '由宇', '0142': '神代', '0143': '大畠', '0144': '柳井港', '0145': '柳井', '0146': '田布施', '0147': '岩田', '0148': '島田', '0149': '光', '0150': '下松', '0151': '櫛ヶ浜', '0152': '徳山', '0153': '新南陽', '0154': '福川', '0155': '戸田', '0156': '富海', '0157': '防府', '0158': '大道', '0159': '四辻', '0160': '新山口', '0161': '嘉川', '0162': '本由良', '0163': '厚東', '0164': '宇部', '0165': '小野田', '0166': '厚狭', '0167': '埴生', '0168': '小月', '0169': '長府', '0170': '新下関', '0171': '幡生', '0172': '下関'},

    # sanin
    "hakubi2": {'0093': '新郷', '0094': '上石見', '0096': '生山', '0097': '上菅', '0098': '黒坂', '0099': '根雨', '0100': '武庫', '0101': '江尾', '0103': '伯耆溝口', '0104': '岸本', '0027': '伯耆大山'},
    "imbi1": {'0621': '智頭', '0620': '因幡社', '0619': '用瀬', '0618': '鷹狩', '0617': '国英', '0616': '河原', '0615': '郡家', '0614': '東郡家', '0613': '津ノ井', '0006': '鳥取'},
    "sanin3": {'0408': '諸寄', '0000': '居組', '0001': '東浜', '0002': '岩美', '0003': '大岩', '0004': '福部', '0006': '鳥取', '0007': '湖山', '0008': '鳥取大学前', '0009': '末恒', '0010': '宝木', '0011': '浜村', '0012': '青谷', '0013': '泊', '0014': '松崎', '0015': '倉吉', '0016': '下北条', '0017': '由良', '0018': '浦安', '0019': '八橋', '0020': '赤碕', '0021': '中山口', '0022': '下市', '0023': '御来屋', '0024': '名和', '0025': '大山口', '0026': '淀江', '0027': '伯耆大山', '0028': '東山公園', '0029': '米子'},
    "sanin4": {'0029': '米子', '0031': '安来', '0032': '荒島', '0033': '揖屋', '0034': '東松江', '0035': '松江', '0036': '乃木', '0037': '玉造温泉', '0038': '来待', '0039': '宍道', '0040': '荘原', '0041': '直江', '0042': '出雲市', '0043': '西出雲', '0044': '出雲神西', '0045': '江南', '0046': '小田', '0047': '田儀', '0048': '波根', '0049': '久手', '0050': '大田市', '0051': '静間', '0052': '五十猛', '0053': '仁万', '0054': '馬路', '0055': '湯里', '0056': '温泉津', '0057': '石見福光', '0058': '黒松', '0059': '浅利', '0060': '江津', '0061': '都野津', '0062': '敬川', '0063': '波子', '0064': '久代', '0065': '下府', '0066': '浜田', '0067': '西浜田', '0068': '周布', '0069': '折居', '0070': '三保三隅', '0071': '岡見', '0072': '鎌手', '0073': '石見津田', '0074': '益田'}
}

# 路線名
lines = [
    "hokuriku",
    "kobesanyo",
    "hokurikubiwako",
    "kyoto",
    "ako",
    "kosei",
    "kusatsu",
    "nara",
    "sagano",
    "sanin1",
    "sanin2",
    "osakahigashi",
    "takarazuka",

]

# 停車種別対応配列
stopTrains = [
    "",
    "新快速",
    "快速",
    "区間快速",
    "直通快速",
    "特急",
    "急行",
    "寝台",
    "SL",
    "観光列車",
    "瑞風"
]

# 路線ID: 路線名
realname = {
    "hokuriku": "北陸線",
    "biwako": "琵琶湖線",
    "kyoto": "JR京都線",
    "kobe": "JR神戸線",
    "sanyo": "山陽線",
    "ako": "赤穂線",
    "kosei": "湖西線",
    "kusatsu": "草津線",
    "nara": "奈良線",
    "sagano": "嵯峨野線",
    "sanin": "山陰線",
    "osakahigashi": "おおさか東線",
    "takarazuka": "JR宝塚線",
    "fukuchiyama": "福知山線",
    "tozai": "JR東西線",
    "gakkentoshi": "学研都市線",
    "kakogawa": "加古川線",
    "bantan": "播但線",
    "kishin": "姫新線",
    "maizuru": "舞鶴線",
    "osakaloop": "大阪環状線",
    "yumesaki": "JRゆめ咲線",
    "yamatoji": "大和路線",
    "hanwa": "阪和線",
    "kansaiairport": "関西空港線",
    "kansai": "関西線",
    "wakayama2": "和歌山線",
    "wakayama1": "和歌山線",
    "manyomahoroba": "万葉まほろば線",
    "kinokuni": "きのくに線",
    "imbi1": "因美線"
 }