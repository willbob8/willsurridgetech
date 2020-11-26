import csv
source_file = open('Wifi info - Static IP to export.csv', 'r')
output_file = open('04-pihole-static-dhcp.conf', 'w')
reader = csv.reader(source_file)

for row in reader:
    string_list = ",".join(row)
    if string_list != ",,,":
        while("" in row) :
            row.remove("")
        if len(row) == 3:
            output_file.write("dhcp-host=" + string_list + "\n")

output_file.close()
