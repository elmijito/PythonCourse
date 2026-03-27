import customtkinter as ctk

#GUI

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        

        self.title("Modo enfocado")
        self.geometry("300x200")
        self.resizable(False, False) 
        

        self.tiempo_trabajo = 25 * 60  # 25 minutos en segundos
        self.tiempo_actual = self.tiempo_trabajo
        self.corriendo = False
        
    
        self.label_tiempo = ctk.CTkLabel(self, text="25:00", font=("Helvetica", 65, "bold"))
        self.label_tiempo.pack(pady=30)
        
        # Contenedor para alinear los botones
        self.frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botones.pack()
        
        # Botones
        self.btn_iniciar = ctk.CTkButton(self.frame_botones, text="Iniciar", command=self.toggle_timer, width=90)
        self.btn_iniciar.pack(side="left", padx=10)
        
        self.btn_reiniciar = ctk.CTkButton(self.frame_botones, text="Reiniciar", command=self.reiniciar_timer, width=90, fg_color="#C8504B", hover_color="#A0403C")
        self.btn_reiniciar.pack(side="left", padx=10)

    # --- LÓGICA DEL TEMPORIZADOR ---
    def toggle_timer(self):
        # Si está pausado, lo arranca. Si está corriendo, lo pausa.
        if not self.corriendo:
            self.corriendo = True
            self.btn_iniciar.configure(text="Pausar")
            self.actualizar_reloj()
        else:
            self.corriendo = False
            self.btn_iniciar.configure(text="Continuar")
    
    def actualizar_reloj(self):
        if self.corriendo and self.tiempo_actual > 0:
           self.tiempo_actual -= 1
           minutos, segundos = divmod(self.tiempo_actual, 60)
           self.label_tiempo.configure(text=f"{minutos:02d}:{segundos:02d}")
           self.after(1000, self.actualizar_reloj)
        elif self.tiempo_actual == 0:
             self.corriendo = False
             self.label_tiempo.configure(text="¡Tiempo!")
             self.btn_iniciar.configure(text="Iniciar")

    def reiniciar_timer(self):
        self.corriendo = False
        self.tiempo_actual = self.tiempo_trabajo
        self.label_tiempo.configure(text='25:00')
        self.btn_iniciar.configure(text='Iniciar')
    

# 3. Encendemos la aplicación
if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()