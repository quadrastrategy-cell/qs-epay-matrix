import streamlit as st
import plotly.express as px
import pandas as pd

# ==========================================
# 1. 全局設定與 KPMG 級極簡視覺規範
# ==========================================
st.set_page_config(page_title="QS 象限戰略 | 商業痛點戰略矩陣", layout="wide", page_icon="♟️")

# 視覺底線：白底、黑字、權威深藍標題 (#003366)、隱藏預設干擾
st.markdown("""
    <style>
    .stApp {background-color: #FFFFFF;}
    h1, h2, h3 {color: #003366 !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 900;}
    p, span, div, label {color: #333333;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* 側邊欄專屬深藍底色與白字微調 */
    [data-testid="stSidebar"] {background-color: #F8F9FA; border-right: 1px solid #E5E5E5;}
    /* 頂級管顧風格卡片邊框 */
    div[data-testid="metric-container"] {border-left: 4px solid #003366; padding-left: 15px; background-color: #FFFFFF; border: 1px solid #EEEEEE; border-radius: 4px;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar)：戰略控制台與動態收銀台
# ==========================================
with st.sidebar:
    st.markdown("<h3>QS 象限戰略</h3>", unsafe_allow_html=True)
    st.sidebar.caption("By HUACHIAO GROUP 樺蕎顧問團隊")
    st.write("---")
    
    # 父層級設計：電子支付戰場
    st.markdown("#### 📂 電子支付戰場")
    target_platform = st.selectbox(
        "選擇分析標的：",
        ("LINE Pay", "街口支付 (即將解鎖)", "全支付 (即將解鎖)")
    )
    
    st.write("---")
    
    # 💳 動態收銀台邏輯 (Dynamic Checkout)
    st.markdown("#### ⚡ 獲取完整決策報告")
    if target_platform == "LINE Pay":
        st.info("當前標的：LINE Pay")
        st.markdown("包含：\n- QS 獨家 2D 痛點/爽點散佈矩陣\n- Impact x Effort 開發優先順序\n- Day 1 Churn 量化模型")
        st.markdown("<h2 style='color: #003366;'>$ 599</h2>", unsafe_allow_html=True)
        # 動態替換為 LINE Pay $599 的 Gumroad 連結
        st.link_button("🛒 立即下載 (LINE Pay 戰術包)", "https://your-gumroad-link.com/linepay599", type="primary", use_container_width=True)
    else:
        st.warning(f"{target_platform} 戰略矩陣運算中。")
        st.markdown("<h2 style='color: #777777;'>敬請期待</h2>", unsafe_allow_html=True)
        st.button("🔒 尚未開放", disabled=True, use_container_width=True)

    st.write("---")
    
    # 👑 創立人署名 (防禦智財權與建立權威)
    st.markdown("**Founders**")
    st.caption("吳樺緯 (Hua-Wei Wu) \n\n吳蕎伊 (Chiao-Yi Wu)")
    
    st.write("---")
    
    # 🛡️ 終極合規防禦聲明
    st.markdown("<p style='font-size: 11px; color: #888; line-height: 1.5;'>© 2026 HUACHIAO GROUP 樺蕎顧問團隊. All rights reserved.<br>數據合規：全數樣本均經語意重構與合成處理。</p>", unsafe_allow_html=True)

# ==========================================
# 3. 主畫面模組化動態載入
# ==========================================

# 模組 A：LINE Pay 決策矩陣
if target_platform == "LINE Pay":
    st.markdown("<h1>LINE Pay 2026 服務痛點與商業衝擊分析</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px; color: #555;'>基於 2,361 筆跨平台真實評價，提煉核心戰場與資源投放優先級。</p>", unsafe_allow_html=True)
    st.write("---")

    # 3-1. 商業衝擊量化模型
    col1, col2, col3 = st.columns(3)
    col1.metric("預估 Day 1 Churn (新手流失率)", "18.5%", "高危險 (登入障礙)", delta_color="inverse")
    col2.metric("潛在月度營收損耗 (介面操作)", "$ 2.4M NTD", "高度警戒", delta_color="inverse")
    col3.metric("競品防禦力對標 (vs 街口)", "弱勢", "需優化首刷禮生態", delta_color="inverse")
    st.write("---")

    # 3-2. 準備假數據 (上線時請替換為你的 df)
    df_lp = pd.DataFrame({
        "戰場標籤": ["獲客與競品對標 (行李箱_街口)", "行銷公關災難 (客服_植村秀)", "架構歷史共業 (ipass)", "基礎流失痛點 (登入_密碼)", "基礎流失痛點 (介面_條碼)"],
        "聲量熱度 (討論量)": [41, 52, 61, 68, 44],
        "情緒滿意度": [-0.408, -0.805, -0.938, -0.577, -0.72],
        "實作成本 (Effort)": [3, 2, 9, 8, 5],
        "商業影響力 (Impact)": [7, 6, 9, 10, 8]
    })

    # 3-3. 子視角 I：QS 戰略散佈矩陣
    st.markdown("<h3>■ 核心圖表 I：QS 服務戰略矩陣</h3>", unsafe_allow_html=True)
    fig1 = px.scatter(
        df_lp, x="情緒滿意度", y="聲量熱度 (討論量)", text="戰場標籤", size="聲量熱度 (討論量)",
        color="情緒滿意度", color_continuous_scale=["#B30000", "#CCCCCC", "#003366"],
        title="LINE Pay 服務落點與情緒分析 (越往左越痛)"
    )
    fig1.update_traces(textposition='top center', marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    fig1.update_layout(
        plot_bgcolor='white', paper_bgcolor='white', font=dict(color='black'),
        xaxis=dict(showgrid=True, gridcolor='#E5E5E5', zeroline=True, zerolinecolor='black'),
        yaxis=dict(showgrid=True, gridcolor='#E5E5E5', zeroline=True, zerolinecolor='black'),
        coloraxis_showscale=False
    )
    fig1.add_hline(y=df_lp["聲量熱度 (討論量)"].mean(), line_dash="dash", line_color="gray")
    fig1.add_vline(x=0, line_dash="dash", line_color="gray")
    st.plotly_chart(fig1, use_container_width=True)

    # 3-4. 子視角 II：Impact x Effort 優先順序
    st.markdown("<h3>■ 核心圖表 II：資源投放優先順序矩陣 (Impact vs Effort)</h3>", unsafe_allow_html=True)
    fig2 = px.scatter(
        df_lp, x="實作成本 (Effort)", y="商業影響力 (Impact)", text="戰場標籤",
        color="戰場標籤", size_max=15,
        title="開發優化建議：左上角為 Quick Wins (高價值/低成本)"
    )
    fig2.update_traces(textposition='bottom center', marker=dict(size=12, symbol='square'))
    fig2.update_layout(
        plot_bgcolor='white', paper_bgcolor='white', font=dict(color='black'), showlegend=False,
        xaxis=dict(title="實作成本 (Effort) → 高", showgrid=True, gridcolor='#E5E5E5'),
        yaxis=dict(title="商業影響力 (Impact) → 高", showgrid=True, gridcolor='#E5E5E5'),
        shapes=[
            dict(type='line', x0=5, x1=5, y0=0, y1=10, line=dict(color='black', dash='dash')),
            dict(type='line', x0=0, x1=10, y0=5, y1=5, line=dict(color='black', dash='dash'))
        ]
    )
    st.plotly_chart(fig2, use_container_width=True)

# 模組 B/C：其他平台預留區
else:
    st.markdown(f"<h1>{target_platform} | 商業衝擊分析</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("此模組的數據正在進行 NLP 語意重構與底層運算中。為確保高階主管決策品質，尚未開放預覽。")
