![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

# 🕵️不正経理パターン検知アプリ（Demo）

## 📌　概要
仕訳データをアップロードするだけで、
不正・誤りの可能性がある仕訳を自動で抽出するデモアプリです。

国税局での調査経験をもとに、
現場でよく見られる「怪しいパターン」を
ルール化しています。

--- 
## 🎯　できること
-　CSVファイルのアップロード
-　不正リスクのスコアリング
-　要確認仕訳の一覧表示
-　リスクスコアによる優先順位付け

## 🛠　使用技術
- Python
- pandas
- Streamlit

## 🚀　使い方
pip install -r requirements.txt
streamlit run app.py

## 📂  データについて
本プロジェクトで使用しているデータは、
すべて動作確認用のダミーデータです。

## 🔮  今後の改善予定
-  機械学習による異常検知
-　レポート出力機能

## 📜  ライセンス
MIT Licence
