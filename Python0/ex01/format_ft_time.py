import datetime
import time
now = datetime.datetime.now()
duration = time.time()
durationcomma = f"{duration:,}"
scientific = f"{duration:.2e}"

print("Seconds since January 1, 1970: ", durationcomma, "or", scientific, "in scientific notation")
print(now.strftime("%b %d %Y"))