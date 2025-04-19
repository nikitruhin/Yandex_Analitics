import pandas as pd
data = pd.read_table(r"filename.tsv", sep='\t')
rating = dict()
for row in data.itertuples():
    if row.p1_votes > row.p2_votes:
        if row.p1 in rating:
            rating[row.p1]+=1
        else:
            rating[row.p1] = 1
    elif row.p1_votes < row.p2_votes :
        if row.p2 in rating:
            rating[row.p2]+=1
        else:
            rating[row.p2] = 1
sorted_rating =sorted(rating.items(), key=lambda item: item[1], reverse=True) 
print(sorted_rating)
