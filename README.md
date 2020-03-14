# kirara_scraper
![result.png](https://github.com/Seigenkousya/kirara_scraper/blob/master/result/result.png)

きららの掲載順を取得し、可視化するスクリプト  
現在はきららMAXのスクリプトを例に置いている。（書き換えることで本誌やキャラット、フォワード等にも対応可能）  
今後すべての雑誌分のスクリプトを用意する予定。（書き換え次第更新）  

# usage
1. mid_get.pyでスクレイピングに必要なデータを取得
1. max_scrape_2020.pyでデータを取得し、
1. 収集したデータをもとにグラフ化

## mid_get.py
スクレイピングに必要なURLのIDを取得するスクリプト。  
urlのMAXの部分は適宜書き換え。  
配列で出力されるのでコピーしてmax_scrape_2020.pyのmid_listに貼り付け。  

## max_scrape_2020.py
最新版。  
MAXとついているがmid_get.pyで取得するデータを変えれば他のものにも代用可能。  
旧版に加え以下の機能を追加。  

- 同じことを何回も書いている部分があるのでオブジェクト化
- 掲載順が下がっているのかセンターカラーの定位置なのかわからなかったのでセンターカラーのときは印をつけた
- 今までfontタグを使って掲載順を判断していたが余計な文章が増えていたので```<font color="8000FF">```で囲われた部分だけを採用するようにした

詳しい概要は以下のリンクを参照。  
[まんがタイムきららMAXの掲載順を可視化・分析する2 // 正弦工社](https://seigenkousya.github.io/post/kirara_order_2020/)  

## max_scrape.py
旧版。  
詳しい概要は以下のリンクを参照。  
[どうびじゅの連載終了が告知され心と胃を痛めているきららmax読者のためのスクレイピングを使ったデータ収集と考察のススメ - Qiita](https://qiita.com/Seigenkousya/items/8f0ffbd2c34a8e8535e2)




