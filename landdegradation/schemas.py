from marshmallow import Schema, fields, pprint

class GEEResults(object):
    def __init__(self, type, datasets):
        self.type = type
        self.datasets = datasets
        
class CloudDataset(object):
    def __init__(self, type, dataset, urls):
        self.type = type
        self.dataset = dataset
        self.urls = urls
        
class CloudUrl(object):
    def __init__(self, url, file_hash):
        self.url = url
        self.file_hash = file_hash
        
class CloudURLSchema(Schema):
    url = fields.Str()
    file_hash = fields.Str()
    
class CloudDatasetSchema(Schema):
    dataset = fields.Str()
    type = fields.Str()
    urls = fields.Nested(CloudURLSchema())
    
class GEEResultsSchema(Schema):
    type = fields.Str()
    datasets = fields.Nested(CloudDatasetSchema())