import streamlit as st
from utils.bmi import calculate_bmi, bmi_status
from utils.ml_model import load_sleep_model
from utils.storage import save_weight, load_weight

st.title("❤️ Theo dõi sức khỏe")

weight = st.number_input("Cân nặng (kg)", 10.0, 200.0, 60.0)
height = st.number_input("Chiều cao (m)", 1.0, 2.5, 1.7)

if st.button("Tính BMI"):
    bmi = calculate_bmi(weight, height)
    st.metric("BMI", f"{bmi:.2f}")
    st.metric("Trạng thái", bmi_status(bmi))

@st.cache_resource
def get_model():
    return load_sleep_model()

model = get_model()

age = st.number_input("Tuổi", 5, 100, 25)
activity = st.slider("Vận động", 1, 10, 5)
screen = st.number_input("Giờ màn hình", 0, 24, 6)

if st.button("Dự đoán ngủ"):
    result = model.predict([[age, activity, screen]])[0]
    st.success(f"Bạn nên ngủ {result:.1f} giờ")

day = st.number_input("Ngày", 1)
w = st.number_input("Cân nặng", 30.0, 200.0)

if st.button("Lưu dữ liệu"):
    save_weight(day, w)
    st.success("Đã lưu!")

df = load_weight()
if not df.empty:
    st.line_chart(df.set_index("day"))
