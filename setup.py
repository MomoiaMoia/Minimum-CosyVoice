from setuptools import setup, find_packages

setup(
    name='sc_cosyvoice',
    version='0.2.0',
    packages=find_packages(),
    package_data={
        "cosyvoice": [
            "tokenizer/assets/*.tiktoken",  # 添加资源文件
            "resources/zero_shot_prompt.wav"
        ],
    },
    install_requires=[
        'conformer~=0.3.2',
        'deepspeed~=0.14.0; sys_platform == "linux"',
        'diffusers~=0.27.0',
        'gdown~=5.1.0',
        'gradio~=5.4.0',
        'grpcio~=1.57.0',
        'grpcio-tools~=1.57.0',
        'huggingface-hub~=0.25.0',
        'hydra-core~=1.3.0',
        'HyperPyYAML~=1.2.0',
        'inflect~=7.3.0',
        'librosa~=0.10.0',
        'lightning~=2.2.0',
        'matplotlib>=3.7.0',
        'modelscope~=1.22.0',
        'networkx',
        'omegaconf~=2.3.0',
        'onnx==1.16.0',
        'onnxruntime-gpu==1.19.2',
        'openai-whisper==20240927',
        'protobuf~=4.25',
        'pydantic>=2.7.0',
        'rich~=13.7.0',
        'soundfile>=0.12.0',
        'tensorboard~=2.14.0',
        'tensorrt-cu12==10.0.1; sys_platform == "linux"',
        'tensorrt-cu12-bindings==10.0.1; sys_platform == "linux"',
        'tensorrt-cu12-libs==10.0.1; sys_platform == "linux"',
        'transformers>=4.40.0',
        'uvicorn>=0.30.0',
        'wget~=3.2',
        'fastapi~=0.115.0',
        'fastapi-cli~=0.0.4',
        'WeTextProcessing~=1.0.0',
        'playsound~=1.3.0',
        'pyarrow~=18.1.0'
    ]
)
