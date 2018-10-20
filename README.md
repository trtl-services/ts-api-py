# TRTL Service Python API Interface

This wrapper allows you to easily interact with the [TRTL Services](https://trtl.services) API to quickly develop applications that interact with the [TurtleCoin](https://turtlecoin.lol) Network.


# Table of Contents

1. [Installation](#installation)
2. [Intialization](#intialization)
3. [Documentation](#documentation)
  1. [Methods](#methods)

# Installation

```bash
pip install ts_api_py
```

# Intialization

```python
from ts_api_py import TRTLServices

```

Generate a token with the TRTL Services [Dashboard](https://trtl.services) and store it as the variable ``TRTL_SERVICES_TOKEN`` in your os environment.


# Documentation

API documentation is available at https://trtl.services/documentation


## Methods

### createAddress()
Create a new TRTL addresses

```python
TRTLServices.createAddress()
```


### deleteAddress(address)
Delete a selected TRTL addresses

```python
TRTLServices.deleteAdddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### ViewAddress()
Get address details by address
```python
TRTLServices.viewAddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### viewAddresses()
View all addresses belonging to the specified token.

```python
TRTLServices.viewAddresses()
```


### scanAddress()
Scan for transactions in the next 100 blocks specified by blockIndex and address.

```python
TRTLServices.scanAddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A", 899093)
```


### getFee()
Calculate the TRTL Services fee for a specified TRTL amount.

```python
TRTLServices.getFee(1092.19)
```


### createTransfer()
Send a TRTL transaction with a specified account.

```python
TRTLServices.createTransfer("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A", "TRTLuzAzNs1E1RBFhteX56A5353vyHuSJ5AYYQfoN97PNbcMDvwQo4pUWHs7SYpuD9ThvA7AD3r742kwTmWh5o9WFaB9JXH8evP", 1000, 1)
```

### viewTransfer()
Lists transaction details with specified hash.

```python
TRTLServices.viewTransfer("EohMUzR1DELyeQM9RVVwpmn5Y1DP0lh1b1ZpLQrfXQsgtvGHnDdJSG31nX2yESYZ")
```


### getStatus()
Get the current status of the TRTL Services infrastructure.

```python
TRTLServices.getStatus()
```


# License

```
Copyright (C) 2018 Fexra, The TurtleCoin Developers

Please see the included LICENSE file for more information.
```