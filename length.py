from datetime import datetime
import random
import datetime
import pytz


def get_timestamp():
    full_time = str(datetime.datetime.now()).split(" ")
    time = full_time[1].split(".")
    full_time[1] = time[0]

    date = full_time[0].split("-")

    timestamp = str(date[1] + "/" + date[2] + "/" + date[0] + " @ " + full_time[1] + "(EST)")

    return timestamp


def time_to_hq():
    full_time = str(datetime.datetime.now()).split(" ")

    new_seconds = full_time[1].split(".")
    full_time[1] = new_seconds[0]

    clean_time = full_time[1].split(":")

    FMT = "%H:%M:%S"
    first_hq_time = "15:00:00"
    second_hq_time = "21:00:00"

    OUTPUT_STRING = "Current Time:\n" + full_time[1] + "\n"

    if int(clean_time[0]) < 15:
        time_left = datetime.datetime.strptime(first_hq_time, FMT) - datetime.datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        OUTPUT_STRING += \
            ("\nNext HQ Time:\n15:00:00\n\nTime remaining to HQ: \n" + out_time[0] + " Hour(s) "
             + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)")

    elif int(clean_time[0]) < 21 and int(clean_time[0]) >= 15:
        time_left = datetime.datetime.strptime(second_hq_time, FMT) - datetime.datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        OUTPUT_STRING += \
            ("\nNext HQ Time:\n21:00:00\n\nTime remaining to HQ: \n" + out_time[0] + " Hour(s) "
                + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)")

    else:
        time_left = datetime.datetime.strptime(first_hq_time, FMT) - datetime.datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")
        fixed_hour = out_time[0].split(",")

        OUTPUT_STRING += \
            ("\nNext HQ Time:\n15:00:00\n\nTime remaining to HQ: \n" + fixed_hour[1] + " Hour(s) "
                + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)")

    return OUTPUT_STRING


def cn_insult():
    insult = "Chinese Insult:\n"
    file = open("cn_insults.txt", encoding="utf8")
    insult_list = []

    for line in file:
        insult_list.append(line)

    insult_index = random.randint(0, len(insult_list)-1)
    insult += insult_list[insult_index]

    return insult


def mick_time():
    utc_time = datetime.datetime.utcnow()
    time_zone = pytz.timezone("Europe/London")

    time = str(pytz.utc.localize(utc_time, is_dst=None).astimezone(time_zone))

    date, current_time = time.split(" ")
    current_time = current_time.split(".")
    current_time = current_time[0]

    cleaned_time = "__**Current Mick Time:**__\n" + current_time + "\n\n__**Current Mick Date:**__\n" + date

    return cleaned_time

def retrieve_nickpost():
    output = "__**Retrieved Random Archived Nickpost:\n"
    file = open("nickposts.txt")
    nickpost_list = []

    for nickpost in file:
        nickpost_list.append(nickpost)

    nickpost_index = random.randint(0, len(nickpost_list)-1)
    output += nickpost_list[nickpost_index]

    return output

#def get_aiden_homework():


def to_piglatin(message):
    output = ""
    consonant_pairs = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    vowls = ['a', 'e', 'i', 'o', 'u']
    message = message.split()
    for word in message:
        if word[:2] in consonant_pairs:
            output += word[2:] + word[:2] + "ay "
        elif not word[0] in vowls:
            output += word[1:] + word[0] + "ay "
        else:
            output += word + "way "

    return output

#def from_piglatin(message):



# print("testing")
print(to_piglatin("latin cheers alpha"))
