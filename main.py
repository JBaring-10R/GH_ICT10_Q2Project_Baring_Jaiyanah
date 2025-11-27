from pyscript import display, document  # type: ignore

def compute_gwa(e):
    try:
        g1 = float(document.getElementById('grade1').value)
        g2 = float(document.getElementById('grade2').value)
        g3 = float(document.getElementById('grade3').value)
        g4 = float(document.getElementById('grade4').value)
        g5 = float(document.getElementById('grade5').value)

        gwa = (g1 + g2 + g3 + g4 + g5) / 5
        display(f'🌙 Your GWA is {gwa:.2f} 🌙', target="output")
    except Exception:
        display("⚠️ Please enter valid numbers in all fields ⚠️", target="output")


clubs = {
    
    "𓊆ྀི ꜱᴄɪᴇɴᴄᴇ ᴄʟᴜʙ 𓊇ྀི": "A community for students who love discovering how things work. Members try hands-on experiments, explore biology, chemistry, and physics, and even build simple robotics and tech projects. It’s an exciting way to learn how science connects to everyday life.",
    "𓊆ྀི ᴀʀᴛꜱ ᴄʟᴜʙ 𓊇ྀི": "A creative space for students who enjoy making visual art. Members paint, draw, sculpt, and experiment with different materials while learning new techniques. It’s a friendly place to express ideas, improve skills, and collaborate with fellow artists.",
    "𓊆ྀི ᴍᴜꜱɪᴄ ᴄʟᴜʙ 𓊇ྀི": "A group for students who enjoy singing, playing instruments, and performing. Members practice together, study new pieces, and join school programs and competitions. It’s a chance to grow musically while enjoying the experience of performing with others.",
    "𓊆ྀི ꜱᴘᴏʀᴛꜱ ᴄʟᴜʙ 𓊇ྀི": "A club for students who want to stay active and enjoy team activities. Members join games like basketball and volleyball while learning teamwork, discipline, and fair play. It’s a fun way to build strength, stay healthy, and make friends."

}

def show_club(e):
    name = document.getElementById('club').value
    info = clubs.get(name, "Club not found.")
    display(info, target="clubOutput")