import time
import sys

def log(message, level="INFO"):
    print(f"[{level}] {message}")

LOG_LEVELS = {
    "INFO": "INFO",
    "WARNING": "WARNING",
    "ERROR": "ERROR",
}

def log_message(level, message):
    level_str = LOG_LEVELS.get(level, "INFO")
    log(message, level=level_str)

for i in range(5):
    if i == 0:
        log_message("INFO", "Process started")
    elif i == 3:
        log_message("WARNING", "CPU usage is high")
    elif i == 4:
        log_message("ERROR", "Process failed")
    else:
        log_message("INFO", f"Running iteration {i}")

x = 0
ellipsis = 0

timetosleep = 4
time.sleep(timetosleep)

while x != 20:
    x += 1
    message = "InfoTech Center System Booting" + "." * ellipsis
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(0.2)

    if ellipsis == 4:
        ellipsis = 0

if x == 20:
    print("\nOperating System Booted Up - Retina Scanned - Access Granted")