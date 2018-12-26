import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name='us-west-2')
# Get the queue
queue = sqs.get_queue_by_name(QueueName='fridge')
print("Queue init")

def GetMessages():
  print("Getting Messages")
  messages = []
  # Process messages by printing out body
  for message in queue.receive_messages():
    # Print out the body of the message
    messages.append(message.body)
    # Let the queue know that the message is processed
    message.delete()
  return messages