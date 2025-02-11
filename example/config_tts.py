from dataclasses import dataclass

@dataclass
class TTSConfig:
    MODEL: str      = "CosyVoice-300M-Instruct"
    # MODEL: str      = "CosyVoice2-0.5B"
    INS_TUNE: str   = "zhiluo_0.5neuro_0.5xiaoling"
    SFT_TUNE: str   = "zhiluo_1.2neuro_-0.2xiaoling"
    MODELPATH: str  = "~/.swarmclone/tts_cosy_voice"
    FLOAT16: bool   = False