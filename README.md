ThinSQS
=========

A thin wrapper around SQS's boto. Adds some functionality like pulling n messages and deleting them after read.

Installing:

This package makes use of python boto library, so go ahead and install it:

    $ pip install boto

Then clone the ThinSQS repo and include it on your project:

    $ git clone https://github.com/mathiasbc/ThinSQS.git

Usage:

```python
from ThinSQS.thinsqs import SQSQueue

MyQueue = SQSQueue(
        queue_name='my_queue',
        SQS_ACCESS_KEY='myaccesskey',
        SQS_SECRET_KEY='mysqssecret'
    )

# this will create a message and push it to the queue
MyQeue.pushMessage(body='Hello World !')

# get 10 messages from the queue, and delete them
messages = MyQueue.getMessages(10)

# show queue size
print MyQueue.count()

# Empty the queue
MyQueue.clearQueue()

```
