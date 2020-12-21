import csv


def read_files_by_file_name_and_column_name(file_name, row_name):
    line_count = 0
    with open(file_name, newline='') as schools_file:
        schools_files_reader = csv.DictReader(schools_file)
        # can use sorted function from operator library to make code more simple
        state = ''
        result = {}
        schools_per_state = 0
        for row in schools_files_reader:
            current_state = row[row_name]
            if line_count > 0 and state != current_state:
                if state in result:
                    schools_per_state = result[state] + schools_per_state
                result[state] = schools_per_state
                state = current_state
                schools_per_state = 1
            else:
                if state == '':
                    state = current_state
                schools_per_state += 1

            line_count += 1
    return line_count, result


def print_counts():
    total_number_of_schools, state_wise_number_of_schools = read_files_by_file_name_and_column_name('sl051bai.csv',
                                                                                                    'LSTATE05')
    metro_centric_local_wise_schools = read_files_by_file_name_and_column_name('sl051bai.csv', 'MLOCALE')[1]
    city_wise_schools = read_files_by_file_name_and_column_name('sl051bai.csv', 'LCITY05')[1]
    city_with_max_schools = max(city_wise_schools, key=city_wise_schools.get)

    print("Total Schools : {}".format(total_number_of_schools))
    print("Schools by state : ")
    print('\n'.join("{}: {}".format(k, v) for k, v in state_wise_number_of_schools.items()))
    print("Schools by Metro-centric locale :")
    print('\n'.join("{}: {}".format(k, v) for k, v in metro_centric_local_wise_schools.items()))
    print('City with most schools: {0} ({1})'.format(city_with_max_schools, city_wise_schools[city_with_max_schools]))
    print('Unique cities with at least one school: {}'.format(len(city_wise_schools.keys())))


if __name__ == '__main__':
    print_counts()
