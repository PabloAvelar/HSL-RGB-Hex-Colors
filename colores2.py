from tkinter import *
from tkinter import ttk
#from tkinter import font

class Color:
    def __init__(self):
        # Variable del color #
        self.codigo_color_rgb = StringVar(value="0")
        self.codigo_color_hex = StringVar(value="#000")
        self.letras = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
        self.key_list = list(self.letras.keys())
        self.val_list = list(self.letras.values())

    def paleta(self):
        # FRAME PALETA DEL TONO DE COLOR A ELEGIR CON EL CURSOR #
        ventana = App().ventana
        self.codigo_color_hex = self.codigo_color_hex.get()
        self.frame_paleta_colores = Frame(ventana)
        self.frame_paleta_colores.config(bg=self.codigo_color_hex, width=400, height=400)
        self.frame_paleta_colores.place(x=10, y=10)

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Colores")
        self.ventana.geometry("600x550")
        self.ventana.resizable(False, False)

    def valor_escala(self, valor):
        """ PARSEÉ A STRING LOS VALORES NUMÉRICOS QUE SERÁN AGREGADOS A UNA LISTA QUE JUNTA EL CÓDIGO HEXADECIMAL
        PARA QUE ME DEJE OBTENERLOS EN UNA VARIABLE JUNTOS, SIN SEPARACIÓN, SIN LOS CORCHETES, SIN COMILLAS,
        COMO SI FUERA TEXTO PLANO SIN ARRAY"""

        # SE LIMPIA EL VALOR ANTERIOR DE LOS CUADROS DE TEXTO PARA QUE SE PONGA EL NUEVO CÓDIGO HEXADECIMAL #
        self.c_hex.delete(0, END)

        valor = int(valor)
        self.resultado = []
        cociente = int(valor/16)
        residuo = int(valor%16)

        # RESULTADO DE LA IZQUIERDA (LAS DECENAS) #
        if cociente in self.letras:
            self.resultado.append(self.letras[cociente])
        else:
            self.resultado.append(str(cociente))

        # RESULTADO DE LA DERECHA (LAS UNIDADES) #
        if residuo in self.letras:
            self.resultado.append(self.letras[residuo])
        else:
            self.resultado.append(str(residuo))

        # CONVERSIÓN HEX - RGB #
        
        #print(self.resultado)
        #for x in self.resultado:
            #if x in self.val_list:
        

        # AGRUPANDO VALORES PARA INSERTARLOS EN LOS CUADROS DE TEXTO Y PARA ACTUALIZAR EL CUADRO DE COLOR #
        codigo = ''.join(self.resultado)
        self.codigo_color_hex = "#{}0000".format(codigo)

        self.frame_paleta_colores.config(bg=self.codigo_color_hex)
        self.c_hex.insert(0, self.codigo_color_hex) # SE INSERTA EL NUEVO VALOR, ANTES SE TIENE QUE LIMPIAR #
        
        #print(self.codigo_color_hex)

    def interfaz(self):
        # FRAME OPCIONES USUARIO #
        frame_config_usuario = Frame(self.ventana)
        frame_config_usuario.config(bg="#fff", width=580, height=120)
        frame_config_usuario.place(x=10, y=450)

        # FRAME PARA LA BARRA ESCALABLE #
        frame_barra_escalable = Frame(self.ventana)
        frame_barra_escalable.config(width=50, height=400)
        frame_barra_escalable.place(x=480, y=0)

        # Barra escalable #
        barra_escalable = Scale(frame_barra_escalable)
        barra_escalable.config(from_=255, to=0, length=400, showvalue=1, command=self.valor_escala)
        barra_escalable.place(x=0, y=0)

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
        def escala_arriba(event):
            valor = barra_escalable.get()
            barra_escalable.set(valor+1)

        def escala_abajo(event):
            valor = barra_escalable.get()
            barra_escalable.set(valor-1)

        def hex_manual(evento):
            """ ESTA FUNCIÓN NO ESTÁ BIEN HECHA, SÓLO ERA PARA PROBAR Y USARLA EN UN FUTURO """
            valor = self.c_hex.get()
            barra_escalable.set(valor)

        # PARA BAJAR Y SUBIR LA BARRA DESDE LAS FLECHAS DEL TECLADO #
        self.ventana.bind("<Up>", escala_arriba)
        self.ventana.bind("<Down>", escala_abajo)
        # PARA PASAR UN CÓDIGO MANUALMENTE #
        self.c_hex.bind("<Return>", hex_manual)

        self.ventana.mainloop()

if __name__ == "__main__":
    App().interfaz()