from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import sqlite3

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


db = sqlite3.connect('rick_quotes.db')

raw_html = simple_get("https://rickandmorty.fandom.com/wiki/Pilot/Transcript")
html = BeautifulSoup(raw_html, 'html.parser')
text = html.select(".poem")[0].text
text2 = text.split('\n')

f = open('text.txt', 'w')
taco_falso = dict()
texto_falso = ''
for (index,item) in enumerate(text2):
    if(item.startswith('Rick')):
        question = text2[index-1][item.find(':') + 1:-1].strip()
        answer =  item[item.find(':') + 1 : - 1].strip()
        f.write(f'{question}\n{answer}')
        texto_falso += f'{question}\n{answer}\n'
f.close()
 ''''
# Inicializamos bot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot(
    'Terminal'
)
#print(help(bot))

#print()

trainer = ListTrainer(bot)
trainer.train(texto_falso.split('\n'))

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
'''