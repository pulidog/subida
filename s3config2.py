# coding=utf-8
#
# config do S3 https://aws.amazon.com/articles/3998


import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto


file = open('ola.txt', 'r+')
print file
 
AWS_KEY = 'AKIAJM3VZNGYFHGUV54A'
AWS_SECRET = ')4lYv]X^n&OZ'
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)
bucket = aws_connection.get_bucket('testpulidog')

key = bucket.new_key('examples/ola.txt')
key = key.set_contents_from_filename('/home/boto/ola.txt')


for file_key in bucket.list():
    print file_key.name