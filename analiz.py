import pandas as pd
df = pd.read_csv('GoogleApps.csv')
y = df['Reviews'].max()
x = df[df['Content Rating'] == 'Teen']['Size'].min()
print()