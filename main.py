import PyPDF2
import pyttsx3
import sys
#to increase and decrease the volume,rate,voice of the speaker
converter = pyttsx3.init()
voiceEngine = pyttsx3.init()
voiceEngine.runAndWait()
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
def speechrate(pro):
   #function for speech rate
   pronounciaiton = pro
   if (pronounciaiton <= 3) or (pronounciaiton >= 0):
       newVoiceRate=80
       voiceEngine.setProperty('rate', newVoiceRate)
       voiceEngine.runAndWait()
   elif (pronounciaiton <= 6) or (pronounciaiton>3):
        newVoiceRate = 160
        voiceEngine.setProperty('rate', newVoiceRate)
        voiceEngine.runAndWait()
   elif (pronounciaiton <= 10) or (pronounciaiton>6):
       newVoiceRate = 340
       voiceEngine.setProperty('rate', newVoiceRate)
       voiceEngine.runAndWait()
   else:
       print('print invalid pronounciation speed')
       sys.exit()
   return;
def volume(vol):
   #function for speech volume
   volumeinput = vol
   if (volumeinput <= 3) and (volumeinput>= 0):
     newVolume = 0.5
     voiceEngine.setProperty('volume', newVolume)
     voiceEngine.runAndWait()
   elif (volumeinput <= 6) and (volumeinput > 3):
       newVolume = 1
       voiceEngine.setProperty('volume', newVolume)
       voiceEngine.runAndWait()
   elif (volumeinput <= 10) and (volumeinput > 6):
       newVolume = 2
       voiceEngine.setProperty('volume', newVolume)
       voiceEngine.runAndWait()
   else:
        print('invalid volume input')
        sys.exit()
   return;
   #function to change the gender of the voice
def voices(gen):
   # changing index, changes voices. o for male
   gender = gen
   if (gender == 1):
       voice_id = 'com.apple.speech.synthesis.voice.veena'
       converter.setProperty('voice', voice_id)
       converter.runAndWait()
   elif (gender == 0):
       voice_id = 'com.apple.speech.synthesis.voice.rishi'
       converter.setProperty('voice', voice_id)
       converter.runAndWait()
   else:
       print('invalid gender input')
       sys.exit()
   return;
def readBook(pd,pa):
    pdfReader = pd
    pages = pa
    for num in range(17, pages):
        speaker = pyttsx3.init()
        page = pdfReader.getPage(17)
        text = page.extractText()
        voiceEngine.say(text)
        speaker.runAndWait()
    return;
def main():
   #function to read the book which is in .pdf format.
   pronounciationin = int(input(print('enter the speed u want the pronounciation to be from 1 - 10')))
   volumein = int(input(print('enter the speed u want the volume of the speech to be from 1 - 10')))
   genderin = int(input(print("which voice do u prefer: press 0 for male voice or 1 for female voice" )))
   book = open('lesson.pdf', 'rb')
   pdfReader = PyPDF2.PdfFileReader(book)
   pages = pdfReader.numPages
   print(pages)
   voices(genderin)
   volume(volumein)
   speechrate(pronounciationin)
   readBook(pdfReader, pages)
main()
#alex voice
#com.apple.speech.synthesis.voice.Alex
#rishi voice
#com.apple.speech.synthesis.voice.rishi
#fred
#com.apple.speech.synthesis.voice.Fred
#damayanti
#com.apple.speech.synthesis.voice.damayanti
#samantha voice
#com.apple.speech.synthesis.voice.samantha
#veena voice
#com.apple.speech.synthesis.voice.veena
#victoria voice
#com.apple.speech.synthesis.voice.Victoria