from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class CatypeType(Enum):
    UNSPECIFIED = "unspecified"
    NONE = "none"


class BroadcastType(Enum):
    ON_AIR = "on-air"
    OFF_AIR = "off-air"


class GenreTypeType(Enum):
    MAIN = "main"
    SECONDARY = "secondary"
    OTHER = "other"


@dataclass
class LocationType:
    class Meta:
        name = "locationType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    time: List["LocationType.Time"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    relative_time: List["LocationType.RelativeTime"] = field(
        default_factory=list,
        metadata={
            "name": "relativeTime",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    bearer: List["LocationType.Bearer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )

    @dataclass
    class Bearer:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"(([0-9a-fA-F]{2}\.[0-9a-fA-F]{4}\.)?[0-9a-fA-F]{4,8}\.[0-9a-fA-F]{1}(\.[0-9a-fA-F]{2})?)|([0-9a-fA-F]{6})",
            }
        )
        radioplayer_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "radioplayerId",
                "type": "Attribute",
                "required": True,
            }
        )
        trigger: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"[0-9a-fA-F]{8}",
            }
        )

    @dataclass
    class Time:
        time: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[^\-].+T[^\.]+",
            }
        )
        duration: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"PT[^\.]+",
            }
        )
        actual_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "actualTime",
                "type": "Attribute",
                "pattern": r"[^\-].+T[^\.]+",
            }
        )
        actual_duration: Optional[str] = field(
            default=None,
            metadata={
                "name": "actualDuration",
                "type": "Attribute",
                "pattern": r"PT[^\.]+",
            }
        )

    @dataclass
    class RelativeTime:
        time: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"PT[^\.]+",
            }
        )
        duration: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"PT[^\.]+",
            }
        )
        actual_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "actualTime",
                "type": "Attribute",
                "pattern": r"PT[^\.]+",
            }
        )
        actual_duration: Optional[str] = field(
            default=None,
            metadata={
                "name": "actualDuration",
                "type": "Attribute",
                "pattern": r"PT[^\.]+",
            }
        )


@dataclass
class MemberOfType:
    class Meta:
        name = "memberOfType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    short_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 16777215,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class MultimediaType(Enum):
    LOGO_UNRESTRICTED = "logo_unrestricted"
    LOGO_MONO_SQUARE = "logo_mono_square"
    LOGO_COLOUR_SQUARE = "logo_colour_square"
    LOGO_MONO_RECTANGLE = "logo_mono_rectangle"
    LOGO_COLOUR_RECTANGLE = "logo_colour_rectangle"


class RecommendationType(Enum):
    YES = "yes"
    NO = "no"


class SystemType(Enum):
    DAB = "DAB"
    DRM = "DRM"


class FormatType(Enum):
    AUDIO = "audio"
    DATA = "data"


class FrequencyTypeType(Enum):
    PRIMARY = "primary"
    ALTERNATIVE = "alternative"


class ServiceIdTypeAttr(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class AlternateSourceTypeProtocol(Enum):
    DAB = "DAB"
    DRM = "DRM"
    URL = "URL"


class AlternateSourceTypeType(Enum):
    MORE = "more"
    LESS = "less"
    SIMILAR = "similar"
    IDENTICAL = "identical"


class ProgrammeGroupTypeType(Enum):
    SERIES = "series"
    SHOW = "show"
    PROGRAM_CONCEPT = "programConcept"
    MAGAZINE = "magazine"
    PROGRAM_COMPILATION = "programCompilation"
    OTHER_COLLECTION = "otherCollection"
    OTHER_CHOICE = "otherChoice"
    TOPIC = "topic"


@dataclass
class BitRateType:
    class Meta:
        name = "bitRateType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    target: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    variable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaCreditType:
    class Meta:
        name = "mediaCreditType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mbid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dbpid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    imdb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class RestrictionTypeRelationship(Enum):
    ALLOW = "allow"
    DENY = "deny"


class RestrictionRelationship(Enum):
    ALLOW = "allow"
    DENY = "deny"


class ServiceGroupIdHead(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class RadioplayerIdType:
    class Meta:
        name = "serviceIdType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SocialIdentifierType:
    class Meta:
        name = "socialIdentifierType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class LangValue(Enum):
    VALUE = ""


@dataclass
class Catype:
    class Meta:
        name = "CAType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    type: CatypeType = field(
        default=CatypeType.NONE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EpgLanguageType:
    class Meta:
        name = "epgLanguageType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class LinkType:
    class Meta:
        name = "linkType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"((crid|CRID|tel|mailto|postal|http|https|dab|drm):(//|\+|SMS=)?)?([a-zA-Z0-9]|\.|@|%|\-|/|_|\+|\?|=|;){1,}",
        }
    )
    mime_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"([!-\.0-~]{1,}/[!-\.0-~]{1,})+",
        }
    )
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 180,
        }
    )
    expiry_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "expiryTime",
            "type": "Attribute",
            "pattern": r"[^\-].+T[^\.]+",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MessageType:
    class Meta:
        name = "messageType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class SimulcastType:
    class Meta:
        name = "simulcastType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    system: Optional[SystemType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(([0-9a-fA-F]{2}\.[0-9a-fA-F]{4}\.)?[0-9a-fA-F]{4,8}\.[0-9a-fA-F]{1}(\.[0-9a-fA-F]{2})?)|([0-9a-fA-F]{6})",
        }
    )


@dataclass
class FrequencyType:
    class Meta:
        name = "frequencyType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSI"

    type: FrequencyTypeType = field(
        default=FrequencyTypeType.PRIMARY,
        metadata={
            "type": "Attribute",
        }
    )
    k_hz: Optional[int] = field(
        default=None,
        metadata={
            "name": "kHz",
            "type": "Attribute",
        }
    )


@dataclass
class ServiceIdType:
    class Meta:
        name = "serviceIDType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSI"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"(([0-9a-fA-F]{2}\.[0-9a-fA-F]{4}\.)?[0-9a-fA-F]{4,8}\.[0-9a-fA-F]{1}(\.[0-9a-fA-F]{2})?)|([0-9a-fA-F]{6})",
        }
    )
    type: ServiceIdTypeAttr = field(
        default=ServiceIdTypeAttr.PRIMARY,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AlternateSourceType:
    class Meta:
        name = "alternateSourceType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"

    protocol: AlternateSourceTypeProtocol = field(
        default=AlternateSourceTypeProtocol.URL,
        metadata={
            "type": "Attribute",
        }
    )
    type: AlternateSourceTypeType = field(
        default=AlternateSourceTypeType.IDENTICAL,
        metadata={
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"((crid|CRID|tel|mailto|postal|http|https|dab|drm):(//|\+|SMS=)?)?([a-zA-Z0-9]|\.|@|%|\-|/|_|\+|\?|=|;){1,}",
        }
    )


@dataclass
class RestrictionType:
    class Meta:
        name = "restrictionType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    relationship: Optional[RestrictionTypeRelationship] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GenreType:
    class Meta:
        name = "genreType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    name: Optional["GenreType.Name"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    definition: Optional[MessageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        }
    )
    type: GenreTypeType = field(
        default=GenreTypeType.MAIN,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Name(MessageType):
        preferred: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class KeywordsType(MessageType):
    class Meta:
        name = "keywordsType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class LongDescriptionType(MessageType):
    class Meta:
        name = "longDescriptionType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class LongNameType(MessageType):
    class Meta:
        name = "longNameType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class MediumNameType(MessageType):
    class Meta:
        name = "mediumNameType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class ShortDescriptionType(MessageType):
    class Meta:
        name = "shortDescriptionType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class ShortNameType(MessageType):
    class Meta:
        name = "shortNameType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"


@dataclass
class AudioStreamType:
    class Meta:
        name = "audioStreamType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    audio_source: Optional["AudioStreamType.AudioSource"] = field(
        default=None,
        metadata={
            "name": "audioSource",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    rtmp_source: Optional["AudioStreamType.RtmpSource"] = field(
        default=None,
        metadata={
            "name": "rtmpSource",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    audio_format: Optional["AudioStreamType.AudioFormat"] = field(
        default=None,
        metadata={
            "name": "audioFormat",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            "required": True,
        }
    )
    bit_rate: Optional[BitRateType] = field(
        default=None,
        metadata={
            "name": "bitRate",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            "required": True,
        }
    )
    restriction: Optional[RestrictionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )

    @dataclass
    class AudioFormat:
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AudioSource:
        mime_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "mimeValue",
                "type": "Attribute",
                "required": True,
                "white_space": "collapse",
                "pattern": r"([!-\.0-~]{1,}/[!-\.0-~]{1,})+",
            }
        )
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RtmpSource:
        server: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        endpoint: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class MediaDescriptionType:
    class Meta:
        name = "mediaDescriptionType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    short_description: List[ShortDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    long_description: List[LongDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "longDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    multimedia: Optional["MediaDescriptionType.Multimedia"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )

    @dataclass
    class Multimedia:
        mime_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "mimeValue",
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"([!-\.0-~]{1,}/[!-\.0-~]{1,})+",
            }
        )
        lang: Union[str, LangValue] = field(
            default="en",
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            }
        )
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"((crid|CRID|tel|mailto|postal|http|https|dab|drm):(//|\+|SMS=)?)?([a-zA-Z0-9]|\.|@|%|\-|/|_|\+|\?|=|;){1,}",
            }
        )
        type: Optional[MultimediaType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        width: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        height: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class AudioStreamGroupType:
    class Meta:
        name = "audioStreamGroupType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    audio_stream: List[AudioStreamType] = field(
        default_factory=list,
        metadata={
            "name": "audioStream",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            "min_occurs": 1,
        }
    )


@dataclass
class ProgrammeGroupType:
    class Meta:
        name = "programmeGroupType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"

    short_name: List[ShortNameType] = field(
        default_factory=list,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    medium_name: List[MediumNameType] = field(
        default_factory=list,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    long_name: List[LongNameType] = field(
        default_factory=list,
        metadata={
            "name": "longName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    media_description: List[MediaDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "mediaDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    genre: List[GenreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    keywords: List[KeywordsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    member_of: List[MemberOfType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    short_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 16777215,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[ProgrammeGroupTypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    num_of_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "numOfItems",
            "type": "Attribute",
        }
    )


@dataclass
class ListenliveGroupType:
    class Meta:
        name = "listenliveGroupType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    listenlive: List["ListenliveGroupType.Listenlive"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Listenlive:
        player: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
                "required": True,
            }
        )
        restriction: Optional["ListenliveGroupType.Listenlive.Restriction"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            }
        )
        audio_stream_group: Optional[AudioStreamGroupType] = field(
            default=None,
            metadata={
                "name": "audioStreamGroup",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            }
        )
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass
        class Restriction:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                }
            )
            relationship: Optional[RestrictionRelationship] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )


@dataclass
class OndemandType:
    class Meta:
        name = "ondemandType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    player: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            "required": True,
        }
    )
    restriction: Optional["OndemandType.Restriction"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    availability: Optional["OndemandType.Availability"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    audio_stream_group: Optional[AudioStreamGroupType] = field(
        default=None,
        metadata={
            "name": "audioStreamGroup",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"PT[^\.]+",
        }
    )

    @dataclass
    class Restriction:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        relationship: Optional[RestrictionRelationship] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Availability:
        scope: Optional["OndemandType.Availability.Scope"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
            }
        )

        @dataclass
        class Scope:
            service_scope: List["OndemandType.Availability.Scope.ServiceScope"] = field(
                default_factory=list,
                metadata={
                    "name": "serviceScope",
                    "type": "Element",
                    "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
                }
            )
            start_time: Optional[str] = field(
                default=None,
                metadata={
                    "name": "startTime",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[^\-].+T[^\.]+",
                }
            )
            stop_time: Optional[str] = field(
                default=None,
                metadata={
                    "name": "stopTime",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[^\-].+T[^\.]+",
                }
            )

            @dataclass
            class ServiceScope:
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "white_space": "collapse",
                        "pattern": r"(([0-9a-fA-F]{2}\.[0-9a-fA-F]{4}\.)?[0-9a-fA-F]{4,8}\.[0-9a-fA-F]{1}(\.[0-9a-fA-F]{2})?)|([0-9a-fA-F]{6})",
                    }
                )


@dataclass
class ServiceGroupType:
    class Meta:
        name = "serviceGroupType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"

    service_group_id: List["ServiceGroupType.ServiceGroupId"] = field(
        default_factory=list,
        metadata={
            "name": "serviceGroupId",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )
    short_name: List[ShortNameType] = field(
        default_factory=list,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    medium_name: List[MediumNameType] = field(
        default_factory=list,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    long_name: List[LongNameType] = field(
        default_factory=list,
        metadata={
            "name": "longName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    media_description: List[MediaDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "mediaDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/rpDataTypes",
        }
    )

    @dataclass
    class ServiceGroupId:
        radioplayer_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "radioplayerId",
                "type": "Attribute",
                "required": True,
            }
        )
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        head: Optional[ServiceGroupIdHead] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class ProgrammeType:
    class Meta:
        name = "programmeType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"

    short_name: List[ShortNameType] = field(
        default_factory=list,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    medium_name: List[MediumNameType] = field(
        default_factory=list,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    long_name: List[LongNameType] = field(
        default_factory=list,
        metadata={
            "name": "longName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    location: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    media_description: List[MediaDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "mediaDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    genre: List[GenreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    ca: Optional[Catype] = field(
        default=None,
        metadata={
            "name": "CA",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    keywords: List[KeywordsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    member_of: List[MemberOfType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    programme_event: List["ProgrammeType.ProgrammeEvent"] = field(
        default_factory=list,
        metadata={
            "name": "programmeEvent",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    ondemand: List[OndemandType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    social_id: List[SocialIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "socialId",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    short_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 16777215,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    recommendation: RecommendationType = field(
        default=RecommendationType.NO,
        metadata={
            "type": "Attribute",
        }
    )
    broadcast: BroadcastType = field(
        default=BroadcastType.ON_AIR,
        metadata={
            "type": "Attribute",
        }
    )
    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    @dataclass
    class ProgrammeEvent:
        short_name: List[ShortNameType] = field(
            default_factory=list,
            metadata={
                "name": "shortName",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        medium_name: List[MediumNameType] = field(
            default_factory=list,
            metadata={
                "name": "mediumName",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
                "min_occurs": 1,
            }
        )
        long_name: List[LongNameType] = field(
            default_factory=list,
            metadata={
                "name": "longName",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        location: List[LocationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
                "min_occurs": 1,
            }
        )
        media_description: List[MediaDescriptionType] = field(
            default_factory=list,
            metadata={
                "name": "mediaDescription",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        genre: List[GenreType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        ca: Optional[Catype] = field(
            default=None,
            metadata={
                "name": "CA",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        keywords: List[KeywordsType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        member_of: List[MemberOfType] = field(
            default_factory=list,
            metadata={
                "name": "memberOf",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        mbid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        isrc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        catalogue: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        barcode: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        media_credit: List[MediaCreditType] = field(
            default_factory=list,
            metadata={
                "name": "mediaCredit",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            }
        )
        short_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "shortId",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 16777215,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
            }
        )
        version: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        recommendation: RecommendationType = field(
            default=RecommendationType.NO,
            metadata={
                "type": "Attribute",
            }
        )
        broadcast: BroadcastType = field(
            default=BroadcastType.ON_AIR,
            metadata={
                "type": "Attribute",
            }
        )
        lang: Union[str, LangValue] = field(
            default="en",
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            }
        )


@dataclass
class ServiceType:
    class Meta:
        name = "serviceType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSI"

    service_id: List[ServiceIdType] = field(
        default_factory=list,
        metadata={
            "name": "serviceID",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
            "min_occurs": 1,
        }
    )
    simulcast: List[SimulcastType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    short_name: List[ShortNameType] = field(
        default_factory=list,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    medium_name: List[MediumNameType] = field(
        default_factory=list,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    long_name: List[LongNameType] = field(
        default_factory=list,
        metadata={
            "name": "longName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    media_description: List[MediaDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "mediaDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    genre: List[GenreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    epg_language: List[EpgLanguageType] = field(
        default_factory=list,
        metadata={
            "name": "epgLanguage",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    ca: Optional[Catype] = field(
        default=None,
        metadata={
            "name": "CA",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    keywords: List[KeywordsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    radioplayer_id: Optional[RadioplayerIdType] = field(
        default=None,
        metadata={
            "name": "radioplayerId",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
            "required": True,
        }
    )
    listenlive_group: Optional[ListenliveGroupType] = field(
        default=None,
        metadata={
            "name": "listenliveGroup",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
            "required": True,
        }
    )
    geo_locations: Optional[str] = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
            "required": True,
        }
    )
    geo_footprint: Optional[str] = field(
        default=None,
        metadata={
            "name": "geoFootprint",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
            "required": True,
        }
    )
    social_id: List[SocialIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "socialId",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    format: FormatType = field(
        default=FormatType.AUDIO,
        metadata={
            "type": "Attribute",
        }
    )
    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ext_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "extFormat",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(([0-3]{1}\.[0-9a-fA-F]{2}\.[0-9a-fA-F]{3})|([0-7]{1}\.[0-9a-fA-F]{4}))((\.([0-9a-fA-F]{2})+)?)",
        }
    )


@dataclass
class ProgrammeGroupsType:
    class Meta:
        name = "programmeGroupsType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"

    programme_group: List[ProgrammeGroupType] = field(
        default_factory=list,
        metadata={
            "name": "programmeGroup",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
            "min_occurs": 1,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Attribute",
            "pattern": r"[^\-].+T[^\.]+",
        }
    )
    originator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class EnsembleType:
    class Meta:
        name = "ensembleType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSI"

    short_name: List[ShortNameType] = field(
        default_factory=list,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    medium_name: List[MediumNameType] = field(
        default_factory=list,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
            "min_occurs": 1,
        }
    )
    long_name: List[LongNameType] = field(
        default_factory=list,
        metadata={
            "name": "longName",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgDataTypes",
        }
    )
    frequency: List[FrequencyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    media_description: List[MediaDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "mediaDescription",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    ca: Optional[Catype] = field(
        default=None,
        metadata={
            "name": "CA",
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    keywords: List[KeywordsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    service: List[ServiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSI",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"([0-9a-fA-F]{2}\.[0-9a-fA-F]{4})|([0-9a-fA-F]{6})",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleType:
    class Meta:
        name = "scheduleType"
        target_namespace = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"

    scope: Optional["ScheduleType.Scope"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
        }
    )
    programme: List[ProgrammeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
            "min_occurs": 1,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Attribute",
            "pattern": r"[^\-].+T[^\.]+",
        }
    )
    originator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 128,
        }
    )

    @dataclass
    class Scope:
        service_scope: List["ScheduleType.Scope.ServiceScope"] = field(
            default_factory=list,
            metadata={
                "name": "serviceScope",
                "type": "Element",
                "namespace": "http://www.radioplayer.co.uk/schemas/11/epgSchedule",
            }
        )
        start_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "startTime",
                "type": "Attribute",
                "required": True,
                "pattern": r"[^\-].+T[^\.]+",
            }
        )
        stop_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "stopTime",
                "type": "Attribute",
                "required": True,
                "pattern": r"[^\-].+T[^\.]+",
            }
        )

        @dataclass
        class ServiceScope:
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "white_space": "collapse",
                    "pattern": r"(([0-9a-fA-F]{2}\.[0-9a-fA-F]{4}\.)?[0-9a-fA-F]{4,8}\.[0-9a-fA-F]{1}(\.[0-9a-fA-F]{2})?)|([0-9a-fA-F]{6})",
                }
            )
            radioplayer_id: Optional[int] = field(
                default=None,
                metadata={
                    "name": "radioplayerId",
                    "type": "Attribute",
                    "required": True,
                }
            )


@dataclass
class ServiceInformation:
    """
    Service information includes the structure of and information about the
    multiplex and its associated services.
    """
    class Meta:
        name = "serviceInformation"
        namespace = "http://www.radioplayer.co.uk/schemas/11/epgSI"

    ensemble: List[EnsembleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    service_group: List[ServiceGroupType] = field(
        default_factory=list,
        metadata={
            "name": "serviceGroup",
            "type": "Element",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Attribute",
            "pattern": r"[^\-].+T[^\.]+",
        }
    )
    originator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 128,
        }
    )
    service_provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceProvider",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    system: SystemType = field(
        default=SystemType.DAB,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )


@dataclass
class Epg:
    class Meta:
        name = "epg"
        namespace = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"

    programme_groups: List[ProgrammeGroupsType] = field(
        default_factory=list,
        metadata={
            "name": "programmeGroups",
            "type": "Element",
        }
    )
    schedule: List[ScheduleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alternate_source: List[AlternateSourceType] = field(
        default_factory=list,
        metadata={
            "name": "alternateSource",
            "type": "Element",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
    system: SystemType = field(
        default=SystemType.DAB,
        metadata={
            "type": "Attribute",
        }
    )
