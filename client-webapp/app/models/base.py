from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        strict=True,
        str_strip_whitespace=True,
        frozen=True,
        hide_input_in_errors=True,
    )
