import customtkinter as ctk
import sounddevice as sd
import numpy as np
import random

class NoiseCancellationUI(ctk.CTk):
    def __init__(self, audio_manager):
        super().__init__()

        self.audio_manager = audio_manager
        
        # Window Setup
        self.title("NoiseCancellation AI")
        self.geometry("500x680")
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#121a24") # Deeper, moodier blue-black

        self.grid_columnconfigure(0, weight=1)

        # 1. Branding Header
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=(40, 20))
        
        self.title_label = ctk.CTkLabel(
            self.header_frame, text="NoiseCancellation", 
            font=("Inter", 32, "bold"), text_color="#e0eafc"
        )
        self.title_label.pack()
        
        self.status_label = ctk.CTkLabel(
            self.header_frame, text="SYSTEM IDLE", 
            font=("Inter", 12, "bold"), text_color="#4f6d8a"
        )
        self.status_label.pack(pady=(5, 0))

        # 2. Main Control Card (The "Frosted" look)
        self.card = ctk.CTkFrame(
            self, 
            fg_color="#1c2938", 
            border_width=2, 
            border_color="#2c3e50",
            corner_radius=25
        )
        self.card.grid(row=1, column=0, padx=40, pady=10, sticky="nsew")
        self.card.grid_columnconfigure(0, weight=1)

        # Refined Input Source Label
        self.input_tag = ctk.CTkLabel(
            self.card, text="INPUT SOURCE", 
            font=("Inter", 10, "bold"), text_color="#6c8fb3"
        )
        self.input_tag.grid(row=0, column=0, pady=(25, 5))

        # High-Aesthetic Dropdown (OptionMenu)
        devices = sd.query_devices()
        device_names = [f"{i}: {d['name'][:28]}" for i, d in enumerate(devices) if d['max_input_channels'] > 0]
        
        self.device_menu = ctk.CTkOptionMenu(
            self.card, 
            values=device_names,
            fg_color="#121a24",           # Dark inner body
            button_color="#2c3e50",       # Darker button
            button_hover_color="#34495e", # Subtle hover
            dropdown_fg_color="#1c2938",  # Dropdown list color
            dropdown_hover_color="#2c3e50",
            dropdown_text_color="#e0eafc",
            width=320, 
            height=45,
            corner_radius=12,
            font=("Inter", 13)
        )
        self.device_menu.grid(row=1, column=0, padx=20, pady=15)

        # Aesthetic Toggle Switch
        self.switch_var = ctk.StringVar(value="off")
        self.switch = ctk.CTkSwitch(
            self.card, 
            text="ACTIVATE FILTER", 
            command=self.toggle_ai, 
            font=("Inter", 12, "bold"),
            variable=self.switch_var, 
            onvalue="on", 
            offvalue="off",
            switch_width=60,      # Slightly wider for better look
            switch_height=28,
            progress_color="#00d2ff" # Vibrant Neon Blue
        )
        self.switch.grid(row=2, column=0, pady=(15, 30))

        # 3. Live Visualizer Card
        self.viz_card = ctk.CTkFrame(
            self, 
            fg_color="#121a24", 
            corner_radius=20, 
            border_width=1, 
            border_color="#1c2938"
        )
        self.viz_card.grid(row=2, column=0, padx=40, pady=25, sticky="nsew")
        
        self.viz_label = ctk.CTkLabel(
            self.viz_card, text="LIVE INPUT VISUALIZER", 
            font=("Inter", 10, "bold"), text_color="#4f6d8a"
        )
        self.viz_label.pack(pady=(15, 5))

        self.canvas = ctk.CTkCanvas(
            self.viz_card, width=340, height=120, 
            background="#121a24", highlightthickness=0
        )
        self.canvas.pack(padx=20, pady=(0, 20))

        # Footer Versioning
        self.footer = ctk.CTkLabel(self, text="Developer v1.5", font=("Inter", 10), text_color="#37474f")
        self.footer.grid(row=3, column=0, pady=10)

        self.update_ui()

    def toggle_ai(self):
        if self.switch_var.get() == "on":
            self.audio_manager.enabled = True
            self.status_label.configure(text="CLEANING LIVE AUDIO", text_color="#00d2ff")
            self.title_label.configure(text_color="#00d2ff")
            self.card.configure(border_color="#1f6aa5") # Glow border when active
        else:
            self.audio_manager.enabled = False
            self.status_label.configure(text="SYSTEM IDLE", text_color="#4f6d8a")
            self.title_label.configure(text_color="#e0eafc")
            self.card.configure(border_color="#2c3e50") # Reset border

    def update_ui(self):
        """Draws the dynamic waveform bars"""
        self.canvas.delete("all")
        width, height = 340, 120
        center_y = height // 2
        
        level = self.audio_manager.current_rms * 600
        
        for i in range(0, width, 10):
            # Generate bars that react to the AI being ON
            h = random.uniform(2, max(5, level)) if self.audio_manager.enabled else 2
            
            # Gradient-like effect based on x-position
            color = "#00d2ff" if i < width * 0.6 else "#3a7bd5"
            
            # Draw rounded-looking bars
            self.canvas.create_rectangle(
                i, center_y - h, i + 5, center_y + h, 
                fill=color, outline=""
            )

        self.after(50, self.update_ui)