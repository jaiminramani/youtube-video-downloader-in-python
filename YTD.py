from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_name = ""

#file location
def openLocation():
    global Folder_name
    Folder_name = filedialog.askdirectory()
    if(len(Folder_name) > 1):
        locationError.config(text = Folder_name , fg = "green")

    else:   
        locationError.config(text = "Please choose Folder !!", fg ="red") 

#download video
def DownloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text = "")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive = True).first() 

        elif (choice == choices[1]):
            select = yt.streams.filter(progressive = True , file_extension = 'mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio = True).first() 

        else:
            ytdError.config(text = "Past Link Again !!" , fg = "red")


# download function
    select.download(Folder_name)
    ytdError.config(text = "Download complete !!")



root = Tk()
root.title("YTD Downloader")
root.geometry("300x400") # set the window
root.columnconfigure(0,weight = 1) # set all the containt in center

#YTD link lable
ytdLable = Label(root,text = "Enter The URL Of The video",font = ("berlin sans fb",15))
ytdLable.grid()

#entry box 
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width = 50,textvariable = ytdEntryVar)
ytdEntry.grid()

#error msg
ytdError = Label(root , text = "Error Msg",fg = "red",font = ("jost",10))
ytdError.grid()

#Asking save file lable
saveLabel = Label(root,text = "Save The Video File" , font = ("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width = 10 , bg = "red" , fg = "white" , text = "Choose path" , command = openLocation)
saveEntry.grid()

#Eroor msg location
locationError = Label(root , text = "Error Msg Of Path" , fg = "red" , font = ("jost",10))
locationError.grid()

#Download quality
ytdQuality = Label(root , text = "Select Quality" , font = ("jost",15))
ytdQuality.grid()

#combobox
choices = ["1080p" ,"480p","only audio"]
ytdChoices = ttk.Combobox(root, values = choices)
ytdChoices.grid()

#download button
downloadButton = Button(root , text = "Download",width = 10 , bg = "red" , fg = "white" , command = DownloadVideo)
downloadButton.grid()

#developer lable
developerlabel = Label(root , text = "Prayosha technology and solution" , font = ("berlin sans fb",15))
developerlabel.grid()

root.mainloop()

