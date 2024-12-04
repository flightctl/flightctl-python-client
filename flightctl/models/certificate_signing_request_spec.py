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

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CertificateSigningRequestSpec(BaseModel):
    """
    Wrapper around a user-created CSR, modeled on kubernetes io.k8s.api.certificates.v1.CertificateSigningRequestSpec
    """ # noqa: E501
    expiration_seconds: Optional[StrictInt] = Field(default=None, description="Requested duration of validity for the certificate", alias="expirationSeconds")
    extra: Optional[Dict[str, List[StrictStr]]] = Field(default=None, description="Extra attributes of the user that created the CSR, populated by the API server on creation and immutable")
    request: Union[StrictBytes, StrictStr] = Field(description="The base64-encoded PEM-encoded PKCS#10 CSR. Matches the spec.request field in a kubernetes CertificateSigningRequest resource")
    signer_name: StrictStr = Field(description="Indicates the requested signer, and is a qualified name", alias="signerName")
    uid: Optional[StrictStr] = Field(default=None, description="UID of the user that created the CSR, populated by the API server on creation and immutable")
    usages: Optional[List[StrictStr]] = Field(default=None, description="Usages specifies a set of key usages requested in the issued certificate.")
    username: Optional[StrictStr] = Field(default=None, description="Name of the user that created the CSR, populated by the API server on creation and immutable")
    __properties: ClassVar[List[str]] = ["expirationSeconds", "extra", "request", "signerName", "uid", "usages", "username"]

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
        """Create an instance of CertificateSigningRequestSpec from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateSigningRequestSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expirationSeconds": obj.get("expirationSeconds"),
            "extra": obj.get("extra"),
            "request": obj.get("request"),
            "signerName": obj.get("signerName"),
            "uid": obj.get("uid"),
            "usages": obj.get("usages"),
            "username": obj.get("username")
        })
        return _obj


