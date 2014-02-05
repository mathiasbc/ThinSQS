# -*- coding: utf-8 -*-

from boto.sqs.connection import SQSConnection
from boto.sqs.message import Message


class SQSQueue(object):
    '''Interface to the Amazon SQS queue using boto'''
    def __init__(self, queue_name, SQS_ACCESS_KEY, SQS_SECRET_KEY):
        # at this point we should be connected to SQS
        self.conn = SQSConnection(SQS_ACCESS_KEY, SQS_SECRET_KEY)
        # get the queue we need to deal with
        self.queue = self.conn.get_queue(queue_name)

    def createMessage(self, body=None):
        '''returns a SQS message to be enqued'''
        msg = Message()
        msg.set_body(body)
        return msg

    def writeMessage(self, message):
        '''writes a message to the queue'''
        return self.queue.write(message)

    def pushMessage(self, body):
        '''creates and writes a message to the queue, 
        createMessage + writeMessage in one step'''
        msg = Message()
        msg.set_body(body)
        return self.queue.write(msg)

    def getMessages(self, n):
        '''returns n messages erasing them, mutliple of 10'''
        msgs=[]
        rs=self.queue.get_messages(10)
        if len(rs) < 1:
            return []
        msgs.extend(rs)
        count = 10
        while count < n:
            rs=self.queue.get_messages(10)
            msgs.extend(rs)
            count += 10
            if len(rs) < 10:
                break
        # delete pulled messages
        for msg in msgs:
            self.queue.delete_message(msg)

        return msgs

    def getAllMessages(self):
        '''Returns all the messges in a queue, since SQS just does 10'''
        all_messages=[]
        rs=self.queue.get_messages(10)
        while len(rs)>0:
            all_messages.extend(rs)
            rs=self.queue.get_messages(10)
        # delete pulled messages
        for msg in all_messages:
            self.queue.delete_message(msg)
        return all_messages

    def count(self):
        ''''returns the size of the queue'''
        return self.queue.count()

    def clearQueue(self):
        '''Erases messages in the queue'''
        self.queue.clear()




