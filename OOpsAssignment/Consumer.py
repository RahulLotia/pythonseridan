class Consumer(object):
    def __init__(self, consumer_id, name):
        self.__consumer_id = consumer_id
        self.__name = name
        
    def get_info_id(self):
        return self.__consumer_id
    
    def get_info_name(self):
        return self.__name
    
    def set_info_id(self, consumer_id):
        self.__consumer_id = consumer_id
        
    def set_info_name(self, name):
        self.__name = name
        
    def __str__(self):
        return f"{self.__consumer_id}, {self.__name}"