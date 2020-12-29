#!/usr/bin/env bash

set -e -o pipefail

echo "----------------------------------------"
echo "Compiling Multisig Command"
echo "----------------------------------------"

# Expected location of SmartPy CLI.
SMART_PY_CLI=~/smartpy-cli/SmartPy.sh


# Ensure we have a SmartPy binary.
if [ ! -f "$SMART_PY_CLI" ]; then
    echo "Fatal: Please install SmartPy CLI at $SMART_PY_CLI" && exit
fi

# Command ID
COMMAND_ID=$1
echo "Using command ID $COMMAND_ID"
echo ""

OUT_DIR="./$COMMAND_ID-out"
echo "Writing to $OUT_DIR"
echo ""

echo "Compiling..."
$SMART_PY_CLI compile-expression "./commands/$COMMAND_ID/command.py" "command" $OUT_DIR
echo "Done!"
echo ""

echo "Michelson lambda:"
cat "$COMMAND_ID-out/command_michelson.tz"
echo ""