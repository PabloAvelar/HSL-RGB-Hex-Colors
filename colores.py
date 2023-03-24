from tkinter import *
from tkinter import ttk
#from tkinter import font

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Colores")
        self.ventana.geometry("600x550")
        self.ventana.resizable(False, False)
        # Variable del color #
        self.letras = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
        self.rgb = { # valores iniciales #
            "rojo": 0, 
            "verde": 0,
            "azul": 0
        }

        self.hex = { # valores iniciales #
            "rojo": ["F","F"],
            "verde": ["0","0"],
            "azul": ["0","0"]
        }

        self.colores_niveles = {
            "color_nivel1": 255, #Rojo
            "color_nivel2": 510, #Amarillo
            "color_nivel3": 765, #Verde
            "color_nivel4": 1020, #Azul clarito
            "color_nivel5": 1275, #Azul
            "color_nivel6": 1530, #Morado
            "color_nivel7": 1785 #Rojo final
        }
        
        self.key_list = list(self.letras.keys())
        self.val_list = list(self.letras.values())

    def calcularRGB(self, valor_escala):
        color_estatico = ["rojo", "verde", "verde", "azul", "azul", "rojo"]
        color_variable = ["verde", "rojo", "azul", "verde", "rojo", "azul"]
        color_pausa = ["azul", "azul", "rojo", "rojo", "verde", "verde", "azul"]
        val_niveles = list(self.colores_niveles.values())
        
        if valor_escala == self.colores_niveles["color_nivel7"]:
            self.rgb["azul"] = 0
        else:
            for i in range(len(val_niveles)):
                nivel_actual = val_niveles[i]
                try:
                    nivel_superior = val_niveles[i+1]
                except:
                    pass
                
                if valor_escala >= nivel_actual and valor_escala <= nivel_superior:
                    self.rgb[color_estatico[i]] = 255 #se mantiene el valor del color que no se mueve#
                    self.rgb[color_pausa[i]] = 0

                if valor_escala >= nivel_actual and valor_escala < nivel_superior:
                    if nivel_actual == 510 or nivel_actual == 1020 or nivel_actual == 1530:
                        calculo = valor_escala - nivel_actual
                        calculo -= 255
                        self.rgb[color_variable[i]] = -calculo #Disminuye el color variable
                    else:
                        calculo = valor_escala - nivel_actual
                        self.rgb[color_variable[i]] = calculo #Aumenta el color variable

    def calcularHEX(self):
        key_hex = list(self.hex.keys())
        for i in range(len(key_hex)):
            #print(int(self.hex[key_hex[i]][0]))
            
            cociente = int((self.rgb[key_hex[i]] / 16))
            residuo = int((self.rgb[key_hex[i]] % 16))
            
            # EL 0 ES PORQUE ESTÁ PRIMERO EN LA LISTA, ESTAS SON LAS DECENAS #
            if cociente in self.letras:
                self.hex[key_hex[i]][0] = self.letras[cociente]
            else:
                self.hex[key_hex[i]][0] = str(cociente)

            # EL 1 ES PORQUE ESTÁ DESPUÉS EN LA LISTA, ESTAS LAS UNIDADES #
            if residuo in self.letras:
                self.hex[key_hex[i]][1] = self.letras[residuo]
            else:
                self.hex[key_hex[i]][1] = str(residuo)

    def calcular(self, valor_escala):
        valor_escala = int(valor_escala)
        #print(valor_escala)
        self.calcularRGB(valor_escala)
        self.calcularHEX()

        self.c_rgb.delete(0, END)
        self.c_hex.delete(0, END)
        val_rgb = list(self.rgb.values())
        val_hex = list(self.hex.values())
        val_hex = val_hex[0]+val_hex[1]+val_hex[2]
        val_hex = "".join(val_hex)

        self.c_rgb.insert(0, val_rgb)
        self.c_hex.insert(0, val_hex)

        self.frame_paleta_colores.config(bg="#"+val_hex)

    def interfaz(self):
        # FRAME PALETA DEL TONO DE COLOR A ELEGIR CON EL CURSOR #
        self.frame_paleta_colores = Frame(self.ventana)
        self.frame_paleta_colores.config(bg="#000", width=400, height=400)
        self.frame_paleta_colores.place(x=10, y=10)

        # FRAME OPCIONES USUARIO #
        frame_config_usuario = Frame(self.ventana)
        frame_config_usuario.config(bg="#fff", width=580, height=120)
        frame_config_usuario.place(x=10, y=450)

        # FRAME PARA LA BARRA ESCALABLE #
        frame_barra_escalable = Frame(self.ventana)
        frame_barra_escalable.config(width=50, height=400)
        frame_barra_escalable.place(x=480, y=0)

        # Barra escalable #
        # ‭1,785‬ = 7 veces 255, suben y bajan los valores #
        self.barra_escalable = Scale(frame_barra_escalable)
        self.barra_escalable.config(from_=255, to=1785, length=400, showvalue=0, resolution=1,command=self.calcular)
        self.barra_escalable.place(x=0, y=0)

        # ETIQUETAS DE TEXTO #
        txt_hex = Label(frame_config_usuario, text="HEX")
        txt_hex.config(bg="#fff", fg="#4B4B4B", font=("Arial", 12, "bold"))
        txt_hex.place(x=10, y=50)

        txt_rgb = Label(frame_config_usuario, text="RGB")
        txt_rgb.config(bg="#fff", fg="#4B4B4B", font=("Arial", 12, "bold"))
        txt_rgb.place(x=200, y=50)

        # CUADROS DE TEXTO #
        self.c_hex = ttk.Entry(frame_config_usuario)
        self.c_hex.place(x=50, y=52)

        self.c_rgb = ttk.Entry(frame_config_usuario)
        self.c_rgb.place(x=240, y=52)

        # EVENTOS Y SUS FUNCIONES #
        def escala_abajo(event):
            valor = self.barra_escalable.get()
            self.barra_escalable.set(valor+1)

        def escala_arriba(event):
            valor = self.barra_escalable.get()
            self.barra_escalable.set(valor-1)

        def hex_manual(evento):
            """ ESTA FUNCIÓN NO ESTÁ BIEN HECHA, SÓLO ERA PARA PROBAR Y USARLA EN UN FUTURO """
            valor = self.c_hex.get()
            barra_escalable.set(valor)

        # PARA BAJAR Y SUBIR LA BARRA DESDE LAS FLECHAS DEL TECLADO #
        self.ventana.bind("<Up>", escala_arriba)
        self.ventana.bind("<Down>", escala_abajo)
        #self.ventana.bind("<Left>", x)
        # PARA PASAR UN CÓDIGO MANUALMENTE #
        self.c_hex.bind("<Return>", hex_manual)

        self.ventana.mainloop()

if __name__ == "__main__":
    App().interfaz()