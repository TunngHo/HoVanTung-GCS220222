import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser

class Song:
    def __init__(self, title, url, rate):
        self.title = title
        self.url = url
        self.rate =rate

class PlayList:
    def __init__(self, PlayListName, description, Rate, SongList):
        self.PlayListName = PlayListName
        self.description = description
        self.Rate = Rate
        self.SongList = SongList
# Function1: Create new playlist
def createPlaylist():
    global playList
    playList = enterPlayList()
    messagebox.showinfo("Playlist", "New playlist created successfully.")
    messagebox.showinfo("Playlist", "Save before exit.")
def enterSong():
    title = simpledialog.askstring("Input", "Enter song title:")
    url = simpledialog.askstring("Input", "Enter song URL:")
    rate = simpledialog.askstring("Input", "Enter song rate:")
    return Song(title, url, rate)

def enterSongList():
    n = simpledialog.askinteger("Input", "Enter number of songs:")
    SongList = []
    for i in range(n):
        song = enterSong()
        SongList.append(song)
    return SongList

def enterPlayList():
    PlayListName = simpledialog.askstring("Input", "Set name for Playlist:")
    description = simpledialog.askstring("Input", "Playlist description:")
    Rate = simpledialog.askstring("Input", "Your review:")
    SongList = enterSongList()
    return PlayList(PlayListName, description, Rate, SongList)

# Function2: Show playlist information
def showPlaylist(playList):
    if not playList:
        messagebox.showinfo("Playlist", "No playlist available.")
        return
    playlistStr = f"Playlist Name: {playList.PlayListName}\nDescription: {playList.description}\nRate: {playList.Rate}\nSongs:\n"
    playlistStr += "\n".join([f"{i+1}. {song.title} \n    Rating: {song.rate}" for i, song in enumerate(playList.SongList)])
    messagebox.showinfo("Playlist", playlistStr)

# Function3: Choose a song to play
def playSong(playList):
    songListStr = "\n".join([f"{i+1}. {song.title}" for i, song in enumerate(playList.SongList)])
    choice = simpledialog.askinteger("Input", f"Select a song to play:\n{songListStr}", minvalue=1, maxvalue=len(playList.SongList))
    if choice:
        webbrowser.open(playList.SongList[choice - 1].url) 

# Function4: Add new song to playlist
def addSongtoPlaylist(playList):
    song = enterSong()
    playList.SongList.append(song)
    messagebox.showinfo("Playlist", "Update new information successfully.")
    messagebox.showinfo("Playlist", "Save before exit.")

# Function5: Update new information for playlist
def updatePlaylistInformation(playList):
    choice = simpledialog.askinteger("Input", "What information do you want to update?\n1. Playlist name\n2. Description\n3. Rate", minvalue=1, maxvalue=3)
    if choice == 1:
        playList.PlayListName = simpledialog.askstring("Input", "Enter new Playlist name:")
    elif choice == 2:
        playList.description = simpledialog.askstring("Input", "Enter new description:")
    elif choice == 3:
        playList.Rate = simpledialog.askstring("Input", "Enter new review:")
    messagebox.showinfo("Playlist", "Update new information successfully.")
    messagebox.showinfo("Playlist", "Save before exit.")

# Function6: Delete a song from playlist
def deleteSong(playList):
    songListStr = "\n".join([f"{i+1}. {song.title}" for i, song in enumerate(playList.SongList)])
    choice = simpledialog.askinteger("Input", f"Select a song to delete:\n{songListStr}", minvalue=1, maxvalue=len(playList.SongList))
    if choice:
        del playList.SongList[choice - 1]
    messagebox.showinfo("Playlist", "Delete successfully.")
    messagebox.showinfo("Playlist", "Save before exit.")

# Function7: Save and exit
def saveAndExit(playList):
    WritePlayListToFile(playList)
    root.destroy()  # Terminate the Tkinter main loop and close the window

def main():
    global playList
    global root  # Declare root as global so it can be used in saveAndExit

    try:
        playList = ReadPlayListFromFile()
    except:
        playList = None
        messagebox.showinfo("Information", "If this is your first time using this program, create your own new playlist.")

    root = tk.Tk()  # Initialize the Tkinter root window
    root.title("Music Player")

    # Set the window size (width x height) and position (optional)
    root.geometry("400x400")  # Window size of 400x400 pixels

    # Buttons with specified sizes
    tk.Button(root, text="Create a Playlist", command=lambda: createPlaylist(), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Show Playlist", command=lambda: showPlaylist(playList), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Play a song", command=lambda: playSong(playList), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Add a song to Playlist", command=lambda: addSongtoPlaylist(playList), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Update playlist information", command=lambda: updatePlaylistInformation(playList), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Delete a song", command=lambda: deleteSong(playList), width=20, height=2).pack(padx=10, pady=5)
    tk.Button(root, text="Save and exit", command=lambda: saveAndExit(playList), width=20, height=2).pack(padx=10, pady=5)

    root.mainloop()



def WritePlayListToFile(playList):
    with open("Song.txt", "w") as file:
        file.write(playList.PlayListName + "\n")
        file.write(playList.description + "\n")
        file.write(playList.Rate + "\n")
        file.write(str(len(playList.SongList)) + "\n")
        for song in playList.SongList:
            file.write(song.title + "\n")
            file.write(song.url + "\n")
            file.write(song.rate + "\n")

def ReadPlayListFromFile():
    with open("Song.txt", "r") as file:
        PlayListName = file.readline().strip()
        description = file.readline().strip()
        Rate = file.readline().strip()
        SongList = []
        n = int(file.readline().strip())
        for _ in range(n):
            title = file.readline().strip()
            url = file.readline().strip()
            rate = file.readline().strip()
            SongList.append(Song(title, url,rate))
    return PlayList(PlayListName, description, Rate, SongList)

if __name__ == "__main__":
    main()
