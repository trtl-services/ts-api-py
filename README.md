# TRTL Service Python API Interface

This wrapper allows you to easily interact with the [TRTL Services](https://trtl.services) 0.9.0 API to quickly develop applications that interact with the [TurtleCoin](https://turtlecoin.lol) Network.


# Table of Contents

1. [Installation](#installation)
2. [Intialization](#intialization)
3. [Documentation](#documentation)
  1. [Methods](#methods)

# Installation

```bash
pip install ts-api-py
```

# Intialization

```python
import os
from TRTLservices import TS

os.environ["TRTL_SERVICES_TOKEN"] = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoieW8iLCJhcHBJZCI6MjAsInVzZXJJZCI6MiwicGVybWlzc2lvbnMiOlsiYWRkcmVzczpuZXciLCJhZGRyZXNzOnZpZXciLCJhZGRyZXNzOmFsbCIsImFkZHJlc3M6c2NhbiIsImFkZHJlc3M6ZGVsZXRlIiwidHJhbnNmZXI6bmV3IiwidHJhbnNmZXI6dmlldyJdLCJpYXQiOjE1Mzk5OTQ4OTgsImV4cCI6MTU3MTU1MjQ5OCwiYXVkIjoiZ2FuZy5jb20iLCJpc3MiOiJUUlRMIFNlcnZpY2VzIiwianRpIjoiMjIifQ.KkKyg18aqZfLGMGTnUDhYQmVSUoocrr4CCdLBm2K7V87s2T-3hTtM2MChJB2UdbDLWnf58GiMa_t8xp9ZjZjIg"

os.environ["TRTL_SERVICES_TIMEOUT"] = 2000

```

Generate a token with the TRTL Services [Dashboard](https://trtl.services) and store it as the variable ``TRTL_SERVICES_TOKEN`` in your os environment along with ``TRTL_SERVICES_TIMEOUT`` if you wish the change the default timeout of 2000.



# Documentation

API documentation is available at https://trtl.services/docs


## Methods

### createAddress()
Create a new TRTL addresses

```python
TS.createAddress()
```


### getAddress(address)
Get address details by address
```python
TS.getAddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### deleteAddress(address)
Delete a selected TRTL address

```python
TS.deleteAdddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### getAddresses()
View all addresses.

```python
TS.getAddresses()
```


### scanAddress(address, blockIndex)
Scan an address for transactions between a 100 block range starting from the specified blockIndex.

```python
TS.scanAddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A", 899093)
```


### getAddressKeys(address)
Get the public and secret spend key of an address.

```python
TS.getAddressKeys("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### integrateAddress(address, paymentId)
Create an integrated address with an address and payment ID.

```python
TS.integrateAddress("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A", "7d89a2d16365a1198c46db5bbe1af03d2b503a06404f39496d1d94a0a46f8804")
```


### getIntegratedAddresses(address)
Get all integrated addresses by address.

```python
TS.getIntegratedAddresses("TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A")
```


### getFee(amount)
Calculate the TRTL Services fee for an amount specified in TRTL with two decimal points.

```python
TS.getFee(1092.19)
```


### createTransfer(sender, receiver, amount, fee, paymentId, extra)
Send a TRTL transaction with an address with the amount specified two decimal points.

```python
TS.createTransfer(
  "TRTLuxH78akDMCsXycnU5HjJE6zPCgM4KRNNQSboqh1yiTnvxuhNVUL9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7aj113A",
  "TRTLuzAzNs1E1RBFhteX56A5353vyHuSJ5AYYQfoN97PNbcMDvwQo4pUWHs7SYpuD9ThvA7AD3r742kwTmWh5o9WFaB9JXH8evP",
  1000.01,
  1.2,
  "7d89a2d16365a1198c46db5bbe1af03d2b503a06404f39496d1d94a0a46f8804",
  "3938f915a11582f62d93f82f710df9203a029f929fd2f915f2701d947f920f99"
)
```
#### You can leave the last two fields (paymentId and extra) blank.


### getTransfer(address)
Get a transaction details specified by transaction hash.

```python
TS.getTransfer("EohMUzR1DELyeQM9RVVwpmn5Y1DP0lh1b1ZpLQrfXQsgtvGHnDdJSG31nX2yESYZ")
```


### getWallet()
Get wallet container info and health check.

```python
TS.getWallet()
```


### getStatus()
Get the current status of the TRTL Services infrastructure.

```python
TS.getStatus()
```