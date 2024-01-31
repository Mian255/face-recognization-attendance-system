import csv
import datetime
import time
import tkinter as tk
from tkinter import ttk, messagebox as mess, simpledialog as tsd
from tkinter.ttk import Progressbar
import cv2, os
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from typing import Optional
import random
import smtplib
from email.message import EmailMessage


class EmailHandler:
    def __init__(self):
        self.sent_otp = None

    def send_otp(self, to_mail):
        otp = ""
        for i in range(6):
            otp += str(random.randint(0, 9))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            from_mail = "teamletsmoveon@gmail.com"
            password = "fgkp zwqa qikj oeoa"
            server.login(from_mail, password)

            subject = "OTP Verification"
            body = f"Your OTP is: {otp}"

            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = from_mail
            msg['To'] = to_mail
            msg.set_content(body)

            server.send_message(msg)
            print("OTP sent successfully.")
            self.sent_otp = otp
            server.quit()
        except Exception as e:
            print("Error sending OTP:", str(e))


class face_recognization_system:

    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def __init__(self, master):
        self.master = master
        self.entered_otp_entry = tk.Entry(self.master)
        self.email_entry = tk.Entry(self.master)
        self.key = ''
        self.ts = time.time()
        self.date = datetime.datetime.fromtimestamp(self.ts).strftime('%d-%m-%Y')
        self.day, self.month, self.year = self.date.split("-")
        self.clock: Optional[tk.Label] = None
        self.tv = ttk.Treeview(self.master)
        # self.tv.pack()
        self.txt = tk.Entry(self.master)
        self.txt2 = tk.Entry(self.master)
        self.message1 = tk.Label(self.master)
        self.message = tk.Label(self.master)
        self.sent_otp = None
        self.email_handler = EmailHandler()

    def run(self):
        self.create_gui()

    def create_gui(self):
        window.geometry("1920x700")
        window.resizable(True, False)
        window.title("Attendance System")
        window.state('zoomed')
        image_path = "C:/Users/user/OneDrive/Desktop/code/SCD LAB PROJECT VERSION 1.5/uni.png"
        img = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(img)
        bg_label = tk.Label(window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        message3 = tk.Label(window, text='Face Recognization Attendence System', font=('comic', 29, 'bold'),
                            fg="black",
                            bg="#EFF5F5", width=55, height=1)
        message3.place(x=0, y=10)

        frame3 = tk.Frame(window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.14, relheight=0.07)

        frame4 = tk.Frame(window, bg="#c4c6ce")
        frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

        datef = tk.Label(frame4, text=self.day + "-" + self.month + "-" + self.year + "    |", fg="black", bg="#EFF5F5",
                         width=55,
                         height=1,
                         font=('comic', 22, 'bold'))
        datef.pack(fill='both', expand=1)

        self.clock = tk.Label(frame3, fg="black", bg="#EFF5F5", width=55, height=1, font=('comic', 22, ' bold '))
        self.clock.pack(fill='both', expand=1)
        self.tick()

        ##################### MENUBAR #################################

        menubar = tk.Menu(window, relief='ridge')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=self.change_pass)
        filemenu.add_command(label='Contact Us', command=self.contact)
        filemenu.add_command(label='Exit', command=window.destroy)
        menubar.add_cascade(label='Help', font=('comic', 29, ' bold '), menu=filemenu)

        ###################### BUTTONS ##################################
        mark_attendance = tk.Button(window, text='Mark Attendance', command=self.create_window,
                                    fg="black",
                                    bg="#BAD7E9",
                                    width=35,
                                    height=1, activebackground="white", font=('comic', 15, ' bold '))
        mark_attendance.place(x=425, y=200)

        add_user = tk.Button(window, text='New User', command=self.create_login_window, fg="black",
                             bg="#BAD7E9",
                             width=35,
                             height=1, activebackground="white", font=('comic', 15, ' bold '))
        add_user.place(x=425, y=300)

        window.configure(menu=menubar)
        window.mainloop()

    def create_login_window(self):
        ver_window = tk.Toplevel()
        ver_window.geometry("1920x700")
        ver_window.resizable(True, False)
        ver_window.title("Attendance System")
        ver_window.state('zoomed')
        image_path = r"C:\Users\user\OneDrive\Desktop\code\SCD LAB PROJECT VERSION 1.5\uni.png"
        img = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(img)
        bg_label = tk.Label(ver_window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.pack()
        message3 = tk.Label(ver_window, text='Face Recognization Attendence System', font=('comic', 29, 'bold'),
                            fg="black",
                            bg="#EFF5F5", width=55, height=1)
        message3.place(x=0, y=10)

        frame22 = tk.Frame(ver_window, bg="#497174")
        frame22.place(relx=0.31, rely=0.17, relwidth=0.39, relheight=0.80)
        head22 = tk.Label(frame22, text="                        OTP VERIFICATION                       ", fg="black",
                          bg="#3a5759", font=('comic', 17, ' bold '))
        head22.grid(row=0, column=0)
        lbl = tk.Label(frame22, text="  Email Address", width=20, height=1, fg="black", bg="#497174",
                       font=('comic', 17, ' bold '))
        lbl.place(x=0, y=55)

        self.email_entry = tk.Entry(frame22, width=32, fg="black", font=('comic', 15, ' bold '))
        self.email_entry.place(x=70, y=90)

        lbl2 = tk.Label(frame22, text="Enter OTP", width=20, fg="black", bg="#497174",
                        font=('comic', 17, ' bold '))
        lbl2.place(x=0, y=200)

        self.entered_otp_entry = tk.Entry(frame22, width=32, fg="black", font=('comic', 15, ' bold '))
        self.entered_otp_entry.place(x=70, y=245)

        snd_otp_btn = tk.Button(frame22, text="Generate OTP ", bg="#BAD7E9", fg="black", command=self.send_otp,
                                width="12", height=1,
                                activebackground="white", font=('comic', 15, ' bold '))
        snd_otp_btn.place(x=270, y=130)

        verify_otp_btn = tk.Button(frame22, text="Verify OTP", bg="#BAD7E9", fg="black", command=self.verify_otp,
                                   width="12", height=1,
                                   activebackground="white", font=('comic', 15, ' bold '))
        verify_otp_btn.place(x=270, y=280)

        ver_window.mainloop()

    def send_otp(self):
        to_mail = self.email_entry.get()
        self.email_handler.send_otp(to_mail)

    def verify_otp(self):
        entered_otp = self.entered_otp_entry.get()
        sent_otp = self.email_handler.sent_otp

        if sent_otp and entered_otp == sent_otp:
            print("OTP verification successful. Login successful.")
            self.create_window_1()
        else:
            print("OTP verification failed. Login failed.")
            self.create_login_window()

    def tick(self):
        time_string = time.strftime('%H:%M:%S')
        if self.clock:
            self.clock.config(text=time_string)
            self.clock.after(200, self.tick)

    def contact(self):
        mess._show(title='Contact us', message="Please contact us on : 'mianasad255@gmail.com' ")

    def check_haarcascadefile(self):
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            window.destroy()

    def save_pass(self):
        self.assure_path_exists("TrainingImageLabel/")
        exists1 = os.path.isfile(r"TrainingImageLabel\psd.txt")
        if exists1:
            tf = open(r"TrainingImageLabel\psd.txt", "r")
            key = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open(r"TrainingImageLabel\psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        op = (old.get())
        newp = (new.get())
        nnewp = (nnew.get())
        if (op == key):
            if (newp == nnewp):
                txf = open("TrainingImageLabel\psd.txt", "w")
                txf.write(newp)
            else:
                mess._show(title='Error', message='Confirm new password again!!!')
                return
        else:
            mess._show(title='Wrong Password', message='Please enter correct old password.')
            return
        mess._show(title='Password Changed', message='Password changed successfully!!')
        master.destroy()

    def change_pass(self):
        global master
        master = tk.Tk()
        master.geometry("400x160")
        master.resizable(False, False)
        master.title("Change Password")
        master.configure(background="white")
        lbl4 = tk.Label(master, text='   Enter Old Password', bg='white', font=('comic', 12, ' bold '))
        lbl4.place(x=10, y=10)
        global old
        old = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, ' bold '), show='*')
        old.place(x=180, y=10)
        lbl5 = tk.Label(master, text=' Enter New Password ', bg='white', font=('comic', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, ' bold '), show='*')
        new.place(x=180, y=45)
        lbl6 = tk.Label(master, text='Confirm New Password  ', bg='white', font=('comic', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, ' bold '), show='*')
        nnew.place(x=180, y=80)
        cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                           activebackground="white", font=('comic', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tk.Button(master, text="Save", command=self.save_pass, fg="black", bg="#00fcca", height=1, width=25,
                          activebackground="white", font=('comic', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()

    def psw(self):
        self.assure_path_exists("TrainingImageLabel/")
        exists1 = os.path.isfile(r"TrainingImageLabel\psd.txt")
        if exists1:
            tf = open(r"TrainingImageLabel\psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open(r"TrainingImageLabel\psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if (password == key):
            self.TrainImages()
        elif (password == None):
            pass
        else:
            mess._show(title='Wrong Password', message='You have entered wrong password')

    def clear(self):
        self.txt.delete(0, 'end')
        self.message1.configure(text="")

    def clear2(self):
        self.txt2.delete(0, 'end')
        res = ""
        self.message1["text"] = res

    def TakeImages(self):
        self.check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
        self.assure_path_exists("StudentDetails/")
        self.assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (self.txt.get())
        name = (self.txt2.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, '', Id, '', name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            self.message1.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                self.message.configure(text=res)

    def TrainImages(self):
        self.check_haarcascadefile()
        self.assure_path_exists("TrainingImageLabel/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = self.getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save(r"TrainingImageLabel\Trainner.yml")
        res = "Profile Saved Successfully"
        self.message1.configure(text=res)
        self.message.configure(text='Total Registrations till now  : ' + str(ID[0]))

    def getImagesAndLabels(self, path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids

    def TrackImages(self):
        global attendance
        self.check_haarcascadefile()
        self.assure_path_exists("Attendance/")
        self.assure_path_exists("StudentDetails/")
        for k in self.tv.get_children():
            self.tv.delete(k)
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile(r"StudentDetails\StudentDetails.csv")
        if exists1:
            df = pd.read_csv(r"StudentDetails\StudentDetails.csv")
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            # cv2.destroyAllWindows()
            # window.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open(r"Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open(r"Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        self.tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()

    def create_window(self):
        windows_1 = tk.Toplevel()
        windows_1.geometry("1920x700")
        windows_1.resizable(True, False)
        windows_1.title("Attendance System")
        windows_1.state('zoomed')
        image_path = "C:/Users/user/OneDrive/Desktop/code/SCD LAB PROJECT VERSION 1.5/uni.png"
        img = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(img)
        bg_label = tk.Label(windows_1, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        frame11 = tk.Frame(windows_1, bg="#497174")
        frame11.place(relx=0.31, rely=0.17, relwidth=0.39, relheight=0.80)
        msg3 = tk.Label(windows_1, text='Face Recognization Attendence System', font=('comic', 29, 'bold'), fg="black",
                        bg="#EFF5F5", width=55, height=1)
        msg3.place(x=0, y=10)

        frame33 = tk.Frame(windows_1, bg="#c4c6ce")
        frame33.place(relx=0.52, rely=0.09, relwidth=0.14, relheight=0.07)
        frame44 = tk.Frame(windows_1, bg="#c4c6ce")
        frame44.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

        datee = tk.Label(frame44, text=self.day + "-" + self.month + "-" + self.year + "    |", fg="black",
                         bg="#EFF5F5", width=55,
                         height=1, font=('comic', 22, 'bold'))
        datee.pack(fill='both', expand=1)
        self.clock = tk.Label(frame33, fg="black", bg="#EFF5F5", width=33, height=1, font=('comic', 22, ' bold '))
        self.clock.pack(fill='both', expand=1)
        self.tick()
        head11 = tk.Label(frame11, text="                        Already Registered                       ", fg="black",
                          bg="#3a5759", font=('comic', 17, ' bold '))
        head11.place(x=0, y=0)
        lbl3 = tk.Label(frame11, text="Attendance", width=20, fg="black", bg="#497174", height=1,
                        font=('comic', 17, ' bold '))
        lbl3.place(x=100, y=115)

        ################## BUTTONS ####################
        trackImg = tk.Button(frame11, text="Take Attendance", command=self.TrackImages, fg="black", bg="#BAD7E9",
                             width=35,
                             height=1,
                             activebackground="white", font=('comic', 15, ' bold '))
        trackImg.place(x=30, y=50)
        quit_Window = tk.Button(frame11, text="Quit", command=window.destroy, fg="black", bg="#BAD7E9", width=35,
                                height=1,
                                activebackground="white", font=('comic', 15, ' bold '))
        quit_Window.place(x=30, y=500)
        back_window = tk.Button(frame11, text="Back", command=windows_1.destroy, fg="black", bg="#BAD7E9", width=35,
                                height=1, activebackground="white", font=('comic', 15, ' bold '))
        back_window.place(x=30, y=450)
        ################## TREEVIEW ATTENDANCE TABLE ####################

        self.tv = ttk.Treeview(frame11, height=13, columns=('name', 'date', 'time'))
        self.tv.column('#0', width=82)
        self.tv.column('name', width=130)
        self.tv.column('date', width=133)
        self.tv.column('time', width=133)
        self.tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
        self.tv.heading('#0', text='ID')
        self.tv.heading('name', text='NAME')
        self.tv.heading('date', text='DATE')
        self.tv.heading('time', text='TIME')

        ###################### SCROLLBAR ################################

        scroll = ttk.Scrollbar(frame11, orient='vertical', command=self.tv.yview)
        scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
        self.tv.configure(yscrollcommand=scroll.set)
        ##################### MENUBAR #################################

        menubar = tk.Menu(self.master, relief='ridge')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=self.change_pass)
        filemenu.add_command(label='Contact Us', command=self.contact)
        filemenu.add_command(label='Exit', command=window.destroy)
        menubar.add_cascade(label='Help', font=('comic', 29, ' bold '), menu=filemenu)
        windows_1.configure(menu=menubar)
        windows_1.mainloop()

    def create_window_1(self):
        windows_2 = tk.Toplevel()
        windows_2.geometry("1920x700")
        windows_2.resizable(True, False)
        windows_2.title("Attendance System")
        windows_2.state('zoomed')
        image_path = "C:/Users/user/OneDrive/Desktop/code/SCD LAB PROJECT VERSION 1.5/uni.png"
        img = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(img)
        bg_label = tk.Label(windows_2, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        frame22 = tk.Frame(windows_2, bg="#497174")
        frame22.place(relx=0.31, rely=0.17, relwidth=0.39, relheight=0.80)
        msg3 = tk.Label(windows_2, text='Face Recognization Attendence System', font=('comic', 29, 'bold'), fg="black",
                        bg="#EFF5F5", width=55, height=1)
        msg3.place(x=0, y=10)

        frame33 = tk.Frame(windows_2, bg="#c4c6ce")
        frame33.place(relx=0.52, rely=0.09, relwidth=0.14, relheight=0.07)
        frame44 = tk.Frame(windows_2, bg="#c4c6ce")
        frame44.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

        datee = tk.Label(frame44, text=self.day + "-" + self.month + "-" + self.year + "    |", fg="black",
                         bg="#EFF5F5", width=55,
                         height=1, font=('comic', 22, 'bold'))
        datee.pack(fill='both', expand=1)
        self.clock = tk.Label(frame33, fg="black", bg="#EFF5F5", width=33, height=1, font=('comic', 22, ' bold '))
        self.clock.pack(fill='both', expand=1)
        self.tick()
        head22 = tk.Label(frame22, text="                        New Registrations                       ", fg="black",
                          bg="#3a5759", font=('comic', 17, ' bold '))
        head22.grid(row=0, column=0)
        lbl = tk.Label(frame22, text="Enter Your Roll Number", width=20, height=1, fg="black", bg="#497174",
                       font=('comic', 17, ' bold '))
        lbl.place(x=80, y=55)

        self.txt = tk.Entry(frame22, width=32, fg="black", font=('comic', 15, ' bold '))
        self.txt.place(x=30, y=88)

        lbl2 = tk.Label(frame22, text="Enter Your Name", width=20, fg="black", bg="#497174",
                        font=('comic', 17, ' bold '))
        lbl2.place(x=80, y=140)

        self.txt2 = tk.Entry(frame22, width=32, fg="black", font=('comic', 15, ' bold '))
        self.txt2.place(x=30, y=173)

        self.message1 = tk.Label(frame22, text="", bg="#497174", fg="black", width=39, height=1,
                                 activebackground="#3ffc00",
                                 font=('comic', 15, ' bold '))
        self.message1.place(x=7, y=230)

        self.message = tk.Label(frame22, text="", bg="#497174", fg="black", width=39, height=1,
                                activebackground="#D4EFBD",
                                font=('comic', 16, ' bold '))
        self.message.place(x=7, y=450)

        res = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    res = res + 1
            res = (res // 2) - 1
            csvFile1.close()
        else:
            res = 0
        self.message.configure(text='Total Registrations till now  : ' + str(res))

        ################## BUTTONS ####################

        # back_window = tk.Button(frame22, text="Back", command=windows_2.destroy, fg="black", bg="#BAD7E9", width=35,
        #                         height=1, activebackground="white", font=('comic', 15, ' bold '))
        # back_window.place(x=30, y=450)
        clearButton = tk.Button(frame22, text="Clear", command=self.clear, fg="black", bg="#BAD7E9",
                                width=11,
                                activebackground="white", font=('comic', 11, ' bold '))
        clearButton.place(x=335, y=86)
        clearButton2 = tk.Button(frame22, text="Clear", command=self.clear2, fg="black",
                                 bg="#BAD7E9", width=11,
                                 activebackground="white", font=('comic', 11, ' bold '))
        clearButton2.place(x=335, y=172)
        takeImg = tk.Button(frame22, text="Enroll Face", command=self.TakeImages, fg="black",
                            bg="#BAD7E9", width=34,
                            height=1,
                            activebackground="white", font=('comic', 15, ' bold '))
        takeImg.place(x=30, y=300)
        trainImg = tk.Button(frame22, text="Save Profile", command=self.psw, fg="black",
                             bg="#BAD7E9", width=34,
                             height=1,
                             activebackground="white", font=('comic', 15, ' bold '))
        trainImg.place(x=30, y=380)

        ##################### MENUBAR #################################

        menubar = tk.Menu(self.master, relief='ridge')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=self.change_pass)
        filemenu.add_command(label='Contact Us', command=self.contact)
        filemenu.add_command(label='Exit', command=window.destroy)
        menubar.add_cascade(label='Help', font=('comic', 29, ' bold '), menu=filemenu)
        windows_2.configure(menu=menubar)
        windows_2.mainloop()


def show_loading_screen():
    root = tk.Tk()
    height = 430
    width = 530
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    image_path = "C:/Users/user/OneDrive/Desktop/code/SCD LAB PROJECT VERSION 1.5/vector2.png"
    img = Image.open(image_path)
    img = img.resize((width, height))
    bg_image = ImageTk.PhotoImage(img)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.overrideredirect(True)
    root.configure(background="#497174")
    welcome_label = tk.Label(root, text="Face Recognition Attendance System", bg="#01dbf5",
                             font=("comic", 15, "bold"))
    welcome_label.place(x=85, y=25)
    progress_label = tk.Label(root, text="Loading...", font=("comic", 13, "bold"), bg="#01dbf5")
    progress_label.place(x=207, y=330)
    progress = ttk.Style()
    progress.theme_use('clam')
    progress.configure("red.Horizontal.TProgressbar", background="#108cff")
    progress = Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate',
                           style="red.Horizontal.TProgressbar")
    progress.place(x=60, y=370)

    def top():
        root.withdraw()
        root.destroy()

    i = 0

    def load():
        nonlocal i
        if i <= 10:
            txt = 'Loading...' + (str(10 * i) + '%')
            progress_label.config(text=txt)
            progress_label.after(600, load)
            progress['value'] = 10 * i
            i += 1
        else:
            top()

    load()
    root.resizable(False, False)
    root.mainloop()


show_loading_screen()
window = tk.Tk()
face_recognition_system_instance = face_recognization_system(master=window)
face_recognition_system_instance.run()
