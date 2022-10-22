from pytube import YouTube 
import os

# Creating Menu
menu_description = """Welcome to YouTubee, to download a video or MP3 from YouTube
please specify MP3(Audio) or MP4 (Video) when prompted."""

print(menu_description)

# Depending on choice download MP4 or MP3
menu = int(input("For Video(MP4) enter 1, for Audio(MP3) enter 2: "))

# Downloads MP4
if menu == 1:
    # Gets URL
    yt = YouTube(str(input("Enter your URL of the Video you'd like to download: ")))
    video = yt.streams.filter(file_extension='mp4').first()
    
    # check for destination to save file
    print("Enter the destination (leave blank for current directory) to save file ")
    destination = str(input(">> ")) or '.'
    
    # download file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    
    # print success message
    print(yt.title + " has successfully downloaded.")
# Downloads MP3    
if menu == 2:
    # Gets URL
    yt = YouTube(str(input("Enter your URL of the Video you'd like to download: ")))
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    print("Enter the destination (leave blank for current directory) to save file ")
    destination = str(input(">> ")) or '.'
    
    # download file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # print success message
    print(yt.title + " has successfully downloaded.")
    
    
    
    