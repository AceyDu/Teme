description = ('Country',
               ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ',
                '2016 ', '2017 ', '2018 ', '2019 ']
               )

year_list = [int(year) for year in description[1]]

dataset = [
 ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
 ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
 ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
 ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
 ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
 ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 ', ': ', '96 ']),
 ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
 ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
 ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
 ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
 ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
 ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
 ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
 ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
 ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
 ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
 ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
 ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
 ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
 ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
 ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
 ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
 ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 ', '95 ']),
 ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ', '82 ', '85 ']),
 ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
 ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
 ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
 ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
 ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
 ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
 ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
 ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
 ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
 ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ', '93 ', '96 ']),
 ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
 ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
 ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
 ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
 ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

country_list = [dataset[i][0] for i in range(len(dataset))]

coverage_list_pre1 = [dataset[i][1] for i in range(len(dataset))]
coverage_list = list()
for i in range(len(coverage_list_pre1)):
    coverage_list_pre2 = list()
    for j in range(len(coverage_list_pre1[i])):
        coverage_data = 0
        if coverage_list_pre1[i][j] != ': ':
            coverage_data = int(coverage_list_pre1[i][j])
        coverage_list_pre2.append(coverage_data)
    coverage_list.append(coverage_list_pre2)


values_list = list()
for b in range(len(coverage_list)):
    year_coverage_list = list()
    for c in range(len(year_list)):
        element = dict()
        value1 = year_list[c]
        value2 = coverage_list[b][c]
        element['year'] = value1
        element['coverage'] = value2
        year_coverage_list.append(element)
    values_list.append(year_coverage_list)

dataset_dictionary = dict()
for a in range(len(country_list)):
    country_name = country_list[a]
    country_data = values_list[a]
    dataset_dictionary[country_name] = country_data


def get_year_data(data_set, year):
    result_dict = dict()
    dict_key = year
    dict_value = list()
    for a_key, a_value in data_set.items():
        list_to_be_made_tuple = list()
        country = a_key
        year_and_coverage_list = a_value
        for i in range(len(year_coverage_list)):
            if year_and_coverage_list[i]['year'] == year:
                coverage = year_and_coverage_list[i]['coverage']
                list_to_be_made_tuple.extend([country, coverage])
                tuples_to_be_added_to_dict_value = tuple(list_to_be_made_tuple)
                dict_value.append(tuples_to_be_added_to_dict_value)
    result_dict[dict_key] = dict_value
    print(result_dict)


# get_year_data(dataset_dictionary,2019)


def get_country_data(data_set, country):
    result_dict = dict()
    dict_key = country
    dict_value = list()
    for i in range(len(data_set[country])):
        list_to_be_made_tuple = list()
        year = data_set[country][i]['year']
        coverage = data_set[country][i]['coverage']
        list_to_be_made_tuple.extend([year, coverage])
        tuples_to_be_added_to_dict_value = tuple(list_to_be_made_tuple)
        dict_value.append(tuples_to_be_added_to_dict_value)
    result_dict[dict_key] = dict_value
    print(result_dict)


# get_country_data(dataset_dictionary, 'RO')


def perform_average(data_set, country):
    coverage_sum = 0
    year_counter = 0
    for i in range(len(data_set[country])):
        year_counter += 1
        coverage_sum += data_set[country][i]['coverage']
    result_average = float(coverage_sum / year_counter)
    print(result_average)


#perform_average(dataset_dictionary, 'XK')