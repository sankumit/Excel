import streamlit as st

# Title of the app
st.title('Excel Data Visualization Dashboard')

# File Upload
uploaded_file = st.file_uploader('Upload your Excel file', type=['xlsx'])

if uploaded_file is not None:
    # Read the file
    import pandas as pd
    df = pd.read_excel(uploaded_file)
    st.write('Dataframe:', df)

    # Column Mapping
    st.sidebar.header('Column Mapping')
    column_options = df.columns.tolist()
    x_axis = st.sidebar.selectbox('Select X-axis column', column_options)
    y_axis = st.sidebar.selectbox('Select Y-axis column', column_options)

    # Interactive Visualization
    st.subheader('Interactive Data Visualization')
    st.line_chart(df[[x_axis, y_axis]])

    # Report Export
    if st.button('Export Report'):
        report_filename = f'report_{uploaded_file.name}.csv'
        df.to_csv(report_filename, index=False)
        st.success(f'Report exported as {report_filename}')
