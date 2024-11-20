import streamlit as st

def generate_urls(base_url, asin_list):
    """Generate Amazon URLs from a list of ASINs."""
    return [base_url.format(asin) for asin in asin_list]

# Streamlit App
st.title("Amazon ASIN Multi-Link Opener")
st.write("Enter ASINs to open their product pages on Amazon with a single click.")

base_url = "https://www.amazon.com/dp/{}"
asin_input = st.text_area("Enter ASINs (one per line):")

if st.button("Open All Links"):
    if asin_input.strip():
        asin_list = [x.strip() for x in asin_input.split("\n") if x.strip()]
        urls = generate_urls(base_url, asin_list)
        
        # Generate JavaScript to open all URLs
        js_code = ""
        for url in urls:
            js_code += f"window.open('{url}', '_blank');\n"
        
        # Inject JavaScript into the browser
        st.markdown(
            f"""
            <script>
            {js_code}
            </script>
            """,
            unsafe_allow_html=True,
        )
        st.success("Links are being opened in new tabs!")
    else:
        st.warning("Please enter at least one ASIN.")
