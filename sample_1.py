import boto3
import uuid

# Client: low-level service access
#s3_client = boto3.client(s3)

# Resource: higher-level object-oriented service access
#s3_resource = boto3.resource('s3')

# You can use either client or resource to interact with S3.

''' 
Also you can access the client directly via the resource 
like so: s3_resource.meta.client
'''

def create_bucket_name(bucket_prefix):
	# The generated bucket name must be between 3 and 63 chars long
	return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
	try:
		session = boto3.session.Session()
		current_region = session.region_name
		bucket_name = create_bucket_name(bucket_prefix)
		bucket_response = s3_connection.create_bucket(
			Bucket=bucket_name, CreateBucketConfiguration={
				'LocationConstraint': current_region})
		print(bucket_name, current_region)
		return bucket_name, bucket_response
	except Exception as e:
		print("Exception:\n", e)


s3_resource = boto3.resource('s3')

# first create one using the client, 
# which gives you back the bucket_response as a dictionary
first_bucket_name, first_response = create_bucket(
	bucket_prefix='test-vineet-client', 
	s3_connection = s3_resource.meta.client)

print('\nAccessing via Client\n')
print('*' * 10)
print("\n First Bucket Name:{0} \nFirst Bucket Response:{1}".format(
	first_bucket_name, first_response))

# second create one using the resource, 
# which gives you back a Bucket instance as the bucket_response
second_bucket_name, second_response  = create_bucket(
	bucket_prefix='test-vineet-resource', 
	s3_connection = s3_resource)

print('\n\nAccessing via Resources\n')
print('*' * 10)
print("\n Second Bucket Name:{0} \nSecond Bucket Response:{1}".format(
	second_bucket_name, second_response))


