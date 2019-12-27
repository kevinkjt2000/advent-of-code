from queue import Queue
import threading
from time import sleep
from intcode import run_program


DIE = threading.Event()


# Thanks StackOverflow https://stackoverflow.com/a/325528/2607949
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


if __name__ == "__main__":
    program = list(map(int, open("day23.input", "r").read().split(",")))
    queues = [Queue() for i in range(50)]
    def create_receiver(net_addr):
        def receive():
            print("booting", net_addr)
            yield net_addr
            while not DIE.is_set():
                if queues[net_addr].empty():
                    yield -1
                    sleep(0.01)
                else:
                    x, y = queues[net_addr].get()
                    yield x
                    yield y
        return receive

    threads = []
    for net_addr in range(50):
        def work():
            og = run_program(program.copy(), create_receiver(net_addr))
            while True:
                try:
                    dest_net_addr, x, y = next(og), next(og), next(og)
                    if dest_net_addr == 255:
                        print("answer", y)
                        DIE.set()
                        break
                    print("sending", (dest_net_addr, x, y))
                    queues[dest_net_addr].put((x, y))
                except StopIteration:
                    break
        t = StoppableThread(target=work)
        threads.append(t)
        t.start()

    for t in threads:
        if DIE.is_set():
            t.stop()
        t.join(0.01)
