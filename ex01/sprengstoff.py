from sys import stdin

class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record):
    largest_number = 0
    current_record = record
    while current_record != None:
        if current_record.value > largest_number:
            largest_number = current_record.value
        current_record = current_record.next
    return largest_number


def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()
