import os
import sys
import shutil
import warnings
import tempfile

from time import time

import playsound
import torchaudio

from .config_tts import TTSConfig
from cosyvoice.cli.cosyvoice import CosyVoice, CosyVoice2
from mfa.align import download_model_and_dict, init_mfa_models, align

if __name__ == "__main__":
    # warnings.filterwarnings("ignore", message=".*LoRACompatibleLinear.*")
    # warnings.filterwarnings("ignore", message=".*torch.nn.utils.weight_norm is deprecated.*")
    # warnings.filterwarnings("ignore", category=FutureWarning, message=r".*weights_only=False.*")
    # warnings.filterwarnings("ignore", category=FutureWarning, message=r".*weights_norm.*")
    
    try:
        model_path = os.path.expanduser(os.path.join(TTSConfig.MODELPATH, TTSConfig.MODEL))
        cosyvoice = CosyVoice(model_path, fp16=TTSConfig.FLOAT16)
    except Exception as e:
        err_msg = str(e).lower()
        if ("file" in err_msg) and ("doesn't" in err_msg) and ("exist" in err_msg):
            catch = input(" * CosyVoice TTS 发生了错误，这可能是由于模型下载不完全导致的，是否清理缓存TTS模型？[y/n] ")
            if catch.strip().lower() == "y":
                shutil.rmtree(os.path.expanduser(TTSConfig.MODELPATH), ignore_errors=True)
                print(" * 清理完成，请重新运行该模块。")
                sys.exit(0)
            else:
                raise
        else:
            raise
    
    mfa_dir = os.path.expanduser(os.path.join(TTSConfig.MODELPATH, "mfa"))
    if not (os.path.exists(mfa_dir) and
            os.path.exists(os.path.join(mfa_dir, "mandarin_china_mfa.dict")) and
            os.path.exists(os.path.join(mfa_dir, "mandarin_mfa.zip"))):
        print(" * SwarmClone 使用 Montreal Forced Aligner 进行对齐，开始下载: ")
        download_model_and_dict(TTSConfig)
    acoustic_model, lexicon_compiler, tokenizer, pretrained_aligner = init_mfa_models(TTSConfig)
        
        
    s = "收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。"
    outputs = list(cosyvoice.inference_sft(s, '中文女', stream=False))[0]["tts_speech"]
    # 音频文件
    audio_name = os.path.abspath(os.path.join("example", "output", f"voice{time()}.mp3"))
    torchaudio.save(audio_name, outputs, 22050)
    # 字幕文件
    txt_name = audio_name.replace(".mp3", ".txt")
    open(txt_name, "w", encoding="utf-8").write(s)
    # 对齐文件
    align(audio_name, txt_name, acoustic_model, lexicon_compiler, tokenizer, pretrained_aligner)
    align_name = audio_name.replace(".mp3", ".TextGrid")
    
    playsound.playsound(audio_name)
    # 删除文件
    # os.remove(audio_name)
    # os.remove(txt_name)
    # os.remove(align_name)


    