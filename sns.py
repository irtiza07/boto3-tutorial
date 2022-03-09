import boto3

sns = boto3.client("sns")

# Create new topic
# response = sns.create_topic(Name="demo_youtube_topic")
# print(response)

# List all topics
# response = sns.list_topics()
# print(response["Topics"])

# Publish to topic
DEMO_YOUTUBE_TEST_TOPIC_SNS_ARN = (
    "arn:aws:sns:us-east-1:725314774014:demo_youtube_topic"
)
for i in range(100):
    print(f"Publishing message: {i}")
    sns.publish(TopicArn=DEMO_YOUTUBE_TEST_TOPIC_SNS_ARN, Message=f"Hello World! {i}")
