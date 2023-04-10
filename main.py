import os

if __name__ == '__main__':
    print("Welcome to Text to Audio converter.")
    flag=1
    while flag==1:
        x = input("Enter Text to convert it into Audio / Press Q to Exit : ")
        if x=="Q" or x=="q":
            x = "Closing Text to Audio Converter."
            flag=0;
        command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)






