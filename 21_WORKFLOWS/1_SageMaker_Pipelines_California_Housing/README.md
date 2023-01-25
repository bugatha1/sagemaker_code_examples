

https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/tabular/tensorflow2-california-housing-sagemaker-pipelines-deploy-endpoint/tensorflow2-california-housing-sagemaker-pipelines-deploy-endpoint.html

Evaluate the model performance - mean square error (MSE). * If MSE is higher than threshold, use a Lambda step to send an E-Mail to the Data Science team. * If MSE is lower than threshold, register the model into the Model Registry, and use a Lambda step to deploy the model to SageMaker Endpoint.

!tar -zxf cal_housing.tgz --no-same-owner

