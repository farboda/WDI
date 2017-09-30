import json

#if you want run script in your local drive, you only need to edit this variable
data_set_location = "/home/farbod/Documents/Uni/WDI/"


def convert_file_to_dict(file, file_format, title_index, file_name):
    title_dict = {}

    if file_format == "csv":
        skip_first_row = True
        for line in file:
            if skip_first_row == False:
                title = line.split(",")[title_index]
                if title != "":
                    title_dict[title] = file_name
            else:
                skip_first_row = False
    return title_dict

def load_data():
    all_files_list = []

    #reading games-features.csv
    games_features_csv_file = open(data_set_location + "games-features.csv", "r")
    games_features_csv_dict = convert_file_to_dict(games_features_csv_file, "csv", 2, "games_features_csv")
    games_features_csv_file.close()
    all_files_list.append(games_features_csv_dict)

    #reading ign.csv
    ign_csv_file = open(data_set_location + "ign.csv", "r")
    ign_csv_dict = convert_file_to_dict(ign_csv_file, "csv", 2, "ign_csv")
    ign_csv_file.close()
    all_files_list.append(ign_csv_dict)

    #reading Managerial_and_Decision_Economics_2013_Video_Games_Dataset.csv
    Managerial_Dataset_csv_file = open(data_set_location + "Managerial_and_Decision_Economics"
                                                           "_2013_Video_Games_Dataset.csv", "r")
    Managerial_Dataset_csv_dict = convert_file_to_dict(Managerial_Dataset_csv_file, "csv", 1, "Managerial_Dataset_csv")
    Managerial_Dataset_csv_file.close()
    all_files_list.append(Managerial_Dataset_csv_dict)

    #reading vgsales.csv
    vgsales_csv_file = open(data_set_location + "vgsales.csv", "r")
    vgsales_csv_dict = convert_file_to_dict(vgsales_csv_file, "csv", 1, "vgsales_csv")
    vgsales_csv_file.close()
    all_files_list.append(vgsales_csv_dict)

    '''
    #reading Video_Games_5.json
    Video_Games_5_json_file = open(data_set_location + "Video_Games_5.json", "r")
    Video_Games_5_json_dict = convert_file_to_dict(Video_Games_5_json_file, "json", 1)
    Video_Games_5_json_file.close()
    all_files_list.append(Video_Games_5_json_dict)
    '''

    #reading Video_Games_Sales_as_at_22_Dec_2016.csv
    Video_Games_Sales_csv_file = open(data_set_location + "Video_Games_Sales_as_at_22_Dec_2016.csv", "r")
    Video_Games_Sales_csv_dict = convert_file_to_dict(Video_Games_Sales_csv_file, "csv", 0, "Video_Games_Sales_csv")
    Video_Games_Sales_csv_file.close()
    all_files_list.append(Video_Games_Sales_csv_dict)

    return all_files_list

def main():
    result_list = []
    all_files_list = load_data()

    for first_dict in range(0, len(all_files_list)):
        for second_dict in range(0, len(all_files_list)):
            result_dict = {}
            cnt = 1
            if first_dict != second_dict:
                for key in all_files_list[first_dict]:
                    if key in all_files_list[second_dict]:
                        value_dict = {}
                        first_value = all_files_list[first_dict][key]
                        second_value = all_files_list[second_dict][key]
                        value_dict[second_value] = cnt
                        result_dict[first_value] = value_dict
                        cnt += 1
                        #print key + " " + str(first_value) + " " + str(second_value)
            result_list.append(result_dict)
    for item in result_list:
        print item
main()
