#!/usr/bin/env python3
import os
import glob
import argparse
import subprocess
import hashlib

PLATFORMS = {
    'hana': 'RPi4 (aarch64 Cortex-A72)',
    'octopus': 'Intel Celeron',
    'rammus': 'Intel 8th and 9th',
    'hatch': 'Intel 10th gen',
    'volteer': 'Intel 11th gen and up',
    'zork': 'AMD',
}

LIB_HASHES = { # ['orig', 'fixed']
    'hana': ['', ''],
    'octopus': ['', ''],
    'rammus': ['', ''],
    'hatch': ['de216faa85674e514949311a612514c9df6fcdb1', '6924eec1d937626d4377423e346fad3ad373f88d'],
    'volteer': ['', ''],
    'zork': ['a455e9b02df576433f9ba13d50638375f8c5ea19', '83536ca8490e5c4e21f07e91d29fc4101b46718e'],
}

LEGACY_VERSION = 'df24d2'
LEGACY_LANGUAGES = [
    'en-us',
    'ja-jp',
    'de-de',
    'fr-fr',
    'it-it',
    'en-ca',
    'en-au',
    'en-gb',
    'en-ie',
    'en-sg',
    'fr-be',
    'fr-ch',
    'en-in',
    'it-ch',
    'de-at',
    'de-be',
    'de-ch',
    'es-us',
    'es-us',
    'fr-ca',
    'hi-in',
    'id-id',
    'ko-kr',
    'pl-pl',
    'th-th',
    'tr-tr',
    'zh-tw',
    'zh-cn',
    'pt-br',
    'ru-ru',
    'vi-vn',
]

CONCH_VERSION = 'cnch24d3'
CONCH_LANGUAGES = [
    'da-dk',
    'de-at',
    'de-be',
    'de-ch',
    'de-de',
    'en-au',
    'en-ca',
    'en-gb',
    'en-ie',
    'en-in',
    'en-sg',
    'en-us',
    'es-es',
    'es-us',
    'fr-be',
    'fr-ca',
    'fr-Ch',
    'fr-fr',
    'hi-in',
    'it-it',
    'ja-jp',
    'ko-kr',
    'nb-no',
    'nl-nl',
    'sv-se',
    ]

URL = 'https://edgedl.me.gvt1.com/edgedl/dlc/'
LATEST = '133-16151.2.0'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--available', help='Show all available platforms and languages', action='store_true')
    parser.add_argument('-c', '--check', help='Check if everything is ready to run', action='store_true')
    parser.add_argument('-s', '--setup', help='Download and setup everything', action='store_true')
    parser.add_argument('-p', '--platform', help='Platform to download/check the library for', choices=PLATFORMS.keys())
    parser.add_argument('-l', '--language', help='ASR model language', choices=set(LEGACY_LANGUAGES+CONCH_LANGUAGES))
    args = parser.parse_args()

    if args.available:
        print('Available platforms:')
        for p,d in PLATFORMS.items():
            print(f'* {p}: ({d})')
        print('Available languages:')
        print(f'* {set(LEGACY_LANGUAGES+CONCH_LANGUAGES)}')
    elif args.check:
        check(args.platform, LATEST, args.language)
    elif args.setup:
        setup(args.platform, LATEST, args.language)
    elif args.platform and args.language:
        print(library_url(args.platform, LATEST))
        print(model_url(args.platform, LATEST, args.language))
    else:
        parser.print_help()

def library_url(platform, release):
    if platform in PLATFORMS.keys():
        return f'{URL}{platform}-release/R{release}/dlc/libsoda/package/dlc.img'
    else:
        return None

def library_name_base(platform, release):
    if platform in PLATFORMS.keys():
        return f'libsoda_{platform}_R{release[:3]}'
    else:
        return None

def model_url(platform, release, language):
    res = None
    if language in CONCH_LANGUAGES:
        res = f'{URL}{platform}-release/R{release}/dlc-scaled/libsoda-model-{language}-{CONCH_VERSION}/package/dlc.img'
    elif language in LEGACY_LANGUAGES:
        res = f'{URL}{platform}-release/R{release}/dlc-scaled/libsoda-model-{language}-{LEGACY_VERSION}/package/dlc.img'
    return res

def model_name_full(language):
    res = None
    if language in CONCH_LANGUAGES:
        res = f'SODAModels_{language}_{CONCH_VERSION}'
    elif language in LEGACY_LANGUAGES:
        res = f'SODAModels_{language}_{LEGACY_VERSION}'
    return res

def download(url, outname):
    import requests
    with open(outname, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length'))
        bar_length = 50 # char length of progress bar
    
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            received = 0
            for data in response.iter_content(chunk_size=4096):
                received += len(data)
                f.write(data)
                progress = int((received / total_length) *bar_length)
                print(f'{outname} ({total_length // 1024 // 1024}M): [{'='*progress}{' '*(bar_length-progress)}]', end='\r')
        print()

def extract_library(lib_base):
    with open(f'{lib_base}.so', 'wb') as f:
        subprocess.run(['7z', 'e', f'{lib_base}.img', '-so', 'root/libsoda.so'], stdout=f)

def extract_model(model_name):
    subprocess.run(['7z', 'x', f'{model_name}.img', 'root'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['mv', 'root', model_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def bitflip(platform, lib_base):
    hex_orig = ''
    hex_fix = ''
    if platform == 'hana':
        print(f'RPi4 fix just needs a single bit flip, will be implemented soon')
    elif platform in ['hatch', 'zork']:
        hex_orig = '4c8dbdc8feffff31f68843704c89ffe8'
        hex_fix  = '4c8dbdc8feffffc64370ff904c89ffe8'

    if hex_orig and hex_fix:
        with open(f'{lib_base}_fixed.so', 'wb') as outf:
            with open(f'{lib_base}.so', 'rb') as inf:
                while True:
                    data = inf.read(4096)
                    if not data:
                        break
                    dhex = data.hex()
                    if hex_orig in dhex:
                        print(f'Found bug, fixing')
                        data = bytes.fromhex(dhex.replace(hex_orig, hex_fix))
                    outf.write(data)
    else:
        print(f'Fixing library on platform {platform} is not implemented yet, please have a look at https://github.com/biemster/gasr/issues/24')
        return

def has_library(platform, lib_base):
    has_img = False
    has_lib = False
    is_fixed = False
    has_symlink = False
    if os.path.exists(f'{lib_base}.img'):
        has_img = True
    if os.path.exists(f'{lib_base}.so'):
        h = get_hash(f'{lib_base}.so')
        h_fix = get_hash(f'{lib_base}_fixed.so')
        if h == LIB_HASHES[platform][0]:
            has_lib = True
        if h_fix == LIB_HASHES[platform][1]:
            is_fixed = True
        if os.path.islink('libsoda.so') and get_hash('libsoda.so') == h_fix:
            has_symlink = True

    return has_img,has_lib,is_fixed,has_symlink

def has_model(model_name):
    has_img = False
    has_dir = False
    has_symlink = False
    if os.path.exists(f'{model_name}.img'):
        has_img = True
    if os.path.isdir(model_name):
        has_dir = True
    if os.path.islink('SODAModels') and os.path.exists('SODAModels/metadata') and os.path.exists(f'{model_name}/metadata') and get_hash('SODAModels/metadata') == get_hash(f'{model_name}/metadata'):
        has_symlink = True
    return has_img,has_dir,has_symlink

def has_linker():
    has_linker = False
    is_fixed = False
    linker = glob.glob('ld-linux*')
    if len(linker):
        has_linker = True
        linker_strings = subprocess.check_output(['strings', linker[0]]).decode().split('\n')
        if 'xibc.so.' in linker_strings:
            is_fixed = True
    return has_linker, is_fixed

def check(platform, release, language):
    if platform:
        lib_base = library_name_base(platform, release)
        lib_ready = has_library(platform, lib_base)
        print(f'Library has .img: ..................... {lib_ready[0]}')
        print(f'Library has .so: ...................... {lib_ready[1]}')
        print(f'Library .so is fixed: ................. {lib_ready[2]}')
        print(f'Library .so is symlinked: ............. {lib_ready[3]}')
    if language:
        model_name = model_name_full(language)
        model_ready = has_model(model_name)
        print(f'Language has .img: .................... {model_ready[0]}')
        print(f'Language .img is extracted to dir:..... {model_ready[1]}')
        print(f'Language dir is symlinked: ............ {model_ready[2]}')
    linker_ready = has_linker()
    print(f'Dynamic linker ld-linux is copied here: {linker_ready[0]}')
    print(f'Dynamic linker ld-linux is fixed: ..... {linker_ready[1]}')

def get_hash(fname):
    sha1 = hashlib.sha1()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def setup_library(platform, release):
    lib_base = library_name_base(platform, release)
    lib_ready = has_library(platform, lib_base)
    if not lib_ready[0]:
        download(library_url(platform, release), f'{lib_base}.img')
    if not lib_ready[1]:
        extract_library(lib_base)
    if not lib_ready[2]:
        bitflip(platform, lib_base)
    if not lib_ready[3]:
        if os.path.islink('libsoda.so'):
            subprocess.run(['rm', 'libsoda.so'])
        subprocess.run(['ln', '-s', f'{lib_base}_fixed.so', 'libsoda.so'])

def setup_model(platform, release, language):
    model_name = model_name_full(language)
    model_ready = has_model(model_name)
    if not model_ready[0]:
        download(model_url(platform, release, language), f'{model_name}.img')
    if not model_ready[1]:
        extract_model(model_name)
    if not model_ready[2]:
        if os.path.islink('SODAModels'):
            subprocess.run(['rm', 'SODAModels'])
        subprocess.run(['ln', '-s', model_name, 'SODAModels'])

def setup_linker():
    linker_orig = None
    linker_fixed = 'ld-linux.so'
    ldd_env = subprocess.check_output(['ldd', '/usr/bin/env']).decode().replace('\t','').split('\n')
    for l in ldd_env:
        if 'ld-linux' in l:
            l_split = l.split(' => ')
            if 'ld-linux' in l_split[0]:
                linker_orig = l_split[0]
                break
    if linker_orig:
        print(f'Found linker {linker_orig}, copying it here and disabling "DT_RELR without GLIBC_ABI_DT_RELR" warning')
        with open(linker_fixed, 'wb') as outf:
            with open(linker_orig, 'rb') as inf:
                while True:
                    data = inf.read(4096)
                    if not data:
                        break
                    dhex = data.hex()
                    if 'libc.so.\0'.encode().hex() in dhex:
                        print(f'Found "libc.so.", replacing with "xibc.so."')
                        data = bytes.fromhex(dhex.replace('libc.so.\0'.encode().hex(), 'xibc.so.\0'.encode().hex()))
                    outf.write(data)
        subprocess.run(['chmod', '744', linker_fixed])
    else:
        print(f'Linker ld-linux not found! This is an error, please report it')

def setup(platform, release, language):
    if platform:
        lib_base = library_name_base(platform, release)
        lib_ready = has_library(platform, lib_base)
        if not all(lib_ready):
            setup_library(platform, release)
        else:
            print(f'Platform {platform} already fully set up.')
    if language:
        model_name = model_name_full(language)
        model_ready = has_model(model_name)
        if not all(model_ready):
            setup_model(platform if platform else PLATFORMS.keys()[0], release, language)
        else:
            print(f'Language {language} already fully set up.')
    linker_ready = has_linker()
    if not linker_ready[0] or not linker_ready[1]:
        print('Dynamic linker not setup yet, doing that now')
        setup_linker()

if __name__ == '__main__':
    main()
