import streamlit as st
from urllib.parse import urlparse

# Function to extract and print main URLs
def extract_main_url(url_list):
    main_urls = []
    for url in url_list:
        parsed_url = urlparse(url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        main_urls.append(main_url)
    return main_urls

# Define the Streamlit app
def main():
    st.title("URL Main Domain Extractor")

    # Input for multiple URLs
    st.sidebar.header("Enter URLs")
    url_input = st.sidebar.text_area("Enter URLs (one per line)", "")

    if st.sidebar.button("Extract Main URLs"):
        # Split the input into a list of URLs
        url_list = url_input.strip().split('\n')

        # Extract main URLs
        main_urls = extract_main_url(url_list)

        # Display the main URLs
        if main_urls:
            st.header("Main URLs")
            for url in main_urls:
                st.write(url)
        else:
            st.warning("No valid URLs entered.")

if __name__ == "__main__":
    main()
