# Single DAO Class for CRUD operations on MongoDB

class CyberIntelDao:

    # Function to get all data from a collection in the db. (Limit is used temporary for performance purposes)
    @staticmethod
    def get_all_data(collection):
        data = collection.find({}, {"_id":0})
        return list(data)

    # Function to get data by parameters from a collection. Column param(optional) can be used to filter columns in the result
    @staticmethod
    def get_data_by_params(collection, params, columns=None):
        data = collection.find(params, columns)
        return list(data)

    # Function to get data count by parameters(optional) from a collection
    @staticmethod
    def get_data_count_by_params(collection, params=None):
        data = collection.find(params)
        return len(list(data))

    # Function to get columns of a collection from db
    @staticmethod
    def get_data_columns(collection, columns):
        data = collection.find({}, columns)
        return list(data)

    # Function to get data from a collection using aggregate function 
    @staticmethod
    def get_data_by_aggregate_func(collection, param):
        data = collection.aggregate(param)
        return list(data)

    # Function to insert data into a collection
    @staticmethod
    def insert_data(collection, data):
        return collection.insert_one(data)
    
    # Function to insert records into a collection
    @staticmethod
    def insert_records(collection, records):
        return collection.insert_many(records)

    # Function to get distinct data from a collection using certain parameters
    @staticmethod
    def get_distinct_data(collection, param):
        data = collection.distinct(param)
        return data