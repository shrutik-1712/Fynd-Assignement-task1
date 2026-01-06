import pandas as pd

# Do this for each of your 3 files
file_names = ['results_v1.csv', 'results_v2.csv', 'results_v3.csv']

for file in file_names:
    df = pd.read_csv(file)
    
    total = len(df)
    # 1. Accuracy: Actual match
    correct = (df['actual'] == df['predicted']).sum()
    accuracy = (correct / total) * 100
    
    # 2. Validity: JSON worked
    valid_json = df['is_valid_json'].sum()
    validity_rate = (valid_json / total) * 100
    
    print(f"--- Results for {file} ---")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"JSON Validity: {validity_rate:.2f}%")
    print("-" * 30)