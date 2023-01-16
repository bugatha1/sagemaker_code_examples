The Dockerfile

The Dockerfile describes the image that we want to build. You can think of it as describing the complete operating system installation of the system that you want to run.

Unlike SageMaker notebook instances, in SageMaker studio, you will not need the build_and_push.sh script anymore. The studio-build CLI will handle pushing the container to ECR for you.


The SageMaker Studio Image Build CLI uses Amazon Elastic Container Registry and AWS CodeBuild so we need to ensure that the role we provide as input to our CLI commands has the necessary policies and permissions attached.

![image](https://user-images.githubusercontent.com/63837999/212499305-10ba315b-5db0-40b0-8300-dde0a7c3fe35.png)

Exception 1 : botocore.exceptions.ClientError: An error occurred (AccessDeniedException) when calling the CreateProject operation: User: user is not authorized to perform: codebuild:CreateProject on resource: role because no identity-based policy allows the codebuild:CreateProject action

To resolve the above exception need to do 2 things.
1. udpate trust policy with codebuild
2. Attach some new permissions to executin role

refer "Ensure the role that will be used has the following" section in below link 

https://sagemaker-examples.readthedocs.io/en/latest/aws_sagemaker_studio/sagemaker_studio_image_build/xgboost_bring_your_own/Batch_Transform_BYO_XGB.html


![image](https://user-images.githubusercontent.com/63837999/212509464-13f63d97-5757-4405-86cb-6b0a548b5b45.png)



 
 
