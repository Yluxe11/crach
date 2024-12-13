import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. تحميل البيانات
data = pd.read_csv("crash_data.csv")  # تأكد من وضع اسم الملف الصحيح

# عرض البيانات
print("بيانات اللعبة:")
print(data.head())

# 2. تجهيز المدخلات والمخرجات
X = data[['Round']]  # الجولات
y = data['Multiplier']  # المضاعف

# 3. تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. إنشاء النموذج
model = LinearRegression()

# تدريب النموذج
model.fit(X_train, y_train)

# 5. التنبؤ
y_pred = model.predict(X_test)

# 6. تقييم الأداء
mse = mean_squared_error(y_test, y_pred)
print(f"متوسط الخطأ: {mse:.2f}")

# 7. عرض النتائج
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Round')
plt.ylabel('Multiplier')
plt.title('Crash Multiplier Prediction')
plt.legend()
plt.show()

# 8. التنبؤ بالجولات المستقبلية
new_rounds = np.array([[101], [102], [103]])  # أمثلة على الجولات المستقبلية
predictions = model.predict(new_rounds)
for round_num, pred in zip(new_rounds.flatten(), predictions):
    print(f"التوقع للجولة {round_num}: x{pred:.2f}")
