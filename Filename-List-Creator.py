import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Функция для выбора папки
def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)
    else:
        folder_path_var.set("")

# Функция для записи названий файлов в текстовый файл (включая файлы в подкаталогах)
def save_filenames_to_txt():
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return

    parent_folder = os.path.dirname(folder_path)
    output_file = os.path.join(parent_folder, "file_list.txt")

    with open(output_file, "w") as f:
        for root_dir, sub_dirs, files in os.walk(folder_path):
            relative_path = os.path.relpath(root_dir, folder_path)
            if relative_path == ".":
                f.write(f"// {os.path.basename(folder_path)}\n")
            else:
                f.write(f"// {relative_path}\n")
            for filename in files:
                f.write(f"{filename}\n")

    messagebox.showinfo("Success", f"File list saved in: {output_file}")

# Создаем основное окно
root = tk.Tk()
root.title("File List Generator")
root.geometry("500x200")

# Устанавливаем тёмную тему
root.configure(bg="#2e2e2e")

# Переменная для хранения пути к папке
folder_path_var = tk.StringVar()

# Метка для выбора папки
label = tk.Label(root, text="Select folder:", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12))
label.pack(pady=10)

# Поле для отображения выбранного пути
folder_entry = tk.Entry(root, textvariable=folder_path_var, width=50, bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12), bd=0, relief="flat")
folder_entry.pack(pady=5)

# Функция для создания стильной кнопки
def create_button(text, command):
    button = tk.Button(root, text=text, command=command, bg="#444444", fg="#ffffff", font=("Helvetica", 12), borderwidth=0, padx=10, pady=5)
    button.pack(pady=5)
    button.bind("<Enter>", lambda e: button.configure(bg="#555555"))
    button.bind("<Leave>", lambda e: button.configure(bg="#444444"))
    return button

# Кнопка для выбора папки
browse_button = create_button("Browse...", choose_folder)

# Кнопка для запуска процесса
generate_button = create_button("Generate File List", save_filenames_to_txt)

# Запуск главного цикла обработки событий
root.mainloop()
