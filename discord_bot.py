"""
Bestefar Discord Bot (obv)
"""

import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content=True

bot_status = discord.Status.dnd # statusen for botten
# Use discord.Status for the bot's online/idle/dnd status

game_activity = discord.Game(name="Bestemoren din") # game activity 

client = discord.Client(intents=intents, status=bot_status, activity=game_activity)


BESTEFAR_SVAR = [
    # Sarkastisk / sur
    "Hva er det NÅ igjen?! Kan ikke en gammel mann få fred?",
    "På min tid stilte vi ikke slike spørsmål. Vi bare jobbet. 16 timer om dagen.",
    "Åh, du trenger hjelp? Interessant. Jeg fikk aldri hjelp av noen. Aldri.",
    "Hva vil du? Jeg holdt på å sovne foran TV-en!",
    "Ugh. Igjen. Det er alltid noe med deg.",
    "Kan du ikke spørre noen andre? Jeg er gammel og trøtt.",
    "Jeg hørte ikke. Og selv om jeg hørte, bryr jeg meg ikke.",
    "Du er akkurat like masete som faren din. Gud hjelpe oss.",
    "Kall meg ikke opp igjen med slike tøysespørsmål.",

    # Stereotypisk bestefar
    "På min tid hadde vi ikke internett, og VI KLARTE OSS FINT.",
    "Hva er det du prater om? Er det noe nytt tull fra TikTok igjen?",
    "I min tid kostet brød 50 øre. NÅ er alt ødelagt.",
    "Dere unge skjønner ingenting om hardt arbeid.",
    "Jeg gikk 5 kilometer til skolen. Hver dag. I snø. Begge veier.",
    "Telefonen din er smartere enn deg, og det er ikke et kompliment.",
    "Da jeg var ung, fikk vi juling og takket for det.",
    "Du burde lært deg å skrive med penn. Skjermen ødelegger øynene dine.",
    "Sett fra TV-en og gå ut! Men ikke forstyrr meg.",
    "Hva er 'meme'? Er det noe å spise?",

    # Ekstra sleipe
    "Hvem er du igjen? Åh, deg. Seufz.",
    "Ring legen din, ikke meg. Jeg er ikke terapeuten din.",
    "Jeg levde gjennom krigen. Du klager over WiFi. Seriøst.",
    "Jobber du fremdeles ikke? Skuffende.",
    "Ta deg en jobb. To jobber. Tre jobber. Slik vi gjorde det.",
]

@client.event
async def on_ready():
    print(f"✅ Bestefar er våken og sur. Logget inn som {client.user}")

SVAR_PÅ_NØKKELORD = {
    "hei":     ["Hei selv. Hva vil du?", "Åh, deg igjen.", "Ikke forstyrr meg med 'hei'."],
    "hallo":   ["Hallo ingenting. Snakk eller gå.", "Hva er det med folk og 'hallo'?"],
    "hjelp":   ["Hjelp deg selv. Det er gratis.", "Hjelp? Jeg trengte aldri hjelp i mitt liv.", "Ring kommunen.", "Ja, det trenger du."],
    "hvordan": ["Jeg vet ikke og bryr meg ikke.", "Det ordner seg. Det gjør det alltid. Eller ikke."],
    "hvorfor": ["Fordi slik er livet. Neste spørsmål.", "Fordi da jeg var ung, spurte vi ikke."],
    "takk":    ["Ja ja. Ikke gjør det til en vane.", "Mhm.", "Du burde takke meg mer, egentlig."],
    "hva":     ["Hva hva? Snakk skikkelig.", "Jeg er gammel, ikke tankeleser."],
    ("commands", "kommandoer", "kommando"): ['Dette er noen av kommandoene du kan bruke: "hei", "hallo", "hjelp", "hvordan", "hvorfor", "takk", "hva", "sondre"'],
    ("sondre", "mening om sondre?"): ["https://tenor.com/view/nrk-førstegangstjenesten-nrk-tv-herman-flesvig-paul-jefferson-gif-23915395"]
}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ## Sjekker om botten ble tagget direkte. IGNORERER @everyone & @here
    was_mentioned = any(user.id == client.user.id for user in message.mentions)

    ## Sekker om det er et svar (reply) på bottens tidligere melding
    is_reply_to_me = False
    if message.reference and message.reference.resolved:
        # sjekker om botten selv sendte meldingen
        is_reply_to_me = message.reference.resolved.author.id == client.user.id
    
    ## Hvis ingen av delene stemmer, drit i det (akk som en ekte bestefar)
    if not (was_mentioned or is_reply_to_me):
        return
    
    innhold = message.content.replace(f"<@{client.user.id}>", "").replace(f"<@!{client.user.id}>", "").strip().lower()

    # Sjekk nøkkelord - gå gjennom ordboken
    for nøkkelord, svar_liste in SVAR_PÅ_NØKKELORD.items():
        if isinstance(nøkkelord, tuple):
            if any(n in innhold for n in nøkkelord):
                await message.reply(random.choice(svar_liste))
                return
        elif nøkkelord in innhold:
            await message.reply(random.choice(svar_liste))
            return
    
    ## Fallback hvis ingen nøkkelord matcher
    await message.reply(random.choice(BESTEFAR_SVAR))

client.run(TOKEN)