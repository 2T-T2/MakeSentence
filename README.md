# MarcovChain_SentenceMaker

# 注意事項！
wakati.vbsは、MicroSoft Wordがインストールされている、Windows環境でのみ動作します。

# 使い方
## 取りあえず文章を生成してみる
1. 比較的長いテキストファイルを用意する。
1. wakaigaki/wakati.vbsのinputFilePathに、1で用意したテキストファイルのパスを入力し、実行する。
1. 下記のようなプログラムをMarcov.py同フォルダに作成する。

      <code>
      
            from Marcov import marcov
            import os

            marcov = marcov()
            marcov.loadCsv(os.path.dirname(__file__) + r"\wakatigaki\after.csv")
            print(marcov.makeSentence())
            
      </code>
      
1. 3で作成したファイルを実行する。→コマンドプロンプトに生成された文章が表示される。

## 各メソッドの説明

      
            from Marcov import marcov

            # インスタンスの作成
            marcov = marcov()
            
            # 文節ごとに区切ったCSVファイルを読み込む
            marcov.loadCsv(入力するcsvファイルパス)
            
            # 読み込まれたデータをjsonファイルとして保存
            marcov.saveDic(出力するjsonファイルパス)
            
            # 上記メソッドで出力した形式のjsonファイルを読み込む
            marcov.loadDic(入力するjsonファイルパス)
            
            # 読み込んだファイルを元に文章を生成する
            print(marcov.makeSentence())
            
            # 始まりの語を指定して文章を生成する
            print(marcov.makeSentence("first Word"))
            

