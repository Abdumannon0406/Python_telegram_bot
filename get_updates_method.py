import telegram

bot = telegram.Bot(token = "8794892081:AAFXck0imaaBYqiQ10V-rbERVuOBwjNJJJc")

updates = bot.getUpdates(offset = 335214824)

for update in updates:
    if update.edited_message !=None:
        
    # else:
    #     print(update.edited_message)
        print(update.edited_message)

# print(len(bot.getUpdates(offset = 335214824)))