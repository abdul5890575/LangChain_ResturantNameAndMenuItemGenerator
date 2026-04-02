import streamlit as st
import langchain_helper
st.title("Restaurant name generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian","Italian","Mexican","Chinese"))


if cuisine:
    res = langchain_helper.get_res_name(cuisine)
    st.header(res["restaurant_name"].strip())
    menu_items = res["menu_items"].strip().split(",")

    for item in menu_items:
        st.write("-",item)

