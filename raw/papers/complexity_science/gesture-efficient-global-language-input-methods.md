---
title: "Gesture-efficient global language input methods"
authors: "Daniel Mailman"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-05T08:16:35.791533"
doi: ""
openalex_id: "https://openalex.org/W7225207003"
source_api: "openalex"
---

# Gesture-efficient global language input methods

**著者**: Daniel Mailman
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

A central task of computer hardware and software is text entry: sending units of human written language to applications such as word processors and spreadsheets. Input units range from individual lexons (Unicode characters) to lexemes (words and compounds). Standard QWERTY keyboards directly access a limited set of lexons and are used to assemble lexemes one lexon at a time. Non-QWERTY lexons and lexemes often require (e.g.) layout switching, dead-key composition, candidate lists, memorized codes, or relatively sophisticated software input methods (IMEs). This dissertation presents µLex, a framework for gesture-efficient IMEs. µLex IMEs are designed to coexist with application and operating system (OS) functionality, support immediate usability, and enable touch-typing over time. OS and application coexistence is largely via IME-only, supplemental gestural semantics associated with keyboard and mouse longpress, presses of keys or buttons for at least a specified duration. Five IME implementation case studies progress from direct lexon selection to branching lexon selection to orthographic lexeme selection to romanized lexeme selection. µTeclas maps QWERTY cues directly to Spanish letters and symbols, supporting keyboard selection with optional display guidance. µLetras adds a mouse-selectable display. µVietChu addresses Vietnamese text entry, where initial cues correspond to multiple targets; display-guided cue sequences resolve the ambiguity. The framework also accommodates input sets such as German, Esperanto, pan-European lexons, and the International Phonetic Alphabet (IPA). µWords and µ词语 (cíyǔ) ‘words’ extend the framework to English and Mandarin lexemes through display-guided selection. Browser prototypes are constructed from frequency lists and romanization data. English spellings and toneless pinyin provide QWERTY-accessible cues; other spelling and romanization systems provide equivalent cues for other languages. Lexeme frequencies guide access, with more frequent lexemes requiring fewer gestures. Across this progression, the dissertation relates cue/target mapping designs to gestural efficiency (GE), measured by gestemes per Unicode character (GPU) and gestemes per lexeme (GPL), with reciprocal Unicode characters per gesteme (UPG) and lexemes per gesteme (LPG). Cumulative corpus coverage (CCC) measures each evaluated inventory’s frequency-weighted coverage within successive gesture budgets. This research strongly indicates that well-engineered cueing systems can enable lexeme IMEs to achieve substantial gestural savings over lexon IMEs.
