try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk
from PIL import ImageTk
from PIL import Image, ImageTk

APP_TITLE = "Drag & Drop Tk Canvas Images"
APP_XPOS = 100
APP_YPOS = 20
APP_WIDTH = 300
APP_HEIGHT = 200

IMAGE_PATH = ""

class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)

        self.canvas = tk.Canvas(self, width=1000, height=1000, bg='white',
                                highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        File="img2.png"
        #self.img = ImageTk.PhotoImage(Image.open(File))
        #self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.scale = 1.0
        self.orig_img = Image.open(File)
        self.img = None
        self.img_id = None
        # draw the initial image at 1x scale
        self.redraw()
        self.canvas.bind_all('<MouseWheel>', self.zoom)

    def zoom(self, event):
        print "checking"
        if event.delta<0:
            self.scale *= 2
        elif event.delta>0:
            self.scale *= 0.5
        self.redraw(0, 0)

    def redraw(self, x=0, y=0):
        if self.img_id: self.canvas.delete(self.img_id)
        iw, ih = self.orig_img.size
        # calculate crop rect
        cw, ch = iw / self.scale, ih / self.scale
        if cw > iw or ch > ih:
            cw = iw
            ch = ih
        # crop it
        _x = int(iw / 2 - cw / 2)
        _y = int(ih / 2 - ch / 2)
        #tmp = self.orig_img.crop((_x, _y, _x + int(cw), _y + int(ch)))
        tmp=self.orig_img
       # self.orig_img.show()
        size = int(iw * self.scale), int(ih * self.scale)
        #print size
        # draw
        self.img = ImageTk.PhotoImage(tmp.resize(size))
        #self.img=self.img.subsample(self,x,y=2)
        self.img_id = self.canvas.create_image(300, 300, image=self.img)


    def close(self):
        print("Application-Shutdown")
        self.master.destroy()
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    # app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))

    app = Application(app_win).pack(fill='both', expand=True)

    app_win.mainloop()


if __name__ == '__main__':
    main()