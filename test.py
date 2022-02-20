import text_grid_parse

class Converter:
    def __init__(self, input_path):
        self.input_path = input_path

    def detect_format(self):
        if self.input_path.endswith('.TextGrid'):
            return "implement the function to process textgrid"
        elif self.input_path.endswith('.conll'):
            return "implement the function to process conll"
        elif self.input_path.endswith('.xml'):
            return "implement the function to process xml"
        elif self.input_path.endswith('.vert'):
            return "implement the function to process vert"
        else:
            print("not recognised format")

    def process_text_grid(self):
        pass

    def process_conll(self):
        pass

    def process_xml(self):
        pass

    def process_vert(self):
        pass
