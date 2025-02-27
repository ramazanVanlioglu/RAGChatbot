#pip install python-telegram-bot

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import nest_asyncio

import rag_proje as rag
#rag yapısını dahil ediyoruz

nest_asyncio.apply()#-> Mevcut event loop'u düzeltir

#*bot api anahtarınızı buraya yapıştırın!

API_KEY="8047104316:AAHYTKPmjHD84-UZzqU8RWbp7E4x7i2oQCU"

#Gelen mesajları işleyen fonksiyon:
async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    user_message=update.message.text 
    chat_id=update.message.chat_id

    print(f"Gelen mesaj {user_message}")


    #Yanıtı kullanıcıya gönder
    response=rag.search(user_message)
    await context.bot.send_message(chat_id=chat_id, text=f"Merhaba! Sorunuz {user_message} alındı.")
    await context.bot.send_message(chat_id=chat_id,text=f"Cevap: {response}")

# Botu başlatan ana fonksiyon

async def main():
    # Application nesnesi oluştur:
    application=ApplicationBuilder().token(API_KEY).build()

    #Mesaj işleme handler'i ekle

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    #Botu çalıştır
    await application.run_polling()

import asyncio
#Uygulamayı başlat
asyncio.run(main())




