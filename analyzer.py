log_file = "logs.txt"

info = 0
error = 0
warning = 0

with open(log_file, "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        elif "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1

with open("report.txt", "w") as report:
    report.write("Log Summary Report\n")
    report.write("-------------------\n")
    report.write(f"INFO: {info}\n")
    report.write(f"ERROR: {error}\n")
    report.write(f"WARNING: {warning}\n")

print("Report Generated!")
