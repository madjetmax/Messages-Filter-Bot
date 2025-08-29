import re

text = "Test< tewefihwfhi?fwef,wfefewwef//f/we.fw.ef"

text = re.findall(r"\w+", text, flags=re.UNICODE)
print(text)