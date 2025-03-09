# classification & Quantization
  ## Classifier.py
    This file contains implementation of Classification, Data Version Control(DVC), Experiment Tracking & Model Registry
    Dataset of 25K images with 5 classes
    Model 1 : EfficientNetv2B0(50MB) --> 97 % Accuracy
    Model 2 : Custom model with 8 layers over 524K parameters(2MB) --> 95 % of Accuracy
    DVC used for dataset versioning as well as experiment tracking and model registry.
  ## GUI.py
    This file contains a gui which prepare data for classification
    Input format
      1) Video
             select video --> Video to frames --> select frames to fall under a category in the UI & skip similar frames
      2) Shuffled Images
             same as above
  ## faceid pipeline 2.py
    Inference for the classification model
    Input format
    1) base64 --> decode --> np.array --> prediction classes
    2) Video --> Frames --> laplacian score(Desc) --> prediction classes
    3) Image --> prediction classes
  ## file categoriser.ipynb
    Categorising shuffles image class via model further used for training
  ## tflite.ipynb
    This contains how to quantise a model without drop in performace using tflite
    Representative dataset is given
    Input and output datatype should be specified
    INT8 quantisation is used
    Converted to onnxmodel & coreml
    Ray is used to improve parallel inference
# Entity extraction(Spacy) & Bio-med Roberta
    NER Extraction using Spacy & Bio-Med RoBerta
# Prompt Versioning
    Versioning LLM Prompts using MLFlow
# Segmentation
    segmentation with 1) efficientnet as encoder and custom decoder
                  2) PartialConvolution
                  3) MultiheadAttention
                  4) both segmentation and classification
# Server Automation
    Auto-mount a temporary disk from aws | azure | gcp to os disk
    Auto-clone a git repo with token
    Auto-create a virtual environment in server  and install necessary python packages
