# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:12:16 2017

@author: User
"""

from threading import Thread
import functools
import time

def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception( e):
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception(je):
                print ('error starting thread')
                raise Exception(je)
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

@timeout(2)
def test():
    time.sleep(5)
    
if __name__ == '__main__':
    test()