while True:
    datafile = open('data.txt', 'r', encoding='utf-8')
    try:
        for lines in datafile:
            stock = {}
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
                # DEBUG Print lines
                # Sort the words before first comma alphabetically
                print(lines)
                # Split lines by comma
                lines = lines.split(',')
                lines = list(dict.fromkeys(lines))
                lines = ','.join(lines)
                if lines != '' and not lines.startswith('#') and not lines.startswith(',') and not lines.endswith(',') and not lines.count(',') > 2:
                    lines = lines.split(',')
                # Assign variables to each element in list
                    code = lines[0]
                    quantity = lines[2]
                    # Assign variables to each element in list. If code is already in dictionary, sum the quantities
                    stock[code] = {}
                    stock[code]['quantity'] = quantity
                    # If code is in dictionary, sum the quantities
                    if code in stock:
                        stock[code]['quantity'] = int(stock[code]['quantity']) + int(quantity)
                    else:
                        stock[code] = {}
                        stock[code]['quantity'] = quantity
                    print('--->', stock)
                else:
                    continue
                #print(stock)
            else:
                continue
    except FileNotFoundError:
        # raise message if file 'data.txt' does not exist
        print("File 'data.txt' does not exist in currennt directory.")
    break

