import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from SIA_APP import p
from time import sleep

root = Tk()
root.minsize(300, 300)

list_of_songs = []

index = 0


def next_song(e):
    global index

    index += 1
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()


def previous_song(e):
    global index

    index -= 1
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()


def stop_song(e):
    pygame.mixer.music.stop()


def directory_chooser():
    directory = askdirectory()
    if directory == '':
        p("No files were entered")
        pass
    else:
        os.chdir(directory)
        for files in os.listdir(directory):
            if files.endswith('.mp3'):
                realdir = os.path.realpath(files)
                list_of_songs.append(files)
            else:
                p("That is not a mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(list_of_songs[0])
    pygame.mixer.music.play()


directory_chooser()

label = Label(root, text="SIA Music Player")
label.pack()
listbox = Listbox(root)
listbox.pack()

list_of_songs.reverse()

for i in list_of_songs:
    listbox.insert(0, i)

next_button = Button(root, text="Next Song")
next_button.pack()
previous_button = Button(root, text="Previous Song")
previous_button.pack()
stop_button = Button(root, text="Stop Music")
stop_button.pack()

next_button.bind("<Button-1>", next_song)
previous_button.bind("<Button-1>", previous_button)
stop_button.bind("<Button-1>", stop_song)


def run():
    p("Music Player Extension for SIA")
    sleep(1)
    p("Please input the directory file filled with the music you wish to play")
    sleep(1)
    p("Please do keep in mind that this extension can only play mp3 files.")
    sleep(1)
    root.mainloop()
