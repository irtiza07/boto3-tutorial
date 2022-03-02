# SQS allows you to queue and then process messages
import boto3

sqs = boto3.resource("sqs")

# !TODO Create the queue
# Talk about Standard Queue vs FIFO queue
# queue = sqs.create_queue(QueueName="test", Attributes={"DelaySeconds": "5"})
# print(queue.url)
# print(queue.attributes)

# !TODO Use existing queue
# queue = sqs.get_queue_by_name(QueueName="test")

# !TODO Get all available queues
# for q in sqs.queues.all():
#     print(q.url)

# !TODO Send messages to queue
# queue = sqs.get_queue_by_name(QueueName="test")
# queue.send_message(MessageBody="Heelllooo World!")

# !TODO Send bulk messages to queue
# count = 0
# messages = []
# for i in range(0, 5):
#     messages.append({"Id": str(count), "MessageBody": f"Another order is in {count} "})
#     count += 1
# queue.send_messages(Entries=messages)

# !TODO Read Messages [Processed in batches]
# Talk about the different attributes
queue = sqs.get_queue_by_name(QueueName="test")

for message in queue.receive_messages(
    AttributeNames=["All"], MaxNumberOfMessages=10, WaitTimeSeconds=20
):
    print(message.body)
    message.delete()

# !TODO Talk about FIFO delivery logic
# https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html

# !TODO Talk about Exactly Once Processing
# https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html

# !TODO Talk about creating automated pipelines with AWS SNS & AWS Lambda
