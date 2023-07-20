import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/barad/Downloads/python/projeto_103"

class fileEventHandle(FileSystemEventHandler):
    def on_created(self,event):
        print(f'{event.src_path}foi criado')
    def on_deleted(self,event):
        print(f'{event.src_path}foi apagado')
    def on_modified(self,event):
        print(f'{event.src_path}foi modificado')    
    def on_moved(self,event):
        print(f'{event.src_path}foi movido pra{event.dest_path}')
event_handle = fileEventHandle()
observer = Observer()
observer.schedule(event_handle,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
        print('funcionando')
except KeyboardInterrupt:
    print('interronpido')
    observer.stop()