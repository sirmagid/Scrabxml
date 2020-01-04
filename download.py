import io
import os
import subprocess
import json
from pprint import pprint

#def extract_audio(video):
#    command = "wget {video} ".format(video=video)
#    subprocess.call(command,shell=True)

#extract_audio('http://choobakmusic.ir/appchoobakmusic/upload/content_file/0048-2018-02-20.mp4')

def extract_audio(video,output):
    command = "ffmpeg -i {video} -vf  scale=320:240 {output}".format(video=video, output=output)
    subprocess.call(command,shell=True)

with open('list_mp4.json') as f:
    data = json.load(f)


for x in data:
 #print(x) 
 filename = x[x.rfind("/")+1:]
 filename_small = filename.replace(".", "_320X240.")
 extract_audio(x,filename_small)
 
#load from file
#print(filename_small) 
#extract_audio(x) 
    
    #pprint(data[data])
   
   
 #for d in data:
 #   for key in d.keys():
 #       print(d[key])
        
    
#pprint(data[])

#with open('list_mp4.json') as f:
    
#    a=f.readlines()
#    a = a.replace("%5Cr%5Cn","")
#    print a
    
#extract_audio(f.readlines())   
#f = open("list_mp4.txt", "r")
#for x in f:
#  print(x)
