import requests
import info.py
def function_work_html_ratio(i):
    html_text = requests.get(info.base_URL+'/?ratio='+str(i), headers={"User-Agent": info.user_agent}).text
    