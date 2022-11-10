#!/usr/bin/python

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

c_1 = challenge[2][1]
c_2 = challenge[2][0]
c_3 = challenge[3]

print("My", c_1, "! The", c_2, "do", c_3)

