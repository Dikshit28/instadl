import requests
import urllib.request

def retriver(url):
    """
    Retrieves the video from the given url and saves it to the given location.
    """
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    try:
        r=requests.get(url+"?__a=1",headers=headers)
    except:
        print("Error: Could not connect to the server.\nPlease check the url : \"",url,"\" and try again.")
        return
    if r.status_code==200:
        r=r.json()
        video_url=r["graphql"]["shortcode_media"]["video_url"]
        downloader(video_url)
    else:
        print("Error:",r.status_code)
    

def downloader(videourl):
    """
    Downloads the video from the given url and saves it to the given location.
    """
    filename=input("Enter the name of the video file or press enter to save with default name: ")+".mp4"
    if filename==".mp4":
        filename="video.mp4"
    try:
        urllib.request.urlretrieve(videourl,filename)
        print("YAY!!! Video downloaded successfully")
    except:
        print("Sorry I couldn't download the video")

if __name__=="__main__":
    url=input("Enter the url of the video: ")
    retriver(url)