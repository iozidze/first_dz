# import os
# import tempfile
# import unittest
# import xml.etree.ElementTree as ET
# import zipfile
from collections import defaultdict
import time
from datetime import datetime
# from unittest.mock import mock_open, patch



testnames = {'2': {'FileSystem/'}, '3': {'FileSystem/Folder2/', 'FileSystem/Folder1/'}, '4': {'FileSystem/Folder2/DVDs/', 'FileSystem/Folder1/Important/'}, '5': {'FileSystem/Folder2/DVDs/Nothing/'}}



def test_ls_command(where):
    # Test ls command functionality
    find_level = where.split('/')
    find_level = list(filter(None, find_level))
    level_now = len(find_level)
    find_true = 0
    for i in testnames[str(level_now+2)]:
        lastsinght = ''
        realname = i
        lastsinght = lastsinght + realname[-1]
        while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
        realname = (realname.split('/'))[-1]
        if realname == "Folder2":
            find_true +=1
        if realname == "Folder1":
            find_true +=1
    if find_true == 2:
        return "ls работает успешно!"
print(test_ls_command("FileSystem"))

    

