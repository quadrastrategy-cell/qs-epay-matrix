import streamlit as st

# ==========================================
# 1. 頁面基礎設定 (外商智庫級排版)
# ==========================================
st.set_page_config(
    page_title="QS 象限戰略 | 台灣電子支付生態戰",
    page_icon="📊",
    layout="centered"
)

# 自訂按鈕顏色與字體樣式 (深海軍藍)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #111827;
        color: white;
        border: 1px solid white;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar) 導覽選單
# ==========================================
st.sidebar.title("📊 QS 象限戰略")
st.sidebar.caption("By HUACHIAO GROUP 樺蕎顧問團隊")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "📂 切換分析戰場：",
    ["👑 三強爭霸終極大包裝", "🟢 LINE Pay 降阻策略", "🔴 街口支付 降阻策略", "🔵 全支付 降阻策略"]
)
st.sidebar.markdown("---")
st.sidebar.info("💡 提示：本系統基於 2024-2026 跨平台真實數據，經 NLP 語意重構萃取。")

# ==========================================
# 3. 各頁面內容與 Gumroad 結帳連結
# ==========================================

if page == "👑 三強爭霸終極大包裝":
    st.title("🔥 2026 台灣電子支付生態戰")
    st.subheader("LINE Pay vs 街口 vs 全支付｜10 大流失矩陣總匯")
    st.markdown("""
    **高階經理人與 PM 專屬的競品決策智庫。**
    
    拒絕無效市調與公關稿，我們運用 NLP 技術探勘海量真實客訴，直接為您建構出台灣三大電子支付的「QS 戰略矩陣」。
    您將一次性獲得三家巨頭的致命流失斷點、生態系綁卡衝突，以及具備量化數據支撐的 **Impact × Effort 開發落地路徑**。
    
    * 🎯 **包含：** LINE Pay、街口支付、全支付 完整分析報告。
    * ⏱️ **效益：** 為您省下至少 100 小時的爬蟲與研究時間，明天直接提案。
    """)
    st.markdown("### 💎 企業級戰略大包裝 (Bundle)")
    st.markdown("原價 NT$ 1,797 ➡️ **終極決策價 NT$ 1,499**")
    
    # Gumroad 結帳按鈕 (新開分頁)
    if st.button("🛒 立即獲取【三強爭霸終極大包裝】"):
        st.write('''<script>window.open("https://quadrastrategy.gumroad.com/l/epay-bundle-2026", "_blank");</script>''', unsafe_allow_html=True)

elif page == "🟢 LINE Pay 降阻策略":
    st.title("🟢 LINE Pay 痛點矩陣與降阻策略")
    st.markdown("""
    **揪出台灣市佔率最高支付工具的隱性流失斷點。**
    
    大家都說 LINE Pay 生態圈很強，但數據顯示，其「核心流失風暴區」正悄悄侵蝕用戶耐心。本報告帶您破解介面廣告干擾與綁卡驗證失效背後的真實數據。
    """)
    st.markdown("### 售價：NT$ 599")
    if st.button("🛒 獲取 LINE Pay 專屬報告"):
        st.write('''<script>window.open("https://quadrastrategy.gumroad.com/l/epay-line-2026", "_blank");</script>''', unsafe_allow_html=True)

elif page == "🔴 街口支付 降阻策略":
    st.title("🔴 街口支付 痛點矩陣與降阻策略")
    st.markdown("""
    **深度解析老牌支付工具的 UX 摩擦與高頻客訴。**
    
    當提領手續費與介面複雜度成為常態性抱怨，PM 該如何決定開發優先級？本報告透過二維矩陣，為您標定街口支付的致命盲區與長線優化路徑。
    """)
    st.markdown("### 售價：NT$ 599")
    if st.button("🛒 獲取 街口支付 專屬報告"):
        st.write('''<script>window.open("https://quadrastrategy.gumroad.com/l/epay-jko-2026", "_blank");</script>''', unsafe_allow_html=True)

elif page == "🔵 全支付 降阻策略":
    st.title("🔵 全支付 痛點矩陣與降阻策略")
    st.markdown("""
    **從婆媽市場到全齡客群，拆解綁卡與點數折抵爭議。**
    
    全支付靠著強大的通路優勢快速崛起，但在高頻操作中，其 EKYC 認證與點數生態卻隱藏著巨大的體驗摩擦。本報告將為您提供針對性的降阻解法。
    """)
    st.markdown("### 售價：NT$ 599")
    if st.button("🛒 獲取 全支付 專屬報告"):
        st.write('''<script>window.open("https://quadrastrategy.gumroad.com/l/epay-px-2026", "_blank");</script>''', unsafe_allow_html=True)

# ==========================================
# 4. 頁尾版權宣告
# ==========================================
st.markdown("---")
st.caption("© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved. | 數據合規：全數樣本均經語意重構與合成處理。")
