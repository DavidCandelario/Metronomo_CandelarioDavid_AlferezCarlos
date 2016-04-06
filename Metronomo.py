import numpy as np
import math

class metronomo:
    def __init__(self, nota, tempo, metrica):
        self.nota = nota
        self.tempo = tempo
        self.metrica = metrica
        self.tiempo = float(60/float(tempo))


    def metrono(self):
        array = []
        
        note=0
        if self.nota == 'c':
            note=261.63
        if self.nota  == 'c#':
            note=277.18
        if self.nota  == 'd':
            note=293.66
        if self.nota  == 'd#':
            note=211.13
        if self.nota  == 'e':
            note=329.63
        if self.nota  == 'f':
            note=349.23
        if self.nota  == 'f#':
            note=369.99
        if self.nota  == 'g':
            note=392
        if self.nota  == 'g#':
            note=415.3
        if self.nota  == 'a':
            note=440
        if self.nota  == 'a#':
            note=466.16
        if self.nota  == 'b':
            note=493.88


        if self.metrica == '24.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val

        if self.metrica == '34.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '44.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '54.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '28.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '68.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '78.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)


            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '98.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)


            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


    def niveldeaudio(self, nivel, info):
                VaP=max(abs(info))
                valornivel=(10**(nivel/20.0))*((2**16)/2)
                valorajustado=valornivel/float(VaP)
                infoajustada=info*valorajustado
                return infoajustada
