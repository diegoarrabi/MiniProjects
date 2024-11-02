from subprocess import run, PIPE
from os import path


def fullFilePath(file_name: str) -> str:
    return path.join(str(path.dirname(__file__)), file_name)

def batteryStatus() -> dict[int, bool]:
    battery_status_dict = {"battery_level": 0, "charge_state": 0}
    process_return = run(["pmset", "-g", "batt"], capture_output= True, text= True)
    result_raw = (process_return.stdout).split("\t")
    battery_status = result_raw[1].split(";")
    battery_status_dict["battery_level"] = int(battery_status[0][:-1])
    battery_status_dict["charge_state"] = chargingStatus(str(battery_status[1][1:]).lower())
    return battery_status_dict

def chargingStatus(charging_status: str) -> bool:
    if charging_status == "charging" or charging_status == "chargedsub":
        return True
    elif charging_status == "discharging":
        return False
    else:
        return None

def checkChargeAlertStatus() -> dict[bool, bool]:
    charge_alert_dict = {"charging_alert": False, "discharging_alert": False}
    charge_alert_list = []
    file_name_list = [charge_file_name, discharge_file_name]
    for individual_file in file_name_list:
        file_path = fullFilePath(individual_file)
        with open(file_path, "r") as file_open:
            file_data = file_open.read() == "1"
            charge_alert_list.append(file_data)
    charge_alert_dict["charging_alert"] = bool(charge_alert_list[0])
    charge_alert_dict["discharging_alert"] = bool(charge_alert_list[1])
    return charge_alert_dict

def sendChargingAlert() -> None:
    run(["osascript", "-e", charged_string])
    with open(fullFilePath(charge_file_name), "w") as file_open:
        file_open.write("1")

def sendDischargingAlert() -> None:
    run(["osascript", "-e", discharged_string])
    with open(fullFilePath(discharge_file_name), "w") as file_open:
        file_open.write("1")

    
charged_string = 'display notification "Remove power source" with title "Laptop at 80%" sound name "Frog"'
discharged_string = 'display notification "Connect power source" with title "Laptop below 20%" sound name "Frog"'

charge_file_name = "charge_notification"
discharge_file_name = "discharge_notification"

charging_alert = checkChargeAlertStatus()["charging_alert"]
discharging_alert = checkChargeAlertStatus()["discharging_alert"]
battery_level = batteryStatus()["battery_level"]
charge_state = batteryStatus()["charge_state"]

# print(f'Battery Percent: {battery_level}')
# print(f'Is charging: {charge_state}')
# print(f'Charged Alert Sent: {charging_alert}')
# print(f'Discharge Alert Sent: {discharging_alert}')





if charge_state and (battery_level > 80) and not charging_alert:
    # print("charging, battery is greater than 80, and alert has not been sent")
    sendChargingAlert()

if not charge_state and (battery_level > 80) and charging_alert:
    # print("not charging, battery is greater than 80, and alert already sent")
    with open(fullFilePath(charge_file_name), "w") as file_open:
        file_open.write("0")



if not charge_state and (battery_level < 20) and not discharging_alert:
    # print("not charging, battery is less than 20, and alert has not been sent")
    sendDischargingAlert()

if charge_state and (battery_level < 20) and discharging_alert:
    # print("charging, battery is less than 20, and alert already sent")
    with open(fullFilePath(discharge_file_name), "w") as file_open:
        file_open.write("0")




    
