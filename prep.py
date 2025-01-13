#!/usr/bin/env python3
import argparse

PLATFORMS = {
    'hana': 'RPi4 (aarch64 Cortex-A72)',
    'octopus': 'Intel Celeron',
    'rammus': 'Intel 8th and 9th',
    'hatch': 'Intel 10th gen',
    'volteer': 'Intel 11th gen and up',
    'zork': 'AMD',
}

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
    parser.add_argument('-s', '--show', help='Show platform and language choices', action='store_true')
    parser.add_argument('-p', '--platform', help='Show download links for specified platform', choices=PLATFORMS.keys())
    parser.add_argument('-l', '--language', help='Show download links for specified language', choices=set(LEGACY_LANGUAGES+CONCH_LANGUAGES))
    args = parser.parse_args()

    if args.show:
        print('Available platforms:')
        for p,d in PLATFORMS.items():
            print(f'* {p}: ({d})')
        print('Available languages:')
        print(f'* {set(LEGACY_LANGUAGES+CONCH_LANGUAGES)}')
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

def model_url(platform, release, language):
    if language in CONCH_LANGUAGES:
        return f'{URL}{platform}-release/R{release}/dlc-scaled/libsoda-model-{language}-cnch24d3/package/dlc.img'
    elif language in LEGACY_LANGUAGES:
        return f'{URL}{platform}-release/R{release}/dlc-scaled/libsoda-model-{language}-df24d2/package/dlc.img'
    else:
        return None

if __name__ == '__main__':
    main()
