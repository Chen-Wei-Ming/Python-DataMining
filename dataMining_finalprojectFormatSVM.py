import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import dump_svmlight_file
# input file
df = pd.read_csv('data/DeathRecords_3000.csv')
# data setting
df = df.fillna(0)
# set data colums
# del df['Id'] , df['Education1989Revision'], df['Education2003Revision'] , df['EducationReportingFlag'] \
#     , df['MonthOfDeath'] , df['AgeType'] , df['AgeSubstitutionFlag'] , df['AgeRecode52'] , df['AgeRecode27'] , df['AgeRecode12'] \
#     , df['InfantAgeRecode22'] , df['CurrentDataYear']
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '1' if isinstance(Code , str) and Code[0] =="A" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '2' if isinstance(Code , str) and Code[0] =="B" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '3' if isinstance(Code , str) and Code[0] =="C" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '4' if isinstance(Code , str) and Code[0] =="D" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '5' if isinstance(Code , str) and Code[0] =="E" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '6' if isinstance(Code , str) and Code[0] =="F" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '7' if isinstance(Code , str) and Code[0] =="G" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '8' if isinstance(Code , str) and Code[0] =="H" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '9' if isinstance(Code , str) and Code[0] =="I" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '10' if isinstance(Code , str) and Code[0] =="J" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '11' if isinstance(Code , str) and Code[0] =="K" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '12' if isinstance(Code , str) and Code[0] =="L" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '13' if isinstance(Code , str) and Code[0] =="M" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '14' if isinstance(Code , str) and Code[0] =="N" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '15' if isinstance(Code , str) and Code[0] =="O" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '16' if isinstance(Code , str) and Code[0] =="P" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '17' if isinstance(Code , str) and Code[0] =="Q" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '18' if isinstance(Code , str) and Code[0] =="R" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '19' if isinstance(Code , str) and Code[0] =="S" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '19' if isinstance(Code , str) and Code[0] =="T" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '20' if isinstance(Code , str) and Code[0] =="V" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '20' if isinstance(Code , str) and Code[0] =="W" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '20' if isinstance(Code , str) and Code[0] =="X" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '20' if isinstance(Code , str) and Code[0] =="Y" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '21' if isinstance(Code , str) and Code[0] =="Z" else Code)
df['Icd10Code'] = df['Icd10Code'].apply(lambda Code : '22' if isinstance(Code , str) and Code[0] =="U" else Code)

attritube_colums = ['ResidentStatus','Sex','Age','MaritalStatus','InjuryAtWork','MannerOfDeath','Race']
attritube_df = df[list(attritube_colums)]
attritube_df = pd.get_dummies(attritube_df)
icdDummy = pd.get_dummies(df['Icd10Code'])
dump_svmlight_file(attritube_df,icdDummy['22'],"output/deathRecord_Icd10Code_22.txt",zero_based=True,multilabel=False)

