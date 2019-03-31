from chatterbot import ChatBot
bot = ChatBot(
    'Terminal',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
)

bot.train('text.txt')
# TODO: save the bot for future usage :V
print('Type something to begin...')
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break