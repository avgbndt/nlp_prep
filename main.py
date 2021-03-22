from tools.Normalize import *

my_text = Normalize('./sample.csv')
my_text.load()
my_text.clean_contents()
my_text.show()