from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video():
    video_url = url_entry.get()
    save_path = folder_path.get()

    try:
        yt = YouTube(video_url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        result_label.config(text="Video downloaded successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def clear_result():
    result_label.config(text="")

root = tk.Tk()
root.title("YouTube Video Downloader")

folder_path = tk.StringVar()

url_label = tk.Label(root, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

folder_label = tk.Label(root, text="Save to:")
folder_label.grid(row=1, column=0, padx=5, pady=5)

folder_entry = tk.Entry(root, textvariable=folder_path, width=40)
folder_entry.grid(row=1, column=1, padx=5, pady=5)

folder_button = tk.Button(root, text="Browse", command=open_file_dialog)
folder_button.grid(row=1, column=2, padx=5, pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=2, column=1, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_result)
clear_button.grid(row=2, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", fg="green")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
