import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import matplotlib.pyplot as plt

# Data Preparation
# Summary Data
summary_data = {
    'Account Number': ['30224527 (Bear Daily)', '309491624 (Jeremy Rich)'],
    'Total to Crypto Platforms': [79245.26, 96128.67],
    'Total Disputed Transactions': [19750.00, 50150.00],
    'Total Amount': [130575.48, 214241.83]
}

# Detailed Bank Transactions
bank_transactions_data = [
    ["12-May-22", "Okcoin.com - Visa Purchase", -3874.75, "Crypto"],
    ["15-May-22", "Okcoin.com - Visa Purchase", -1085.11, "Crypto"],
    ["15-May-22", "Okcoin.com - Visa Purchase", -1085.11, "Crypto"],
    ["16-May-22", "MOON PAY AUD - Visa Purchase", -4000.00, "Crypto"],
    ["18-May-22", "HTTP //WWW.BINANCE.COM", -5000.00, "Crypto"],
    ["24-May-22", "BTC Markets Transfer", -1000.00, "Crypto"],
    ["02-Jun-22", "Jeremy BTC - Osko Payment", -1000.00, "Crypto"],
    ["13-Jun-22", "Binance - Visa Purchase", -3000.00, "Crypto"],
    ["26-Jun-22", "Jeremy BTC - Osko Payment", -1000.00, "Crypto"],
    ["10-Jul-22", "Coinbase - Visa Purchase", -2000.00, "Crypto"],
    ["15-Jul-22", "Coinbase - Visa Purchase", -1500.00, "Crypto"],
    ["20-Jul-22", "PayPal - Transfer", -1200.00, "Shopping"],
    ["25-Jul-22", "Bank Transfer to Savings", -5000.00, "Savings"],
    ["28-Jul-22", "ATM Withdrawal", -300.00, "Cash"],
    # Add more transactions as needed
]

# Disputed Transactions
disputed_transactions_data = [
    ["16-May-22", "MOON PAY AUD - Visa Purchase", -5000.00, "Jeremy Rich"],
    ["24-May-22", "Binance - Visa Purchase", -7500.00, "Jeremy Rich"],
    ["15-Jun-22", "Bitcoin Transfer", -3000.00, "Jeremy Rich"],
    ["20-Jul-22", "Bank Transfer to Savings", -5000.00, "Jeremy Rich"],
    ["15-Aug-22", "PayPal - Transfer", -2500.00, "Jeremy Rich"],
    # Add all relevant disputed transactions here
]

# Detailed BTC Transactions
btc_transactions_data = [
    ["05-Mar-23", "1ABC23xyz...", 0.15, "Transfer"],
    ["10-Mar-23", "1ABC23xyz...", 0.20, "Purchase"],
    ["20-Apr-23", "1DEF45ghi...", 0.25, "Sale"],
    ["05-May-23", "1GHI67jkl...", 0.10, "Transfer"],
    ["15-Jun-23", "1JKL89mno...", 0.30, "Purchase"],
    ["10-Jul-23", "1MNO12pqr...", 0.40, "Sale"],
    ["20-Jul-23", "1PQR34stu...", 0.50, "Purchase"],
    # Add more BTC transactions as needed
]

# Convert to DataFrames
summary_df = pd.DataFrame(summary_data)
bank_transactions_df = pd.DataFrame(bank_transactions_data, columns=["Date", "Description", "Amount", "Category"])
disputed_transactions_df = pd.DataFrame(disputed_transactions_data, columns=["Date", "Description", "Amount", "Account Holder"])
btc_transactions_df = pd.DataFrame(btc_transactions_data, columns=["Date", "Wallet Address", "Amount BTC", "Transaction Type"])

# Create a Pandas Excel writer using Openpyxl as the engine
excel_path = 'Jeremy_Rich_Transactions.xlsx'

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    # Write each DataFrame to a specific sheet
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    bank_transactions_df.to_excel(writer, sheet_name='Bank Transactions', index=False)
    disputed_transactions_df.to_excel(writer, sheet_name='Disputed Transactions', index=False)
    btc_transactions_df.to_excel(writer, sheet_name='BTC Transactions', index=False)

    workbook = writer.book

    # Visual timeline using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(bank_transactions_df['Date'], bank_transactions_df['Amount'], marker='o', label='Bank Transactions', color='blue')
    if "Amount BTC" in btc_transactions_df.columns:
        plt.plot(btc_transactions_df['Date'], btc_transactions_df['Amount BTC'], marker='o', label='BTC Transactions', linestyle='--', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Amount/BTC')
    plt.title('Transaction Timeline')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a file
    timeline_plot_path = 'timeline_plot.png'
    plt.savefig(timeline_plot_path)

    # Add a new sheet for the timeline and insert the plot
    ws = workbook.create_sheet('Timeline')
    img = Image(timeline_plot_path)
    ws.add_image(img, 'A1')

# End of the script
