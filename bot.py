import telebot
from telebot import types  
import time

# Инициализация бота
bot = telebot.TeleBot('7087261239:AAFWiGpPwSqi5aB6HuqPjvyfoelRpsz9UTE')

@bot.message_handler(commands=['start'])
def start_game(message):
    chat_id = message.chat.id
    
    # Создание клавиатуры для выбора действия
    keyboard = types.InlineKeyboardMarkup()
    option_1_button = types.InlineKeyboardButton("Правила (рекомендую)", callback_data='rules')
    option_2_button = types.InlineKeyboardButton("Начать игру", callback_data='start_game')
    keyboard.add(option_1_button, option_2_button)
    
    bot.send_message(chat_id, "Привет! Выберите действие⬇️:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    chat_id = call.message.chat.id
    
    if call.data == 'start_game':
        bot.send_message(chat_id, "Эй, ты тут?")
        time.sleep(3)
        
        bot.send_message(chat_id, "Я нашел телефон здесь")
        time.sleep(4)
        
        bot.send_message(chat_id, "Тут единственный вбитый номер — твой")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Эм... Ты кто?", callback_data='option_1')
        option_2_button = types.InlineKeyboardButton("Откуда номер?!", callback_data='option_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(chat_id, "Выберите один из вариантов:", reply_markup=keyboard)
        
    elif call.data == 'rules':
        rules_text = (
            "Правила игры:\n"
            "1. Все действия в игре происходят при помощи нажатия на кнопки. Внимательно выбирай каждый шаг — исход событий зависит от твоего выбора.\n"
            "2. Если кнопка не прогружается сразу, не нужно нажимать её несколько раз. Это может быть связано с сервером. Просто дождись отклика программы.\n"
            "3. Будь внимателен: каждое твоё действие может повлиять на дальнейший ход игры. \n"
            "4. Желаем удачи! Пусть тебе сопутствует успех в этой непростой истории.\n"
            "P.S. Не забудь подписаться на наш официальный Telegram-канал для обновлений и новостей!"
        )
        bot.send_message(chat_id, rules_text)
        bot.send_message(call.message.chat.id, rules_text)

    elif call.data in ['option_1', 'option_2']:
        if call.data =='option_1':
            bot.send_message(call.message.chat.id, "📱 Я: Эм... Ты кто?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "знакомство давай отложим на потом")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "если быстро- меня Женя зовут")  
            time.sleep(3)
        
        elif call.data == 'option_2':
            bot.send_message(call.message.chat.id, "📱 Я: Откуда у тебя мой номер?!")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "я же сказал, этот номер вбит в телефон")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "как и что я без понятия")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "у меня из-за этого тоже возникают вопросы")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "какого фига твой номер вбит в этот телефон")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ладно, прости")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "я на нервах, мне жаль что я так резко реагирую")
            time.sleep(3)
    
        bot.send_message(call.message.chat.id, "скажи пожалуйста, ты хоть в какой стране?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Я тебя не знаю...", callback_data='closedness')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
       
    elif call.data == 'closedness':
        bot.send_message(call.message.chat.id, "📱 Я: Слушай, я тебя вообще не знаю")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "📱 Я: Давай если нужна помощь- достаточно моего присутсвия")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "да. согласен. прости")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "эм. ну если в двух словах")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "я не знаю где я, и я не помню почему я тут")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "но я в дерьме")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "в прямом и переносном смысле хах") 
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Инетересно но непонятно.", callback_data='interes_1')
        option_2_button = types.InlineKeyboardButton("Я тут причем?", callback_data='interes_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
       
    elif call.data in ['interes_1', 'interes_2']:
        if call.data == 'interes_1':    
            bot.send_message(call.message.chat.id, "📱 Я: Очень инетересно, но ничего непонятно.")
            time.sleep(3)
       
            bot.send_message(call.message.chat.id, "📱 Я: Ладно, слушаю.")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "спасибо!")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "ну вот да, я в дерьме в плане ситуации и видимо местонахождении")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "скорее всего я где-то на ферме") 
            time.sleep(3)
            
        elif call.data == 'interes_2':
            bot.send_message(call.message.chat.id, "📱 Я: Слушай, я тут причем вообще?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "я тебя прошу")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "сейчас вероятно идет вопрос о жизни и смерти")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "выслушай меня")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "все указывает на то, что меня похители хах")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ха-ха-ха", callback_data='lol') 
        option_2_button = types.InlineKeyboardButton("Чего?", callback_data='what')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
        
    elif call.data in ['lol', 'what']:
        if call.data == 'lol':
            bot.send_message(call.message.chat.id, "📱 Я: Ха-ха-ха. Очень смешно. Это какой-то пранк?) Где смеяться?")
            time.sleep(3)
        
            with open('Designer.jpeg', 'rb') as photo: 
                bot.send_photo(call.message.chat.id, photo, caption="а так смешно?")
                time.sleep(4)
            
                bot.send_message(call.message.chat.id, "я сам пытался убедить себя в том, что это шутка")
                time.sleep(3)
            
                bot.send_message(call.message.chat.id, "достаточно аргументов?")
                time.sleep(4)
        
        elif call.data == 'what':
            bot.send_message(call.message.chat.id, "📱 Я: Что?")
            time.sleep(3)
            
            with open('похищение.jpeg', 'rb') as photo: 
                bot.send_photo(call.message.chat.id, photo, caption="вот как-то так")
                time.sleep(4)
                
                bot.send_message(call.message.chat.id, "пытаюсь убедить себя что это не взаправду")
                time.sleep(3)
                
                bot.send_message(call.message.chat.id, "не получается")
                time.sleep(3)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ну допустим", callback_data='info') 
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
        
    elif call.data == 'info':
       bot.send_message(call.message.chat.id, "📱 Я: Ну допустим") 
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "📱 Я: Но! Это еще не значит что я тебе полностью верю!")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "я рад что хотя бы так")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "в любом случае спасибо!")
       time.sleep(5)
       
       bot.send_message(call.message.chat.id, "так, я очнулся в ангаре, пока осматривался нашел этот телефон")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "больше особо лишник движений не делал. голова разрывается") 
       time.sleep(3)
       
       keyboard = types.InlineKeyboardMarkup()
       option_1_button = types.InlineKeyboardButton("Ты давно уже там?", callback_data='quesion_1')
       option_2_button = types.InlineKeyboardButton("Ты ранен?", callback_data='question_2')
       keyboard.add(option_1_button, option_2_button)
       bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
    
    elif call.data in ['quesion_1', 'question_2']:
        
        if call.data == 'quesion_1': 
            bot.send_message(call.message.chat.id, "📱 Я: Ты давно уже там?")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "при памяти около полутора часа")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "а сколько уже являюсь близким другом коров- без понятия")
            time.sleep(4)
        
        elif call.data == 'question_2':
            bot.send_message(call.message.chat.id, "📱 Я: Ты ранен? С тобой все хорошо?")
            time.sleep(5)
            
            bot.send_message(call.message.chat.id, "не ранен, по крайней мере крови нигде не заметил")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "но может только головой ударился, раз мне это все кажется")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "а сейчас на самом деле просто сплю")
            time.sleep(4)            
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Оптимист", callback_data='humor')
        keyboard.add(option_1_button) 
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
        
    elif call.data == 'humor':
        bot.send_message(call.message.chat.id, "📱 Я: Не теряешь оптимизма")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "оптимизма и надежды")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тут связь ловит только в одном месте")         
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "поэтому мне нужно наверно осмотреться и я на какое-то время пропаду") 
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "только ты пожалуйста будь на связи")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ок. Осмотри ангар", callback_data='angar_1')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)
        
        
    elif call.data == 'angar_1':
        bot.send_message(call.message.chat.id, "📱 Я: Да, буду на связи. Наверно тебе стоит осмотреть ангар")
        time.sleep(2)
        
        bot.send_message(call.message.chat.id, "окей, я тоже так думаю")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тогда выйду на связь чуть позже")
        time.sleep(900)
        
        bot.send_message(call.message.chat.id, "я тут")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ворота закрыты, коровы мычат, загон в который меня закиунли- открыт")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "последний факт очень приятный на самом деле")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вообще ничего ?", callback_data='nothing')
        option_2_button = types.InlineKeyboardButton("Все осмотрел?", callback_data='real')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выберите один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['nothing', 'real']:
        
        if call.data == 'nothing':
            bot.send_message(call.message.chat.id, "📱 Я: Ты осмотрел все и вообще ничего не нашел? Это же ангар, должно быть хоть что-то")
            time.sleep(4)
        
        elif call.data == 'real':
            bot.send_message(call.message.chat.id, "📱 Я: Офигеть. Ты полностью осмотрел ангар?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "каждый угол обошел, и каждый открытый загон")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "ну я думаю не зря меня сюда закинули") 
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "все почистили, чтобы их гость не смог пораниться)))")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на самом деле есть тут какой-то сарай, но дверь закрыта")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "думаю что все, что могло было бы быть- там")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Не густо.", callback_data='mda')
        option_2_button = types.InlineKeyboardButton("Еще варианты?", callback_data='quesion_3')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выберите один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['mda', 'quesion_3']:
        if call.data == 'mda':
            bot.send_message(call.message.chat.id, "📱 Я: Не густо")     
            time.sleep(2)
        
            bot.send_message(call.message.chat.id, "согласен")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "но я удивлен что телефон нашел")
            time.sleep(3)
        
        elif call.data == 'quesion_3':
            bot.send_message(call.message.chat.id, "📱 Я: Еще варианты?")     
            time.sleep(2)
            
            bot.send_message(call.message.chat.id, "ну вариант покопаться в телефоне")     
            time.sleep(2)
            
            bot.send_message(call.message.chat.id, "который странным образом был забыт или брошен тут")     
            time.sleep(2)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да, странно", callback_data='strange')
        option_2_button = types.InlineKeyboardButton("Откуда он там?", callback_data='warum?')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['strange', 'warum?']:
        if call.data == 'strange':
            bot.send_message(call.message.chat.id, "📱 Я: Да, странно")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "ладно, как говорится- дареному коню в зубы не смотрят")
            time.sleep(4)
        
        elif call.data == 'warum?':
            bot.send_message(call.message.chat.id, "📱 Я: Откуда он там?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "лежал в соседнем загоне")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "в сене")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ладно")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "я сейчас пожалуй покапаюсь в настройках, может тут хоть какой-то аккаунт или карты работают")
        time.sleep(120)
        
        bot.send_message(call.message.chat.id, "есть две новости")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "к сожалению не хорошая и плохая, а плохая и очень плохая")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "с какой начать?)")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("С очень плохой", callback_data='very_bad')
        option_2_button = types.InlineKeyboardButton("С плохой", callback_data='bad')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['very_bad', 'bad']:
        
        if call.data == 'very_bad':    
            bot.send_message(call.message.chat.id, "📱 Я: Давай с очень плохой")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ну навигатора тут нет")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "даже намека на хоть какую-то геолокацию нет")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "а похая- никакого аккаунта тоже в телефоне нет")
            time.sleep(3)
        
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, "📱 Я: Давай с просто плохой")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "ну просто плохая- никакого аккаунта в телефоне нет")
            time.sleep(6)
            
            bot.send_message(call.message.chat.id, "очень плохая- навигатора, геолокации и прочее, что могло бы указать на мое местоположение")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "тупо нет")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "ну как тебе новости?)")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Подозрение", callback_data='podozrenie')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажми на вариант:", reply_markup=keyboard)
        
    elif call.data == 'podozrenie':
        bot.send_message(call.message.chat.id, "📱 Я: Как-то все это странно. Ниоткуда телефон, где вбит только мой номер (все еще считаю что это подозрительно)")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "📱 Я: Ты непонятно где, где явно все почистили перед твоим приходом")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "📱 Я: А телефон прям забыли")
        time.sleep(3)
                
        bot.send_message(call.message.chat.id, "да, не согласиться с тобой я тупо не могу")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну во всяком случае не выброшу же я его")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Осмотрись еще", callback_data='check')
        option_2_button = types.InlineKeyboardButton("Отдохни", callback_data='relax') 
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов :", reply_markup=keyboard)
        
    elif call.data in ['check', 'relax']:
        
        if call.data == 'relax':
            bot.send_message(call.message.chat.id, "📱 Я:  Думаю может тебе стоит отдохнуть. Непонятно что будет дальше, силы пригодятся")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "силы конечно нужны, но немонятно сколько у меня есть свободного времени")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "ладно, отдохну минут 5 и напишу тебе")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "спасибо за поддержку!")
            time.sleep(420)
            
        elif call.data == 'check':
        
            bot.send_message(call.message.chat.id, "📱 Я: Ты еще сено не осматривал, может хоть там что-то найдется")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "да, сейчас гляну")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу тогда позже")
            time.sleep(300)
        
        bot.send_message(call.message.chat.id, "ЕСТЬ!!!!")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Что?", callback_data='what_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажмите на вариант :", reply_markup=keyboard)
        
    elif call.data == 'what_2':
        bot.send_message(call.message.chat.id, "📱 Я: Что там?")
        time.sleep(3)
        
        with open('key.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="КЛЮЧ!!!!")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "выглядит как единственная надежда в моей жизни")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "как думаешь, с чего начать?")
            time.sleep(3)
            

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ворота", callback_data='gates')
        option_2_button = types.InlineKeyboardButton("Сарай", callback_data='barn')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data in ['barn', 'gates']:
        if call.data == 'gates':
            bot.send_message(call.message.chat.id, "📱 Я: Попробуй открыть ворота из ангара")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "окей, напишу тогда позже")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "спасибо тебе за помощь")
            time.sleep(120)
        
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "ворота не открываются, следовательно это ключ от сарая")
            time.sleep(4)
            
        elif call.data == 'barn':
            bot.send_message(call.message.chat.id, "📱 Я: Попробуй открыть сарай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "да, хорошо. тогда напишу тогда позже")
            time.sleep(2)
            
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(220)
            
            bot.send_message(call.message.chat.id, "ключ подошел")
            time.sleep(6)
        
        bot.send_message(call.message.chat.id, "я бы пошел сразу проверять все и смотреть, но за стеной какие-то шаги слышал")
        time.sleep(3)
    
        bot.send_message(call.message.chat.id, "поэтому решил перестраховаться и вернуться туда, где меня оставили")
        time.sleep(4)
       

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Хорошо", callback_data='good_idea_2')
        option_2_button = types.InlineKeyboardButton("Иди в сарай", callback_data='go')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)

    elif call.data == 'go':
        bot.send_message(call.message.chat.id, "📱 Я: Все равно иди проверь сарай")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ладно, попробую тихонько проверить")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу потом")
        time.sleep(215)
        
        bot.send_message(call.message.chat.id, "_Евгений пытался действовать тихо, но как по сюжету любых хоррор фильмов- в сарае упала лопата_", parse_mode='Markdown')
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "_Похититель услышал посторонние звуки и двинулся в ангар, где увидел убегающего Женю из сарая_", parse_mode='Markdown')
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "_Он погиб, так и не узнав причину своего похищения_", parse_mode='Markdown')
        time.sleep(7)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_good_idea = types.InlineKeyboardButton("К предыдущему выбору", callback_data='retry_good_idea_2')
        keyboard.add(retry_good_idea)


        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)

    elif call.data == 'retry_good_idea_2': 
        bot.send_message(call.message.chat.id, "Возвращаемся к предыдущему выбору.")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Хорошо", callback_data='good_idea_2')
        option_2_button = types.InlineKeyboardButton("Иди в сарай", callback_data='go')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
        
    elif call.data == 'good_idea_2':
        bot.send_message(call.message.chat.id, "📱 Я: Хорошее решение")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "давай может пока затишье перед бурей- хоть познакомимся")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Кто ты?", callback_data='who_u')
        option_2_button = types.InlineKeyboardButton("Иди отдыхай", callback_data='relax_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data in ['who_u', 'relax_2']:
        if call.data == 'relax_2':
            bot.send_message(call.message.chat.id, "📱 Я: Может стоит отдохнуть?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "оке, думаю минут 10 хватит")
            time.sleep(780)
            
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "наотдыхался")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "давай хоть о себе расскажу")
            time.sleep(5)
            
        
        elif call.data == 'who_u':
            bot.send_message(call.message.chat.id, "📱 Я: Давай. Кто ты?")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "хах")
            time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ну меня зовут Женя, мне 23, я студент ХАИ")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кредитов не набирал")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "врагов не имею")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "поэтому кто со мной решил так справиться- вообще без понятия")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "про тебя я пожалуй спрашивать не буду")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ибо неизвестно откуда этот телефон появился тут и какие будут последствия")
        time.sleep(3)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Правильно", callback_data='right')
        option_2_button = types.InlineKeyboardButton("Ага, спс", callback_data='m_ok')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard) 
        
    elif call.data in ['right', 'm_ok']:
        
        if call.data == 'right': 
            bot.send_message(call.message.chat.id, "📱 Я: Да, я думаю это правильное решение, спасибо")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "📱 Я: Не так давно ты очень интересовался моим местонахождением")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "м-да")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "это было тупо с моей стороны, прости")
            time.sleep(4)

        elif call.data == 'm_ok':
            bot.send_message(call.message.chat.id, "📱 Я: Ага, спс")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "да, согласен")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "сначала я был очень неаккуратный и импульсивный")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "я думаю можно меня понять")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "еще раз извини")
            time.sleep(5)
        
        bot.send_message(call.message.chat.id, "кстати забавный факт")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "заряд на телефоне соврешенно не изменяется")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "он изначально был с 74%, сколько времени прошло- все еще 74")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Скажешь модель?)", callback_data='heh')
        option_2_button = types.InlineKeyboardButton("Ну это хорошо", callback_data='good')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard) 
        
    elif call.data in ['heh', 'good']:
        
        if call.data == 'heh':
            bot.send_message(call.message.chat.id, "📱 Я: Ого, скажешь модель телефона?) Тоже гляну себе такой")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "nokia ахахах")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "такое ощущение что аккамуляторы не меняются, а просто переделывают под усовершенственные модели")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "но это к лучшему")
            time.sleep(5)
        
        elif call.data == 'good':
            bot.send_message(call.message.chat.id, "📱 Я: Ну это же хорошо, телефон сейчас главная вещь в твоем инвентаре")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "да, согласен")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ценим то, что хорошо")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "так, я не знаю что там с шагами")
        time.sleep(3)
                       
        bot.send_message(call.message.chat.id, "но вроде все тихо")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "и сколько времени у меня- я без понятия")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "пойду к сараю, гляну что там")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(300)
        
        bot.send_message(call.message.chat.id, "ку")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну если обобщить, то мы имеем")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "хлам и всякое, что может хоть как-то напоминать оружие")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "какой выбираете лот?)")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Оборона", callback_data='retry_guns')
        option_2_button = types.InlineKeyboardButton("Хлам", callback_data='retry_hlam')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай с оружием разберемся")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "вилы для сена, лопата, грабли, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твои предложения?")
        time.sleep(3) 
    
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вилы", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Грабли", callback_data='grabli')
        option_4_buttom = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_buttom)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard) 
   
    elif call.data == 'vily':
        bot.send_message(call.message.chat.id, "📱 Я: Бери вилы")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "окей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тогда я их пожалуй пока спрячу под сено, ибо хочу хоть немного перерыв сделать")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(90)
        
        with open('vily.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="и сверху зарою сеном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарыл возле себя, на случай если прийдется неожиданно обороняться")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да", callback_data='yes')
        option_2_button = types.InlineKeyboardButton("Так себе", callback_data='m_ne')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data == 'yes':
        
        bot.send_message(call.message.chat.id, "📱 Я: Да, в самый раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тогда я наверно отдохну немного")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "даже если кто-то зайдет- я с ним справлюсь")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на связи!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут это")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кто-то идет")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "и это уже не просто шаги за стеной, а уверенно к воротам")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "че делать???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Делай вид, что спишь", callback_data='sleep')
        option_2_button = types.InlineKeyboardButton("Нападай", callback_data='fight')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)

    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Делай вид что спишь, но будь на готове! У тебя рядом вилы, помни!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. да, рядом вилы")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потом")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_В момент, когда Евгений делал вид, что он спит - маньяк заметил отсутствие вил в сарае и сразу же двинулся к Жене._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Спрячься, подбери момент и нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, будем пробовать")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Произошла борьба за жизнь, он успел схватить вилы и напал на маньяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Но у похитителя было ружье, которым он воспользовался. Женя погиб, так и не разгадав тайну своего похищения._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Выбор оружия", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Выбор хлама", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай с оружием разберемся")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вилы для сена, лопата, грабли, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твои предложения?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вилы", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Грабли", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data == 'lopata':
        bot.send_message(call.message.chat.id, "📱 Я: Что насчет лопаты?")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "лопата так лопата")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тогда я их пожалуй пока спрячу под сено, ибо хочу хоть немного перерыв сделать")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(90)
        
        with open('lopata.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="и сверху зарою сеном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарыл возле себя, на случай если прийдется неожиданно обороняться")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да", callback_data='yes')
        option_2_button = types.InlineKeyboardButton("Так себе", callback_data='m_ne')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data == 'yes':
        
        bot.send_message(call.message.chat.id, "📱 Я: Да, в самый раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тогда я наверно отдохну немного")
        
        bot.send_message(call.message.chat.id, "даже если кто-то зайдет- я с ним справлюсь")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на связи!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут это")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кто-то идет")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "и это уже не просто шаги за стеной, а уверенно к воротам")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "че делать???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Делай вид что спишь", callback_data='sleep_2')
        option_2_button = types.InlineKeyboardButton("Спрячься и нападай", callback_data='fight_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Делай вид что спишь, но будь на готове! У тебя рядом лопата, помни!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. да, рядом лопата")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потом")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_В момент, когда Евгений делал вид, что он спит - маньяк заметил отсутствие вил в сарае и сразу же двинулся к Жене._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Спрячься, подбери момент и нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, будем пробовать")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Произошла борьба за жизнь, он успел схватить вилы и напал на маньяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Но у похитителя было ружье, которым он воспользовался. Женя погиб, так и не разгадав тайну своего похищения._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Выбор хлама", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Выбор оружия", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай с оружием разберемся")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вилы для сена, лопата, грабли, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твои предложения?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вилы", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Грабли", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data == 'grabli':
        bot.send_message(call.message.chat.id, "📱 Я: Что насчет грабель?")
        time.sleep(3) 
        bot.send_message(call.message.chat.id, "значит будут грабли")
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тогда я их пожалуй пока спрячу под сено, ибо хочу хоть немного перерыв сделать")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(90)
        
        with open('grabli.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="и сверху зарою сеном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарыл возле себя, на случай если прийдется неожиданно обороняться")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да", callback_data='yes_3')
        option_2_button = types.InlineKeyboardButton("Так себе", callback_data='m_ne_3')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data == 'yes_3':
        
        bot.send_message(call.message.chat.id, "📱 Я: Да, в самый раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тогда я наверно отдохну немного")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "даже если кто-то зайдет- я с ним справлюсь")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на связи!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут это")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кто-то идет")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "и это уже не просто шаги за стеной, а уверенно к воротам")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "че делать???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Делай вид что спишь", callback_data='sleep_3')
        option_2_button = types.InlineKeyboardButton("Спрячься и нападай", callback_data='fight_3')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Делай вид что спишь, но будь на готове! У тебя рядом грабли, помни!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. да, рядом грабли")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потом")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_В момент, когда Евгений делал вид, что он спит - маньяк заметил отсутствие вил в сарае и сразу же двинулся к Жене._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Спрячься, подбери момент и нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, будем пробовать")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Произошла борьба за жизнь, он успел схватить вилы и напал на маньяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Но у похитителя было ружье, которым он воспользовался. Женя погиб, так и не разгадав тайну своего похищения._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Выбор оружия", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Выбор хлама", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай с оружием разберемся")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вилы для сена, лопата, грабли, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твои предложения?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вилы", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Грабли", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data == 'tesak':
        bot.send_message(call.message.chat.id, "📱 Я: Что насчет тесака?")
        time.sleep(3) 
        bot.send_message(call.message.chat.id, "да, внушающая вещь")
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тогда его пожалуй пока спрячу под сено, ибо хочу хоть немного перерыв сделать")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(90)
        
        with open('tesak.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="и сверху зарою сеном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарыл возле себя, на случай если прийдется неожиданно обороняться")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да", callback_data='yes_4')
        option_2_button = types.InlineKeyboardButton("Так себе", callback_data='m_ne_4')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
    
    elif call.data == 'yes_4':
        
        bot.send_message(call.message.chat.id, "📱 Я: Да, в самый раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тогда я наверно отдохну немного")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "даже если кто-то зайдет- я с ним справлюсь")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на связи!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут это")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кто-то идет")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "и это уже не просто шаги за стеной, а уверенно к воротам")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "че делать???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Делай вид что спишь", callback_data='sleep_4')
        option_2_button = types.InlineKeyboardButton("Спрячься и нападай", callback_data='fight_4')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Делай вид что спишь, но будь на готове! У тебя рядом нож, помни!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. да, рядом нож")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потом")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_В момент, когда Евгений делал вид, что он спит - маньяк заметил отсутствие вил в сарае и сразу же двинулся к Жене._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Спрячься, подбери момент и нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, будем пробовать")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Произошла борьба за жизнь, он успел схватить вилы и напал на маньяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Но у похитителя было ружье, которым он воспользовался. Женя погиб, так и не разгадав тайну своего похищения._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Выбор оружия", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Выбор хлама", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)
        
        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)
        
    elif call.data == 'retry_hlam':
        bot.send_message(call.message.chat.id, "📱 Я: Давай в хламе покапаемся. Что конкретно там?")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "так, хлам у нас это")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "гвозди")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "веревка")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ведро")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кирпичи")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "лобзик")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "варианты?")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Гвозди", callback_data='gvozdi')
        option_2_button = types.InlineKeyboardButton("Лобзик", callback_data='lobzik')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard) 
    
    elif call.data in ['lobzik', 'gvozdi']:
        
        if call.data == 'lobzik':
            bot.send_message(call.message.chat.id, "📱 Я: Давай лобзик возьмешь")
            time.sleep(4)    
            
            bot.send_message(call.message.chat.id, "лобзик так лобзик, а зачем он мне сейчас?")
            time.sleep(4)   
            
            bot.send_message(call.message.chat.id, "нечего разрезать пока что хах")
            time.sleep(4)   
            
            bot.send_message(call.message.chat.id, "но ладно")
            time.sleep(4)   
    
        elif call.data == 'gvozdi':
            bot.send_message(call.message.chat.id, "📱 Я: Предлагаю сначала взять гвозди, вдруг пригодятся")
            time.sleep(3)     
        
            bot.send_message(call.message.chat.id, "оке")
            time.sleep(4)     
        
            bot.send_message(call.message.chat.id, "ну гвозди я и в карман могу положить")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "что еще?")
        time.sleep(3)
        
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Веревка", callback_data='verevka_2')
        option_2_button = types.InlineKeyboardButton("Ведро", callback_data='vedro_2')
        option_3_button = types.InlineKeyboardButton("Кирпичи", callback_data='kirpich_2')
        keyboard.add(option_1_button, option_2_button, option_3_button)

        bot.send_message(call.message.chat.id, "Выбери один из вариантов⬇️:", reply_markup=keyboard) 
    
    elif call.data in ['verevka_2', 'vedro_2', 'kirpich_2']:
        
        if call.data == 'verevka_2':
            bot.send_message(call.message.chat.id, "📱 Я: Веревку давай")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "веревка!")
            time.sleep(3)
        
        elif call.data == 'vedro_2':
            bot.send_message(call.message.chat.id, "📱 Я: А что если ведро взять?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ведро!")
            time.sleep(3)
            
        elif call.data == 'kirpich_2':
            bot.send_message(call.message.chat.id, "📱 Я: Слушай, может кирпичи взять?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "слушай, точно")
            time.sleep(3)
            
        bot.send_message(call.message.chat.id, "короче есть идея")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "берем ведро, утяжелаем его, благодаря веревке привязываем к воротам и делаем так, чтобы примерно ведро было посередине")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "если он зайдет- веревка сорвется и прямо на голову")
        time.sleep(4)               
        
        bot.send_message(call.message.chat.id, "убьет не убьет- все равно")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "но оглушит точно")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "только чем утяжелить можно?")
        time.sleep(4)     
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Кирпичи!", callback_data='kirpich_idea_1')
        option_2_button = types.InlineKeyboardButton("Молоко?", callback_data='moloko_1')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data == 'kirpich_idea_1':
        bot.send_message(call.message.chat.id, "📱 Я: Давай кирпичи. Сколько их там?")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "сейчас гляну")
        time.sleep(67)
        
        bot.send_message(call.message.chat.id, "три таких строительных кирпича")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну как раньше было модно покупать обои с кирпичем красным")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "вот такие же")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "ладно, сейчас буду делать эту конструкцию")
        time.sleep(240)
        
        with open('vedro+kirpich.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="вот как-то так")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "выглядит странно, надеюсь сработает")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "ладно, я пошел")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "пожелай мне удачи!")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Удачи!", callback_data='enjoi_1')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажми на вариант:", reply_markup=keyboard)
    
    elif call.data == 'enjoi_1':   
        bot.send_message(call.message.chat.id, "📱 Я: Давай, удачи!")
        time.sleep(510)
        
        bot.send_message(call.message.chat.id, "кто-то идет")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "занимаю позицию и будем ждать")
        time.sleep(900)
        
        bot.send_message(call.message.chat.id, "_Похититель зашел в ангар и на него свалилось ведро, подготовленное Женей_", parse_mode='Markdown')
        time.sleep(5)
            
        bot.send_message(call.message.chat.id, "_Маньяк получил серьезный удар, но тяжести было недостаточно._", parse_mode='Markdown')
        time.sleep(10)

        bot.send_message(call.message.chat.id, "_Разъеренный он двинулся к Жене._", parse_mode='Markdown')
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "_Евгений погиб, так и не разгадав причину его похищения._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_button = types.InlineKeyboardButton("Вернуться к выбору", callback_data='retry_kirpich_moloko')
        keyboard.add(retry_button)
        
        bot.send_message(call.message.chat.id, "Игра закончена. Хочешь вернуться к одному из предыдущих этапов?", reply_markup=keyboard)
        
    elif call.data == 'retry_kirpich_moloko':
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Кирпичи!", callback_data='kirpich_idea_2')
        option_2_button = types.InlineKeyboardButton("Молоко?", callback_data='moloko_2')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Выбери один из вариантов:", reply_markup=keyboard)
        
    elif call.data == 'moloko_2':
        bot.send_message(call.message.chat.id, "📱 Я: Слушай, ты умеешь доить коров?")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "я в городе живу, никогда с этим не сталкивался")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "подожди, а к чему этот вопрос?")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Для утяжеления", callback_data='moloko+1')        
        keyboard.add(option_1_button)
    
        bot.send_message(call.message.chat.id, "Нажмите на вариант:", reply_markup=keyboard)
        
    elif call.data == 'moloko+1':
        bot.send_message(call.message.chat.id, "📱 Я: Ты подоишь корову, благодаря чему тяжесть ведра будет приличная")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "ох...")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "как бы идея хорошая")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "но вот реализация конечно так себе")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "а вдруг она орать начнет?")
        time.sleep(7)
        
        bot.send_message(call.message.chat.id, "ладно, все бывает в первый раз")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "первое похищение, первое близкое знаковство с коровой")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "ну в хорошем смысле")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ладно, буду доить. напишу позже")
        time.sleep(2)
        
        with open('vedro+moloko.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="вот такая конструкция")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "сейчас буду устанавливать")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "ладно, я пошел")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "пожелай мне удачи!")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Удачи!", callback_data='enjoi_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажми на вариант:", reply_markup=keyboard)
    
    elif call.data == 'enjoi_2':   
        bot.send_message(call.message.chat.id, "📱 Я: Давай, удачи!")
        time.sleep(2)
        
        bot.send_message(call.message.chat.id, "так, ловушка джокера установлена")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "и ждать осталось немного")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "опять слышу шаги")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "думаю на этот раз они уже идут в ангар")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "напишу потом")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "я тут!!!!")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "мы его вырубили!!!!")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "вырубили суку!!!!!!!")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "так, че дальше делать?")
        time.sleep(4)
        
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Карманы", callback_data='karmany')
        option_2_button = types.InlineKeyboardButton("Сарай", callback_data='saray_2')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)

    elif call.data == 'saray_2':
        bot.send_message(call.message.chat.id, '📱 Я: Дуй в сарай')
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "_Ваш выбор повлиял на события в игре_", parse_mode='Markdown')
        time.sleep(5)    
        
        bot.send_message(call.message.chat.id, "окей, там как раз кучу всего осталось")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "так, я услышал что он начал как-то бухтеть")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "и взял то, что попалась просто сразу под руку")
        time.sleep(4)

        with open('нож в руке.jpeg', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption="вот")
            time.sleep(7)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Выходи", callback_data='go_away')
        keyboard.add(option_1_button)

        bot.send_message(call.message.chat.id, "Нажмите на вариант вариант:", reply_markup=keyboard)

    elif call.data == 'karmany':
        bot.send_message(call.message.chat.id, "📱 Я: Проверь его карманы")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "да, хорошо, проверю")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "я нашел связку ключей, один из них 100% от ворот но пока не знаю остальные от чего")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "ладно, когда выдйду за пределы ангара и гляну еще")
        time.sleep(5)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Сарай", callback_data='saray_3')
        option_2_button = types.InlineKeyboardButton("Выходи", callback_data='go_away')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)
        
    elif call.data == 'go_away':
        bot.send_message(call.message.chat.id, "📱 Я: Давай двигай оттуда уже, пока он не очнулся")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "да, хорошо")
        time.sleep(2)
        
        bot.send_message(call.message.chat.id, "напишу позже")
        time.sleep(2)
        
        bot.send_message(call.message.chat.id, "вышел")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "и связь лучше тут ловит")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ладно, пожалуй буду осматриваться")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "так, ну тут есть дом и стоит машина")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "куда первым делом двигаться?")
        time.sleep(2)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Дом", callback_data='house')
        option_2_button = types.InlineKeyboardButton("Машина", callback_data='car')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)

    elif call.data == 'saray_3':
        bot.send_message(call.message.chat.id, "📱 Я: Заскочи в сарай, нужно глянуть что там взять можно")
        time.sleep(5)

        bot.send_message(call.message.chat.id, "да, хорошая идея, там как раз кучу всего осталось")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "так, я услышал что он начал как-то бухтеть")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "и взял то, что попалась просто сразу под руку")
        time.sleep(4)

        with open('нож в руке.jpeg', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption="вот")
            time.sleep(7)

    
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Супер", callback_data='super_2')
        option_2_button = types.InlineKeyboardButton("Надо было другое", callback_data='another')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)

    elif call.data == 'super_2' or call.data == 'another':
        if call.data == 'super_2':
            bot.send_message(call.message.chat.id, "📱 Я:  Супер")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "да, думаю тоже неплохой вариант")
            time.sleep(3)

        elif call.data == 'another':
            bot.send_message(call.message.chat.id, "📱 Я: Надо было что-то другое")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "ну другое я уже не могу")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "не думаю что у меня много свободного времени")
            time.sleep(4)

        bot.send_message(call.message.chat.id, "ладно, я буду двигаться на выход и закрою ангар")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "надеюсь на улице связь будет лучше")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "напишу")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "закрыл ворота")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "и связь лучше тут ловит")
        time.sleep(3)
    
        bot.send_message(call.message.chat.id, "ладно, пожалуй буду осматриваться")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "так, ну тут есть дом и стоит машина")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "куда первым делом двигаться?")
        time.sleep(2)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Дом", callback_data='house')
        option_2_button = types.InlineKeyboardButton("Машина", callback_data='car')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)

    elif call.data in ['house', 'car']:
        if call.data == 'car':
            bot.send_message(call.message.chat.id, "📱 Я: Осмотри машину")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "оке, сейчас гляну")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "что и требовалось доказать- закрыто")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "ладно, тогда в дом пойду")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "напишу позже")
            time.sleep(4)
            
        elif call.data == 'house':
            bot.send_message(call.message.chat.id, "📱 Я: Давай сразу в дом иди, смотри что там ")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "оке, иду")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "напишу позже")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "так, ну я зашел")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "было открыто, но на самом деле это неудивительно")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "в такой жопе мира зачем закрывать")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Осмотрись", callback_data='what_see')
        option_2_button = types.InlineKeyboardButton("Никого не слышно?", callback_data='what_lisen')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)
        
    elif call.data in ['what_see', 'what_lisen']:
        if call.data == 'what_lisen':
            bot.send_message(call.message.chat.id, "📱 Я: Ничего не слышно?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "вроде тихо")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "но в любом случае если что-то и будет- я услышу")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "у меня тут слух х100 из-за адреналина")
            time.sleep(4)
            
        elif call.data == 'what_see':    
            bot.send_message(call.message.chat.id, "📱 Я: Что в доме видно? Есть что-то полезное?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "да, сейчас постараюсь осмотреться")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "свет и фонарик включать не буду, от луны достаточно света")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тогда осмотрюсь и напишу")
        time.sleep(4)
    
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Жду", callback_data='weit')
        option_2_button = types.InlineKeyboardButton("Ага", callback_data='mda_4')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Выберите вариант:", reply_markup=keyboard)
        
    elif call.data in ['weit', 'mda_4']:
        if call.data == 'weit':
            bot.send_message(call.message.chat.id, "📱 Я: Да, жду тогда")
            time.sleep(4)
            
        elif call.data == 'mda_4':
            bot.send_message(call.message.chat.id, "📱 Я: Ага, не торопись")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "это...")
        time.sleep(4)
            
        bot.send_message(call.message.chat.id, "помоги...")
        time.sleep(20)
        
        bot.send_message(
    call.message.chat.id,
    "_Вы дошли до конца первой части игры 'WHY AM I HERE'. Все ваши выборы в этой части повлияют на дальнейшие события игры. Следите за обновлениями в официальном телеграм-канале 'WHY AM I HERE|OFFICIAL'_",
    parse_mode='Markdown'
)
time.sleep(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        

def send_message_in_ukrainian(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    rules_button = types.InlineKeyboardButton("Правила (рекомендую)", callback_data='rules')
    start_button = types.InlineKeyboardButton("Розпочати гру", callback_data='start_game')
    keyboard.add(rules_button, start_button)
    bot.send_message(chat_id, "Привіт! Оберіть дію⬇️:", reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'start_game':        
        bot.send_message(call.message.chat.id, "є тут хтось?")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "я знайшов телефон тут")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "та єдиний доступний номер- цей")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("А ти хто?", callback_data='option_1')
        option_2_button = types.InlineKeyboardButton("Звідки номер?!", callback_data='option_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data == 'rules':
        rules_text = (
            "Правила гри:\n"
            "1. Всі дії в грі відбуваються за допомогою натискання на кнопки. Уважно вибирай кожен крок - результат подій залежить від твого вибору.\n"
            "2) Якщо кнопка не прогружається відразу, не потрібно натискати її кілька разів. Це може бути пов'язано із сервером. Просто дочекайся відгуку програми.\n"
            "3 Будь уважний: кожна твоя дія може вплинути на подальший хід гри. \n"
            "4. Бажаємо удачі! Нехай тебе супроводжує успіх у цій непростій історії.\n"
            
            "P.S. Не забудь підписатися на наш офіційний Telegram-канал для оновлень і новин!\n"
        )      
        
    elif call.data in ['option_1', 'option_2']:
        if call.data =='option_1':
            bot.send_message(call.message.chat.id, "📱 Я: Ти взагалі хто?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "Знайомство давай потім")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "якщо швидко, то мене Євген звати")  
            time.sleep(3)
        
        elif call.data == 'option_2':
            bot.send_message(call.message.chat.id, "📱 Я: Звідки в тебе мій номер взагалі?!")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "я ж сказав, цей номер вбитий у телефон")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "як і що я без поняття")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "у мене через це теж виникають запитання")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "якого чорта твій номер вбитий у цей телефон")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "гаразд, вибач")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "я на нервах, мені шкода що я так різко реагую")
            time.sleep(3)
    
        bot.send_message(call.message.chat.id, "скажи будь ласка, ти хоч у якій країні?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Я тебе не знаю...", callback_data='closedness')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
       
    elif call.data == 'closedness':
        bot.send_message(call.message.chat.id, "📱 Я: Слухай, я тебе взагалі не знаю")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "📱 Я: Давай якщо потрібна допомога - достатньо моєї присутності")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "так. згоден. вибач")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну якщо швидко ")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "я не знаю де я, і я не пам'ятаю чому я тут")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "але я у лайні")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "у прямому і переносному сенсі хах") 
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Цікаво, але незрозуміло.", callback_data='interes_1')
        option_2_button = types.InlineKeyboardButton("Я тут до чого?", callback_data='interes_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
       
    elif call.data in ['interes_1', 'interes_2']:
        if call.data == 'interes_1':    
            bot.send_message(call.message.chat.id, "📱 Я: Дуже цікаво, але нічого незрозуміло.")
            time.sleep(3)
       
            bot.send_message(call.message.chat.id, "📱 Я: Гаразд, слухаю.")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "дякую!")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "ну ось так, я в лайні як з ситуації та, мабуть, місцезнаходження")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "найімовірніше я десь на фермі") 
            time.sleep(3)
            
        elif call.data == 'interes_2':
            bot.send_message(call.message.chat.id, "📱 Я: Слухай, я тут до чого взагалі?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "я тебе прошу")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "зараз, імовірно, йде питання про життя і смерть")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "вислухай мене")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "усе вказує на те, що мене викрали хах")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ха-ха-ха", callback_data='lol') 
        option_2_button = types.InlineKeyboardButton("Що?", callback_data='what')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['lol', 'what']:
        if call.data == 'lol':
            bot.send_message(call.message.chat.id, "📱 Я: Ха-ха-ха. Дуже смішно. Це якийсь пранк?) Де сміятися?")
            time.sleep(3)
        
            with open('Designer.jpeg', 'rb') as photo: 
                bot.send_photo(call.message.chat.id, photo, caption="а так смішно?")
                time.sleep(4)
            
                bot.send_message(call.message.chat.id, "я сам намагався переконати себе в тому, що це жарт")
                time.sleep(3)
            
                bot.send_message(call.message.chat.id, "достатньо аргументів?")
                time.sleep(4)
        
        elif call.data == 'what':
            bot.send_message(call.message.chat.id, "📱 Я: Що?")
            time.sleep(3)
            
            with open('похищение.jpeg', 'rb') as photo: 
                bot.send_photo(call.message.chat.id, photo, caption="ось якось так")
                time.sleep(4)
                
                bot.send_message(call.message.chat.id, "намагаюся переконати себе що це не насправді")
                time.sleep(3)
                
                bot.send_message(call.message.chat.id, "не виходить")
                time.sleep(3)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ну припустимо", callback_data='info') 
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data == 'info':
       bot.send_message(call.message.chat.id, "📱 Я: Ну припустимо") 
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "📱 Я: Але це ще не означає, що я тобі повністю вірю!")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "я радий, що хоча б так")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "у будь-якому випадку дякую!")
       time.sleep(5)
       
       bot.send_message(call.message.chat.id, "так, я прокинувся в ангарі, поки оглядався знайшов цей телефон")
       time.sleep(3)
       
       bot.send_message(call.message.chat.id, "більше особливо зайвих рухів не робив. голова розривається") 
       time.sleep(3)
       
       keyboard = types.InlineKeyboardMarkup()
       option_1_button = types.InlineKeyboardButton("Ти давно вже там?", callback_data='quesion_1')
       option_2_button = types.InlineKeyboardButton("Ти поранений?", callback_data='question_2')
       keyboard.add(option_1_button, option_2_button)
       bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data in ['question_1', 'question_2']:
        
        if call.data == 'question_1': 
            bot.send_message(call.message.chat.id, "📱 Я: Ти давно вже там?")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "при пам'яті близько півтори години")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "а скільки вже є близьким другом корів - без поняття")
            time.sleep(4)
        
        elif call.data == 'question_2':
            bot.send_message(call.message.chat.id, "📱 Я: Ти поранений? З тобою все гаразд?")
            time.sleep(5)
            
            bot.send_message(call.message.chat.id, "не поранений, принаймні крові ніде не помітив")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "але може тільки головою вдарився, раз мені це все здається")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "а зараз насправді просто сплю")
            time.sleep(4)            
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Оптиміст", callback_data='humor')
        keyboard.add(option_1_button) 
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data == 'humor':
        bot.send_message(call.message.chat.id, "📱 Я: Не втрачаєш оптимізму")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "оптимізму та надії")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тут зв'язок ловить тільки в одному місці")         
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тому мені потрібно напевно озирнутися та я на якийсь час пропаду") 
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тільки ти будь ласка будь на зв'язку")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Гаразд. Оглянь ангар", callback_data='angar_1')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
        
    elif call.data == 'angar_1':
        bot.send_message(call.message.chat.id, "📱 Я: Так, буду на зв'язку. Напевно тобі варто оглянути ангар")
        time.sleep(2)
        
        bot.send_message(call.message.chat.id, "окей, я теж так думаю")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тоді вийду на зв'язок трохи пізніше")
        time.sleep(900)
        
        bot.send_message(call.message.chat.id, "я тут")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ворота зачинені, корови мукають, загін, у який мене закинули, - відкритий")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "останній факт дуже приємний насправді")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Взагалі нічого?", callback_data='nothing')
        option_2_button = types.InlineKeyboardButton("Все оглянув?", callback_data='real')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['nothing', 'real']:
        
        if call.data == 'nothing':
            bot.send_message(call.message.chat.id, "📱 Я: Ти оглянув усе і взагалі нічого не знайшов? Це ж ангар, має бути хоч щось")
            time.sleep(4)
        
        elif call.data == 'real':
            bot.send_message(call.message.chat.id, "📱 Я: Очманіти. Ти повністю оглянув ангар?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "кожен кут обійшов, і кожен відкритий загін")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "ну я думаю не дарма мене сюди закинули") 
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "все почистили, щоб їхній гість не зміг поранитися)))")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "насправді є тут якийсь сарай, але двері зачинені")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "думаю що все, що могло б бути - там")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Не густо.", callback_data='mda')
        option_2_button = types.InlineKeyboardButton("Ще варіанти?", callback_data='quesion_3')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['mda', 'quesion_3']:
        if call.data == 'mda':
            bot.send_message(call.message.chat.id, "📱 Я: Не густо")     
            time.sleep(2)
        
            bot.send_message(call.message.chat.id, "згоден")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "але я здивований, що телефон знайшов")
            time.sleep(3)
        
        elif call.data == 'quesion_3':
            bot.send_message(call.message.chat.id, "📱 Я: Ще варіанти?")     
            time.sleep(2)
            
            bot.send_message(call.message.chat.id, "ну варіант подивитись що в телефоні")     
            time.sleep(2)
            
            bot.send_message(call.message.chat.id, "який дивним чином був забутий або кинутий тут")     
            time.sleep(2)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Так, дивно", callback_data='strange')
        option_2_button = types.InlineKeyboardButton("Звідки він там?", callback_data='warum?')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['strange', 'warum?']:
        if call.data == 'strange':
            bot.send_message(call.message.chat.id, "📱 Я: Так, дивно")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "гаразд, як то кажуть - дарованому коню в зуби не дивляться")
            time.sleep(4)
        
        elif call.data == 'warum?':
            bot.send_message(call.message.chat.id, "📱 Я: Звідки він там?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "лежав у сусідній загороді")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "у сіні")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "гаразд")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "я зараз, мабуть, покопаюся в налаштуваннях, може тут хоч якийсь акаунт або карти працюють")
        time.sleep(120)
        
        bot.send_message(call.message.chat.id, "є дві новини")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "на жаль не хороша і погана, а погана і дуже погана")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "з якої почати?)")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("З дуже поганою", callback_data='very_bad')
        option_2_button = types.InlineKeyboardButton("З поганою", callback_data='bad')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['very_bad', 'bad']:
        
        if call.data == 'very_bad':    
            bot.send_message(call.message.chat.id, "📱 Я: Давай з дуже поганою")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ну навігатора тут немає")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "навіть натяку на хоч якусь геолокацію немає")
            time.sleep(5)
        
            bot.send_message(call.message.chat.id, "а погана - ніякого акаунта теж у телефоні немає")
            time.sleep(3)
        
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, "📱 Я: Давай з просто поганою")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "ну якщо просто погана - ніякого акаунта в телефоні немає")
            time.sleep(6)
            
            bot.send_message(call.message.chat.id, "дуже погана - навігатора, геолокації та інше, що могло б указати на моє місце розташування")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "тупо немає")
            time.sleep(4)
            
        bot.send_message(call.message.chat.id, "ну як тобі новини?)")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Підозра", callback_data='podozrenie')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data == 'podozrenie':
        bot.send_message(call.message.chat.id, "📱 Я: Якось усе це дивно. Нізвідки телефон, де вбитий тільки мій номер (усе ще вважаю, що це підозріло)")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "📱 Я: Ти незрозуміло де, де явно все почистили перед твоїм приходом")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "📱 Я: А телефон забули")
        time.sleep(3)
                
        bot.send_message(call.message.chat.id, "так, не погодитися з тобою я взагалі не можу")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну в усякому разі не викину ж я його")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Озирнися ще", callback_data='check')
        option_2_button = types.InlineKeyboardButton("Відпочинь", callback_data='relax') 
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['check', 'relax']:
        
        if call.data == 'relax':
            bot.send_message(call.message.chat.id, "📱 Я:  Думаю, може тобі варто відпочити. Незрозуміло що буде далі, сили знадобляться")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "сили, звісно, потрібні, але незрозуміло скільки в мене є вільного часу")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "гаразд, відпочину хвилин 5 і напишу тобі")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "дякую за підтримку!")
            time.sleep(420)
            
        elif call.data == 'check':
        
            bot.send_message(call.message.chat.id, "📱 Я: Ти ще сіно не оглядав, може хоч там щось знайдеться")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "так, зараз гляну")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу тоді пізніше")
            time.sleep(300)
        
        bot.send_message(call.message.chat.id, "Є!!!!")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Що?", callback_data='what_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data == 'what_2':
        bot.send_message(call.message.chat.id, "📱 Я: Що там?")
        time.sleep(3)
        
        with open('key.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="КЛЮЧ!!!!")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "виглядає як єдина надія в моєму житті")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "як думаєш, з чого почати?")
            time.sleep(3)
            

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Ворота", callback_data='gates')
        option_2_button = types.InlineKeyboardButton("Сарай", callback_data='barn')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data in ['barn', 'gates']:
        if call.data == 'gates':
            bot.send_message(call.message.chat.id, "📱 Я: Спробуй відкрити ворота з ангара")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "окей, напишу тоді пізніше")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "дякую ще раз за допомогу")
            time.sleep(120)
        
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "ворота не відчиняються, отже це ключ від сараю")
            time.sleep(4)
            
        elif call.data == 'barn':
            bot.send_message(call.message.chat.id, "📱 Я: Спробуй відкрити сарай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, добре. тоді напишу тоді пізніше")
            time.sleep(220)
            
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ключ підійшов")
            time.sleep(6)
        
        bot.send_message(call.message.chat.id, "я б пішов одразу перевіряти все і дивитися, але за стіною якісь кроки чув")
        time.sleep(3)
    
        bot.send_message(call.message.chat.id, "тому вирішив перестрахуватися і повернутися туди, де мене залишили")
        time.sleep(4)
       

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Добре", callback_data='good_idea_2')
        option_2_button = types.InlineKeyboardButton("Іди в сарай", callback_data='go')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)

    elif call.data == 'go':
        bot.send_message(call.message.chat.id, "📱 Я: Все одно йди перевір сарай")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "гаразд, спробую тихенько перевірити")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу потім")
        time.sleep(215)
        
        bot.send_message(call.message.chat.id, "_Євгеній намагався діяти тихо, але як за сюжетом будь-яких хоррор фільмів - у сараї впала лопата_", parse_mode='Markdown')
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "_Викрадач почув сторонні звуки і рушив до ангару, де побачив Женю, який тікав із сараю_", parse_mode='Markdown')
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "_Він загинув, так і не дізнавшись причину свого викрадення_", parse_mode='Markdown')
        time.sleep(7)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_good_idea = types.InlineKeyboardButton("До попереднього вибору", callback_data='retry_good_idea_2')
        keyboard.add(retry_good_idea)


        bot.send_message(call.message.chat.id, "Гру закінчено. Хочеш повернутися до одного з попередніх етапів?", reply_markup=keyboard)

    elif call.data == 'retry_good_idea_2': 
        bot.send_message(call.message.chat.id, "Повертаємося до попереднього вибору.")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Добре", callback_data='good_idea_2')
        option_2_button = types.InlineKeyboardButton("Іди в сарай", callback_data='go')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
        
    elif call.data == 'good_idea_2':
        bot.send_message(call.message.chat.id, "📱 Я: Хороше рішення")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "давай може поки затишшя перед бурею - хоч познайомимося")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Хто ти?", callback_data='who_u')
        option_2_button = types.InlineKeyboardButton("Відпочивай", callback_data='relax_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data in ['who_u', 'relax_2']:
        if call.data == 'relax_2':
            bot.send_message(call.message.chat.id, "📱 Я: Може варто відпочити?")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "оке, думаю хвилин 10 вистачить")
            time.sleep(780)
            
            bot.send_message(call.message.chat.id, "я тут")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "навідпочився")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "давай хоч про себе розповім")
            time.sleep(5)
            
        
        elif call.data == 'who_u':
            bot.send_message(call.message.chat.id, "📱 Я: Давай. Хто ти?")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "хах")
            time.sleep(4)
        
        bot.send_message(call.message.chat.id, "ну мене звуть Женя, мені 23, я студент ХАІ")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "кредитів не набирав")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ворогів не маю")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "тому хто зі мною вирішив так упоратися - взагалі без поняття")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "про тебе я мабуть питати не буду")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "бо невідомо звідки цей телефон з'явився тут і які будуть наслідки")
        time.sleep(3)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Правильно", callback_data='right')
        option_2_button = types.InlineKeyboardButton("Ага, дяк", callback_data='m_ok')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard) 
        
    elif call.data in ['right', 'm_ok']:
        
        if call.data == 'right': 
            bot.send_message(call.message.chat.id, "📱 Я: Так, я думаю це правильне рішення, дякую")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "📱 Я: Не так давно ти дуже цікавився моїм місцезнаходженням")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "так...")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "це було тупо з мого боку, вибач")
            time.sleep(4)

        elif call.data == 'm_ok':
            bot.send_message(call.message.chat.id, "📱 Я: Ага, дяк")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, згоден")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "спочатку я був дуже неакуратний та імпульсивний")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "я думаю можна мене зрозуміти")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "ще раз вибач")
            time.sleep(5)
        
        bot.send_message(call.message.chat.id, "до речі кумедний факт")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "заряд на телефоні зовсім не змінюється")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "він спочатку був із 74%, скільки часу минуло - все ще 74")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Скажеш модель?)", callback_data='heh')
        option_2_button = types.InlineKeyboardButton("Ну це добре", callback_data='good')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard) 
        
    elif call.data in ['heh', 'good']:
        if call.data == 'heh':
            bot.send_message(call.message.chat.id, "📱 Я: Ого, скажеш модель телефону?) Теж гляну собі такий")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "nokia ахахах")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "таке відчуття, що аккамулятори не змінюються, а просто переробляють під вдосконалені моделі")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "але це на краще")
            time.sleep(5)
        
        elif call.data == 'good':
            bot.send_message(call.message.chat.id, "📱 Я: Ну це ж добре, телефон зараз головна річ у твоєму інвентарі")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "так, згоден")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "цінуємо те, що добре")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "так, я не знаю що там із кроками")
        time.sleep(3)
                       
        bot.send_message(call.message.chat.id, "але начебто все тихо")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "і скільки часу в мене - я без поняття")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "піду до сараю, гляну що там")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(300)
        
        bot.send_message(call.message.chat.id, "ку")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну якщо узагальнити, то ми маємо")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "мотлох і всяке, що може хоч якось нагадувати зброю")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "який обираєте лот?)")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Оборона", callback_data='retry_guns')
        option_2_button = types.InlineKeyboardButton("Мотлох", callback_data='retry_hlam')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай зі зброєю розберемося")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "віли для сіна, лопата, граблі, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твої пропозиції?")
        time.sleep(3) 
    
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Віли", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Граблі", callback_data='grabli')
        option_4_buttom = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_buttom)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard) 
   
    elif call.data == 'vily':
        bot.send_message(call.message.chat.id, "📱 Я: Бери віли")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "окей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тТоді я їх, мабуть, поки сховаю під сіно, бо хочу хоч трохи перерву зробити")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(111)
        
        with open('vily.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="і зверху зарою сіном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарив біля себе, на випадок якщо доведеться несподівано оборонятися")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Так", callback_data='yes')
        option_2_button = types.InlineKeyboardButton("Ну таке", callback_data='m_ne')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data == 'yes':
        
        bot.send_message(call.message.chat.id, "📱 Я: Так, в самий раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тоді я напевно відпочину трохи")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "навіть якщо хтось зайде - я з ним упораюся")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на зв'язку!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут це")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "хтось іде")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "і це вже не просто кроки за стіною, а впевнено до воріт")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "що робити???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Роби вигляд, що спиш", callback_data='sleep')
        option_2_button = types.InlineKeyboardButton("Нападай", callback_data='fight')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)

    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Роби вигляд, що спиш, але будь напоготові! У тебе поруч вила, пам'ятай!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. так, поруч вила")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потім")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_У момент, коли Євген робив вигляд, що він спить - маніяк помітив відсутність вил у сараї й одразу ж рушив до Жені._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Сховайся, підбери момент і нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, будемо пробувати")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Відбулася боротьба за життя, він встиг схопити вила і напав на маніяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Але у викрадача була рушниця, якою він скористався. Женя загинув, так і не розгадавши таємницю свого викрадення._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Вибір зброї", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Вибір мотлоху", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Гру закінчено. Хочеш повернутися до одного з попередніх етапів?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай зі зброєю розберемося")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вила для сіна, лопата, граблі, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твої пропозиції?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вила", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Граблі", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data == 'lopata':
        bot.send_message(call.message.chat.id, "📱 Я: Що щодо лопати?")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "лопата так лопата")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тоді я їх, мабуть, поки сховаю під сіно, бо хочу хоч трохи перерву зробити")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(90)
        
        with open('lopata.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="і зверху зарою сіном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зарив біля себе, на випадок якщо доведеться несподівано оборонятися")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Так", callback_data='yes')
        option_2_button = types.InlineKeyboardButton("Ну таке", callback_data='m_ne')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
    
    elif call.data == 'yes':
        
        bot.send_message(call.message.chat.id, "📱 Я: Так, в самий раз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тоді я напевно відпочину трохи")
        
        bot.send_message(call.message.chat.id, "навіть якщо хтось зайде - я з ним упораюся")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на зв'язку!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут цей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "хтось іде")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "і це вже не просто кроки за стіною, а впевнено до воріт")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "що робити???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Роби вигляд, що спиш", callback_data='sleep_2')
        option_2_button = types.InlineKeyboardButton("Сховайся і нападай", callback_data='fight_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Роби вигляд, що спиш, але будь напоготові! У тебе поруч лопата, пам'ятай!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. так, поруч лопата")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потім")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_У момент, коли Євген робив вигляд, що він спить - маніяк помітив відсутність вил у сараї й одразу ж рушив до Жені._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Сховайся, підбери момент і нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, пробуватимемо")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Відбулася боротьба за життя, він встиг схопити вила і напав на маніяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Але у викрадача була рушниця, якою він скористався. Женя загинув, не розгадавши таємницю свого викрадення._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Вибір мотлоху", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Вибір зброї", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Гра закінчена. Хочеш повернутися до одного із попередніх етапів?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай зі зброєю розберемося")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "добреее")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вила для сіна, лопата, граблі, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твої пропозиції?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вила", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Граблі", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Вибери один із варіантів:", reply_markup=keyboard)
        
    elif call.data == 'grabli':
        bot.send_message(call.message.chat.id, "📱 Я: Може граблі?")
        time.sleep(3) 
        bot.send_message(call.message.chat.id, "значить будуть граблі")
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тоді я їх мабуть поки сховаю під сіно, бо хочу хоч трохи перерву зробити")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(90)
        
        with open('grabli.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="і зверху зарою сіном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "закопав біля себе, на випадок якщо доведеться несподівано оборонятися")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Так", callback_data='yes_3')
        option_2_button = types.InlineKeyboardButton("Так собі", callback_data='m_ne_3')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Вибери один із варіантів:", reply_markup=keyboard)
    
    elif call.data == 'yes_3':
        
        bot.send_message(call.message.chat.id, "📱 Я: Так, якраз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тоді я напевно відпочину трохи")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "навіть якщо хтось зайде- я з ним впораюся")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на зв'язку!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут це")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "хтось іде")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "і це вже не просто кроки за стіною, а впевнено до воріт")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "че робити???")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Роби вигляд, що спиш", callback_data='sleep_2')
        option_2_button = types.InlineKeyboardButton("Сховайся і нападай", callback_data='fight_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Роби вигляд, що спиш, але будь на готові! У тебе поряд граблі, пам'ятай!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. так, поруч граблі")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потім")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_У момент, коли Євген вдавав, що він спить - маніяк помітив відсутність грабель у сараї і відразу ж рушив до Жені._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Сховайся, підбери момент і нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, пробуватимемо")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Відбулася боротьба за життя, він встиг схопити граблі та напав на маніяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Але у викрадача була рушниця, якою він скористався. Женя загинув, не розгадавши таємницю свого викрадення._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Вибір мотлоху", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Вибір зброї", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Гра закінчена. Хочеш повернутися до одного із попередніх етапів?", reply_markup=keyboard)
        
    elif call.data == 'retry_guns':
        bot.send_message(call.message.chat.id, "📱 Я: Давай зі зброєю розберемося")
        time.sleep(3)     
        
        bot.send_message(call.message.chat.id, "добреее")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "вила для сіна, лопата, граблі, тесак")
        time.sleep(3) 
        
        bot.send_message(call.message.chat.id, "твої пропозиції?")
        time.sleep(3) 
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Вила", callback_data='vily')
        option_2_button = types.InlineKeyboardButton("Лопата", callback_data='lopata')
        option_3_button = types.InlineKeyboardButton("Граблі", callback_data='grabli')
        option_4_button = types.InlineKeyboardButton("Тесак", callback_data='tesak')        
        keyboard.add(option_1_button, option_2_button, option_3_button, option_4_button)
        
        bot.send_message(call.message.chat.id, "Вибери один із варіантів:", reply_markup=keyboard)
        
    elif call.data == 'tesak':
        bot.send_message(call.message.chat.id, "📱 Я: Тесак?")
        time.sleep(3) 
        bot.send_message(call.message.chat.id, "так, що вселяє річ")
        time.sleep(3)
        bot.send_message(call.message.chat.id, "тоді його мабуть поки сховаю під сіно, бо хочу хоч трохи перерву зробити")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(90)
        
        with open('tesak.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="і зверху зарою сіном")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "закопав біля себе, на випадок якщо доведеться несподівано оборонятися")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "норм?")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Да", callback_data='yes_4')
        option_2_button = types.InlineKeyboardButton("Таке", callback_data='m_ne_4')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Вибери один із варіантів:", reply_markup=keyboard)
    
    elif call.data == 'yes_4':
        
        bot.send_message(call.message.chat.id, "📱 Я: Так, якраз")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "супер")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "тоді я напевно відпочину трохи")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "навіть якщо хтось зайде- я з ним впораюся")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "на зв'язку!")
        time.sleep(300)
                    
        bot.send_message(call.message.chat.id, "тут це")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "хтось іде")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "і це вже не просто кроки за стіною, а впевнено до воріт")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "що робити?")
        time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Роби вигляд, що спиш", callback_data='sleep_2')
        option_2_button = types.InlineKeyboardButton("Сховайся і нападай", callback_data='fight_2')
        keyboard.add(option_1_button, option_2_button)
        bot.send_message(call.message.chat.id, "Виберіть варіанрт⬇️:", reply_markup=keyboard)
        
    elif call.data in ['sleep', 'fihgt']:
        if call.data == 'sleep':
            bot.send_message(call.message.chat.id, "📱 Я: Роби вигляд, що спиш, але будь на готові! У тебе поряд ніж, пам'ятай!")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "ок. так, поруч ніж")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "напишу потім")
            time.sleep(10)
        
            bot.send_message(call.message.chat.id, "_У момент, коли Євген вдавав, що він спить - маніяк помітив відсутність вил у сараї і відразу ж рушив до Жені._", parse_mode='Markdown')
            time.sleep(5)
            
        elif call.data == 'fight':
            bot.send_message(call.message.chat.id, "📱 Я: Сховайся, підбери момент і нападай")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "так, окей, пробуватимемо")
            time.sleep(3)

        bot.send_message(call.message.chat.id, "_Відбулася боротьба за життя, він встиг схопити ніж та напав на маніяка._", parse_mode='Markdown')
        time.sleep(5)

        bot.send_message(call.message.chat.id, "_Але у викрадача була рушниця, якою він скористався. Женя загинув, не розгадавши таємницю свого викрадення._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_guns_button = types.InlineKeyboardButton("Вибір мотлоху", callback_data='retry_guns')
        retry_hlam_button = types.InlineKeyboardButton("Вибір зброї", callback_data='retry_hlam')
        keyboard.add(retry_guns_button, retry_hlam_button)

        bot.send_message(call.message.chat.id, "Гра закінчена. Хочеш повернутися до одного із попередніх етапів?", reply_markup=keyboard)
        
        
    elif call.data == 'retry_hlam':
        bot.send_message(call.message.chat.id, "📱 Я: Давай у мотлоху покопаємося. Що конкретно там?")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "океей")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "так, мотлох у нас це")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "цвяхи")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "мотузка")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "відро")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "цеглини")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "лобзик")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "варіанти?")
        time.sleep(3)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Цвяхи", callback_data='gvozdi')
        option_2_button = types.InlineKeyboardButton("Лобзик", callback_data='lobzik')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Обери один із вариантов⬇️:", reply_markup=keyboard) 
    
    elif call.data in ['lobzik', 'gvozdi']:
        
        if call.data == 'lobzik':
            bot.send_message(call.message.chat.id, "📱 Я: Давай лобзик візьмеш")
            time.sleep(4)    
            
            bot.send_message(call.message.chat.id, "лобзик так лобзик, а навіщо він мені зараз?")
            time.sleep(4)   
            
            bot.send_message(call.message.chat.id, "нічого розрізати поки що хах")
            time.sleep(4)   
            
            bot.send_message(call.message.chat.id, "але гаразд")
            time.sleep(4)   
    
        elif call.data == 'gvozdi':
            bot.send_message(call.message.chat.id, "📱 Я: Пропоную спочатку взяти цвяхи, раптом знадобляться")
            time.sleep(3)     
        
            bot.send_message(call.message.chat.id, "оке")
            time.sleep(4)     
        
            bot.send_message(call.message.chat.id, "ну цвяхи я і в кишеню можу покласти")
            time.sleep(3)
        
        bot.send_message(call.message.chat.id, "що ще?")
        time.sleep(3)
        
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Мотузка", callback_data='verevka_2')
        option_2_button = types.InlineKeyboardButton("Відро", callback_data='vedro_2')
        option_3_button = types.InlineKeyboardButton("Цегла", callback_data='kirpich_2')
        keyboard.add(option_1_button, option_2_button, option_3_button)

        bot.send_message(call.message.chat.id, "Обери один із вариантов⬇️:", reply_markup=keyboard) 
    
    elif call.data in ['verevka_2', 'vedro_2', 'kirpich_2']:
        
        if call.data == 'verevka_2':
            bot.send_message(call.message.chat.id, "📱 Я: Мотузку давай")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "мотузка!")
            time.sleep(3)
        
        elif call.data == 'vedro_2':
            bot.send_message(call.message.chat.id, "📱 Я: А що як відро взяти?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "відро!")
            time.sleep(3)
            
        elif call.data == 'kirpich_2':
            bot.send_message(call.message.chat.id, "📱 Я: Слухай, може цеглу взяти?")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "слухай, точно")
            time.sleep(3)
            
        bot.send_message(call.message.chat.id, "є ідея")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "беремо відро, обважнюємо його, завдяки мотузці прив'язуємо до воріт і робимо так, щоб приблизно відро було посередині")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "якщо він зайде - мотузка зірветься і прямо на голову")
        time.sleep(4)               
        
        bot.send_message(call.message.chat.id, "вб'є не вб'є - все одно")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "але оглушить точно")
        time.sleep(4)     
        
        bot.send_message(call.message.chat.id, "тільки чим обважнити можна?")
        time.sleep(4)     
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Цеглини!", callback_data='kirpich_idea_1')
        option_2_button = types.InlineKeyboardButton("Молоко?", callback_data='moloko_1')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Обери один із варіантів:", reply_markup=keyboard)
        
    elif call.data == 'kirpich_idea_1':
        bot.send_message(call.message.chat.id, "📱 Я: Давай цеглу. Скільки їх там?")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "зараз гляну")
        time.sleep(67)
        
        bot.send_message(call.message.chat.id, "три такі будівельні цеглини")
        time.sleep(3)
        
        bot.send_message(call.message.chat.id, "ну як раніше було модно купувати шпалери з цеглою червоною")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "ось такі ж")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "гаразд, зараз буду робити цю конструкцію")
        time.sleep(240)
        
        with open('vedro+kirpich.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="ось якось так")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "виглядає дивно, сподіваюся спрацює")
            time.sleep(4)
            
            bot.send_message(call.message.chat.id, "гаразд, я пішов")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "побажай мені удачі!")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Успіхів!", callback_data='enjoi_1')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Нажми на вариант:", reply_markup=keyboard)
    
    elif call.data == 'enjoi_1':   
        bot.send_message(call.message.chat.id, "📱 Я: Давай, успіхів")
        time.sleep(510)
        
        bot.send_message(call.message.chat.id, "хтось іде")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "занимаю позицию и будем ждать")
        time.sleep(900)
        
        bot.send_message(call.message.chat.id, "_Викрадач зайшов в ангар і на нього звалилося відро, підготовлене Женею_", parse_mode='Markdown')
        time.sleep(5)
            
        bot.send_message(call.message.chat.id, "_Маніяк отримав серйозний удар, але тяжкості було недостатньо._", parse_mode='Markdown')
        time.sleep(10)

        bot.send_message(call.message.chat.id, "_Розлючений він рушив до Жені._", parse_mode='Markdown')
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "_Євген загинув, так і не розгадавши причину його викрадення._", parse_mode='Markdown')
        time.sleep(5)
        
        keyboard = types.InlineKeyboardMarkup()
        retry_button = types.InlineKeyboardButton("Повернутися до вибору", callback_data='retry_kirpich_moloko')
        keyboard.add(retry_button)
        
        bot.send_message(call.message.chat.id, "Гру закінчено. Хочеш повернутися до одного з попередніх етапів?", reply_markup=keyboard)
        
    elif call.data == 'retry_kirpich_moloko':
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Цеглини!", callback_data='kirpich_idea_2')
        option_2_button = types.InlineKeyboardButton("Молоко?", callback_data='moloko_2')
        keyboard.add(option_1_button, option_2_button)
        
        bot.send_message(call.message.chat.id, "Обери один із варіантів:", reply_markup=keyboard)
        
    elif call.data == 'moloko_2':
        bot.send_message(call.message.chat.id, "📱 Я: Слухай, ти вмієш доїти корів?")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "я в місті живу, ніколи з цим не стикався")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "почекай, а до чого це запитання?")
        time.sleep(4)
        
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Для обважнення", callback_data='moloko+1')        
        keyboard.add(option_1_button)
    
        bot.send_message(call.message.chat.id, "Натисніть на варіант:", reply_markup=keyboard)
        
    elif call.data == 'moloko+1':
        bot.send_message(call.message.chat.id, "📱 Я: Ти подоїш корову, завдяки чому вага відра буде пристойна")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "ох...")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "нібито ідея хороша")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "але ось реалізація звичайно так собі")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "а раптом вона кричати почне?")
        time.sleep(7)
        
        bot.send_message(call.message.chat.id, "гаразд, усе буває вперше")
        time.sleep(6)
        
        bot.send_message(call.message.chat.id, "перше викрадення, перше близьке знайомство з коровою")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "ну в хорошому сенсі")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "гаразд, буду доїти. напишу пізніше")
        time.sleep(930)
        
        with open('vedro+moloko.jpeg', 'rb') as photo: 
            bot.send_photo(call.message.chat.id, photo, caption="ось така конструкція")
            time.sleep(7)
            
            bot.send_message(call.message.chat.id, "зараз буду встановлювати")
            time.sleep(3)
        
            bot.send_message(call.message.chat.id, "гаразд, я пішов")
            time.sleep(3)
            
            bot.send_message(call.message.chat.id, "побажай мені успіху!")
            time.sleep(3)
            
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Успіхів!", callback_data='enjoi_2')
        keyboard.add(option_1_button)
        bot.send_message(call.message.chat.id, "Натисни на варіант:", reply_markup=keyboard)
    
    elif call.data == 'enjoi_2':   
        bot.send_message(call.message.chat.id, "📱 Я: Давай, успіхів!")
        time.sleep(400)
        
        bot.send_message(call.message.chat.id, "так, пастка джокера встановлена")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "і чекати залишилося небагато")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "знову чую кроки")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "думаю цього разу вони вже йдуть в ангар")
        time.sleep(4)
        
        bot.send_message(call.message.chat.id, "напишу потім")
        time.sleep(700)
        
        bot.send_message(call.message.chat.id, "я тут!!!!")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "ми його вирубили!!!!")
        time.sleep(5)

        bot.send_message(call.message.chat.id, "вирубили його!!!!!!!")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "так, що далі робити?")
        time.sleep(4)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Кишені", callback_data='karmany')
        option_2_button = types.InlineKeyboardButton("Сарай", callback_data='saray_2')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)

    elif call.data == 'saray_2':
        bot.send_message(call.message.chat.id, '📱 Я: Іди в сарай')
        time.sleep(5)
    
        bot.send_message(call.message.chat.id, "_Ваш вибір вплинув на події у грі_", parse_mode='Markdown')
        time.sleep(5)    
    
        bot.send_message(call.message.chat.id, "окей, там якраз купа всього залишилося")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "так, я почув, що він почав якось бурмотіти")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "і взяв те, що попалося під руку")
        time.sleep(4)

        with open('ніж у руці.jpeg', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption="ось")
            time.sleep(7)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Виходь", callback_data='go_away')
        keyboard.add(option_1_button)

        bot.send_message(call.message.chat.id, "Натисніть на варіант:", reply_markup=keyboard)

    elif call.data == 'karmany':
        bot.send_message(call.message.chat.id, "📱 Я: Перевір його кишені")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "так, добре, перевірю")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "я знайшов зв'язку ключів, один з них точно від воріт, але поки що не знаю, від чого інші")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "гаразд, коли вийду за межі ангару, подивлюся ще")
        time.sleep(5)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Сарай", callback_data='saray_3')
        option_2_button = types.InlineKeyboardButton("Виходь", callback_data='go_away')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)

    elif call.data == 'go_away':
        bot.send_message(call.message.chat.id, "📱 Я: Рухайся звідти, поки він не прийшов до тями")
        time.sleep(5)

        bot.send_message(call.message.chat.id, "так, добре")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "напишу пізніше")
        time.sleep(500)

        bot.send_message(call.message.chat.id, "вийшов")
        time.sleep(5)

        bot.send_message(call.message.chat.id, "і зв'язок краще тут ловить")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "гаразд, буду оглядатися")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "так, ну тут є будинок і стоїть машина")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "куди першим ділом рухатися?")
        time.sleep(4)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Будинок", callback_data='house')
        option_2_button = types.InlineKeyboardButton("Машина", callback_data='car')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)

    elif call.data == 'saray_3':
        bot.send_message(call.message.chat.id, "📱 Я: Забіжи в сарай, потрібно подивитися, що можна взяти")
        time.sleep(5)

        bot.send_message(call.message.chat.id, "так, гарна ідея, там якраз купа всього залишилася")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "так, я почув, що він почав бурмотіти")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "і взяв те, що потрапило під руку")
        time.sleep(4)

        with open('ніж у руці.jpeg', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption="ось")
            time.sleep(7)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Супер", callback_data='super_2')
        option_2_button = types.InlineKeyboardButton("Треба було інше", callback_data='another')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)

    elif call.data == 'super_2' or call.data == 'another':
        if call.data == 'super_2':
            bot.send_message(call.message.chat.id, "📱 Я: Супер")
            time.sleep(3)

            bot.send_message(call.message.chat.id, "так, думаю, теж непоганий варіант")
            time.sleep(3)

        elif call.data == 'another':
            bot.send_message(call.message.chat.id, "📱 Я: Треба було щось інше")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "ну інше я вже не можу взяти")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "не думаю, що у мене багато часу")
            time.sleep(4)

        bot.send_message(call.message.chat.id, "гаразд, я буду рухатися до виходу та зачиню ангар")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "сподіваюся, на вулиці зв'язок буде кращим")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "напишу")
        time.sleep(500)

        bot.send_message(call.message.chat.id, "зачинив ворота")
        time.sleep(2)

        bot.send_message(call.message.chat.id, "і зв'язок краще тут ловить")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "гаразд, буду оглядатися")
        time.sleep(180)

        bot.send_message(call.message.chat.id, "так, тут є будинок і стоїть машина")
        time.sleep(3)

        bot.send_message(call.message.chat.id, "куди першим ділом рухатися?")
        time.sleep(4)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Будинок", callback_data='house')
        option_2_button = types.InlineKeyboardButton("Машина", callback_data='car')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)

    elif call.data in ['house', 'car']:
        if call.data == 'car':
            bot.send_message(call.message.chat.id, "📱 Я: Оглянь машину")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "окей, зараз гляну")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "як і передбачалося - зачинено")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "гаразд, тоді піду до будинку")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "напишу пізніше")
            time.sleep(4)

        elif call.data == 'house':
            bot.send_message(call.message.chat.id, "📱 Я: Іди в будинок, подивися, що там")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "окей, іду")
            time.sleep(4)

            bot.send_message(call.message.chat.id, "напишу пізніше")
            time.sleep(280)

        bot.send_message(call.message.chat.id, "так, я зайшов")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "було відчинено, але це не дивно")
        time.sleep(4)

        bot.send_message(call.message.chat.id, "в такій глушині навіщо замикати")
        time.sleep(4)
    
        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Оглянься", callback_data='what_see')
        option_2_button = types.InlineKeyboardButton("Нікого не чутно?", callback_data='what_lisen')
        keyboard.add(option_1_button, option_2_button)

        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)
    
    elif call.data in ['what_see', 'what_lisen']:
        if call.data == 'what_lisen':
            bot.send_message(call.message.chat.id, "📱 Я: Нічого не чутно?")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "начебто тихо")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "але у будь-якому разі, якщо щось і буде – я почую")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "у мене тут слух х100 через адреналін")
            time.sleep(4)
        
        elif call.data == 'what_see':
            bot.send_message(call.message.chat.id, "📱 Я: Що видно в будинку? Є щось корисне?")
            time.sleep(4)
        
            bot.send_message(call.message.chat.id, "так, зараз спробую оглянутись")
            time.sleep(4)
        
        bot.send_message(call.message.chat.id, "світло та ліхтарик вмикати не буду, і так достатньо світла")
        time.sleep(4)
    
        bot.send_message(call.message.chat.id, "тоді оглянуся і напишу")
        time.sleep(4)

        keyboard = types.InlineKeyboardMarkup()
        option_1_button = types.InlineKeyboardButton("Чекаю", callback_data='weit')
        option_2_button = types.InlineKeyboardButton("Ага", callback_data='mda_4')
        keyboard.add(option_1_button, option_2_button)
    
        bot.send_message(call.message.chat.id, "Оберіть варіант:", reply_markup=keyboard)
    
    elif call.data in ['weit', 'mda_4']:
        if call.data == 'weit':
            bot.send_message(call.message.chat.id, "📱 Я: Так, чекаю тоді")
            time.sleep(960)
        
        elif call.data == 'mda_4':
            bot.send_message(call.message.chat.id, "📱 Я: Ага, не поспішай")
            time.sleep(960)
        
        bot.send_message(call.message.chat.id, "це...")
        time.sleep(5)
        
        bot.send_message(call.message.chat.id, "допоможи...")
        time.sleep(20)
    
    bot.send_message(
        call.message.chat.id,
        "_Ви дійшли до кінця першої частини гри 'WHY AM I HERE'. Усі ваші вибори в цій частині вплинуть на подальші події гри. Слідкуйте за оновленнями в офіційному телеграм-каналі 'WHY AM I HERE|OFFICIAL'_",
        parse_mode='Markdown'
    )






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




            
        
            
            
                    
        
        
            
            
            
        
        







                   
bot.polling(none_stop=True)
