from data.prepare_data import load_and_prepare_data
df = load_and_prepare_data("data/support_emails.csv")
print(df.head())