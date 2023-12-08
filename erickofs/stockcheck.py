while True:
    datafile = open('data.txt', 'r', encoding='utf-8')
    try:
        for lines in datafile:
            # Strip lines of whitespace
            lines = lines.strip()
            # Strip spaces between commas
            lines = lines.replace(' ,', ',')
            # Remove lines that have double commas
            lines = lines.replace(',,', '')
            # Strip lines
            lines = lines.strip()
            # Change all letters to first letter uppercase
            lines = lines.title()
            # Apply initial filtering rules along with new ones
            if lines != '' and not lines.startswith('#') and not lines.startswith(',') and not lines.endswith(',') and lines.count(',') >= 2:
                print(lines)
        break
    except FileNotFoundError:
        # raise message if file 'data.txt' does not exist
        print("File 'data.txt' does not exist in currennt directory.")
    break

# Create a dictionary to store the data
stock = {}
for lines in datafile:
    (key, val) = lines.split(',')
    stock[key] = val
print(stock)

