#!/bin/bash

# this script installs hwreport

if [ "$EUID" -ne 0 ]; then
    echo "Run this with sudo!"
    exit 1
fi

INSTALL_LIB_PATH="/usr/local/lib/hwreport"
INSTALL_BIN_PATH="/usr/local/bin/hwreport"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing hwreport..."

if [ -d "$INSTALL_LIB_PATH" ]; then
    rm -rf "$INSTALL_LIB_PATH"
fi

# copy the actual python package into place
cp -r "$SCRIPT_DIR/hwreport" "$INSTALL_LIB_PATH"

# write a tiny launcher script that just runs the real python code
cat > "$INSTALL_BIN_PATH" << EOF
#!/bin/bash
python3 "$INSTALL_LIB_PATH/main.py" "\$@"
EOF

chmod +x "$INSTALL_BIN_PATH"

echo "hwreport installed. Run it with: hwreport"
