import streamlit as st
st.header("Analysis of facial features according to the Five Elements")

st.markdown("Select the features you feel are true to your face")

st.subheader("Eyes")

eyes_good = st.multiselect("Good features of the eyes: ",[

"Bright and expressive eyes (Quick thinking, positive energy)",

"Long and even eyes (Strategic vision and deep inner self)",

"Smiling eyes (Approachable, friendly and good communication)"

])

eyes_bad = st.multiselect("Not-so-good features of the eyes: ",[

"Dull, lifeless eyes (Lack of vitality and fatigue)",

"Asymmetrical eyes (Lack of balance and weak vision)",

"Mixed whites and blacks of the iris (Prone to instability, fluctuating emotions)"

])
st.subheader("Nose")
nose_good = st.multiselect("Good characteristics of the nose: ", [
"High, straight and full nose (good fortune, easy career)",

"Thick, even nostrils (Good at saving money and managing finances)",

"Round and full nose tip (Eager to learn, tolerant, kind)"

])
nose_bad = st.multiselect("Not-so-good characteristics of the nose: ", [
"Crossed nose (unstable personality)",

"Upturned nose (difficult to save money, prone to spending)",

"Thin nostrils (unstable finances)"

])

st.subheader("Forehead")

forehead_good = st.multiselect("Good characteristics of the forehead: ", [
"High and wide forehead (Intelligent, logical thinking)",

"Full, smooth forehead (good career, favorable)",

"No early wrinkles (stable positive thinking)"

])
forehead_bad = st.multiselect("Unfavorable characteristics of the forehead: ",[

"Low and narrow forehead (limited vision)",

"Slanted forehead (lack of steadfastness)",

"Concave forehead (easily influenced, indecisive)"

])
st.subheader("Ears")

ears_good = st.multiselect("Favorable characteristics of the ears: ", [
"Full ears, clear rims (good health, good fortune)",

"Thick earlobes (stable future)",

"Ears higher than eyebrows (good thinking, bright intellect)"

])

ears_bad = st.multiselect("Unfavorable characteristics of the ears: ", [
"Thin ears (weak fortune, easily influenced)",

"Ears sticking out (hot-tempered, impulsive)",

"Ears lower than eyebrows (lack of strategic thinking)"

])