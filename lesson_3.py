import random, pandas, numpy

seed = "АДВИ_2023"
N = 1000

random.seed(seed)

index = []
for i in range (1, N + 1):
	index.append(i)
random.shuffle(index)

groups = []
for i in range (N):
	groups.append(random.choices(['группа_1', 'группа_2', 'группа_3',
								 'группа_4', 'группа_5']))

uniform = []
for i in range(N):
	uniform.append(random.randint(50, 100))

gauss_1 = []
for i in range(N):
	gauss_1.append(random.gauss(0, 1))
	
gauss_2 = []
for i in range(N):
	gauss_2.append(random.gauss(0, 12))

gauss_3 = []
for i in range(N):
	gauss_3.append(random.gauss(50, 9))
	
diag = pandas.DataFrame({"index":index, "groups":groups, "uniform":uniform, "gauss_1":gauss_1, "gauss_2":gauss_2, "gauss_3":gauss_3})
diag.index = index

diag.loc[diag["index"] % 121 == 0, "gauss_1"] = None
diag.loc[diag["gauss_2"].apply(lambda x: x - int(x) > 0.95), "gauss_2"] = None

diag["gauss_2"].fillna(diag["gauss_2"].mean(), inplace = True)
diag.dropna(subset = ["gauss_1"], inplace = True)

diag["gausss"] = (diag.gauss_1 + diag.gauss_2)/diag.gauss_3 

av = diag.gausss.quantile(0.7)
freq = diag['groups'].value_counts()
print(diag)






















