import tkinter as tk
from tkinter import font as tkfont

class GoodMorningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Καλημέρα")
        
        # Set window size and center it on screen
        window_width = 380
        window_height = 220
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        # Modern Dark Theme Colors (Catppuccin Mocha inspired)
        self.bg_color = "#1e1e2e"       # Base dark background
        self.card_color = "#252538"     # Slightly lighter dark for container
        self.text_color = "#cdd6f4"     # Soft white text
        self.accent_color = "#89b4fa"   # Pastel blue for button
        self.accent_hover = "#b4befe"   # Lighter lavender/blue for hover
        self.button_text = "#11111b"    # Dark text for contrast on light button
        
        root.configure(bg=self.bg_color)
        root.resizable(False, False)
        
        # Create custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.subtitle_font = tkfont.Font(family="Helvetica", size=11)
        self.button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        
        # Container frame for padding and background structure
        self.main_frame = tk.Frame(root, bg=self.bg_color, padx=20, pady=25)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sunrise/Sun icon or emoji
        self.emoji_label = tk.Label(
            self.main_frame, 
            text="☀️", 
            font=("Helvetica", 28), 
            bg=self.bg_color, 
            fg="#f9e2af" # Vibrant gold color
        )
        self.emoji_label.pack(pady=(0, 5))
        
        # "Καλημέρα!" main text
        self.msg_label = tk.Label(
            self.main_frame, 
            text="Καλημέρα!", 
            font=self.title_font, 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.msg_label.pack(pady=(0, 2))
        
        # Subtitle message
        self.sub_label = tk.Label(
            self.main_frame, 
            text="Να έχετε μια υπέροχη μέρα!", 
            font=self.subtitle_font, 
            bg=self.bg_color, 
            fg="#a6adc8" # Muted text color
        )
        self.sub_label.pack(pady=(0, 20))
        
        # Premium Modern "OK" Button
        # We simulate a modern button using a Label with bind events for a flawless look
        self.ok_btn = tk.Label(
            self.main_frame, 
            text="ΟΚ", 
            font=self.button_font, 
            bg=self.accent_color, 
            fg=self.button_text,
            padx=40,
            pady=8,
            cursor="hand2",
            relief="flat",
            bd=0
        )
        self.ok_btn.pack()
        
        # Bind interactive hover effects and click actions
        self.ok_btn.bind("<Enter>", self.on_hover)
        self.ok_btn.bind("<Leave>", self.on_leave)
        self.ok_btn.bind("<Button-1>", self.on_click)
        
        # Also bind Enter key to close the app
        root.bind("<Return>", lambda event: root.destroy())
        root.bind("<Escape>", lambda event: root.destroy())

    def on_hover(self, event):
        self.ok_btn.configure(bg=self.accent_hover)

    def on_leave(self, event):
        self.ok_btn.configure(bg=self.accent_color)

    def on_click(self, event):
        # Graceful exit
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GoodMorningApp(root)
    root.mainloop()
