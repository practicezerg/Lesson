
import datetime

sw = "swich "
port = "port"
time = datetime.datetime.now()
time2 = str(time)
time2 = time2.replace(":", "-").replace(".", "--")
print(time2)
my_file = open("{}".format(time2), "w+")
my_file.write("{} + {}".format(sw, port))
my_file.close()
