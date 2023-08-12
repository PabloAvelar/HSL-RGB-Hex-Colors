from tkinter import *
from tkinter import ttk
import webbrowser
#from tkinter import font

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Colores")
        self.ventana.geometry("600x550")
        self.ventana.resizable(False, False)
        self.color_ventana = "#303030"
        self.ventana.config(bg=self.color_ventana)

        # Imagenes #
        self.info_img = PhotoImage(file="img/info.png")
        self.twitter_img = PhotoImage(file="img/twitter.png")
        self.twitch_img = PhotoImage(file="img/twitch.png")
        self.youtube_img = PhotoImage(file="img/youtube.png")
        self.github_img = PhotoImage(file="img/github.png")


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

        self.hsl = {
            "h": 0,
            "s": 0,
            "l": 0
        }
        
    def rgb_a_hex(self):
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

            # EL 1 ES PORQUE ESTÁ DESPUÉS EN LA LISTA, ESTAS SON LAS UNIDADES #
            if residuo in self.letras:
                self.hex[key_hex[i]][1] = self.letras[residuo]
            else:
                self.hex[key_hex[i]][1] = str(residuo)

    def hsl_a_rgb(self):
        H = self.hsl["h"] #Hue
        S = self.hsl["s"] #Saturation
        L = self.hsl["l"] #Lightness
        c = (1 - abs(L*2 - 1)) * S
        x = c * (1 - abs((H / 60) % 2 - 1))
        m = L - c/2

        R1 = 0
        G1 = 0
        B1 = 0
        #Calcular R1,G1,B1, en base a los grados del círculo, desde 0 a 360 #
        #Dependiendo el grado, se le asignarán valores diferentes calculados anteriormente #
        if H >= 0 and H < 60:
            R1,G1,B1 = c,x,0
        if H >= 60 and H < 120:
            R1,G1,B1 = x,c,0
        if H >= 120 and H < 180:
            R1,G1,B1 = 0,c,x
        if H >= 180 and H < 240:
            R1,G1,B1 = 0,x,c
        if H >= 240 and H < 300:
            R1,G1,B1 = x,0,c
        if H >= 300 and H <= 360:
            R1,G1,B1 = c,0,x

        R,G,B = int((R1+m)*255), int((G1+m)*255), int((B1+m)*255)
        self.rgb["rojo"], self.rgb["verde"], self.rgb["azul"] = R,G,B

    def tono(self, valor):
        valor = int(valor)
        self.hsl["h"] = valor
        self.calcular()
        
    def saturacion(self, valor):
        valor = float(valor)
        self.hsl["s"] = valor
        self.calcular()

    def brillo(self, valor):
        valor = float(valor)
        self.hsl["l"] = valor
        self.calcular()

    def calcular(self):
        self.hsl_a_rgb()
        self.rgb_a_hex()

        self.c_hsl.delete(0, END)
        self.c_rgb.delete(0, END)
        self.c_hex.delete(0, END)
        
        val_hsl_reales = list(self.hsl.values())
        val_rgb = list(self.rgb.values())
        val_hex = list(self.hex.values())
        val_hex = val_hex[0]+val_hex[1]+val_hex[2]

        #Para que no haya espacios y quede todo pegado#
        val_hex = "".join(val_hex)
        #Para convertirlos en porcentajes, los decimales por 100#
        val_hsl_reales[1] *= 100
        val_hsl_reales[2] *= 100
        #Para quitar los decimales#
        val_hsl_reales[1], val_hsl_reales[2] = int(val_hsl_reales[1]), int(val_hsl_reales[2])

        #Para agregarles el signo de porcentaje#
        h = str(val_hsl_reales[0])
        s = str(val_hsl_reales[1]) + "%"
        l = str(val_hsl_reales[2]) + "%"

        self.c_hsl.insert(0, [h,s,l])
        self.c_rgb.insert(0, val_rgb)
        self.c_hex.insert(0, val_hex)

        #Cambia el color del cuadro y escalas usando el código hexadecimal#
        self.frame_paleta_colores.config(bg="#"+val_hex)
        self.barra_H.config(highlightbackground="#"+val_hex, borderwidth=0.5, relief=SUNKEN, sliderlength=25)
        self.barra_S.config(highlightbackground="#"+val_hex, borderwidth=0.5, relief=SUNKEN, sliderlength=25)
        self.barra_L.config(highlightbackground="#"+val_hex, borderwidth=0.5, relief=SUNKEN, sliderlength=25)

    def interfaz(self):
        # FRAME PALETA DEL TONO DE COLOR A ELEGIR CON EL CURSOR #
        self.frame_paleta_colores = Frame(self.ventana)
        self.frame_paleta_colores.config(bg="#000", width=300, height=300, highlightbackground="#1C1C1C", highlightthickness=4)
        self.frame_paleta_colores.place(relx=0.5, y=160, anchor=CENTER)

        # FRAME OPCIONES USUARIO #
        frame_config_usuario = Frame(self.ventana)
        frame_config_usuario.config(bg="#444444", width=580, height=90, highlightbackground="#1C1C1C", highlightthickness=3)
        frame_config_usuario.place(x=10, y=450)

        # FRAME PARA LA BARRA ESCALABLE #
        frame_barra_escalable = Frame(self.ventana)
        frame_barra_escalable.config(width=430, height=120, bg=self.color_ventana)
        frame_barra_escalable.place(relx=0.5, y=390, anchor=CENTER)

        # Barras escalables #
        # valor final de 360 por los 360grados de un circulo #
        self.barra_H = Scale(frame_barra_escalable)
        self.barra_H.config(from_=0, to=360, length=400, showvalue=0, orient=HORIZONTAL, highlightbackground="#f00", borderwidth=0.5, command=self.tono, relief=SUNKEN, sliderlength=25)
        self.barra_H.place(x=20, y=0)

        self.barra_S = Scale(frame_barra_escalable)
        self.barra_S.config(from_=0, to=1, length=400, showvalue=0, resolution=0.01, orient=HORIZONTAL, highlightbackground="#f00", borderwidth=0.5, command=self.saturacion, relief=SUNKEN, sliderlength=25)
        self.barra_S.place(x=20, y=40)
        
        self.barra_L = Scale(frame_barra_escalable)
        self.barra_L.config(from_=0, to=1, length=400, showvalue=0, resolution=0.01, orient=HORIZONTAL, highlightbackground="#f00", borderwidth=0.5, command=self.brillo, relief=SUNKEN, sliderlength=25)
        self.barra_L.place(x=20, y=80)

        # Valores iniciales de las barras #
        self.barra_H.set(0)
        self.barra_S.set(1)
        self.barra_L.set(0.5)

        # ETIQUETAS DE TEXTO #
        txt_hue = Label(frame_barra_escalable, text="H")
        txt_hue.config(bg=self.color_ventana, fg="#ccc", font=("Arial", 12, "bold"))
        txt_hue.place(x=0, y=0)

        txt_saturation = Label(frame_barra_escalable, text="S")
        txt_saturation.config(bg=self.color_ventana, fg="#ccc", font=("Arial", 12, "bold"))
        txt_saturation.place(x=0, y=40)

        txt_lightness = Label(frame_barra_escalable, text="L")
        txt_lightness.config(bg=self.color_ventana, fg="#ccc", font=("Arial", 12, "bold"))
        txt_lightness.place(x=0, y=80)

        txt_hex = Label(frame_config_usuario, text="HEX")
        txt_hex.config(bg="#444444", fg="#ccc", font=("Arial", 12, "bold"))
        txt_hex.place(x=10, y=35)

        txt_rgb = Label(frame_config_usuario, text="RGB")
        txt_rgb.config(bg="#444444", fg="#ccc", font=("Arial", 12, "bold"))
        txt_rgb.place(x=200, y=35)

        txt_hex = Label(frame_config_usuario, text="HSL")
        txt_hex.config(bg="#444444", fg="#ccc", font=("Arial", 12, "bold"))
        txt_hex.place(x=390, y=35)

        # CUADROS DE TEXTO #
        self.c_hex = ttk.Entry(frame_config_usuario)
        self.c_hex.place(x=50, y=37)

        self.c_rgb = ttk.Entry(frame_config_usuario)
        self.c_rgb.place(x=240, y=37)

        self.c_hsl = ttk.Entry(frame_config_usuario)
        self.c_hsl.place(x=430, y=37)

        #Botones#
        info_app = Button(self.ventana, image=self.info_img)
        info_app.config(bg=self.color_ventana, activebackground=self.color_ventana, relief=FLAT, cursor="hand2", command=lambda:informacion())
        info_app.place(x=560, y=8)

        # EVENTOS Y FUNCIONES #
        def escala_arriba(event):
            valor = self.barra_H.get()
            self.barra_H.set(valor+1)

        def escala_abajo(event):
            valor = self.barra_H.get()
            self.barra_H.set(valor-1)

        def informacion():
            win = Toplevel()
            win.geometry("500x350")
            win.resizable(False, False)
            win.title("¡Hola!")
            win.config(bg=self.color_ventana)

            Label(win, text="Este es un programa para obtener colores en código\nHSL, RGB y Hexadecimal. Lo hice yo solito sólo para\npasar el rato ☻",
                bg=self.color_ventana,
                fg="#fff",
                font=("Arial", 13, "bold"),
                justify=LEFT).pack(pady=15)

            Label(win, text="Mis redes",
            bg=self.color_ventana,
            fg="#b92b27",
            font=("Arial", 30, "bold"),
            anchor="e").pack()

            twitter = Button(win, image=self.twitter_img, command=lambda:webbrowser.open_new("https://twitter.com/_PabloAvelar"))
            twitter.pack(padx=20,side=LEFT, fill=X, expand=True)
            twitter.config(
                cursor="hand2",
                relief=FLAT,
                bg=self.color_ventana,
                activebackground=self.color_ventana
            )

            twitch = Button(win, image=self.twitch_img, command=lambda:webbrowser.open_new("https://www.twitch.tv/pablitoavelar"))
            twitch.pack(padx=20,side=LEFT, fill=X, expand=True)
            twitch.config(
                cursor="hand2",
                relief=FLAT,
                bg=self.color_ventana,
                activebackground=self.color_ventana
            )

            youtube = Button(win, image=self.youtube_img, command=lambda:webbrowser.open_new("https://www.youtube.com/c/PabloAvelarYT"))
            youtube.pack(padx=20,side=LEFT, fill=X, expand=True)
            youtube.config(
                cursor="hand2",
                relief=FLAT,
                bg=self.color_ventana,
                activebackground=self.color_ventana
            )

            github = Button(win, image=self.github_img, command=lambda:webbrowser.open_new("https://github.com/PabloAvelar"))
            github.pack(padx=20,side=LEFT, fill=X, expand=True)
            github.config(
                cursor="hand2",
                relief=FLAT,
                bg=self.color_ventana,
                activebackground=self.color_ventana
            )

            Label(win, text="@_PabloAvelar", bg="#55acee", fg="#fff", width=12).place(x=19, y=300)
            Label(win, text="PablitoAvelar", bg="#6441a5", fg="#fff", width=12).place(x=144, y=300)
            Label(win, text="Pablo Avelar", bg="#cd201f", fg="#fff", width=12).place(x=269, y=300)
            Label(win, text="Pablo Avelar", bg="#24292E", fg="#fff", width=12).place(x=394, y=300)

            win.mainloop()

        # PARA BAJAR Y SUBIR LA BARRA DESDE LAS FLECHAS DEL TECLADO #
        self.ventana.bind("<Right>", escala_arriba)
        self.ventana.bind("<Left>", escala_abajo)

        self.ventana.mainloop()

if __name__ == "__main__":
    App().interfaz()
