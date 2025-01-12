# Minimum-CosyVoice

## 简介

**Minimum-CosyVoice** 是从 [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 修改而来的精简版语音合成库。该版本为 [SwarmClone](https://github.com/SwarmClone/SwarmClone) 调整，移除了未使用的功能和文件，优化了模型管理。

## 修改内容

- 移除了未被使用的 `MatchTTS` 的多数文件，以减少库的体积和复杂性。
- 模型将被自动下载到用户目录下的路径：
  ```
  USER_HOME/.swarmclone/tts_cosy_voice/
  ```
- 不支持通过传入参数的方式修改模型下载路径，如果需要更改模型存储位置，可以通过创建软链接的方式实现。例如：
    ```bash
    ln -s /your/custom/path/tts_cosy_voice $HOME/.swarmclone/tts_cosy_voice
    ```
- 系统适配：
  - **Linux 系统**：使用 `ttsfrd`。
  - **Windows 系统**：使用 `wetextprocessing`。

## 安装

```bash
pip install -r requirements_tts_cosyvoice.txt
```

## 使用方法

请参考 [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 项目的具体文档获取更多关于使用方法的细节。

## 贡献

如果你对本项目有改进建议或发现任何问题，欢迎提交 Issue 或 Pull Request！

## 许可协议

本项目基于原 [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 项目的许可证，具体请参阅 [LICENSE](./LICENSE) 文件。

