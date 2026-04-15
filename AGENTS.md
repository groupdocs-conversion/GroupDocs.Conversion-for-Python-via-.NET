<!-- generator:skip -->
# GroupDocs.Conversion for Python via .NET -- AGENTS.md

> Instructions for AI agents working with this package.

Convert between 10,000+ document format pairs -- DOCX, PDF, XLSX, PPTX, images, CAD, email, and more.

## Install

```bash
pip install groupdocs-conversion-net
```

**Python**: 3.5 - 3.14 | **Platforms**: Windows, Linux, macOS

## Resources

| Resource | URL |
|---|---|
| Documentation | https://docs.groupdocs.com/conversion/python-net/ |
| LLM-optimized docs | https://docs.groupdocs.com/conversion/python-net/llms-full.txt |
| API reference | https://reference.groupdocs.com/conversion/python-net/ |
| Code examples | https://docs.groupdocs.com/conversion/python-net/developer-guide/ |
| Release notes | https://releases.groupdocs.com/conversion/python-net/release-notes/ |
| PyPI | https://pypi.org/project/groupdocs-conversion-net/ |
| Free support forum | https://forum.groupdocs.com/c/conversion/ |
| Temporary license | https://purchase.groupdocs.com/temporary-license |

## MCP Server

If your environment has MCP configured, you can connect your AI tool to the GroupDocs documentation server for on-demand API lookups:

```json
{
  "mcpServers": {
    "groupdocs-docs": {
      "url": "https://docs.groupdocs.com/mcp"
    }
  }
}
```

Works with Claude Code (`~/.claude/settings.json`), Cursor (`.cursor/mcp.json`), VS Code Copilot (`.vscode/mcp.json`), and any MCP-compatible client. If MCP is unavailable, fall back to the LLM-optimized docs URL above and this file — both are shipped inside the wheel.

## Imports

```python
from groupdocs.conversion import License, Converter, ConverterSettings, ConversionByPageFailedException
from groupdocs.conversion.caching import FileCache, MemoryCache
from groupdocs.conversion.contracts import DocumentInfo, AudioDocumentInfo, ValueObject, BitmapInfo, Bzip2DocumentInfo
from groupdocs.conversion.filetypes import (
    FileType, AudioFileType, CadFileType, CompressionFileType, DatabaseFileType,
    EBookFileType, EmailFileType, FontFileType, ImageFileType, NoteFileType,
    PageDescriptionLanguageFileType, PdfFileType, PresentationFileType,
    ProjectManagementFileType, SpreadsheetFileType, ThreeDFileType,
    WebFileType, WordProcessingFileType,
)
from groupdocs.conversion.logging import ConsoleLogger           # FileLogger was removed in 26.3.0
from groupdocs.conversion.options import PageMarginOptions, PageSize, PageSizeOptions
from groupdocs.conversion.options.load import WordProcessingLoadOptions, SpreadsheetLoadOptions
from groupdocs.conversion.options.convert import (
    PdfConvertOptions, ImageConvertOptions, WordProcessingConvertOptions,
    Rotation, ImageFlipModes, WatermarkTextOptions,
)
```

## Quick Start

```python
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

with Converter("input.docx") as converter:
    converter.convert("output.pdf", PdfConvertOptions())
```

## Convert with Options

```python
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions
from groupdocs.conversion.options.load import WordProcessingLoadOptions

load_options = WordProcessingLoadOptions()
load_options.password = "secret"

with Converter("protected.docx", load_options) as converter:
    options = PdfConvertOptions()
    options.dpi = 300
    options.page_number = 1
    options.pages_count = 2
    converter.convert("output.pdf", options)
```

**Converter constructor.** `Converter(source, load_options=None, settings=None)` accepts all three positional **or** as kwargs. Prefer kwargs when you only need `settings`:

```python
from groupdocs.conversion import Converter, ConverterSettings
from groupdocs.conversion.logging import ConsoleLogger

settings = ConverterSettings()
settings.logger = ConsoleLogger()

with Converter("input.docx", settings=settings) as converter:   # no None placeholder
    converter.convert("output.pdf", PdfConvertOptions())
```

## Get Document Info

```python
from groupdocs.conversion import Converter

with Converter("document.pdf") as converter:
    info = converter.get_document_info()
    print(f"Pages: {info.pages_count}, Format: {info.format}")
```

## Convert from Stream

```python
import io
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

with open("input.docx", "rb") as stream:
    with Converter(stream) as converter:
        converter.convert("output.pdf", PdfConvertOptions())
```

## Per-page, stream, and callback conversions

In addition to `convert(target_path, options)`, `Converter` exposes four fast-path methods (available in 26.3.0+):

```python
# 1. One output file per page, written to a directory as page_1.<ext>, page_2.<ext>, ...
from groupdocs.conversion.options.convert import ImageConvertOptions
with Converter("input.docx") as c:
    c.convert_by_page("out_dir", ImageConvertOptions())
```

```python
# 2. Convert to an in-memory bytes payload (no disk write)
from groupdocs.conversion.options.convert import PdfConvertOptions
with Converter("input.docx") as c:
    payload: bytes = c.convert_to_stream(PdfConvertOptions())
```

```python
# 3. Per-document callback — fires once per completed document.
# ctx: dict with source_file, source_format, target_format, hierarchy_level, item_index
def on_done(ctx):
    print("done:", ctx["source_file"], "->", ctx["target_format"])
with Converter("archive.zip") as c:
    c.convert_with_callback(PdfConvertOptions(), on_done)
```

```python
# 4. Per-page callback — fires once per converted page.
# ctx: dict with source_file, source_format, target_format, page
def on_page(ctx):
    print("page", ctx["page"], "done")
with Converter("input.docx") as c:
    c.convert_with_callback_per_page(ImageConvertOptions(), on_page)
```

**Not supported** (older C# examples may try these — they won't work through the Python binding):

- Returning a .NET `Stream` from a Python callback (the `Func<SavePageContext, Stream>` per-page stream sink used in the C# `ConvertToImage` examples). Use `convert_by_page(out_dir, ...)` or `convert_to_stream(...)` instead.
- Writing your own per-entry `Stream` factory for archives or multi-message emails. Use `convert_with_callback` and let the library place outputs.

## Licensing

```python
from groupdocs.conversion import License

# From file
License().set_license("path/to/license.lic")

# From stream
with open("license.lic", "rb") as f:
    License().set_license(f)
```

Or auto-apply: `export GROUPDOCS_LIC_PATH="path/to/license.lic"`

**Evaluation vs licensed.** Without a license the library still runs, but PDF output carries an evaluation watermark stamp and non-PDF targets show an equivalent evaluation mark; there is also a page/document count cap. Set `GROUPDOCS_LIC_PATH` (or call `License().set_license(...)`) and re-run to clear both. A 30-day full license is free: https://purchase.groupdocs.com/temporary-license

## API Reference

### Converter

| Method | Returns | Description |
|---|---|---|
| `__init__(source, load_options=None, settings=None)` | | Positional or kwargs; `source` is path, bytes, or stream |
| `convert(target, convert_options)` | `None` | Single output file or stream |
| `convert_by_page(output_dir, convert_options)` | `None` | Writes `page_N.<ext>` per page |
| `convert_to_stream(convert_options)` | `bytes` | In-memory output |
| `convert_with_callback(convert_options, callback)` | `None` | Fires `callback(ctx)` once per completed document |
| `convert_with_callback_per_page(convert_options, callback)` | `None` | Fires `callback(ctx)` once per converted page |
| `get_document_info()` | `IDocumentInfo` |  |
| `is_document_password_protected()` | `bool` |  |
| `get_possible_conversions()` | `PossibleConversions` | instance |
| `get_all_possible_conversions()` | `list` | classmethod |

### PdfConvertOptions

| Property | Type | Writable |
|---|---|---|
| `dpi` | `int` | yes |
| `password` | `str` | yes |
| `pdf_options` | `PdfOptions` | yes |
| `rotate` | `Rotation` | yes |
| `fallback_page_size` | `PageSize` | yes |
| `margin_settings` | `PageMarginOptions` | yes |
| `size_settings` | `PageSizeOptions` | yes |
| `orientation_settings` | `PageOrientation` | yes |
| `resize_mode` | `PageResizeMode` | yes |
| `embed_full_fonts` | `bool` | yes |

### WordProcessingLoadOptions

| Property | Type | Writable |
|---|---|---|
| `format` | `WordProcessingFileType` | yes |
| `font_name_substitution_enabled` | `bool` | yes |
| `font_config_substitution_enabled` | `bool` | yes |
| `font_info_substitution_enabled` | `bool` | yes |
| `default_font` | `str` | yes |
| `font_substitutes` | `list` | yes |
| `font_transformations` | `list` | yes |
| `embed_true_type_fonts` | `bool` | yes |
| `update_page_layout` | `bool` | yes |
| `update_fields` | `bool` | yes |
| `keep_date_field_original_value` | `bool` | yes |
| `password` | `str` | yes |
| `hide_word_tracked_changes` | `bool` | yes |
| `bookmark_options` | `WordProcessingBookmarksOptions` | yes |
| `preserve_form_fields` | `bool` | yes |
| `use_text_shaper` | `bool` | yes |
| `skip_external_resources` | `bool` | yes |
| `whitelisted_resources` | `list` | yes |
| `preserve_document_structure` | `bool` | yes |
| `page_numbering` | `bool` | yes |
| `hyphenation_options` | `HyphenationOptions` | yes |
| `convert_owner` | `bool` | yes |
| `convert_owned` | `bool` | yes |
| `depth` | `int` | yes |
| `clear_built_in_document_properties` | `bool` | yes |
| `clear_custom_document_properties` | `bool` | yes |
| `comment_display_mode` | `WordProcessingCommentDisplay` | yes |
| `show_full_commenter_name` | `bool` | yes |
| `margin_settings` | `PageMarginOptions` | yes |
| `size_settings` | `PageSizeOptions` | yes |

### SpreadsheetLoadOptions

| Property | Type | Writable |
|---|---|---|
| `sheets` | `list` | yes |
| `sheet_indexes` | `list` | yes |
| `format` | `SpreadsheetFileType` | yes |
| `default_font` | `str` | yes |
| `font_substitutes` | `list` | yes |
| `show_grid_lines` | `bool` | yes |
| `show_hidden_sheets` | `bool` | yes |
| `skip_headers` | `bool` | yes |
| `skip_footers` | `bool` | yes |
| `one_page_per_sheet` | `bool` | yes |
| `optimize_pdf_size` | `bool` | yes |
| `convert_range` | `str` | yes |
| `skip_empty_rows_and_columns` | `bool` | yes |
| `password` | `str` | yes |
| `check_excel_restriction` | `bool` | yes |
| `culture_info` | `CultureInfo` | yes |
| `all_columns_in_one_page_per_sheet` | `bool` | yes |
| `auto_fit_rows` | `bool` | yes |
| `columns_per_page` | `int` | yes |
| `rows_per_page` | `int` | yes |
| `convert_owner` | `bool` | yes |
| `convert_owned` | `bool` | yes |
| `depth` | `int` | yes |
| `clear_built_in_document_properties` | `bool` | yes |
| `clear_custom_document_properties` | `bool` | yes |
| `ignore_formula_calculation_errors` | `bool` | yes |
| `preserve_document_structure` | `bool` | yes |
| `print_comments` | `SpreadsheetPrintComments` | yes |
| `reset_font_folders` | `bool` | yes |
| `skip_external_resources` | `bool` | yes |
| `whitelisted_resources` | `list` | yes |
| `margin_settings` | `PageMarginOptions` | yes |
| `size_settings` | `PageSizeOptions` | yes |

## FileType enums

Each file-type class exposes only the members shown below. `Json` lives on `WebFileType`, not `SpreadsheetFileType` — this is the most common mistake when translating C# examples.

| Class | Members |
|---|---|
| `WordProcessingFileType` | `Doc, Docm, Docx, Dot, Dotm, Dotx, Rtf, Odt, Ott, Txt, Md, FlatOpc` |
| `SpreadsheetFileType` | `Xls, Xlsx, Xlsm, Xlsb, Ods, Ots, Xltx, Xlt, Xltm, Tsv, Xlam, Csv, Fods, Dif, Sxc, Numbers, FlatOpc` |
| `PresentationFileType` | `Ppt, Pps, Pptx, Ppsx, Odp, Otp, Potx, Pot, Potm, Pptm, Ppsm, Fodp` |
| `ImageFileType` | `Jpg, Jpeg, Png, Gif, Bmp, Tiff, Tif, Psd, Webp, Ico, Emf, Wmf, Heic, Avif, Dcm, Dng, Jp2, Ai, Tga, Psb, Jfif, ...` |
| `WebFileType` | `Html, Htm, Mht, Mhtml, Xml, Json, Chm` |
| `PageDescriptionLanguageFileType` | `Svg, Svgz, Eps, Cgm, Xps, Tex, Ps, Pcl, Oxps` |
| `PdfFileType` | `Pdf` |
| `EmailFileType` | `Msg, Eml, Emlx, Vcf, Mbox, Pst, Ost, Olm, Ics` |
| `EBookFileType` | `Epub, Mobi, Azw3` |
| `CadFileType` | `Dxf, Dwg, Dgn, Dwf, Stl, Ifc, Plt, Igs, Dwt, Dwfx, Cf2` |

Use `FileType.from_extension("json")` when you don't know which subclass owns a format — it returns the correct concrete instance.

## Key Patterns

- **Properties**: use `snake_case` -- auto-mapped to .NET `PascalCase`
- **Context managers**: `with Converter(...) as x:` ensures resources are released
- **Streams**: pass `open("file", "rb")` or `io.BytesIO(data)` where .NET expects Stream
- **Stream write-back**: `BytesIO` objects are updated after .NET writes to them
- **Enums**: case-insensitive, lazy-loaded (e.g., `FileType.DOCX`)
- **Collections**: `for item in result` and `len(result)` work on .NET collections
- **Callbacks**: Python functions work for the per-document and per-page variants exposed as `convert_with_callback` and `convert_with_callback_per_page` (see above). Returning a .NET `Stream` from a Python callback is **not** supported — use `convert_by_page(dir, ...)` or `convert_to_stream(...)` instead.

## Platform Requirements

| Platform | Requirements |
|---|---|
| Windows | None |
| Linux | `apt install libgdiplus libfontconfig1 ttf-mscorefonts-installer` |
| macOS | `brew install mono-libgdiplus` |

## Troubleshooting

**`"Saving the entire document is only supported when converting to TIFF format"`** -- raised by `convert("out.jpg", ImageConvertOptions())` and similar raster targets. Use the per-page fast path instead:

```python
with Converter("input.docx") as c:
    c.convert_by_page("out_dir", ImageConvertOptions())   # writes out_dir/page_1.jpg, ...
```

**`ConversionNotSupportedException`** -- the source/target format pair is rejected by the underlying engine (e.g. `jls -> pdf`, `mpp -> html`). Probe before converting:

```python
from groupdocs.conversion import Converter

# classmethod: list every supported pair known to the engine
for pair in Converter.get_all_possible_conversions():
    print(pair.source_format, "->", [t.format for t in pair.all_conversions])

# instance method: only the pairs available for the open document
with Converter("input.vss") as c:
    print(c.get_possible_conversions().all)
```

**`System.Drawing.Common is not supported`** -- install libgdiplus: `sudo apt install libgdiplus` (Linux) / `brew install mono-libgdiplus` (macOS)

**`Gdip` type initializer exception** -- outdated libgdiplus: `brew reinstall mono-libgdiplus` (macOS)

**Garbled text / missing fonts** -- install fonts: `sudo apt install ttf-mscorefonts-installer fontconfig && sudo fc-cache -f`

**`DllNotFoundException: libSkiaSharp`** -- stale system copy conflicts with bundled version. Rename it: `sudo mv /usr/local/lib/libSkiaSharp.dylib /usr/local/lib/libSkiaSharp.dylib.bak`

**`DOTNET_SYSTEM_GLOBALIZATION_INVARIANT` errors** -- do NOT set this. Install ICU: `sudo apt install libicu-dev`

**`TypeLoadException`** -- reinstall: `pip install --force-reinstall groupdocs-conversion-net`

**Still stuck?** Post your question at https://forum.groupdocs.com/c/conversion/ -- the development team responds directly.
