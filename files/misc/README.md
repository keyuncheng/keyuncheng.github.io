# How to use 7z

## Install

### Dependencies

7z

```
sudo apt-get install p7zip-full
```

## Get

```
7z x <filename>.7z
```

## Set

```
7z a <filename>.7z <file_to_compress> -p -mhe=on
```

## Update

```
7z u <filename>.7z <file_to_modify> -p -mhe=on
```