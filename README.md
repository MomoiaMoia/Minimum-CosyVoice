# Minimum-CosyVoice

## 简介

**Minimum-CosyVoice** 是从 [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 修改而来的精简版语音合成库。该版本为 [SwarmClone](https://github.com/SwarmClone/SwarmClone) 调整，移除了未使用的功能和文件，优化了模型管理。

## 修改内容

- [2025年1月19日] 添加 [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) 生成对齐文件。
- 移除了未被使用的 `MatchTTS` 的多数文件，以减少库的体积和复杂性。
- 模型将被自动下载到用户目录下的路径：

  ```bash
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

该版本 CosyVoice 使用 PyTorch == 2.5.1，安装其他依赖请使用：

```bash
python get_cosyvoice_reqs.py
```

## 使用方法

运行示例请使用：

```bash
python -m example.example
```

运行将在 example/output/ 目录下生成 `voice{time()}.mp3`,`voice{time()}.txt`,`voice{time()}.TextGrid`。

请参考 [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 项目的具体文档获取更多关于其他使用方法的细节。

## 贡献

如果你对本项目有改进建议或发现任何问题，欢迎提交 Issue 或 Pull Request！

## 许可协议

本项目基于 **GNU General Public License v3.0 (GPL-3.0)** 进行分发和使用。  

此外，本项目依赖以下两个开源项目，并在 `licenses` 目录中提供了它们的相关许可证文件：  

1. **[CosyVoice](https://github.com/FunAudioLLM/CosyVoice)**  
   - 使用 **Apache License 2.0**  
   - 许可证文件详见 `licenses/cosyvoice_LICENSE`。

2. **[Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)**  
   - 使用 **MIT License**  
   - 许可证文件详见 `licenses/mfa_LICENSE`。
