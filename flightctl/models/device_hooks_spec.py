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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from flightctl.models.device_reboot_hook_spec import DeviceRebootHookSpec
from flightctl.models.device_update_hook_spec import DeviceUpdateHookSpec
from typing import Optional, Set
from typing_extensions import Self

class DeviceHooksSpec(BaseModel):
    """
    DeviceHooksSpec
    """ # noqa: E501
    before_updating: Optional[List[DeviceUpdateHookSpec]] = Field(default=None, description="Hooks executed before updating allow for custom actions and integration with other systems or services. These actions occur before configuration changes are applied to the device. ", alias="beforeUpdating")
    after_updating: Optional[List[DeviceUpdateHookSpec]] = Field(default=None, description="Hooks executed after updating enable custom actions and integration with other systems or services. These actions occur after configuration changes have been applied to the device. ", alias="afterUpdating")
    before_rebooting: Optional[List[DeviceRebootHookSpec]] = Field(default=None, description="Hooks executed before rebooting allow for custom actions and integration with other systems or services. These actions occur before the device is rebooted. ", alias="beforeRebooting")
    after_rebooting: Optional[List[DeviceRebootHookSpec]] = Field(default=None, description="Hooks executed after rebooting enable custom actions and integration with other systems or services. These actions occur after the device has rebooted, allowing for post-reboot tasks. ", alias="afterRebooting")
    __properties: ClassVar[List[str]] = ["beforeUpdating", "afterUpdating", "beforeRebooting", "afterRebooting"]

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
        """Create an instance of DeviceHooksSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in before_updating (list)
        _items = []
        if self.before_updating:
            for _item_before_updating in self.before_updating:
                if _item_before_updating:
                    _items.append(_item_before_updating.to_dict())
            _dict['beforeUpdating'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in after_updating (list)
        _items = []
        if self.after_updating:
            for _item_after_updating in self.after_updating:
                if _item_after_updating:
                    _items.append(_item_after_updating.to_dict())
            _dict['afterUpdating'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in before_rebooting (list)
        _items = []
        if self.before_rebooting:
            for _item_before_rebooting in self.before_rebooting:
                if _item_before_rebooting:
                    _items.append(_item_before_rebooting.to_dict())
            _dict['beforeRebooting'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in after_rebooting (list)
        _items = []
        if self.after_rebooting:
            for _item_after_rebooting in self.after_rebooting:
                if _item_after_rebooting:
                    _items.append(_item_after_rebooting.to_dict())
            _dict['afterRebooting'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceHooksSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "beforeUpdating": [DeviceUpdateHookSpec.from_dict(_item) for _item in obj["beforeUpdating"]] if obj.get("beforeUpdating") is not None else None,
            "afterUpdating": [DeviceUpdateHookSpec.from_dict(_item) for _item in obj["afterUpdating"]] if obj.get("afterUpdating") is not None else None,
            "beforeRebooting": [DeviceRebootHookSpec.from_dict(_item) for _item in obj["beforeRebooting"]] if obj.get("beforeRebooting") is not None else None,
            "afterRebooting": [DeviceRebootHookSpec.from_dict(_item) for _item in obj["afterRebooting"]] if obj.get("afterRebooting") is not None else None
        })
        return _obj


