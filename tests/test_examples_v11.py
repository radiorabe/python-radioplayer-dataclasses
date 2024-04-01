import pytest
from lxml.etree import parse, tostring
from xmldiff import main as xmldiff  # type: ignore[import]
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from radioplayer.dataclasses import (
    AudioStreamGroupType,
    AudioStreamType,
    BitRateType,
    EnsembleType,
    Epg,
    EpgLanguageType,
    GenreType,
    LinkType,
    ListenliveGroupType,
    LocationType,
    LongNameType,
    MediaCreditType,
    MediaDescriptionType,
    MediumNameType,
    OndemandType,
    ProgrammeType,
    RadioplayerIdType,
    RestrictionType,
    ScheduleType,
    ServiceIdType,
    ServiceInformation,
    ServiceType,
    ShortNameType,
    SocialIdentifierType,
)

_FILE_OD_XML = "Radioplayer_Metadata_Examples_for_v11/20120101_1_OD.xml"
_FILE_PE_XML = "Radioplayer_Metadata_Examples_for_v11/20120101_1_PE.xml"
_FILE_PI_XML = "Radioplayer_Metadata_Examples_for_v11/20120101_1_PI.xml"
_FILE_SI_XML = "Radioplayer_Metadata_Examples_for_v11/20120101_1_SI.xml"

_XMLNS_EPG_SCHEDULE = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"
_XSD_EPG_SCHEDULE = "http://www.radioplayer.co.uk/schemas/11/epgSchedule_11.xsd"
_XMLNS_SI = "http://www.radioplayer.co.uk/schemas/11/epgSI"
_XSD_SI = "http://www.radioplayer.co.uk/schemas/11/epgSI_11.xsd"
_XMLNS_EPG_DATA = "http://www.radioplayer.co.uk/schemas/11/epgDataTypes"
_XMLNS_RP_DATA = "http://www.radioplayer.co.uk/schemas/11/rpDataTypes"


@pytest.fixture(name="schema_location")
def fixture_schema_location():
    return f"{_XMLNS_EPG_SCHEDULE} {_XSD_EPG_SCHEDULE}"


@pytest.fixture(name="xml_serializer")
def fixture_xml_serializer(schema_location):
    config = SerializerConfig(
        pretty_print=True, xml_declaration=False, schema_location=schema_location
    )
    return XmlSerializer(config=config)


def test_example_od(xml_serializer):
    """Test generating an OD XML."""
    epg = Epg(
        lang="en",
        schedule=ScheduleType(
            creation_time="2012-01-01T00:00:00+00:00",
            originator="myoriginator",
            version="111",
            scope=ScheduleType.Scope(
                start_time="2012-01-01T00:00:00+00:00",
                stop_time="2012-01-01T00:02:00+00:00",
                service_scope=ScheduleType.Scope.ServiceScope(
                    id="e1.0000.0000.0", radioplayer_id="1"
                ),
            ),
            programme=ProgrammeType(
                id="crid://mysite.com/od/100",
                short_id="100",
                recommendation="no",
                broadcast="on-air",
                bitrate="111",
                version="111",
                medium_name=MediumNameType(value="Medium Name", lang="en"),
                long_name=LongNameType(value="Long Name", lang="en"),
                media_description=MediaDescriptionType(
                    multimedia=MediaDescriptionType.Multimedia(
                        lang="en",
                        mime_value="image/png",
                        url="http://mysite.com/web-search.png",
                        width="86",
                        height="48",
                        index="1",
                    )
                ),
                genre=GenreType(
                    type_value="main",
                    href="urn:radioplayer:metadata:cs:Category:2012:1",
                    name="Pop/Chart",
                ),
                ondemand=OndemandType(
                    duration="PT2H",
                    player="http://mysite.com/player/ondemanditem",
                    restriction=OndemandType.Restriction(
                        relationship="allow", value="UK"
                    ),
                    availability=OndemandType.Availability(
                        scope=OndemandType.Availability.Scope(
                            start_time="2012-01-01T00:02:00+00:00",
                            stop_time="2012-07-01T00:02:00+00:00",
                            service_scope=OndemandType.Availability.Scope.ServiceScope(
                                id="e1.0000.0000.0"
                            ),
                        )
                    ),
                    audio_stream_group=AudioStreamGroupType(
                        audio_stream=AudioStreamType(
                            audio_source=AudioStreamType.AudioSource(
                                mime_value="audio/mp3",
                                url="http://mysite.com/od100.mp3",
                            ),
                            audio_format=AudioStreamType.AudioFormat(
                                href="urn:mpeg:mpeg7:cs:AudioPresentationCS:2001:3"
                            ),
                            bit_rate=BitRateType(target="2164000", variable=False),
                            restriction=RestrictionType(
                                relationship="allow", value="UK"
                            ),
                        )
                    ),
                ),
            ),
        ),
    )

    expected_string = tostring(parse(f"tests/data/{_FILE_OD_XML}"))
    actual_string = xml_serializer.render(
        epg,
        ns_map={
            None: _XMLNS_EPG_SCHEDULE,
            "epg": _XMLNS_EPG_DATA,
            "radioplayer": _XMLNS_RP_DATA,
        },
    )
    assert not xmldiff.diff_texts(left=actual_string, right=expected_string)


def test_example_pe(xml_serializer):
    """Test generating a simple PE XML."""
    epg = Epg(
        lang="en",
        schedule=ScheduleType(
            creation_time="2012-01-01T00:00:00+00:00",
            originator="myoriginator",
            version="111",
            scope=ScheduleType.Scope(
                start_time="2012-01-01T00:00:00+00:00",
                stop_time="2012-01-01T00:02:00+00:00",
                service_scope=ScheduleType.Scope.ServiceScope(
                    id="e1.0000.0000.0", radioplayer_id="1"
                ),
            ),
            programme=ProgrammeType(
                id="crid://mysite.com/progs/100",
                short_id="100",
                recommendation="no",
                broadcast="on-air",
                bitrate="111",
                version="111",
                medium_name=MediumNameType(value="Medium Name", lang="en"),
                long_name=LongNameType(value="Long Name", lang="en"),
                location=LocationType(
                    time=LocationType.Time(
                        time="2012-01-01T00:00:00+00:00", duration="PT2H"
                    ),
                    bearer=LocationType.Bearer(id="e1.0000.0000.0", radioplayer_id="1"),
                ),
                media_description=MediaDescriptionType(
                    multimedia=MediaDescriptionType.Multimedia(
                        lang="en",
                        mime_value="image/png",
                        url="http://mysite.com/web-search.png",
                        width="86",
                        height="48",
                        index="1",
                    )
                ),
                genre=GenreType(
                    type_value="main",
                    href="urn:radioplayer:metadata:cs:Category:2012:1",
                    name="Pop/Chart",
                ),
                programme_event=ProgrammeType.ProgrammeEvent(
                    id="crid://mysite.com/nowplaying",
                    short_id="0",
                    recommendation="no",
                    broadcast="on-air",
                    medium_name=MediumNameType(value="The Luckiest Guy", lang="en"),
                    long_name=LongNameType(
                        value="The Luckiest Guy on the Lower East Side", lang="en"
                    ),
                    lang=None,
                    location=LocationType(
                        relative_time=LocationType.RelativeTime(
                            time="PT1H51M23S", duration="PT3M23S"
                        )
                    ),
                    genre=GenreType(
                        href="urn:tva:metadata:cs:ContentCS:2002:3.6.1", type_value=None
                    ),
                    media_credit=MediaCreditType(
                        role="artist", scheme="urn:ebu", value="The Magnetic Fields"
                    ),
                ),
            ),
        ),
    )

    expected_string = tostring(parse(f"tests/data/{_FILE_PE_XML}"))
    actual_string = xml_serializer.render(
        epg,
        ns_map={
            None: _XMLNS_EPG_SCHEDULE,
            "epg": _XMLNS_EPG_DATA,
            "radioplayer": _XMLNS_RP_DATA,
        },
    )
    assert not xmldiff.diff_texts(left=actual_string, right=expected_string)


def test_example_pi(xml_serializer):
    """Test generating an PI XML."""
    epg = Epg(
        lang="en",
        schedule=ScheduleType(
            creation_time="2012-01-01T00:00:00+00:00",
            originator="myoriginator",
            version="111",
            scope=ScheduleType.Scope(
                start_time="2012-01-01T00:00:00+00:00",
                stop_time="2012-01-01T00:02:00+00:00",
                service_scope=ScheduleType.Scope.ServiceScope(
                    id="e1.0000.0000.0", radioplayer_id="1"
                ),
            ),
            programme=ProgrammeType(
                id="crid://mysite.com/progs/100",
                short_id="100",
                recommendation="no",
                broadcast="on-air",
                bitrate="111",
                version="111",
                medium_name=MediumNameType(value="Medium Name", lang="en"),
                long_name=LongNameType(value="Long Name", lang="en"),
                location=LocationType(
                    time=LocationType.Time(
                        time="2012-01-01T00:00:00+00:00", duration="PT2H"
                    ),
                    bearer=LocationType.Bearer(id="e1.0000.0000.0", radioplayer_id="1"),
                ),
                genre=GenreType(
                    type_value="main",
                    href="urn:radioplayer:metadata:cs:Category:2012:1",
                    name="Pop/Chart",
                ),
                ondemand=OndemandType(
                    player="http://mysite.com/player",
                    restriction=OndemandType.Restriction(
                        relationship="allow", value="UK"
                    ),
                    availability=OndemandType.Availability(
                        scope=OndemandType.Availability.Scope(
                            start_time="2012-01-01T00:02:00+00:00",
                            stop_time="2012-07-01T00:02:00+00:00",
                            service_scope=OndemandType.Availability.Scope.ServiceScope(
                                id="e1.0000.0000.0"
                            ),
                        )
                    ),
                    audio_stream_group=AudioStreamGroupType(
                        audio_stream=AudioStreamType(
                            audio_source=AudioStreamType.AudioSource(
                                mime_value="audio/mp3", url="http://mysite.com/100.mp3"
                            ),
                            audio_format=AudioStreamType.AudioFormat(
                                href="urn:mpeg:mpeg7:cs:AudioPresentationCS:2001:3"
                            ),
                            bit_rate=BitRateType(target="2164000", variable=False),
                            restriction=RestrictionType(
                                relationship="allow", value="UK"
                            ),
                        )
                    ),
                ),
                social_id=[
                    SocialIdentifierType(type_value="facebook", uid="12345678"),
                    SocialIdentifierType(type_value="twitter", uid="12345678"),
                ],
            ),
        ),
    )

    expected_string = tostring(parse(f"tests/data/{_FILE_PI_XML}"))
    actual_string = xml_serializer.render(
        epg,
        ns_map={
            None: _XMLNS_EPG_SCHEDULE,
            "epg": _XMLNS_EPG_DATA,
            "radioplayer": _XMLNS_RP_DATA,
        },
    )
    assert not xmldiff.diff_texts(left=actual_string, right=expected_string)


@pytest.mark.parametrize("schema_location", [f"{_XMLNS_SI} {_XSD_SI}"])
def test_example_si(xml_serializer):
    """Test generating an SI XML."""
    service_information = ServiceInformation(
        lang="en",
        ensemble=EnsembleType(
            id="00.0000",
            short_name=ShortNameType(lang=None),
            medium_name=MediumNameType(lang=None),
            service=ServiceType(
                service_id=ServiceIdType(id="e1.0000.0000.0", type_value=None),
                short_name="Short",
                medium_name="Medium Name",
                long_name="Long Name",
                media_description=[
                    MediaDescriptionType(
                        short_description="Short description",
                        long_description="Long description",
                    ),
                    MediaDescriptionType(
                        multimedia=MediaDescriptionType.Multimedia(
                            lang="en",
                            mime_value="image/png",
                            url="http://mysite.com/web-search.png",
                            width="86",
                            height="48",
                            index="1",
                        )
                    ),
                    MediaDescriptionType(
                        multimedia=MediaDescriptionType.Multimedia(
                            lang="en",
                            mime_value="image/png",
                            url="http://mysite.com/web-search2.png",
                            width="86",
                            height="48",
                            index="2",
                        )
                    ),
                    MediaDescriptionType(
                        multimedia=MediaDescriptionType.Multimedia(
                            lang="en",
                            mime_value="image/png",
                            url="http://mysite.com/mobile-small.png",
                            width="160",
                            height="90",
                            index="1",
                        )
                    ),
                    MediaDescriptionType(
                        multimedia=MediaDescriptionType.Multimedia(
                            lang="en",
                            mime_value="image/png",
                            url="http://mysite.com/mobile-large.png",
                            width="288",
                            height="162",
                            index="1",
                        )
                    ),
                ],
                genre=GenreType(
                    type_value="main",
                    href="urn:tva:metadata:cs:ContentCS:2002:3.7.1",
                    name="Content games categories",
                ),
                epg_language=EpgLanguageType(lang="en"),
                link=LinkType(
                    lang=None,
                    url="http://mysite/mobile",
                    mime_value="text/html",
                    type_value="rp-handheld-station-view",
                    index="0",
                ),
                radioplayer_id=RadioplayerIdType(id="1"),
                listenlive_group=ListenliveGroupType(
                    listenlive=ListenliveGroupType.Listenlive(
                        player="http://mysite.com/player",
                        audio_stream_group=AudioStreamGroupType(
                            audio_stream=[
                                AudioStreamType(
                                    audio_source=AudioStreamType.AudioSource(
                                        mime_value="audio/mp3",
                                        url="http://mystreamer.com/low.mp3",
                                    ),
                                    audio_format=AudioStreamType.AudioFormat(
                                        href="urn:mpeg:mpeg7:cs:AudioPresentationCS:2001:3"
                                    ),
                                    bit_rate=BitRateType(
                                        target="48000", variable=False
                                    ),
                                    restriction=RestrictionType(
                                        relationship="allow", value="UK"
                                    ),
                                ),
                                AudioStreamType(
                                    audio_source=AudioStreamType.AudioSource(
                                        mime_value="audio/mp3",
                                        url="http://mystreamer.com/high.mp3",
                                    ),
                                    audio_format=AudioStreamType.AudioFormat(
                                        href="urn:mpeg:mpeg7:cs:AudioPresentationCS:2001:3"
                                    ),
                                    bit_rate=BitRateType(
                                        target="128000", variable=False
                                    ),
                                    restriction=RestrictionType(
                                        relationship="allow", value="UK"
                                    ),
                                ),
                                AudioStreamType(
                                    rtmp_source=AudioStreamType.RtmpSource(
                                        server="rtmp://rtmp.mystreamer.com/",
                                        endpoint="live",
                                    ),
                                    audio_format=AudioStreamType.AudioFormat(
                                        href="urn:mpeg:mpeg7:cs:AudioPresentationCS:2001:3"
                                    ),
                                    bit_rate=BitRateType(
                                        target="128000", variable=False
                                    ),
                                    restriction=RestrictionType(
                                        relationship="allow", value="UK"
                                    ),
                                ),
                            ]
                        ),
                    )
                ),
                geo_locations="York",
                geo_footprint="53.95059 -1.060181, 53.951399 -1.044302, 53.947509 -1.04147, 53.941498 -1.057863, 53.943923 -1.060095, 53.95059 -1.060181",  # noqa: E501
                social_id=[
                    SocialIdentifierType(type_value="googleplus", uid="123645"),
                    SocialIdentifierType(type_value="twitter", uid="123645"),
                    SocialIdentifierType(type_value="facebook", uid="mystation"),
                ],
            ),
        ),
    )

    expected_string = tostring(parse(f"tests/data/{_FILE_SI_XML}"))
    actual_string = xml_serializer.render(
        service_information,
        ns_map={None: _XMLNS_SI, "epg": _XMLNS_EPG_DATA, "radioplayer": _XMLNS_RP_DATA},
    )
    assert not xmldiff.diff_texts(left=actual_string, right=expected_string)
