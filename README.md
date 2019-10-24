# ipa-dict - Monolingual wordlists with pronunciation information in IPA

This project aims to provide a series of dictionaries consisting of wordlists with accompanying phonemic pronunciation information in International Phonetic Alphabet (IPA) transcription for as many words as possible in as many languages / dialects / variants as possible.

The dictionary data is available in a number of human- and machine-readable [formats](#formats), in order to make it as useful as possible for various other [applications](#applications).

* [Background](#background)
* [Formats](#formats)
  * [Raw data](#raw-data)
  * [JSON](#json)
  * [XML](#xml)
  * [CSV](#csv)
  * [Other formats](#other-formats)
* [Languages](#languages)
* [Applications](#applications)
* [Demo](#demo)
* [Notes](#notes)
* [Credits](#credits)
* [License](#license)

## Background

There is no existing central, standardized location for checking the correspondence between orthography and pronunciation in any given language.

Furthermore, IPA information even for large languages can be surprisingly difficult to find, and is generally not provided for each form of a word. In many languages, reference works only carry pronunciation notation for lemmas (headwords), and very little information is available on conjugations and forms of word classes other than the dictionary form. For highly inflected languages (e.g. French), each verb may have 40 or more conjugated forms, but pronunciation will only be listed for the dictionary form.

In fact, many languages do not have any significant amount of IPA information available at all, even in dictionaries, and this is even more likely to be the case for language variants and non-standard varieties.

This project aims to resolve these problems by compiling wordlists for each language along with accompanying IPA transcription.

A combination of manual and semi-automatic generation has been used to compile the pronunciations. Whenever possible, pronunciations have been checked manually by consulting multiple reference works, particularly for lemmas (which are usually more easily available). Inflected forms have been either added manually or with semi-automatic guidance when multiple pronunciations can be pre-determined with some certainty.

## Formats

For convenience, the IPA data is provided here in several different formats:

* tab delimited
* JSON
* CSV
* XML

All filenames refer to the [ISO language code](https://en.wikipedia.org/wiki/ISO_639-1) of the relevant language (e.g. `sw.json` is a JSON file containing pronunciations for Swahili.

### Raw data

The raw data in this repository is provided as a series of text files with each word and its corresponding pronunciation in IPA on a separate line delimited by tab characters. The tab delimited files are plain text UTF-8 encoded files with the filename suffix `.txt` in the following format:

    [ENTRY][TAB][IPA]

This file format is simple, lightweight, human- and machine-readable, and is also easily convertible to other common formats. Several of those formats (e.g. JSON, XML, CSV) are provided as downloads in the [Releases](https://github.com/open-dict-data/ipa-dict/releases) section.

### JSON

The JSON files are in the following format:

```json
{
    "LANG":
        [{
            "ENTRY1":"IPA1",
            "ENTRY2":"IPA2",
            "ENTRY3":"IPA3",
            "ENTRY4":"IPA4"
        }]
}
```

### XML

XML files have been generated for all the word lists in the following format:

```xml
    <IpaEntry EntryID="1">
      <Item>ENTRY</Item>
      <Ipa>/IPA/</Ipa>
    </IpaEntry>
```

### CSV

There are comma-separated files available for use with spreadsheet programs and so on. These are in some ways similar to the raw data files, with the exception that they are delimited by commas rather than tabs. In most spreadsheet programs, you should be able to open these directly from the file menu.

### Other formats

The [ipa-dict-dsl](https://github.com/open-dsl-dict/ipa-dict-dsl) project has converted all of the IPA data into DSL format dictionary files for use with dictionary software such as [ABBY Lingvo](https://www.lingvolive.com/en-us), [GoldenDict](http://goldendict.org/), or [gdcl](https://github.com/dohliam/gdcl). Pre-compiled and compressed dictionary files for individual languages can be downloaded from the project [releases page](https://github.com/open-dsl-dict/ipa-dict-dsl/releases).

There is also a _homonyms_ package containing all homonyms sorted by IPA reading for each language. Homonym lists are available for French, Japanese, Norwegian, Swedish, Cantonese, and Mandarin. The lists can be downloaded from the [releases section](https://github.com/open-dict-data/ipa-dict/releases/tag/1.0).

If there is another format not listed here that would be useful to you, please feel free to open an issue or PR to add it.

## Languages

IPA data is currently available for the following languages:

Language | Code
-------- | ----
ar | Arabic (Modern Standard)
de | German
en_UK | English (Received Pronunciation)
en_US | English (General American)
eo | Esperanto
es_ES | Spanish (Spain)
es_MX | Spanish (Mexico)
fa | Persian
fi | Finnish
fr_FR | French (France)
fr_QC | French (Québec)
is | Icelandic
ja | Japanese
jam | Jamaican Creole
km | Khmer
ko | Korean
ma | Malay (Malaysian and Indonesian)
nb | Norwegian Bokmål
or | Odia
ro | Romanian
sv | Swedish
sw | Swahili
tts | Isan
vi_C | Vietnamese (Central)
vi_N | Vietnamese (Northern)
vi_S | Vietnamese (Southern)
yue | Cantonese
zh | Mandarin

## Applications

This project provides an accessible source for IPA pronunciation information that other dictionary projects (e.g. Wiktionary) and electronic dictionaries can draw on rather than manually adding pronunciations for each entry.

An [updated collection of dictionaries](https://github.com/open-dsl-dict/ipa-dict-dsl) in ABBYY Lingvo DSL format is maintained by the [open-dsl-dict](https://github.com/open-dsl-dict) project for use in dictionary programs such as [Goldendict](https://github.com/goldendict/goldendict) and [gdcl](https://github.com/dohliam/gdcl):

![ipa](https://cloud.githubusercontent.com/assets/9295750/20906588/af21d25c-bafd-11e6-9832-0c70138142b7.gif)

You can download the binary dictionary files [here](https://github.com/open-dsl-dict/ipa-dict-dsl/releases).

The [IPA Lookup](https://open-dict-data.github.io/ipa-lookup/) project provides a web interface for searching the dictionaries in different languages:

![IPA Lookup screenshots](https://cloud.githubusercontent.com/assets/9295750/21977686/0aa0b7f2-db8c-11e6-88b8-cdec8305ef5e.gif)

Links to all the available languages can be found on the [project homepage](https://open-dict-data.github.io/ipa-lookup/).

Apart from the above, there are several other ways that this data could be (and has been) applied:

* Providing pronunciation information for a series of learner's grammars currently being compiled by the [Open Grammar Project](https://github.com/opengrammar/)
* Cross-language comparison of common phonemes
* Intra-language analysis of phoneme patterns
* Automatic generation of homonym lists (a selection of these is now available for download in the [releases section](https://github.com/open-dict-data/ipa-dict/releases/tag/1.0))
* Generating complete IPA transcriptions for stories in multiple languages as part of the [Storybooks Speech and Hearing](https://global-asp.github.io/storybooks-sah/) project

## Demo

You can search the data online on the [IPA Lookup](https://open-dict-data.github.io/ipa-lookup/) page for each language. The website makes use of the [JSON formatted data](#json).

## Notes

* Pronunciations provided are broadly phonemic, and should represent what one might expect to find in a dictionary or other popular reference work.
* Some familiarty with basic IPA is assumed, however since variation frequently exists among reference works, the transcriptions here try to maximize readability and usefulness for learners (rather than, say linguists, who might prefer to make finer distinctions).
* Pronunciation is provided where possible for each inflected form of a given lexeme, so _run_, _ran_, _runs_, and _running_ for example would each be separate entries.
* The emphasis is on the correspondence between orthography and phonemic pronunciation, so separate entries are given for homonyms that are written or spelled differently.
* Where multiple possible pronunciations exist for a given entry, they should all be listed (separated by commas), even if they have different senses. For example, the word _est_ has two different pronunciations in French (/ɛst/ and /ɛ/), depending on whether it is a noun or an (unrelated) verb, so the entry for _est_ lists both of these pronunciations.
* Conversely, words with different orthographies are considered separate entries, even if they have the same pronunciation. This is because the lists are primarily meant to provide possible pronunciations for unique spellings rather than dictionary information for the possible spellings of unique words.
* Mandarin Chinese data has been provided in two orthographic variants -- _Traditional_ (`_hant`) and _Simplified_ (`_hans`) for convenience. Apart from orthography, the pronunciation data in the two versions are always the same -- the codes indicate the specific written standard used rather than pronunciation differences in different regions.

## Credits

* [Aspell](http://aspell.net/) for reference wordlists
* [Folkets lexikon](https://folkets-lexikon.csc.kth.se/folkets/) for Swedish pronunciation data. ([CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/))
* [Edict](https://www.edrdg.org/jmdict/edict.html) for Japanese pronunciation data ([CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
* [_A Learner's Grammar of Jamaican_](https://github.com/opengrammar/jam-learners-grammar) from the [Open Grammar Project](https://github.com/opengrammar) for Jamaican Creole pronunciation data ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))
* [Unihan](https://www.unicode.org/charts/unihan.html) for Chinese character pronunciation data ([Unicode License](https://www.unicode.org/license.html))
* [KFCD Pinyin](https://github.com/kfcd/pinyin) for Mandarin IPA data ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/))
* [KFCD Pingyam](https://github.com/kfcd/pingyam) for Cantonese IPA data ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/))
* Multisyllabic pronunciation data for Cantonese from [開放粵語詞典](http://kaifangcidian.com/han/yue) ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/))
* Multisyllabic pronunciation data for Mandarin from [開放漢語詞典](http://kaifangcidian.com/han/han) ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/))
* [prosodic1b](https://github.com/jsfalk/prosodic1b) by @jsfalk for Finnish IPA data (Finnish wordlist from [The Institute for the Languages of Finland](http://kaino.kotus.fi/sanat/nykysuomi/)) ([GPL 2.0](https://github.com/jsfalk/prosodic1b/blob/master/LICENSE))
* English (US) IPA data based on modified version of [cmudict-ipa](https://github.com/lingz/cmudict-ipa) by @lingz, with addition of stress markers made possible by [syllabify](https://github.com/kylebgorman/syllabify) by @kylebgorman ([MIT](https://github.com/lingz/cmudict-ipa/blob/master/LICENSE))
* English (UK) IPA data derived from [ipacards](https://github.com/leoboiko/ipacards) by @leoboiko ([GPL 3.0](https://github.com/leoboiko/ipacards/blob/master/LICENSE))
* Experimental IPA for German has been generated using [germanipa](https://github.com/kdelaney/germanipa) by @kdelaney. Feedback and corrections appreciated!
* Experimental IPA for Spanish (`es_ES` and `es_MX`) has been generated using Timur Baytukalov's [spanish-pronunciation-rules](https://github.com/easypronunciation/spanish-pronunciation-rules-php) PHP script. Additions, corrections, and expansion of the dictionaries to other Spanish locales are welcome!
* Arabic IPA has been generated by Tim Buckwalter's [Arabic Morphological Analyzer](https://catalog.ldc.upenn.edu/LDC2004L02), with adjustments to allow for UTF-8 input and IPA output, with inspiration from the [arabic_tools](https://github.com/lingz/arabic_tools) project by @lingz.
* Persian vowelled texts are extremely difficult to find, possibly even more so than Arabic. The Persian IPA data here has been pieced together from [Wiktionary](https://fa.wiktionary.org/), the [PersPred](http://perspred.cnrs.fr/perspred-project) project, and a great deal of guesswork. It should be considered extremely experimental until more reliable sources become available.
* Odia IPA data provided by @psubhashish, based on [converted text](https://github.com/OdiaWikimedia/Converter/tree/master/IPA-Romanization) from Odia-language Wikimedia data dumps.
* Data for Québécois French has been generated using the [qc-ipa converter](https://github.com/dohliam/qc-ipa) and is _highly experimental_. It is provided here for demonstration purposes only. Improvements to the conversion process and additional data should be contributed directly to the [qc-ipa project](https://github.com/dohliam/qc-ipa) project and the results will be merged here.
* Vietnamese pronunciation data has been generated by @TasseDeCafe using [vPhon](https://github.com/kirbyj/vPhon) in combination  with [this wordlist](https://www.informatik.uni-leipzig.de/~duc/software/misc/wordlist.html) by Ho Ngoc Duc.
* Many thanks to Dr. Espen Stranger-Johannessen of the Inland Norway University of Applied Sciences for assistance with correcting and updating the Norwegian IPA data.
* Icelandic IPA is from the [Pronunciation Dictionary for Icelandic](http://malfong.is/?pg=framburdur&lang=en) by the [Hjal project](http://www.malfong.is/index.php?pg=hjal&lang=en), released under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/), with [some changes](https://github.com/egilll/icelandic-pronunciation-dataset).
* Khmer data extracted from the [Khmer-English Dictionary](https://www.aakanee.com/AC-Khmer/X/dict.html) at [aakanee.com](https://www.aakanee.com) ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/))
* Isan data extracted from the [Isaan-English Dictionary](https://www.aakanee.com/AC-Isaan/X/dict.html) at [aakanee.com](https://www.aakanee.com) ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/))
* Romanian data provided by [MaRePhoR](https://speech.utcluj.ro/marephor/) ([CC BY-NC](https://creativecommons.org/licenses/by-nc/3.0/))
* Korean data provided by [korean-word-ipa-dictionary](https://github.com/laviande22/korean-word-ipa-dictionary), extracted from Korean Wiktionary by @laviande22 ([CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/))

## License

All material in this repository released under the **MIT license** unless otherwise specified. Please note that third-party datasets retain their original licenses -- refer to the [Credits](#credits) section above for details.
