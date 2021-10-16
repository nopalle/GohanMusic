# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
from pyrogram import Client

from config import BOT_USERNAME as bu
from helpers.filters import command


@Client.on_message(command(["asupan", f"asupan@{bu}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("sabar coli dulu")


@Client.on_message(command(["wibu", f"wibu@{bu}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("...")


@Client.on_message(command(["chika", f"chika@{bu}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("sabar coli dulu")


@Client.on_message(command(["truth", f"truth@{bu}"]))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("...")


@Client.on_message(command(["dare", f"dare@{bu}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("...")


@Client.on_message(command(["lyrics", f"lyrics@{bu}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**hah nyari apa?**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text(f"🔎 **Lirik sedang dicari**")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit(
            f"**Lyrics tidak ditemukan.** \nCoba cari dengan judul lagu yang lebih jelas"
        )
