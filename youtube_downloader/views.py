from django.shortcuts import render
#pytube package used
from pytube import YouTube

# Create your views here.

def ytb_down(request):
    return render(request, 'ytb_main.html')

def yt_download(request): 
    url = request.GET.get('url')
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.streams.all()

    for i in strm_all:
        resolutions.append(i.resolution)
        resolutions = list(dict.fromkeys(resolutions))
    # resolutions = list(dict.fromkeys(resolution))
    #  print('resolutions :', resolutions)
    #  print('url :', url)
  
    embed_link = url.replace("watch?v=","embed/")
    
#     d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
# try: 
#     # downloading the video 
#     d_video.download(SAVE_PATH) 
# except: 
#     print("Some Error!") 
# print('Task Completed!')

    
       #  return render(request, 'yt_download.html')
    return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link})
   
