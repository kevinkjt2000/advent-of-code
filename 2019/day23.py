from queue import Queue
import threading
from time import sleep
from intcode import run_program


SLEEP_INTERVAL = 0.001
NAT_X, NAT_Y = None, None
NAT_LOCK = threading.Lock()
DIE = threading.Event()


if __name__ == "__main__":
    program = list(map(int, open("day23.input", "r").read().split(",")))
    queues = [Queue() for i in range(50)]
    def create_receiver(net_addr):
        def receive():
            yield net_addr
            while not DIE.is_set():
                if queues[net_addr].empty():
                    yield -1
                    sleep(SLEEP_INTERVAL)
                else:
                    x, y = queues[net_addr].get()
                    yield x
                    yield y
        return receive

    threads = []
    for net_addr in range(50):
        def work(net_addr):
            global NAT_X, NAT_Y
            og = run_program(program.copy(), create_receiver(net_addr))
            while not DIE.is_set():
                try:
                    dest_net_addr, x, y = next(og), next(og), next(og)
                    if dest_net_addr == 255:
                        with NAT_LOCK:
                            NAT_X, NAT_Y = x, y
                        continue
                    queues[dest_net_addr].put((x, y))
                except StopIteration:
                    break
        t = threading.Thread(target=work, args=(net_addr,))
        threads.append(t)
        t.start()

    def nat_work():
        prev_y = None
        while not DIE.is_set():
            with NAT_LOCK:
                if NAT_Y and all(map(lambda q: q.empty(), queues)):
                    if prev_y == NAT_Y:
                        DIE.set()
                        print("duplicate NAT_Y", NAT_Y)
                        break
                    queues[0].put((NAT_X, NAT_Y))
                    prev_y = NAT_Y
            sleep(SLEEP_INTERVAL)
    nat_thread = threading.Thread(target=nat_work)
    nat_thread.start()

    while any(map(lambda t: t.is_alive(), threads)):
        t.join(SLEEP_INTERVAL)
    nat_thread.join()
