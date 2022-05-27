import pandas as pd

class JpPrefecture(object):
    def __init__(self):
        self._prefecture_names = {
            "北海道" : 'Hokkaido',
            "青森県" : 'Aomori',
            "岩手県" : 'Iwate',
            "宮城県" : 'Miyagi',
            "秋田県" : 'Akita',
            "山形県" : 'Yamagata',
            "福島県" : 'Fukushima',
            "茨城県" : 'Ibaraki',
            "栃木県" : 'Tochigi',
            "群馬県" : 'Gunma',
            "埼玉県" : 'Saitama',
            "千葉県" : 'Chiba',
            "東京都" : 'Tokyo',
            "神奈川県" : 'Kanagawa',
            "新潟県" : 'Niigata',
            "富山県" : 'Toyama',
            "石川県" : 'Ishikawa',
            "福井県" : 'Fukui',
            "山梨県" : 'Yamanashi',
            "長野県" : 'Nagano',
            "岐阜県" : 'Gifu',
            "静岡県" : 'Shizuoka',
            "愛知県" : 'Aichi',
            "三重県" : 'Mie',
            "滋賀県" : 'Shiga',
            "京都府" : 'Kyoto',
            "大阪府" : 'Osaka',
            "兵庫県" : 'Hyogo',
            "奈良県" : 'Nara',
            "和歌山県" : 'Wakayama',
            "鳥取県" : 'Tottori',
            "島根県" : 'Shimane',
            "岡山県" : 'Okayama',
            "広島県" : 'Hiroshima',
            "山口県" : 'Yamaguchi',
            "徳島県" : 'Tokushima',
            "香川県" : 'Kagawa',
            "愛媛県" : 'Ehime',
            "高知県" : 'Kochi',
            "福岡県" : 'Fukuoka',
            "佐賀県" : 'Saga',
            "長崎県" : 'Nagasaki',
            "熊本県" : 'Kumamoto',
            "大分県" : 'Oita',
            "宮崎県" : 'Miyazaki',
            "鹿児島県" : 'Kagoshima',
            "沖縄県" : 'Okinawa',
        }

        # Index is code (JIS X 0401-1973)
        self.prefectures = pd.DataFrame(
            dict(
                name = [p for p in self._prefecture_names.keys()],
                short_name = [p[:-1] for p in self._prefecture_names.keys()],
                alphabet_name = [p for p in self._prefecture_names.values()],
            ),
            index = pd.Index(range(1, 1 + len(self._prefecture_names)),
                             name="code"),
        )

    def name2code(self, name: str) -> int:
        """ Convert prefecture name to code """
        code = None
        try:
            name = name.capitalize()
            for label in self.prefectures.columns:
                d = self.prefectures.index[self.prefectures[label] == name]
                if len(d):
                    code = d[0]
        except KeyError:
            pass
        return code

    def code2name(self, code: int) -> str:
        """ Convert prefecture code to name """
        try:
            name = self.prefectures.at[code, 'name']
        except KeyError:
            name = None
        return name

    def code2alphabet(self, code: int) -> str:
        """ Convert prefecture code to alphabet_name """
        try:
            name = self.prefectures.at[code, 'alphabet_name']
        except KeyError:
            name = None
        return name

    def name2alphabet(self, name: str) -> str:
        """ Convert a prefecture name to alphabet_name """
        alphabet = None
        try:
            name = name.capitalize()
            for label in self.prefectures.columns:
                d = self.prefectures.index[self.prefectures[label] == name]
                if len(d):
                    alphabet = self.prefectures.at[d[0], 'alphabet_name']
        except KeyError:
            pass
        return alphabet


    def alphabet2name(self, alphabet_name: str) -> str:
        """ Convert a prefecture alphabet_name to name """
        name = None
        try:
            alphabet_name = alphabet_name.capitalize()
            for label in self.prefectures.columns:
                d = self.prefectures.index[self.prefectures[label] == alphabet_name]
                if len(d):
                    name = self.prefectures.at[d[0], 'alphabet_name']
        except KeyError:
            pass

jp_prefectures = JpPrefecture()
