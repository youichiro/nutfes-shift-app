"""アプリ共通変数の定義"""

# 学科
DEPARTMENTS = ['機械', '電気', '物材', '環社', '建設', '生物', '情経', '原子力', 'シス安', '未所属']

# 学年
GRADES = ['D3', 'D2', 'D1', 'M2', 'M1', 'B4', 'B3', 'B2', 'B1', 'その他']

BELONG_COLORS = {
    '委員長': 'tomato',
    '副委員長': 'tomato',
    '総務局': 'green',
    '企画局': 'orange',
    '制作局': 'pink',
    '渉外局': 'blue',
    '財務局': 'gold',
}

# 所属 ([局, 部門, 略称, color])
BELONGS = [
    ['委員長', None, '委員長', BELONG_COLORS['委員長']],
    ['副委員長', None, '副委員長', BELONG_COLORS['副委員長']],
    # 総務局
    ['総務局', '局長', '総務局長', BELONG_COLORS['総務局']],
    ['総務局', '副局長', '総務副局長', BELONG_COLORS['総務局']],
    ['総務局', '参加団体部門', '参加団体', BELONG_COLORS['総務局']],
    ['総務局', '会場電力部門', '会場電力', BELONG_COLORS['総務局']],
    ['総務局', '衛生管理部門', '衛生管理', BELONG_COLORS['総務局']],
    ['総務局', '国際交流部門', '国際交流', BELONG_COLORS['総務局']],
    ['総務局', '物品管理部門', '物品管理', BELONG_COLORS['総務局']],
    ['総務局', '情報処理部門', '情報', BELONG_COLORS['総務局']],
    ['総務局', 'その他', '総務局員', BELONG_COLORS['総務局']],
    # 企画局
    ['企画局', '局長', '企画局長', BELONG_COLORS['企画局']],
    ['企画局', '副局長', '企画副局長', BELONG_COLORS['企画局']],
    ['企画局', 'ヒーローショー部門', 'ヒーローショー', BELONG_COLORS['企画局']],
    ['企画局', '中夜祭部門', '中夜祭', BELONG_COLORS['企画局']],
    ['企画局', 'フレンドパーク部門', 'フレパ', BELONG_COLORS['企画局']],
    ['企画局', '研究フォーラム部門', 'フォーラム', BELONG_COLORS['企画局']],
    ['企画局', 'ビンゴ部門', 'ビンゴ', BELONG_COLORS['企画局']],
    ['企画局', 'ゆるキャラ部門', 'ゆるキャラ', BELONG_COLORS['企画局']],
    ['企画局', '脱出ゲーム部門', '脱出ゲーム', BELONG_COLORS['企画局']],
    ['企画局', 'その他', '企画局員', BELONG_COLORS['企画局']],
    # 制作局
    ['制作局', '局長', '制作局長', BELONG_COLORS['制作局']],
    ['制作局', '副局長', '制作副局長', BELONG_COLORS['制作局']],
    ['制作局', '総務局窓口部門', '制作総務', BELONG_COLORS['制作局']],
    ['制作局', '渉外局窓口部門', '制作渉外', BELONG_COLORS['制作局']],
    ['制作局', '企画局窓口部門', '制作企画', BELONG_COLORS['制作局']],
    ['制作局', 'Webデザイン部門', 'Webデザイン', BELONG_COLORS['制作局']],
    ['制作局', 'その他', '制作局員', BELONG_COLORS['制作局']],
    # 渉外局
    ['渉外局', '局長', '渉外局長', BELONG_COLORS['渉外局']],
    ['渉外局', '副局長', '渉外副局長', BELONG_COLORS['渉外局']],
    ['渉外局', 'ゲスト部門', 'ゲスト', BELONG_COLORS['渉外局']],
    ['渉外局', '地域他大学誘致部門', '地域他大', BELONG_COLORS['渉外局']],
    ['渉外局', '広報部門', '広報', BELONG_COLORS['渉外局']],
    ['渉外局', '演舞誘致部門', '演舞', BELONG_COLORS['渉外局']],
    ['渉外局', '企業協賛部門', '企業協賛', BELONG_COLORS['渉外局']],
    ['渉外局', 'フリマ誘致部門', 'フリマ', BELONG_COLORS['渉外局']],
    ['渉外局', 'その他', '渉外局員', BELONG_COLORS['渉外局']],
    # 財務局
    ['財務局', '局長', '財務局長', BELONG_COLORS['財務局']],
    ['財務局', '副局長', '財務副局長', BELONG_COLORS['財務局']],
    ['財務局', '局長補佐部門', '財務補佐', BELONG_COLORS['財務局']],
    ['財務局', '補助金管理部門', '補助金', BELONG_COLORS['財務局']],
    ['財務局', 'ごはん関連部門', 'ごはん', BELONG_COLORS['財務局']],
    ['財務局', 'その他', '財務局員', BELONG_COLORS['財務局']],
    # その他
    ['未所属', None, '未所属', 'black'],
]

# 天気
WEATHERS = [('晴', '晴'), ('雨', '雨')]

# シート名
SHEETS = [
    {
        "name": "準備日晴れ",
        "day": 13,
        "weather": WEATHERS[0][0]
    },
    {
        "name": "準備日雨",
        "day": 13,
        "weather": WEATHERS[1][0]
    },
    {
        "name": "1日目晴れ",
        "day": 14,
        "weather": WEATHERS[0][0]
    },
    {
        "name": "1日目雨",
        "day": 14,
        "weather": WEATHERS[1][0]
    },
    {
        "name": "2日目晴れ",
        "day": 15,
        "weather": WEATHERS[0][0]
    },
    {
        "name": "2日目雨",
        "day": 15,
        "weather": WEATHERS[1][0]
    },
    {
        "name": "片付け日晴れ",
        "day": 16,
        "weather": WEATHERS[0][0]
    },
    {
        "name": "片付け日雨",
        "day": 16,
        "weather": WEATHERS[1][0]
    }
]

# シフトの時間
SHIFT_START_TIME = '06:00:00'  # 開始時間
SHIFT_END_TIME = '23:00:00'  # 終了時間
SHIFT_INTERVAL = 30  # 時間間隔(分指定)
SHIFT_START_ROW = 3
