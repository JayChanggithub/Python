# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1SessionAffinityConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_ip': 'V1ClientIPConfig'
    }

    attribute_map = {
        'client_ip': 'clientIP'
    }

    def __init__(self, client_ip=None):
        """
        V1SessionAffinityConfig - a model defined in Swagger
        """

        self._client_ip = None
        self.discriminator = None

        if client_ip is not None:
          self.client_ip = client_ip

    @property
    def client_ip(self):
        """
        Gets the client_ip of this V1SessionAffinityConfig.
        clientIP contains the configurations of Client IP based session affinity.

        :return: The client_ip of this V1SessionAffinityConfig.
        :rtype: V1ClientIPConfig
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """
        Sets the client_ip of this V1SessionAffinityConfig.
        clientIP contains the configurations of Client IP based session affinity.

        :param client_ip: The client_ip of this V1SessionAffinityConfig.
        :type: V1ClientIPConfig
        """

        self._client_ip = client_ip

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1SessionAffinityConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
