import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.drawing.image import Image
import matplotlib.pyplot as plt

# Data Preparation
# Summary of Transactions
summary_data = {
    'Account Number': ['30224527 (Bear Daily)', '309491624 (Jeremy Rich)'],
    'Total to Crypto Platforms': [79245.26, 96128.67],
    'Total Disputed Transactions': [19750.00, 50150.00],
    'Total Amount': [130575.48, 214241.83]
}

# Detailed Bank Transactions
bank_transactions_data = [
    ["12-May-22", "Okcoin.com - Visa Purchase", 3874.75],
    ["15-May-22", "Okcoin.com - Visa Purchase", 1085.11],
    ["15-May-22", "Okcoin.com - Visa Purchase", 1085.11],
    ["16-May-22", "MOON PAY AUD - Visa Purchase", 4000.00]
]

# Detailed BTC Transactions
btc_transactions_data = [
    ["05-Mar-23", "1ABC23xyz...", 0.15],
    ["10-Mar-23", "1ABC23xyz...", 0.20],
    ["20-Apr-23", "1DEF45ghi...", 0.25]
]

# Convert to DataFrames
summary_df = pd.DataFrame(summary_data)
bank_transactions_df = pd.DataFrame(bank_transactions_data, columns=["Date", "Description", "Amount"])
btc_transactions_df = pd.DataFrame(btc_transactions_data, columns=["Date", "Wallet Address", "Amount BTC"])

# Create a Pandas Excel writer using Openpyxl as the engine
excel_path = 'Jeremy_Rich_Transactions.xlsx'
writer = pd.ExcelWriter(excel_path, engine='openpyxl')

# Write each DataFrame to a specific sheet
summary_df.to_excel(writer, sheet_name='Summary', index=False)
bank_transactions_df.to_excel(writer, sheet_name='Bank Transactions', index=False)
btc_transactions_df.to_excel(writer, sheet_name='BTC Transactions', index=False)

# Visual timeline using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(bank_transactions_df['Date'], bank_transactions_df['Amount'], marker='o', label='Bank Transactions')
plt.plot(btc_transactions_df['Date'], btc_transactions_df['Amount BTC'], marker='o', label='BTC Transactions', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Transaction Timeline')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
timeline_plot_path = 'timeline_plot.png'
plt.savefig(timeline_plot_path)

# Add a new sheet for the timeline and insert the plot
wb = writer.book
ws = wb.create_sheet('Timeline')
img = Image(timeline_plot_path)
ws.add_image(img, 'A1')

# Save the workbook
writer.save()
