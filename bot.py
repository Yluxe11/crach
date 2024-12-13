from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ضع الـ API Token الخاص بك هنا
API_TOKEN = '8073238511:AAErQnp5OJNNMhPj-_-U2sUscsIe3_t2qcc'

# 1. تعريف أمر البدء
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا بك! أنا بوت Telegram جاهز للمساعدة. 😊")

# 2. تعريف أمر مخصص
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("الأوامر المتاحة:\n/start - بدء المحادثة\n/help - المساعدة")

# 3. وظيفة للتنبؤ (كمثال)
def predict(update: Update, context: CallbackContext) -> None:
    # جلب الأرقام التي أرسلها المستخدم
    if context.args:
        try:
            round_number = int(context.args[0])
            # هنا مكان مناداة النموذج لتوقع النتيجة (كمثال)
            prediction = f"x{round_number * 1.5:.2f}"  # مثال على توقع وهمي
            update.message.reply_text(f"التوقع للجولة {round_number}: {prediction}")
        except ValueError:
            update.message.reply_text("الرجاء إدخال رقم صحيح.")
    else:
        update.message.reply_text("الرجاء إرسال رقم الجولة بعد الأمر. مثال: /predict 101")

# 4. إعداد البوت
def main():
    # إعداد Updater
    updater = Updater(API_TOKEN)

    # إضافة الأوامر
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("predict", predict))

    # تشغيل البوت
    updater.start_polling()
    print("البوت يعمل الآن 🚀")
    updater.idle()

if __name__ == '__main__':
    main()
