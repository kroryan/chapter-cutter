import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import sys
from chapter_cutter.core import split_file, merge_folder

LANGS = [
    'Spanish', 'English', 'French', 'German', 'Italian', 'Portuguese', 'Russian', 'Chinese', 'Japanese'
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Chapter Cutter')
        self.geometry('640x340')
        self.minsize(520, 300)

        # icon if available in bundle
        icon_path = self._resource_path('app-icon.ico')
        try:
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception:
            pass

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TFrame', background='#f0f4f8')
        style.configure('TLabel', background='#f0f4f8', font=('Segoe UI', 10))
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'))
        style.configure('Accent.TButton', background='#2b8cff', foreground='white')
        style.map('Accent.TButton', background=[('active', '#1a6fe0')])

        frm = ttk.Frame(self, padding=14)
        frm.pack(fill='both', expand=True)

        # Split controls
        ttk.Label(frm, text='Cortar archivo (.txt)', style='Header.TLabel').grid(column=0, row=0, sticky='w', columnspan=4)
        self.split_path_var = tk.StringVar()
        e1 = ttk.Entry(frm, textvariable=self.split_path_var)
        e1.grid(column=0, row=1, columnspan=3, sticky='ew', padx=(0,8))
        ttk.Button(frm, text='Seleccionar archivo', command=self.select_file, style='Accent.TButton').grid(column=3, row=1, sticky='e')

        # Language
        ttk.Label(frm, text='Idioma:').grid(column=0, row=2, sticky='w', pady=(8,0))
        self.lang_var = tk.StringVar(value='Spanish')
        cb = ttk.Combobox(frm, values=LANGS, textvariable=self.lang_var, state='readonly', width=24)
        cb.grid(column=0, row=3, sticky='w')

        ttk.Label(frm, text='Salida (carpeta opcional)').grid(column=1, row=2, sticky='w', pady=(8,0))
        self.out_dir_var = tk.StringVar()
        e2 = ttk.Entry(frm, textvariable=self.out_dir_var)
        e2.grid(column=1, row=3, columnspan=2, sticky='ew', padx=(0,8))
        ttk.Button(frm, text='Seleccionar carpeta', command=self.select_out_folder).grid(column=3, row=3, sticky='e')

        ttk.Button(frm, text='Cortar archivo', command=self.do_split, style='Accent.TButton').grid(column=0, row=4, pady=(12,0), sticky='w')

        # Merge controls
        ttk.Separator(frm, orient='horizontal').grid(column=0, row=5, columnspan=4, sticky='ew', pady=14)
        ttk.Label(frm, text='Fusionar capítulos (.txt)', style='Header.TLabel').grid(column=0, row=6, sticky='w', columnspan=4)
        self.merge_folder_var = tk.StringVar()
        e3 = ttk.Entry(frm, textvariable=self.merge_folder_var)
        e3.grid(column=0, row=7, columnspan=3, sticky='ew', padx=(0,8))
        ttk.Button(frm, text='Seleccionar carpeta', command=self.select_merge_folder).grid(column=3, row=7, sticky='e')
        ttk.Button(frm, text='Fusionar', command=self.do_merge, style='Accent.TButton').grid(column=0, row=8, pady=(12,0), sticky='w')

        # Status
        self.status_var = tk.StringVar(value='Listo')
        ttk.Label(frm, textvariable=self.status_var).grid(column=0, row=9, columnspan=4, sticky='w', pady=(12,0))

        # column weights so entries expand
        for c in range(4):
            frm.columnconfigure(c, weight=1)

    def select_file(self):
        p = filedialog.askopenfilename(filetypes=[('Text files','*.txt')])
        if p:
            self.split_path_var.set(p)

    def select_out_folder(self):
        d = filedialog.askdirectory()
        if d:
            self.out_dir_var.set(d)

    def select_merge_folder(self):
        d = filedialog.askdirectory()
        if d:
            self.merge_folder_var.set(d)

    def _resource_path(self, relative):
        # Get path to resource, works for dev and PyInstaller onefile
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)

    def do_split(self):
        path = self.split_path_var.get().strip()
        if not path or not os.path.isfile(path):
            messagebox.showerror('Error', 'Selecciona un archivo .txt válido para cortar')
            return
        lang = self.lang_var.get()
        out = self.out_dir_var.get().strip() or None
        t = threading.Thread(target=self._split_thread, args=(path, lang, out), daemon=True)
        t.start()

    def _split_thread(self, path, lang, out):
        try:
            self.status_var.set('Cortando...')
            files = split_file(path, lang=lang, out_dir=out)
            self.status_var.set(f'Wrote {len(files)} files to {os.path.dirname(files[0]) if files else out}')
            messagebox.showinfo('OK', f'Se han escrito {len(files)} archivos.')
        except Exception as e:
            messagebox.showerror('Error', str(e))
            self.status_var.set('Error')

    def do_merge(self):
        folder = self.merge_folder_var.get().strip()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror('Error', 'Selecciona una carpeta válida con capítulos .txt')
            return
        t = threading.Thread(target=self._merge_thread, args=(folder,), daemon=True)
        t.start()

    def _merge_thread(self, folder):
        try:
            self.status_var.set('Fusionando...')
            out = merge_folder(folder)
            self.status_var.set(f'Merged into {out}')
            messagebox.showinfo('OK', f'Fusionado a: {out}')
        except Exception as e:
            messagebox.showerror('Error', str(e))
            self.status_var.set('Error')


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
