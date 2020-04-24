# kirara_scraper
![result.png](https://github.com/Seigenkousya/kirara_scraper/blob/master/result/max_result.png)

きららの掲載順を取得し、可視化するスクリプト  
現在はきららMAXとキャラットに対応しているスクリプトを用意している。  
今後残りのきらら本誌、ミラク、フォワードについても対応する予定。（開発次第更新）  

# usage
1. mid_get.pyでスクレイピングに必要なデータを取得
1. 任意のスクリプトでデータを取得し、
1. 収集したデータをもとにグラフ化

## mid_get.py
スクレイピングに必要なURLのIDを取得するスクリプト。  
urlのMAXの部分は適宜書き換え。  
配列で出力されるのでコピーして各雑誌のスクリプトのmid_listに貼り付け。  

## max_scrape_2020.py
最新版。  
MAXとついているがmid_get.pyで取得するデータを変えれば他のものにも代用可能。  
旧版に加え以下の機能を追加。  

- 同じことを何回も書いている部分があるのでオブジェクト化
- 掲載順が下がっているのかセンターカラーの定位置なのかわからなかったのでセンターカラーのときは印をつけた
- 今までfontタグを使って掲載順を判断していたが余計な文章が増えていたので```<font color="8000FF">```で囲われた部分だけを採用するようにした

詳しい概要は以下のリンクを参照。  
[まんがタイムきららMAXの掲載順を可視化・分析する2 - 正弦工社](https://seigenkousya.github.io/post/kirara_order_2020/)  

## carat_scrape_2020.py
キャラット版。  
MAXで使用したスクリプトをそのまま流用できなかったため書き直し。  
同じくmidについてはmid_get.pyを使って取得する。  

詳しい概要は以下のリンクを参照。  
[まんがタイムきららキャラットの掲載順を可視化・分析する2020   - 正弦工社](https://seigenkousya.github.io/post/carat_order_2020/)  

## max_scrape_2019.py
旧版。  
詳しい概要は以下のリンクを参照。  
[どうびじゅの連載終了が告知され心と胃を痛めているきららmax読者のためのスクレイピングを使ったデータ収集と考察のススメ - Qiita](https://qiita.com/Seigenkousya/items/8f0ffbd2c34a8e8535e2)

# contact
正弦工社【セイゲンコウシャ】  
きららと百合のための研究・評論・技術開発を行う謎の団体。
  
homopage:[https://seigenkousya.github.io/](https://seigenkousya.github.io/)  
twitter:[https://twitter.com/Seigenkousya](https://twitter.com/Seigenkousya)  


