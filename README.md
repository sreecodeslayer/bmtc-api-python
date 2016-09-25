# Python Wrapper for BMTC API

Bangalore Metropolitan Transport Corporation BMTC recently released its Intelligent Transport System (ITS) , But as of now there is no official public api available. This is an approach to build a python wrapper based on the Reverse engineering work done by [**tachyons**](https://github.com/tachyons)

API Reference : https://github.com/tachyons/bmtc-api

## Installation

```python
# From source provided you keep __init__.py
from bmtc import 'Bmtc'
```

## Usage

Create a new instance.

```python
bmtc = Bmtc()
```

Route wise details.

```python
result = bmtc.route_wise('<direction>', '<routeNo>')
```

Route map details.
```python
result = bmtc.route_map('<direction>', '<routeNo>')
```
Nearest stop details.

```python
result = bmtc.nearest_stop('<lattitude>', '<longitude>')
```
Get stops matching the query string.

```python
result = bmtc.search_stop('<keyword>')
```
Get stop details based on Stop ID.

```python
result = bmtc.buses_in_stop('<stopId>')
```
Get a trip fare.

```python
result = bmtc.trip_fare(<source>, <destination>, <service types>, <number of adults>)
```
Service types can be either
* ordinary
* vajra
* vayu_vajra
* atal_sarige
* nice_service
* bengaluru_darshini

Note: Every methods described above either returns an array of objects or a NULL array.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sreecodeslayer/bmtc-api-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

This repository is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
