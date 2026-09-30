import yt_dlp
import os

def download_video_finale(url):
    download_path = "Download_Progetto_IFTS"
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        
        # --- GESTIONE SOTTOTITOLI ---
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['it', 'en'],
        # Trucco fondamentale: se il sottotitolo fallisce, non bloccare tutto il programma
        'ignoreerrors': True, 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\n--- Download in corso ---")
            ydl.download([url])
            print("\n--- Processo Terminato ---")
            print(f"Controlla la cartella: {os.path.abspath(download_path)}")
    except Exception as e:
        print(f"Errore critico: {e}")

if __name__ == "__main__":
    link_video = "https://youtube.com/watch?v=XxlBMIbhkTo"
    download_video_finale(link_video)
