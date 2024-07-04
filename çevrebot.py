import discord
import time
import os
import random
from discord.ext import commands
from tokenpy import token
intents = discord.Intents.default()
intents.message_content = True
liste = ["taş","kağıt","makas"]
bot = commands.Bot(command_prefix='/', intents=intents)
def tkmo():
    global tkmr
    tkmr = random.ranint(1,3)
    return
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def bilgi(ctx):
    await ctx.send("Bu bot çevre kirliliği ve erozyonu engellemeyi amaçlayıp ağaçlandırma vakıfları hakkında bilgiler veren bir discord botu")
@bot.command()
async def yardım(ctx):
    await ctx.send("koşular hakkında bilgi için k/koşu|Vakıflar akkında bilgi için /vakıflar, vakıf|quiz için /quiz|Bana ne yaptığımı sorabilirsin mesela:)")
@bot.command()
async def koşu(ctx):
    await ctx.send("tema vakfının koşuları hakkında bilgi almak ister misin?|/evet-/hayır")
    @bot.command()
    async def evet(ctx):
        await ctx.send("açılıyor")
        time.sleep(1)
        os.startfile("https://www.tema.org.tr/bagis-ve-destek/yardimseverlik-kosulari")
@bot.command
async def vakıflar(ctx, vakf):
    if vakf == "çevko":
        await ctx.send("Çevko, Türkiye’de çevrenin korunması, toplumsal gelişim ve ekonomiye katkı sağlamak amacıyla sürdürülebilir bir geri kazanım sistemini sanayinin öncülüğünde geliştirmeyi hedefleyen bir vakıftır")
        time.sleep(1)
        os.startfile("https://www.cevko.org.tr/index.php?option=com_content&view=featured&Itemid=100&lang=tr")
    elif vakf == "tema":
        await ctx.send("Toprağa sahip çıkmak ve onu korumayı hedefleyen bir vakıftır")
        time.sleep(1)
        os.startfile("https://www.tema.org.tr/anasayfa")
    elif vakf == "tuçev":
        await ctx.send("Çevre değerlerinin korunması ve geliştirilmesine yönelik çalışmalara katkı ve destek sağlayan bir sivil toplum kuruluşudur")
        time.sleep(1)
        os.startfile("https://tucev.csb.gov.tr")

@bot.command
async def naber(ctx):
    await ctx.send("doğayı korumaya devam ediyorum tabiki:)")
@bot.command
async def quiz(ctx):
    os.startfile("https://quizizz.com/admin/quiz/5f535c6d13fefc001b3bdd1c/cevre-koruma")
@bot.command
async def yağhesap(ctx, lt):
    await ctx.send(f"{lt}litre yağ {lt*1000000}litre suyu kirletir")
    

bot.run(token)