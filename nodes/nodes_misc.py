import torch
import comfy.sd

class SC_Seed:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})}}

    RETURN_TYPES = ("INT", "STRING", )
    RETURN_NAMES = ("seed", "show_help", )
    FUNCTION = "seedint"
    OUTPUT_NODE = True
    CATEGORY = "Slim-Comfy/Misc"

    @staticmethod
    def seedint(seed):
        show_help = "no help currently"
        return (seed, show_help,)