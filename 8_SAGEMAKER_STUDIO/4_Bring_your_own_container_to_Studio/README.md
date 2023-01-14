The Dockerfile

The Dockerfile describes the image that we want to build. You can think of it as describing the complete operating system installation of the system that you want to run.

Unlike SageMaker notebook instances, in SageMaker studio, you will not need the build_and_push.sh script anymore. The studio-build CLI will handle pushing the container to ECR for you.


The SageMaker Studio Image Build CLI uses Amazon Elastic Container Registry and AWS CodeBuild so we need to ensure that the role we provide as input to our CLI commands has the necessary policies and permissions attached.

