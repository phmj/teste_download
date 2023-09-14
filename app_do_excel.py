import streamlit as st
import pandas as pd
import io
#import xlsxwriter

#buffer = io.BytesIO()

# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
#df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})

st.write(df1)
#st.write(df2)

# ========
# Método 1
# ========

buffer = io.BytesIO()

# Create a Pandas Excel writer using XlsxWriter as the engine.
#with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:

    # Write each dataframe to a different worksheet.
    df1.to_excel(writer, sheet_name='Sheet1')
    #df2.to_excel(writer, sheet_name='Sheet2')

    # Close the Pandas Excel writer and output the Excel file to the buffer
    writer.save()

    st.download_button(
        label="Download Excel worksheets - Método 1",
        data=buffer,
        file_name="pandas_multiple.xlsx",
        mime="application/vnd.ms-excel"
    )

# ========
# Método 2
# ========

# Assuming 'data' is your DataFrame
data = df1.copy()
data.to_excel("output.xlsx", index=False)

if st.button("Download Excel File = Método 2"):
    with open("output.xlsx", "rb") as file:
        data = file.read()
        st.download_button(
            label="Click here to download",
            data=data,
            file_name="output.xlsx",
            key="excel-download",
        )


















