import csv
import os
from halo import Halo
import base64
import json

DROP = {1, 3}
processed_data = []


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


processing_spinner = Halo(text="Processing heads.csv...", spinner="dots")
processing_spinner.start()


def make_texture(hash):
    data = {
        "textures": {"SKIN": {"url": f"http://textures.minecraft.net/texture/{hash}"}}
    }
    return base64.b64encode(json.dumps(data).encode()).decode()


with open("heads.csv", "r", encoding="utf-8") as infile, open(
    "heads_temp.csv", "w", newline="", encoding="utf-8"
) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) == 4:
            next(reader, None)  # remove first line
            new_row = [
                val for i, val in enumerate(row) if i not in DROP
            ]  # remove 2nd and 4th columns, they are unnecessary

        else:
            new_row = row  # keep unchanged if not 4 columns
            # TODO: log if columns are not 4 i.e. already filtered using spinner.info()

        writer.writerow(new_row)
        processed_data.append(new_row)


# Replace original file
os.replace("heads_temp.csv", "heads.csv")
processing_spinner.succeed(
    f"{bcolors.OKGREEN}Finished processing heads.csv!{bcolors.ENDC}"
)
resetting_spinner = Halo(text="Resetting files...", spinner="dots")
resetting_spinner.start()


def reset_files():
    with open(
        "data/allplayerheads/function/load.mcfunction", "w", encoding="utf-8"
    ) as loadfile:
        loadfile.write("# we must create all triggers here\n")
        loadfile.write("scoreboard objectives add get_head trigger\n")
        loadfile.write("scoreboard objectives add version trigger\n")
    with open(
        "data/allplayerheads/function/tick.mcfunction", "w", encoding="utf-8"
    ) as tickfile:
        tickfile.write("scoreboard players enable @a get_head\n")
        tickfile.write("scoreboard players enable @a version\n")
        tickfile.write(
            "execute as @a[scores={get_head=1..}] at @s run function allplayerheads:handle_trigger\n"
        )
        tickfile.write("scoreboard players set @a[scores={get_head=1..}] get_head 0\n")
        tickfile.write(
            "execute as @a[scores={version=1..}] run function allplayerheads:version\n"
        )
        tickfile.write("scoreboard players set @a[scores={version=1..}] version 0")


reset_files()
resetting_spinner.succeed(f"{bcolors.OKGREEN}Finished resetting files!{bcolors.ENDC}")

trigger_spinner = Halo(text="Creating triggers", spinner="dots")
trigger_spinner.start()
with open("heads.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader, start=1):
        with open(
            "data/allplayerheads/function/load.mcfunction", "a", encoding="utf-8"
        ) as loadfile:
            texture = make_texture(row[1].strip())
            loadfile.write(
                f'data modify storage allplayerheads:data heads.{index} set value {{texture: "{texture}"}}\n'
            )
trigger_spinner.succeed(f"{bcolors.OKGREEN}Finished creating data!{bcolors.ENDC}")
version_spinner = Halo(text="Setting version...", spinner="dots")
version_spinner.start()
with open("version.txt", "r", encoding="utf-8") as versionfile:
    version = versionfile.read().strip()
with open(
    "data/allplayerheads/function/version.mcfunction", "w", encoding="utf-8"
) as versionfile:
    versionfile.write(f'tellraw @s {{"text": "Version {version}"}}\n')
version_spinner.succeed(f"{bcolors.OKGREEN}Finished setting version!{bcolors.ENDC}")
