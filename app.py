import streamlit as st

# ==========================================
# 1. 頁面基礎設定 (外商智庫級排版)
# ==========================================
st.set_page_config(
    page_title="QS 象限戰略 | 台灣電子支付生態戰",
    page_icon="📊",
    layout="centered"
)
# ==========================================
# 💡 KPMG 級別頂級管顧視覺化設定 (CSS 注入)
# ==========================================
st.markdown("""
    <style>
    /* 1. 全局字體與背景微調 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* 2. KPMG 權威深藍標題 */
    h1, h2, h3 {
        color: #00338D !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    
    /* 3. 銳利化跳轉按鈕 (st.link_button) */
    .stLinkButton > a {
        background-color: #00338D !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 2px !important; /* 管顧菁英風的微銳角 */
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        text-align: center;
        display: block;
    }
    
    /* 按鈕懸停效果 (Hover) 變成亮藍色 */
    .stLinkButton > a:hover {
        background-color: #0091DA !important;
        box-shadow: 0 4px 6px rgba(0, 51, 141, 0.2);
    }
    
    /* 4. 側邊欄高質感底色 */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA;
        border-right: 1px solid #EBEBEB;
    }
    
    /* 側邊欄內的字體顏色 */
    [data-testid="stSidebar"] h1 {
        color: #00338D !important;
    }
    </style>
""", unsafe_allow_html=True)
# ==========================================
# 2. 側邊欄 (Sidebar) - 資料夾導覽與創辦人署名
# ==========================================
st.sidebar.title("📊 QS 象限戰略")
st.sidebar.caption("By HUACHIAO GROUP 樺蕎顧問團隊")
st.sidebar.markdown("---")

# 📂 第一個資料夾：電子支付戰場 (預設展開)
with st.sidebar.expander("📂 電子支付戰場 (E-Pay)", expanded=True):
    page = st.radio(
        "選擇戰略報告：",
        ["👑 三強爭霸終極大包裝", "🟢 LINE Pay 降阻策略", "🔴 街口支付 降阻策略", "🔵 全支付 降阻策略"],
        label_visibility="collapsed"
    )

# 📂 第二個資料夾：純網銀戰場 (預設收合，未來擴充用)
with st.sidebar.expander("📂 純網銀戰場 (即將推出)", expanded=False):
    st.info("即將釋出：LINE Bank 痛點分析與突圍戰略")

st.sidebar.markdown("---")

# 👑 創立人署名 (防禦智財權與建立權威)
st.sidebar.markdown("**Founders**")
st.sidebar.caption("吳樺緯 (Hua-Wei Wu) \n\n 吳蕎伊 (Chiao-Yi Wu)")

# ==========================================
# 3. 各頁面內容與 Gumroad 安全跳轉按鈕 (st.link_button)
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
    
    # 使用安全的按鈕跳轉機制，並加粗強調
    st.link_button("🛒 立即獲取【三強爭霸終極大包裝】", "https://quadrastrategy.gumroad.com/l/epay-bundle-2026", type="primary")

elif page == "🟢 LINE Pay 降阻策略":
    st.title("🟢 LINE Pay 痛點矩陣與降阻策略")
    st.markdown("揪出台灣市佔率最高支付工具的隱性流失斷點。大家都說 LINE Pay 生態圈很強，但數據顯示，其「核心流失風暴區」正悄悄侵蝕用戶耐心。")
    st.markdown("### 售價：NT$ 599")
    st.link_button("🛒 獲取 LINE Pay 專屬報告", "https://quadrastrategy.gumroad.com/l/epay-line-2026")

elif page == "🔴 街口支付 降阻策略":
    st.title("🔴 街口支付 痛點矩陣與降阻策略")
    st.markdown("深度解析老牌支付工具的 UX 摩擦與高頻客訴。當提領手續費與介面複雜度成為常態性抱怨，PM 該如何決定開發優先級？")
    st.markdown("### 售價：NT$ 599")
    st.link_button("🛒 獲取 街口支付 專屬報告", "https://quadrastrategy.gumroad.com/l/epay-jko-2026")

elif page == "🔵 全支付 降阻策略":
    st.title("🔵 全支付 痛點矩陣與降阻策略")
    st.markdown("從婆媽市場到全齡客群，拆解綁卡與點數折抵爭議。全支付靠著強大的通路優勢快速崛起，但在高頻操作中卻隱藏著巨大的體驗摩擦。")
    st.markdown("### 售價：NT$ 599")
    st.link_button("🛒 獲取 全支付 專屬報告", "https://quadrastrategy.gumroad.com/l/epay-px-2026")

# ==========================================
# 4. 頁尾版權宣告
# ==========================================
st.markdown("---")
st.caption("© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved. | 數據合規：全數樣本均經語意重構與合成處理。")
