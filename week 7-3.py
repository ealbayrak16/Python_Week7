"""Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
 Then New Yorker article on wind farms...
Output :
franky
sinatra123"""
import regex as re
text_ = """The advencements in biomarine studies franky@google.com with the investments necessary and Davos
sinatra123@yahoo.com.Then New Yorker article on wind farms..."""
x = re.findall("[a-zA-Z0-9_.-]+@",text_)
for i in range(len(x)):
    print(x[i][:-1])