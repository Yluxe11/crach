import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ضع الـ API Token الخاص بك هنا
API_TOKEN = '8073238511:AAErQnp5OJNNMhPj-_-U2sUscsIe3_t2qcc'

# 1. تحميل البيانات وبناء النموذج
def train_model():
    try:
        # قراءة البيانات من الملف
        data = pd.read_csv("crash_data.csv")
        
        # تجهيز البيانات
        X = data[['Round']]  # المدخلات: رقم الجولة
        y = data['Multiplier']  # المخرجات: المضاعف
        
        # إنشاء النموذج
        model = LinearRegression()
        model.fit(X, y)
        print("تم تدريب النموذج بنجاح.")
        return model
    except Exception as e:
        print(f"خطأ أثناء تدريب النموذج: {e}")
        return None

# تدريب النموذج
model = train_model()

# 2. تعريف أوامر البوت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا بك في بوت التنبؤ بلعبة Crash! 🎮")

def predict(update: Update, context: CallbackContext) -> None:
    if not model:
        update.message.reply_text("النموذج غير جاهز. تأكد من صحة البيانات.")
        return
    
    # التحقق من إدخال المستخدم
    if context.args:
        try:
            round_number = int(context.args[0])
            prediction = model.predict([[round_number]])[0]
            update.message.reply_text(f"التوقع للجولة {round_number}: x{round(prediction, 2)}")
        except ValueError:
            update.message.reply_text("الرجاء إدخال رقم صحيح.")
        except Exception as e:
            update.message.reply_text(f"حدث خطأ أثناء التنبؤ: {e}")
    else:
        update.message.reply_text("الرجاء إرسال رقم الجولة بعد الأمر. مثال: /predict 101")

# 3. إعداد البوت
def main():
    updater = Updater(API_TOKEN)

    # إضافة الأوامر
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("predict", predict))

    # تشغيل البوت
    updater.start_polling()
    print("البوت يعمل الآن 🚀")
    updater.idle()

if __name__ == '__main__':
    main()
