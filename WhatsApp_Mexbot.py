import random
import time
import keyboard
clock = time.strftime("%H:%M:%S")
current_version = " MexBot 1.1.0.2.0"
commands = ["!kick (comming soon)", "!time", "!adminMode (comming soon)", "!quiz", "!timer", "!msg", "!spamer", "!fun"]
random_quiz = ["Wer ist der Coder dieses Bots?", "Welches Item ist in Minecraft aus Mario 64 übernommenen worden?", "Facebook (Unternehmen) heißt nicht mehr Facebook. Wie heißt das Unternehmen jetzt?"]
random_quiz_answer = ["Max", "Elytra", "Der neue Name ist Meta"]
random_question = random.randint(0, 2)
ad = "https://chat.whatsapp.com/CMJdcUooMgTKqfxZ4cp0AO"
action = input("Your Action:")
timer = [int(input("S:")), int(input("M:")), int(input("H:"))]
target = input("Target:")
msg = input("Message")
count = int(input("Count of messages"))
time.sleep(10)
if action == "!msg":
    msg = msg + " " + target + " is fired"
    keyboard.press_and_release('ctrl+f')
    time.sleep(1)
    keyboard.write(target)
    time.sleep(4)
    keyboard.press('enter')
    time.sleep(2.1)
    keyboard.write(msg)
    keyboard.press('enter')

if action == "!time":
    keyboard.write("Uhrzeit: " + clock)
    keyboard.press('enter')
if action == "!quiz":
    keyboard.write(str(random_quiz[random_question]))
    keyboard.press('enter')
    time.sleep(30)
    keyboard.write('Die Antwort ist:' + str(random_quiz_answer[random_question]))
    keyboard.press('enter')

if action == "!info":
    keyboard.write("Version:" + current_version)
    keyboard.press_and_release('shift+enter')
    keyboard.write("Commands:")
    keyboard.press_and_release('shift+enter')
    keyboard.write(str(commands[1]) + ' ' + str(commands[3]) + " " + str(commands[7]))
    keyboard.press_and_release('shift+enter')
    keyboard.write(str(commands[4]) + " " + str(commands[5]) + " " + str(commands[6]))
    keyboard.press_and_release('shift+enter')
    keyboard.write("Uhrzeit: " + clock)
    keyboard.press_and_release('shift+enter')
    keyboard.write("Für mehr Features einfach bei wa.me/+494915204498918 melden")
    keyboard.press_and_release('shift+enter')
    keyboard.write("WhatsApp Group : " + ad)
    keyboard.press_and_release('shift+enter')
    keyboard.write("Partner Gruppe: ")

    keyboard.press('enter')

if action == "!timer":
    m = int(timer[1])
    h = int(timer[2])
    s = 59 * m
    while True:
        time.sleep(1)
        s -= 1
        print(s)
        if s == 59:
            keyboard.write("Letzte Minute")
        if s == 29:
            keyboard.write("nur noch eine halbe minute")
            keyboard.press('enter')
        if s == 9:
            keyboard.write(str(s))
            keyboard.press('enter')
        if s == 0:
            keyboard.write('ich rufe sie jetzt an')
            keyboard.press('enter')
if action == "!spamer":
    while True:
        count -= 1
        keyboard.write(msg)
        keyboard.press('enter')
        if count == 0:
            break
if action == "!fun":
    keyboard.write("Fun module")
    keyboard.press('enter')
    keyboard.write("🙃")
    keyboard.press('enter')
    keyboard.write("😊")
    keyboard.press('enter')
    keyboard.write("🙃")
    keyboard.press('enter')
    keyboard.write("🙂")
    keyboard.press('enter')

