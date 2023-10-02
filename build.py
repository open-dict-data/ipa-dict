#!/usr/bin/env python3

import argparse
import os
import sys

def overwrite_maybe(filename, data):
    """Check that the contents of the file need to change and write new
       data if so. Do nothing otherwise.
    """

    try:
        with open(filename, "rb") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        if contents == data: return

    sys.stderr.write(f"writing {filename}\n")
    with open(f"{filename}.tmp", "wb") as f:
        f.write(data)

    os.rename(f"{filename}.tmp", filename)

language = {}
filename = "LANGUAGES.tsv"
with open(filename, "r") as f:
    lineno = 0
    for line in f.readlines():
        lineno += 1
        try:
            if line[-1:] == "\n": line = line[:-1]
            code, name, *rest = line.split("\t", 2)
            variant = ""
            if len(rest) == 0:
                pass
            elif len(rest) == 1:
                variant = rest[0]
            else:
                raise ValueError("can't parse LANGUAGES.tsv")
            language[code] = name, variant
        except:
            sys.stderr.write(f"while processing line {lineno} of {filename}\n")
            raise

def load_ipa(code):
    result = {}
    filename = os.path.join("data", f"{code}.txt")
    with open(filename, "r") as f:
        lineno = 0
        for line in f.readlines():
            lineno += 1
            try:
                if line[-1:] == "\n": line = line[:-1]
                word, transcription = line.split("\t")
                result[word] = transcription
            except:
                sys.stderr.write(f"while processing line {lineno} of {filename}\n")
                raise
    return result

def write_dsl(code, name, description, ipa):
    output  = f'#NAME "IPA Dictionary - {code}: {description}"\n'
    output += f'#INDEX_LANGUAGE "{name}"\n'
    output += f'#CONTENTS_LANGUAGE "{name}"\n\n'
    for word, transcription in ipa.items():
        output += f"{word}\n\t[m1]{transcription}[/m]\n\n"

    # write DSL files both in UTF8 and UTF16, because some software requires
    # them to be encoded in the latter
    for enc in ["utf8", "utf16"]:
        data = bytes(output, enc)
        os.makedirs(f"dsl_{enc}", exist_ok = True)
        overwrite_maybe(os.path.join(f"dsl_{enc}", f"{code}_ipa.dsl"), data)

parser = argparse.ArgumentParser(prog="build", description="build stuff from data files", add_help = True)
targets = parser.add_argument_group(title="targets", description="build targets, at least one must be specified (default: all)")
targets.add_argument("--dsl", dest="cmds", action="append_const", const="dsl", help="build DSL dictionaries")
parser.add_argument("codes", metavar="CODE", nargs="*", type=str, help="language codes to process (default: all)")

args = parser.parse_args(sys.argv[1:])

if args.cmds is not None and len(args.cmds) > 0:
    cmds = args.cmds
else:
    cmds = ["dsl"]

if len(args.codes) > 0:
    codes = args.codes
else:
    codes = language.keys()

for code in codes:
    ipa = load_ipa(code)
    name, variant = language[code]
    description = name
    if variant:
        description += f" ({variant})"

    for cmd in cmds:
        if cmd == "dsl":
            write_dsl(code, name, description, ipa)
        else:
            raise NotImplementedError(cmd)
