class Knob:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float": ("FLOAT", {
                    "default": 1.0,
                    "min": 1.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, # The value representing the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display":"knob",
                    "lazy": False,
                    "gradient_stops": "rgb(150, 0, 0);rgb(0, 216, 72);rgb(14, 182, 201)" # Could not find a mechanism to make this work, as the type is FLOAT and not Knob.
                }),
                "int": ("INT", {
                    "default": 1.0,
                    "min": 1.0,
                    "max": 100.0,
                    "step": 1,
                    "round": 0.001, # The value representing the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display":"knob",
                    "lazy": False,
                    "gradient_stops": "rgb(150, 0, 0);rgb(0, 216, 72);rgb(14, 182, 201)" # Could not find a mechanism to make this work, as the type is INT and not Knob.
                }),
                "text":("STRING",{
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!",
                    "lazy": False,
                })
            },
        }

    RETURN_TYPES = ("FLOAT","INT",)
    RETURN_NAMES = ("as_float","as_int",)

    FUNCTION = "do"

    OUTPUT_NODE = False

    CATEGORY = "utils/widgets"

    def check_lazy_status(self,int,float,text):
        return []

    def do(self, int,float,text):
        return (float,int)

# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Widgets:Knob": Knob
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Widgets:Knob": "Knob"
}
