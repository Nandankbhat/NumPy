import numpy as np

np.random.seed(10)

#1
arr = np.arange(5, 101, 5).reshape(4, 5)
print("Reshaped 4x5 matrix:\n", arr)
print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)

#2
m = np.ones((5, 5), dtype=int)
m[1:4, 1:4] = 0
m[2, 2] = 9
print("Resulting 5x5 matrix:\n", m)


#3
prices = np.array([120, 250, 80, 450, 300])
quantities = np.array([4, 2, 10, 1, 3])
revenue = prices * quantities
print("Revenue per product:", revenue)
print("Total revenue:", revenue.sum())
print("Average revenue per product:", revenue.mean())
print("Index of highest-earning product:", np.argmax(revenue))

#4
rainfall = np.array([12.5, -1.0, 0.0, 18.2, -99.0, 5.4, 22.1, 0.0, -1.0, 14.8])
print("Valid readings:", rainfall[rainfall >= 0])
rainfall[rainfall < 0] = 0.0
print("Cleaned array:", rainfall)
print("Heavy rainfall days (>10 mm):", np.sum(rainfall > 10.0))

#5
np.random.seed(10)
scores5 = np.random.randint(20, 101, 12)
print("Original scores:", scores5)
status = np.where(scores5 >= 40, "Pass", "Fail")
print("Status:", status)
updated_scores = np.where(scores5 < 40, scores5 + 5, scores5)
print("Updated scores:", updated_scores)

#6
np.random.seed(10)
marks = np.random.randint(50, 101, (6, 4))
print("Marks matrix:\n", marks)
avg = np.round(marks.mean(axis=1), 2)
print("Student averages: ", avg)
print("Highest mark per subject:", marks.max(axis=0))
print("Students with average > 75:\n", marks[avg > 75])

#7
houses = np.array([[1200, 2, 55],
                   [1800, 3, 85],
                   [950, 1, 40],
                   [2400, 4, 120],
                   [1500, 3, 70]])
x_min, x_max = houses.min(axis=0), houses.max(axis=0)
norm = (houses - x_min) / (x_max - x_min)
print("Normalized array:\n", np.round(norm, 3))

#8
morning_sales = np.array([[15, 20], [10, 12], [25, 30]])
evening_sales = np.array([[18, 22], [14, 15], [20, 28]])
full_day = np.hstack((morning_sales, evening_sales))
print("3x4 full-day sales:\n", full_day)
full_day = np.vstack((full_day, [12, 16, 15, 19]))
print("Final 4x4 matrix:\n", full_day)
print("Column totals:", full_day.sum(axis=0))

#9
ratings = np.array([5, 4, 3, 5, 2, 5, 4, 1, 3, 5, 4, 4, 2, 5, 3, 4, 5, 1, 4, 3])
values, counts = np.unique(ratings, return_counts=True)
pct = np.round(counts / ratings.size * 100, 1)
lines = np.char.add(
    np.char.add(np.char.add("Rating ", values.astype(str)), ": "),
    np.char.add(np.char.add(counts.astype(str), " responses ("),
                np.char.add(pct.astype(str), "%)")))
print(*lines, sep="\n")

#10
emp_ids = np.array(["E101", "E102", "E103", "E104", "E105", "E106"])
scores = np.array([78, 92, 65, 88, 95, 71])
order = np.argsort(scores)[::-1]
sorted_ids, sorted_scores = emp_ids[order], scores[order]
print("Descending index order:", order)
print("Top 3 Employee IDs:", sorted_ids[:3])
print("Top 3 Scores:", sorted_scores[:3])