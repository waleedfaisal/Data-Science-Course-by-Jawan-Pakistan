from datetime import datetime

now = datetime.now()

time = now.strftime("%d/%m/%Y, %I:%M:%S %p");
print ("Current Date and Time:" ,time);
