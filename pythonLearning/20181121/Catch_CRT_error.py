# $language = "Python"
# $interface = "1.0"

def exe_cmd(mycmd):
    crt.Screen.WaitForStrings(["#", ">", "?"], 2)
    crt.Screen.Send(mycmd + "\n")


def Main():
    errNum = 0
    relNum = 0

    # Ensure that we don't "miss" data coming from the remote by setting
    # our Screen's Synchronous flag to true.


    while True:
        nIndex = crt.Screen.WaitForStrings(g_vWaitFors)

        if nIndex == 1:
            crt.Screen.Send("\n")
            exe_cmd("enable")

            exe_cmd("****   " + "err:" + str(errNum) + " reload:" + str(relNum) + "   ****")

            exe_cmd("reload")
            crt.Sleep(1000)
            exe_cmd("n")
            crt.Sleep(1000)
            exe_cmd("y")
            relNum = relNum + 1
        if nIndex == 2:
            errNum = errNum + 1


g_vWaitFors = [
    "Press any key to start the shell!",
    "octeon_i2c_read: bad status before read"]

Main()