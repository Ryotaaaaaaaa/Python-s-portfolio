"""
レイアウト
↓
ウインドウ作成
↓　                                        ←どこかのタイミングでボタンアクション入れる
ウインドウのイベントループ
↓
ウインドウを閉じる
"""
import PySimpleGUI as sg
import random
import webbrowser

WorldHeritage = ["法隆寺地域の仏教建造物　奈良県", "姫路城　兵庫県", "屋久島	鹿児島県", "白神山地	青森県・秋田県", "古都京都の文化財（京都市、宇治市、大津市）	京都府・滋賀県", "白川郷・五箇山の合掌造り集落	岐阜県・富山県"
, "原爆ドーム	広島県", "厳島神社	広島県", "古都奈良の文化財	奈良県", "日光の社寺	栃木県", "琉球王国のグスク及び関連遺産群	沖縄県", "紀伊山地の霊場と参詣道	三重県・奈良県・和歌山県", "知床	北海道", "石見銀山遺跡とその文化的景観	島根県"
, "小笠原諸島	東京都", "平泉‐仏国土（浄土）を表す建築・庭園及び考古学的遺跡群‐	岩手県" , "富士山‐信仰の対象と芸術の源泉‐	山梨県・静岡県", "富岡製糸場と絹産業遺産群	群馬県", "明治日本の産業革命遺産　製鉄・製鋼、造船、石炭産業	福岡県・佐賀県・長崎県・熊本県・鹿児島県・山口県・岩手県・静岡県"
, "ル・コルビュジエの建築作品‐近代建築運動への顕著な貢献‐	東京都", "「神宿る島」宗像・沖ノ島と関連遺産群	福岡県", "長崎と天草地方の潜伏キリシタン関連遺産	長崎県・熊本県", "百舌鳥・古市古墳群‐古代日本の墳墓群‐	大阪府", "奄美大島、徳之島、沖縄島北部及び西表島	鹿児島県・沖縄県", "北海道・北東北の縄文遺跡群	北海道・青森県・岩手県・秋田県"]

sg.theme('Material1')

# ウィンドウのレイアウト
layout = [ 
            [sg.Button('日本の世界遺産'), sg.MLine(size=(40,8), key = 'tx1')],
            [
   sg.Text('サイトリンク', font=('メイリオ', 10), auto_size_text=True),
   sg.Button('古都京都の文化財'),
   sg.Button('厳島神社'),
   sg.Button('日光の社寺'),
   ],
   #[sg.Button('aaa')]
          ]

# ウィンドウオブジェクトの作成
window = sg.Window('PySimpleGUI Sample', layout, size=(600, 300))

# イベントループ
while True:
   event, value = window.read() # イベント読み取り（ここでイベント待ち）
   #　「日本の世界遺産」を押したときの処理
   if event == '日本の世界遺産':

            #　ランダムを起動する
            WorldHeritage_random = random.choice(WorldHeritage)
            window['tx1'].update(WorldHeritage_random)

   if event == '古都京都の文化財':
       webbrowser.open('https://bunka.nii.ac.jp/special_content/hlink3')
   if event == '厳島神社':
       webbrowser.open('https://bunka.nii.ac.jp/special_content/hlink6')
   if event == '日光の社寺':
       webbrowser.open('https://bunka.nii.ac.jp/special_content/hlink8')
   if event == None:
       break

#サイトリンクにいくつか場所を記載する, [Python]PySimpleGUIで何かを起動するボタンを作る方法, 日本の世界遺産一覧　文化庁
#アウトプットされたものの書かれる場所の用意