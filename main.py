import subprocess
from sys import path
from web_cache_deception_helper import WCDhelper
from utils import *


if __name__ == "__main__":

    arg=command_parser()
    # init url crawler
    subprocess.Popen(['python','urlcrawler.py','--url',arg.url]).communicate() 
    
    helper=WCDhelper()
    data=html2list(f'./data/{arg.url[8:-1]}.html')

    query_url=helper.url_grouping(data,1)
    path_url=helper.url_grouping(data,2)

    possible_url1=helper.pathurl_helper(path_url)
    possible_url2=helper.queryurl_helper(query_url)
    
    createFolder('result')
    writeFile(f'./result/{arg.url[8,-1]}1.txt',possible_url1)
    writeFile(f'./result/{arg.url[8,-1]}2.txt',possible_url2)
