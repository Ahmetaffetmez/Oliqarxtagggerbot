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
api_id = "21814744" #my.telegram.org/apps adresinden alabilirsiniz 
api_hash = "024ac6bfea2094f8e5e326d778fdcb54" #my.telegram.org/apps adresinden alabilirsiniz
bot_token = "5845484003:AAG81qb0FMNWPD3zCloAfvKLduSvifrEL78" #botfatherdan alabilirsiniz

client = TelegramClient("Samil", api_id, api_hash).start(bot_token=bot_token)

USERNAME = "OliqarxTagBot" #botunuzun kullanıcı adı
log_qrup = -1002025981280 #log qrupunuzun idsi
startmesaj = "💌 Əmrlər Düyməsini Klikləyin Və Əmrləri Öyrənin...\n📚 Mən Bəzi Faydalı Xüsusiyyətləri Olan Telegram Üzvü Tagger Botuyam" #start mesajınız
komutlar = "🇦🇿 Bütün Əmrlər ;\n\n» /utag   <  mesaj  >\n   - Userləri 5'li tağ edər .\n\n» /tag   <  mesaj  >\n   - Userləri tək tək tağ edər .\n\n» /atag   <  mesaj  >\n   - Adminləri tağ edər .\n\n» /etag   <  mesaj  >\n   - Userləri emoji ilə tağ edər .\n\n» /stag   <  mesaj  >\n   - Userləri gözəl sözlər ilə tağ edər .\n\n» /cancel = >\n   - Tağ prosesin deyandirar ." #komutların olduğu mesaj
qrupstart = "• 𝖲𝗎𝖺𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗄𝗍𝖺𝗒𝗂𝗆 . . .\n\n• Əmrləri 𝖦𝗈𝗋𝗆𝖾𝗄 İ𝖼𝗂𝗇 𝖡𝗈𝗍a Start Verib B𝖺𝗌𝗅𝖺𝗍𝗂𝗇 . . ." #aktif olduğunda gruba gelen mesaj
support = "OliqarxTeam" #destek qrupunuzun kullanıcı adı
sahib = "MuradAndMee" #sahibinizin kullanıcı adı
noadmin = "➻ Üzgünüm Ama Yönetici Değilsiniz ." #yönetici olmayanlar için mesaj

#
# 
# 
# 

