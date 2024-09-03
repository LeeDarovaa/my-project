#Продолжение кода

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Что случилось?", callback_data='what_hepening')
        option_2_button = types.InlineKeyboardButton("Помогаю", callback_data='helpening')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)
        
    elif call.data in ['what_hepening', 'helpening']:
        if call.data == 'what_hepening':
            bot.send_message(call.message.chat.id, "📱 Я: Да, жду тогда")
            time.sleep(4)