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




import os
import heroku3
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient, events
import random

#
# 
api_id = 26090016 #my.telegram.org/apps adresinden alabilirsiniz 
api_hash = "5b842f9801712684f2b98d70ead6538d" #my.telegram.org/apps adresinden alabilirsiniz
bot_token = "6735913033:AAFAtIgbv046k_Dm37BZteAD3JCq40I1dWI" #botfatherdan alabilirsiniz

client = TelegramClient("Samil", api_id, api_hash).start(bot_token=bot_token)

USERNAME = "ferootagbot" #botunuzun kullanıcı adı
log_qrup = -1001896209643 #log qrupunuzun idsi
startmesaj = "💌 Əmrlər Düyməsini Klikləyin Və Əmrləri Öyrənin...\n📚 Mən Bəzi Faydalı Xüsusiyyətləri Olan Telegram Üzvü Tagger Botuyam" #start mesajınız
komutlar = "🇦🇿 Bütün Əmrlər ;\n\n» /utag   <  mesaj  >\n   - Userləri 5'li tağ edər .\n\n» /tag   <  mesaj  >\n   - Userləri tək tək tağ edər .\n\n» /atag   <  mesaj  >\n   - Adminləri tağ edər .\n\n» /etag   <  mesaj  >\n   - Userləri emoji ilə tağ edər .\n\n» /stag   <  mesaj  >\n   - Userləri gözəl sözlər ilə tağ edər .\n\n» /cancel < mesaj >\n   - Tağ prosesin deyandirar ." #komutların olduğu mesaj
qrupstart = "• 𝖲𝗎𝖺𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗄𝗍𝖺𝗒𝗂𝗆 . . .\n\n• Əmrləri 𝖦𝗈𝗋𝗆𝖾𝗄 İ𝖼𝗂𝗇 𝖡𝗈𝗍a Start Verib B𝖺𝗌𝗅𝖺𝗍𝗂𝗇 . . ." #aktif olduğunda gruba gelen mesaj
support = "sah_team" #destek qrupunuzun kullanıcı adı
sahib = "The_ferid" #sahibinizin kullanıcı adı
noadmin = "➻ Üzgünüm Ama Yönetici Değilsiniz ." #yönetici olmayanlar için mesaj

#
# 
# 
# 

