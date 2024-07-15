revenues = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
prev_revenue = 0
for idx, revenue in enumerate(revenues):
    next_revenue = revenues[idx + 1] if idx < len(revenues) - 1 else 0
    prev_revenue = revenues[idx - 1] if idx > 0 else 0
    print(prev_revenue, revenue, next_revenue)


