# Music Player using Tkinter

from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title('Aryan\'s Music Player')
root.iconbitmap("Desktop\Python Practice\Music Player using Tkinter")
root.geometry("1000x600")


pygame.mixer.init()

#  Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*mp3"), ))
    
    # Strip out the directory info and .mp3 extension from the
    # song = song.replace("C:\Users\Administrator\Desktop\From Redmi Note 8 Pro\Video Songs", " ")
    # song = song.replace(".mp3", "")
    
    # Add song to listbox
    song_box.insert(END, song)
    
# Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'{song}'
     
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
# Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#  Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Button Images
back_btn_img = PhotoImage(file="Desktop\Python Practice\Music Player using Tkinter\Back.png")
# back_btn_img  = pygame.transform.scale(back_btn, (50, 50))
forward_btn_img = PhotoImage(file="Desktop\Python Practice\Music Player using Tkinter\Forward.png")
play_btn_img = PhotoImage(file="Desktop\Python Practice\Music Player using Tkinter\Play.png")
pause_btn_img = PhotoImage(file="Desktop\Python Practice\Music Player using Tkinter\Pause.png")
stop_btn_img = PhotoImage(file="Desktop\Python Practice\Music Player using Tkinter\Stop.png")

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=10)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=5)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=10, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=5)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=1, comman=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
root.mainloop()