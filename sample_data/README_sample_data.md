# Sample data

Small hand-made folders (empty placeholder files) for trying the checker.
Select any folder in the app and compare against the expected result.

| complete_sequence | shot010_comp.1001-1006.exr | No missing frames |

| missing_frame | shot010_comp.1001-1006.tga without 1003 | Missing: 1003 |

| mixed_files | two .exr frames (1001, 1003) plus notes.txt and preview.pdf | comp missing 1002; non-image files ignored |

| multiple_sequences | shot010_beauty (1001, 1002, 1004) and shot010_depth (1001-1003) | beauty missing 1003; depth complete |

| single_frame | shot010_comp.1001.exr | Single frame, nothing missing |
