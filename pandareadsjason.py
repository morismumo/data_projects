import pandas as pd
import pandas.io.json as pd_json

f = open('data.json', 'r')
data = pd_json.loads(f.read())
df = pd.json_normalize(data, record_path='records')


print('-'*30)
print(df.head(2).to_json())

print('-'*30)
print(df.head(2).to_json(orient='records'))