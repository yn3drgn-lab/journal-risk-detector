import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

st.title("不正経理パターン検知アプリ（デモ）")

uploaded_file = st.file_uploader("仕訳データcsvをアップロードしてください", type="csv")

def calc_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    score = 0

    #1.　キリのいい金額（1万円単位）
    flag_round_amount = (df["amount"] % 10000 == 0)
    score += flag_round_amount.astype(int)

    #2.  休日仕訳（日曜・土曜）
    dates = pd.to_datetime(df["date"])
    flag_weekend = dates.dt.weekday >= 5
    score += flag_weekend.astype(int)

    #3. 要注意ワード
    suspicious_words = ["雑費","調整","一時","仮","テスト"]
    memo = df["memo"].fillna("").astype(str)
    flag_memo = memo.apply(lambda x: any(w in x for w in suspicious_words))
    score += flag_memo.astype(int)

    df["risk_score"] = score
    df["flag_round_amount"] = flag_round_amount
    df["flag_weekend"] = flag_weekend
    df["flag_memo"] = flag_memo

    return df

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="cp932")
    df_scored = calc_risk_score(df)

    st.subheader("サマリ")
    st.write(f"総件数: {len(df_scored)}件")
    st.write(f"リスクスコア1以上: {(df_scored['risk_score'] >= 1).sum()}件")
    st.write(f"リスクスコア2以上: {(df_scored['risk_score'] >= 2).sum()}件")

    threshold = st.slider("表示するリスクスコアの下限",0,5,1)
    st.subheader(f"リスクスコア{threshold}点以上の仕訳")
    st.dataframe(df_scored[df_scored["risk_score"] >= threshold].sort_values("risk_score", ascending=False))
    



    