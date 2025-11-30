from pyscript import document, display

# GWA
def compute_gwa(e):
    g1 = float(document.getElementById("grade1").value)
    g2 = float(document.getElementById("grade2").value)
    g3 = float(document.getElementById("grade3").value)
    g4 = float(document.getElementById("grade4").value)
    g5 = float(document.getElementById("grade5").value)

    total = g1 + g2 + g3 + g4 + g5
    gwa = total / 5

    display(f"🌙 Your GWA is {gwa:.2f} 🌙", target="output")

# CLUB INFO
clubs = {
    "𓊆ྀི ꜱᴄɪᴇɴᴄᴇ ᴄʟᴜʙ 𓊇ྀི": "A community for curious minds who explore experiments and science.",
    "𓊆ྀི ᴀʀᴛꜱ ᴄʟᴜʙ 𓊇ྀི": "A creative group for students who love drawing, painting, and crafts.",
    "𓊆ྀི ᴍᴜꜱɪᴄ ᴄʟᴜʙ 𓊇ྀི": "A place to practice singing, instruments, and musical performance.",
    "𓊆ྀི ꜱᴘᴏʀᴛꜱ ᴄʟᴜʙ 𓊇ྀི": "A team-focused club for activities like basketball and volleyball."
}

def show_club_info(e):
    name = document.getElementById("club").value
    info = clubs[name]
    display(info, target="clubOutput")

# SECTION SWITCHING (NO CONDITIONS)
def hide_all():
    sections = document.querySelectorAll(".section")
    for s in sections:
        s.style.display = "none"

def show_home(e):
    hide_all()
    document.getElementById("home").style.display = "block"

def show_gwa(e):
    hide_all()
    document.getElementById("gwa").style.display = "block"

def show_clubs(e):
    hide_all()
    document.getElementById("clubs").style.display = "block"
