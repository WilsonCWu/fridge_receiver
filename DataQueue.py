import boto3


f=open("passwords/aws_key", "r")
key = f.read().rstrip()
f=open("passwords/aws_secret", "r")
secret = f.read().rstrip()
# Get the service resource
sqs = boto3.resource(
    'sqs',
    region_name='us-west-2',
    aws_access_key_id = key,
    aws_secret_access_key = secret)

# Get the queue
queue = sqs.get_queue_by_name(QueueName='fridge')
print("Queue init")

def GetMessages():
  print("Getting AWS Messages")
  messages = []
  # Process messages by printing out body
  for message in queue.receive_messages():
    # Print out the body of the message
    messages.append(message.body)
    # Let the queue know that the message is processed
    message.delete()
  return messages
def Quit():
  return