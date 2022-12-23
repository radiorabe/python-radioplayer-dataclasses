import pytest
from xmldiff import main as xmldiff  # type: ignore
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from radioplayer.dataclasses import LongNameType

_XMLNS_EPG_SCHEDULE = "http://www.radioplayer.co.uk/schemas/11/epgSchedule"
_XSD_EPG_SCHEDULE = "http://www.radioplayer.co.uk/schemas/11/epgSchedule_11.xsd"


@pytest.fixture(name="xml_serializer")
def fixture_xml_serializer():
    config = SerializerConfig(
        pretty_print=True,
        xml_declaration=False,
        schema_location=f"{_XMLNS_EPG_SCHEDULE} {_XSD_EPG_SCHEDULE}",
    )
    yield XmlSerializer(config=config)


def test_ampersand_in_show(xml_serializer):
    """Test if show with an ampersand in their name get rendered properly.

    * https://github.com/radiorabe/nowplaying/issues/151
    """
    long_name = LongNameType(value="Rythm & Blues", lang="en")

    expected_string = (
        '<longNameType xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.radioplayer.co.uk/schemas/11/epgSchedule '
        'http://www.radioplayer.co.uk/schemas/11/epgSchedule_11.xsd" '
        'xml:lang="en">Rythm &amp; Blues</longNameType>'
    )
    actual_string = xml_serializer.render(long_name)
    assert not xmldiff.diff_texts(left=actual_string, right=expected_string)
