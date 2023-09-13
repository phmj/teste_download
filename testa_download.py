import streamlit as st
import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

st.title("Download Excel File Example")

st.write("Here is your DataFrame:")
st.write(df)

# Create a button for downloading the Excel file
if st.button("Download Excel File"):
    # Set the filename for the Excel file
    excel_filename = "example_data.xlsx"

    # Create an Excel writer object with Pandas
    excel_writer = pd.ExcelWriter(excel_filename, engine='openpyxl')
    df.to_excel(excel_writer, index=False, sheet_name='Sheet1')
    excel_writer.save()

    # Display a download link for the Excel file
    #st.markdown(f"Download the Excel file [here](data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{excel_filename})")

