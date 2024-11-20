import streamlit as st
import webbrowser

def open_urls(base_url, values):
    """
    Opens URLs in the default web browser.

    :param base_url: Base URL with a placeholder (e.g., 'https://example.com/{}').
    :param values: A list of values to substitute into the base URL.
    """
    for value in values:
        url = base_url.format(value)
        webbrowser.open_new_tab(url)
        st.write(f"Opened: {url}")

# Streamlit App
st.title("ASIN URL Opener")
st.write("Enter Amazon ASINs to generate and open product URLs.")

base_url = 'https://www.amazon.com/dp/{}'
asin_input = st.text_input("ASINs (comma-separated, no spaces):")

if st.button("Open URLs"):
    if asin_input.strip():
        values = asin_input.strip().split(",")
        open_urls(base_url, values)
    else:
        st.warning("Please enter at least one ASIN.")
