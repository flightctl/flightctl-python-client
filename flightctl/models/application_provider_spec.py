# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://flightctl.io) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flightctl.models.app_type import AppType
from flightctl.models.application_content import ApplicationContent
from flightctl.models.application_volume import ApplicationVolume
from typing import Optional, Set
from typing_extensions import Self

class ApplicationProviderSpec(BaseModel):
    """
    ApplicationProviderSpec
    """ # noqa: E501
    env_vars: Optional[Dict[str, StrictStr]] = Field(default=None, description="Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters.", alias="envVars")
    name: Optional[StrictStr] = Field(default=None, description="The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace.")
    app_type: Optional[AppType] = Field(default=None, alias="appType")
    volumes: Optional[List[ApplicationVolume]] = Field(default=None, description="List of application volumes.")
    image: StrictStr = Field(description="Reference to the container image for the application package.")
    inline: List[ApplicationContent] = Field(description="A list of application content.")
    __properties: ClassVar[List[str]] = ["envVars", "name", "appType", "volumes", "image", "inline"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApplicationProviderSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item_volumes in self.volumes:
                if _item_volumes:
                    _items.append(_item_volumes.to_dict())
            _dict['volumes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inline (list)
        _items = []
        if self.inline:
            for _item_inline in self.inline:
                if _item_inline:
                    _items.append(_item_inline.to_dict())
            _dict['inline'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationProviderSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "envVars": obj.get("envVars"),
            "name": obj.get("name"),
            "appType": obj.get("appType"),
            "volumes": [ApplicationVolume.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None,
            "image": obj.get("image"),
            "inline": [ApplicationContent.from_dict(_item) for _item in obj["inline"]] if obj.get("inline") is not None else None
        })
        return _obj


