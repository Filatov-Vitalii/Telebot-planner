import telebot

token = "5266823542:AAHBnHj_MYhSlFwI-NbQPLHJ38NfEcLKPMU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.from_user.id, "Список команд - /info\n"
                                      "Запланировать задачу - /start\n"
                                      "\n"
                                      "Просмотр задач:\n"
                                      "   на понедельник - /monday\n"
                                      "   на вторник - /tuesday\n"
                                      "   на среду - /wednesday\n"
                                      "   на четверг - /thursday\n"
                                      "   на пятницу - /friday\n"
                                      "   на субботу - /saturday\n"
                                      "   на воскресенье - /sunday\n"
                                      "\n"
                                      "Просмотр всех планов на неделю - /show_all\n"
                                      "Удалить все запланированные задачи - /delete_all")


@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте! Я планировщик задач. "
                                      "Введите день недели, на который хотите запланировать задачу, или "
                                      "введите /info чтобы увидеть список команд")


monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []


#Удаление всех задач
@bot.message_handler(commands=["delete_all"])
def delete_all(message):
    monday.clear()
    tuesday.clear()
    wednesday.clear()
    thursday.clear()
    friday.clear()
    saturday.clear()
    sunday.clear()
    bot.send_message(message.from_user.id, "Все ваши задачи удалены")


#Просмотр списка задач
@bot.message_handler(commands=["monday"])
def view_monday(message):
    bot.send_message(message.from_user.id, "ПОНЕДЕЛЬНИК: ")
    for i in monday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if monday == []:
        bot.send_message(message.from_user.id, "(На понедельник задач нет)")

@bot.message_handler(commands=["tuesday"])
def view_tuesday(message):
    bot.send_message(message.from_user.id, "ВТОРНИК: ")
    for i in tuesday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if tuesday == []:
        bot.send_message(message.from_user.id, "(На вторник задач нет)")

@bot.message_handler(commands=["wednesday"])
def view_wednesday(message):
    bot.send_message(message.from_user.id, "СРЕДА: ")
    for i in wednesday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if wednesday == []:
        bot.send_message(message.from_user.id, "(На среду задач нет)")

@bot.message_handler(commands=["thursday"])
def view_thursday(message):
    bot.send_message(message.from_user.id, "ЧЕТВЕРГ: ")
    for i in thursday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if thursday == []:
        bot.send_message(message.from_user.id, "(На четверг задач нет)")

@bot.message_handler(commands=["friday"])
def view_friday(message):
    bot.send_message(message.from_user.id, "ПЯТНИЦА: ")
    for i in friday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if friday == []:
        bot.send_message(message.from_user.id, "(На пятницу задач нет)")

@bot.message_handler(commands=["saturday"])
def view_saturday(message):
    bot.send_message(message.from_user.id, "СУББОТА: ")
    for i in saturday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if saturday == []:
        bot.send_message(message.from_user.id, "(На субботу задач нет)")

@bot.message_handler(commands=["sunday"])
def view_sunday(message):
    bot.send_message(message.from_user.id, "ВОСКРЕСЕНЬЕ: ")
    for i in sunday:
        bot.send_message(message.from_user.id, ("- " + i.capitalize()))
    if sunday == []:
        bot.send_message(message.from_user.id, "(На воскресенье задач нет)")

@bot.message_handler(commands=["show_all"])
def view_all(message):
    try:
        view_monday(message)
        view_tuesday(message)
        view_wednesday(message)
        view_thursday(message)
        view_friday(message)
        view_saturday(message)
        view_sunday(message)
    except:
        bot.send_message(message.from_user.id, "Ошибка")


#Внесение новой задачи в существующий список
def monday_append(message):
    plan = message.text.capitalize().strip()
    monday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на понедельник. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def tuesday_append(message):
    plan = message.text.capitalize().strip()
    tuesday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на вторник. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def wednesday_append(message):
    plan = message.text.capitalize().strip()
    wednesday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на среду. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def thursday_append(message):
    plan = message.text.capitalize().strip()
    thursday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на четверг. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def friday_append(message):
    plan = message.text.capitalize().strip()
    friday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на пятницу. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def saturday_append(message):
    plan = message.text.capitalize().strip()
    saturday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на субботу. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")

def sunday_append(message):
    plan = message.text.capitalize().strip()
    sunday.append(plan)
    bot.send_message(message.from_user.id, "Записал эту задачу на воскресенье. Если вы хотите запланировать что-то ещё, "
                                      "выберите день недели")


if __name__ == "__main__":

#Выбор дня недели
    @bot.message_handler(content_types=["text"])
    def weekday_choose(message):
        chosen_weekday = message.text.capitalize().strip()
        if chosen_weekday == "Понедельник":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в понедельник")
            bot.register_next_step_handler(message, monday_append)
        elif chosen_weekday == "Вторник":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать во вторник")
            bot.register_next_step_handler(message, tuesday_append)
        elif chosen_weekday == "Среда":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в среду")
            bot.register_next_step_handler(message, wednesday_append)
        elif chosen_weekday == "Четверг":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в четверг")
            bot.register_next_step_handler(message, thursday_append)
        elif chosen_weekday == "Пятница":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в пятницу")
            bot.register_next_step_handler(message, friday_append)
        elif chosen_weekday == "Суббота":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в субботу")
            bot.register_next_step_handler(message, saturday_append)
        elif chosen_weekday == "Воскресенье":
            bot.send_message(message.from_user.id, "Опишите задачу, которую вам нужно сделать в воскресенье")
            bot.register_next_step_handler(message, sunday_append)
        else:
            bot.send_message(message.from_user.id, "Введите день недели или команду")


bot.infinity_polling()