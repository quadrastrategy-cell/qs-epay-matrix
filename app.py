import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# ==========================================
# 1. 全局設定與頂級智庫視覺規範 (黑金曜石 終極版)
# ==========================================
st.set_page_config(page_title="QS 象限戰略 | 頂級商業情報雷達", layout="wide", page_icon="♟️")

# 注入黑卡級別 CSS - 包含所有選單防護與浮動視窗修正
st.markdown("""
    <style>
    /* 核心背景與字體 */
    .stApp {background-color: #0A0A0A;}
    h1, h2, h3 {color: #BF953F !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 900; letter-spacing: 1px;}
    h4, p, span, div, label, li {color: #EBEBEB;}
    
    /* 隱藏系統預設選單 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 🛡️ 側邊欄與下拉選單的終極防護 */
    [data-testid="stSidebar"] {background-color: #121212; border-right: 1px solid #333333;}
    
    /* 針對選單外框與未展開的文字 */
    div[data-baseweb="select"] > div {background-color: #262626 !important; color: #BF953F !important; border-color: #333333 !important;}
    div[data-testid="stSelectbox"] label {color: #EBEBEB !important; font-weight: 700;}
    
    /* 🛡️ 浮動選單 (Popover) 鬼剃頭修正：強制黑底金字 */
    div[data-baseweb="popover"] > div,
    ul[role="listbox"] {
        background-color: #1A1A1A !important;
    }
    ul[role="listbox"] li {
        color: #BF953F !important;
        background-color: #1A1A1A !important;
    }
    ul[role="listbox"] li:hover {
        background-color: #333333 !important;
        color: #FFFFFF !important;
    }
    
    /* 數據面板 (Metric) 黑金化 */
    div[data-testid="metric-container"] {border-left: 4px solid #BF953F; padding: 10px 15px; background-color: #1A1A1A; border-radius: 6px; box-shadow: 0 4px 6px rgba(0,0,0,0.5);}
    div[data-testid="stMetricValue"] {color: #FFFFFF !important;}
    
    /* 信任標章與合規聲明 */
    .trust-badge {font-size: 11px; color: #888; text-align: center; margin-top: 5px; margin-bottom: 15px; padding: 8px; background-color: #1A1A1A; border-radius: 4px; border: 1px solid #333;}
    .legal-warning {background-color: #1A1A1A; color: #888; padding: 12px 16px; border-left: 4px solid #555; font-size: 12px; margin-bottom: 20px; line-height: 1.6;}
    
    /* 戰略誘餌區塊 (Bait Box) */
    .bait-box {background-color: #1F1505; border-left: 4px solid #BF953F; padding: 16px; margin-bottom: 25px; border-radius: 0 6px 6px 0;}
    .bait-title {color: #BF953F; font-weight: 800; font-size: 15px; margin-bottom: 6px;}
    
    /* ⚠️ 坑人防呆提示 */
    .discount-warning {font-size: 12px; color: #BF953F; background-color: #1A1A1A; padding: 8px; border-radius: 4px; border: 1px solid #BF953F; margin-bottom: 10px; text-align: center; font-weight: 700;}
    
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar)：全線解鎖與早鳥直通收銀台
# ==========================================
with st.sidebar:
    st.markdown("<h3>QS 象限戰略</h3>", unsafe_allow_html=True)
    st.caption("HUACHIAO GROUP 樺蕎顧問團隊")
    st.write("---")
    
    st.markdown("#### 📂 戰略情報板塊")
    market_sector = st.radio(
        "切換產業領域：",
        ["電子支付戰場", "實體與大眾化情報庫"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if market_sector == "電子支付戰場":
        st.markdown("#### 📱 電子支付標的")
        # 👑 三大陣營全數解鎖，1499 穩坐旗艦位
        target_platform = st.selectbox(
            "選擇分析標的 (2026 Q2)：",
            (
                "🏆 台灣電支三強 終極包 ($1499)", 
                "🟢 LINE Pay 戰術包 ($599)",
                "🔴 街口支付 戰術包 ($599)", 
                "🔵 全支付 戰術包 ($599)"
            )
        )
    else:
        st.markdown("#### 🌍 跨界情報標的")
        target_platform = st.selectbox(
            "選擇分析標的：",
            (
                "王品集團 (連鎖餐飲情報) - [運算中]",
                "星巴克/路易莎 (連鎖咖啡情報) - [運算中]",
                "UberEats (外送生活) - [運算中]"
            )
        )
    
    st.write("---")
    
    # 💰 動態收銀台 
    st.markdown("#### ⚡ 獲取完整決策報告")
    st.markdown("<div class='discount-warning'>⚠️ 早鳥 8 折僅限前 10 名。點擊下方按鈕後，請務必在結帳頁面確認最終顯示金額為 8 折價再付款。</div>", unsafe_allow_html=True)
    
    # 判斷選擇的平台，給予對應的 Gumroad 結帳連結
    if target_platform == "🏆 台灣電支三強 終極包 ($1499)":
        st.info("當前標的：電支三強宏觀對標矩陣 (全 9 頁)")
        st.markdown("<h2 style='color: #BF953F; margin-top: -10px; margin-bottom: 5px;'>$ 1499</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取終極包 (前 10 名自動享 8 折)", "https://quadrastrategy.gumroad.com/l/epay-bundle-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
        
    elif target_platform == "🟢 LINE Pay 戰術包 ($599)":
        st.info("當前標的：LINE 生態系流失斷點報告 (全 10 頁)")
        st.markdown("<h2 style='color: #BF953F; margin-top: -10px; margin-bottom: 5px;'>$ 599</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 LINE Pay 戰術包 (自動帶入 8 折)", "https://quadrastrategy.gumroad.com/l/epay-line-2026Q2/QS2026EARLY", type="primary", use_container_width=True)

    elif target_platform == "🔴 街口支付 戰術包 ($599)":
        st.info("當前標的：街口支付客訴迴圈報告 (全 10 頁)")
        st.markdown("<h2 style='color: #BF953F; margin-top: -10px; margin-bottom: 5px;'>$ 599</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 街口支付 戰術包 (自動帶入 8 折)", "https://quadrastrategy.gumroad.com/l/epay-jko-2026Q2/QS2026EARLY", type="primary", use_container_width=True)

    elif target_platform == "🔵 全支付 戰術包 ($599)":
        st.info("當前標的：全支付體驗落差報告 (全 10 頁)")
        st.markdown("<h2 style='color: #BF953F; margin-top: -10px; margin-bottom: 5px;'>$ 599</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 全支付 戰術包 (自動帶入 8 折)", "https://quadrastrategy.gumroad.com/l/epay-px-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
    
    else:
        st.warning(f"該產業情報模型建置中。")
        st.button("🔒 尚未開放", disabled=True, use_container_width=True)

    st.markdown("<div class='trust-badge'>🔒 國際金流 Gumroad 託管 | 支援 Google Pay / Apple Pay / 國際信用卡<br>結帳後 3 秒自動發送企業級浮水印 PDF 至信箱</div>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("<p style='font-size: 11px; color: #666; line-height: 1.5;'>© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved.</p>", unsafe_allow_html=True)

# ==========================================
# 3. 主畫面動態載入 (恐懼行銷火力展示)
# ==========================================

st.markdown("<div class='legal-warning'><b>⚖️ 智庫合規與抽樣限制聲明：</b> 本矩陣為 QS 象限戰略演算法於公開網路抽樣之消費者情緒量化結果，全數文本皆經向量化與主題聚合處理，無法回推原始個資。拒絕主觀通靈，只用底層數據說話。</div>", unsafe_allow_html=True)

# 🏆 旗艦：$1499 終極包
if target_platform == "🏆 台灣電支三強 終極包 ($1499)":
    st.markdown("<h1>🏆 台灣電支三強：終極防禦與痛點對標矩陣</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='bait-box'>
        <div class='bait-title'>🔥 終極情報預覽 (Cross-Platform Analysis)：</div>
        透過三方矩陣疊加，我們發現<b>「跨境支付生態 API 延遲」</b>與<b>「逆向金流退款黑箱」</b>是決定 2026 年高淨值用戶跳槽率的兩大絕對關鍵。其中一方已在此戰場出現嚴重失血。解鎖全份 9 頁戰略報告，獲取完整競品弱點地圖。
        </div>
    """, unsafe_allow_html=True)

    st.write("### 📊 競品致命弱點交叉掃描 (預覽)")
    col1, col2, col3 = st.columns(3)
    col1.metric("🟢 LINE Pay 最大流失節點", "登入與 3D 驗證斷流", "已被鎖定", delta_color="inverse")
    col2.metric("🔴 街口支付 最大流失節點", "🔒 解鎖報告獲取座標", "高度隱匿", delta_color="off")
    col3.metric("🔵 全支付 最大流失節點", "🔒 解鎖報告獲取座標", "高度隱匿", delta_color="off")
    st.write("---")

# 模組 B：各別 599 戰術包 (專業矩陣圖表)
elif "戰術包" in target_platform:
    brand_name = target_platform.split(" ")[1] 
    st.markdown(f"<h1>{brand_name} 2026 Q2 商業痛點戰略矩陣</h1>", unsafe_allow_html=True)
    
    bait_text = ""
    # 根據不同品牌編寫專屬專業 Placeholder 數據
    if brand_name == "LINE":
        bait_text = "模型偵測到大量「登入_重新_密碼」落於極度痛點區。驗證了 <b>Onboarding 死亡漏斗</b> 是目前新戶首刷 GMV 歸零的核心死因。"
        labels = ["【解密】Onboarding死亡區", "戰區 Beta ( blindspot )", "戰區 Gamma (On-Hold)", "戰區 Delta (競品共業)", "戰區 Epsilon (延遲阻力)"]
        討論量 = [68, 41, 52, 61, 44]
        情緒 = [-0.577, -0.408, -0.805, -0.938, -0.72]
        
    elif brand_name == "街口支付":
        bait_text = "模型偵測出「實體店與平台責任互踢」的強烈負面情緒。揭露了引發消保客訴暴增的 <b>逆向金流黑箱</b> 底層邏輯。"
        labels = ["【解密】退款黑箱區", "戰區 J1 (卡頓流失)", "戰區 J2 (警戒點)", "戰區 J3 (競品共業)", "戰區 J4 (KYC流程死鎖)"]
        討論量 = [55, 71, 44, 61, 59]
        情緒 = [-0.852, -0.312, -0.661, -0.938, -0.78]
        
    elif brand_name == "全支付":
        bait_text = "數據顯示高齡用戶在「換機與換門號」情境下遭遇極高數位門檻。這是導致線下門市癱瘓與 <b>資產凍結客訴</b> 的致命斷點。"
        labels = ["【解密】身份驗證死亡區", "戰區 P1 (換機阻力)", "戰區 P2 (跨境Timeout)", "戰區 P3 (競品共業)", "戰區 P4 (生態系整合點)"]
        討論量 = [49, 39, 66, 61, 51]
        情緒 = [-0.915, -0.622, -0.811, -0.938, -0.55]

    st.markdown(f"""
        <div class='bait-box'>
        <div class='bait-title'>💡 QS 象限戰略獨家洞察解密 (Sample)：</div>
        {bait_text}
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("預估核心流程中斷率", "高危險", "急需優化", delta_color="inverse")
    col2.metric("潛在月度營收損耗", "警戒等級", "持續失血", delta_color="inverse")
    col3.metric("底層優化座標 (Sprint)", "🔒 解鎖獲取", "10頁濃縮", delta_color="off")
    st.write("---")

    df_pro = pd.DataFrame({
        "戰場標籤": labels,
        "聲量熱度 (討論量)": 討論量,
        "情緒滿意度": 情緒,
        "商業影響力 (Impact)": np.random.randint(6, 11, 5) 
    })

    fig1 = px.scatter(df_pro, x="情緒滿意度", y="聲量熱度 (討論量)", text="戰場標籤", size="聲量熱度 (討論量)", color="情緒滿意度", color_continuous_scale=["#B30000", "#BF953F", "#FFFFFF"], title=f"{brand_name} 服務落點與情緒分析 (越往左越痛)")
    fig1.update_traces(textposition='top center')
    
    fig1.update_layout(
        template="plotly_dark", 
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)', 
        coloraxis_showscale=False,
        yaxis=dict(title=dict(standoff=15), ticksuffix=" ", showgrid=False),
        xaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig1, use_container_width=True)

# 模組 C：建置中
else:
    st.markdown(f"<h1>{target_platform}</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("此產業模組的數據正在進行 NLP 語意重構與底層運算中。為確保高階主管決策品質，尚未開放預覽。")
