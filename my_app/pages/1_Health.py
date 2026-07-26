import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import feedparser
import numpy as np
import time
import matplotlib.pyplot as plt
import random
import time
#===================  CSS LÀM ĐẸP GIAO DIỆN  ====================
st.title("🎧 Health Application")

main1, main2 = st.tabs([
    "Basic Health Check",
    "Professional Health Check"
])
with main1:
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs([
        "BMI Check",
        "Sleep Duration Check",
        "Heartbeat Check",
        "Daily Water Intake",
        "Daily Step Counter",
        "Rest Reminder & Exercise"
    ])
    with tab1:
        st.header("BMI Check")
        can_nang = st.number_input("Weight", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
        chieu_cao = st.number_input("Height", min_value=1.0, max_value=2.5, value=1.7, step=0.01)

        bmi_min = 18.5
        can_nang_min = bmi_min * (chieu_cao ** 2)
        can_nang_tang = can_nang_min - can_nang

        bmi_max = 24.9
        can_nang_max = bmi_max * (chieu_cao ** 2)
        can_nang_giam = can_nang - can_nang_max

        if st.button("Calculate BMI"):
            bmi = can_nang / (chieu_cao ** 2)
            st.success(f"Your BMI: {bmi:.2f}")

            if bmi < 18.5:
                st.warning("You are underweight. Try to eat more nutritious food.")
                st.info(f"You need to gain {can_nang_tang:.2f} kg")

            elif 18.5 <= bmi < 25:
                st.info("Your weight is within the healthy range.")

            elif 25 <= bmi < 30:
                st.warning("You are overweight. Eat healthier and exercise more.")
                st.info(f"You need to lose {can_nang_giam:.2f} kg")

            else:
                st.error("You are obese. Please consult a healthcare professional.")
                st.info(f"You need to lose {can_nang_giam:.2f} kg")

    with tab2:
        st.header("Sleep Duration Estimator")

        x = [
            [10, 1, 8],
            [20, 5, 6],
            [25, 8, 3],
            [30, 6, 5],
            [35, 2, 9],
            [40, 4, 3]
        ]

        y = [10, 8, 6, 7, 9.5, 9]

        model = LinearRegression()
        model.fit(x, y)

        st.write("Personal Information")

        age = st.number_input("Age:", min_value=5, max_value=100, value=25)
        activity = st.slider("Activity Level (1 = Very Low, 10 = Very High)", 1, 10, 5)
        screen_time = st.number_input("Daily Screen Time (hours)", min_value=0, max_value=24, value=6)

        if st.button("Predict"):
            input_data = [[age, activity, screen_time]]
            result = model.predict(input_data)[0]

            st.success(f"You should sleep about {result:.1f} hours per night")

            if result < 6.5:
                st.warning("😴 You should get more sleep to stay healthy.")

            elif result > 9:
                st.info("Try to catch up on sleep—you've been working hard.")

            else:
                st.success("Excellent! Your sleep duration is ideal. Keep it up!")

    with tab3:
        st.header("Heart Rate Assessment")

        model = LinearRegression()
        model.fit(x, y)

        st.subheader("Personal Information")

        hr = st.number_input("Heart Rate (bpm):", min_value=40, max_value=200, value=75)
        age = st.number_input("Age:", min_value=1, max_value=120, value=30)
        weight = st.number_input("Weight (kg):", min_value=10.0, max_value=200.0, value=60.0)

        if st.button("Check",key="a"):
            score = model.predict([[hr, age, weight]])[0]

            st.success(f"Health Risk Score: **{score:.2f}**")

            if age < 13:
                safe_threshold = 1.5
            elif age < 60:
                safe_threshold = 2.0
            else:
                safe_threshold = 2.5

            if score < safe_threshold:
                st.info("Your health condition looks excellent. Keep maintaining your healthy lifestyle.")

            elif score < (safe_threshold + 1):
                st.warning("Your health shows slight abnormalities. Regular check-ups are recommended.")

            elif score < (safe_threshold + 2):
                st.warning("Your health condition is not ideal. Please visit a hospital for further examination.")

            else:
                st.error("Your health may be at serious risk. Seek medical attention immediately.")
    with tab4:
        st.header("Daily Water Intake")
        age3 = st.number_input("Age:", min_value=0.0, max_value=120.0, value=18.0, step=1.0)

        if st.button("Check",key="b"):
            if age3 < 4:
                st.info("You should drink **1.3 liters of water** per day.")
            elif 4 <= age3 <= 8:
                st.info("You should drink **1.7 liters of water** per day.")
            elif 9 <= age3 <= 13:
                st.info("You should drink **2.1–2.4 liters of water** per day.")
            elif 14 <= age3 <= 18:
                st.info("You should drink **2.3–3.3 liters of water** per day.")
            elif 19 <= age3 <= 50:
                st.warning("You should drink **2.7 liters/day (women) or 3.3 liters/day (men)**.")
            else:
                st.error("You should drink **2.5–3.0 liters of water** per day depending on your health condition and activity level.")

    with tab5:
        st.header("Daily Step Recommendation")
        st.title("How Many Steps Should You Walk Each Day?")

        age2 = st.number_input(
            "Enter your age:",
            min_value=0.0,
            max_value=130.0,
            value=18.0,
            step=1.0
        )

        if st.button("Check Steps"):
            if age2 < 18:
                st.info("You should walk **12,000–15,000 steps** per day.")
            elif 18 <= age2 <= 39:
                st.info("You should walk **8,000–10,000 steps** per day.")
            elif 40 <= age2 <= 64:
                st.warning("You should walk **7,000–9,000 steps** per day.")
            elif age2 > 64:
                st.warning("You should walk **6,000–8,000 steps** per day.")
            else:
                st.error("An error occurred. Please check your information and try again.")
    with tab6:
        minutes = st.number_input(
                    "Enter your working time (minutes):",
                    min_value=1,
                    step=1,
                    value=1
                )
        
        if st.button("Start Countdown"):
            st.info(f"Countdown started: {minutes} minute(s)")
            my_bar = st.progress(0)
            total_seconds = minutes * 60
        
            for sec in range(total_seconds):
                percent = int(((sec + 1) / total_seconds) * 100)
                my_bar.progress(percent)
                time.sleep(1)
        
            st.success("Time's up! Stand up, take a break, and do some stretching!")
        
            audio_file = open("alarm.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
        
        st.set_page_config(
                    page_title="Advanced Health Application",
                    layout="centered"
                )
        
        st.title("Advanced Health Monitoring Application")
        
        st.header("Personal Information")
        
        name = st.text_input("Full Name:")
        
        age = st.number_input(
                    "Age:",
                    min_value=0,
                    max_value=120,
                    step=1
                )
        
        gender = st.radio(
                    "Gender:",
                    ("Male", "Female")
                )
        
        height = st.number_input(
                    "Height (cm):",
                    min_value=50.0,
                    max_value=250.0,
                    step=0.1
                )
        
        weight = st.number_input(
                    "Weight (kg):",
                    min_value=10.0,
                    max_value=250.0,
                    step=0.1
                )
        
        activity_level = st.selectbox(
                    "Physical Activity Level:",
                    [
                        "Sedentary",
                        "Lightly Active (1–3 days/week)",
                        "Moderately Active (3–5 days/week)",
                        "Very Active (6–7 days/week)",
                        "Extremely Active (Twice a day)"
                    ]
                )
        
        if st.button("Analyze Health"):
        
            if height > 0 and weight > 0:
        
                height_m = height / 100
                bmi = weight / (height_m ** 2)
        
                if gender == "Male":
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5
                else:
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
                activity_factors = {
                            "Sedentary": 1.2,
                            "Lightly Active (1–3 days/week)": 1.375,
                            "Moderately Active (3–5 days/week)": 1.55,
                            "Very Active (6–7 days/week)": 1.725,
                            "Extremely Active (Twice a day)": 1.9
                        }
        
                activity_factor = activity_factors[activity_level]
                tdee = bmr * activity_factor
                water_intake = weight * 35 / 1000
        
                st.subheader("Health Analysis Results")
        
                st.write(f"**Hello, {name}!**")
                st.write(f"**BMI:** {bmi:.2f}")
                st.write(f"**BMR (Basal Metabolic Rate):** {bmr:.0f} kcal/day")
                st.write(f"**TDEE (Total Daily Energy Expenditure):** {tdee:.0f} kcal/day")
                st.write(f"**Recommended Daily Water Intake:** {water_intake:.1f} liters")
        
                st.markdown("### BMI Evaluation")
        
                if bmi < 18.5:
                    st.warning(
                                f"You are underweight. You should gain approximately {round(((18.5-bmi)*(height_m**2)),2)} kg."
                            )
        
                elif 18.5 <= bmi < 24.9:
                    st.success(
                                "Your weight is within the healthy range. Keep up your healthy lifestyle!"
                            )
        
                elif 25 <= bmi < 29.9:
                    st.warning(
                                f"You are overweight. Consider improving your diet and increasing physical activity. You should lose approximately {round(((bmi-24.9)*(height_m**2)),2)} kg."
                            )
        
                else:
                    st.error(
                                f"You are obese. It is recommended that you consult a healthcare professional. You should lose approximately {round(((bmi-24.9)*(height_m**2)),2)} kg."
                            )
        
                st.markdown("### Suggested Calorie Intake")
        
                col1, col2 = st.columns(2)
        
                with col1:
                    st.info("**Maintain Weight**")
                    st.write(f"Consume about **{tdee:.0f} kcal/day**")
        
                with col2:
                    st.info("**Lose Weight**")
                    st.write(f"Consume about **{tdee-300:.0f} kcal/day**")
        
                st.markdown("### Sample Daily Meal Plan")
        
                st.markdown("""
            - **Breakfast:** Boiled eggs, whole-grain bread, fresh fruit
            - **Lunch:** Brown rice, grilled chicken breast, steamed vegetables, soup
            - **Dinner:** Green salad, steamed fish, low-sugar fruit
            - **Snack:** Mixed nuts, low-sugar yogurt
            """)
with main2:
    tab6, tab7, tab8=st.tabs([    
        "Personality Assessment",
        "Rest & Exercise Reminder",
        "Weight Prediction"
    ])
    with tab6:

        st.header("DISC Personality Assessment")
        st.markdown("Choose the statement that best describes you and the one that describes you the least in each group.")

        groups = [
            {
                "D": "I am decisive and enjoy taking control.",
                "I": "I am friendly and enjoy talking with people.",
                "S": "I am patient and dependable.",
                "C": "I am accurate and systematic.",
            },
            {
                "D": "I enjoy challenges and act quickly.",
                "I": "I am energetic and optimistic.",
                "S": "I am steady and supportive.",
                "C": "I prefer working with clear rules and procedures.",
            },
            {
                "D": "I like being in control of the results.",
                "I": "I enjoy receiving recognition.",
                "S": "I value harmony above all.",
                "C": "I pay close attention to details and analysis.",
            }
        ]

        scores = {"D": 0, "I": 0, "S": 0, "C": 0}

        for idx, group in enumerate(groups):
            st.markdown(f"### Group {idx + 1}")

            options = list(group.values())

            most = st.radio(
                "Most like you:",
                options,
                key=f"most_{idx}"
            )

            least = st.radio(
                "Least like you:",
                options,
                key=f"least_{idx}"
            )

            for key, val in group.items():
                if val == most:
                    scores[key] += 1
                if val == least:
                    scores[key] -= 1

        if st.button("View DISC Result"):
            st.header("Your DISC Result")

            max_type = max(scores, key=scores.get)

            for style, score in scores.items():
                st.write(f"{style}: {score} points")

            st.markdown(f"**Your dominant personality type is: {max_type}**")

            descriptions = {
                "D": "Decisive, result-oriented, and enjoys taking control.",
                "I": "Outgoing, energetic, and inspiring communicator.",
                "S": "Patient, dependable, and supportive of others.",
                "C": "Accurate, analytical, and follows procedures carefully."
            }

            st.info(descriptions[max_type])

            st.markdown("---")
            st.markdown("### DISC Personality Types")

            st.markdown("""
    - **D (Dominance):** A leader who is proactive and competitive. Example: CEO, Founder.
    - **I (Influence):** An inspiring communicator who enjoys social interaction. Example: Marketer, Public Speaker.
    - **S (Steadiness):** Loyal, patient, and supportive. Example: Teacher, Nurse.
    - **C (Conscientiousness):** Detail-oriented, analytical, and process-driven. Example: Accountant, Engineer.
            """)

            st.caption("This DISC assessment is for reference purposes only.")

        st.header("Five-Element Face Analysis")
        st.markdown("Select the facial features that best match your appearance.")

        st.subheader("Eyes")

        eyes_good = st.multiselect(
            "Positive eye features:",
            [
                "Bright and expressive eyes (Quick thinking and positive energy)",
                "Long and balanced eyes (Strategic vision and deep insight)",
                "Smiling eyes (Friendly, approachable, and good communication)"
            ]
        )

        eyes_bad = st.multiselect(
            "Less favorable eye features:",
            [
                "Dull, lifeless eyes (Low vitality and fatigue)",
                "Uneven eyes (Lack of balance or weak visual impression)",
                "White showing around the iris (Emotional instability or mood swings)"
            ]
        )

        st.subheader("Nose")

        nose_good = st.multiselect(
            "Positive nose features:",
            [
                "Straight, well-shaped nose (Good financial fortune and career potential)",
                "Thick, even nostrils (Good money management)",
                "Rounded nose tip (Curious, kind, and generous)"
            ]
        )

        nose_bad = st.multiselect(
            "Less favorable nose features:",
            [
                "Crooked nose (Unstable personality)",
                "Upturned nose (Difficulty saving money)",
                "Thin nostrils (Financial instability)"
            ]
        )

        st.subheader("Forehead")

        forehead_good = st.multiselect(
            "Positive forehead features:",
            [
                "High and broad forehead (Intelligent and logical thinker)",
                "Full and smooth forehead (Successful career prospects)",
                "No early wrinkles (Positive and stable mindset)"
            ]
        )

        forehead_bad = st.multiselect(
            "Less favorable forehead features:",
            [
                "Low and narrow forehead (Limited vision)",
                "Sloping forehead (Lack of persistence)",
                "Sunken forehead (Indecisive and easily influenced)"
            ]
        )

        st.subheader("Ears")

        ears_good = st.multiselect(
            "Positive ear features:",
            [
                "Full ears with well-defined rims (Good health and fortune)",
                "Thick earlobes (Prosperous later life)",
                "Ears positioned above the eyebrows (Strong intellect)"
            ]
        )

        ears_bad = st.multiselect(
            "Less favorable ear features:",
            [
                "Thin ears (Weaker fortune and easily influenced)",
                "Protruding ears (Impulsive personality)",
                "Ears positioned below the eyebrows (Limited strategic thinking)"
            ]
        )
    with tab7:
        st.subheader("Rest Reminder & Exercise")
        minutes = st.number_input(
            "Enter your working time (minutes):",
            min_value=1,
            step=1,
            value=1,
            key="A"
        )

        if st.button("Start Countdown",key="B"):
            st.info(f"Countdown started: {minutes} minute(s)")
            my_bar = st.progress(0)
            total_seconds = minutes * 60

            for sec in range(total_seconds):
                percent = int(((sec + 1) / total_seconds) * 100)
                my_bar.progress(percent)
                time.sleep(1)

            st.success("Time's up! Stand up, take a break, and do some stretching!")

            audio_file = open("alarm.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

        st.set_page_config(
            page_title="Advanced Health Application",
            layout="centered"
        )

        st.title("Advanced Health Monitoring Application")

        st.header("Personal Information")

        name = st.text_input("Full Name:",key="C")

        age = st.number_input(
            "Age:",
            min_value=0,
            max_value=120,
            step=1,
            key="F"
        )

        gender = st.radio(
            "Gender:",
            ("Male", "Female"),
            key="D"
        )

        height = st.number_input(
            "Height (cm):",
            min_value=50.0,
            max_value=250.0,
            step=0.1,
            key="E"
        )

        weight = st.number_input(
            "Weight (kg):",
            min_value=10.0,
            max_value=250.0,
            step=0.1,
            key="G"
        )

        activity_level = st.selectbox(
            "Physical Activity Level:",
            [
                "Sedentary",
                "Lightly Active (1–3 days/week)",
                "Moderately Active (3–5 days/week)",
                "Very Active (6–7 days/week)",
                "Extremely Active (Twice a day)"
            ],
            key="N"
        )

        if st.button("Analyze Health",key="J"):

            if height > 0 and weight > 0:

                height_m = height / 100
                bmi = weight / (height_m ** 2)

                if gender == "Male":
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5
                else:
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161

                activity_factors = {
                    "Sedentary": 1.2,
                    "Lightly Active (1–3 days/week)": 1.375,
                    "Moderately Active (3–5 days/week)": 1.55,
                    "Very Active (6–7 days/week)": 1.725,
                    "Extremely Active (Twice a day)": 1.9
                }

                activity_factor = activity_factors[activity_level]
                tdee = bmr * activity_factor
                water_intake = weight * 35 / 1000

                st.subheader("Health Analysis Results")

                st.write(f"**Hello, {name}!**")
                st.write(f"**BMI:** {bmi:.2f}")
                st.write(f"**BMR (Basal Metabolic Rate):** {bmr:.0f} kcal/day")
                st.write(f"**TDEE (Total Daily Energy Expenditure):** {tdee:.0f} kcal/day")
                st.write(f"**Recommended Daily Water Intake:** {water_intake:.1f} liters")

                st.markdown("### BMI Evaluation")

                if bmi < 18.5:
                    st.warning(
                        f"You are underweight. You should gain approximately {round(((18.5-bmi)*(height_m**2)),2)} kg."
                    )

                elif 18.5 <= bmi < 24.9:
                    st.success(
                        "Your weight is within the healthy range. Keep up your healthy lifestyle!"
                    )

                elif 25 <= bmi < 29.9:
                    st.warning(
                        f"You are overweight. Consider improving your diet and increasing physical activity. You should lose approximately {round(((bmi-24.9)*(height_m**2)),2)} kg."
                    )

                else:
                    st.error(
                        f"You are obese. It is recommended that you consult a healthcare professional. You should lose approximately {round(((bmi-24.9)*(height_m**2)),2)} kg."
                    )

                st.markdown("### Suggested Calorie Intake")

                col1, col2 = st.columns(2)

                with col1:
                    st.info("**Maintain Weight**")
                    st.write(f"Consume about **{tdee:.0f} kcal/day**")

                with col2:
                    st.info("**Lose Weight**")
                    st.write(f"Consume about **{tdee-300:.0f} kcal/day**")

                st.markdown("### Sample Daily Meal Plan")

                st.markdown("""
    - **Breakfast:** Boiled eggs, whole-grain bread, fresh fruit
    - **Lunch:** Brown rice, grilled chicken breast, steamed vegetables, soup
    - **Dinner:** Green salad, steamed fish, low-sugar fruit
    - **Snack:** Mixed nuts, low-sugar yogurt
    """)