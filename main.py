# 5630214889:AAHzg3LkEEYloZKEVRTUsujJhyPb9xNlQuc
# X-Api-Key':'JXbzGYR1GSxaqLTKppDPiw==E5CN6szQDeno2I4O

import telebot
import requests

# Create a Telebot instance with your API token
bot = telebot.TeleBot("5630214889:AAHzg3LkEEYloZKEVRTUsujJhyPb9xNlQuc")

# Define a function to handle incoming messages
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Define the welcome message
    welcome_message = "Hello! Welcome to my bot. You can use the /quote command to get a random quote, or use the optional argument to get a quote from a specific category.\n\nFor example, to get a quote about success, use the command /quote success.\n\nYou can also use the /categories command to see a list of available categories.\n\nEnjoy!"

    # Send the welcome message to the user
    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(commands=['developer'])
def handle_developer(message):
    # Define the message about yourself and your channel
    text = "I'm *Gemechis Chala*, the developer of this bot. You can find me on [Telegram](https://t.me/gladson1).\n\nYou can also check out my channel [MaalGaariin](https://t.me/maalgaariin) for more information about my projects."

    # Send the message with markdown formatting to the user
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


@bot.message_handler(commands=['categories'])
def handle_categories(message):
    # Define the categories message
    categories_message = "Categories list are: \n\nage\n alone\n amazing\n anger\n architecture\n art\n attitude\n beauty\n best\n birthday\n business\n car\n change\n communications\n computers\n cool\n courage\n dad\n dating\n death\n design\n dreams\n education\n environmental\n equality\n experience\n failure\n faith\n family\n famous\n fear\n fitness\n food\n forgiveness\n freedom\n friendship\n funny\n future\n god\n good\n government\n graduation\n great\n happiness\n health\n history\n home\n hope\n humor\n imagination\n inspirational\n intelligence\n jealousy\n knowledge\n leadership\n learning\n legal\n life\n love\n marriage\n medical\n men\n mom\n money\n morning\n movies\n success"

    # Send the categories message to the user
    bot.send_message(message.chat.id, categories_message)


@bot.message_handler(commands=['quote'])
def handle_quote(message):
    # Get the user's message text
    message_text = message.text

    # Parse the message text as a command
    command_parts = message_text.split()

    # If the command is "/quote", call the Ninja API and send the response to the user
    if command_parts[0] == "/quote":
        # If the user specified a category, use that category. Otherwise, request a random quote.
        if len(command_parts) > 1:
            category = command_parts[1]
        else:
            category = ""

        # Call the Ninja API using the category
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': 'JXbzGYR1GSxaqLTKppDPiw==E5CN6szQDeno2I4O'})

        # If the API call is successful, send the quote to the user
        if response.status_code == requests.codes.ok:
            # If the category doesn't exist, request a random quote instead
            if len(response.json()) == 0:
                api_url = 'https://api.api-ninjas.com/v1/quotes'
                response = requests.get(api_url, headers={'X-Api-Key': 'JXbzGYR1GSxaqLTKppDPiw==E5CN6szQDeno2I4O'})

            quote = response.json()[0]["quote"]
            author = response.json()[0]["author"]
            response_text = f'"{quote}"\n- {author}'
            bot.send_message(message.chat.id, response_text)
        else:
            bot.send_message(message.chat.id, "Error: {}".format(response.status_code))

# Start the bot
bot.polling()
