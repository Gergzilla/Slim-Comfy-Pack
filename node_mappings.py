try:

    from .nodes.nodes_lora import *

except ImportError:
    print("\033[34mmSlim-Comfy v0.1 \033[92mFailed to load ELora nodes\033[0m")


    NODE_CLASS_MAPPINGS = { 
    ### LoRA Nodes    
    "SC Load LoRA": SC_LoraLoader,    
    "SC LoRA Stack": SC_LoRAStack,
    "SC Apply LoRA Stack": SC_ApplyLoRAStack,  
    }

    NODE_DISPLAY_NAME_MAPPINGS = {
    ### LoRA Nodes    
    "SC Load LoRA": "💊 SC Load LoRA",    
    "SC LoRA Stack": "💊 SC LoRA Stack",
    "SC Apply LoRA Stack": "💊 SC Apply LoRA Stack",
    }