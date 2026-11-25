import streamlit as st

st.set_page_config(
    page_title="IT STEP",
    page_icon="💻"
)

# st.header("IT STEP")
# st.subheader("Welcome to IT STEP!")
# st.text("Some text")
# st.write("Some text")
# st.markdown("**Bold** and *italic*")
# st.markdown("""
# ```python
# import random
# random_number = random.randint(1, 100)
# """)

# name = st.text_input("Name:")
# age   = st.slider("Your age", 0, 100, 25)
# color = st.selectbox("Your favourite color", ["red", "green", "blue"])
# agree = st.checkbox("I agree with the terms and conditions")
# file  = st.file_uploader("Upload a CSV")
# button = st.button("Submit")
# date = st.date_input("Your birthday:")


# col1, col2, col3, col4, col5 = st.columns(5)
# with col1:
#     st.write("Left")
# with col2:
#     st.write("Right")
# with col3:
#     st.write("three")
# with col4:
#     st.write("four")
# with col5:
#     st.write("five")


# st.sidebar.title("Settings")
# option = st.sidebar.radio(
#   "View", ["Home","About", "Contact"])


# tab1, tab2 = st.tabs(
#     ["Data", "Chart"])
# with tab1:
#     st.write("Data view")
# with tab2:
#     st.write("Chart view")


# with st.expander("Details"):
#     st.write("Hidden content revealed on click")
#     st.write("Hidden content revealed on click")
#     st.write("Hidden content revealed on click")
#     st.checkbox("I agree")


# import pandas as pd
# df = pd.DataFrame({
#     "x": range(10),
#     "y": range(10, 20)
# })
# st.dataframe(df)  # interactive
# st.table(df)

# st.line_chart(df)
# st.bar_chart(df)
# st.area_chart(df)


# st.metric(
#     label="Bitcoin",
#     value="$1.2M",
#     delta="+5%"
# )


# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# if st.button("Increment"):
#     st.session_state.counter += 1

# st.write("Count:", st.session_state.counter)


import streamlit as st
import pandas as pd

st.title("CSV Explorer")

uploaded_file = st.file_uploader(
    "Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    column = st.selectbox(
        "Choose a column",
        df.columns)

    st.line_chart(df[column])
    st.write(df[column].describe())