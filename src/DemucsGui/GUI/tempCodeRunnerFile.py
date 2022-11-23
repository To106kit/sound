    def OpenLog():
        if sys.platform == "win32":
            subprocess.run(["cmd", "/c", "explorer", str(logfile)])
        elif sys.platform == "darwin":
            subprocess.run(["open", str(logfile)])
        else:
            if tkinter.messagebox.askyesno("Demucs-GUI Log", "Do you want to copy log directory to your clipboard? "):
                pyperclip.copy(logfile)