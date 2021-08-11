
def parse_ranges(ranges_string):
    ranges = (number.split("-") for number in ranges_string.split(","))
    numbers = (index for start,end in ranges for index in range(int(start), int(end) + 1) )
    return " ".join( str(num) for num in numbers )
if __name__ == '__main__':
    print(parse_ranges("1-2,4-4,8-10"))