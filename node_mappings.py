try:
    from .nodes.nodes_misc import *
    from .nodes.nodes_aspect_ratio import *
    from .nodes.nodes_lora import *

except ImportError:
    print("\033[34mmSlim-Comfy v0.1 \033[92mFailed to load Core nodes\033[0m")


NODE_CLASS_MAPPINGS = { 
    ### Misc Nodes
    "SC Seed": SC_Seed,
    ### Aspect Ratio Nodes
    "SC SD1.5 Aspect Ratio": SC_AspectRatioSD15,
    "SC SDXL Aspect Ratio": SC_SDXLAspectRatio,
    "SC Aspect Ratio": SC_AspectRatio,
    ### LoRA Nodes    
    "SC Load LoRA": SC_LoraLoader,    
    "SC LoRA Stack": SC_LoRAStack,
    "SC Apply LoRA Stack": SC_ApplyLoRAStack,  
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    ### Misc Nodes
    "SC Seed": "SC Seed",
    ### Aspect Ratio Nodes
    "SC SD1.5 Aspect Ratio": "SC SD1.5 Aspect Ratio",
    "SC SDXL Aspect Ratio": "SC SDXL Aspect Ratio",    
    "SC Aspect Ratio": "SC Aspect Ratio",
    ### LoRA Nodes    
    "SC Load LoRA": "SC Load LoRA",    
    "SC LoRA Stack": "SC LoRA Stack",
    "SC Apply LoRA Stack": "SC Apply LoRA Stack",
    }