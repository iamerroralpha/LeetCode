#%%
values: [8,1,5,2,6]

for 0
score 0,1 = 8 + 1 + 0 - 1 
score 1,2 = 8 + 5 + 0 - 2

#%%
values = [8, 1, 5, 2, 6]
lenValues = len(values)
maxScore = 0
for i in range(lenValues):
    print(f"i : {i}")
    for j in range(i+1, lenValues):
        print(f"j: {j}")
        indScore = values[i] + values[j] + i - j
        print(f"indscore: {indScore}")
        if indScore > maxScore:
            maxScore = indScore
            print(f"we have a breakthrough with {i}, {j}")

print(maxScore)
# %%
