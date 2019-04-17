from gtts import gTTS
text=''
with open('text to speech.txt','r') as saama:
    for i in saama:
        text=text+i
ppp=gTTS(text,'hi',)
ppp.save('hello.mp3')
