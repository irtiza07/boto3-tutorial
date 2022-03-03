import boto3

TOPIC_ARN = "arn:aws:sns:us-east-1:725314774014:youtube_test_topic"
sns = boto3.client("sns")

# TODO: Create new topic
response = sns.create_topic(Name="youtube_test_topic")
print(response)

# TODO: List all topics
response = sns.list_topics()
print(response["Topics"])

# TODO: Publish to topics
for i in range(100):
    sns.publish(TopicArn=TOPIC_ARN, Message=f"Hello World! {i}")
