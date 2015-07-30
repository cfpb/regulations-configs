# regulations-configs

[eRegulations](http://cfpb.github.io/eRegulations) is a web-based tool that makes regulations easier to find, read and understand with features such as inline official interpretations, highlighted defined terms, and a revision comparison view.

eRegs is made up of three core components:

* [regulations-parser](https://github.com/cfpb/regulations-parser): Parse regulations
* [regulations-core](https://github.com/cfpb/regulations-core): Regulations API
* [regulations-site](https://github.com/cfpb/regulations-site): Display the regulations

This repository contains configuration related specifically to parsing [CFPB's
regulations](http://www.consumerfinance.gov/eregulations/) with 
[regulations-parser](https://github.com/cfpb/regulations-parser). These
configuration files can also be used as examples in cases unrelated to
CFPB's regulations.

## Using 

To use this configuration *for CFPB regulations only*, install this
package in the same Python environment as regulations-parser. For
example, from a working git clone of this repository that you can modify:

```shell
cd regulations-configs
pip install -e .
```

Then regulations-parser should pick up the configuration in `regconfig`
automatically.

To install directly, not as a working copy that you modify but as a
standard Python package that will have to be reinstalled if there are
any configuration changes, run the following command within the
regulations-parser Python environment:

```shell
pip install pip install git+https://github.com/cfpb/regulations-configs
```

## Open source licensing info

1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

