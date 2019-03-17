import Evtx.Evtx as evtx
import Evtx.Views as e_views

from bs4 import BeautifulSoup

""" One Object Parsing """
FilePath = "C:\Windows\System32\winevt\Logs\Security.evtx"

with evtx.Evtx(FilePath) as evtx:
    record = evtx.get_file_header()
    print(record)