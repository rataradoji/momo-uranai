import streamlit as st
import random

# サインの名前の2次元リスト
sign_names = [
    ["チーム", "宝結び", "湖の魚", "王の椅子", "勲章", "本"],
    ["扉", "焚火", "消火", "荒野", "猛獣", "閃光"],
    ["師匠", "蜃気楼", "大河", "草の芽", "嵐", "凪"],
    ["宝の箱", "たくらみ", "宝石", "塔", "砂の山", "山寺"],
    ["突風", "剣", "霧", "スパイ", "疾走", "飛翔"],
    ["芸術", "太陽", "月", "大地", "星", "青空"]
]

# キーワードの2次元リスト
keywords = [
    ["協力", "予見", "環境", "成就", "名誉", "知恵"],
    ["決断", "熱意", "冷え", "枯渇", "挑戦", "希望"],
    ["善行", "幻想", "浄化", "成長", "混乱", "救済"],
    ["発見", "誘惑", "豊かさ", "安定", "崩壊", "着実"],
    ["勢い", "勝利", "空虚", "障害", "名誉", "安心"],
    ["美、知識", "光明", "感性", "保護", "革命", "解放"]
]

# アプリのタイトルと説明
st.title("MOMO占い")
st.markdown("ボタンを押して、今日の運勢を占おう！")

# ボタンクリックで占い実行
if st.button("MOMO占いスタート"):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sign = sign_names[die1 - 1][die2 - 1]
    keyword = keywords[die1 - 1][die2 - 1]
    # カード風デザインで結果表示
    st.markdown(f"""
    <div style='border: 2px solid #007bff; padding: 15px; border-radius: 10px; background-color: #f8f9fa;'>
        <h3>占い結果</h3>
        <p><b>サイコロの出目</b>: {die1} と {die2}</p>
        <p><b>サイン</b>: {sign}</p>
        <p><b>キーワード</b>: {keyword}</p>
    </div>
    """, unsafe_allow_html=True)