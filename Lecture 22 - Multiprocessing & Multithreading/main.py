import threading
# from threading import Thread
import time
import requests, multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def worker(task):
    print(f"worker {task} started")
    time.sleep(2)
    print(f"worker {task} finished")

start = time.time()

# worker('Task1')
# worker('Task2')

thread1 = threading.Thread(target=worker, args=('Task1',), name='1st thread')
thread2 = threading.Thread(target=worker, args=('Task2',), name='2nd thread')

thread1.start()
thread2.start()

print(threading.active_count())
print(threading.enumerate())

thread1.join()
thread2.join()

print(threading.active_count())
print(threading.enumerate())


end = time.time()
print(f"Total time taken: {end - start}")


def fetch_info(task, post_id):
    print(f'Fetching data from {task}...')

    BASE_URL = 'https://jsonplaceholder.typicode.com/todos/{id}'

    response = requests.get(BASE_URL.format(id=post_id))

    return response.json()


start = time.time()

thread_list = []

for i in range(1, 11):
    # fetch_data(f'Task{i}', i)

    thread = threading.Thread(target=fetch_info, args=(f'Task{i}', i))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end = time.time()
print(f"Total time taken: {end - start}")


# lock = threading.Lock()
# counter = 0

# def increment():
#     global counter
#     for _ in range(100_000):
#         with lock:
#             counter += 1  

# threads = [threading.Thread(
#     target=increment) for _ in range(5)]

# for t in threads: t.start()
# for t in threads: t.join()
# print(counter)



def increment():
    counter = 0

    for _ in range(100_000):
        counter += 1  

    print(counter)


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=increment) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


f_name = __name__
print(__name__)


urls = [f'https://jsonplaceholder.typicode.com/comments/{i}' for i in range(1, 21)]

def fetch_data(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


with ThreadPoolExecutor(max_workers=5) as executor:
    result = list(executor.map(fetch_data, urls))
    
print(result)