from tkinter import *
 
class Paint(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)
         self.parent = parent
 
 
def main():
    root = Tk()
    root.geometry("1920x1080+300+300")
    app = Paint(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()
