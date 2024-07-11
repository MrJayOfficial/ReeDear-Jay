import os
import sys
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from googletrans import Translator
import time
from gtts import gTTS
import subprocess
from PyPDF2 import PdfReader
from PyPDF2 import *
import pygame
import threading
# import multiprocessing
# import customtkinter

import requests
import webbrowser
from pydub import AudioSegment
from pydub.playback import play as pydub_play
import ttkbootstrap as ts
# from ttkbootstrap.dialogs import messagebox
# 
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor
from tkinter.font import Font
from ttkbootstrap.toast import ToastNotification
from tkinter import Tk,font

# root = customtkinter.CTk()
root = ts.Window(themename="vapor")
root.geometry("750x600")
root.resizable(False,False)

logo = "C:\\Users\\tanze\\Downloads\\codeforsell\\Reedear\\Images\\appLogo.png"

logo_img= os.path.join(logo, logo)
convert_button_path = "C:\\Users\\tanze\\Downloads\\codeforsell\\Reedear\\Images\\convert.png"
convert_button_img = os.path.join(convert_button_path, convert_button_path)
#font for convert buttn  and play button 
main_font = Font(family="Roboto", weight="bold",size=15)
sescond_main_font = Font(family="Roboto", weight="bold",size=10)

#creating first frame 

play_pathh = "C:\\Users\\tanze\\Downloads\\codeforsell\\Reedear\\Images\\play_button.png"
play_img = os.path.join(play_pathh, play_pathh)

home_buton_path = "C:\\Users\\tanze\\Downloads\\codeforsell\\Reedear\\Images\\homenewt.png"

home_img= os.path.join(home_buton_path, home_buton_path)
audio_file_path = ""
result_text = ""

pdf_page_num = None
trans_text = ""
execute = False
max_value = 100
results = ""
pdf = None
home_button_pressed = False

lang_get = "English"
accent_get='en-English'
voice_get = ""
user_filepath =  ""
file_name = ""
get_var = 0
counter = 0
notebook = ts.Notebook(root, bootstyle="dark")
notebook.pack(fill=BOTH, expand=True)
# Create and add the first screen (Tab 1) - Hidden

screen1 = ts.Frame(notebook)
notebook.add(screen1, text="")  # Hide the tab header

# Create and add the second screen (Tab 2) - Hidden
screen2 = ts.Frame(notebook)
notebook.add(screen2, text="") 
bar_var = IntVar()
user_filepath = ""


f3 =Frame(screen2,width=340,height=240)

f3.grid(row=1,column=0,columnspan=1)

f3.grid_propagate(False)

from_word = Label(f3, text="Starting Page",font=sescond_main_font)
from_word.place(x=13, y=100)


to_word = Label(f3, text="Ending Page",font=sescond_main_font)
to_word.place(x=200, y=100)



f1 =Frame(screen2,width=340,height=250, relief=SOLID, borderwidth=3)

f1.grid(row=0, column=0,pady=20, padx=20,rowspan=1,columnspan=1)
f1.grid_propagate(False)

#creating  second frame 
f2 =Frame(screen2,width=340,height=400,  bg="red")

f2.grid(padx=10, row=0, column=1)
f2.grid_propagate(False)

#cratig third frame 



f4 =Frame(screen2,width=340,height=200,bg="yellow")

f4.grid(row=1,column=1)
f4.grid_propagate(False)

#asking te user to save the file name 
from_num = ts.Entry(f3, width=20)
from_num.insert(0, "Enter starting page no")
from_num.place(x=2, y=140)

to_num = ts.Entry(f3, width=20)
to_num.insert(0, "Enter ending page no")
to_num.place(x=180, y=140)

starting_number = 0
ending_number = 0
prgress_bar_font = Font(family="Fonts/digital-7.(mono).ttf", weight="bold",size=30)

#progress bar label 
prgress_bar_show = Label(f1,text="", font=(prgress_bar_font,15))
prgress_bar_show.place(x=130,y=60)

#progressbar font 



def main_screen():
    
    global counter, get_var, pdf, lang_get, results, user_filepath, starting_number, ending_number,bton,save_button,my_page,meter,from_num,to_num,prgress_bar_show
    counter = -90
    get_var = 0
    pdf = None
    lang_get = ""
    results = ""
    user_filepath = ""
    pdf_page_num = 0

    prgress_bar_show.config(text=" ")
    accent.current(0)
    lang.current(0)
    my_page.destroy()
    buton = ts.Button(f1, text="Select PDF",bootstyle="danger",command=OpenFileDir)

    buton.place(x=80,y=90)
  
    meter['amountused'] = 0

    starting_number = 0
    ending_number = 0
    # bton.config(state=DISABLED)
    
    # # Reset widget states
    # for tab_id in notebook.tabs():
    #     notebook.tab(tab_id, state="hidden")
    # notebook.select(screen1)
    # buton.config(state=NORMAL)
    # convert_button.config(state=NORMAL)
    # play_buton.config(state=NORMAL)
    # meter.configure(amountused=0)
    # prgress_bar_show.config(text="")
    # lang.set(langes[0])
    # accent.set(acc[0])
    
    
def clear_starting_page_text(event):
    
    from_num.delete(0, END)

    
    
def clear_ending_page_text(event):
    to_num.delete(0, END)



def store_starting_page_num(event):
    global starting_number
    starting_number = from_num.get()
    print(f"stgarting number {starting_number}")

def store_endingg_page_num(even):
    global ending_number
    ending_number= to_num.get()
    print(f"Enging number {ending_number}")
    
    
    if starting_number != 0 or ending_number != None:
        if int(ending_number)- int(starting_number)>5:
            messagebox.showinfo("You can't select pages range to greater than 5 ","Invalid")
            convert_button.config(state=DISABLED)
            play_buton.config(state=DISABLED)
            
        elif int(starting_number) < 0:
            messagebox.showinfo("starting number must be  greater than 0  ","Invalid")
            convert_button.config(state=DISABLED)
            play_buton.config(state=DISABLED)
            
            

    
        elif int(starting_number) > int(ending_number) :
            messagebox.showinfo("Ending number must be greater  than Starting Number  ","Invalid")
            convert_button.config(state=DISABLED)
            play_buton.config(state=DISABLED)
            
            
        elif int(starting_number) > pdf_page_num or int(ending_number) > pdf_page_num:
            messagebox.showinfo("Number is greater than entire pdf pages number  ","Invalid")
            convert_button.config(state=DISABLED)
            play_buton.config(state=DISABLED)
            
            
            
        else:
            convert_button.config(state=NORMAL)
            play_buton.config(state=NORMAL)
            
            
            
    else:
        messagebox.showinfo("Must be greater than 0  ","Invalid")
        convert_button.config(state=DISABLED)
        play_buton.config(state=DISABLED)
        
        
        
        


    


def save_audio():
    global user_filepath
    user_filepath = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    
    if user_filepath:

        print(user_filepath)
        file_name = user_filepath.split('/')[-1]
  
        toast = ToastNotification(title="File Saved",duration=3000, alert=True, position=(-1200,30, 'n'),message=f"your file is saved as {file_name}")
        toast.show_toast()
    
        bton.config(state=NORMAL)
        
    
        
        
def show_notification(message):
    message.showinfo("Notification", tex)

# Example usage:
tex = "Make sure starting page number must be at least greater than 4 or 4 because generally PDF first few pages don't have any text so it can throw an error."

        

def meterOn():
    global meter, counter, max_value, ending_number, starting_number
    global pdf_page_num
    counter+=1
 
 
    if int(ending_number) - int(starting_number) == 5:

    # check_loading_while_clicking()
        if counter<=max_value: 
            meter.configure(amountused=counter)
            root.after(600,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=NORMAL)
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
        
 
    elif int(ending_number) - int(starting_number) == 4:

    # check_loading_while_clicking()
        if counter<=max_value:
            meter.configure(amountused=counter)
            root.after(500,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=DISABLED)
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
        
                
    elif int(ending_number) - int(starting_number) == 3:

    # check_loading_while_clicking()
        if counter<=max_value:
            meter.configure(amountused=counter)
            root.after(400,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=DISABLED)
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
            
    elif int(ending_number) - int(starting_number) == 2:

    # check_loading_while_clicking()
        if counter<=max_value:
            meter.configure(amountused=counter)
            root.after(300,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=DISABLED) 
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
        
                
            
    elif int(ending_number) - int(starting_number) == 1:

    # check_loading_while_clicking()
        if counter<=max_value:
            meter.configure(amountused=counter)
            root.after(150,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=DISABLED)
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
        
                
    else:
        if counter<=max_value:
            meter.configure(amountused=counter)
            root.after(50,meterOn)    
            play_buton.config(state=DISABLED)
            convert_button.config(state=DISABLED)
            home_button.config(state=DISABLED)
            
            
            
        else:
            toast = ToastNotification(title="Success",duration=3000, alert=True, position=(-1200,30, 'n'),message="Success")
            toast.show_toast()
            play_buton.config(state=NORMAL)
            convert_button.config(state=NORMAL)
            home_button.config(state=NORMAL)
        

    
def play_voice():
    global user_filepath
    webbrowser.open(user_filepath)


def play_threading():
    play = threading.Thread(target=play_voice)
    play.start()
def lang_Bind(e):
    global lang_get
    lang_get = lang.get()
   
def accent_Bind(e):
    global accent_get
    full_accent = accent.get().split('-')
    accent_get = full_accent[0]
def pitch_bind(e):
    print(f"this is the alue of scale pitch {int(pitch.get())}")
    
#creawting three frames 
def loading_pdf():
    global my_page, audio_file_path


    global bar_var,my_page,get_var, convert_button, play_buton,prgress_bar_show
    for _ in range(1,101):
        get_var+=1
        prgress_bar_show.configure(text=f"{get_var} %")

        bar_var.set(get_var)
        root.update_idletasks()
        # time.sleep(0.1)  # 
    
    
        if (get_var==100):
            my_page.stop()
        
            convert_button.config(state=NORMAL)
            play_buton.config(state=NORMAL)

def loading_thread():
    load_thread = threading.Thread(target=loading_pdf)
    load_thread.start()
    
            

def check_loading_while_clicking():
    global get_var,convert_button, play_buton
    if get_var<100:

        convert_button.config(state=DISABLED)
        play_buton.config(state=DISABLED)


def switch_to_next_tab():



    for tab_id in notebook.tabs():
        notebook.tab(tab_id, state="hidden")

    notebook.select(screen2)
    
    show_notification(messagebox)  

def getvolumetext(e):
    global volume
    #volume text , speed test and pitch text
    text.config(text=f"{int(volume.get())}")

    
def getpithctext(e):
    text.config(text=f"{int(pitch.get())}")
 

def OpenFileDir():
    global audio_file_path
    try:
        audio_file_path = filedialog.askopenfilename(initialdir="C:\\", title="Upload a file ", filetypes=(("pdf files", "*.pdf"), ("all", "*.*")))
        print(f"Selected PDF file: {audio_file_path}")

        style = ttk.Style()

        def thread2():
            global pdf_page_num
            if audio_file_path:
                print(audio_file_path)
                global pdf
                pdf = PdfReader(open(audio_file_path, 'rb'))
                pdf_page_num = len(pdf.pages)
                buton.destroy()
                style = ttk.Style()
                style.configure('Custom.Horizontal.TProgressbar', background="green")

                global my_page
                my_page = ttk.Progressbar(f1,
                                         variable=bar_var,
                                         maximum=100,
                                         orient="horizontal",
                                         mode="determinate",
                                         style="Custom.Horizontal.TProgressbar")
                my_page.place(x=100,y=100)
                
                loading_thread()

        thre2 = threading.Thread(target=thread2)
        thre2.start()

        # Wait for the thread to finish before exiting
        # thre2.join()

    except Exception as e:
        print(f"Error: {e}")

    
            
    except Exception as e:
        print(f"Error: {e}")
        

def openthread():
    global audio_file_path
    thr2 = threading.Thread(target=OpenFileDir)
    thr2.start()
    thr2.join()
    
    
    
def extract_and_translate_page(page_num):
    global pdf, lang_get,results

    try:
        print(f"Processing page {page_num}")
        pdf_page = pdf.pages[page_num]
        text_pdf = pdf_page.extract_text()

        translator = Translator()
        translation = translator.translate(text=text_pdf, dest=lang_get)
        results += translation.text
        print(results)

    except Exception as e:
        print("ERORO:"+str(e))


def texttospech():
    
    global result_text,accent_get, voice_get,volume, speed, pitch,user_filepath,results
    
    try:
        if results and user_filepath:
            tts  = gTTS(text=results, lang=accent_get)         
            tts.save(user_filepath)
            print("sucesfully createed mp3 file ")
        else:
            print("not  successful")
    except Exception as e:
        print(f"ERROR:{e}")
        
     
    


        


def threadspeak():
    print(starting_number)
    print(ending_number)
    execute = True
    global pdf, lang_get, result_text
    

    # Ensure pdf is loaded
    if pdf is None:
        ts.messagebox.showinfo("NO PDF IS LOADED", "no pdf is loaded ")
        return
    pages_no = len(pdf.pages)
    
    
    #starting the meter thread on mean when user presss  convert button we start the meter 
    meter_thread = threading.Thread(target=meterOn)
    meter_thread.start()
    
    # Use ThreadPoolExecutor to process pages concurrently
    with ThreadPoolExecutor() as executor:
        for page_numbee in range(int(starting_number), int(ending_number) + 1):
            executor.submit(extract_and_translate_page, page_numbee)

 
 
    texttospech()
                
            

 


def ts2():
    tr2 = threading.Thread(target=threadspeak)
    tr2.start()

    
            
def checking_while_prssing_loading():
    if counter!= 99:
        play_buton.config(state=DISABLED)
        convert_button.config(state=DISABLED)

    else:
        play_buton.config(state=NORMAL)
        convert_button.config(state=NORMAL)


#Uplad a PDF label 
text = Label(f1, text="Upload a PDF",font=("Georgia", 15))
text.config(fg="orange")
text.place(x=85,y=2)


#slect pdf button 
buton = ts.Button(f1, text="Select PDF",bootstyle="danger",command=OpenFileDir)

buton.place(x=80,y=90)



for tab_id in notebook.tabs():
    notebook.tab(tab_id, state="hidden")
notebook.select(screen1)


#language label 
lang_text =Label(f3, text="Languages", font=("Consolas", 12),bg="black")
lang_text.place(x=40, y=0)


# list of languages 
langes = [
    'English',
    'Spanish',
    'French',
    'German',
    'Chinese',
    'Japanese',
    'Korean',
    'Arabic',
    'Russian',
    'Italian',
    'Dutch',
    'Swedish',
    'Norwegian',
    'Danish',
    'Finnish',
    'Greek',
    'Turkish',
    'Hindi',
    'Urdu',
    'Bengali',
    'Thai',
    'Vietnamese',
    'Indonesia',
    'Malay',
]



lang = ts.Combobox(f3, bootstyle="danger", values=langes,width=20)
lang.config(state="readonly")
lang.current(0)
lang.place(x=2, y=25)




#acent text
accent_text =Label(f3, text="Accent", font=("Consolas", 13),bg="black")
accent_text.place(x=230, y=0)

#acent
acc = [
    'af-Afrikaans', 'sq-Albanian', 'am-Amharic', 'ar-Arabic', 'hy-Armenian',
    'az-Azerbaijani', 'eu-Basque', 'be-Belarusian', 'bn-Bengali', 'bs-Bosnian',
    'bg-Bulgarian', 'ca-Catalan', 'ceb-Cebuano', 'ny-Chichewa', 'zh-CN-Chinese (Simplified)',
    'zh-TW-Chinese (Traditional)', 'co-Corsican', 'hr-Croatian', 'cs-Czech',
    'da-Danish', 'nl-Dutch', 'en-English',  'tl-Filipino',
    'fi-Finnish', 'fr-French', 'fy-Frisian', 'gl-Galician', 'ka-Georgian', 'de-German',
    'el-Greek', 'gu-Gujarati', 'ht-Haitian Creole', 'ha-Hausa', 'haw-Hawaiian',
    'iw-Hebrew', 'he-Hebrew', 'hi-Hindi', 'hmn-Hmong', 'hu-Hungarian', 'is-Icelandic',
    'ig-Igbo', 'id-Indonesian', 'ga-Irish', 'it-Italian', 'ja-Japanese', 'jw-Javanese',
    'kn-Kannada', 'kk-Kazakh', 'km-Khmer', 'rw-Kinyarwanda', 'ko-Korean', 'ku-Kurdish',
    'ky-Kyrgyz', 'lo-Lao', 'la-Latin', 'lv-Latvian', 'lt-Lithuanian', 'lb-Luxembourgish',
    'mk-Macedonian', 'mg-Malagasy', 'ms-Malay', 'ml-Malayalam', 'mt-Maltese',
    'mi-Maori', 'mr-Marathi', 'mn-Mongolian', 'my-Burmese', 'ne-Nepali', 'no-Norwegian',
    'or-Oriya', 'ps-Pashto', 'fa-Persian', 'pl-Polish', 
    'ro-Romanian', 'ru-Russian', 'sm-Samoan', 'gd-Scots Gaelic', 'sr-Serbian',
    'st-Sesotho', 'sn-Shona', 'sd-Sindhi', 'si-Sinhala', 'sk-Slovak', 'sl-Slovenian',
    'so-Somali', 'es-Spanish', 'su-Sundanese', 'sw-Swahili', 'sv-Swedish', 'tg-Tajik',
    'ta-Tamil', 'te-Telugu', 'th-Thai', 'tr-Turkish', 'uk-Ukrainian', 'ur-Urdu', 'ug-Uyghur',
    'uz-Uzbek', 'vi-Vietnamese', 'cy-Welsh', 'xh-Xhosa', 'yi-Yiddish']

accent = ts.Combobox(f3, bootstyle="warning", values=acc,width=20)
accent.config(state="readonly")
accent.current(0)
accent.place(x=180,y=25)

 
home_bton= ts.Image.open(home_img)
home_res = home_bton.resize((30, 30), Image.LANCZOS)
home_button_image  = ImageTk.PhotoImage(home_res)
#home buton 


home_button = Button(screen2, command=main_screen)
home_button.config(image = home_button_image, relief = SOLID, borderwidth=3)
home_button.place(x=700, y=1)


#convert button 
convert_button = Button(f4, text="Convert",font=main_font, width=25, height=2,command=ts2)
convert_button.config(bg="orange",fg="black",relief=SOLID, borderwidth=3, padx=20)
convert_button.grid(padx=40,row=0,column=1, pady=20)


#text from range 


#enter number for text 



from_num.bind("<FocusIn>", clear_starting_page_text)
to_num.bind("<FocusIn>", clear_ending_page_text)
from_num.bind("<FocusOut>", store_starting_page_num)
to_num.bind("<FocusOut>", store_endingg_page_num)

#play button 
play_buton = Button(f4, text="Play",font=main_font,padx=20,width=25, height=3, command=play_threading)
play_buton.config(bg="green",relief=SOLID, borderwidth=3)
play_buton.grid(padx=40,row=1,column=1)





#iocn for convert button 

icon_convert = ts.Image.open(convert_button_img)
icn1_resize = icon_convert.resize((30, 30), Image.LANCZOS)
ic1 = ImageTk.PhotoImage(icn1_resize)

# Icon for play button

icon_play_button = ts.Image.open(play_img)
ic2_resize = icon_play_button.resize((30, 30), Image.LANCZOS)
ic2 = ImageTk.PhotoImage(ic2_resize)
#attaching the icon for uplaod pdf button


#attaching the icon for convert button 
convert_button.config(image=ic1, compound=LEFT, width=190, height=60)  


#attaching the iocn for play button 
play_buton.config(image=ic2, compound=LEFT, width=190, height=60)  



#APP LOGO 

logo = ts.Image.open(logo_img)
logo_resize = logo.resize((300, 300), Image.LANCZOS)  # Adjust the size as needed
final_logo = ImageTk.PhotoImage(logo_resize)
my_logo = Label(screen1,image=final_logo)
my_logo.place(x=50, y=20)
        

#font for save button 
button_font = Font(family="Fonts/digital-7.(mono).ttf", weight="bold",size=15)





#Meter for loading 
meter = ts.Meter(f2, bootstyle="success", subtext="", interactive=False,textright="%",
                 metertype="full", stripethickness=5, metersize=240, padding=(0,40), amountused=counter, amounttotal=max_value,
                 subtextstyle="success")
meter.pack()



#making the binding function for comboboxes

lang.bind("<<ComboboxSelected>>", lang_Bind)
accent.bind("<<ComboboxSelected>>", accent_Bind)


#font for next button 
digital7_font = Font(family="Fonts/digital-7.(mono).ttf", weight="bold",size=10)

#next button 

bton = ts.Button(screen1,text="Next", bootstyle="success, outline" , state=DISABLED, command=switch_to_next_tab)
bton.place(x=550, y=150)



#save button 

save_button = ts.Button(screen1,text="Save", bootstyle="secondary, outline" , command=save_audio)
save_button.place(x=550, y=50)






#Heading ofSome Rules  

labelfont = Font(family="Fonts/digital-7.(mono).ttf", weight="bold",size=30)
rules = Label(screen1, text=" SOME RULES ", font=labelfont)
rules.place(x=200, y=290)

font_fonder_name = Font(family="Script MT Bold", size=10)

#here are some rules 
textfont = Font(family="Fonts/digital-7.(mono).ttf", weight="bold",size=7)
rul1 = Label(screen1, text=   "1: First make sure you pc is connected to wifi save the file\n name and then you can press next button", font=textfont)

rul5 = Label(screen1, text=   "2:Select the language in which  you want to translate your pdf text \n and then select the accent too  and after that select pages range starting page \n and ending pages and  make sure pages range not greater than 5", font=textfont)


rul2 = Label(screen1, text=   "3: After when you press convert button it started converting \n so it takes 45 seconds to convert during that time you \n can't press convert button and play button",font=textfont)
rul3 = Label(screen1, text=   "4: After saving the MP3 audio file, you have the flexibility to \n utilize that audio file containing the text from the \n PDF anywhere you need.",font=textfont)

rul1.place(x=175,y=350)
rul2.place(x=175, y=450)
rul3.place(x=175, y=500)
rul5.place(x=175,y=400)



#app font 
comic_sans_font = font.nametofont("TkDefaultFont")
comic_sans_font.configure(family="comic sans ms", size=18)

#app name 
app_name = Label(screen1, text="ReeDear", font=comic_sans_font)
app_name.place(x=600, y=520)

founder_name = Label(screen1, text="Founder: Jay",font=font_fonder_name)
founder_name.place(x=30,y=10)
root.mainloop()
