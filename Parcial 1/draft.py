import tkinter as tk
from tkinter import filedialog, simpledialog

class IDEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IDE Simple")

        self.text_editor = tk.Text(self.root, wrap="word")
        self.text_editor.pack(expand="yes", fill="both")

        # Menú
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.destroy)

        # Botones para cambiar el color
        self.color_frame = tk.Frame(self.root)
        self.color_frame.pack(fill="x")

        self.bg_color_button = tk.Button(self.color_frame, text="Color de Fondo", command=self.change_bg_color)
        self.bg_color_button.pack(side=tk.LEFT, padx=5)

        self.text_color_button = tk.Button(self.color_frame, text="Color de Texto", command=self.change_text_color)
        self.text_color_button.pack(side=tk.LEFT, padx=5)

    def new_file(self):
        self.text_editor.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_editor.get(1.0, tk.END)
                file.write(content)

    def change_bg_color(self):
        color = self.get_color()
        if color:
            self.text_editor.config(bg=color)

    def change_text_color(self):
        color = self.get_color()
        if color:
            self.text_editor.config(fg=color)

    def get_color(self):
        color = simpledialog.askstring("Color", "Introduce el código hexadecimal del color (por ejemplo, #RRGGBB):")
        return color

if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)
    root.mainloop()
