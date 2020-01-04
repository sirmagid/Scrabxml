#!/usr/bin/python
# enable debugging
import cgitb
import io
import os
import subprocess
import json
import urllib2
from pprint import pprint

cgitb.enable()
print "Content-Type: text/plain\r\n\r\n"
print
print "run"


filename = os.environ['QUERY_STRING'] #os.environ['QUERY_STRING'] 7395-2018-09-04_320X240.mp4
filename_small = filename.replace(".","_320X240.")
address_tispoon="http://downloadline.ir/tispoonpanel/upload/content_file/"+filename
print(filename_small)
print(address_tispoon)

def extract_audio(video,output):
    command = "ffmpeg -i {video} -vf  scale=320:240 {output}".format(video=video, output=output)
    subprocess.call(command,shell=True)
    
extract_audio(address_tispoon,filename_small)

# SearchParams is an array of type [['key','value'],['key','value']]
# for example 'k1=val1&data=test' will transform to 
#[['k1','val1'],['data','test']]
#for key, value in SearchParams:
    #print('<b>' + key + '</b>: ' + value + '<br>\n')
    
    

#dir_path = os.path.dirname(os.path.realpath(__file__))
#print dir_path
#path = '/home/sirmagid/public_html/tisfoon'
#text_files = [f for f in os.listdir(path) if f.endswith('.mp4')]

#for x in text_files: 
#   address_file=x.replace("_320X240.",".")
#   ret = urllib2.urlopen('http://downloadline.ir/tispoonpanel/upload/content_file/'+address_file)
#   if ret.code == 200:
#    print "Exists!"
#   else:
#    print "NotExists!"


#print text_files
