from tkinter import *
import bluetooth
import speech_recognition as sr


print("Searching for devices...")
print("")
nearby_devices = bluetooth.discover_devices()
num = 0
print("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print(num , ": " , bluetooth.lookup_name( i ))


selection = int(input("> ")) - 1
print( "You have selected", bluetooth.lookup_name(nearby_devices[selection]))
bd_addr = nearby_devices[selection]

print("bd_addr:", bd_addr)
port = 1

root = Tk()

class Application():
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.buttons()
        self.sock.connect((bd_addr, port))
        root.mainloop()

    def tela(self):
        self.root.title('Connect')
        self.root.geometry('700x55')
        self.root.resizable(False,False)

    # cria os frames para adcionar os componentes
    def frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx = 0 , rely = 0,relwidth = 1, relheight = 1)

    def buttons(self):
        #Bottao connect 
        self.btnConnect = Button(self.frame, text = 'Connect', command = self.connect)
        self.btnConnect.place ( relx = 0, rely = 0, width = 130, height = 50)
        
        #Bottao disconnect 
        self.btnDisconnect = Button(self.frame, text = 'Disconnect', command = self.disconnect)
        self.btnDisconnect.place ( relx = 0.2, rely = 0, width = 130, height = 50)
        
        #Bottao on 
        self.btnOn = Button(self.frame, text = 'On', command = self.on)
        self.btnOn.place ( relx = 0.4, rely = 0, width = 130, height = 50)
        
        #Bottao off 
        self.btnOff = Button(self.frame, text = 'Off', command = self.off)
        self.btnOff.place ( relx = 0.6, rely = 0, width = 130, height = 50)

        #Bottao Ouvir 
        self.btnStop = Button(self.frame, text = 'Ouvir', command = self.ouvir_microfone)
        self.btnStop.place ( relx = 0.8, rely = 0, width = 130, height = 50)

    #Create a connection to the socket for Bluetooth
    #communication
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    def disconnect(self):
        self.sock.close()

    def connect(self):
        print("connect")
        
        
    def on(self):
        data = "Rele01:off"
        self.sock.send(data)

    def off(self):
        data = "Rele01:on"
        self.sock.send(data)

    #Funcao responsavel por ouvir e reconhecer a fala
    def ouvir_microfone(self):
        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #Chama a funcao de reducao de ruido disponivel na speech_recognition
            microfone.adjust_for_ambient_noise(source)
            #Avisa ao usuario que esta pronto para ouvir
            print("Diga alguma coisa: ")
            #Armazena a informacao de audio na variavel
            audio = microfone.listen(source)


        try:
            #Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio,language='pt-BR')
            #Após alguns segundos, retorna a frase falada
            print("Você disse: " + frase)

            #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnkownValueError:
            print("Não entendi")

        if frase == "Ligar luz da sala":
            data = "Rele01:off"
            self.sock.send(data)

        if frase == "Desligar luz da sala":
            data = "Rele01:on"
            self.sock.send(data)

        return frase

Application()