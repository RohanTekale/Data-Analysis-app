import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import base64
from io import BytesIO

def main():
    st.title("CSV Data Analysis with Data Profiling")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Display basic information
        st.write("### Data Overview")
        st.write(df.head())
        st.write(f"### Data Shape: {df.shape}")
        st.write(f"### Data Columns: {df.columns.tolist()}")

        # Generate and save profile report
        profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
        
        # Save to a BytesIO object
        profile_html = profile.to_html()
        b64 = base64.b64encode(profile_html.encode()).decode()
        href = f'<a href="data:text/html;base64,{b64}" download="report.html">Download Profile Report</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Display HTML in Streamlit
        st.components.v1.html(profile_html, height=1000, scrolling=True)

if __name__ == "__main__":
    main()
