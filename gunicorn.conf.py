import os

workers = os.cpu_count() + 1
bind = "0.0.0.0:5000"
accesslog = '-'
errorlog = '-'