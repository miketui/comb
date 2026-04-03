#!/usr/bin/env bash
set -euo pipefail

# TAYLKOMB Local Export Runbook
# Run after activating your CAD environment
#
# For build123d:  pip install build123d
# For CadQuery:   conda install -c cadquery cadquery
# For OpenSCAD:   install from https://openscad.org

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="$SCRIPT_DIR/exports"
mkdir -p "$OUT_DIR/step" "$OUT_DIR/stl"

echo "=== TAYLKOMB Export Runbook ==="
echo "Output: $OUT_DIR"
echo ""

# --- build123d exports ---
echo "--- build123d scripts ---"
for script in \
    build123d/main_comb_master_tang.py \
    build123d/shared_receiver_core.py \
    build123d/button_detent_module.py \
    build123d/comb_family_corrected.py \
    build123d/handle_family_corrected.py; do
    if [ -f "$SCRIPT_DIR/$script" ]; then
        echo "Running: $script"
        cd "$SCRIPT_DIR/$(dirname $script)"
        python "$(basename $script)" || echo "  SKIPPED (build123d not available)"
        cd "$SCRIPT_DIR"
    fi
done

# --- CadQuery exports (alternative engine) ---
echo ""
echo "--- CadQuery scripts ---"
for script in \
    cadquery/main_comb_master_tang.py \
    cadquery/shared_receiver_core.py \
    cadquery/button_detent_module.py \
    cadquery/fit_coupon_male_tang.py \
    cadquery/fit_coupon_receiver_nominal.py \
    cadquery/fit_coupon_receiver_relief.py; do
    if [ -f "$SCRIPT_DIR/$script" ]; then
        echo "Running: $script"
        cd "$SCRIPT_DIR/$(dirname $script)"
        python "$(basename $script)" || echo "  SKIPPED (CadQuery not available)"
        cd "$SCRIPT_DIR"
    fi
done

# --- OpenSCAD visual exports ---
echo ""
echo "--- OpenSCAD visual exports ---"
for scad in "$SCRIPT_DIR"/openscad/*.scad; do
    name="$(basename "$scad" .scad)"
    echo "Rendering: $name"
    openscad -o "$OUT_DIR/stl/${name}.stl" "$scad" 2>/dev/null || echo "  SKIPPED (OpenSCAD not available)"
done

echo ""
echo "=== Export complete ==="
echo "Check $OUT_DIR for outputs"
