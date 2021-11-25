# Build with obfuscation

## Install
```
pip install -r requirements.txt
```

## Obfuscate
```
pip install pyarmor pyinstaller
```

```
pyarmor obfuscate foo.py
```

## Build
```
pyarmor pack --clean -e "--onefile " foo.py
```