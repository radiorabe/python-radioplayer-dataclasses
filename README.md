# Python Radioplayer Dataclasses

Classes for generating [radioplayer](https://radioplayer.co.uk) compatible data. Generated using [xsdata](https://xsdata.readthedocs.io/).

## Installation

```bash
pip install radioplayer-dataclasses
```

## Usage

The `radioplayer.dataclasses` module may be used to build radioplayer compatible structures.
Serializing is done using the `xsdata` library.

```python
>>> from radioplayer.dataclasses import *
>>> epg = Epg(lang="en")
>>> epg
Epg(programme_groups=[], schedule=[], alternate_source=[], lang='en', system=<SystemType.DAB: 'DAB'>)

>>> from xsdata.formats.dataclass.serializers import XmlSerializer
>>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
>>>
>>> config = SerializerConfig(
...     pretty_print=True,
...     xml_declaration=False,
... )
>>> serializer = XmlSerializer(config=config)
>>> xml = serializer.render(epg, ns_map={None: Epg.Meta.namespace})
>>> print(xml.strip())
<epg xmlns="http://www.radioplayer.co.uk/schemas/11/epgSchedule" xml:lang="en" system="DAB"/>

```

Additional examples are available in the `tests/` directory.

## Development

### Getting Started

```bash
pip install -r requirements-dev.txt
```

### Loading XSD files

```bash
mkdir schemas
pushd schemas/
curl -L -O http://www.w3.org/2001/xml.xsd
curl -L -O https://radioplayer.co.uk/schemas/11/epgSchedule_11.xsd
curl -L -O https://radioplayer.co.uk/schemas/11/epgDataTypes_11.xsd
curl -L -O https://radioplayer.co.uk/schemas/11/rpDataTypes_11.xsd
curl -L -O https://radioplayer.co.uk/schemas/11/epgSI_11.xsd
popd
```

Some touchups where made to the files to make them validate where necessary.

### Generating dataclasses

```bash
xsdata -c .xsdata.xml schemas/
```

### Running tests

```bash
pytest
```

## Release Management

The CI/CD setup uses semantic commit messages following the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/).
There is a GitHub Action in [.github/workflows/semantic-release.yaml](./.github/workflows/semantic-release.yaml)
that uses [go-semantic-commit](https://go-semantic-release.xyz/) to create new
releases.

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

1. **fix:** a commit of the type `fix` patches gets released with a PATCH version bump
1. **feat:** a commit of the type `feat` gets released as a MINOR version bump
1. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:` gets released as a MAJOR version bump
1. types other than `fix:` and `feat:` are allowed and don't trigger a release

If a commit does not contain a conventional commit style message you can fix
it during the squash and merge operation on the PR.

Once a commit has landed on the `main` branch a release will be created and automatically published to [pypi](https://pypi.org/)
using the GitHub Action in [.github/workflows/pypi.yaml](./.github/workflows/pypi.yaml) which uses [twine](https://twine.readthedocs.io/)
to publish the package to pypi.

## License

This application is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, version 3 of the License.

## Copyright

Copyright (c) 2022 [Radio Bern RaBe](http://www.rabe.ch)
