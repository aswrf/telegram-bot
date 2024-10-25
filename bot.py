from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging

# Thiết lập logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Handler cho lệnh /start
async def start(update, context):
    await update.message.reply_text('Xin chào! Gõ /getid để lấy ID của nhóm chat.')

# Handler cho lệnh /getid
async def get_id(update, context):
    chat_id = update.effective_chat.id
    chat_title = update.effective_chat.title
    await update.message.reply_text(f"ID của nhóm {chat_title} là: {chat_id}")

# Handler cho các tin nhắn thông thường
async def echo(update, context):
    print(f"Nhận được tin nhắn: {update.message.text}")
    print(f"Từ chat ID: {update.effective_chat.id}")

def main():
    # Thay YOUR_BOT_TOKEN bằng token thật của bot bạn
    TOKEN = "7980399039:AAHovYsLhT6P_9bfoDjSwLB72KivKm45zfk"
    
    print("Bot đang khởi động...")
    
    # Khởi tạo ứng dụng
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Thêm các handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("getid", get_id))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot đã sẵn sàng!")
    # Chạy bot
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()