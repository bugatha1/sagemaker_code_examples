https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/tabular/lambda-step/sagemaker-pipelines-lambda-step_outputs.html

This notebook illustrates how a Lambda function can be run as a step in a SageMaker Pipeline.

The steps in this pipeline include: * Preprocess the Abalone dataset * Train an XGBoost Model * Evaluate the model performance * Create a model * Deploy the model to a SageMaker Hosted Endpoint using a Lambda Function, through SageMaker Pipelines