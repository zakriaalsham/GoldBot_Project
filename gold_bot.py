from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import requests
import schedule
import time

load_dotenv()
TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أنا بوت الذهب الذكي. استخدم /gold_now")

async def send_gold_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # محاكاة بيانات حية (سنستبدلها ببيانات حقيقية لاحقاً)
    price = 3385.50 + (time.localtime().tm_min % 10)  # سعر متغير كل دقيقة
    signal = "🟢 شراء عند 3380" if price < 3390 else "🔴 بيع عند 3420"
   
    # أخبار عاجلة (مثال)
    news_list = [
        "تسارع المفاوضات الفلسطينية - دعم للذهب",
        "تصعيد في تايوان - الذهب يرتفع 1.2%",
        "استقرار الأسواق - ذهب مستقر"
    ]
    news = news_list[time.localtime().tm_min % 3]
   
    await update.message.reply_text(
        f"【 📈 تحديث الذهب الفوري 】\n"
        f"🕒 الوقت: {time.strftime('%H:%M', time.localtime())}\n"
        f"💰 السعر: {price:.2f}$\n"
        f"📊 الإشارة: {signal}\n"
        f"🌍 الخبر: {news}"
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gold_now", send_gold_update))
    app.run_polling()