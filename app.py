import streamlit as st
import pandas as pd

st.set_page_config(page_title="Weekly HR Planner", page_icon="📅", layout="wide")

# ส่วนหัว
st.title("📅 Weekly Exercise Planner")
st.subheader("วางแผนการออกกำลังกายรายสัปดาห์ตามหลัก Karvonen")
st.divider()

# รับข้อมูล
col_input, col_info = st.columns([1, 1])
with col_input:
    age = st.number_input("อายุ (ปี)", value=30)
    resting_hr = st.number_input("Resting HR (ชีพจรขณะพัก)", value=60)

max_hr = 220 - age
hrr = max_hr - resting_hr

def get_hr(intensity):
    return int((hrr * intensity) + resting_hr)

# คำนวณแต่ละโซน
z2_low, z2_high = get_hr(0.6), get_hr(0.7)
z3_low, z3_high = get_hr(0.7), get_hr(0.8)
z4_low, z4_high = get_hr(0.8), get_hr(0.9)

st.divider()

# แสดงผลเป้าหมายรายสัปดาห์ (Weekly Goals)
st.header("🎯 เป้าหมายรายสัปดาห์ (Weekly Goals)")
st.info("💡 อ้างอิงคำแนะนำ: ออกกำลังกายปานกลางอย่างน้อย 150 นาที หรือ หนักมาก 75 นาที ต่อสัปดาห์")

# สร้างการ์ดสรุปรายสัปดาห์
c1, c2, c3 = st.columns(3)

with c1:
    st.info("### 🔵 Zone 2\n**Endurance & Fat Burn**")
    st.metric("อัตราการเต้นหัวใจ", f"{z2_low} - {z2_high} bpm")
    st.success("✅ **เป้าหมาย: 150 นาที/สัปดาห์**")
    st.write("📌 **คำแนะนำ:** แบ่งเป็น 30-50 นาที x 3-5 วัน")

with c2:
    st.success("### 🟢 Zone 3\n**Aerobic & Tempo**")
    st.metric("อัตราการเต้นหัวใจ", f"{z3_low} - {z3_high} bpm")
    st.success("✅ **เป้าหมาย: 75-100 นาที/สัปดาห์**")
    st.write("📌 **คำแนะนำ:** แบ่งเป็น 25-35 นาที x 3 วัน")

with c3:
    st.warning("### 🔴 Zone 4\n**HIIT & Threshold**")
    st.metric("อัตราการเต้นหัวใจ", f"{z4_low} - {z4_high} bpm")
    st.success("✅ **เป้าหมาย: 40-60 นาที/สัปดาห์**")
    st.write("📌 **คำแนะนำ:** เช่น Norwegian 4x4 x 2 วัน")

st.divider()

# ตารางเปรียบเทียบสำหรับการพิมพ์หรือบันทึก
with st.expander("📋 ตารางสรุปแผนการฝึกซ้อมรายสัปดาห์"):
    weekly_plan = {
        "ประเภทการออกกำลังกาย": ["ความหนักต่ำ (Zone 2)", "ความหนักปานกลาง (Zone 3)", "ความหนักสูง (Zone 4)"],
        "ช่วงหัวใจ (bpm)": [f"{z2_low}-{z2_high}", f"{z3_low}-{z3_high}", f"{z4_low}-{z4_high}"],
        "เป้าหมายรวม/สัปดาห์": ["150 นาที", "75-100 นาที", "40-60 นาที"],
        "ความถี่ที่แนะนำ": ["3-5 ครั้ง/สัปดาห์", "2-3 ครั้ง/สัปดาห์", "1-2 ครั้ง/สัปดาห์"],
        "ความรู้สึก": ["พูดเป็นประโยคได้", "พูดได้สั้นๆ", "หอบจนพูดแทบไม่ได้"]
    }
    st.table(pd.DataFrame(weekly_plan))

st.caption("หมายเหตุ: ข้อมูลนี้เป็นคำแนะนำเบื้องต้น หากคุณเป็นมือใหม่ควรเริ่มจาก Zone 2 และค่อยๆ เพิ่มความเข้มข้นขึ้น")
