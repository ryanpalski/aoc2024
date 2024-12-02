
            

def is_report_safe(reports: list):
    is_increasing = int(reports[1]) - int(reports[0]) > 0
    for i in range(1, len(reports)):
        diff = int(reports[i]) - int(reports[i-1])
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if is_increasing and diff < 0 or not is_increasing and diff > 0:
            return False
        
    return True

def is_report_safe_permutations(reports: list):
    # This is so bad :_)
    for i in range(-1, len(reports)):
        if i == -1:
            if is_report_safe(reports):
                return True
        safer_report = reports.copy()
        del safer_report[i]
        if is_report_safe(safer_report):
            return True
    
    return False

def safe_reports():
    file_name = "day2/reports_puzzle_input.txt"
    safe_reports = 0

    with open(file_name, "r") as file:
        for line in file:
            if is_report_safe_permutations(line.split()):
                safe_reports += 1

    return safe_reports

print(safe_reports())