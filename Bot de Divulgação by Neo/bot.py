#By @Neo_Scr and GPT ;) , entre no nosso grupo de buscas https://t.me/NeoBuscasS2
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Token do seu bot do Telegram
TOKEN = 'TOKEN'

# ID do seu grupo no Telegram
CHAT_ID = CHAT ID

# Mensagem a ser enviada
MENSAGEM = " Para dar paragrafo escreva \n , exemplo : Compre no nosso site \n www.compreaqui.com ;) "

# Função assíncrona para enviar mensagem
async def enviar_mensagem(bot, chat_id, mensagem):
    try:
        await bot.send_message(chat_id=chat_id, text=mensagem)
    except TelegramError as e:
        print(f"Erro ao enviar mensagem: {e}")

async def main():
    # Criação do objeto Bot
    bot = Bot(token=TOKEN)

    # Loop para enviar mensagens a cada 10 minuto
    while True:
        await enviar_mensagem(bot, CHAT_ID, MENSAGEM)
        await asyncio.sleep(600)  # Aguarda 10 minuto antes do próximo envio, para alterar lembre-se 1 minuto = 60 segs

if __name__ == '__main__':
    asyncio.run(main())
