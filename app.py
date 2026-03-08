import streamlit as st
import plotly.express as px
import pandas as pd

# ==========================================
# 1. 全局設定與極簡視覺規範 (重裝防禦版)
# ==========================================
st.set_page_config(page_title="QS 象限戰略 | 商業痛點戰略矩陣", layout="wide", page_icon="♟️")

st.markdown("""
    <style>
    .stApp {background-color: #FFFFFF;}
    h1 {color: #003366 !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 900; letter-spacing: -0.5px;}
    h2, h3, h4 {color: #003366 !important; font-weight: 700;}
    p, span, div, label {color: #333333;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    [data-testid="stSidebar"] {background-color: #F8F9FA; border-right: 1px solid #EBEBEB;}
    div[data-testid="metric-container"] {border-left: 4px solid #003366; padding: 10px 15px; background-color: #FFFFFF; border: 1px solid #EEEEEE; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);}
    
    .trust-badge {font-size: 11px; color: #666; text-align: center; margin-top: 5px; margin-bottom: 15px; padding: 8px; background-color: #F0F2F6; border-radius: 4px;}
    .legal-warning {background-color: #F8F9FA; color: #555; padding: 12px 16px; border-left: 4px solid #6C757D; font-size: 12px; margin-bottom: 20px; line-height: 1.6;}
    .methodology-box {background-color: #F4F8FC; border: 1px solid #D6E4F0; padding: 12px 16px; border-radius: 6px; margin-bottom: 20px;}
    .bait-box {background-color: #F4F6F9; border-left: 4px solid #B30000; padding: 16px; margin-bottom: 25px; border-radius: 0 6px 6px 0;}
    .bait-title {color: #B30000; font-weight: 800; font-size: 15px; margin-bottom: 6px;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar)：雙層級路由與動態收銀台
# ==========================================
with st.sidebar:
    st.markdown("<h3>QS 象限戰略</h3>", unsafe_allow_html=True)
    st.caption("By HUACHIAO GROUP 樺蕎顧問團隊")
    st.write("---")
    
    st.markdown("#### 📂 戰略情報板塊")
    market_sector = st.radio(
        "切換產業領域：",
        ["電子支付戰場", "實體與大眾化情報庫"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if market_sector == "電子支付戰場":
        st.markdown("#### 📱 電子支付標的")
        # 👑 實裝 CEO 戰略：將 $1499 終極包拉上第一線當作旗艦選項
        target_platform = st.selectbox(
            "選擇分析標的：",
            (
                "🏆 台灣電支三強 終極包 ($1499)", 
                "LINE Pay ($599)",
                "街口支付 ($599-即將解鎖)", 
                "全支付 ($599-即將解鎖)"
            )
        )
    else:
        st.markdown("#### 🌍 跨界情報標的")
        target_platform = st.selectbox(
            "選擇分析標的：",
            (
                "王品集團 (連鎖餐飲情報) - [運算中]",
                "星巴克/路易莎 (連鎖咖啡情報) - [運算中]",
                "UberEats (外送生活) - [運算中]",
                "Tinder (交友軟體) - [運算中]"
            )
        )
    
    st.write("---")
    
    st.markdown("#### ⚡ 獲取完整決策報告")
    
    # 收銀台邏輯 1：單看 LINE Pay 的人，給他 $599，順便問他要不要升級
    if target_platform == "LINE Pay":
        pricing_tier = st.radio("選擇授權方案：", ["單一戰區分析 ($599)", "升級電支三強 終極包 ($1499)"])
        if "$599" in pricing_tier:
            st.markdown("<h2 style='color: #003366; margin-top: -10px; margin-bottom: 5px;'>$ 599</h2>", unsafe_allow_html=True)
            st.link_button("💳 立即獲取 (LINE Pay 戰術包)", "https://quadrastrategy.gumroad.com/l/epay-line-2026", type="primary", use_container_width=True)
        else:
            st.markdown("<h2 style='color: #B30000; margin-top: -10px; margin-bottom: 5px;'>$ 1499</h2>", unsafe_allow_html=True)
            st.link_button("💳 立即獲取 (電支三強終極包)", "https://quadrastrategy.gumroad.com/l/epay-bundle-2026", type="primary", use_container_width=True)
        st.markdown("<div class='trust-badge'>🔒 國際金流 Gumroad 託管 | 256-bit SSL 加密<br>Apple Pay / 信用卡結帳後 3 秒自動發送</div>", unsafe_allow_html=True)

    # 收銀台邏輯 2：直接點選 1499 旗艦包的人，直接鎖死 $1499 收銀台
    elif target_platform == "🏆 台灣電支三強 終極包 ($1499)":
        st.info("當前標的：電支三強終極防禦包")
        st.markdown("<h2 style='color: #B30000; margin-top: -10px; margin-bottom: 5px;'>$ 1499</h2>", unsafe_allow_html=True)
        st.caption("內含：LINE Pay, 街口, 全支付 三大陣營痛點對標與流失率盲區掃描。")
        st.link_button("💳 立即獲取 (電支三強終極包)", "https://quadrastrategy.gumroad.com/l/epay-bundle-2026", type="primary", use_container_width=True)
        st.markdown("<div class='trust-badge'>🔒 國際金流 Gumroad 託管 | 256-bit SSL 加密<br>Apple Pay / 信用卡結帳後 3 秒自動發送</div>", unsafe_allow_html=True)
    
    else:
        st.warning(f"該產業情報模型建置中。")
        st.button("🔒 尚未開放", disabled=True, use_container_width=True)

    st.write("---")
    st.markdown("**Founders**")
    st.caption("吳樺緯 (Hua-Wei Wu) \n\n吳蕎伊 (Chiao-Yi Wu)")
    st.write("---")
    st.markdown("<p style='font-size: 11px; color: #888; line-height: 1.5;'>© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved.<br>數據合規：本報告所有洞察均來自 QS 象限戰略開源聲量捕捉引擎，全數文本皆經向量化與主題聚合處理，無法回推原始個資。</p>", unsafe_allow_html=True)

# ==========================================
# 3. 主畫面模組化動態載入
# ==========================================

# 模組 A：LINE Pay 基礎版主畫面
if target_platform == "LINE Pay":
    st.markdown("<h1>LINE Pay 2026 Q2 商業痛點戰略矩陣</h1>", unsafe_allow_html=True)
    st.markdown("<div class='legal-warning'><b>⚖️ 智庫合規與抽樣限制聲明：</b> 本矩陣僅代表特定期間內，經 QS 象限戰略演算法於公開網路抽樣之消費者情緒量化結果，不構成對任何品牌或產品之全面性評價與指控。所有洞察僅供企業內部產品改進參考。</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='methodology-box'>
        <b>🔬 QS 象限戰略數據煉丹爐 (Data Pipeline)：</b><br>
        <code style='color:#003366;'>Raw Text -> Text Embedding -> BERTopic -> Sentiment Mapping -> Pain Matrix</code>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='bait-box'>
        <div class='bait-title'>💡 QS 象限戰略獨家洞察解密 (Sample)：</div>
        模型偵測到大量「登入_重新_密碼」等關鍵字落於極度痛點區。驗證了 <b>Day 1 Churn (新手登入流失)</b> 是目前該平台最嚴重的基礎建設漏洞。
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("預估 Day 1 Churn (新手流失率)", "18.5%", "高危險", delta_color="inverse")
    col2.metric("潛在月度營收損耗 (核心流程)", "$ 2.4M NTD", "警戒", delta_color="inverse")
    col3.metric("競品防禦力對標 (vs 街口)", "弱勢", "需優化 [隱匿]", delta_color="inverse")
    st.write("---")

    df_teaser = pd.DataFrame({
        "戰場標籤": ["【解密】基礎流失 (登入)", "戰區 Beta (盲區)", "戰區 Gamma (警戒)", "戰區 Delta (共業)", "戰區 Epsilon (結帳中斷)"],
        "聲量熱度 (討論量)": [68, 41, 52, 61, 44],
        "情緒滿意度": [-0.577, -0.408, -0.805, -0.938, -0.72],
        "商業影響力 (Impact)": [10, 7, 6, 9, 8]
    })

    fig1 = px.scatter(df_teaser, x="情緒滿意度", y="聲量熱度 (討論量)", text="戰場標籤", size="聲量熱度 (討論量)", color="情緒滿意度", color_continuous_scale=["#B30000", "#CCCCCC", "#003366"], title="LINE Pay 服務落點與情緒分析 (越往左越痛)")
    fig1.update_traces(textposition='top center')
    fig1.update_layout(plot_bgcolor='white', paper_bgcolor='white', coloraxis_showscale=False)
    st.plotly_chart(fig1, use_container_width=True)

# 模組 B：$1499 終極包專屬主畫面 (火力展示版)
elif target_platform == "🏆 台灣電支三強 終極包 ($1499)":
    st.markdown("<h1>🏆 台灣電支三強：終極防禦與痛點對標矩陣</h1>", unsafe_allow_html=True)
    st.markdown("<div class='legal-warning'><b>⚖️ 智庫合規與抽樣限制聲明：</b> 本矩陣包含 LINE Pay, 街口支付, 全支付 三大品牌之交叉比對，純屬 NLP 演算法量化結果，不構成企業營運評價。</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='bait-box'>
        <div class='bait-title'>🔥 終極情報預覽 (Cross-Platform Analysis)：</div>
        透過三方矩陣疊加，我們發現<b>「跨境支付生態」</b>與<b>「點數折抵UI」</b>是決定 2026 年用戶跳槽率的兩大絕對關鍵。其中一方已在此戰場出現嚴重失血（情緒分數低於 -0.85）。解鎖報告獲取完整競品弱點地圖。
        </div>
    """, unsafe_allow_html=True)

    # 針對三強設計的高階比較數據版塊
    st.write("### 📊 競品致命弱點交叉掃描 (預覽)")
    col1, col2, col3 = st.columns(3)
    col1.metric("🟢 LINE Pay 最大流失節點", "登入驗證與換機", "已被鎖定", delta_color="inverse")
    col2.metric("🔴 街口支付 最大流失節點", "🔒 解鎖完整報告", "高度隱匿", delta_color="off")
    col3.metric("🔵 全支付 最大流失節點", "🔒 解鎖完整報告", "高度隱匿", delta_color="off")
    st.write("---")
    
    st.info("💡 完整版包含：三方痛點座標全覆蓋疊加圖、跨平台 UI 體驗落差評估、行銷資源投放優先順序 (Impact x Effort Matrix) 等 30 頁高階分析。")

# 模組 C：其他建置中平台
else:
    st.markdown(f"<h1>{target_platform}</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("此產業模組的數據正在進行 NLP 語意重構與底層運算中。為確保高階主管決策品質，尚未開放預覽。")
