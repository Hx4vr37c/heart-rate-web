import streamlit as st

# ตั้งค่าหน้าตาเว็บ
st.set_page_config(page_title="Heart Rate Zone Calculator", layout="centered")

st.title("🏃‍♂️ Karvonen HR Zone Calculator")
st.write("คำนวณโซนการฝึกซ้อมที่แม่นยำสำหรับคุณ")

# ส่วนรับข้อมูล (Sidebar หรือหน้าหลัก)
with st.container():
    age = st.number_input("อายุของคุณ (ปี)", min_value=1, max_value=120, value=30)
    resting_hr = st.number_input("อัตราการเต้นหัวใจขณะพัก (RHR)", min_value=30, max_value=120, value=60)

# คำนวณ
max_hr = 220 - age
hrr = max_hr - resting_hr

# แสดงผลแบบการ์ดสวยๆ
st.divider()
st.subheader("โซนการออกกำลังกายของคุณ")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Zone 2**\n\n(Fat Burn)\n\n" + f"{ (hrr * 0.6) + resting_hr :.0f} - { (hrr * 0.7) + resting_hr :.0f} bpm")

with col2:
    st.success("**Zone 3**\n\n(Aerobic)\n\n" + f"{ (hrr * 0.7) + resting_hr :.0f} - { (hrr * 0.8) + resting_hr :.0f} bpm")

with col3:
    st.warning("**Zone 4**\n\n(Threshold)\n\n" + f"{ (hrr * 0.8) + resting_hr :.0f} - { (hrr * 0.9) + resting_hr :.0f} bpm")
