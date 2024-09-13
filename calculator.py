class DataAnalise:
    def __init__(self) -> None:
        pass

    def sum_of_elements(self, lst_numb:list):
        _sum = 0
        for i in lst_numb:
            _sum += i
        print(_sum)

    def count_unique_characters(self, s:str):
        return len(set(s))
    
    def flatten_list(self,nested_list:list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(self.flatten_list(item))
                flat_list.append(item)
        return flat_list