# import time
#
#
# # current_time = time.time()
# # print(current_time)
#
# def speed_calc_decorator(function):
#     def wrapper_function():
#         time_before_run = time.time()
#         function()
#         time_after_run = time.time()
#         print(f"{function.__name__} run time: {time_after_run - time_before_run}s")
#
#     return wrapper_function
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()

from typing import Union
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Not authenticated")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")



user = User("angela")

create_blog_post(user)
user.is_logged_in = True
create_blog_post(user)


