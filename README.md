# ipa-dict - Monolingual wordlists with pronunciation information in IPA

This project aims to provide a series of dictionaries consisting of wordlists with accompanying phonemic pronunciation information in International Phonetic Alphabet (IPA) transcription for as many words as possible in as many languages / dialects / variants as possible.

The dictionary data is available in a number of human- and machine-readable [formats](#formats), in order to make it as useful as possible for various other [applications](#applications).

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

All filenames refer to the [ISO language code](http://en.wikipedia.org/wiki/ISO_639-1) of the relevant language (e.g. `sw.json` is a JSON file containing pronunciations for Swahili.

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

There is also a concurrent project to convert the data into DSL format dictionary files for use with dictionary software such as ABBY Lingvo or Goldendict.

There is also a _homonyms_ package containing all homonyms sorted by IPA reading for each language. Homonym lists are available for French, Japanese, Norwegian, Swedish, Cantonese, and Mandarin. The lists can be downloaded from the [releases section](https://github.com/open-dict-data/ipa-dict/releases/tag/1.0).

If there is another format not listed here that would be useful to you, please feel free to open an issue or PR to add it.

## Languages

IPA data is currently available for the following languages:

Language | Code
-------- | ----
Cantonese | yue
English (General American) | en_US
Esperanto | eo
Finnish | fi
French | fr
German | de
Jamaican Creole | jam
Japanese | ja
Malay | ma
Mandarin | zh
Norwegian Bokmål | nb
Spanish (Mexico) | es_MX
Spanish (Spain) | es_ES
Swahili | sw
Swedish | sv

## Applications

This project provides an accessible source for IPA pronunciation information that other dictionary projects (e.g. Wiktionary) and electronic dictionaries can draw on rather than manually adding pronunciations for each entry.

Apart from this, there are several ways that this data could (and has been applied):

* Providing pronunciation information for a series of learner's grammars currently being compiled by the Open Grammar Project
* Cross-language comparison of common phonemes
* Intra-language analysis of phoneme patterns
* Automatic generation of homonym lists (a selection of these is now available for download in the [releases section](https://github.com/open-dict-data/ipa-dict/releases/tag/1.0))

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
* [Folkets lexikon](http://folkets-lexikon.csc.kth.se/folkets/) for Swedish pronunciation data
* [Edict](http://www.edrdg.org/jmdict/edict.html) for Japanese pronunciation data
* _A Learner's Grammar of Jamaican_ from the Open Grammar Project for Jamaican Creole pronunciation data
* [Unihan](http://www.unicode.org/charts/unihan.html) for Chinese character pronunciation data
* [KFCD Pinyin](https://github.com/kfcd/pinyin) for Mandarin IPA data
* [KFCD Pingyam](https://github.com/kfcd/pingyam) for Cantonese IPA data
* Multisyllabic pronunciation data for Cantonese from [開放粵語詞典](http://kaifangcidian.com/han/yue)
* Multisyllabic pronunciation data for Mandarin from [開放漢語詞典](http://kaifangcidian.com/han/han)
* [prosodic1b](https://github.com/jsfalk/prosodic1b) by @jsfalk for Finnish IPA data (Finnish wordlist from [The Institute for the Languages of Finland](http://kaino.kotus.fi/sanat/nykysuomi/))
* English (US) IPA data based on modified version of [cmudict-ipa](https://github.com/lingz/cmudict-ipa) by @lingz, with addition of stress markers made possible by [syllabify](https://github.com/kylebgorman/syllabify) by @kylebgorman
* Experimental IPA for German has been generated using [germanipa](https://github.com/kdelaney/germanipa) by @kdelaney. Feedback and corrections appreciated!
* Experimental IPA for Spanish (`es_ES` and `es_MX`) has been generated using Timur Baytukalov's [spanish-pronunciation-rules](https://github.com/easypronunciation/spanish-pronunciation-rules-php) PHP script. Additions, corrections, and expansion of the dictionaries to other Spanish locales are welcome!

## License

MIT.
