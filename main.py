import telebot
import yt_dlp

TOKEN = '8156014824:AAHYwOpugQN3mf-vSOqy795zCwzwnwwxQW0'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me a YouTube link, and I'll download the video for you!")


@bot.message_handler(commands=['help'])
def send_msg(message):
    bot.reply_to(message , "to more inquery drop message to this username @zeeman1337")

@bot.message_handler(func=lambda msg: True)
def download_youtube_video(message):
    url = message.text.strip()
    
    bot.reply_to(message, "Downloading video... Please wait.")

    ydl_opts = {
        'format': 'best',
        
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
            
        with open(file_name, 'rb') as f:
            bot.send_video(message.chat.id, f)

    except Exception as e:
        bot.reply_to(message, f"❌ Failed: {e}")

bot.polling()
