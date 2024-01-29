import pandas as pd

file_path = ("/Users/ryan/Documents/Datathon/catA_train.csv")
df = pd.read_csv(file_path)
#print(df.info())

#print(df.head(5))

columns_to_drop = ['LATITUDE', 'LONGITUDE','AccountID', 'Company','Industry','8-Digit SIC Code','8-Digit SIC Description','Entity Type','Parent Company','Parent Country','Company Description','Square Footage','Company Status (Active/Inactive)','Fiscal Year End','Global Ultimate Company','Global Ultimate Country','Domestic Ultimate Company']
df2 = df.drop(columns=columns_to_drop)
#print(df2.info())

df2 = df2.dropna(subset = ['Year Found'])
#print(df2.info())

df2 = pd.get_dummies(df2, columns=['Ownership Type'], prefix='Ownership Type')
df2 = pd.get_dummies(df2, columns=['Import/Export Status'], prefix='Import/Export Status')

#print(df2.info())

##CHECKING NUMBER OF DATAPOINTS FOR EACH CATEGORY##

category_ownership = {'Ownership Type_Non-Corporates': ['0', '1']}
category_breakdown = df2['Ownership Type_Non-Corporates'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Non-Corporates' column:")
#print(category_breakdown)

category_ownership = {'Ownership Type_Nonprofit': ['0', '1']}
category_breakdown = df2['Ownership Type_Nonprofit'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Nonprofit' column:")
#print(category_breakdown)

category_ownership = {'Ownership Type_Partnership': ['0', '1']}
category_breakdown = df2['Ownership Type_Partnership'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Partnership' column:")
#print(category_breakdown)

category_ownership = {'Ownership Type_Private': ['0', '1']}
category_breakdown = df2['Ownership Type_Private'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Private' column:")
#print(category_breakdown)

category_ownership = {'Ownership Type_Public': ['0', '1']}
category_breakdown = df2['Ownership Type_Public'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Public' column:")
#print(category_breakdown)

category_ownership = {'Ownership Type_Public Sector ': ['0', '1']}
category_breakdown = df2['Ownership Type_Public Sector'].value_counts()
# Display the breakdown
#print("\nBreakdown of unique values in the 'Ownership Type_Public Sector :")
#print(category_breakdown)

###########################################################################


#group into 1s and 0s
grouped_global = df2.groupby(by = "Is Global Ultimate")
index_global_1 = grouped_global.groups[1]
df2.loc[df2.index.isin(index_global_1), 'Is Domestic Ultimate'] = 0
#alter values in is domestic ultimate to 0
#print(df2)


#top3 largest SIC groupings: 6719, 8742, 7371
value_counts = df2['SIC Code'].value_counts()
#print(value_counts)

grouped_SIC = df2.groupby(by = "SIC Code")
index_SIC_1st = grouped_SIC.get_group(6719.0).index.tolist()
index_SIC_2nd = grouped_SIC.get_group(8742.0).index.tolist()
index_SIC_3rd = grouped_SIC.get_group(7371.0).index.tolist()
index_SIC_top3 = index_SIC_1st + index_SIC_2nd + index_SIC_3rd
index_SIC_all = set(df2.index)
index_SIC_others = list(index_SIC_all.difference(index_SIC_top3))

df2.loc[df2.index.isin(index_SIC_others), 'SIC Code'] = "Others"
#print(df2)


df2['SIC Code'] = df2['SIC Code'].astype(str)
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
label_encoder = LabelEncoder()
df2['SIC Code'] = label_encoder.fit_transform(df2['SIC Code'])
df2["SIC Code"].unique()
print(df2)


