from pygame import mixer
import os

def find_artist_folder(artist_name, base_directory):
    """Find artist folder based on user input"""
    excluded_folders = {'.elasticbeanstalk', '.venv'}
    artist_name = artist_name.lower()
    for folder in os.listdir(base_directory):
        if folder in excluded_folders:
            continue
        folder_path = os.path.join(base_directory, folder)
        if os.path.isdir(folder_path) and artist_name in folder.lower():
            return folder_path
    return None

def find_song_file(song_name, directory):
    """Find song file in the specified directory"""
    audio_extensions = ['.mp3', '.wav', '.ogg']
    song_name = song_name.lower()
    
    for file in os.listdir(directory):
        file_lower = file.lower()
        if song_name in file_lower and any(file_lower.endswith(ext) for ext in audio_extensions):
            return os.path.join(directory, file)
    return None

def show_available_artists(base_directory):
    """Show list of available artists"""
    excluded_folders = {'.elasticbeanstalk', '.venv'}
    print("\nAvailable artists:")
    for folder in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder)
        if os.path.isdir(folder_path) and folder not in excluded_folders:
            print(f"- {folder.replace('-folder', '')}")


def show_available_songs(directory):
    """Show list of available songs in the artist's folder"""
    print("\nAvailable songs:")
    for file in os.listdir(directory):
        if file.endswith(('.mp3', '.wav', '.ogg')):
            print(f"- {os.path.splitext(file)[0]}")

def play_music():
    # Starting the mixer 
    mixer.init()
    # Base directory containing all artist folders
    base_directory = "d:/Python"
    
    while True:
        try:
            # Show available artists
            show_available_artists(base_directory)
            # Ask user for artist
            artist = input("\nEnter the artist name: ")
            # Find artist folder
            artist_folder = find_artist_folder(artist, base_directory)
            if not artist_folder:
                print(f"Error: No artist folder found containing '{artist}'")
                continue
            # Show available songs for the artist
            show_available_songs(artist_folder)
            # Ask for song
            song = input("\nEnter the song to play: ")
            # Find the song file
            song_path = find_song_file(song, artist_folder)
            if not song_path:
                print(f"Error: No song containing '{song}' found in {os.path.basename(artist_folder)}")
                continue 
            # Loading the song 
            mixer.music.load(song_path)
            print(f"\nNow playing: {os.path.basename(song_path)}")
            break
            
        except Exception as e:
            print(f"Error: {e}")
            continue

    # Setting the volume 
    mixer.music.set_volume(0.6)
    
    # Start playing the song 
    mixer.music.play()
    
    # Control loop
    music_is_playing = True
    while music_is_playing:
        print("\nControl keys:")
        print("'p' - pause")
        print("'r' - resume")
        print("'e' - exit")
        
        control_key = input("Enter command: ").lower()
        
        if control_key == 'p':
            mixer.music.pause()
            print("Music paused")
        elif control_key == 'r':
            mixer.music.unpause()
            print("Music resumed")
        elif control_key == 'e':
            mixer.music.stop()
            mixer.quit()
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    try:
        play_music()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        mixer.quit()