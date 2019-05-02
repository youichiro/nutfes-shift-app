"""アプリ共通変数の定義"""

# 学科
DEPARTMENTS = ['機械', '電気', '物材', '環社', '生物', '情経', '原子力', 'シス安', '未所属']

# 学年
GRADES = ['B1', 'B2', 'B3', 'B4', 'M1', 'M2', 'D1', 'D2', 'D3', 'その他']

# 所属
BELONGS = [
    ['委員長', '委員長'], ['副委員長', '副委員長'],
    # 総務局
    ['総務局-局長/副局長', '総務頭'], ['総務局-参加団体部門', '参加団体'], ['総務局-会場電力部門', '会場電力'],
    ['総務局-衛生管理部門', '衛生管理'], ['総務局-国際交流部門', '国際交流'], ['総務局-物品管理部門', '物品管理'],
    ['総務局-情報処理部門', '情報'], ['総務局-その他', '総務'],
    # 企画局
    ['企画局-局長/副局長', '企画頭'], ['企画局-ヒーローショー部門', 'ヒーローショー'],
    ['企画局-中夜祭部門', '中夜祭'], ['企画局-フレンドパーク部門', 'フレパ'], ['企画局-研究フォーラム部門', 'フォーラム'],
    ['企画局-ビンゴ部門', 'ビンゴ'], ['企画局-ゆるキャラ部門', 'ゆるキャラ'], ['企画局-その他', '企画'],
    # 制作局
    ['制作局-局長/副局長', '制作頭'], ['制作局-総務局窓口部門', '制作総務'], ['制作局-渉外局窓口部門', '制作渉外'],
    ['制作局-企画局窓口部門', '制作企画'], ['制作局-Webデザイン部門', 'Webデザイン'], ['制作局-その他', '制作'],
    # 渉外局
    ['渉外局-局長/副局長', '渉外頭'], ['渉外局-広報部門', '広報'], ['渉外局-演舞誘致部門', '演舞'],
    ['渉外局-企業協賛部門', '企業協賛'], ['渉外局-ゲスト部門', 'ゲスト'], ['渉外局-フリマ誘致部門', 'フリマ'],
    ['渉外局-その他', '渉外'],
    # 財務局
    ['財務局-局長/副局長', '財務頭'], ['財務局-局長補佐', '財務補佐'], ['財務局-補助金管理部門', '補助金'],
    ['財務局-ごはん関連部門', 'ごはん'], ['財務局-その他', '財務'],
    # その他
    ['未所属', '未所属'],
]

# 今年度の実施日
FES_DATES = [
    ['準備日', '2019-09-13'],
    ['1日目晴', '2019-09-14'],
    ['1日目雨', '2019-09-14'],
    ['2日目晴', '2019-09-15'],
    ['2日目雨', '2019-09-15'],
]

# タスクの実施場所
PLACES = ['24', 'セコム', '本部', 'ポパイ', '講義棟', '受付1', '受付2', '受付3',
          '体育館', 'メインステージ', 'サブステージ']

# シフトの時間
SHIFT_START_TIME = '08:00:00'  # 開始時間
SHIFT_END_TIME = '20:00:00'  # 終了時間
SHIFT_INTERVAL = 30  # 時間間隔(分指定)
