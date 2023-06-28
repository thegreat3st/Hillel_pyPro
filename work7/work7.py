import multiprocessing
import os
import requests
import threading
from threading import Thread
import time

class multi():
    
    def __init__(self, path: str, image_url: str) -> None:
        self._path = path
        self._image_url = image_url
        
    def mafile(self):
        with open(self._path, "r", encoding="latin-1") as file:
            myNames = [line.strip() for line in file]
        return myNames
        
    # CPU-bound task (heavy computation)
    def encrypt_file(self):
        print(f"Processing image from {self._image_url} in process {os.getpid()}")
        # Simulate heavy computation by sleeping for a while
        _ = [i for i in range(100_000_000)]

    # I/O-bound task (downloading image from URL)
    def download_image(self):
        print(f"Downloading image from {self._image_url} in thread {threading.current_thread().name}")
        res = requests.get(self._image_url, stream=True)
        filename = f"{self._image_url.split('/')[-3]}.jpg"
        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)

    def encryption_counter(self):
        
        start = time.perf_counter()
        dishes: list = [multi.mafile(self)]
        threads: list[multiprocessing.Process] = [
            multiprocessing.Process ( 
                target= multi.encrypt_file(self),
                args= [dish],
            )
        for dish in dishes
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread. join()
            
        return (time.perf_counter() - start)
    
    def download_counter(self):
        
        start = time.perf_counter()

        worker = Thread(
            target=multi.download_image(self)
            )
        worker.daemon = True
        worker.start()
        
        worker.join()
        
        return (time.perf_counter() - start)
    
    def total(self):
        return multi.download_counter(self) + multi.encryption_counter(self)
    
def main():
    
    try:
        mul = multi("rockyou.txt", "https://picsum.photos/1000/1000")
        dict = {"Time taken for encryption task": mul.encryption_counter(),
                "I/O-bound task": mul.download_counter(),
                "Total" : mul.total()
        }
        print(f"{dict}")
    except Exception as e:
        print(f"Error occurred: {e}")
        
if __name__ == "__main__":  
        start = time.perf_counter()
        main()
        print(f"All cooking time: {time.perf_counter() - start}")
