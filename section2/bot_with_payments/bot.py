import telebot

bot = telebot.TeleBot('')
TOKEN_CLICK = ''
TOKEN_PAYME = ''
de

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_invoice(message.from_user.id,
                     title='Monthly subscription',
                     description='Activation gives access to movies',
                     provider_token=TOKEN_PAYME,
                     currency='uzs',
                     photo_url='https://i.postimg.cc/Y2bb0xmq/channels4-profile.jpg',
                     photo_width=300,  # 416
                     photo_height=234,  # 234
                     photo_size=416,  # 416
                     is_flexible=False,
                     prices=[telebot.types.LabeledPrice(
                         label='Subscription for 1 month', amount=3000000)],
                     start_parameter='one-month-subscription',
                     invoice_payload='test-invoice-payload', )


@bot.pre_checkout_query_handler(lambda query: True)
def pre_check(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    bot.send_message(message.from_user.id, 'Successful payment!')


bot.polling(non_stop=True)
