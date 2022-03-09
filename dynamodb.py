import boto3

client = boto3.client("dynamodb")

# TODO: Get Item
# Result: {'customer_id': {'N': '1'}, 'name': {'S': 'Bob'}}
# response = client.get_item(
#     TableName="customer",
#     Key={"customer_id": {"N": "1"}},
#     AttributesToGet=["customer_id", "name"],
# )
# print(response)

# TODO: Delete Item
# response = client.delete_item(TableName="customer", Key={"customer_id": {"N": "1"}})
# print(response)

# TODO: Put Item
# response = client.put_item(
#     TableName="customer",
#     Item={"customer_id": {"N": "4"}, "name": {"S": "NewLarry"}},
#     ConditionExpression="attribute_not_exists(customer_id)",
# )

# TODO: Update Item
# response = client.update_item(
#     TableName="customer",
#     Key={"customer_id": {"N": "2"}},
#     AttributeUpdates={"name": {"Value": {"S": "MissingName"}, "Action": "PUT"}},
# )
