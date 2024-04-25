import math
from typing import Literal

from invokeai.app.invocations.fields import FieldDescriptions
from invokeai.invocation_api import (
    BaseInvocation,
    BaseInvocationOutput,
    InputField,
    InvocationContext,
    OutputField,
    WithMetadata,
    invocation,
    invocation_output,
)
@invocation_output("aspect_ratio_output")
class AspectRatioOutput(BaseInvocationOutput):
    """Class to encapsulate output of WxH from aspect ratio node"""
    width: int = OutputField(description="The calculated width")
    height: int = OutputField(description="The calculated height")

@invocation(
    "aspect_ratio",
    title="Aspect Ratio",
    tags=["aspect", "ratio", "resolution"],
    category="math",
    version="1.0.0",
)
class AspectRatioInvocation(BaseInvocation):
    """Calculates the width and height based on a base resolution and aspect ratio"""
    base_resolution: int = InputField(default=512, description="The base resolution (the length of the shortest side)")

    aspect_ratio: Literal["1:1", "16:9", "3:4", "3:2", "3:5", "5:4"] = InputField(default="16:9", description="The desired aspect ratio")

    orientation: Literal["landscape", "portrait"] = InputField(default="landscape", description="The orientation of the output resolution")

    def invoke(self, context:InvocationContext) -> AspectRatioOutput:
        base_resolution = round(self.base_resolution // 8) * 8  # Round to the nearest multiple of 8

        aspect_ratio_map = {
            "1:1": 1.0,
            "16:9": 16/9,
            "4:3": 4/3,
            "3:5": 5/3,
            "3:2": 3/2,
            "5:4": 5/4
        }

        aspect_ratio_value = aspect_ratio_map[self.aspect_ratio]

        if self.orientation == "landscape":
            if aspect_ratio_value >= 1:
                width = base_resolution * aspect_ratio_value
                height = base_resolution
            else:
                width = base_resolution
                height = base_resolution / aspect_ratio_value
        else:  # portrait orientation
            if aspect_ratio_value >= 1:
                width = base_resolution
                height = base_resolution * aspect_ratio_value
            else:
                width = base_resolution / aspect_ratio_value
                height = base_resolution

        # Round width and height to the nearest multiple of 8
        width = round(width / 8) * 8
        height = round(height / 8) * 8

        return AspectRatioOutput(
            width=round(width),
            height=round(height)
        )