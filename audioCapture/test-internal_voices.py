# Baseado nos vídeos: https://youtu.be/dRsK4UPSJrE?si=Sa5yG0OR0q7-GITl; https://youtu.be/fMyzSrDoT-E?si=goeJh5SjM-bjmrLs; https://youtu.be/36RIoJeV95M?si=Ty6mnemZgo2Bn3Qd

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def falar(audio):
    engine.say(audio)
    engine.runAndWait()

def inicial():
    hour = int(datetime.datetime.now().hour)
    strHour = datetime.datetime.now().strftime("%d/%m/%y, as %H:%M:%S")
    falar(f"Hoje é {strHour}")

    if hour >= 0 and hour < 12:
        falar("Bom dia!")
    elif hour >=12 and hour < 18:
        falar("Boa Tarde!")
    else: 
        falar("Boa noite!")
    falar("Senhor, estou pronto para começar. Me fale o que fazer.")


def ouvir():
    rec = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Pode falar")
        rec.adjust_for_ambient_noise(source, duration=0.5)
        rec.pause_threshold = 1
        audio = rec.listen(source)
    

    try:
        text = rec.recognize_google(audio, language="pt-BR")
        text = text.lower()

        if 'jarvis' in text:
            text = text.replace('jarvis', '').strip()
            falar(text)
            return text
        else:
            return ""

    except sr.UnknownValueError:
        falar("Não entendi, tem como repetir?")
        return "none"
    except Exception as e:
        print(f"Erro: {e}")
        return "none"


if __name__ == "__main__": 
    inicial()
    while True:
        pedido = ouvir().lower()

        if pedido == "none":
            continue

        if 'abrir youtube' in pedido:
            falar("abrindo youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            print(pedido)

        elif 'abrir google' in pedido:
            webbrowser.open("https://www.google.com")
            print(pedido)

        elif 'horas' in pedido:
            hora_atual = datetime.datetime.now().strftime("%H:%M")
            falar(f"Agora são {hora_atual}")
            print(pedido)
            
        elif 'tchau' in pedido:
            falar("Até mais!")
            print(pedido)
            break