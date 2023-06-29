import requests
from queue import Queue
from threading import Thread
from time import perf_counter

NUM_THREADS = 3
q = Queue()


def download_img():
    """
    Download image from img_url in curent directory
    """
    global q

    while True:
        img_url = q.get()

        res = requests.get(img_url, stream=True)
        filename = f"{img_url.split('/')[-3]}.jpg"

        with open(filename, "wb") as f:
            for block in res.iter_content(1024):
                f.write(block)
        q.task_done()


def main():
    image = [
        "https://picsum.photos/id/100/1000/1000",
        "https://picsum.photos/id/200/1000/1000",
        "https://picsum.photos/id/300/1000/1000",
    ]

    for img_url in image[0:3]:
        q.put(img_url)

    for t in range(NUM_THREADS):
        worker = Thread(target=download_img)
        worker.daemon = True
        worker.start()
    q.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"&{perf_counter() - start}")
