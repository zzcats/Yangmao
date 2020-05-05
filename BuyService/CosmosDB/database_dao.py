from azure.cosmos import exceptions, CosmosClient, PartitionKey


class DatabaseDAO:
    def __init__(self, endpoint, key, database_name, container_name):
        self.key = key
        self.database_name=database_name
        client = CosmosClient(endpoint, key)
        self.database = client.create_database_if_not_exists(id=database_name)
        self.container = self.database.create_container_if_not_exists(
            id=container_name,
            partition_key=PartitionKey(path="/id"),
            offer_throughput=400
        )

    def select_by_name(self, name):
        query="SELECT * FROM c where CONTAINS(c.name, '" + name+"' ORDER BY c._ts DESC)"
        return self.select_items(query)

    def add_item(self, item_content):
        self.container.create_item(body=item_content)

    def delete_item(self, item_content):
        self.container.create_item(body=item_content)

    def select_items(self, query):
        return list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))

    def read_item(self, key):
        return self.container.read_item(key,partition_key=key)

    def update_item(self, item):
        self.container.upsert_item(item)

    #https://docs.microsoft.com/en-us/azure/cosmos-db/sql-query-offset-limit
    def list_item(self, page_number, page_count):
        #'{0} {1} cost ${2}'.format(6, 'bananas', 1.74)
        offset = (page_number - 1) * page_count
        query = "SELECT * FROM c ORDER BY c._ts DESC OFFSET {0} LIMIT {1}".format(offset,page_count)
        return self.select_items(query)


def getDBClient():
    endpoint = "https://yangmao.documents.azure.com:443/"
    key = ''
    database_name = 'yangmao'
    container_name = "product"
    instance = DatabaseDAO(endpoint, key, database_name, container_name);
    return instance