import os
import sys
import shutil
import warnings
import tempfile

from time import time

import playsound
import torchaudio

from config_tts import TTSConfig
from cosyvoice.cli.cosyvoice import CosyVoice, CosyVoice2


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
        
    outputs = list(cosyvoice.inference_sft("收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。", '中文女', stream=False))[0]["tts_speech"]
    
    temp_dir = tempfile.gettempdir()
    fname = os.path.join(temp_dir, f"voice{time()}.mp3")
    torchaudio.save(fname, outputs, 22050)
    playsound.playsound(os.path.abspath(fname))
    os.remove(os.path.abspath(fname))


    