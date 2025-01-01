### @Samilben
### @Samilbots

# -*- coding: utf-8 -*-

# (c) @maybeslow (Github) | https://t.me/birsamil | @birsamil (Telegram)

# ==============================================================================
#
# Project: EtiketTaggerBot
# Copyright (C) 2021-2022 by maybeslow@Github, < https://github.com/maybeslow >.
#
# This file is part of < https://github.com/maybeslow/Tagger > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see <https://github.com/maybeslow >
#
# All rights reserved.
#
# ==============================================================================
#
# Proje: EtiketTaggerBot
# Telif Hakkı (C) 2021-2022 maybeslow@Github, <https://github.com/maybeslow>.
#
# Bu dosya <https://github.com/maybeslow/Tagger> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. <https://github.com/maybeslow/Tagger >
#
# Her hakkı saklıdır.
#
# ========================================================================


import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, log_qrup, startmesaj, qrupstart, komutlar, sahib, support, noadmin
import heroku3
import random
import asyncio
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from pyrogram import Client 
from pyrogram import filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from time import sleep
from telethon.sync import TelegramClient, events


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s' #"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


anlik_calisan = [] # bu botun çalıştığını anlamak için kullanılır
etiket_tagger = [] # etiket tagger için kullanılır


@client.on(events.NewMessage(pattern="^/cance$"))
async def cancel(event):
    global etiket_tagger


# etiket_tagger.remove(event.chat_id)


# etiket işlemini iptal eder
@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel(event):
    global etiket_tagger
    if event.chat_id in etiket_tagger:
        etiket_tagger.remove(event.chat_id)


  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"👋 Selam [{usr.first_name}](tg://user?id={usr.id}) "
     grup_link = f"https://t.me/{USERNAME}?startgroup=a"
     await client.send_message(log_qrup, f"ℹ️ **Yeni Kullanıcı -** \n {ad}")
     return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.url('🎉  beni gruba davet et  🎉', f'https://t.me/{USERNAME}?startgroup=a')],
                      [
                       Button.url('📚  komutlar ', f'https://t.me/kurtlar_sofrasi_oyun'), #komutların olduğu kanal
                       Button.url('👨‍💻  Sahip  ', f'https://t.me/kurucu_sahipp')], #sahibin telegram profil linki
                       [Button.url('📝  Kanal  ', f'https://t.me/kurtlar_sofrasi_oyun')] #Kanalın destek grubu vs
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")

# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"👋 Salam [{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.url('🎉  beni gruba davet et 🎉', f'https://t.me/{USERNAME}?startgroup=a')],
                      [Button.url("📚  komutlar ", f'https://t.me/kurtlar_sofrasi_oyun'), #komutların olduğu kanal
                       Button.url('👨‍💻  Sahib  ', f'https://t.me/kurucu_sahipp')] #sahibin telegram profil linki
                       [Button.url('📝  Kanal  ', f'https://t.me/kurtlar_sofrasi_oyun')] #Kanalın destek grubu vs
                    ),
                    link_preview=False)

#komutlar menüsünü butondan açmak için
@client.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.url('📣 Sohbet grubu  ', f'https://t.me/kurtlar_sofrasi_oyun'), #destek grubun linki
                      Button.url('📣 SAHİP ', f'https://t.me/kurucu_sahipp') #sahibin telegram profil linki
                      ],
                      [
                      Button.inline("<  𝖦𝖾𝗋𝗂  >", data="start"),
                      ]
                    ),
                    link_preview=False)

# 5 li etiketleme modulü
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("➻ eski mesajları göremiyorum ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("➻ Tağ üçün mesaj yazmadın ! ")
  else:
    return await event.respond("➻ etiket için bir sebep yazın ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, " 📢 üyeleri etiketleme işlemi başladı . . .",
                    buttons=(
                      [
                      Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ üyeleri etiketleme işlemi durduruldu. . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg} \n {usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# admin etiketleme modülü
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("➻ 𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("➻ Tağ etmək üçün səbəb yaz ! ")
  else:
    return await event.respond("➻ etiket islemi icin bir sebep yazın ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, " 📢 𝖠𝖽𝗆𝗂𝗇 etiket islemi başladı . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f" [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ 𝖠𝖽𝗆𝗂𝗇 etiket islemi durduruldu . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# tek tek etiketleme modülü
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tektag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("➻ Eski mesajları goremiyorum ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("➻ etiket için mesaj 𝖸𝖺𝗓𝗆𝖺𝖽ın ! ")
  else:
    return await event.respond("➻ etiket için bir neden yazınız  ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, " 📢 üyeleri etiketleme işlemi başladı . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f" [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ üyeleri etiketleme işlemi durduruldu . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# Emoji ile etiketleme modülü

anlik_calisan = []

tekli_calisan = []




emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡  👻 💀 👽 👾 🤖 🎃 😺 😸 😹 " \
        "😻 😼 😽 🙀 😿 😾 ❄️ 🌺 🌨 🌩 ⛈ 🌧 ☁️ ☀️ 🌈 🌪 ✨ 🌟 ☃️ 🪐 🌏 🌙 🌔 🌚 🌝 🕊 🦩 🦦 🌱 🌿 ☘ 🍂 🌹 🥀 🌾 " \
        "🌦 🍃 🎋🦓 🐅 🐈‍⬛ 🐄 🦄 🐇 🐁 🐷 🐶 🙈 🙊 🐻 🐼 🦊 🐮 🐍 🐊 🦨 🦔 🐒 🦣 🦘 🦥 🦦 🦇 🦍 🐥 🐦 🦜 🕊️ 🦤 🦢 " \
        "🦩 🦚 🦃 🐣 🐓 🐬 🦈 🐠 🐳 🦗 🪳 🐝 🐞 🦋 🐟 🕷️ 🦑".split(" ")

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("➻ eski mesajları goremiyorum! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("➻ etiket icin sebep yazmadın ! ")
  else:
    return await event.respond("➻ üyeleri etiketleme icin bir neden yaziniz ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, " 📢 üyeleri etiketleme işlemi başladı . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) , "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ üyeleri etiketleme işlemi durduruldu . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# söz ile etiketleme modülü

soz = (
'ᴜsʟᴜᴘ ᴋᴀʀᴀᴋᴛᴇʀɪᴅɪʀ ʙɪʀ ɪɴsᴀɴɪɴ', 
'ɪʏɪʏɪᴍ ᴅᴇsᴇᴍ ɪɴᴀɴᴀᴄᴀᴋ , ᴏ ᴋᴀᴅᴀʀ ʜᴀʙᴇʀsɪᴢ ʙᴇɴᴅᴇɴ', 
'ᴍᴇsᴀғᴇʟᴇʀ ᴜᴍʀᴜᴍᴅᴀ ᴅᴇɢɪʟ , ɪᴄɪᴍᴅᴇ ᴇɴ ɢᴜᴢᴇʟ ʏᴇʀᴅᴇsɪɴ',
'ʙɪʀ ᴍᴜᴄɪᴢᴇʏᴇ ɪʜᴛɪʏᴀᴄɪᴍ ᴠᴀʀᴅɪ , ʜᴀʏᴀᴛ sᴇɴɪ ᴋᴀʀsɪᴍᴀ ᴄɪᴋᴀʀᴅɪ', 
'ᴏʏʟᴇ ɢᴜᴢᴇʟ ʙᴀᴋᴛɪɴ ᴋɪ , ᴋᴀʟʙɪɴ ᴅᴇ ɢᴜʟᴜsᴜɴ ᴋᴀᴅᴀʀ ɢᴜᴢᴇʟ sᴀɴᴍɪsᴛɪᴍ', 
'ʜᴀʏᴀᴛ ɴᴇ ɢɪᴅᴇɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ , ɴᴇ ᴅᴇ ᴋᴀʏʙᴇᴛᴛɪɢɪɴ ᴢᴀᴍᴀɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ', 
'sᴇᴠᴍᴇᴋ ɪᴄɪɴ sᴇʙᴇᴘ ᴀʀᴀᴍᴀᴅɪᴍ , ʙɪʀ ᴛᴇᴋ sᴇsɪ ʏᴇᴛᴛɪ ᴋᴀʟʙɪᴍᴇ', 
'ᴍᴜᴛʟᴜʏᴜɴ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴇɴɪɴʟᴇ', 
'ʙᴇɴ ʜᴇᴘ sᴇᴠɪʟᴍᴇᴋ ɪsᴛᴇᴅɪɢɪᴍ ɢɪʙɪ sᴇᴠɪɴᴅɪᴍ', 
'ʙɪʀɪ ᴠᴀʀ ɴᴇ ᴏᴢʟᴇᴍᴇᴋᴛᴇɴ ʏᴏʀᴜʟᴅᴜᴍ ɴᴇ sᴇᴠᴍᴇᴋᴛᴇɴ', 
'ᴄᴏᴋ ᴢᴏʀ ʙᴇ sᴇɴɪ sᴇᴠᴍᴇʏᴇɴ ʙɪʀɪɴᴇ ᴀsɪᴋ ᴏʟᴍᴀᴋ', 
'ᴄᴏᴋ ᴏɴᴇᴍsɪᴢʟɪᴋ ɪsᴇ ʏᴀʀᴀᴍᴀᴅɪ ᴀʀᴛɪᴋ ʙᴏs ᴠᴇʀɪʏᴏʀᴜᴢ', 
'ʜᴇʀᴋᴇsɪɴ ʙɪʀ ɢᴇᴄᴍɪsɪ ᴠᴀʀ , ʙɪʀ ᴅᴇ ᴠᴀᴢɢᴇᴄᴍɪsɪ', 
'ᴀsɪᴋ ᴏʟᴍᴀᴋ ɢᴜᴢᴇʟ ʙɪʀ sᴇʏ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴀɴᴀ', 
'ᴀɴʟᴀʏᴀɴ ʏᴏᴋᴛᴜ , sᴜsᴍᴀʏɪ ᴛᴇʀᴄɪʜ ᴇᴛᴛɪᴍ', 
'sᴇɴ ᴄᴏᴋ sᴇᴠ ᴅᴇ ʙɪʀᴀᴋɪᴘ ɢɪᴅᴇɴ ʏᴀʀ ᴜᴛᴀɴsɪɴ', 
'ᴏ ɢɪᴛᴛɪᴋᴛᴇɴ sᴏɴʀᴀ ɢᴇᴄᴇᴍ ɢᴜɴᴅᴜᴢᴇ ʜᴀsʀᴇᴛ ᴋᴀʟᴅɪ', 
'ʜᴇʀ sᴇʏɪɴ ʙɪᴛᴛɪɢɪ ʏᴇʀᴅᴇ ʙᴇɴᴅᴇ ʙɪᴛᴛɪᴍ ᴅᴇɢɪsᴛɪɴ ᴅɪʏᴇɴʟᴇʀɪɴ ᴇsɪʀɪʏɪᴍ', 
'ɢᴜᴠᴇɴᴍᴇᴋ  sᴇᴠᴍᴇᴋᴛᴇɴ ᴅᴀʜᴀ ᴅᴇɢᴇʀʟɪ , ᴢᴀᴍᴀɴʟᴀ ᴀɴʟᴀʀsɪɴ', 
'ɪɴsᴀɴ ʙᴀᴢᴇɴ ʙᴜʏᴜᴋ ʜᴀʏᴀʟʟᴇʀɪɴɪ ᴋᴜᴄᴜᴋ ɪɴsᴀɴʟᴀʀʟᴀ ᴢɪʏᴀɴ ᴇᴅᴇʀ', 
'ᴋɪᴍsᴇ ᴋɪᴍsᴇʏɪ ᴋᴀʏʙᴇᴛᴍᴇᴢ  ɢɪᴅᴇɴ ʙᴀsᴋᴀsɪɴɪ ʙᴜʟᴜʀ , ᴋᴀʟᴀɴ ᴋᴇɴᴅɪɴɪ', 
'ɢᴜᴄʟᴜ ɢᴏʀᴜɴᴇʙɪʟɪʀɪᴍ ᴀᴍᴀ ɪɴᴀɴ ʙᴀɴᴀ ʏᴏʀɢᴜɴᴜᴍ', 
'ᴏᴍʀᴜɴᴜᴢᴜ sᴜsᴛᴜᴋʟᴀʀɪɴɪᴢɪ ᴅᴜʏᴀɴ  ʙɪʀɪʏʟᴇ ɢᴇᴄɪʀɪɴ', 
'ʜᴀʏᴀᴛ ɪʟᴇʀɪʏᴇ ʙᴀᴋɪʟᴀʀᴀᴋ ʏᴀsᴀɴɪʀ ɢᴇʀɪʏᴇ ʙᴀᴋᴀʀᴀᴋ ᴀɴʟᴀsɪʟɪʀ', 
'ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ sᴇʏ ᴇsᴋɪsɪ ɢɪʙɪ ᴅᴇɢɪʟ ʙᴜɴᴀ ʙᴇɴᴅᴇ ᴅᴀʜɪʟɪᴍ', 
'ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴᴇ ɢᴏɴᴜʟᴅᴇ ᴠᴇʀɪʟɪʀ ᴏᴍᴜʀᴅᴇ', 
'ʙɪʀ ᴄɪᴄᴇᴋʟᴇ ɢᴜʟᴇʀ ᴋᴀᴅɪɴ , ʙɪʀ ʟᴀғʟᴀ ʜᴜᴢᴜɴ', 
'ᴋᴀʟʙɪ ɢᴜᴢᴇʟ ᴏʟᴀɴ ɪɴsᴀɴɪɴ ɢᴏᴢᴜɴᴅᴇɴ ʏᴀs ᴇᴋsɪᴋ ᴏʟᴍᴀᴢᴍɪs', 
'ʜᴇʀ sᴇʏɪ ʙɪʟᴇɴ ᴅᴇɢɪʟ ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴ ɪɴsᴀɴʟᴀʀ ᴏʟsᴜɴ ʜᴀʏᴀᴛɪɴɪᴢᴅᴀ', 
'ᴍᴇsᴀғᴇ ɪʏɪᴅɪʀ ɴᴇ ʜᴀᴅᴅɪɴɪ ᴀsᴀɴ ᴏʟᴜʀ , ɴᴇ ᴅᴇ ᴄᴀɴɪɴɪ sɪᴋᴀɴ', 
'ʏᴜʀᴇɢɪᴍɪɴ ᴛᴀᴍ ᴏʀᴛᴀsɪɴᴅᴀ ʙᴜʏᴜᴋ ʙɪʀ ʏᴏʀɢᴜɴʟᴜᴋ ᴠᴀʀ', 
'ᴠᴇʀɪʟᴇɴ ᴅᴇɢᴇʀɪɴ ɴᴀɴᴋᴏʀᴜ ᴏʟᴍᴀʏɪɴ ɢᴇʀɪsɪ ʜᴀʟʟ ᴏʟᴜʀ', 
'ʜᴇᴍ ɢᴜᴄʟᴜ ᴏʟᴜᴘ ʜᴇᴍ ʜᴀssᴀs ᴋᴀʟᴘʟɪ ʙɪʀɪ ᴏʟᴍᴀᴋ ᴄᴏᴋ ᴢᴏʀ', 
'ᴍᴜʜᴛᴀᴄ ᴋᴀʟɪɴ ʏᴜʀᴇɢɪ ɢᴜᴢᴇʟ  ɪɴsᴀɴʟᴀʀᴀ', 
'ɪɴsᴀɴ ᴀɴʟᴀᴅɪɢɪ ᴠᴇ ᴀɴʟᴀsɪʟᴅɪɢɪ ɪɴsᴀɴᴅᴀ ᴄɪᴄᴇᴋ ᴀᴄᴀʀ', 
'ɪsᴛᴇʏᴇɴ ᴅᴀɢʟᴀʀɪ ᴀsᴀʀ ɪsᴛᴇᴍᴇʏᴇɴ ᴛᴜᴍsᴇɢɪ ʙɪʟᴇ ɢᴇᴄᴇᴍᴇᴢ', 
'ɪɴsᴀʟʟᴀʜ sᴀʙɪʀʟᴀ ʙᴇᴋʟᴇᴅɪɢɪɴ sᴇʏ ɪᴄɪɴ ʜᴀʏɪʀʟɪ ʙɪʀ ʜᴀʙᴇʀ ᴀʟɪʀsɪɴ', 
'ɪʏɪ ᴏʟᴀɴ ᴋᴀʏʙᴇᴛsᴇ ᴅᴇ ᴋᴀᴢᴀɴɪʀ', 
'ɢᴏɴʟᴜɴᴜᴢᴇ ᴀʟᴅɪɢɪɴɪᴢ , ɢᴏɴʟᴜɴᴜᴢᴜ ᴀʟᴍᴀʏɪ ʙɪʟsɪɴ', 
'ʏɪɴᴇ ʏɪʀᴛɪᴋ ᴄᴇʙɪᴍᴇ ᴋᴏʏᴍᴜsᴜᴍ ᴜᴍᴜᴅᴜᴍᴜ', 
'ᴏʟᴍᴇᴋ ʙɪʀ sᴇʏ ᴅᴇɢɪʟ ʏᴀsᴀᴍᴀᴋ ᴋᴏʀᴋᴜɴᴄ', 
'ɴᴇ ɪᴄɪᴍᴅᴇᴋɪ sᴏᴋᴀᴋʟᴀʀᴀ sɪɢᴀʙɪʟᴅɪᴍ ɴᴇ ᴅᴇ ᴅɪsᴀʀɪᴅᴀᴋɪ ᴅᴜɴʏᴀʏᴀ', 
'ɪɴsᴀɴ sᴇᴠɪʟᴍᴇᴋᴛᴇɴ ᴄᴏᴋ ᴀɴʟᴀsɪʟᴍᴀʏɪ ɪsᴛɪʏᴏʀᴅᴜ ʙᴇʟᴋɪ ᴅᴇ', 
'ᴇᴋᴍᴇᴋ ᴘᴀʜᴀʟɪ , ᴇᴍᴇᴋ ᴜᴄᴜᴢᴅᴜʀ', 
'sᴀᴠᴀsᴍᴀʏɪ ʙɪʀᴀᴋɪʏᴏʀᴜᴍ ʙᴜɴᴜ ᴠᴇᴅᴀ sᴀʏ'
) 


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("➻ Eski mesajları goremiyorum ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("➻ etiket için sebep yazmadın  ! ")
  else:
    return await event.respond("➻ etiket icin bir neden yazmadin ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, " 📢 uyeleri etiketleme başladıldı . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ üyeleri etiketleme işlemi durduruldu . . .",
                    buttons=(
                      [
                       Button.url('📝  KANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    
#########################

# bayrak ile etiketleme modülü
renk = " 🇿🇼 🇿🇲 🇿🇦 🇾🇹 🇾🇪 🇽🇰 🇼🇸 🇼🇫 🏴󠁧󠁢󠁷󠁬󠁳󠁿 🇻🇺 🇻🇳 🇻🇮 🇻🇬 🇻🇪 🇻🇨 🇻🇦 🇺🇿 🇺🇾 🇺🇸 🇺🇳 🇺🇬 🇺🇦 🇹🇿 🇹🇼 🇹🇻 🇹🇹 🇹🇷 🇹🇴 🇹🇳 🇹🇲 🇹🇱 🇹🇰 🇹🇭 🇹🇫 🇹🇨 🇹🇦 🇸🇿 🇸🇾 🇸🇽 " \
         " 🇸🇻 🇸🇸 🇸🇴 🇸🇲 🇸🇱 🇸🇰 🇸🇮 🇸🇭 🇸🇬 🇸🇪 🇸🇩 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🇸🇦 🇷🇼 🇷🇺 🇷🇸 🇷🇴 🇷🇪 🇶🇦 🇵🇾 🇵🇼 🇵🇹 🇵🇸 🇵🇷 🇵🇳 🇵🇲 🇵🇱 🇵🇰 🇵🇭 🇵🇫 🇵🇪 " \
         " 🇵🇦 🇴🇲 🇳🇿 🇳🇷 🇳🇵 🇳🇴 🇳🇱 🇳🇮 🇳🇬 🇳🇫 🇳🇪 🇳🇨 🇳🇦 🇲🇾 🇲🇽 🇲🇼 🇲🇻 🇲🇹 🇲🇷 🇲🇶 🇲🇵 🇲🇴 🇲🇳 🇲🇰 🇲🇭 🇲🇬 🇲🇪 🇲🇩 🇲🇨 🇲🇦 🇱🇾 🇱🇻 " \
         " 🇱🇺 🇱🇸 🇱🇷 🇱🇰 🇱🇮 🇱🇨 🇱🇧 🇱🇦 🇰🇿 🇰🇾 🇰🇼 🇰🇷 🇰🇵 🇰🇳 🇰🇲 🇰🇮 🇰🇭  🇰🇬 🇰🇪 🇯🇵 🇯🇴 🇯🇲 🇯🇪 🇮🇹 🇮🇸 🇮🇷 🇮🇶 🇮🇴 🇮🇳 🇮🇲 🇮🇱 🇮🇪 " \
         " 🇮🇩 🇮🇨 🇭🇺 🇭🇹 🇭🇷 🇭🇳 🇭🇰 🇬🇺 🇬🇹 🇬🇸 🇬🇷 🇬🇶 🇬🇵 🇬🇲 🇬🇱 🇬🇮 🇬🇬 🇬🇪 🇬🇧 🇬🇦 🇫🇷 🇫🇴 🇫🇲 🇫🇰 🇫🇮 🇪🇺 🇪🇸 🇪🇷 🇪🇭 🇪🇪 " \
         " 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇪🇨 🇩🇿 🇩🇴 🇩🇲 🇩🇰 🇩🇯 🇩🇪 🇨🇿 🇨🇾 🇨🇽 🇨🇼 🇨🇻 🇨🇺 🇨🇷 🇨🇭 🇨🇦 🇦🇿 " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def rtag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**➻ Eski mesajları goremiyorum !**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**➻ etiket icin sebep yazmadın !**")
  else:
    return await event.respond("**➻ etiketlemek için bir sebep yazın!**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ üyeleri etiketleyin . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ üyeleri etiketleme işlemi durduruldu ...",
                    buttons=(
                      [
                       Button.url('📝  𝖪ANAL  📝', f'https://t.me/kurtlar_sofrasi_oyun')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


### Eros Oku ###


@client.on(events.NewMessage(pattern='/eros'))
async def eros_oku(event):
    users = []
    async for user in client.iter_participants(event.chat_id):
        if not user.bot and not user.deleted and not user.is_self:
            users.append(user)

    if len(users) < 2:
        return
    
    first_user, second_user = random.sample(users, 2)
    first_user_md_mention = f'**[{first_user.first_name}](tg://user?id={first_user.id})**'
    second_user_md_mention = f'**[{second_user.first_name}](tg://user?id={second_user.id})**'
    
    response = (
        f"**Eros'un oku atıldı.💘**\n**Aşıklar:**\n\n"
        f"{first_user_md_mention} 💞 {second_user_md_mention} \n`Uyumluluk oranı: %{random.randint(0, 100)}`"
    )
    
    await event.respond(response, parse_mode="Markdown")
client.run_until_disconnected()


print(">> Bot çalışmaktadir merak etme 🚀 @kurucu_sahipp bilgi alabilirsin. <<")
client.run_until_disconnected()
run_until_disconnected()
