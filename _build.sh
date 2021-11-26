rm -rf dist
mkdir -p dist

pyarmor pack --clean -e "--onefile --windowed" centrify.py
pyarmor pack --clean -e "--onefile --windowed" trigger.py

bash _shasum.sh