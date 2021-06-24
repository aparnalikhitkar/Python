import time

starttime = time.time()
lasttime = starttime
lapnum = 1
print("Press Enter to count laps .\n press CTRL+C to stop")
try:
    while True:
        # Input for the Enter Key press
        input()
    # the current lap time
        laptime = round((time.time() - lasttime), 2)

    # Total time elapsed
    # since the timer started

    toataltimetime - round((time.time() - starttime), 2)
    print("lap No " + str(lapnum))
    print("Total time  " + str(totaltime))
    print("lap No " + str(laptime))

    print("*" * 20)
    lasttime = time.time()
    lapnum += 1
except KeyboardInterrupt:
    print("Done")