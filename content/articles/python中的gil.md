Title: Python中的GIL
Date: 2019-05-23 00:07
Author: PwnForWhat
Category: Code
Tags: Python
Slug: Python中的GIL
Status: published



> 人们只瞧见了上帝关了门，却没瞅到上帝也开了窗

### 什么是GIL？

> **GIL**即**全局解释器锁**（英语：Global Interpreter Lock，缩写**GIL**），是[计算机程序设计语言](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80)[解释器](https://zh.wikipedia.org/wiki/%E8%A7%A3%E9%87%8A%E5%99%A8)用于[同步](https://zh.wikipedia.org/wiki/%E5%90%8C%E6%AD%A5)[线程](https://zh.wikipedia.org/wiki/%E7%BA%BF%E7%A8%8B)的一种机制，它使得任何时刻仅有一个线程在执行。即便在[多核心处理器](https://zh.wikipedia.org/wiki/%E5%A4%9A%E6%A0%B8%E5%BF%83%E8%99%95%E7%90%86%E5%99%A8)上，使用 GIL 的解释器也只允许同一时间执行一个线程。
>
> From [wikipedia](https://zh.wikipedia.org/zh-hans/%E5%85%A8%E5%B1%80%E8%A7%A3%E9%87%8A%E5%99%A8%E9%94%81)

为什么需要GIL呢？网上很多博客都说是历史遗留问题。但实际上，我认为这和Python的内存管理机制有关。在Python中，每个对象都维护着一个引用计数，而当这个计数变为0时，这个对象将会被回收。如果没有GIL，两个进程对同一个对象的引用计数的更改就会导致错误，这里举个例子：

进程X删除对象A使得其引用计数减1变为0，对象A被回收。进程Y删除对象A，这本报错的。但由于没有GIL，这两个进程同时进行，所以没有报错。这是错误的。

因此，GIL的重要性不言而喻。但也是因为它，使得Python的多线程活生生地由并行变成了并发。

为了减少GIL所带来的性能损耗，我们能做什么呢？

``` 
关于Python内存管理机制，你可以查看这篇文章： https://www.cnblogs.com/geaozhang/p/7111961.html#yinyongjishu 
```

#### 被GIL削弱的多线程

> 由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等），而不是需要多处理器并行的计算密集型任务。
>
> From [Python cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p01_start_stop_thread.html)

下面是一例实验：

``` python
import queue
import time
import threading

q = queue.Queue()


def init_queue():
	for i in range(10):
		q.put(i)
		print('队列初始化完成')


def job():
	while not q.empty():
		time.sleep(0.5)
		data = q.get()
		time.sleep(0.5)
		print('任务完成')


if __name__ == '__main__':
	init_queue()
	print('=====单线程十次作业开始=====')
	start_time = time.time()
	for _ in range(10):
		job()
		print(f'作业时间：{time.time() - start_time}')
	print('=====单线程十次作业完成=====')

    init_queue()
    print('=====多线程十次作业开始=====')
    start_time = time.time()
    thread_list = [threading.Thread(target=job) for _ in range(10)]
    for t in thread_list:
        t.start()
        for t in thread_list:
            if t.is_alive():
                t.join()
    print(f'作业时间：{time.time() - start_time}')
    print('=====多线程十次作业完成=====')


```

``` 
队列初始化完成
=====单线程十次作业开始=====
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
作业时间：10.010543823242188
=====单线程十次作业完成=====
队列初始化完成
=====多线程十次作业开始=====
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
任务完成
作业时间：1.0054144859313965
=====多线程十次作业完成=====
```

值得注意的是，如果将job函数中后面一个sleep函数去掉，会导致多线程测试不能完成。具体原因还未弄清。

### 那么，计算密集型任务呢？

对于IO密集型任务，Python的伪多线程可以解决，但是对于计算密集型任务，它仍旧无法真正在同一时间调用多个函数。这个时候，多线程的作用就出来了。

``` python
import multiprocessing
import queue
import time

q = queue.Queue()


def init_queue():
	for i in range(10):
		q.put(i)
		print('队列初始化完成')


def job():
	while not q.empty():
		time.sleep(0.5)
		data = q.get()
		for i in range(20):
			data *= i
			time.sleep(0.5)
			print('任务完成')


if __name__ == '__main__':
	init_queue()
	print('=====单线程十次作业开始=====')
	start_time = time.time()
	for _ in range(10):
		job()
		print(f'作业时间：{time.time() - start_time}')
	print('=====单线程十次作业完成=====')

	init_queue()
	print('=====多进程十次作业开始=====')
	start_time = time.time()
	process_list = [multiprocessing.Process(target=job) for _ in range(10)]
	for t in process_list:
		t.start()
		for t in process_list:
			if t.is_alive():
				t.join()
	print(f'作业时间：{time.time() - start_time}')
	print('=====多进程十次作业完成=====')
```

输出结果：

``` {.wp-block-preformatted}
队列初始化完成

=====单线程十次作业开始=====

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

作业时间：10.008376598358154

=====单线程十次作业完成=====

队列初始化完成

=====多进程十次作业开始=====

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

任务完成

作业时间：1.4181747436523438

=====多进程十次作业完成=====
```

> 虽然GIL给Python的性能关上了一扇门，但是这并不意味着我们就要忽略标准库里为我们打开的每一扇窗。
