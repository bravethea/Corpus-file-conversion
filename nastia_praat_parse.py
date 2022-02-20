import codecs

praat_file_path = "Mary_John_bell.TextGrid"

praat_parsed = {}


with codecs.open(praat_file_path, 'r', 'utf16') as input_file:
    text_file = input_file.read()
    metadata, data = text_file.split('item []:')[0], text_file.split('item []:')[1]
    metadata_lines = metadata.split('\n')[3:]
    duration = float(metadata_lines[1][7:]) - float(metadata_lines[0][7:])
    size = float(metadata_lines[3][7:])
    metadata_file = {'duration': duration, "size": size}
    praat_parsed['metadata_file'] = metadata_file
    praat_parsed['annotation_layers'] = {}

    # data part
    items = data.split("item [")
    number_of_layers = 0
    for i in items:
        layer_name = "layer_" + str(number_of_layers + 1)
        item = i[4:].strip().rstrip().split("intervals [")

        item_metadata = item[0]
        metadata_layer_rows = item_metadata.split('\n')
        if len(metadata_layer_rows) > 1:
            number_of_layers += 1
            type = metadata_layer_rows[0].rstrip().strip()[9: -2]
            name = metadata_layer_rows[1].rstrip().strip()[8: -1]

            duration = float(metadata_layer_rows[3].rstrip().strip()[7:]) - float(metadata_layer_rows[2].rstrip().strip()[7:])
            num_intervals = metadata_layer_rows[4].rstrip().strip()[18:]
            metadata_layer = {"type": type, "duration": duration, "name": name, "num_intervals": num_intervals}
            praat_parsed['annotation_layers'][layer_name] = {"metadata_layer": metadata_layer}

            item_data = item[1:]

            praat_parsed['annotation_layers'][layer_name]["intervals"] = {}
            number_of_intervals = 0
            for j in item_data:
                number_of_intervals += 1
                name_of_interval = "interval_" + str(number_of_intervals)
                data_list = j[4:].strip().rstrip().split('\n')
                praat_parsed['annotation_layers'][layer_name]["intervals"][name_of_interval] = {"duration": float(data_list[1].rstrip().strip()[7:]) - float(data_list[0].rstrip().strip()[7:]),
               "text":  data_list[2].strip().rstrip()[7:]}


print(praat_parsed)