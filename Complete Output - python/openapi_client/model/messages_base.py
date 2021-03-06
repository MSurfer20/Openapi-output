"""
    Zulip REST API

    Powerful open source group chat   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.emoji_reaction import EmojiReaction
    from openapi_client.model.messages_base_topic_links import MessagesBaseTopicLinks
    globals()['EmojiReaction'] = EmojiReaction
    globals()['MessagesBaseTopicLinks'] = MessagesBaseTopicLinks


class MessagesBase(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'avatar_url': (str, none_type,),  # noqa: E501
            'client': (str,),  # noqa: E501
            'content': (str,),  # noqa: E501
            'content_type': (str,),  # noqa: E501
            'display_recipient': (dict,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'is_me_message': (bool,),  # noqa: E501
            'reactions': ([EmojiReaction],),  # noqa: E501
            'recipient_id': (int,),  # noqa: E501
            'sender_email': (str,),  # noqa: E501
            'sender_full_name': (str,),  # noqa: E501
            'sender_id': (int,),  # noqa: E501
            'sender_realm_str': (str,),  # noqa: E501
            'stream_id': (int,),  # noqa: E501
            'subject': (str,),  # noqa: E501
            'topic_links': ([MessagesBaseTopicLinks],),  # noqa: E501
            'submessages': ([str],),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'avatar_url': 'avatar_url',  # noqa: E501
        'client': 'client',  # noqa: E501
        'content': 'content',  # noqa: E501
        'content_type': 'content_type',  # noqa: E501
        'display_recipient': 'display_recipient',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_me_message': 'is_me_message',  # noqa: E501
        'reactions': 'reactions',  # noqa: E501
        'recipient_id': 'recipient_id',  # noqa: E501
        'sender_email': 'sender_email',  # noqa: E501
        'sender_full_name': 'sender_full_name',  # noqa: E501
        'sender_id': 'sender_id',  # noqa: E501
        'sender_realm_str': 'sender_realm_str',  # noqa: E501
        'stream_id': 'stream_id',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'topic_links': 'topic_links',  # noqa: E501
        'submessages': 'submessages',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MessagesBase - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            avatar_url (str, none_type): The URL of the user's avatar.  Can be null only if client_gravatar was passed, which means that the user has not uploaded an avatar in Zulip, and the client should compute the gravatar URL by hashing the user's email address itself for this user. . [optional]  # noqa: E501
            client (str): A Zulip \"client\" string, describing what Zulip client sent the message. . [optional]  # noqa: E501
            content (str): The content/body of the message. . [optional]  # noqa: E501
            content_type (str): The HTTP `content_type` for the message content.  This will be `text/html` or `text/x-markdown`, depending on whether `apply_markdown` was set. . [optional]  # noqa: E501
            display_recipient (dict): Data on the recipient of the message; either the name of a stream or a dictionary containing basic data on the users who received the message. . [optional]  # noqa: E501
            id (int): The unique message ID.  Messages should always be displayed sorted by ID. . [optional]  # noqa: E501
            is_me_message (bool): Whether the message is a [/me status message][status-messages]  [status-messages]: /help/format-your-message-using-markdown#status-messages . [optional]  # noqa: E501
            reactions ([EmojiReaction]): Data on any reactions to the message. . [optional]  # noqa: E501
            recipient_id (int): A unique ID for the set of users receiving the message (either a stream or group of users).  Useful primarily for hashing. . [optional]  # noqa: E501
            sender_email (str): The Zulip display email address of the message's sender. . [optional]  # noqa: E501
            sender_full_name (str): The full name of the message's sender. . [optional]  # noqa: E501
            sender_id (int): The user ID of the message's sender. . [optional]  # noqa: E501
            sender_realm_str (str): A string identifier for the realm the sender is in.  Unique only within the context of a given Zulip server.  E.g. on `example.zulip.com`, this will be `example`. . [optional]  # noqa: E501
            stream_id (int): Only present for stream messages; the ID of the stream. . [optional]  # noqa: E501
            subject (str): The `topic` of the message.  Currently always `\"\"` for private messages, though this could change if Zulip adds support for topics in private message conversations.  The field name is a legacy holdover from when topics were called \"subjects\" and will eventually change. . [optional]  # noqa: E501
            topic_links ([MessagesBaseTopicLinks]): Data on any links to be included in the `topic` line (these are generated by [custom linkification filters](/help/add-a-custom-linkifier) that match content in the message's topic.)  **Changes**: This field contained a list of urls before   Zulip 4.0 (feature level 46).  New in Zulip 3.0 (feature level 1): Previously, this field was called `subject_links`; clients are recommended to rename `subject_links` to `topic_links` if present for compatibility with older Zulip servers. . [optional]  # noqa: E501
            submessages ([str]): Data used for certain experimental Zulip integrations. . [optional]  # noqa: E501
            timestamp (int): The UNIX timestamp for when the message was sent, in UTC seconds. . [optional]  # noqa: E501
            type (str): The type of the message: `stream` or `private`. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MessagesBase - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            avatar_url (str, none_type): The URL of the user's avatar.  Can be null only if client_gravatar was passed, which means that the user has not uploaded an avatar in Zulip, and the client should compute the gravatar URL by hashing the user's email address itself for this user. . [optional]  # noqa: E501
            client (str): A Zulip \"client\" string, describing what Zulip client sent the message. . [optional]  # noqa: E501
            content (str): The content/body of the message. . [optional]  # noqa: E501
            content_type (str): The HTTP `content_type` for the message content.  This will be `text/html` or `text/x-markdown`, depending on whether `apply_markdown` was set. . [optional]  # noqa: E501
            display_recipient (dict): Data on the recipient of the message; either the name of a stream or a dictionary containing basic data on the users who received the message. . [optional]  # noqa: E501
            id (int): The unique message ID.  Messages should always be displayed sorted by ID. . [optional]  # noqa: E501
            is_me_message (bool): Whether the message is a [/me status message][status-messages]  [status-messages]: /help/format-your-message-using-markdown#status-messages . [optional]  # noqa: E501
            reactions ([EmojiReaction]): Data on any reactions to the message. . [optional]  # noqa: E501
            recipient_id (int): A unique ID for the set of users receiving the message (either a stream or group of users).  Useful primarily for hashing. . [optional]  # noqa: E501
            sender_email (str): The Zulip display email address of the message's sender. . [optional]  # noqa: E501
            sender_full_name (str): The full name of the message's sender. . [optional]  # noqa: E501
            sender_id (int): The user ID of the message's sender. . [optional]  # noqa: E501
            sender_realm_str (str): A string identifier for the realm the sender is in.  Unique only within the context of a given Zulip server.  E.g. on `example.zulip.com`, this will be `example`. . [optional]  # noqa: E501
            stream_id (int): Only present for stream messages; the ID of the stream. . [optional]  # noqa: E501
            subject (str): The `topic` of the message.  Currently always `\"\"` for private messages, though this could change if Zulip adds support for topics in private message conversations.  The field name is a legacy holdover from when topics were called \"subjects\" and will eventually change. . [optional]  # noqa: E501
            topic_links ([MessagesBaseTopicLinks]): Data on any links to be included in the `topic` line (these are generated by [custom linkification filters](/help/add-a-custom-linkifier) that match content in the message's topic.)  **Changes**: This field contained a list of urls before   Zulip 4.0 (feature level 46).  New in Zulip 3.0 (feature level 1): Previously, this field was called `subject_links`; clients are recommended to rename `subject_links` to `topic_links` if present for compatibility with older Zulip servers. . [optional]  # noqa: E501
            submessages ([str]): Data used for certain experimental Zulip integrations. . [optional]  # noqa: E501
            timestamp (int): The UNIX timestamp for when the message was sent, in UTC seconds. . [optional]  # noqa: E501
            type (str): The type of the message: `stream` or `private`. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
