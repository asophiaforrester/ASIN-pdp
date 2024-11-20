import streamlit as st

def generate_urls(base_url, values):
    """
    Generates URLs by substituting values into the base URL.

    :param base_url: Base URL with a placeholder (e.g., 'https://example.com/{}').
    :param values: A list of values to substitute into the base URL.
    :return: A list of complete URLs.
    """
    return [base_url.format(value) for value in values]

# Streamlit App
st.title("ASIN URL Generator")
st.write("Enter Amazon ASINs to generate clickable product URLs.")

base_url = 'https://www.amazon.com/dp/{}'
asin_input = st.text_input("ASINs (comma-separated, no spaces):")

if st.button("Generate URLs"):
    if asin_input.strip():
        values = asin_input.strip().split(",")
        urls = generate_urls(base_url, values)
        st.write("### Clickable Links:")
        for url in urls:
            st.markdown(f"- [Open {url}]({url})", unsafe_allow_html=True)
    else:
        st.warning("Please enter at least one ASIN.")
