import csv
import time

schools_list = []


def strict_school_match(schools, val):
    hits = 0
    for school_obj in schools:
        if school_obj['school'] == val and hits < 3:
            print_search_result(hits, school_obj['school'], school_obj['city'], school_obj['state'])
            hits += 1

    return hits


def lenient_match(schools, val, hits, column_name):
    values = val.split(' ')
    for school_obj in schools:
        if hits >= 3:
            break

        for v in values:
            name_ = school_obj[column_name]
            if v in name_ and hits < 3:
                print_search_result(hits, school_obj['school'], school_obj['city'], school_obj['state'])
                hits += 1
                break

    return hits


def search_schools():
    val = input('Enter Search text : ').upper()
    start = time.process_time()
    read_from_csv('sl051bai.csv')
    hits = strict_school_match(schools_list, val)
    if hits < 3:
        hits = lenient_match(schools_list, val, hits, 'school')
    if hits < 3:
        hits = lenient_match(schools_list, val, hits, 'city')
    if hits < 3:
        lenient_match(schools_list, val, hits, 'state')
    print('Time taken in s: ', time.process_time() - start)


def print_search_result(hits, school, city, state):
    print(str(hits + 1) + ". " + school)
    print(city + ', ' + state)


def read_from_csv(file_name):
    with open(file_name, newline='') as schools_file:
        schools_files_reader = csv.DictReader(schools_file)
        for row in schools_files_reader:
            result = {'school': row['SCHNAM05'], 'city': row['LCITY05'], 'state': row['LSTATE05']}
            schools_list.append(result)


if __name__ == '__main__':
    search_schools()
