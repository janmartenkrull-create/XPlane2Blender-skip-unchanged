"""Skip writing OBJ files when export output matches the last successful export."""

import hashlib

from .xplane_helpers import ExportableRoot


def content_hash(obj_text: str) -> str:
    return hashlib.sha256(obj_text.encode("utf-8")).hexdigest()


def layer_props_for_exportable_root(exportable_root: ExportableRoot):
    return exportable_root.xplane.layer


def should_skip_unchanged_export(
    skip_enabled: bool,
    force_all: bool,
    stored_hash: str,
    obj_text: str,
) -> bool:
    if not skip_enabled or force_all:
        return False
    if not stored_hash:
        return False
    return content_hash(obj_text) == stored_hash


def remember_successful_export_hash(
    exportable_root: ExportableRoot, obj_text: str
) -> None:
    layer_props_for_exportable_root(exportable_root).last_export_content_hash = (
        content_hash(obj_text)
    )
