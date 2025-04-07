import discord 
import random
from discord.ext import commands 
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
fikirler ={
    "Şişe":[
        "Şişeleri eşya olarak kulanabiliriz",
        "Şişeleri geri dönüştürüp yeni ürünler yapabiliriz",
        "Şişelerden su tabancası  yapabiliriz",
        "şişelerden saksı yapabailiriz",
    ]
    ,
    "Teneke":[
        "Tenekeden saksı yapabiliriz",
        "Tenekeden bir şans mıknatıs yapabiliriz",
        "Tenekeyi eritebilir yeniden kullanabiliriz",


    ]
    ,
    "Kapak":
    [
        "kapaklardan tekerlekli sandalye yapabiliriz",
        "kapakları tekerlek olarak kullanilirz",
        "kapaklardan kule yapabiliriz ve oyun oynayabiliriz",
    ] 

}
@bot.event 
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def kategori(ctx):
    kategori_listesi="\n".join(fikirler.keys())
    await ctx.send(f"Mevcut kategoriler:\n{kategori_listesi}")
@bot.command()
async def fikir(ctx):
    kategori=random.choice(list(fikirler.keys()))
    fikir=random.choice(fikirler[kategori])
    await ctx.send(f"**Kategori:** {kategori} \n💡 {fikir}")
@bot.command()
async def yardım(ctx):
    await ctx.send("!fikir yazarsanız rastgele bir fikir alırsınız\n") 

bot.run("tokeninizi buraya girin")
