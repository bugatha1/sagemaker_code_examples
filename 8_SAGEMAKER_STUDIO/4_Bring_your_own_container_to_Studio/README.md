The Dockerfile

The Dockerfile describes the image that we want to build. You can think of it as describing the complete operating system installation of the system that you want to run.

Unlike SageMaker notebook instances, in SageMaker studio, you will not need the build_and_push.sh script anymore. The studio-build CLI will handle pushing the container to ECR for you.