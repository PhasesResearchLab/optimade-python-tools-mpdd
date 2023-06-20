<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable-next-line MD041 -->
<div align="center">
<img id="mpddlogo" width="100px" src="https://images.squarespace-cdn.com/content/v1/5d7c199aa75aa00cdd43098b/1625971605808-B8K2666QM0FBF921E9HR/logo.png">
<img width="100px" src="https://matsci.org/uploads/default/original/2X/b/bd2f59b3bf14fb046b74538750699d7da4c19ac1.svg">
</div>

# <div align="center">OPTIMADE Python tools - modified for MPDD</div>
<div align="center">
<table>
<thead align="center">
<tr><th align="center">Latest release</th><th align="center">Build status</th><th align="center">Activity</th></tr>
</thead>

<tbody>
<tr>
  <td align="center">
    <a href="https://pypi.org/project/optimade"><img alt="PyPI version" src="https://img.shields.io/pypi/v/optimade?logo=pypi&logoColor=white"></a><br>
    <a href="https://pypi.org/project/optimade"><img alt="PyPI - Python Version"  src="https://img.shields.io/pypi/pyversions/optimade?logo=python&logoColor=white"></a><br>
    <a href="https://github.com/Materials-Consortia/OPTIMADE"><img alt="OPTIMADE version" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Materials-Consortia/optimade-python-tools/master/optimade-version.json"></a>
  </td>
  <td align="center">
    <a href="https://github.com/Materials-Consortia/optimade-python-tools/actions?query=branch%3Amaster+"><img alt="Build Status" src="https://img.shields.io/github/actions/workflow/status/Materials-Consortia/optimade-python-tools/ci.yml?logo=github"></a><br>
    <a href="https://optimade.org/optimade-python-tools"><img alt="Docs" src="https://img.shields.io/github/actions/workflow/status/Materials-Consortia/optimade-python-tools/ci_cd_updated_master.yml?label=docs&logo=github"></a><br>
    <a href="https://codecov.io/gh/Materials-Consortia/optimade-python-tools"><img alt="Codecov" src="https://img.shields.io/codecov/c/github/Materials-Consortia/optimade-python-tools?logo=codecov&logoColor=white&token=UJAtmqkZZO"></a><br>
  </td>
  <td align="center">
    <a href="https://github.com/Materials-Consortia/optimade-python-tools/pulse"><img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/m/Materials-Consortia/optimade-python-tools?logo=github"></a><br>
    <a href="https://github.com/Materials-Consortia/optimade-python-tools/commits/master"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/Materials-Consortia/optimade-python-tools/master?logo=github"></a><br>
    <a href="https://github.com/Materials-Consortia/optimade-python-tools/graphs/contributors"><img alt="Contributors" src="https://badgen.net/github/contributors/Materials-Consortia/optimade-python-tools?icon=github"></a>
  </td>
</tr>
</tbody>
</table>

</div>

This is a fork of the [optimade-python-tools](https://github.com/Materials-Consortia/optimade-python-tools) modified and truncated for [MPDD Database (phaseslab.com/mpdd)](https://phaseslab.com/mpdd) use.

The aim of [OPTIMADE](https://optimade.org) is to develop a common API, compliant with the [JSON:API 1.0](http://jsonapi.org/format/1.0/) specification.
This is to enable interoperability among databases that serve crystal structures and calculated properties of existing and hypothetical materials.


## Supported OPTIMADE versions

Each release of the `optimade` package from this repository only targets one version of the OPTIMADE specification, summarised in the table below.

<div align="center">

<table>

<thead>
    <tr>
        <th align="center">OPTIMADE API version</th>
        <th align="center"><code>optimade</code> version</th>
    </tr>
</thead>

<tbody>
    <tr>
        <td align="center"><a href="https://github.com/Materials-Consortia/OPTIMADE/blob/v1.0.0/optimade.rst">v1.0.0</a></td>
        <td align="center"><a href="https://github.com/Materials-Consortia/optimade-python-tools/tree/v0.12.9">v0.12.9</a></td>
    </tr>
    <tr>
        <td align="center"><a href="https://github.com/Materials-Consortia/OPTIMADE/blob/v1.1.0/optimade.rst">v1.1.0</a></td>
        <td align="center"><a href="https://github.com/Materials-Consortia/optimade-python-tools/tree/v0.16.0">v0.16.0+</a></td>
    </tr>
</tbody>
</table>
</div>

## Links

- [OPTIMADE Specification](https://github.com/Materials-Consortia/OPTIMADE/blob/develop/optimade.rst), the human-readable specification that this library is based on.
- [optimade-validator-action](https://github.com/Materials-Consortia/optimade-validator-action), a GitHub action that can be used to validate implementations from a URL (using the validator from this repo).
- [OpenAPI](https://github.com/OAI/OpenAPI-Specification), the machine-readable format used to specify the OPTIMADE API in [`openapi.json`](openapi/openapi.json) and [`index_openapi.json`](openapi/index_openapi.json).
- [Interactive documentation](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/Materials-Consortia/optimade-python-tools/master/openapi/openapi.json) generated from [`openapi.json`](openapi/openapi.json) (see also [interactive JSON editor](https://editor.swagger.io/?url=https://raw.githubusercontent.com/Materials-Consortia/optimade-python-tools/master/openapi/openapi.json)).
- [pydantic](https://pydantic-docs.helpmanual.io/), the library used for generating the OpenAPI schema from [Python models](https://www.optimade.org/optimade-python-tools/all_models/).
- [FastAPI](https://fastapi.tiangolo.com/), the framework used for generating the reference implementation expressed by the [`openapi.json`](openapi/openapi.json) specification.
- [Lark](https://github.com/lark-parser/lark), the library used to parse the filter language in OPTIMADE queries.
