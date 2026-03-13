# Din frekke bestefar har nå blitt digital

![](./akward_smiling_man_memeb.jpg)

# Setup 🤖⚙️⚡

### Kopier git filen

```bash
git clone https://github.com/wineredbbqsauce/Frekk-Bestefar.git
```

### Endre .env filen

```.env
Endre "your_token" til din discord bot token
```

[Discord Bot Token](https://discord.com/developers/applications)

---

# Automagisk setup 🔄</>🖥️⚙️

_For UNIX-like enviroments, like LInux / macOS_

### Tillat setup

```bash
chmod +x  ./setup.sh
```

### Kjør setup

```bash
./setup.sh
```

Det kan være at man må bruke _sudo_ for å kjøre filen.

Hvis den feiler og sier: _permission denied_. (eller noe liknende)

Kjør **sudo ./setup.sh** - Skriv inn passordet ditt her

---

# Manuell setup ⚙️ 🛠️🚧🏗️ ✍

### Last ned venv og aktiver det:

```python
python3 -m venv .venv
```

**Windows Command Prompt (CMD):** .\.venv\Scripts\activate.bat

---

Windows PowerShell: **.\.venv\Scripts\Activate.ps1**

---

**Windows Git Bash / WSL:** source .venv/Scripts/activate

---

macOS / Linux ---- Bash / Zsh: **source .venv/bin/activate**

---

### Installer nødvendigheter

```python
pip install -r requirements.txt
```

---

### Endre fil

Endre "_your \_token_" til din faktiske [discord bot token](https://discord.com/developers/applications) i **_.env_** filen

---

### Start botten

```python
python3 discord_bot.py
```

---

# _voila_

## Commands

@_navnet på botten din_ - F.eks @Bestefar

- @Bestefar hei
- @Bestefar hallo
- @Bestefar hjelp
- @Bestefar hvordan
- @Bestefar hvorfor
- @Bestefar takk
- @Bestefar hva
- @Bestefar commands

---

Husk at du må ha [python](https://python.org) lastet ned for at prosjektet skal fungere

---

###### Built with ❤️, caffeine ☕, and questionable decisions

© 0

Made by BBQ Sauce Inc. Coop. Com. Org. Net.
