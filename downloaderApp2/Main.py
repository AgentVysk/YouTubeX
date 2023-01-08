from tkinter import *
from pytube import YouTube
import os

root = Tk()
root.title("Vysakh's YouTube Downloader")
root.iconbitmap('D:\Code_Pythonians\PyTubeCodes\downloaderApp2\youtubeX.ico')

downloadPath = 'D:\Videos\YouTubeVideos'

def urlChecker():
    global url
    global urlinput
    url = urlinput.get()
    title = YouTube(url).title
    print(YouTube(url).title)
    info = Label(root, text=title, relief=SUNKEN)
    info.grid(column=0, row=3, columnspan=3, pady=5)

def downLoader():
    global url
    global urlinput
    url = urlinput.get()
    video = YouTube(url)
    video = video.streams.get_by_resolution("720p")
    video.download(downloadPath)
    

def Exiter():
    root.quit()

def Helper():
    Window = Toplevel()
    help = Label(Window, text="Welcome to Vyakh's YouTube Video Downloader. \n I believe you have some doubts regarding the operation of this app.\n Fear not I'm here to help!!\n\n First make a folder with the path (D:\Videos\YouTubeVideos). This is where the downloaded videos will be available.\n Currently it is fixed as the app is still in its infancy and the developer is still learning how these things work!!\nAlso the quality of video downloaded is also fixed but it may change in the future version!\n\n The app is ready to use now.\n\nNow go to YouTube and copy the link of the video which you want to download.\nPaste the link inside the 'Youtube Video URL' input box.\nNow you can check the link if it's correct or not by clicking the 'Check' button\nIf the link is correct, the title of the video will be visible\nYou can proceed to download by clicking 'Download' button.\nKeep in mind it might take a while to download depending on Internet speed and video quality.")
    help.grid(column=0, row=0)

    def Backer():
        Window.destroy()
    
    backbutton = Button(Window, text="Back", bg='tomato', command=Backer)
    backbutton.grid(column=0, row=1)
    
def Audiomer():
    global url
    global urlinput
    url = urlinput.get()
    video = YouTube(url)
    video = video.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=downloadPath)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)



frameOne = LabelFrame(root, text="Youtube Video URL", padx=5, pady=5)
frameOne.grid(column=0, row=1, columnspan=3, padx=10, pady=5)
urlinput = Entry(frameOne, borderwidth=5, width=50,  )
urlinput.grid(column=0, row=0, columnspan=2)

info = Label(root, text="<Title>", relief=SUNKEN, width=45)
info.grid(column=0, row=3, columnspan=3, pady=5)

helpbutton = Button(root, text="help", padx=5, bg='LightBlue3', command=Helper)
checkbutton = Button(root, text="Check", bg='spring green', padx=10, command=urlChecker)
downloadbutton = Button(root, text="mp4 Download", bg='cornflower blue', padx=10, command=downLoader)
exitbutton = Button(root, text="Exit", bg='tomato', padx=10, command=Exiter)
audiobutton = Button(root,text="mp3 Download", bg='MediumPurple2', padx=10, command=Audiomer)

helpbutton.grid(column=2, row=0, sticky=E, padx=5)
checkbutton.grid(column=0, row=4, sticky=E)
downloadbutton.grid(column=1, row=4)
exitbutton.grid(column=2, row=4, sticky=W)
audiobutton.grid(column=1, row=5,)



root.mainloop()