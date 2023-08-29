# Flask, Gunicorn, Gevent and Asyncio Don't Mix

This is a simple sandbox appliation I put together to investigate and prove weather some problems I was running into were the result of the attempting to use the combination of these tools.

Unfortunatly, using these together results in instability when handling requests concurrently and it appears that somehow it ends up with the flask process being run within an async context which then fails when attempting to use asgiref to convert the async route handler back to syncronous.


``` shell
   1   │ 2023-08-29 16:38:10,986 DEBUG asyncio Dummy-1 : Using selector: GeventSelector
   2   │ 2023-08-29 16:38:10,987 DEBUG asyncio Dummy-2 : Using selector: GeventSelector
   3   │ 2023-08-29 16:38:10,987 ERROR app Dummy-2 : Exception on / [GET]
   4   │ Traceback (most recent call last):
   5   │   File "/usr/local/lib/python3.11/site-packages/asgiref/sync.py", line 285, in _run_event_loop
   6   │     loop.run_until_complete(coro)
   7   │   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 629, in run_until_complete
   8   │     self._check_running()
   9   │   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 590, in _check_running
  10   │     raise RuntimeError(
  11   │ RuntimeError: Cannot run the event loop while another loop is running
  12   │
  13   │ During handling of the above exception, another exception occurred:
  14   │
  15   │ Traceback (most recent call last):
  16   │   File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 2529, in wsgi_app
  17   │     response = self.full_dispatch_request()
  18   │                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  19   │   File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 1825, in full_dispatch_request
  20   │     rv = self.handle_user_exception(e)
  21   │          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  22   │   File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 1823, in full_dispatch_request
  23   │     rv = self.dispatch_request()
  24   │          ^^^^^^^^^^^^^^^^^^^^^^^
  25   │   File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 1799, in dispatch_request
  26   │     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  27   │            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  28   │   File "/usr/local/lib/python3.11/site-packages/asgiref/sync.py", line 257, in __call__
  29   │     loop_future.result()
  30   │   File "/usr/local/lib/python3.11/concurrent/futures/_base.py", line 449, in result
  31   │     return self.__get_result()
  32   │            ^^^^^^^^^^^^^^^^^^^
  33   │   File "/usr/local/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
  34   │     raise self._exception
  35   │   File "/usr/local/lib/python3.11/concurrent/futures/thread.py", line 58, in run
  36   │     result = self.fn(*self.args, **self.kwargs)
  37   │              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  38   │   File "/usr/local/lib/python3.11/site-packages/asgiref/sync.py", line 297, in _run_event_loop
  39   │     loop.run_until_complete(gather())
  40   │   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 629, in run_until_complete
  41   │     self._check_running()
  42   │   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 590, in _check_running
  43   │     raise RuntimeError(
  44   │ RuntimeError: Cannot run the event loop while another loop is running
```

As of now I don't plan on digging deeper for a solution, other than the obvious of not using these things together.  I'm posting this up in case this helps someone in the future save a bit of time troubleshooting.

It may be notable that the [asyncio-gevent](https://pypi.org/project/asyncio-gevent/) library seems to attempt to make these work together better, but in testing I didn't see any improvement.
