# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from flightctl.models.disruption_allowance import DisruptionAllowance
from flightctl.models.rollout_device_selection import RolloutDeviceSelection
from typing import Optional, Set
from typing_extensions import Self

class RolloutPolicy(BaseModel):
    """
    RolloutPolicy is the rollout policy of the fleet.
    """ # noqa: E501
    disruption_allowance: Optional[DisruptionAllowance] = Field(default=None, alias="disruptionAllowance")
    device_selection: Optional[RolloutDeviceSelection] = Field(default=None, alias="deviceSelection")
    success_threshold: Optional[StrictStr] = Field(default=None, description="Percentage is the string format representing percentage string.", alias="successThreshold")
    default_update_timeout: Optional[Annotated[str, Field(strict=True)]] = Field(default='0s', description="The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: - 's' for seconds - 'm' for minutes - 'h' for hours - 'd' for days ", alias="defaultUpdateTimeout")
    __properties: ClassVar[List[str]] = ["disruptionAllowance", "deviceSelection", "successThreshold", "defaultUpdateTimeout"]

    @field_validator('default_update_timeout')
    def default_update_timeout_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[1-9]\d*[smhd]$", value):
            raise ValueError(r"must validate the regular expression /^[1-9]\d*[smhd]$/")
        return value

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
        """Create an instance of RolloutPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of disruption_allowance
        if self.disruption_allowance:
            _dict['disruptionAllowance'] = self.disruption_allowance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_selection
        if self.device_selection:
            _dict['deviceSelection'] = self.device_selection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RolloutPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disruptionAllowance": DisruptionAllowance.from_dict(obj["disruptionAllowance"]) if obj.get("disruptionAllowance") is not None else None,
            "deviceSelection": RolloutDeviceSelection.from_dict(obj["deviceSelection"]) if obj.get("deviceSelection") is not None else None,
            "successThreshold": obj.get("successThreshold"),
            "defaultUpdateTimeout": obj.get("defaultUpdateTimeout") if obj.get("defaultUpdateTimeout") is not None else '0s'
        })
        return _obj


