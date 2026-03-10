# import streamlit as st
# import pandas as pd
# import plotly.express as px

# df = pd.read_csv("cleaned_data.csv")

# st.title("Smart Farming Soil Moisture Dashboard")

# st.subheader("Soil Moisture Trend")
# fig = px.line(df, x="datetime", y="moisture0")
# st.plotly_chart(fig)

# st.subheader("Current Soil Moisture")
# current = df["moisture0"].iloc[-1]
# st.metric("Moisture Level", current)

# st.subheader("Sensor Correlation")

# corr = df[["moisture0","moisture1","moisture2","moisture3","moisture4"]].corr()
# fig2 = px.imshow(corr, text_auto=True)

# st.plotly_chart(fig2)

# st.subheader("Irrigation Alert")

# threshold = 300

# if current < threshold:
#     st.error("⚠ Soil too dry! Irrigation needed")
# else:
#     st.success("Soil moisture is normal")

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# st.title("Smart Farming Dashboard - Soil Moisture Monitoring")

# # Load data
# df = pd.read_csv("cleaned_data.csv")

# # convert datetime
# df['datetime'] = pd.to_datetime(df['datetime'])

# # =========================
# # 1 TIME SERIES MOISTURE TREND
# # =========================

# st.subheader("Soil Moisture Trend Over Time")

# fig = px.line(
#     df,
#     x="datetime",
#     y=["moisture0","moisture1","moisture2","moisture3","moisture4"]
# )

# st.plotly_chart(fig)

# # =========================
# # 2 GAUGE METER
# # =========================

# st.subheader("Current Soil Moisture Gauge")

# latest = df.iloc[-1]
# threshold = 300

# st.subheader("Irrigation Alert")

# if latest["moisture0"] < threshold:
#     st.error("⚠ Soil too dry! Irrigation needed")
# else:
#     st.success("Soil moisture is normal")

# fig = go.Figure(go.Indicator(
#     mode="gauge+number",
#     value=latest["moisture0"],
#     title={'text': "Moisture Sensor level"},
#     gauge={
#         'axis': {'range': [0,1000]},
#         'bar': {'color': "blue"},
#         'steps': [
#             {'range': [0, 300], 'color': "red"},
#             {'range': [300, 600], 'color': "yellow"},
#             {'range': [600, 1000], 'color': "green"}
#         ]
#     }
# ))

# st.plotly_chart(fig)

# # =========================
# # 3 HEATMAP
# # =========================

# st.subheader("Sensor Correlation Heatmap")

# corr = df[['moisture0','moisture1','moisture2','moisture3','moisture4']].corr()

# fig = px.imshow(corr, text_auto=True)

# st.plotly_chart(fig)

# # =========================
# # 4 ALERT SYSTEM
# # =========================

# st.subheader("Irrigation Alert")

# threshold = 30

# if latest["moisture0"] < threshold:
#     st.error("⚠ Soil moisture is too low! Irrigation needed.")
# else:
#     st.success("Soil moisture is within safe range.")

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

# Load data
df = pd.read_csv("cleaned_data.csv")

# Title
st.title("📊🌱Smart Farming Soil Moisture Dashboard")

# Ambil data terakhir
latest = df.iloc[-1]
current = latest["moisture0"]
threshold = 300

# Layout 2 kolom
col1, col2 = st.columns(2)

# =====================
# Gauge Moisture
# =====================
with col1:

    st.subheader("✨Current Soil Moisture")

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current,
        title={'text': "Moisture Level"},
        gauge={
            'axis': {'range': [0, 1000]},
            'steps': [
                {'range': [0, 300], 'color': "red"},
                {'range': [300, 600], 'color': "yellow"},
                {'range': [600, 1000], 'color': "green"}
            ]
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

# =====================
# Alert System
# =====================
with col2:

    st.subheader("🚨 Irrigation Alert")

    if current < threshold:
        st.error("⚠ Soil too dry! Irrigation needed")
    else:
        st.success("✅ Soil moisture is normal")

# =====================
# Time Series
# =====================

st.subheader("📊 Moisture Sensor Trend")

fig = px.line(
    df,
    x="datetime",
    y=["moisture0","moisture1","moisture2","moisture3","moisture4"],
    title="Soil Moisture Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# =====================
# Correlation Heatmap
# =====================

st.subheader("📊 Sensor Correlation Heatmap")

corr = df[
    ["moisture0","moisture1","moisture2","moisture3","moisture4"]
].corr()

fig2 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues"
)

st.plotly_chart(fig2, use_container_width=True)

# =====================
#   Histogram
# =====================
st.subheader("  📊 Moisture Distribution")

fig_hist = px.histogram(
    df,
    x="moisture0",
    nbins=40,
    title="Distribution of Soil Moisture Sensor 0"
)

st.plotly_chart(fig_hist, use_container_width=True)

# =====================
#   Bar Chart
# =====================
st.subheader("  📊 Average Moisture per Sensor")

sensor_avg = df[
    ["moisture0","moisture1","moisture2","moisture3","moisture4"]
].mean()

fig_bar = px.bar(
    x=sensor_avg.index,
    y=sensor_avg.values,
    labels={"x":"Sensor","y":"Average Moisture"},
    title="Average Moisture per Sensor"
)

st.plotly_chart(fig_bar, use_container_width=True)

# =====================
# Box Plot
# =====================
st.subheader("  📊 Moisture Variability")
fig_box = px.box(
    df,
    y=["moisture0","moisture1","moisture2","moisture3","moisture4"],
    title="Box Plot of Moisture Sensors"
)
st.plotly_chart(fig_box, use_container_width=True)

# =====================
# Line Chart with Threshold
# ===================== 
st.subheader("  📊 Moisture Trend with Threshold")
fig_line_thresh = go.Figure()   
fig_line_thresh.add_trace(go.Scatter(x=df["datetime"], y=df["moisture0"], mode='lines', name='Moisture 0'))
fig_line_thresh.add_trace(go.Scatter(x=df["datetime"], y=[threshold]*len(df), mode='lines', name='Threshold', line=dict(dash='dash', color='red')))
fig_line_thresh.update_layout(title="Moisture Trend with Threshold", xaxis_title="Datetime", yaxis_title="Moisture Level")
st.plotly_chart(fig_line_thresh, use_container_width=True)  

# =====================
# Scatter Plot
# =====================     
st.subheader("  📊 Moisture Sensor Scatter Plot")
fig_scatter = px.scatter(
    df,
    x="moisture0",
    y="moisture1",
    title="Scatter Plot of Moisture Sensor 0 vs Sensor 1",
    labels={"moisture0":"Moisture Sensor 0", "moisture1":"Moisture Sensor 1"}
)
st.plotly_chart(fig_scatter, use_container_width=True)
