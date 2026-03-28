import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# ==========================================
# 1. 全局設定與頂級智庫視覺規範 (行動端優先瀑布流版)
# ==========================================
st.set_page_config(page_title="QS 象限戰略 | 頂級商業情報雷達", layout="centered", page_icon="♟️")

st.markdown("""
    <style>
    /* 核心背景與字體 */
    .stApp {background-color: #0A0A0A;}
    h1, h2, h3 {color: #BF953F !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 900; letter-spacing: 1px;}
    h4, p, span, div, label, li {color: #EBEBEB;}
    
    /* 隱藏系統預設選單與多餘空白 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    
    /* 針對選單外框與未展開的文字 */
    div[data-baseweb="select"] > div {background-color: #1A1A1A !important; color: #BF953F !important; border: 1px solid #BF953F !important;}
    div[data-testid="stSelectbox"] label {color: #BF953F !important; font-weight: 800; font-size: 18px !important; margin-bottom: 5px;}
    
    /* 強制貫穿所有浮動選單 (Popover/Menu) 的底層標籤 */
    div[data-baseweb="popover"], div[data-baseweb="popover"] > div, div[data-baseweb="menu"], ul[role="listbox"], li[role="option"] {
        background-color: #1A1A1A !important; color: #BF953F !important;
    }
    li[role="option"]:hover, li[role="option"]:focus, li[aria-selected="true"] {
        background-color: #333333 !important; color: #FFFFFF !important;
    }
    
    /* 數據面板 (Metric) 黑金化 */
    div[data-testid="metric-container"] {border-left: 4px solid #BF953F; padding: 15px; background-color: #121212; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.8); margin-bottom: 10px;}
    div[data-testid="stMetricValue"] {color: #FFFFFF !important; font-size: 24px !important;}
    
    /* 信任標章與合規聲明 */
    .trust-badge {font-size: 12px; color: #888; text-align: center; margin-top: 20px; padding: 15px; background-color: #121212; border-radius: 6px; border: 1px solid #333;}
    .legal-warning {background-color: #121212; color: #888; padding: 12px 16px; border-left: 4px solid #555; font-size: 12px; margin-bottom: 25px; line-height: 1.6;}
    
    /* 戰略誘餌區塊 (Bait Box) */
    .bait-box {background-color: #1F1505; border-left: 4px solid #BF953F; padding: 18px; margin-bottom: 25px; border-radius: 0 6px 6px 0;}
    .bait-title {color: #BF953F; font-weight: 800; font-size: 16px; margin-bottom: 8px;}
    
    /* ⚠️ 坑人防呆提示 */
    .discount-warning {font-size: 13px; color: #BF953F; background-color: #1A1A1A; padding: 10px; border-radius: 6px; border: 1px dashed #BF953F; margin-bottom: 15px; text-align: center; font-weight: 700;}
    
    /* 結帳區塊框 */
    .checkout-box {background-color: #121212; padding: 25px; border-radius: 10px; border: 1px solid #333; margin-top: 30px;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 瀑布流主畫面設計 (無隱藏選單，一滑到底)
# ==========================================

# 頂部 LOGO 與標題
st.markdown("<h1 style='text-align: center;'>QS 象限戰略 | 頂級商業情報雷達</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top:-15px; margin-bottom:30px;'>By HUACHIAO GROUP 樺蕎顧問團隊</p>", unsafe_allow_html=True)

st.markdown("<div class='legal-warning'><b>⚖️ 智庫合規與抽樣限制聲明：</b> 本矩陣為 QS 象限戰略演算法於公開網路抽樣之消費者情緒量化結果，全數文本皆經向量化與主題聚合處理，無法回推原始個資。拒絕主觀通靈，只用底層數據說話。</div>", unsafe_allow_html=True)

# 核心選擇器：放在畫面正中央，手機用戶絕對不會錯過
target_platform = st.selectbox(
    "👇 請選擇 2026 Q2 欲解析之戰場標的：",
    ("🏆 台灣電支三強 終極對標包 ($1499)", "🟢 LINE Pay 戰術包 ($599)", "🔴 街口支付 戰術包 ($599)", "🔵 全支付 戰術包 ($599)", "☕ 星巴克/路易莎情報 (運算中...)", "🍔 王品集團情報 (運算中...)")
)

st.write("---")

# ==========================================
# 3. 情報預覽與圖表區 (根據選擇動態替換)
# ==========================================

if target_platform == "🏆 台灣電支三強 終極對標包 ($1499)":
    st.markdown("<h2>🏆 台灣電支三強：終極防禦與痛點對標矩陣</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='bait-box'>
        <div class='bait-title'>🔥 終極情報預覽 (Cross-Platform Analysis)：</div>
        透過三方矩陣疊加，我們發現<b>「跨境支付生態 API 延遲」</b>與<b>「逆向金流退款黑箱」</b>是決定 2026 年高淨值用戶跳槽率的兩大絕對關鍵。其中一方已在此戰場出現嚴重失血。解鎖全份 9 頁戰略報告，獲取完整競品弱點地圖。
        </div>
    """, unsafe_allow_html=True)

    st.write("### 📊 競品致命弱點交叉掃描 (預覽)")
    col1, col2, col3 = st.columns(3)
    col1.metric("🟢 LINE Pay 最大流失節點", "登入與 3D 驗證", "已被鎖定", delta_color="inverse")
    col2.metric("🔴 街口支付 最大流失節點", "🔒 解鎖報告獲取", "高度隱匿", delta_color="off")
    col3.metric("🔵 全支付 最大流失節點", "🔒 解鎖報告獲取", "高度隱匿", delta_color="off")

elif "戰術包" in target_platform:
    brand_name = target_platform.split(" ")[1] 
    st.markdown(f"<h2>{brand_name} 2026 Q2 商業痛點戰略矩陣</h2>", unsafe_allow_html=True)
    
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
        <div class='bait-title'>💡 QS 象限獨家洞察解密 (Sample)：</div>
        {bait_text}
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    col1.metric("預估核心流程中斷率", "高危險", "急需優化", delta_color="inverse")
    col2.metric("底層優化座標 (Sprint)", "🔒 解鎖獲取", "10頁濃縮", delta_color="off")

    df_pro = pd.DataFrame({
        "戰場標籤": labels, "聲量熱度 (討論量)": 討論量, "情緒滿意度": 情緒, "商業影響力 (Impact)": np.random.randint(6, 11, 5) 
    })
    fig1 = px.scatter(df_pro, x="情緒滿意度", y="聲量熱度 (討論量)", text="戰場標籤", size="聲量熱度 (討論量)", color="情緒滿意度", color_continuous_scale=["#B30000", "#BF953F", "#FFFFFF"], title=f"{brand_name} 痛點座標分佈 (越往左越痛)")
    fig1.update_traces(textposition='top center')
    fig1.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', coloraxis_showscale=False, yaxis=dict(title=dict(standoff=15), ticksuffix=" ", showgrid=False), xaxis=dict(showgrid=False), margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig1, use_container_width=True)

else:
    st.info("此產業模組的數據正在進行 NLP 語意重構與底層運算中。尚未開放預覽。")

# ==========================================
# 4. 結帳收銀台 (錨定在最下方，看完數據立刻買)
# ==========================================

if "運算中" not in target_platform:
    st.markdown("<div class='checkout-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>⚡ 獲取完整決策報告</h3>", unsafe_allow_html=True)
    st.markdown("<div class='discount-warning'>⚠️ <b>早鳥 8 折僅限前 10 名。</b>點擊下方按鈕後，請務必在結帳頁面確認最終顯示金額為 8 折價再付款。</div>", unsafe_allow_html=True)
    
    if target_platform == "🏆 台灣電支三強 終極對標包 ($1499)":
        st.markdown("<h2 style='text-align: center; color: #BF953F;'>$ 1499 NTD</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取終極包 (前 10 名自動享 8 折)", "https://quadrastrategy.gumroad.com/l/epay-bundle-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
    elif "LINE" in target_platform:
        st.markdown("<h2 style='text-align: center; color: #BF953F;'>$ 599 NTD</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 LINE Pay 戰術包 (自動享 8 折)", "https://quadrastrategy.gumroad.com/l/epay-line-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
    elif "街口" in target_platform:
        st.markdown("<h2 style='text-align: center; color: #BF953F;'>$ 599 NTD</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 街口支付 戰術包 (自動享 8 折)", "https://quadrastrategy.gumroad.com/l/epay-jko-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
    elif "全支付" in target_platform:
        st.markdown("<h2 style='text-align: center; color: #BF953F;'>$ 599 NTD</h2>", unsafe_allow_html=True)
        st.link_button("💳 獲取 全支付 戰術包 (自動享 8 折)", "https://quadrastrategy.gumroad.com/l/epay-px-2026Q2/QS2026EARLY", type="primary", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# 頁尾免責聲明
st.markdown("<div class='trust-badge'>🔒 國際金流 Gumroad 託管 | 支援 Google Pay / Apple Pay / 國際信用卡<br>結帳後 3 秒自動發送企業級浮水印 PDF 至信箱<br><br><span style='color: #666; font-size: 10px;'>※ 本智庫採用美國 Gumroad 企業級金流託管，結帳時您的發卡銀行可能會收取微幅海外交易手續費或產生匯差。</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 11px; color: #666; margin-top: 20px;'>© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved.</p>", unsafe_allow_html=True)
