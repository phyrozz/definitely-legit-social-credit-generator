from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import winsound


class App:
    def __init__(self, master):

        self.master = master

        self.frame = Frame(self.master).pack()

        self.enter_amount = IntVar()

        self.image1 = Image.open("img/1.jpg")
        self.image2 = Image.open("img/2.jpg")
        self.image3 = Image.open("img/3.jpg")
        self.image4 = Image.open("img/4.jpg")
        self.resized_image1 = self.image1.resize((150, 150), Image.ANTIALIAS)
        self.resized_image2 = self.image2.resize((150, 150), Image.ANTIALIAS)
        self.resized_image3 = self.image3.resize((150, 150), Image.ANTIALIAS)
        self.resized_image4 = self.image4.resize((220, 150), Image.ANTIALIAS)
        self.img_lefttop = ImageTk.PhotoImage(self.resized_image1)
        self.img_right = ImageTk.PhotoImage(self.resized_image2)
        self.img_leftbottom = ImageTk.PhotoImage(self.resized_image3)
        self.img_rightbottom = ImageTk.PhotoImage(self.resized_image4)

        self.left_top_panel = Label(self.frame, image=self.img_lefttop)
        self.left_top_panel.place(relx=.15, rely=.7, anchor=CENTER)

        self.left_bottom_panel = Label(self.frame, image=self.img_leftbottom)
        self.left_bottom_panel.place(relx=.15, rely=.35, anchor=CENTER)

        self.right_panel = Label(self.frame, image=self.img_right)
        self.right_panel.place(relx=.85, rely=.5, anchor=CENTER)

        self.right_bottom_panel = Label(self.frame, image=self.img_rightbottom)
        self.right_bottom_panel.place(relx=.5, rely=.70, anchor=CENTER)

        self.label = Label(self.frame, text="Social Credit Generator 社会信用评分生成器", font="Arial, 30")
        self.label.place(relx=.5, rely=.10, anchor=CENTER)

        self.amount_label = Label(self.frame, text="Enter amount输入金额:", font="Arial, 18")
        self.amount_label.place(relx=.5, rely=.22, anchor=CENTER)

        self.text_box = Entry(self.frame, font="Arial, 20", textvariable=self.enter_amount, width=25, highlightcolor="green")
        self.text_box.place(relx=.5, rely=.3, anchor=CENTER)

        self.generate_btn = Button(self.frame, text="Generate now 现在生成", font="Arial, 24", bg="green", command=self.new_window)
        self.generate_btn.place(relx=.5, rely=.45, anchor=CENTER)

    def new_window(self):
        try:
            if self.enter_amount.get() != 0:
                self.enter_amount.get()
                root.withdraw()
                self.new = Toplevel(self.master)
                self.new.geometry("600x300")
                self.new.resizable(False, False)
                self.new.configure(bg="red")
                self.new.iconbitmap("icon.ico")

                self.app = confirmWindow(self.new)

                self.new.protocol("WM_DELETE_WINDOW", self.hide_window)
                self.new.bind('<Escape>', lambda e: root.destroy())
            else:
                error()
        except:
            error()

    def hide_window(self):
        root.deiconify()
        self.new.destroy()


class confirmWindow:
    def __init__(self, master):
        self.master = master

        self.get_name = StringVar()
        self.get_id = StringVar()

        self.title_label = Label(self.master, text="Please enter your information", font="Arial, 24")
        self.title_label.place(relx=.5, rely=0.01, anchor=N)
        self.title_label_bottom = Label(self.master, text="请输入您的信息", font="Arial, 24")
        self.title_label_bottom.place(relx=.5, rely=0.15, anchor=N)

        self.full_name_label = Label(self.master, text="Full name 全名", font='Arial, 16')
        self.full_name_label.place(relx=.5, rely=0.3, anchor=N)
        self.full_name = Entry(self.master, font="Arial, 16", width=30, textvariable=self.get_name)
        self.full_name.place(relx=.5, rely=0.4, anchor=N)

        self.social_id_label = Label(self.master, text="Social ID 社会身份", font='Arial, 16')
        self.social_id_label.place(relx=.5, rely=0.5, anchor=N)
        self.social_id = Entry(self.master, font="Arial, 16", width=30, textvariable=self.get_id)
        self.social_id.place(relx=.5, rely=0.6, anchor=N)

        self.submit = Button(self.master, text="submit 提交", font="Arial, 20", command=self.submit_info).place(relx=.5, rely=0.75, anchor=N)


    def submit_info(self):
        if self.get_name.get() and self.get_id.get() != "" and self.get_id.get().isnumeric():
            root.destroy()
            self.new = Tk()
            self.new.title("WARNING警告！!!!!!")
            self.new.geometry("1000x600")
            self.new.resizable(False, False)
            self.new.configure(bg="red")
            self.new.iconbitmap("icon.ico")

            self.app = reportWindow(self.new)
            self.new.protocol("WM_DELETE_WINDOW", self.close_app)
            self.new.bind('<Escape>', lambda e: self.new.destroy())
        else:
            error()

    def close_app(self):
        if messagebox.askyesno("退出", "你想放弃吗？"):
            self.new.destroy()


class reportWindow:
    def __init__(self, master):
        winsound.PlaySound('warning.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        self.master = master

        self.title_label = Label(self.master, text="Your activity has been recorded to CCP authorities!", font="Arial, 30")
        self.title_label.place(relx=.5, rely=0.01, anchor=N)
        self.title_label_bottom = Label(self.master, text="您的活动已被中共当局记录",
                                 font="Arial, 30")
        self.title_label_bottom.place(relx=.5, rely=0.09, anchor=N)
        self.text1 = Label(self.master, text="you have been caught with using generator software, which violate law. Therefor,", font="Arial, 16")
        self.text1.place(relx=.5, rely=0.30, anchor=N)
        self.text2 = Label(self.master, text="you will lose ∞ social credit points and your computer will be confiscated", font="Arial, 16")
        self.text2.place(relx=.5, rely=0.40, anchor=N)
        self.text3 = Label(self.master, text="by the authorities.", font="Arial, 16")
        self.text3.place(relx=.5, rely=0.50, anchor=N)

        self.image = Image.open("img/5.gif")
        self.ccp_logo = Image.open("img/6.png")
        self.resized_image = self.image.resize((150, 150), Image.ANTIALIAS)
        self.resized_ccp_logo = self.ccp_logo.resize((150, 150), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized_image)
        self.ccp = ImageTk.PhotoImage(self.resized_ccp_logo)

        self.warning_left = Label(self.master, image=self.img)
        self.warning_left.place(relx=.01, rely=.7, anchor=W)
        self.warning_right = Label(self.master, image=self.img)
        self.warning_right.place(relx=.99, rely=.7, anchor=E)
        self.logo = Label(self.master, image=self.ccp)
        self.logo.place(relx=.5, rely=.85, anchor=S)


def error():
    messagebox.showerror("错误", "Wrong input. please try again 输入错误。 请再试一次")


def root_close():
    if messagebox.askyesno("退出", "你想放弃吗？"):
        root.destroy()


if __name__ == "__main__":
    root = Tk()

    root.title("社会信用评分生成器")
    root.geometry("800x500")
    root.resizable(False, False)
    root.configure(bg="red")
    root.iconbitmap("icon.ico")

    app = App(root)
    root.protocol("WM_DELETE_WINDOW", root_close)
    root.bind('<Escape>', lambda e: root.destroy())

    winsound.PlaySound('bg.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

    root.mainloop()
