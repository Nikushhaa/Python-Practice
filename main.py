import numpy as np
from sklearn.linear_model import LinearRegression

# მონაცემები (ფართობი კვ.მ-ში)
X = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)

# შესაბამისი ფასები
y = np.array([100000, 120000, 140000, 160000, 180000])

# ვქმნით მოდელს
model = LinearRegression()

# ვავარჯიშებთ
model.fit(X, y)

# ვაკეთებთ პროგნოზს
prediction = model.predict([[75]])

print("75 კვ.მ სახლის სავარაუდო ფასი არის:", prediction[0])