import boto3

subnet1a = 'subnet-0fc4d2543f3dcc255'
subnet1b = 'subnet-09b9d0dbca4bae8a5'
subnet1c = 'subnet-0437dfe009676c434'

ec2_client = boto3.client("ec2")
ec2_client.
servicecatalog_client = boto3.client("servicecatalog")
service.
servicecatalog_client.servicecatalog.
response = ec2_client.create_fleet(
     SpotOptions= {
      'AllocationStrategy': 'lowest-price',
      'InstanceInterruptionBehavior': 'terminate',
      'SingleInstanceType': True,
      'SingleAvailabilityZone': True,
      'MinTargetCapacity': 3
    },
     LaunchTemplateConfigs = [
      {
        'LaunchTemplateSpecification': {
          'LaunchTemplateName': 'myLaunchTemplate',
          'Version': '1'
        },
        'Overrides': [
          {
            'InstanceType': 'c3.large',
            'SubnetId': subnet1a          
          },
          {
            'InstanceType': 'c3.large',
            'SubnetId': subnet1b
          },
          {
            'InstanceType': 'c3.large',
            'SubnetId': subnet1c
          },
          {
            'InstanceType': 'c4.large',
            'SubnetId': subnet1a          
          },
          {
            'InstanceType': 'c4.large',
            'SubnetId': subnet1b
          },
          {
            'InstanceType': 'c4.large',
            'SubnetId': subnet1c
          },
          {
            'InstanceType': 'c5.large',
            'SubnetId': subnet1a          
          },
          {
            'InstanceType': 'c5.large',
            'SubnetId': subnet1b
          },
          {
            'InstanceType': 'c5.large',
            'SubnetId': subnet1c
          }
        ]
      }
    ],
    TargetCapacitySpecification = {
        
      'TotalTargetCapacity': 3,
      'DefaultTargetCapacityType': 'spot'
    },
    Type='instant'
  )

ec2_service = boto3.resource("ec2")
ec2_servic
  InstanceType='t3a.xlarge',
  ElasticGpuSpecification=''
  )